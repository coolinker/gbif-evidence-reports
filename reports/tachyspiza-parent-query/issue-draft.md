# Occurrence search for `Accipitriformes` excludes published `Tachyspiza` records

## Summary

An occurrence search for `Accipitriformes` in the GBIF iNaturalist dataset
returns 36,493 Australian records for 2020-2025. A separate query for
`Tachyspiza` returns 4,144 records from the same dataset, country, and years.
The two result sets contain no duplicate GBIF occurrence keys.

An order is broader than a genus. If `Tachyspiza` were retained beneath
`Accipitriformes` in the hierarchy used by the occurrence filter, Query B's
records would normally be a subset of Query A's records. The issue is not
whether Query A or Query B has the larger count; it is that the 4,144 Query B
records have zero overlap with Query A.

This was measured by retrieving all `36,493` Query A occurrence keys and all
`4,144` Query B occurrence keys, then calculating their set intersection by
GBIF occurrence key. The intersection contained `0` keys. The three examples
below illustrate why; they are not the basis of the aggregate overlap claim.

The source observations identify `Tachyspiza` species within
`Accipitriformes`. In GBIF, the affected occurrences are interpreted only as
the doubtful genus `Tachyspiza` (taxon key `4852732`), have no `order` value,
and carry `TAXON_ID_NOT_FOUND`. They are published and individually
accessible, but are absent from the `Accipitriformes` parent-taxon result.

This report concerns occurrence-query behaviour and hierarchy placement. It
does not ask GBIF to choose between competing taxonomies.

## Reproduction

**Query A — `Accipitriformes`, taxon key `7191147`:**

https://api.gbif.org/v1/occurrence/search?country=AU&taxon_key=7191147&year=2020%2C2025&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=0

Observed on 2026-08-03:

```text
36,493 records
```

**Query B — `Tachyspiza`, taxon key `4852732`:**

https://api.gbif.org/v1/occurrence/search?country=AU&taxon_key=4852732&year=2020%2C2025&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=0

Observed on 2026-08-03:

```text
4,144 records
```

## Single-record proof

The following two searches are identical except for `taxon_key`. Both are
restricted to iNaturalist observation `379649975`, published by GBIF as
occurrence `6441464971`.

**The record is found with the `Tachyspiza` genus key `4852732`:**

https://api.gbif.org/v1/occurrence/search?occurrence_id=https%3A%2F%2Fwww.inaturalist.org%2Fobservations%2F379649975&taxon_key=4852732&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=1

```json
{
  "count": 1,
  "key": 6441464971,
  "taxonKey": 4852732,
  "scientificName": "Tachyspiza Kaup, 1844",
  "order": null
}
```

**The same record is not found with the `Accipitriformes` order key
`7191147`:**

https://api.gbif.org/v1/occurrence/search?occurrence_id=https%3A%2F%2Fwww.inaturalist.org%2Fobservations%2F379649975&taxon_key=7191147&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=1

```json
{
  "count": 0,
  "results": []
}
```

Occurrence-search parameters are combined with `AND`, so this directly shows
that GBIF includes the occurrence beneath the genus filter but not beneath the
expected order filter.

## Minimal examples

The occurrence pages display the publisher's `taxonID`. For this dataset,
those are iNaturalist species identifiers. They are different from GBIF's
interpreted `taxonKey`, which is the identifier used by the occurrence API's
`taxon_key` filter.

| GBIF occurrence | Source `taxonID` | Source scientific name | Source order | GBIF `taxonKey` | GBIF interpreted name | GBIF order |
|---|---:|---|---|---:|---|---|
| [6441464971](https://www.gbif.org/occurrence/6441464971) | `1582863` | `Tachyspiza cirrocephala` | `Accipitriformes` | `4852732` | `Tachyspiza` | absent |
| [5938571149](https://www.gbif.org/occurrence/5938571149) | `1583256` | `Tachyspiza fasciata` | `Accipitriformes` | `4852732` | `Tachyspiza` | absent |
| [4946532804](https://www.gbif.org/occurrence/4946532804) | `1583020` | `Tachyspiza novaehollandiae` | `Accipitriformes` | `4852732` | `Tachyspiza` | absent |

This is how the examples relate to the two queries:

- Query A uses GBIF taxon key `7191147` for `Accipitriformes`.
- The verbatim source records state `order=Accipitriformes`.
- GBIF interprets all three records as taxon key `4852732`, the doubtful genus
  `Tachyspiza`; this is Query B.
- GBIF taxon key `4852732` has `Aves` as its direct parent and has no
  `Accipitriformes` order in its hierarchy.
- Parent filtering therefore does not treat these records as descendants of
  Query A's taxon key.

The source and interpreted representations can be compared directly through
the occurrence API:

- https://api.gbif.org/v1/occurrence/6441464971
- https://api.gbif.org/v1/occurrence/6441464971/verbatim

## Expected and observed behaviour

**Expected:** A user querying a parent taxon can either retrieve these
published source-group records or use a documented API signal or method to
discover taxa detached from that parent hierarchy.

**Observed:** Query A neither returns nor indicates the existence of the 4,144
Query B records. Adding the separate genus query recovered 4,142 of 4,149
aligned iNaturalist observations that appeared absent from Query A.

## Question

Is this the intended semantic behaviour of `taxon_key` parent filtering? If
so, is there an existing API method or recommended reproducible strategy for
discovering and retrieving records assigned to taxa that are detached from
their expected parent hierarchy?

Detailed evidence and a standard-library reproduction script:

https://github.com/coolinker/gbif-evidence-reports/tree/main/reports/tachyspiza-parent-query
