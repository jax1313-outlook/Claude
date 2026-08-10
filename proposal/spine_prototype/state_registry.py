"""Illustrative State Registry component of the Dispatch Spine prototype.

In-memory only. Not connected to any real storage or production data.
"""

from dataclasses import dataclass, field
from enum import Enum


class Classification(str, Enum):
    ROUTINE = "Routine"
    STATUS = "Status"
    REVIEW_NEEDED = "Review Needed"
    DECISION_NEEDED = "Decision Needed"
    CONFLICT = "Conflict"
    AUTHORITY = "Authority"
    ARCHIVE = "Archive"
    LIBRARY_CANDIDATE = "Library Candidate"
    NOISE = "Noise"


class Status(str, Enum):
    INTAKE = "intake"
    VALIDATED = "validated"
    ROUTED = "routed"
    IN_PROGRESS = "in_progress"
    AWAITING_MIKE = "awaiting_mike"
    RESOLVED = "resolved"


@dataclass
class WorkItem:
    id: str
    item_type: str
    payload: dict = field(default_factory=dict)
    status: Status = Status.INTAKE
    classification: Classification | None = None
    priority: int | None = None
    owner_function: str | None = None

    def set_status(self, status: Status) -> None:
        self.status = status


class StateRegistry:
    """Tracks WorkItem status. Deterministic. No reasoning happens here."""

    def __init__(self) -> None:
        self._items: dict[str, WorkItem] = {}

    def create(self, item: WorkItem) -> WorkItem:
        self._items[item.id] = item
        return item

    def get(self, item_id: str) -> WorkItem:
        return self._items[item_id]

    def all(self) -> list[WorkItem]:
        return list(self._items.values())
