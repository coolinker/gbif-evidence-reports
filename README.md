# GBIF Evidence Reports

Independent, reproducible reports about GBIF API, taxonomy interpretation, and
data-selection behaviour.

This repository is not affiliated with GBIF. Confirmed issues should be
submitted to the official
[`gbif/portal-feedback`](https://github.com/gbif/portal-feedback) repository.
The purpose of this repository is to keep the supporting evidence, methods, and
small reproduction tools publicly accessible.

## Reports

| Report | Status |
|---|---|
| [`Tachyspiza` records omitted from an `Accipitriformes` parent query](reports/tachyspiza-parent-query/) | Draft for submission |

## Reproduce the current GBIF result

The reproduction script uses only the Python standard library:

```bash
python3 scripts/check_tachyspiza_query.py
```

It retrieves the current counts for the two GBIF occurrence queries and checks
three public example records.

## Reporting principles

- Separate observed API behaviour from taxonomic opinion.
- Include clickable queries, stable identifiers, and retrieval dates.
- State expected and observed behaviour explicitly.
- Use a minimal example before presenting aggregate measurements.
- Record negative tests and limitations to avoid overgeneralization.
- Keep the external issue concise and link to detailed evidence here.

## License

The documentation and code in this repository are released under the MIT
License.
