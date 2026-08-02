# Occurrence search for `Accipitriformes` excludes published `Tachyspiza` records

## Summary

An occurrence search for `Accipitriformes` in the GBIF iNaturalist dataset
returns 36,493 Australian records for 2020-2025. A separate query for
`Tachyspiza` returns another 4,144 records from the same dataset, country, and
years.

The `Tachyspiza` records are published and individually accessible, but their
GBIF interpretation has no `order` value. They are therefore absent from the
`Accipitriformes` parent-taxon result.

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

The two result sets contain no duplicate GBIF occurrence keys.

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

**Expected:** There is a documented API method to retrieve the complete source
group or to detect source taxa detached from their expected parent hierarchy.

**Observed:** The normal parent-taxon query silently excludes these published
records. Adding the separate genus query recovered 4,142 of 4,149 aligned
iNaturalist observations that appeared absent from Query A.

## Question

Is this exclusion intended behaviour? If so, what API method should users use
to discover and retrieve records assigned to taxa that are detached from their
expected parent hierarchy?

Detailed evidence and a standard-library reproduction script:

https://github.com/coolinker/gbif-evidence-reports/tree/main/reports/tachyspiza-parent-query
