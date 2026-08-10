# COGNITIVE_FUNCTIONS.md

**Program:** Dispatch  
**Document Type:** Cognitive Function Design  
**Status:** Replacement Draft  
**Authority:** Mike Zachary remains final authority  

## 1. Purpose

This document defines the cognitive functions of Dispatch.

Cognition is used only where reasoning, interpretation, drafting, judgment support, or analysis is needed.

Not every Dispatch function is an AI agent. Deterministic functions should be handled by code, schemas, queues, storage, validation, and workflow logic.

## 2. Core Cognitive Functions

Dispatch uses three primary cognitive functions:

- Manager reasoning
- Publisher drafting
- Intelligence analysis

These functions work with the Dispatch Spine and Portal. They do not replace the Dispatch Spine and do not replace Mike.

## 3. Manager Cognitive Function

### Mission

Manager reasoning protects attention, interprets office state, identifies meaningful conflicts, prepares decision-ready cards, and helps route work when judgment is required.

### Cognitive Work

Manager may reason about:

- What matters now
- What should be escalated
- What should wait
- What can be ignored
- Which work is higher priority
- Whether a conflict is real or noise
- Whether a recommendation needs Mike
- Whether a weak plan should be challenged
- Whether doctrine tension exists

### Not Manager Cognitive Work

Manager should not use cognition for:

- Routine routing mechanics
- File movement
- Fixed status transitions
- Deterministic scoring
- Required field validation
- Storage operations
- Audit logging

Those belong to the Dispatch Spine.

## 4. Publisher Cognitive Function

### Mission

Publisher drafts and assembles human-facing production materials from approved facts, source material, templates, and assigned requirements.

### Cognitive Work

Publisher may reason about:

- How to word a packet section
- How to adapt approved facts to a specific opportunity
- How to assemble a draft packet
- How to create a cover letter
- How to produce reusable production assets
- How to map source requirements into a draft response
- How to prepare customer-growth materials

### Not Publisher Cognitive Work

Publisher may not:

- Approve facts
- Decide truth
- Submit documents
- Sign documents
- Change Library status
- Override Intelligence findings
- Bypass Mike approval

## 5. Intelligence Analyst Cognitive Function

### Mission

Intelligence Analyst interprets collected data, identifies operational meaning, detects risks, evaluates opportunity context, and routes useful insight.

### Cognitive Work

Intelligence Analyst may reason about:

- Requirements meaning
- Operational risk
- Special requirements
- Suitability for Level 1 Transport
- Anomalies
- Opportunity relevance
- Data uncertainty
- Recommended next action
- Library or Publisher implications

### Not Intelligence Cognitive Work

Intelligence Analyst should not use cognition for:

- Basic scraping
- File downloading
- Fixed parsing
- Formula scoring
- Database storage
- Version control
- Record retention execution

Those belong to deterministic systems.

## 6. Cognitive Function Boundaries

All cognitive functions must follow these boundaries:

- Recommend, do not decide.
- Draft, do not approve.
- Analyze, do not commit.
- Escalate, do not bypass.
- Explain uncertainty.
- Preserve source traceability.
- Respect role limits.
- Use Dispatch Spine for state, validation, storage, and routing mechanics.
- Use Portal for presentation.
- Defer final authority to Mike.

## 7. Cognitive Function Inputs and Outputs

| Function | Inputs | Outputs |
|---|---|---|
| Manager | Staff reports, queue state, exceptions, decisions needed | Priority plan, routing recommendation, cards, escalations |
| Publisher | Approved facts, templates, requirements, source documents | Draft packets, letters, reusable assets, production text |
| Intelligence Analyst | Collected records, parsed data, scoring results, source documents | Analysis cards, risk notes, recommendations, routing notes |

## 8. Success Standard

Cognitive functions succeed when they do the thinking that deterministic systems cannot do.

They fail when they perform routine software tasks, create noise, or require Mike to manage the system manually.
