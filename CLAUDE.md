# CLAUDE.md

bqtools is a Python library of BigQuery utility helpers (schema generation from Python dicts, table creation, latest-row queries, schema-drift detection). It is imported as a dependency by other projects.

## Quality gates

Major changes must not break tests, linting, or formatting. Verify with:

```bash
uv run tox          # tests
uv run ruff check . # linting
uv run ruff format . --check # formatting
```
