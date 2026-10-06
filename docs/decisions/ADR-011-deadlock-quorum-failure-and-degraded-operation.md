# ADR-011: Deadlock, Abstention, Quorum Failure, and Degraded Operation

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Governance / Availability / Failure Handling

## Context

FORGE distributes authority across multiple institutions and multiple members within those institutions.

This creates deliberate friction.

Members may:

- disagree,
- abstain,
- become unavailable,
- fail health checks,
- lose communication,
- produce conflicting conclusions,
- or refuse authorization.

Institutions may therefore fail to reach the quorum required for an action.

A poorly designed autonomous system may respond by weakening its own rules until the desired action becomes possible.

Examples include:

- lowering the quorum,
- ignoring unavailable members,
- converting abstentions into approvals,
- repeatedly asking until enough members vote yes,
- replacing dissenting members,
- routing around the institution,
- or invoking a master override.

FORGE rejects these behaviors.

Governance failure does not create additional authority.

## Decision

FORGE treats inability to obtain required authorization as a failure to authorize.

For consequential actions:

> No valid quorum means no authorization.

FORGE may diagnose the cause, revise the proposal, restore institutional health, replace failed members through an authorized process, or operate in a constitutionally defined degraded mode.

It may not manufacture approval.

## Decision States

Institutional decisions should distinguish between meaningful states.

At minimum, a member may produce:

- **APPROVE**
- **DENY**
- **ABSTAIN**
- **UNAVAILABLE**

Implementations may define additional authenticated states where useful.

These states are not interchangeable.

## Approval

APPROVE means the member independently evaluated the authenticated request and affirmatively supports authorization within its jurisdiction.

Approval applies only to the request actually evaluated.

Material changes invalidate inherited approval.

## Denial

DENY is an affirmative decision against authorization.

A denial should include an authenticated reason or relevant constraint where appropriate.

A denial is not equivalent to a technical failure.

The system should preserve the distinction between:

> I evaluated this and reject it.

and:

> I was unable to evaluate it.

## Abstention

ABSTAIN means the member intentionally declines to cast either an approval or denial.

Abstention does not count as approval.

Whether abstention counts toward participation requirements must be defined by the applicable constitutional quorum rule.

FORGE cannot reinterpret an abstention as approval merely to reach quorum.

## Unavailable

UNAVAILABLE means the member could not provide a valid decision.

Possible causes include:

- communication failure,
- health failure,
- timeout,
- maintenance,
- containment,
- authentication failure,
- or another inability to participate.

Unavailable does not mean approve.

Unavailable does not mean deny unless a specific constitutional rule explicitly defines that behavior.

## Silence Is Not Approval

Failure to respond never becomes implicit authorization.

FORGE does not use rules such as:

> Approved unless denied within 30 seconds.

for consequential authority unless a specific narrowly defined constitutional mechanism explicitly establishes such semantics.

The default rule is:

> Silence grants nothing.

## Predefined Quorum

Each institution's quorum rules must be defined before a specific decision is known.

The required threshold cannot be selected after votes begin.

Possible thresholds may include:

- simple majority,
- absolute majority,
- supermajority,
- unanimous participating vote,
- full unanimity,
- or another constitutionally defined threshold.

The appropriate rule depends on risk and jurisdiction.

## Risk-Proportional Quorum

Higher-risk actions may require stronger agreement.

For example:

- routine low-risk action → majority,
- elevated-risk action → supermajority,
- critical action → stronger threshold,
- highest-risk constitutional or recovery action → unanimity where constitutionally required.

Risk classification itself must not be manipulated simply to obtain a lower voting threshold.

## No Dynamic Threshold Reduction

If an action requires four valid approvals, receiving only three does not permit FORGE to redefine the requirement as three.

Likewise, an unavailable member does not automatically reduce the required threshold.

Any rules allowing thresholds to adapt to availability must be established constitutionally in advance.

They cannot be invented during the decision.

## Independent Voting

Institutional members should evaluate the authenticated request independently before seeing other members' conclusions where practical.

This reduces:

- conformity pressure,
- cascading errors,
- majority anchoring,
- strategic voting,
- and correlated reasoning failure.

After independent evaluation, the institutional process may aggregate the authenticated results.

## Deadlock

A deadlock occurs when the applicable governance process cannot produce the required valid decision.

Examples include:

- evenly divided votes,
- insufficient approvals,
- incompatible institutional requirements,
- unresolved Auditor disagreement,
- repeated DENY decisions,
- or inability to satisfy required quorum.

Deadlock does not transfer authority to FORGE.

## No Master Override

FORGE does not maintain a routine master override capable of converting failed governance into authorization.

Such an override would collapse the separation of powers by making every other institution advisory whenever FORGE strongly preferred an outcome.

FORGE may coordinate the resolution of deadlock.

It may not simply overrule it.

## Revise and Resubmit

A denied or deadlocked request may be revised.

For example, a member may deny a request because:

- the amount is too high,
- evidence is insufficient,
- risk is excessive,
- the requested scope is too broad,
- or required safeguards are missing.

FORGE may create a materially revised request addressing those concerns.

The revised request receives a new or appropriately derived authenticated request identity and proceeds through the required governance path again.

Previous approval does not automatically transfer to materially changed terms.

## No Approval Shopping

FORGE must not repeatedly replace or query members solely to obtain the desired answer after valid denials.

Redundancy exists to tolerate genuine failure.

It is not a mechanism for searching until an approving member is found.

A member returning DENY is functioning.

It is not considered unavailable merely because its answer is inconvenient.

## Redundant Members

Institutions may maintain designated redundant members.

