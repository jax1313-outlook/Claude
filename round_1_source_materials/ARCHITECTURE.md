# ARCHITECTURE.md

**Program:** Dispatch  
**Document Type:** Architecture Model  
**Status:** Replacement Draft  
**Authority:** Mike Zachary remains final authority  

## 1. Core Architecture Statement

Dispatch is a governed digital office built on a deterministic Dispatch Spine with bounded cognitive functions attached where reasoning, interpretation, drafting, or judgment support is required.

Dispatch is not an uncontrolled AI agent mesh.

Dispatch is not a chatbot.

Dispatch is not a fully autonomous operator.

Dispatch is a practical business system designed to reduce owner/operator cognitive load and produce usable human deliverables.

## 2. Architecture Layers

```text
Authority Layer
    Mike Zachary

Presentation Layer
    Portal

Organizational Layer
    Manager
    Publisher
    Intelligence Analyst
    Library
    Archive

Dispatch Spine
    State
    Routing
    Validation
    Storage
    Queues
    Scoring
    Automation
    Audit Trail

Cognitive Layer
    Manager Reasoning
    Publisher Drafting
    Intelligence Analysis
```

## 3. Authority Layer

Mike Zachary is final authority.

All decisions, approvals, external submissions, business commitments, doctrine changes, and deployment approvals remain under Mike's control.

No system component may transfer, simulate, or bypass Mike's authority.

## 4. Presentation Layer: Portal

Portal equals Presentation Layer.

The Portal is how Dispatch becomes visible and useful.

The Portal presents:

- Decision cards
- Review cards
- Active work
- Driver-facing information
- Customer or broker visibility where appropriate
- Packet approval items
- Intelligence summaries
- Operational alerts

Without Portal, Dispatch has no practical human-facing value.

## 5. Organizational Layer

The organizational layer defines the business functions of the Dispatch office.

### Manager

Runs the office, protects priorities, routes work, receives reports, watches exceptions, and prepares human decision cards.

### Publisher

Drafts and assembles documents, packets, letters, templates, and production assets.

### Intelligence Analyst

Interprets collected information, detects risks, evaluates opportunity meaning, and routes intelligence.

### Library

Stores approved reusable knowledge, facts, templates, and production assets.

### Archive

Stores completed history, source records, finished packets, and audit material.

## 6. Dispatch Spine

The Dispatch Spine is deterministic machinery.

It handles:

- Workflow state
- Routing mechanics
- Queue management
- Validation
- Required field checks
- Storage operations
- Audit logs
- Scoring formulas
- Automation triggers
- Event handling

The Spine should be reliable, auditable, and boring.

## 7. Cognitive Layer

Cognitive functions are used where reasoning is required.

Primary cognitive functions:

- Manager reasoning
- Publisher drafting
- Intelligence analysis

Cognitive functions do not own routing mechanics, storage mechanics, scoring formulas, or approval gates.

## 8. Deterministic vs Cognitive Separation

| Work Type | Owner |
|---|---|
| File movement | Dispatch Spine |
| Workflow state | Dispatch Spine |
| Required field validation | Dispatch Spine |
| Formula scoring | Dispatch Spine |
| Source collection | Sweeper or acquisition module |
| Parsing where structured | Parsing module |
| Meaning interpretation | Intelligence Analyst |
| Packet drafting | Publisher |
| Attention filtering | Manager |
| Final decision | Mike |

## 9. Intelligence Architecture

Intelligence is layered:

```text
Sweepers
    ↓
Acquisition
    ↓
Parsing and Extraction
    ↓
Scoring Engine
    ↓
Intelligence Analyst
    ↓
Manager / Publisher / Library / Archive / Portal
```

## 10. Manager Architecture

Manager is not an LLM router.

Manager is the Run Office function operating over a deterministic Dispatch Spine.

Manager's cognitive role is to interpret office state, protect attention, detect meaningful exceptions, and prepare decision-ready output.

The Spine performs deterministic routing mechanics.

## 11. Library and Archive Architecture

Library and Archive begin as deterministic services.

Library handles approved reuse.

Archive handles completed history.

Cognitive assistance may be added later for classification, retention recommendations, duplicate detection, or summarization, but the base services must be reliable first.

## 12. Removed Architecture Elements

### Research Scout

Research Scout is removed from Dispatch architecture. It remains a separate external discovery program and may feed material into Dispatch only through approved intake paths.

### Refinement Analyst

Refinement Analyst is retired. Review becomes Quality Control Review when needed, not a standing agent.

## 13. Portal and Multi-User Reality

Portal is critical.

Multi-user views may be phased, but the architecture must preserve the need for:

- Mike cockpit
- Driver Portal
- Customer, broker, or shipper visibility windows where appropriate

Portal is not optional because human-useful deliverables are the point of the system.

## 14. Success Standard

Dispatch succeeds when the system produces useful human deliverables, reduces Mike's cognitive load, preserves human authority, and makes the business more capable.

Dispatch fails when it becomes an elegant machine that Mike cannot see, use, trust, or benefit from.
