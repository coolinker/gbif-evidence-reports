# Occurrence search for `Accipitriformes` excludes published `Tachyspiza` records

## Summary

An occurrence search for `Accipitriformes` in the GBIF iNaturalist dataset
returns 36,493 Australian records for 2020-2025. A separate query for
`Tachyspiza` returns 4,144 records from the same dataset, country, and years.
The two result sets contain no duplicate GBIF occurrence keys.

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

## Minimal examples

- https://www.gbif.org/occurrence/6441464971
- https://www.gbif.org/occurrence/5938571149
- https://www.gbif.org/occurrence/4946532804

Each example:

- belongs to the selected iNaturalist dataset;
- has GBIF taxon key `4852732`;
- has no `order` value;
- carries `TAXON_ID_NOT_FOUND`;
- remains directly accessible through GBIF.

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
