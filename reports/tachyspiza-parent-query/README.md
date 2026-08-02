# `Tachyspiza` parent-query omission

## Finding

Published iNaturalist records assigned by GBIF to the doubtful genus
`Tachyspiza` are not returned by an occurrence query for the expected parent
order `Accipitriformes`.

The report concerns API selection behaviour and hierarchy placement. It does
not claim that either taxonomy is biologically correct.

## Current status

- First audit: 2026-07-31 to 2026-08-01
- Live query rechecked: 2026-08-03
- External GBIF issue: not yet submitted

## Contents

- [`issue-draft.md`](issue-draft.md): concise draft for `gbif/portal-feedback`
- [`evidence.md`](evidence.md): methods, aggregate measurements, and limitations
- [`example-records.csv`](example-records.csv): three public record examples
- [`../../scripts/check_tachyspiza_query.py`](../../scripts/check_tachyspiza_query.py):
  live API reproduction
