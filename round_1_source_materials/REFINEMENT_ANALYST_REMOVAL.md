# REFINEMENT_ANALYST_REMOVAL.md

**Program:** Dispatch  
**Document Type:** Retirement Notice and Replacement Doctrine  
**Status:** Replacement Draft  
**Authority:** Mike Zachary remains final authority  

## 1. Decision

The Refinement Analyst role is retired from the Dispatch architecture.

The concept of refinement remains useful, but the dedicated Refinement Analyst role creates unnecessary complexity and risks turning review into an argument loop.

## 2. Reason for Removal

The Refinement Analyst was intended to improve quality and prevent drift. That goal remains valid. However, making refinement a standing cognitive role creates several risks:

- Too many agents reviewing other agents
- Increased latency
- Increased API cost
- Excessive internal debate
- Confusion about authority
- More cards and alerts for Mike
- Higher cognitive load

## 3. Controlled Aggression Clarification

"Controlled aggression" is not a standing doctrine requiring a permanent adversarial agent.

In Dispatch, controlled aggression means urgency, challenge pressure, and refusal to accept weak work when review is appropriate.

It is a review posture, not a full-time role.

## 4. Replacement Model: Quality Control Review

If review is needed, Dispatch may use a limited Quality Control Review mode.

Quality Control Review is not an agent with standing authority.

It may be invoked for:

- Architecture review
- High-risk packet review
- Major doctrine review
- Deployment readiness review
- Drift review
- Critical government opportunity review
- High-value operational decision review

It should not be invoked for:

- Routine file movement
- Simple formatting
- Deterministic validation
- Every draft
- Every agent output
- Minor wording preference
- Low-risk status updates

## 5. Preferred Validation Method

Where possible, Dispatch should prefer deterministic validation over cognitive debate.

Examples:

- Schema validation
- Required field checks
- File existence checks
- Approval status checks
- Version checks
- Mathematical scoring checks
- Audit log checks

## 6. Remaining Review Authority

Mike remains final authority.

Manager may recommend review.

Dispatch Spine may trigger validation exceptions.

Quality Control Review may assist when invoked.

No review function may approve, promote, deploy, or change doctrine without Mike.

## 7. Success Standard

The removal succeeds when Dispatch avoids unnecessary argument loops while preserving strong review where it truly matters.
