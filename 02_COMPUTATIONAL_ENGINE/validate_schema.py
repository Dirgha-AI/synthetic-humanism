"""
Recursive JSON Schema Validator for Ahimsa Impact Assessment (AIA v1.1)

Validates all top-level and nested properties, required keys, enum constraints,
numeric bounds (minimum/maximum), array item schemas, and additionalProperties
restrictions without requiring external packages.
"""

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = BASE_DIR / "schema" / "ahimsa-schema.json"


def _check_type(val, expected_type: str) -> bool:
    if expected_type == "object":
        return isinstance(val, dict)
    if expected_type == "array":
        return isinstance(val, list)
    if expected_type == "string":
        return isinstance(val, str)
    if expected_type == "boolean":
        return isinstance(val, bool)
    if expected_type == "integer":
        return isinstance(val, int) and not isinstance(val, bool)
    if expected_type == "number":
        return isinstance(val, (int, float)) and not isinstance(val, bool)
    return True


def validate_node(instance, schema_node: dict, path: str):
    expected_type = schema_node.get("type")
    if expected_type and not _check_type(instance, expected_type):
        raise ValueError(f"{path}: expected type '{expected_type}', got {type(instance).__name__} ({instance!r})")

    if "enum" in schema_node:
        if instance not in schema_node["enum"]:
            raise ValueError(f"{path}: value {instance!r} not in allowed enum {schema_node['enum']}")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema_node and instance < schema_node["minimum"]:
            raise ValueError(f"{path}: value {instance} < minimum {schema_node['minimum']}")
        if "maximum" in schema_node and instance > schema_node["maximum"]:
            raise ValueError(f"{path}: value {instance} > maximum {schema_node['maximum']}")

    if isinstance(instance, dict):
        req = set(schema_node.get("required", []))
        missing = req - set(instance.keys())
        if missing:
            raise ValueError(f"{path}: missing required properties {sorted(missing)}")

        props = schema_node.get("properties", {})
        if schema_node.get("additionalProperties") is False and props:
            extra = set(instance.keys()) - set(props.keys())
            if extra:
                raise ValueError(f"{path}: unexpected additional properties {sorted(extra)}")

        # Ensure red_line_check includes all 5 conceptual red lines (via v1.1 or v1.0 alias)
        if path.endswith(".red_line_check"):
            has_strat = (
                "demographic_or_hereditary_stratification" in instance
                or "algorithmic_caste_scoring" in instance
            )
            has_transfer = (
                "unsanctioned_kinetic_or_coercive_transfer" in instance
                or "atrocity_regime_export" in instance
            )
            if not has_strat:
                raise ValueError(
                    f"{path}: must specify 'demographic_or_hereditary_stratification' (or 'algorithmic_caste_scoring')"
                )
            if not has_transfer:
                raise ValueError(
                    f"{path}: must specify 'unsanctioned_kinetic_or_coercive_transfer' (or 'atrocity_regime_export')"
                )

        for k, v in instance.items():
            if k in props:
                validate_node(v, props[k], f"{path}.{k}")

    elif isinstance(instance, list) and "items" in schema_node:
        item_schema = schema_node["items"]
        for idx, elem in enumerate(instance):
            validate_node(elem, item_schema, f"{path}[{idx}]")


def main():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = json.load(f)

    with open(BASE_DIR / "scorer" / "example_project.json", "r", encoding="utf-8") as f:
        validate_node(json.load(f), schema, "example_project.json")

    with open(BASE_DIR / "scorer" / "example_refused.json", "r", encoding="utf-8") as f:
        validate_node(json.load(f), schema, "example_refused.json")

    count = 0
    with open(BASE_DIR / "benchmark" / "benchmark_50.jsonl", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if line.strip():
                count += 1
                validate_node(json.loads(line), schema, f"benchmark_50.jsonl[row {i+1}]")

    print(
        f"Recursive JSON Schema v1.1 validation passed: example_project.json, "
        f"example_refused.json, and all {count} benchmark systems verified!"
    )


if __name__ == "__main__":
    sys.exit(main())
