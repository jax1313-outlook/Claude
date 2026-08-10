# DISPATCH_PROGRAM_MAP.md

**Program:** Dispatch
**Document Type:** Total Program Map (Deliverable 1 of the Program Map and Build Proposal exercise)
**Status:** Proposal / Planning Draft — NOT an approved controlling document
**Owner:** Mike Zachary / Level 1 Transport
**Authority:** Mike Zachary remains final authority. This document is a recommendation only. No action is authorized. Mike decides.

---

## How This Document Was Built

This map was built strictly from the current clean-repository documents, per `SUPERSESSION_MAP.md`:

`DISPATCH_CONSTITUTION_v2.md`, `CONTEXT_MASTER.md`, `ARCHITECTURE.md`, `MANAGER.md`, `INTELLIGENCE_ANALYST.md`, `PORTAL_DESCRIPTION.md`, `COGNITIVE_FUNCTIONS.md`, `DISPATCH_SPINE_OVERVIEW.md`, `ARCHITECTURAL_DISPOSITION.md`, `SUPERSESSION_MAP.md`, `REFINEMENT_ANALYST_REMOVAL.md`.

**A naming trap worth flagging up front:** `DISPATCH_CONTEXT_MASTER_v2.md` is also present in the repo and, by filename, looks like the newest context document. It is not. It describes an older 11-agent-mesh model (standing Dispatcher Agent, Automation Agent, Acquisition Agent, Processing/Rules Agent, Mission-Specific Refinement Analysts as cognitive roles) that `SUPERSESSION_MAP.md` explicitly lists as superseded, and that `ARCHITECTURAL_DISPOSITION.md` and `REFINEMENT_ANALYST_REMOVAL.md` retire or reassign. This map treats `CONTEXT_MASTER.md` (Round 2) as current and `DISPATCH_CONTEXT_MASTER_v2.md` as historical, per the instruction not to assume older Dispatch versions are current. See Section 16 for the full conflict note.

This document does not authorize deployment, does not alter doctrine, and does not override Mike Zachary.

---

## 1. What Dispatch Is

Dispatch is a governed digital office built for Level 1 Transport. Its job is to lower Mike's cognitive and administrative load and to produce things a human can actually use: decision cards, packets, checklists, status views, and operational visibility.

Dispatch is built around six things working together: Mike as final authority, the Portal as how Mike sees and touches the system, the organizational functions (Manager, Publisher, Intelligence Analyst, Library, Archive) that do the office's work, and the Dispatch Spine underneath all of it, running the deterministic, boring, reliable machinery.

Dispatch may recommend, draft, organize, validate, route, summarize, and prepare. It does not have to be beautiful engineering — it has to be useful to a person running a transport business.

## 2. What Dispatch Is Not

Dispatch is not a chatbot. It is not an 11-agent mesh of standing autonomous agents. It is not a self-governing company. It is not a fully autonomous freight operator. It cannot approve, sign, submit, book a load, commit the business, alter its own doctrine, or transfer authority away from Mike.

It also does not invent facts. If information is missing, Dispatch marks it MISSING, UNKNOWN, NEEDS REVIEW, NEEDS SOURCE, or NEEDS MIKE DECISION rather than guessing.

Specifically forbidden, regardless of how "capable" a build gets: autonomous load booking, autonomous contract commitment, autonomous government submission, autonomous final approval, self-modifying prompts, self-modifying code, authority transfer away from Mike, hidden decisions, direct external access to internal databases, and AI approval of truth, facts, packets, or submissions.

## 3. Major System Layers

Dispatch has five layers, stacked from human authority down to raw machinery:

```
Authority Layer        Mike Zachary — final say on everything that matters
Presentation Layer     Portal — the only place Mike, drivers, and approved
                        outsiders actually see or touch the system
Organizational Layer   Manager, Publisher, Intelligence Analyst, Library, Archive
                        — the business functions of the office
Cognitive Layer        Manager reasoning, Publisher drafting, Intelligence
                        analysis — the three places reasoning is actually used
Deterministic Layer    Dispatch Spine — state, routing, validation, storage,
                        queues, scoring, audit, event log
```

Cognitive functions sit "inside" the organizational layer — they are how Manager, Publisher, and Intelligence Analyst do their thinking. The Spine sits underneath everything, silently keeping the system honest, auditable, and reliable, and it is the only layer that talks to storage, queues, and automation directly.

## 4. Organizational Functions

These are the business departments of the office. Each has one job.

