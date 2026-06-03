# bqtools

BigQuery utility helpers — schema generation from Python dicts, table creation, latest-row queries, and schema-drift detection.

## Installing

Add to your project's `pyproject.toml` dependencies:

```
"bqtools @ git+https://github.com/asterisk-digital/bqtools.git@main"
```

The library can be used as follows:

```(python)
from google.cloud import bigquery
import bqtools

client = bigquery.Client()
bqtools.make_bq_table(client, "project.dataset.table", {"id": 1, "name": "x"})
```

## Development setup

```(bash)
uv sync
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
