# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`bqtools` is a Python library of BigQuery utility helpers. Uses a src-layout with the main package at `src/bqtools/`.

It is a library (not an application) — no `main` entrypoint, no `App` class. Consumers import functions like `make_bq_table`, `get_latest_bq_rows`, and `check_schema_drift` directly from the `bqtools` package.

## Commands

```bash
# Setup (requires uv)
uv sync

# Linting
ruff check .

# Formatting
ruff format .

# Run all tests
tox

# Run a single test
pytest tests/test_bqtools.py::test_pydict_to_bqschema_appends_sync_timestamp
```

## Architecture

- **bqtools.py**: All public helpers live here. Re-exported from `bqtools/__init__.py`.
  - Schema generation from Python dicts: `python_type_to_bq_type`, `pydict_to_bqschema_recursive`, `pydict_to_bqschema`.
  - Table operations: `does_bq_table_exist`, `make_bq_table`.
  - Querying: `get_latest_bq_rows` returns the most recent row per PK based on the sync-timestamp column.
  - Schema drift: `check_schema_drift` compares an incoming dataset's fields against the live BQ schema and raises `SchemaDriftError` with `ALTER TABLE` statements when new fields are detected.

## Conventions

- The sync timestamp column defaults to `AsteriskSyncDate` and is created with `DEFAULT CURRENT_TIMESTAMP()`.
- All scalar/record fields are `NULLABLE`; lists become `REPEATED`.
