"""Illustrative Validation Layer component of the Dispatch Spine prototype.

Pure deterministic field checking. Never makes a judgment call.
"""

from dataclasses import dataclass

from state_registry import WorkItem


@dataclass
class ValidationResult:
    passed: bool
    missing_fields: list[str]


# Required-field schemas keyed by work item type. Illustrative only.
REQUIRED_FIELDS: dict[str, list[str]] = {
    "opportunity": ["title", "source", "deadline"],
    "packet_request": ["requirement", "requested_by"],
}


def validate(item: WorkItem) -> ValidationResult:
    required = REQUIRED_FIELDS.get(item.item_type, [])
    missing = [field for field in required if not item.payload.get(field)]
    return ValidationResult(passed=not missing, missing_fields=missing)