- **Manager** — runs the office. Protects Mike's attention, classifies and prioritizes incoming work, prepares cards, escalates real problems, stays quiet when nothing needs a human.
- **Publisher** — produces documents. Drafts and assembles packets, letters, forms, checklists, and tenders from facts and requirements that are already approved. Never invents facts, never submits, never approves.
- **Intelligence Analyst** — interprets. Takes collected, parsed, scored data and explains what it actually means for Level 1 Transport: risk, suitability, special requirements, patterns.
- **Library** — stores approved reusable truth: facts, templates, forms, rate sheets, production parts. Starts as a plain deterministic storage service; cognitive help (like auto-classification) may be layered in later.
- **Archive** — stores completed history: final records, evidence, source records, decision records, submission history. Also starts deterministic.
- **Portal** — the presentation layer. Not the system of record. Shows cards, statuses, decisions, and controlled workflow to humans.

Two things in the older material are *not* current standing departments in this sense: Dispatcher and Refinement Analyst are addressed separately in Sections 5–6 and 16, because the current documents changed how they're realized.

## 5. Deterministic Runtime Functions

Everything that doesn't need judgment lives in the Dispatch Spine, not in an AI call. The Spine owns:

- **State Registry** — tracks the status of every work item.
- **Routing Table** — defines fixed, deterministic paths for where work goes next.
- **Queue** — holds pending work waiting to be processed.
- **Validation Layer** — checks required fields and schemas before anything moves forward.
- **Storage Layer** — saves files, metadata, and records.
- **Scoring Engine** — runs formula-driven scores (not judgment calls).
- **Event Log** — records what happened, when.
- **Audit Trail** — preserves traceability for everything.
- **Automation Hooks** — trigger pre-approved routine actions only.

The Spine never reasons about business meaning, never drafts, never interprets a solicitation, never decides what Mike should do, and never approves anything. It is meant to be reliable, boring, and auditable — the opposite of clever.

Older material named some of this machinery as if it were staffed by standing AI agents — Automation Agent, Acquisition Agent, Processing/Rules Agent. Per `ARCHITECTURAL_DISPOSITION.md`, that framing is retired: automation, acquisition/intake, and rules/scoring/parsing are all deterministic Spine components now, not cognitive roles.

## 6. Cognitive Functions

Dispatch uses reasoning in exactly three places, because that's where reasoning actually earns its keep:

- **Manager reasoning** — attention protection, prioritization, escalation, coordination. Fires on scheduled reviews, workflow events, exceptions, and Portal-mediated human actions — not continuously.
- **Publisher drafting** — assembling human-facing documents from approved facts and templates. Drafts only; never approves or submits.
- **Intelligence analysis** — turning collected/scored data into operational meaning: risk, suitability, anomalies, recommendations.

Every cognitive function follows the same boundary rules: recommend, don't decide; draft, don't approve; analyze, don't commit; escalate, don't bypass; explain uncertainty; preserve source traceability; use the Spine for state/storage/routing; use Portal for presentation; defer final authority to Mike.

Not every function is an agent. Deterministic work stays in code, schemas, and state machines — see Section 5.

## 7. Human Authority Flow

Authority in Dispatch flows in exactly one direction: down from Mike, never up past him.

```
Mike Zachary (final authority)
    ↓ works through
Portal (the only interface Mike actually uses to touch the system)
    ↓ Portal actions become
Structured Events
    ↓ recorded and routed by
Dispatch Spine
    ↓ Manager reacts only when needed
Manager (coordination / escalation / prioritization / attention filtering)
    ↓ delegates work to
Publisher / Intelligence Analyst / Library / Archive
```

Mike does not directly operate Manager, Publisher, or Intelligence Analyst. He acts through the Portal. Whatever any cognitive function proposes — a draft, an interpretation, a recommendation — routes back up through a Portal card for Mike's decision when a decision is actually required. No function in the system can grant itself authority Mike hasn't given it, and nothing can quietly expand its own boundary — that's a Conflict Notice trigger, not a decision the system is allowed to make on its own.

## 8. Portal Flow

The Portal is not optional — it's the only way Dispatch produces value a human can use.

```
Mike opens Portal
    → sees decision cards, review cards, active queue, packet approvals,
      recommendations, exceptions/conflicts, Archive/Library prompts, alerts
    → takes an action (approve / reject / request revision / defer / ignore / flag)
        → action becomes a structured event
            → Dispatch Spine records the event
                → Manager reacts if coordination/escalation/prioritization is needed
                    → downstream function (Publisher, Intelligence Analyst, etc.)
                      does the actual work
                        → result comes back to Portal as a new/updated card
```

Portal presentation is filtered by consequence, not flooded with everything happening in the system:

| Level | Display Type | Human Burden |
|---|---|---|
| 0 | Silent log | None |
| 1 | Status | Awareness only |
| 2 | Review | Optional inspection |
| 3 | Decision | Mike action required |
| 4 | Conflict | Mike resolution required |
| 5 | Authority | Final approval required |

