# Occurrence search for `Accipitriformes` excludes published `Tachyspiza` records

## Summary

Published iNaturalist occurrences interpreted by GBIF as `Tachyspiza` are not
returned by an `Accipitriformes` parent-taxon query, although their source
records place them in that order.

## Minimal reproduction

Example: GBIF occurrence
[`6441464971`](https://www.gbif.org/occurrence/6441464971).
Its [verbatim record](https://api.gbif.org/v1/occurrence/6441464971/verbatim)
contains:

```text
scientificName = Tachyspiza cirrocephala
order = Accipitriformes
```

The occurrence is returned when filtered by GBIF's `Tachyspiza` key
`4852732`:

https://api.gbif.org/v1/occurrence/search?occurrence_id=https%3A%2F%2Fwww.inaturalist.org%2Fobservations%2F379649975&taxon_key=4852732&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=1

```json
{"count": 1}
```

The same occurrence is not returned when filtered by GBIF's
`Accipitriformes` key `7191147`:

https://api.gbif.org/v1/occurrence/search?occurrence_id=https%3A%2F%2Fwww.inaturalist.org%2Fobservations%2F379649975&taxon_key=7191147&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=1

```json
{"count": 0}
```

## Control

For GBIF occurrence
[`5006702322`](https://www.gbif.org/occurrence/5006702322), interpreted as
`Aquila audax audax`, the equivalent filters work as expected:

- [`Aquila` genus key `2480498`](https://api.gbif.org/v1/occurrence/search?occurrence_id=https%3A%2F%2Fwww.inaturalist.org%2Fobservations%2F257351571&taxon_key=2480498&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=1):
  `count: 1`
- [`Accipitriformes` order key `7191147`](https://api.gbif.org/v1/occurrence/search?occurrence_id=https%3A%2F%2Fwww.inaturalist.org%2Fobservations%2F257351571&taxon_key=7191147&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=1):
  `count: 1`

## Scope

Using the same dataset, country, and year filters:

- [`Accipitriformes`](https://api.gbif.org/v1/occurrence/search?country=AU&taxon_key=7191147&year=2020%2C2025&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=0):
  `36,493` records.
- [`Tachyspiza`](https://api.gbif.org/v1/occurrence/search?country=AU&taxon_key=4852732&year=2020%2C2025&dataset_key=50c9509d-22c7-4a22-a47d-8c48425ef4a7&limit=0):
  `4,144` records.
- Intersection by GBIF occurrence key: `0`.

Queries were checked on 2026-08-03.

## Question

Is this intended behaviour for `taxon_key` parent filtering? If so, what API
method should users use to discover records assigned to taxa that are detached
from their expected parent hierarchy?

Supporting evidence and reproduction script:

https://github.com/coolinker/gbif-evidence-reports/tree/main/reports/tachyspiza-parent-query
