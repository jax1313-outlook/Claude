# DISPATCH_BUILD_PROPOSAL.md

**Program:** Dispatch
**Document Type:** Proposed Implementation Plan (companion to `DISPATCH_PROGRAM_MAP.md`)
**Status:** Proposal / Planning Draft — NOT an approved controlling document, NOT a build authorization
**Owner:** Mike Zachary / Level 1 Transport
**Authority:** Mike Zachary remains final authority.

> This is not approval to deploy. This is not approval to alter doctrine. This is not approval to override Mike Zachary. Per `DISPATCH_CONSTITUTION_v2.md` Section 19: No Spec. No Prompt. No Build. No Approval. No Implementation. Everything below is a proposed spec for Mike's review — not an implementation that has been authorized to go live.

---

## 1. Purpose

`DISPATCH_PROGRAM_MAP.md` describes what Dispatch is in plain language. This document proposes how to actually build it: runtime design, repository structure, Portal design, cognitive function design, the deterministic Spine design, a phased deployment path, and a first-pass illustrative code scaffold. Every phase below ends at a Mike approval gate — nothing here green-lights moving past prototype into production or into contact with real business data.

## 2. Architecture Recap

```
Authority Layer        Mike Zachary
Presentation Layer     Portal
Organizational Layer   Manager · Publisher · Intelligence Analyst · Library · Archive
Cognitive Layer        Manager reasoning · Publisher drafting · Intelligence analysis
Deterministic Layer    Dispatch Spine
```

The single architectural rule that shapes every design decision below: **deterministic work never lives in a model call, and cognitive work never owns storage, routing, or approval gates.** Anywhere this proposal is tempted to put a judgment call into the Spine, or put state ownership into an agent, that's a design error to fix before build.

## 3. Runtime Design

At runtime, a single request moves through the system like this:

```
1. Trigger arrives (Portal action, scheduled review, or a Spine-detected event)
2. Dispatch Spine validates the trigger, assigns/updates state, writes an event
3. Spine's routing table decides: does this need a cognitive function, or is it
   purely mechanical (storage, status change, formula scoring)?
       → Mechanical: Spine handles it directly, no model call, done.
       → Needs judgment: Spine invokes exactly one cognitive function
         (Manager reasoning, Publisher drafting, or Intelligence analysis)
         with a bounded, structured input — not open-ended chat context.
4. Cognitive function returns a structured output (a card, a draft, a
   recommendation) — never a direct external action.
5. Spine records the output as an event, updates state, and — if the
   classification warrants it — creates a Portal card.
6. Portal surfaces the card to the right human (Mike, driver, or approved
   external viewer) filtered by consequence level (0-5, see Program Map §8).
7. Human action in Portal becomes a new structured event, and the loop repeats.
```

Two runtime guarantees fall out of this directly, and both are enforced in the Spine, not left to agent discipline:
- **No cognitive function calls another cognitive function directly.** Manager reasoning, Publisher drafting, and Intelligence analysis only ever talk to the Spine. Cross-function handoffs (Intelligence → Publisher, Publisher → Manager) are Spine-routed events, so every handoff is logged and auditable.
- **No cognitive function has direct write access to Library, Archive, or an external system.** They can only *propose* — the write itself is a Spine operation gated by the classification/approval rules in the Program Map.

## 4. Repository Structure Proposal

A structure that keeps the deterministic/cognitive/presentation split visible in the filesystem, not just in documentation:

```
dispatch/
├── docs/                          # governance & architecture (this repo's current content)
│   ├── DISPATCH_CONSTITUTION_v2.md
│   ├── CONTEXT_MASTER.md
│   ├── ARCHITECTURE.md
│   ├── MANAGER.md / PUBLISHER.md / INTELLIGENCE_ANALYST.md
│   ├── PORTAL_DESCRIPTION.md / COGNITIVE_FUNCTIONS.md
│   ├── DISPATCH_SPINE_OVERVIEW.md
│   ├── ARCHITECTURAL_DISPOSITION.md / SUPERSESSION_MAP.md
│   └── archive/superseded/        # old drafts, e.g. DISPATCH_CONTEXT_MASTER_v2.md
│
├── spine/                         # deterministic layer — no model calls anywhere in here
│   ├── state/                     # state registry, work item schema
│   ├── routing/                   # routing table, event dispatch
│   ├── queue/                     # pending work queues
│   ├── validation/                # required-field & schema checks
│   ├── scoring/                   # formula-driven scoring engine
│   ├── storage/                   # file + metadata storage adapters
│   ├── audit/                     # event log, audit trail
│   └── automation/                # pre-approved automation hooks only
│
├── cognitive/                     # the three cognitive functions — thin, bounded, structured I/O
│   ├── manager_reasoning/
│   ├── publisher_drafting/
│   └── intelligence_analysis/
│
├── intelligence_pipeline/         # deterministic sub-pipeline feeding Intelligence Analyst
│   ├── sweepers/
│   ├── acquisition/
│   ├── parsing/
│   └── scoring/                   # may reuse spine/scoring
│
├── library/                       # approved reusable truth — deterministic service first
├── archive/                       # completed history — deterministic service first
│
├── portal/                        # presentation layer
│   ├── mike_view/                 # command cockpit
│   ├── driver_view/                # phased in later
│   └── external_view/             # customer/broker/shipper — confidence windows only
│
├── governance/                    # agent charters, once approved — empty until Mike approves any
│   └── charters/
│
└── tests/
    ├── spine/
    ├── cognitive/
    └── portal/
```

