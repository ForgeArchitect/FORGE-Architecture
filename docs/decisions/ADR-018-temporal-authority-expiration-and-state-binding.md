# ADR-018: Temporal Authority, Expiration, and State Binding

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Authorization / Temporal Integrity / State Governance

## Context

FORGE binds consequential actions to authenticated requests, institutional decisions, authorization, evidence, and execution.

However, authorization exists within time and state.

An action that was valid when approved may no longer be valid when execution occurs.

For example:

Banker may approve a transaction when sufficient funds exist.

Before execution:

- another transaction may occur,
- the balance may change,
- the destination may change,
- the authorization may expire,
- the account may be locked,
- or the applicable financial policy may change.

Likewise, Doctor may determine that a subsystem is healthy.

Before an update begins:

- the subsystem may degrade,
- another update may occur,
- configuration may change,
- a security incident may occur,
- or the health evidence may become stale.

A Security approval may become invalid after network configuration changes.

An Engineer approval may become invalid after the proposed package changes.

A human approval may become invalid after its intended execution window expires.

Therefore, FORGE must not treat authorization as permanently valid merely because it was once valid.

## Decision

Consequential authority in FORGE is bound not only to the requested action but also to the relevant temporal and state conditions under which that authority was granted.

Authorization may expire.

Authorization may be invalidated by material state change.

Execution must establish that the authorization remains valid immediately before consequential use.

## Core Rule

> Authorization is valid only while the conditions supporting that authorization remain valid.

Past permission is not necessarily present permission.

## Authorization Context

An authorization may be bound to:

- request identity,
- action identity,
- target identity,
- institutional membership state,
- constitutional version,
- system state,
- resource state,
- credential state,
- health state,
- security state,
- financial state,
- external state,
- time window,
- dependency state,
- and other material conditions.

Not every authorization requires every binding.

The required bindings depend on risk and jurisdiction.

## Temporal Authority

Authority may have a defined lifetime.

An authorization may specify:

- issued time,
- earliest valid execution time,
- expiration time,
- maximum age,
- permitted execution window,
- or event-based expiration.

After expiration:

> The authorization no longer grants execution authority.

## Expiration

Expired authority cannot be revived merely because the underlying request remains desirable.

If execution is still required, FORGE must obtain new or renewed authorization through the applicable governance process.

## No Silent Renewal

FORGE cannot silently extend an authorization's expiration.

Renewal is a governance event where required.

For example:

An approval valid for ten minutes cannot become valid for one hour because execution was delayed.

## No Retroactive Extension

After authority expires, FORGE cannot retroactively change the expiration time to make an attempted execution appear authorized.

Historical expiration remains part of the evidence record.

## State Binding

Some authorization depends on specific state rather than merely time.

For example:

Banker approves:

> Transfer $500 if available balance remains at least $10,000.

The authorization depends on financial state.

Doctor approves:

> Update subsystem while health state remains READY.

The authorization depends on health state.

Security approves:

> Connect to Endpoint X while certificate identity remains Y.

The authorization depends on security state.

If the required state changes, the authorization may become invalid.

## State Identity

Where appropriate, FORGE may assign an authenticated identity to relevant state.

Examples include:

- configuration version,
- software version,
- account-state snapshot,
- health baseline,
- membership version,
- constitutional version,
- security-policy version,
- infrastructure state,
- credential version,
- or resource snapshot.

Authorization can reference these identities.

## Material State Change

Not every state change invalidates authorization.

The system must distinguish between:

- immaterial state change,

and:

- material state change.

A material state change is one that could reasonably affect the basis, scope, risk, meaning, or validity of the authorization.

## Materiality Rules

Materiality should be defined by the applicable institution or constitutional policy where possible.

FORGE should not have unrestricted discretion to declare inconvenient changes immaterial.

Examples of potentially material changes include:

- target change,
- amount change,
- recipient change,
- software package change,
- destination change,
- permission change,
- security-policy change,
- health degradation,
- credential rotation,
- institutional membership change,
- constitutional version change,
- or significant resource-state change.

## Request Mutation

Material mutation of the request invalidates authorization inherited from the previous request state.

For example:

Approved:

> Transfer $500 to Account A.

Modified:

> Transfer $5,000 to Account A.

The original authorization does not apply.

Likewise:

Approved:

> Deploy Package Hash X.

Modified:

> Deploy Package Hash Y.

The original approval does not authorize Package Y.

## Authorization Fingerprint

Consequential authorization should be bound to an authenticated representation of the approved action.

This may include a cryptographic digest or equivalent request fingerprint.

The purpose is to make material mutation detectable.

## State Preconditions

Authorization may contain explicit preconditions.

For example:

- balance must remain above threshold,
- Doctor state must remain READY,
- Security posture must remain VERIFIED,
- target software version must equal X,
- recipient identity must equal Y,
- resource use must remain below Z,
- or constitutional version must equal C.

Execution checks applicable preconditions before acting.

## State Postconditions

Some actions may also require postconditions.

