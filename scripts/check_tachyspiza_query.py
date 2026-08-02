#!/usr/bin/env python3
"""Reproduce the current GBIF Tachyspiza parent-query evidence."""

from __future__ import annotations

import json
import sys
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_ROOT = "https://api.gbif.org/v1"
DATASET_KEY = "50c9509d-22c7-4a22-a47d-8c48425ef4a7"
PARENT_TAXON_KEY = 7191147
DETACHED_TAXON_KEY = 4852732
EXAMPLE_KEYS = (6441464971, 5938571149, 4946532804)
SCIENTIFIC_NAME_TERM = "http://rs.tdwg.org/dwc/terms/scientificName"
ORDER_TERM = "http://rs.tdwg.org/dwc/terms/order"
TAXON_ID_TERM = "http://rs.tdwg.org/dwc/terms/taxonID"


def get_json(url: str) -> dict[str, Any]:
    for attempt in range(4):
        request = Request(url, headers={"User-Agent": "gbif-evidence-reports/1.0"})
        try:
            with urlopen(request, timeout=60) as response:
                return json.load(response)
        except HTTPError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == 3:
                raise
        except URLError:
            if attempt == 3:
                raise
        time.sleep(2**attempt)
    raise RuntimeError("Unreachable retry state")


def occurrence_query(taxon_key: int) -> tuple[str, dict[str, Any]]:
    parameters = {
        "country": "AU",
        "taxon_key": taxon_key,
        "year": "2020,2025",
        "dataset_key": DATASET_KEY,
        "limit": 0,
    }
    url = f"{API_ROOT}/occurrence/search?{urlencode(parameters)}"
    return url, get_json(url)


def check_example(key: int) -> dict[str, Any]:
    record = get_json(f"{API_ROOT}/occurrence/{key}")
    verbatim = get_json(f"{API_ROOT}/occurrence/{key}/verbatim")
    checks = {
        "dataset_matches": record.get("datasetKey") == DATASET_KEY,
        "source_order_is_accipitriformes": verbatim.get(ORDER_TERM)
        == "Accipitriformes",
        "taxon_matches": record.get("taxonKey") == DETACHED_TAXON_KEY,
        "order_is_missing": not record.get("order"),
        "taxon_id_not_found": "TAXON_ID_NOT_FOUND" in record.get("issues", []),
    }
    return {
        "key": key,
        "occurrenceID": record.get("occurrenceID"),
        "source": {
            "taxonID": verbatim.get(TAXON_ID_TERM),
            "scientificName": verbatim.get(SCIENTIFIC_NAME_TERM),
            "order": verbatim.get(ORDER_TERM),
        },
        "gbif_interpretation": {
            "taxonKey": record.get("taxonKey"),
            "scientificName": record.get("scientificName"),
            "order": record.get("order"),
            "issues": record.get("issues", []),
        },
        "checks": checks,
    }


def main() -> int:
    parent_url, parent_result = occurrence_query(PARENT_TAXON_KEY)
    detached_url, detached_result = occurrence_query(DETACHED_TAXON_KEY)
    examples = [check_example(key) for key in EXAMPLE_KEYS]

    output = {
        "queries": {
            "parent": {
                "url": parent_url,
                "count": parent_result.get("count"),
            },
            "detached_genus": {
                "url": detached_url,
                "count": detached_result.get("count"),
            },
        },
        "examples": examples,
    }
    print(json.dumps(output, indent=2, sort_keys=True))

    checks = [
        value
        for example in examples
        for value in example["checks"].values()
    ]
    if not all(checks):
        print("One or more example records no longer match the report.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