Nothing under `cognitive/` or `governance/charters/` should contain real production logic until an Agent Charter exists for that function and Mike has approved it (Program Map §16, item 4). Until then those directories hold interface stubs and test doubles only.

## 5. Portal Design

Portal is one front door with permission-based views over a single Dispatch operational spine — not three separate systems.

**Mike view (command cockpit).** The only place decisions actually get made. Shows: decision cards, review cards, active work queue, packet approvals, load/opportunity recommendations, exceptions and conflicts, Archive/Library review prompts, high-value alerts. Every action Mike takes here is captured as a structured event and sent to the Spine — the Portal itself never resolves an approval; it just collects the human's choice and hands it to the Spine as data.

**Driver view.** Moment-to-moment operational support: assignment info, route notes, pickup/delivery details, required documents, proof-of-delivery photo instructions, route risk notes, check-in prompts. Read-mostly, scoped to that driver's own assignments — no visibility into Mike's decision queue or internal scoring.

**External view (customer/broker/shipper).** Confidence-building windows only — status of their shipment/engagement, not a database query surface. Never exposes internal scoring logic, internal decision notes, or direct database access, per the Constitution's forbidden-actions list.

**Consequence filtering (0–5 levels)** is a Portal rendering rule fed directly by the Spine's classification of each item — the Portal doesn't decide what's noisy, the Spine's classification does, and the Portal just respects it. This keeps "don't show Mike low-value noise" a deterministic, testable rule instead of a UI heuristic.

## 6. Cognitive Function Design

Each of the three cognitive functions is proposed as a narrow, structured-I/O service — not a general chat agent with tool access.

**Manager reasoning**
- Trigger conditions: scheduled review fired by Spine cron, workflow event from routing table, exception condition flagged by validation/scoring, Portal-mediated human action event.
- Input: a structured "office state" snapshot (open items, their classifications, priorities, deadlines) — never a raw chat prompt.
- Output: classification + priority + routing decision + card level (0–5), in the fixed schema from `MANAGER.md` §5 (source function, work item ID, status, priority, required action, risk level, deadline, recommended routing, human-attention flag).
- Forbidden at the interface level: no tool that lets it approve, submit, book, sign, or modify its own instructions.

**Publisher drafting**
- Trigger: a requirement/packet request routed from Intelligence Analyst, Manager, or a Mike-initiated Portal request.
- Input: approved Library assets + assigned requirements + source facts already validated by the Spine.
- Output: a draft document/packet plus a missing-artifact report, using the Recommendation Card format where a decision is implied.
- Forbidden at the interface level: no tool that submits externally, signs, certifies, or writes directly to Library/Archive (those are Spine-mediated after Mike approval).

**Intelligence analysis**
- Trigger: new scored intelligence item arriving from the deterministic pipeline (sweeper → acquisition → parsing → scoring).
- Input: structured, already-scored records — not raw unparsed source material.
- Output: one of the fixed card types from `INTELLIGENCE_ANALYST.md` §5, plus a routing recommendation from the table in §6.
- Forbidden at the interface level: no tool that changes scoring rules, promotes Library truth, or makes a final business decision.

All three share one integration pattern: the Spine calls them with a bounded structured payload and a defined output schema, records the input/output pair in the audit trail, and never lets them call each other, storage, or the outside world directly. This is what makes "AI decides nothing" (Constitution §4) enforceable in code rather than just in policy.

## 7. Deterministic Dispatch Spine Design

Component responsibilities, expanded from `DISPATCH_SPINE_OVERVIEW.md` into a rough data-model sketch:

| Component | Core record | Key fields (illustrative) |
|---|---|---|
| State Registry | WorkItem | id, type, status, classification, priority, owner_function, created_at, updated_at |
| Routing Table | RoutingRule | trigger_type, condition, destination_function, requires_cognition (bool) |
| Queue | QueueEntry | work_item_id, queue_name, enqueued_at, attempts |
| Validation Layer | ValidationResult | work_item_id, schema_id, passed (bool), missing_fields[] |
| Storage Layer | StoredObject | id, kind (file/metadata/record), location, checksum |
| Scoring Engine | ScoreResult | work_item_id, formula_id, inputs{}, score, threshold_bucket |
| Event Log | Event | id, work_item_id, event_type, actor (human/spine/function name), payload, timestamp |
| Audit Trail | AuditEntry | event_id, before_state, after_state, approval_ref (nullable) |
| Automation Hooks | AutomationTrigger | rule_id, precondition, approved_action_id |