For example:

After an update:

- expected software version must be present,
- Doctor must establish acceptable health,
- Security must verify required controls,
- and Watchers must observe the expected resulting state.

Failure of a required postcondition may trigger:

- halt,
- investigation,
- remediation,
- rollback consideration,
- or recovery.

## Time-of-Check / Time-of-Use

FORGE explicitly accounts for the gap between:

> Time of Check

and:

> Time of Use.

A valid condition at approval time may no longer exist at execution time.

Therefore, high-risk state-dependent conditions should be revalidated as close to execution as reasonably possible.

## Final Pre-Execution Validation

Immediately before consequential execution, FORGE should verify the applicable authorization envelope.

This may include:

- request identity,
- authorization identity,
- expiration,
- required institutional approvals,
- target identity,
- material state,
- resource limits,
- credential validity,
- health status,
- security status,
- and constitutional version.

If required validation fails, execution does not proceed.

## Execution Window

Some actions may have an explicit execution window.

For example:

> Valid between 02:00 and 02:15.

Execution before or after that window is unauthorized unless separately governed.

## Delayed Execution

Queueing an authorized action does not freeze authority indefinitely.

A queued action remains subject to:

- expiration,
- state change,
- revocation,
- constitutional change,
- health change,
- and other applicable invalidation conditions.

## Scheduled Actions

Scheduled actions require special treatment.

A request authorized today for execution tomorrow must still satisfy applicable conditions tomorrow.

Scheduling creates an intended future execution.

It does not guarantee future authorization regardless of changed conditions.

## Recurring Authority

Recurring actions should not rely on one unlimited permanent authorization where narrower authority is practical.

Recurring authorization may define:

- frequency,
- maximum number of executions,
- maximum cumulative resource use,
- time horizon,
- permitted targets,
- conditions,
- and expiration.

Each execution remains attributable.

## Long-Lived Authority

Long-lived authority increases risk.

Where long-lived authorization is necessary, FORGE should use compensating controls such as:

- narrower scope,
- periodic revalidation,
- resource ceilings,
- Watcher coverage,
- revocation capability,
- health checks,
- and expiration.

## Event-Based Invalidation

Authority may terminate when a specified event occurs.

Examples include:

- constitutional amendment,
- credential compromise,
- member removal,
- health-state change,
- security incident,
- target-state change,
- resource threshold reached,
- completion of the authorized action,
- or HARD STOP.

## Single-Use Authority

Some authority is valid for exactly one execution.

After successful use, the authority is consumed.

A second execution requires new authority.

This is especially important for:

- financial transactions,
- privileged credential capabilities,
- irreversible actions,
- and other high-risk operations.

## Failed Attempt

Policy must define whether a failed execution attempt consumes single-use authority.

For high-risk actions, uncertainty about whether the external action occurred may require the authority to be treated as consumed until the outcome is established.

This prevents accidental duplicate execution.

## Idempotency

Where possible, consequential external actions should use idempotency mechanisms or equivalent duplicate-prevention controls.

This helps distinguish:

> Retry the same authorized action.

from:

> Perform the authorized action again.

## Revocation

Valid authority may be revoked before expiration.

Revocation should identify:

- authorization,
- revoking authority,
- reason where appropriate,
- effective state,
- and relevant time or sequence.

Once effective, revoked authority cannot execute.

## Revocation Propagation

Revocation must reach components capable of exercising the affected authority.

A revoked token remaining usable by an isolated Executor represents incomplete revocation.

High-risk authority may require positive revocation verification.

## HARD STOP

HARD STOP may immediately invalidate or suspend affected execution authority according to ADR-007.

Clearing the emergency does not automatically restore previously suspended authority.

RESET/RESUME governance determines what authority may return.

## Constitutional Change

A constitutional change may affect outstanding authorization.

The amendment process should define whether existing authority:

- remains valid,
- requires revalidation,
- is suspended,
- or is revoked.

FORGE must not assume that old authority automatically survives a constitutional change.

## Membership Change

Institutional membership changes may affect outstanding institutional decisions.

For high-risk actions, a material membership transition before execution may require revalidation.

The applicable rule should be defined by institutional policy.

## Credential Change

If a credential or credential service changes materially after authorization, affected authority may require revalidation.

A capability bound to an old credential state must not silently migrate to a new credential context.

## Health Change

Doctor health state may invalidate operations that require health readiness.

For example:

READY  
→ DEGRADED

may suspend an update authorization if READY was a required precondition.

Doctor does not thereby control the underlying action.

Doctor establishes whether the health condition remains satisfied.

## Security Change

A material security-state change may invalidate security-dependent authorization.

Examples include:

- compromise detection,
- certificate change,
- firewall change,
- identity anomaly,
- privilege escalation,
- or newly discovered vulnerability.

## Financial Change

A financial authorization may depend on:

- available funds,
- cumulative spending,
- transaction limits,
- budget period,
- recipient state,
- or fraud indicators.

A material change may require Banker revalidation.

## Resource Change

