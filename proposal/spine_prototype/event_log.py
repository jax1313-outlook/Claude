"""Illustrative Event Log / Audit Trail component of the Dispatch Spine prototype.

Append-only. In memory. Every entry is meant to make "why did Dispatch do X"
answerable without reconstructing a chat transcript.
"""

from dataclasses import dataclass, field


@dataclass
class Event:
    work_item_id: str
    event_type: str
    actor: str
    detail: str
    seq: int = field(default=0)


class EventLog:
    def __init__(self) -> None:
        self._events: list[Event] = []

    def record(self, work_item_id: str, event_type: str, actor: str, detail: str) -> Event:
        event = Event(
            work_item_id=work_item_id,
            event_type=event_type,
            actor=actor,
            detail=detail,
            seq=len(self._events) + 1,
        )
        self._events.append(event)
        return event

    def for_item(self, work_item_id: str) -> list[Event]:
        return [e for e in self._events if e.work_item_id == work_item_id]

    def all(self) -> list[Event]:
        return list(self._events)