Every cognitive-function call is itself just another `Event` with `actor` set to the function name and its structured input/output stored as the `payload` — so the audit trail answers "why did Dispatch do X" without needing to reconstruct a chat transcript.

## 8. Data Flow / Integration Diagram

```
External sources (SAM, load boards, email, folders)
        │  Sweepers (deterministic collection)
        ▼
Acquisition (store + prepare)  ──────────────┐
        │  Parsing & Extraction               │  all deterministic,
        ▼                                      │  all Spine-owned
Scoring Engine (formulas)  ───────────────────┘
        │
        ▼
Intelligence Analyst (cognitive — interprets)
        │
        ▼
Routing decision (Spine routing table) ──► Library review
                                       ├──► Archive
                                       ├──► Publisher (packet requirement)
                                       └──► Manager (escalation/opportunity) ──► Portal ──► Mike
```

Portal actions flow the opposite direction, always re-entering as Spine events (Program Map §8). No arrow in this diagram skips the Spine.

## 9. Deployment Path

Phased, each phase gated on Mike's explicit approval before the next begins. Nothing here is a commitment to a timeline — it's a proposed sequence.

- **Phase 0 — Spine skeleton.** State Registry, Event Log, Audit Trail, Validation Layer. No cognitive functions, no Portal, no real data. Purpose: prove the deterministic backbone is reliable and auditable on its own.
- **Phase 1 — Library & Archive as deterministic services.** Plain storage + retrieval, schema-validated intake, no cognitive classification yet. Purpose: get approved-truth storage and history storage solid before anything drafts against them.
- **Phase 2 — Portal MVP, Mike view only.** Read-only cockpit showing Spine state (status cards, queue) with no cognitive functions feeding it yet — proves the presentation layer and the "Portal is not the system of record" boundary before any judgment-based content flows through it.
- **Phase 3 — Intelligence pipeline (deterministic half) + Intelligence Analyst (cognitive half).** Sweepers/Acquisition/Parsing/Scoring first, validated end-to-end on sample data; Intelligence Analyst added last, behind an Agent Charter, on a sandbox/non-production data set before any live source feeds it.
- **Phase 4 — Manager reasoning + Publisher drafting.** Added only after Phase 3 proves the interpretation layer is trustworthy and after Agent Charters exist for both. Manager first (it only reasons about internal office state), Publisher second (it produces external-facing drafts, so it needs Library to already be solid from Phase 1).
- **Phase 5 — Driver and external Portal views.** Added last, since they're the most exposed surfaces and depend on every upstream function already being stable and governed.

No phase includes autonomous booking, submission, or approval at any point — those remain Mike-only actions through every phase, permanently, not just until some later phase "unlocks" them.

## 10. First-Pass Code

A minimal, illustrative scaffold of the Phase 0 Spine skeleton has been added under `proposal/spine_prototype/`. It is explicitly **not** wired to real data, has no network access, no automation hooks that do anything beyond logging, and is meant to demonstrate the shape of the State Registry / Event Log / Validation Layer / Routing Table split described in Section 7 — nothing more. See that directory's own README for scope and limits.

## 11. Governance Compliance Checklist

- [x] No autonomous load booking, contract commitment, government submission, or final approval anywhere in this design.
- [x] No self-modifying prompts or code — cognitive function interfaces are fixed, structured schemas, not editable-by-itself instructions.
- [x] No authority transfer away from Mike — every approval-level (5) item terminates at a Portal card for Mike, in every phase.
- [x] No hidden decisions — every cognitive-function call is logged as an auditable Event with input/output payload.
- [x] No direct external access to internal databases from the External Portal view.
- [x] No AI approval of truth, facts, packets, or submissions — Library/Archive writes are Spine-gated, not cognitive-function-gated.
- [x] Library and Archive remain separate services at every phase; no merge.
- [x] Cognitive functions cannot call each other directly — Spine-mediated only.
- [ ] Agent Charters — **not yet in place for any function.** Per `DISPATCH_CONSTITUTION_v2.md` §13, this is required before Phase 3–4 cognitive functions move past prototype. Flagged as an open item, not resolved by this proposal.

## 12. Open Questions for Mike

1. Should `proposal/spine_prototype/` be treated as the actual Phase 0 starting point, or purely illustrative/throwaway once reviewed?
2. Should Agent Charter drafting begin now (in parallel with Phase 0/1 build), or only after Phase 0/1 are proven?
3. Confirm the repository-structure proposal in Section 4 (or redirect it) before any real code beyond the illustrative scaffold is written.
4. Confirm the `DISPATCH_CONTEXT_MASTER_v2.md` disposition question raised in `DISPATCH_PROGRAM_MAP.md` §16 — it affects whether any of its content (e.g. the Agent Relationship Matrix) should be mined for Phase 3-4 design or left retired.

---

**Required Closing**

This is a recommendation only.
No action is authorized.
Mike decides.