Resource authorization remains subject to ADR-012.

A request cannot use an old authorization to exceed:

- current resource ceilings,
- cumulative limits,
- concurrency limits,
- or newly exhausted resource envelopes.

## External State

Some authorization depends on state outside FORGE.

External state is inherently less controllable.

FORGE should identify which external conditions are sufficiently important to require revalidation.

Examples include:

- account balance,
- market state,
- target availability,
- external identity,
- API permission,
- or physical environment.

## Evidence Freshness

Evidence supporting authorization may itself expire.

Examples include:

- health results,
- security scans,
- account-state observations,
- identity verification,
- or external status.

Expired supporting evidence cannot continue supporting authority indefinitely.

## Trusted Time

Temporal authority depends on a trustworthy concept of time or ordering.

FORGE should not rely blindly on a single mutable application clock for high-risk expiration decisions.

Implementation may use:

- authenticated system time,
- monotonic clocks,
- trusted time services,
- signed timestamps,
- sequence numbers,
- hardware-backed time,
- or combinations of these mechanisms.

## Clock Failure

If required temporal validity cannot be established because trusted time is unavailable or contradictory, FORGE fails closed for authority that depends on that time.

Unknown time does not mean unexpired authority.

## Clock Manipulation

Changing a system clock must not revive expired authority.

Expiration logic should be designed to resist rollback of local time where technically practical.

## Ordering

Some governance questions require trustworthy ordering rather than exact wall-clock time.

For example:

Did revocation occur before execution?

Did approval occur before request mutation?

Did HARD STOP occur before the second transaction attempt?

FORGE should preserve sufficient ordering evidence to answer these questions.

## Historian Role

Historian preserves:

- authorization issuance,
- expiration,
- state bindings,
- revocation,
- execution attempts,
- state transitions,
- and relevant temporal evidence.

Historical records should preserve the original validity conditions.

## Auditor Role

Auditors may verify:

- authorization was valid when used,
- required state conditions remained satisfied,
- expiration had not occurred,
- revocation had not already taken effect,
- request identity remained unchanged,
- and execution occurred within the permitted authority envelope.

Auditors do not extend expired authority.

## Watcher Role

Watchers may observe:

- execution timing,
- target state,
- state transitions,
- duplicate execution,
- use after revocation,
- use after expiration,
- and mismatch between authorized and actual conditions.

Watcher observations become evidence under ADR-017.

## Doctor Role

Doctor provides authenticated health-state evidence where health is a condition of authorization.

Doctor does not alter expiration merely to permit execution.

## Banker Role

Banker may define financial state conditions and temporal constraints for financial authority within its jurisdiction.

Banker authorization does not override unrelated constitutional conditions.

## Executor Role

Executor must validate applicable authority immediately before consequential use.

Executor cannot rely solely on the fact that an authorization existed when the action entered the queue.

## TOCTOU Detection

Where a meaningful delay exists between final validation and irreversible execution, FORGE should minimize the interval and detect material state changes where technically practical.

If the required state changes during the interval, execution should halt where safely possible.

## Atomicity

Where supported, FORGE may use transactional or atomic mechanisms to bind validation and execution more closely.

This reduces the opportunity for state to change between authorization verification and action.

## Irreversible Actions

Irreversible actions require particularly strict temporal and state validation.

Examples may include:

- irreversible financial settlement,
- destructive deletion,
- permanent credential destruction,
- physical actuation,
- or external publication.

Stale authority is unacceptable merely because reversal is difficult.

## Pending Requests After Recovery

Requests surviving system recovery must be revalidated.

Recovery does not automatically revive:

- expired authorization,
- consumed capability,
- revoked authority,
- stale evidence,
- or state-dependent approvals.

## Constitutional Recovery

During ADR-014 Constitutional Recovery, outstanding authority may be suspended or revoked.

After governance restoration, previously pending requests must satisfy current temporal and state requirements before execution.

## No Authorization Resurrection

FORGE must never create a path where:

Expired  
→ System Restart  
→ Valid Again

or:

Revoked  
→ Recovery  
→ Valid Again

unless a new constitutionally valid authorization explicitly recreates that authority.

## Fail-Closed Rule

If FORGE cannot establish whether required authorization remains temporally and contextually valid, the consequential action does not proceed.

Unknown validity is not valid authority.

## Consequences

Temporal and state-bound authorization introduces:

- additional state tracking,
- expiration logic,
- trusted ordering,
- revalidation,
- revocation infrastructure,
- execution latency,
- and more frequent governance requests.

FORGE accepts this cost.

Authorization that ignores time and state can remain technically authentic while becoming operationally meaningless.

## Foundational Principle

> Authorization is not permanent merely because it was once valid.

> Authority belongs to a request, a scope, a state, and when necessary, a time.

> Material change requires revalidation.

> Expired authority is dead authority.

> Revoked authority is dead authority.

> FORGE verifies authority at the moment authority is used.

A consequential action may execute only while the complete authorization conditions that permit it remain valid.
