"""Illustrative Routing Table component of the Dispatch Spine prototype.

Deterministic decisions only: does this work item need a cognitive
function, and if so which one? The Spine decides the *path*; it never
performs the reasoning itself.
"""

from dataclasses import dataclass

from state_registry import Classification, WorkItem


@dataclass
class RoutingDecision:
    destination_function: str
    requires_cognition: bool


# Fixed routing rules keyed by (item_type, classification). Illustrative only.
ROUTING_TABLE: dict[tuple[str, Classification], RoutingDecision] = {
    ("opportunity", Classification.REVIEW_NEEDED): RoutingDecision(
        destination_function="intelligence_analysis", requires_cognition=True
    ),
    ("opportunity", Classification.NOISE): RoutingDecision(
        destination_function="archive", requires_cognition=False
    ),
    ("packet_request", Classification.DECISION_NEEDED): RoutingDecision(
        destination_function="publisher_drafting", requires_cognition=True
    ),
}

DEFAULT_ROUTE = RoutingDecision(destination_function="manager_reasoning", requires_cognition=True)


def route(item: WorkItem) -> RoutingDecision:
    if item.classification is None:
        raise ValueError("Work item must be classified before routing.")
    key = (item.item_type, item.classification)
    return ROUTING_TABLE.get(key, DEFAULT_ROUTE)
