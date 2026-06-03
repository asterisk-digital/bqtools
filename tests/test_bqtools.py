from bqtools import pydict_to_bqschema, pydict_to_bqschema_recursive, python_type_to_bq_type


def test_python_type_to_bq_type_scalars():
    assert python_type_to_bq_type(True) == "BOOLEAN"
    assert python_type_to_bq_type(1) == "INT64"
    assert python_type_to_bq_type(1.5) == "FLOAT64"
    assert python_type_to_bq_type("x") == "STRING"
    assert python_type_to_bq_type(None) == "STRING"


def test_pydict_to_bqschema_recursive_flat():
    schema = pydict_to_bqschema_recursive({"id": 1, "name": "x", "active": True})

    by_name = {f.name: f for f in schema}
    assert by_name["id"].field_type == "INT64"
    assert by_name["name"].field_type == "STRING"
    assert by_name["active"].field_type == "BOOLEAN"
    assert all(f.mode == "NULLABLE" for f in schema)


def test_pydict_to_bqschema_recursive_nested_and_repeated():
    schema = pydict_to_bqschema_recursive(
        {
            "owner": {"name": "x", "age": 30},
            "tags": ["a", "b"],
            "children": [{"id": 1}],
            "empty": [],
        }
    )

    by_name = {f.name: f for f in schema}

    assert by_name["owner"].field_type == "RECORD"
    assert by_name["owner"].mode == "NULLABLE"
    assert {f.name for f in by_name["owner"].fields} == {"name", "age"}

    assert by_name["tags"].field_type == "STRING"
    assert by_name["tags"].mode == "REPEATED"

    assert by_name["children"].field_type == "RECORD"
    assert by_name["children"].mode == "REPEATED"
    assert {f.name for f in by_name["children"].fields} == {"id"}

    assert by_name["empty"].field_type == "STRING"
    assert by_name["empty"].mode == "REPEATED"


def test_pydict_to_bqschema_appends_sync_timestamp():
    schema = pydict_to_bqschema({"id": 1})

    last = schema[-1]
    assert last.name == "AsteriskSyncDate"
    assert last.field_type == "TIMESTAMP"
    assert last.mode == "REQUIRED"


def test_pydict_to_bqschema_custom_sync_column():
    schema = pydict_to_bqschema({"id": 1}, sync_timestamp_column="ingested_at")

    assert schema[-1].name == "ingested_at"
