# Spine Prototype — Illustrative Only

This directory is a first-pass, in-memory illustration of the Phase 0 Dispatch
Spine skeleton proposed in `DISPATCH_BUILD_PROPOSAL.md` Section 9.

**Scope and limits, read before touching:**

- No network access, no database, no file storage — everything lives in
  memory for the length of the `demo.py` run.
- No cognitive functions are called. `demo.py` simulates where Manager
  reasoning / Publisher drafting / Intelligence analysis *would* be invoked
  by printing a placeholder instead of calling a model.
- No automation hook does anything beyond appending to the event log —
  none of them can take an external action.
- This is not wired to real Level 1 Transport data and must not be treated
  as a production system, a deployed component, or an approval to deploy.
- This is a recommendation/proposal artifact only. No action is authorized.
  Mike decides.

## Files

- `state_registry.py` — WorkItem records and status transitions.
- `validation.py` — required-field / schema checks.
- `routing.py` — deterministic routing table (decides whether a work item
  needs a cognitive function or is purely mechanical).
- `event_log.py` — append-only event + audit log.
- `demo.py` — runs one illustrative work item through the skeleton end to
  end and prints what happened at each step.

## Running the demo

```
python3 proposal/spine_prototype/demo.py
```