Beyond the Mike cockpit, the Portal architecture also has to preserve room for a Driver view (assignments, route notes, pickup/delivery details, required documents, POD guidance) and limited external visibility for customers/brokers/shippers — confidence-building windows only, never direct database or scoring-logic access.

## 9. Data Flow

The end-to-end data path, from raw source material to something Mike can act on:

```
Sweepers (collect from SAM, load boards, email intake, folders, approved sources)
    ↓
Acquisition (obtain, name, store, prepare source material — deterministic)
    ↓
Parsing & Extraction (pull structured fields: dates, titles, solicitation numbers,
    locations, deadlines, contacts, rates — deterministic)
    ↓
Scoring Engine (formula-driven scores, thresholds, tables — deterministic)
    ↓
Intelligence Analyst (interprets: what does this mean for Level 1 Transport? — cognitive)
    ↓
Routing to the correct destination:
    Library review · Archive · Publisher · Manager/Portal (decision or risk) · discard
    ↓
Manager (prioritizes, classifies, prepares cards)
    ↓
Portal (presents to Mike)
    ↓
Mike decides
```

Everything up through Scoring is deterministic Spine work. Interpretation is the one cognitive hop in the middle. Nothing skips Manager's classification before it reaches Portal, and nothing reaches an external party without passing through Publisher and Mike approval first.

## 10. Work Item Lifecycle

Every piece of work — an opportunity, a load, a document request, a cleanup task — follows the same generic lifecycle inside the Spine, coordinated by Manager:

1. Intake event received
2. Source identified
3. Classification assigned (Routine / Status / Review Needed / Decision Needed / Conflict / Authority / Archive / Library Candidate / Noise)
4. Priority assigned (consequence first, urgency second)
5. Owner function assigned (Publisher, Intelligence Analyst, Library, Archive, etc.)
6. Required output defined
7. Validation requirement assigned
8. Status tracked by Dispatch Spine
9. Result returned
10. Portal card created — only if the classification actually warrants one
11. Mike action captured, if required
12. Final disposition recorded
13. Archive or Library routing completed, if applicable

Manager's priority order for ranking competing work: safety/compliance/legal/authority risk first, then active revenue opportunity, then customer/broker/shipper/driver-facing needs, then government deadlines, then operational positioning, then document production, then Library/Archive/cleanup, then discovery/research intake, then deferred improvement work.

## 11. Approval Lifecycle

Approval is the one lifecycle that can never terminate inside the system — it always terminates at Mike.

```
Work item reaches an authority-level consequence
    (final decision, external submission, business commitment, doctrine change,
     deployment approval, rate/compliance/legal call)
    ↓
Classified as Authority (Level 5) — never lower
    ↓
Manager prepares an Authority Card (or a Conflict Card if the request itself is
    improper — e.g. it would require inventing facts, signing, submitting, or
    changing doctrine)
    ↓
Presented through Portal — never resolved in a chat window, never resolved by
    a cognitive function acting alone
    ↓
Mike approves, rejects, or requests revision
    ↓
Decision recorded as an event in the Spine (state + audit trail)
    ↓
Downstream function (Publisher, Automation hook, etc.) may now act — but only
    within the exact scope Mike approved
```

No agent, builder, or workflow may quietly resolve an approval itself. If a task would require approving, submitting, certifying, signing, deciding rates, deciding compliance, or deciding legal sufficiency, the correct system behavior is a Conflict Notice, not an autonomous action.

## 12. Library Lifecycle

Library holds *approved reusable truth* — nothing enters it without a decision.

```
Candidate identified (by Intelligence Analyst, Publisher, or Archive review)
    ↓
Library Candidate classification assigned by Manager
    ↓
Review — deterministic checks first (schema, completeness, duplication),
    Quality Control Review only if the item is genuinely high-risk or
    architecturally significant (not for routine candidates)
    ↓
Mike approval (or approved workflow) required before promotion
    ↓
Stored in Library as approved reusable truth
    ↓
Reused by Publisher / Intelligence Analyst / Manager / Portal as source material
    ↓
Superseded or retired candidates are removed from active Library status,
    not silently overwritten — history goes to Archive
```

Library is never a temporary workspace, and Publisher may *nominate* candidates but may never promote its own drafts into Library truth — that promotion path is explicitly forbidden without approval.

## 13. Archive Lifecycle

Archive holds *completed history* — it is not a second Library and not the active workspace.

```
Work item reaches a terminal state (submitted, rejected, closed, superseded,
    or otherwise finished)
    ↓
Archive classification assigned by Manager
    ↓
Final record, evidence, source record, decision record, or audit bundle
    stored in Archive
    ↓
Available for reference via Portal / Manager, and for compliance or audit lookup
    ↓
May be nominated for Library review (e.g. a proven template worth reusing) —
    but promotion into Library still requires the normal Library approval path;
    Archive cannot promote itself into Library truth
```

