# ADR-002: Authenticated Request Chain and Execution Integrity

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Security / Governance

## Context

A governed autonomous system cannot rely on a single component to truthfully report what a user originally requested.

If a request is approved at one stage but can be modified before reaching another subsystem or the execution layer, authorization loses its meaning.

For example, an institution may approve an action for one amount, target, resource, or purpose. If those parameters can later change while retaining the original approval, the system has authorized one action but executed another.

FORGE therefore requires a verifiable chain connecting:

1. What was originally requested.
2. What was reviewed.
3. What was authorized.
4. What was executed.
5. What actually occurred.

## Decision

FORGE adopts an authenticated request chain in which consequential requests receive a unique authenticated identity bound to their normalized intent and relevant execution parameters.

The current governed flow is:

Request  
→ Dispatcher  
→ Gatekeeper  
→ Auditor Checkpoint  
→ Relevant Subsystem Institution(s)  
→ Auditor Checkpoint  
→ Authorization  
→ FORGE Execution Process  
→ Watcher Observation  
→ Final Auditor Verification

The request identity follows the action through the governed process.

A component does not need to trust another component's description of the request when an independent authenticated record can be verified.

## Dispatcher

The Dispatcher is the controlled routing authority for governed requests.

Its responsibilities include:

- accepting requests through the authorized ingress path,
- assigning or associating authenticated request identity,
- routing requests to the constitutionally required institutions,
- and preventing privileged actions from bypassing the governed route.

Legacy or alternate routes must not provide an independent path to privileged execution.

The Dispatcher routes authority.

It does not create authority.

## Gatekeeper

The Gatekeeper determines whether a request is admissible under the applicable constitutional and deterministic constraints.

The Gatekeeper may approve passage or deny passage.

It does not execute the requested action.

Gatekeeper approval does not replace the jurisdiction-specific approvals required from other institutions.

## Authenticated Request Identity

A consequential request receives an authenticated identifier associated with the material characteristics of the requested action.

The identity must be bound strongly enough that material alteration of the request cannot silently inherit the previous authorization.

Relevant bound information may include:

- request identity,
- normalized intent,
- target,
- requested operation,
- material parameters,
- authorization context,
- version information,
- and other execution-critical constraints.

The precise cryptographic implementation is an implementation concern and may evolve without changing this architectural decision.

## First Auditor Checkpoint

The Auditor independently records or verifies the authenticated request state entering the governed process.

This creates an independent reference for what was actually presented for review.

Subsystem institutions therefore do not have to rely solely on the Dispatcher, FORGE, or another subsystem to tell them what the original request contained.

## Subsystem Verification

When the request reaches a relevant subsystem institution, the institution can verify the authenticated request identity against the independently preserved audit record.

If the authenticated identity or material request state does not match the state that was previously recorded, processing stops.

The changed request must enter the authorization process as a new or revised request.

## Authorization Binding

Institutional approvals are bound to the authenticated request they evaluated.

Approval of one request does not constitute approval of a materially different request.

Therefore:

> Changed action = changed authorization requirement.

Authorization cannot be treated as a reusable general permission.

## Second Auditor Checkpoint

Before execution authority is granted, the Auditor verifies that the request presented for execution remains consistent with the request and authorization chain previously recorded.

This helps detect modification occurring between institutional review and execution.

## Execution

FORGE may coordinate execution only after the constitutionally required approvals and integrity checks are satisfied.

Execution authority is scoped to the authorized request.

FORGE does not receive unrestricted authority merely because a related request was approved.

## Watcher Observation

Independent Watchers observe the execution and resulting state.

Watchers answer a different question from the Auditor.

The Auditor asks:

> Is this the request and authorization that were actually approved?

The Watcher asks:

> What actually happened?

Separating these functions prevents the executor from being the sole authority describing its own behavior.

## Final Auditor Verification

After execution, the Auditor compares:

- authenticated request,
- authorization record,
- execution evidence,
- Watcher observations,
- and resulting state evidence where available.

The objective is to determine whether the observed execution corresponds to the action that received authorization.

## Mutation Rule

A material change to a governed request invalidates authorization inherited from the previous request state.

Examples may include changing:

- amount,
- destination,
- target,
- scope,
- resource,
- operation,
- execution constraints,
- or another parameter material to institutional approval.

The modified action must be re-evaluated through the appropriate governed path.

## Replay Protection

Previous authorization must not become standing authority for repeated execution.

Execution authority should therefore be action-bound and, where appropriate, single-use, time-limited, state-bound, or otherwise resistant to unauthorized replay.

## Failure Behavior

If FORGE cannot establish the integrity of the request or authorization chain, the consequential action fails closed.

Uncertainty does not become authorization.

Silence does not become authorization.

A broken verification chain does not become authorization.

## Consequences

The authenticated request chain adds additional verification operations and architectural complexity.

FORGE accepts this overhead because authorization is meaningful only when the system can establish that the action being executed is the same action that was reviewed and approved.

## Foundational Principle

> Do not trust a component to describe what was authorized when the system can independently verify it.

FORGE binds request, authorization, execution, observation, and verification into a continuous chain of evidence.
