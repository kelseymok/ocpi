import decimal
import json
from dataclasses import asdict

from jsonschema.validators import Draft4Validator
import os


def remove_nones(data):
    if isinstance(data, dict):
        return {k: remove_nones(v) for k, v in data.items() if v is not None}

    elif isinstance(data, list):
        return [remove_nones(v) for v in data if v is not None]

    return data


def validator(instance, version="v2.2.1"):
    cleaned_version = version.replace(".", "")
    path = os.path.join(
        os.path.dirname(__file__),
        "..", "..", "..",
        "src", "ocpi", cleaned_version, "schemas", f"{instance.__class__.__name__}.json")

    with open(path, 'r', encoding='utf-8-sig') as f:
        schema = f.read()
        v = Draft4Validator(json.loads(schema, parse_float=decimal.Decimal))
        result_dict = asdict(instance)
        result_cleaned = remove_nones(result_dict)
        v.validate(result_cleaned)


