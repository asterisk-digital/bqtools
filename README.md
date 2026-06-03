# bqtools

BigQuery utility helpers — schema generation from Python dicts, table creation, latest-row queries, and schema-drift detection.

## Setup

To set up the python environment you need `uv`, then run:
```(bash)
uv sync
```

## Usage

```python
from google.cloud import bigquery
from bqtools import make_bq_table, get_latest_bq_rows, check_schema_drift

client = bigquery.Client()
make_bq_table(client, "project.dataset.table", {"id": 1, "name": "x"})
```

## Checks

These checks should always pass before pushing.

### Testing

```(bash)
uv run tox
```

### Linting

```(bash)
uv run ruff check .
```

### Formatting

```(bash)
uv run ruff format --check .
```
