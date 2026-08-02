# Evidence

## Scope

| Field | Value |
|---|---|
| GBIF dataset | iNaturalist Research-grade Observations |
| Dataset key | `50c9509d-22c7-4a22-a47d-8c48425ef4a7` |
| Country | Australia |
| Observation years | 2020-2025 |
| Parent taxon | `Accipitriformes`, GBIF key `7191147` |
| Detached taxon | `Tachyspiza`, GBIF key `4852732` |
| API | GBIF occurrence API v1 |
| Audit period | 2026-07-31 to 2026-08-01 |
| Live recheck | 2026-08-03 |

## Aggregate reconciliation

The original GBIF parent query and a separate `Tachyspiza` query were
deduplicated by GBIF occurrence key. iNaturalist observation IDs embedded in
GBIF `occurrenceID` values were then reconciled against an aligned source
snapshot.

| Measure | Parent query only | Parent plus detached genus |
|---|---:|---:|
| GBIF records | 36,493 | 40,637 |
| Aligned iNaturalist observations | 40,611 | 40,611 |
| Matched source observation IDs | 36,462 | 40,604 |
| Unmatched source observation IDs | 4,149 | 7 |
| Unmatched rate | 10.216% | 0.017% |

The additional query recovered 4,142 of 4,149 previously unmatched source
observations, or 99.83%.

No duplicate GBIF occurrence keys were found between the parent and detached
genus query results.

## Negative benchmark

Six preselected taxonomy-boundary candidates and three controls were evaluated
across Amphibia, Aves, and Reptilia. All 33,913 published benchmark records
were returned by their expected parent query.

This negative result limits the claim: ordinary synonymy, fuzzy matching, or
higher-rank matching did not generally produce parent-filter omission. The
validated distinguishing condition in this case is missing expected hierarchy
placement.

## Candidate warning signal

A bounded detector warned when:

1. the expected parent name was absent from the GBIF record hierarchy; and
2. the record carried `TAXON_ID_NOT_FOUND` or used a doubtful taxon.

It warned for all 4,144 `Tachyspiza` records and none of the 33,913 locked
benchmark records. This is not a generally validated classifier because the
positive set contains only one taxonomic group.

`TAXON_ID_NOT_FOUND` alone was not discriminating: it also appeared in all
benchmark negatives. Missing expected parent hierarchy was the useful signal.

## Limitations

- The positive mechanism is one taxonomic group in one constituent dataset.
- The audit is limited to Australia and observation years 2020-2025.
- Counts can change when GBIF reprocesses records or updates its taxonomy.
- The result measures query selection, not biological taxonomy correctness.
- Seven aligned source observations were not found in the selected GBIF
  dataset.
- Thirty-three GBIF records were not present in the aligned source snapshot,
  potentially because of timing or eligibility differences.