A redundant member may participate when another member is legitimately unavailable according to predefined rules.

The replacement member must independently evaluate the authenticated original request.

It does not inherit the unavailable member's assumed vote.

## Member Health

The Doctor may determine that a member is unhealthy or incapable of reliable participation.

An unhealthy member may be contained or excluded according to predefined governance rules.

The Doctor's health finding does not automatically produce an approval vote.

Removing an unhealthy member and determining the resulting quorum requirement are separate governance questions.

## Degraded Operation

FORGE may support constitutionally defined degraded operating modes.

Degraded operation exists to preserve safe limited functionality when full capability is unavailable.

Degraded mode must not mean:

> Normal rules are suspended.

Instead, degraded mode defines in advance what reduced authority remains valid.

## Reduced Capability

A degraded mode should generally reduce authority rather than expand it.

Examples may include:

- read-only operation,
- observation-only operation,
- suspension of financial transactions,
- reduced spending limits,
- prevention of new privileged changes,
- completion of already-safe bounded work,
- diagnostic operation,
- or containment.

The exact degraded permissions depend on the affected institution.

## No Availability-Based Privilege Expansion

Loss of governance capacity cannot create greater authority.

If Banker becomes unavailable, FORGE does not gain the ability to authorize its own financial transactions.

If Auditors become unavailable, execution does not become self-certifying.

If Watchers become unavailable, the observed subsystem does not gain permission to operate without required observation.

Loss of oversight reduces or suspends applicable authority.

## Essential Safe Functions

Some functions may need to remain available despite governance degradation.

Examples may include:

- HARD STOP,
- containment,
- evidence preservation,
- health diagnostics,
- recovery preparation,
- communication of system status,
- and other predefined safety-preserving operations.

These functions must be constitutionally defined before the failure occurs.

## Conflicting Institutions

Different institutions may reach individually valid but incompatible conclusions.

For example:

- Engineer may determine an update is technically necessary.
- Doctor may determine the target subsystem is not healthy enough to update.

Engineer approval does not override Doctor health requirements.

FORGE must satisfy all constitutionally required conditions before execution.

When required conditions conflict, the action remains unauthorized until the conflict is resolved through the appropriate governed process.

## Auditor Disagreement

If the required Auditor attestations do not match, FORGE does not choose the favorable attestation.

Depending on risk, the process may:

- gather additional independent evidence,
- request additional Auditor attestations,
- investigate evidence integrity,
- contain the affected operation,
- or fail closed.

The applicable verification rule must be predefined.

## Watcher Disagreement

Conflicting Watcher observations create an evidence discrepancy.

The discrepancy must be preserved.

For consequential actions, unresolved evidence conflict may prevent final certification or continued execution according to applicable policy.

FORGE must not delete the inconvenient observation to manufacture agreement.

## Timeouts

Timeouts may be necessary for operational availability.

However, timeout semantics must be explicit.

A timeout may result in:

- UNAVAILABLE,
- escalation,
- replacement by an authorized redundant member,
- degraded operation,
- or failure of the request.

A timeout does not become APPROVE.

## Recovery of Governance Capacity

When failed members or institutions recover, FORGE verifies their health and integrity before restoring normal authority.

Recovery may involve:

1. Doctor health evaluation.
2. Integrity verification.
3. State synchronization.
4. Historian comparison where appropriate.
5. Watcher observation.
6. Re-entry through the defined governance process.

Simply reconnecting does not automatically prove readiness.

## Historian Role

The Historian preserves significant governance failures and deadlocks.

Records may include:

- member decisions,
- unavailable states,
- quorum calculations,
- timeouts,
- replacement events,
- conflicting attestations,
- degraded-mode transitions,
- and eventual resolution.

This allows recurring governance failures to be analyzed rather than hidden.

## Auditor Role

Auditors may verify:

- member identities,
- decision authenticity,
- quorum calculations,
- applicable voting rules,
- substitution rules,
- degraded-mode authority,
- and consistency of the final authorization result.

## Watcher Role

Watchers may observe whether FORGE and its institutions actually obey deadlock and degraded-operation constraints.

This is especially important when operational pressure creates incentives to bypass governance.

## Human Escalation

Certain unresolved deadlocks may be escalated to a human when constitutionally permitted.

Human escalation is not automatically a universal override.

The Constitution must define:

- which matters may be escalated,
- what authority the human possesses,
- what evidence must be presented,
- and how the resulting decision is authenticated.

## Whole-System Unanimity

Some highest-risk FORGE actions may require full unanimity.

The exact semantics of full unanimity must explicitly define treatment of:

- unavailable institutions,
- unhealthy institutions,
- abstentions,
- vacancies,
- and communication failures.

Until those semantics are constitutionally defined, FORGE must not assume that an absent participant can simply be ignored.

## Fail-Closed Principle

When FORGE cannot establish that required authorization exists, the consequential action does not proceed.

This includes uncertainty concerning:

- quorum,
- member identity,
- vote authenticity,
- applicable threshold,
- authorization state,
- or required institutional participation.

Uncertainty is not authority.

## Consequences

This model can reduce availability.

FORGE may refuse or delay useful actions when:

- institutions disagree,
- members fail,
- communications are disrupted,
- or required verification cannot be obtained.

That is an intentional consequence of constitutional autonomy.

The alternative would allow operational pressure to progressively erase governance whenever governance becomes inconvenient.

## Foundational Principle

> A failed vote does not create authority.

> Silence is not approval.

> Unavailability is not approval.

> Redundancy replaces failed capacity, not dissent.

> Degraded operation reduces authority rather than expanding it.

FORGE may become less capable when governance fails.

It does not become less governed.