Library and Archive must never be merged or blurred — that's an explicit forbidden action for every agent in the system.

## 14. Intelligence Lifecycle

This is the deterministic-to-cognitive pipeline described in Section 9, viewed as a lifecycle for a single piece of incoming intelligence:

```
Collected (Sweeper) → Acquired & stored (Acquisition) → Extracted (Parsing)
    → Scored (Scoring Engine) → Interpreted (Intelligence Analyst)
    → Routed to Library / Archive / Publisher / Manager+Portal / discard
```

The Intelligence Analyst's outputs are always one of a fixed set of card types: opportunity intelligence card, load intelligence summary, special requirements note, operational risk note, Library candidate recommendation, Publisher packet requirement note, Archive classification recommendation, Manager escalation recommendation, or a human decision request through Portal. It may learn from new documents, scans, corrections, and recurring patterns only within approved boundaries — it may not treat research, unverified templates, or internet content as truth, and it may not change scoring rules or approve anything itself.

## 15. Publisher

Publisher is the document-and-packet production function: it drafts, assembles, formats, compares, maps requirements, detects gaps, produces checklists, and nominates Library candidates — always from facts and requirements that are already approved.

```
Requirement/trigger received (from Intelligence Analyst, Manager, or a Portal
    request Mike initiated)
    ↓
Publisher gathers approved source material (Library assets, approved facts,
    assigned requirements) — never invents missing facts
    ↓
Publisher drafts: packet, letter, form, checklist, tender, application section
    ↓
Missing-artifact / requirement-gap reporting if source material is incomplete
    ↓
Draft returned to Manager → Portal as a Review or Decision card
    ↓
Mike approves, rejects, or requests revision
    ↓
Approved output moves to Archive (as completed history) and, if reusable,
    nominated to Library
```

Publisher may think deeply and produce powerfully, but it may never invent facts, decide pursuit, decide rates, decide compliance or legal sufficiency, approve submission, certify eligibility, sign forms, or submit packages. Government packet material (VA/DLA/FEMA forms, agency letters, tender formats, carrier/broker/shipper packets) is explicitly Publisher/Library production work, not Research Scout work — Research Scout sits entirely outside Dispatch and has no production or approval authority here.

---

## 16. Flagged Conflicts and Open Items for Mike

These are not resolved by this document — they're surfaced for Mike's decision, per the Constitution's No-Architecture-Drift and Conflict Notice rules.

1. **`DISPATCH_CONTEXT_MASTER_v2.md` is legacy despite its filename.** It describes the pre-Round-2 model (Dispatcher/Automation/Acquisition/Processing-Rules as standing cognitive agents, Mission-Specific Refinement Analysts as a live role). `SUPERSESSION_MAP.md` marks that model superseded. Recommend either retitling/relocating this file into `archive/superseded/` per `SUPERSESSION_MAP.md` Section 5, or explicitly re-confirming it is retired, so no future session mistakes it for current guidance based on its "v2" name.
2. **`DISPATCH_AGENT_GOVERNANCE_LAW_v1.md` is referenced but absent.** Both `DISPATCH_CONSTITUTION_v2.md` (Section 13) and `DISPATCH_CONTEXT_MASTER_v2.md` require it before any agent work proceeds, and no agent may exist without an Agent Charter/Governance per the Constitution. It is not in this repository. Recommend confirming whether it exists elsewhere and should be added to the clean repo, or whether it needs to be authored before any cognitive-function build (Manager reasoning, Publisher drafting, Intelligence analysis) proceeds past prototype/proposal stage.
3. **Constitution Section 6 still lists "Mission-Specific Refinement Analysts" as a Core Department**, while `REFINEMENT_ANALYST_REMOVAL.md` retires the standing role in favor of invoked-only Quality Control Review. The two documents read as reconcilable (the Constitution names a function; Round 2 changes *how* it's staffed — on-demand review, not a standing agent), but the Constitution's own text has not been updated to reflect that. Recommend a housekeeping pass to align the Constitution's wording with the current disposition, or an explicit Mike note confirming the current reading is correct as-is.
4. **No agent in this system currently has an approved Agent Charter.** Per the Constitution (Section 13) and the build priority list in `DISPATCH_CONTEXT_MASTER_v2.md` Section 13, Agent Governance Law review/lock and Agent Charter work are supposed to precede any Publisher/Library/Archive cognitive build. This program map and the accompanying build proposal are planning artifacts only — they do not constitute charters, and no cognitive function should be implemented against real data until charters exist and Mike approves them.

---

**Required Closing**

This is a recommendation only.
No action is authorized.
Mike decides.
