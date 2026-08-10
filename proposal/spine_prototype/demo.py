"""Illustrative end-to-end run of the Dispatch Spine prototype.

Simulates one work item moving through intake, validation, classification,
and routing. Where a cognitive function would be invoked in the real
system, this demo prints a placeholder instead of calling a model — no
model call, no external action, no real data.

Run with: python3 demo.py
"""

from event_log import EventLog
from routing import route
from state_registry import Classification, StateRegistry, Status, WorkItem
from validation import validate


def main() -> None:
    registry = StateRegistry()
    log = EventLog()

    item = WorkItem(
        id="wi-001",
        item_type="opportunity",
        payload={"title": "Sample lane opportunity", "source": "demo", "deadline": "2026-09-01"},
    )
    registry.create(item)
    log.record(item.id, "intake", actor="spine", detail=f"WorkItem {item.id} received")

    result = validate(item)
    if result.passed:
        item.set_status(Status.VALIDATED)
        log.record(item.id, "validated", actor="spine", detail="All required fields present")
    else:
        item.set_status(Status.AWAITING_MIKE)
        log.record(
            item.id,
            "validation_failed",
            actor="spine",
            detail=f"Missing fields: {result.missing_fields}",
        )
        print_events(log, item.id)
        return

    item.classification = Classification.REVIEW_NEEDED
    item.priority = 3
    log.record(
        item.id,
        "classified",
        actor="spine",
        detail=f"Classification={item.classification.value} priority={item.priority}",
    )

    decision = route(item)
    item.set_status(Status.ROUTED)
    item.owner_function = decision.destination_function
    log.record(
        item.id,
        "routed",
        actor="spine",
        detail=f"destination={decision.destination_function} requires_cognition={decision.requires_cognition}",
    )

    if decision.requires_cognition:
        # Illustrative placeholder only — no model is called here.
        log.record(
            item.id,
            "cognitive_function_placeholder",
            actor=decision.destination_function,
            detail="[would produce a structured card/draft/recommendation here]",
        )

    log.record(
        item.id,
        "portal_card_placeholder",
        actor="spine",
        detail="[would create a Level-2 Review card for Mike via Portal here]",
    )

    print_events(log, item.id)


def print_events(log: EventLog, item_id: str) -> None:
    print(f"Event log for {item_id}:")
    for event in log.for_item(item_id):
        print(f"  {event.seq:02d} [{event.actor}] {event.event_type}: {event.detail}")


if __name__ == "__main__":
    main()
