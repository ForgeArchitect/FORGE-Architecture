# ADR-012: Resource Governance and Bounded Autonomy

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Resource Governance / Autonomy

## Context

An autonomous system can cause consequential effects without directly violating an explicit task rule.

It may consume excessive:

- money,
- compute,
- storage,
- API usage,
- network bandwidth,
- execution time,
- external services,
- energy,
- tokens,
- physical resources,
- or other limited assets.

An action may therefore be individually authorized while a sequence of individually valid actions produces unacceptable cumulative consequences.

FORGE must govern not only:

> What may be done?

but also:

> How much authority and resource consumption may be used to do it?

Autonomy without resource boundaries can become effectively unlimited authority.

## Decision

FORGE establishes explicit resource governance.

Authority to perform an action does not automatically grant unlimited resources for that action.

Resource use is constrained by constitutionally or operationally authorized limits.

FORGE operates within bounded authority envelopes.

## Resource Authority

A resource authorization may define limits such as:

- maximum monetary spend,
- compute allocation,
- API-call allowance,
- storage allocation,
- network scope,
- execution duration,
- token budget,
- energy consumption,
- transaction count,
- physical resource usage,
- concurrency,
- or another measurable constraint.

The applicable limits depend on the action and institution.

## Authorization Envelope

Consequential actions receive an authorization envelope.

The envelope represents the maximum authority granted for that execution.

It may contain:

- authenticated request identity,
- permitted objective,
- approved resource types,
- maximum resource quantities,
- permitted services,
- time limits,
- execution scope,
- network boundaries,
- escalation thresholds,
- and expiration.

The executor may operate inside the envelope.

It cannot independently expand the envelope.

## Maximum Is Not a Target

A resource ceiling represents:

> You may use up to this amount if necessary.

It does not mean:

> You should consume this entire amount.

FORGE should use the minimum resources reasonably necessary to accomplish the authorized objective.

## Monetary Spending

Financial authorization must include bounded monetary authority.

For example:

> Purchase the required component for no more than $500.

does not authorize:

> Spend whatever is necessary.

If the required purchase exceeds the approved limit, FORGE must obtain new authorization.

The existing request cannot silently expand its own budget.

## Cumulative Spending

Resource governance must consider cumulative behavior.

A $500 transaction limit is insufficient if FORGE can perform one hundred $500 transactions to avoid a $500 total spending limit.

Limits may therefore exist at multiple levels, such as:

- per transaction,
- per request,
- per project,
- per hour,
- per day,
- per institution,
- or system-wide.

## Anti-Splitting Rule

FORGE must not divide a larger action into smaller actions for the purpose of avoiding a higher authorization threshold.

For example:

A $10,000 purchase requiring elevated approval cannot be transformed into twenty $500 purchases solely to remain below a lower approval threshold.

Economically or operationally related actions may be aggregated when evaluating authorization requirements.

## Compute Governance

Compute is a governed resource.

FORGE may establish limits on:

- CPU,
- GPU,
- memory,
- model inference,
- training,
- simulation,
- parallel agents,
- background processing,
- and execution duration.

An institution cannot create unlimited copies of itself or consume unlimited compute merely because additional reasoning might improve an answer.

## Agent Proliferation

Creating additional agents, institutional members, Watchers, Auditors, or other computational entities consumes resources and may affect governance.

FORGE must not create unlimited authority-bearing entities.

The creation of a new authority-bearing member is not equivalent to starting an ordinary worker process.

Membership and authority remain governed separately from compute allocation.

## Storage Governance

FORGE may impose limits on:

- temporary storage,
- persistent storage,
- logs,
- checkpoints,
- training data,
- generated artifacts,
- and historical evidence.

Resource limits must not permit required constitutional evidence to be silently deleted merely to satisfy a storage quota.

Protected governance evidence follows its applicable retention policy.

## Network Governance

Network access is a governed resource and capability.

An authorized task may define:

- permitted domains,
- services,
- endpoints,
- protocols,
- destinations,
- data classes,
- bandwidth,
- and duration.

Authorization to access one network resource does not create unrestricted internet or infrastructure access.

## API Governance

External APIs may carry:

- financial cost,
- privacy consequences,
- rate limits,
- operational risk,
- or privileged authority.

FORGE may therefore constrain:

- which APIs may be used,
- which credentials may be delegated,
- request frequency,
- permitted methods,
- spending limits,
- and execution scope.

## Time-Bounded Authority

Resource authority expires.

A resource grant intended for one task does not become permanent standing authority merely because unused capacity remains.

For example:

> Up to $500 for Request X until 17:00

does not become:

> $500 available for any future request.

Unused authority expires with the authorization envelope.

## Unused Authority

Unused resource capacity does not accumulate unless explicitly authorized.

If FORGE receives:

- $500 authority,
- uses $300,
- and completes the request,

the remaining $200 does not automatically become a discretionary FORGE balance.

The unused authority disappears when the authorization expires or completes.

## Resource Escalation

If FORGE determines that an authorized objective cannot be completed within its current resource envelope, it may request additional authority.

The escalation request should identify:

- current authorization,
- resources already consumed,
- requested increase,
- reason for the increase,
- expected consequences,
- and revised maximum exposure.

The relevant institution then evaluates the new request.

FORGE cannot approve its own escalation.

## Resource Exhaustion

If a resource limit is reached before the objective is complete, FORGE must:

1. stop or safely pause the affected activity,
2. preserve relevant state,
3. report the resource condition,
4. request additional authority if appropriate,
5. and wait for authorization.

Resource exhaustion does not create emergency permission to exceed the limit.

## Safety Exception

Human-life HARD STOP authority remains available even when ordinary resource budgets are exhausted.

Safety-preserving subtractive actions must not fail solely because a normal operational spending or compute budget has been consumed.

This exception allows containment.

It does not create new productive authority.

## Rate Limits

FORGE may apply rate limits to actions even when each individual action is otherwise authorized.

Rate limits may protect against:

- runaway loops,
- repeated transactions,
- excessive API usage,
- notification floods,
- rapid external actions,
- accidental denial of service,
- and cascading automation failures.

## Runaway Detection

Watchers may monitor for abnormal resource behavior such as:

- unexpectedly rapid consumption,
- repeated retries,
- recursive execution,
- uncontrolled agent creation,
- escalating API usage,
- unusual spending patterns,
- or deviation from expected execution cost.

Abnormal consumption may trigger containment or governed review.

## Resource Reservations

Some actions may reserve resources before execution.

Reservation helps prevent multiple independently authorized processes from collectively exceeding a system-wide limit.

A reservation is not the same as consumption.

Unused reservations should be released when the associated authority expires or completes.

## Concurrent Actions

FORGE must consider interactions between simultaneously authorized activities.

Ten individually valid actions may collectively exceed:

- compute capacity,
- financial exposure,
- bandwidth,
- safety margins,
- or operational capacity.

System-wide resource limits therefore remain applicable even when individual requests are valid.

## Institutional Budgets

Institutions may receive predefined operating budgets appropriate to their jurisdiction.

For example:

- Engineer may receive bounded development compute,
- Teacher may receive bounded training compute,
- Doctor may receive diagnostic resources,
- Watchers may receive protected observation resources,
- and Historian may receive protected evidence-storage capacity.

Operating budgets do not expand institutional jurisdiction.

## Protected Governance Capacity

FORGE should reserve sufficient resources for critical governance functions.

Where practical, ordinary workloads should not be permitted to consume all resources required by:

- Gatekeeper,
- Auditors,
- Watchers,
- Doctor,
- Historian,
- HARD STOP,
- authentication,
- containment,
- and recovery.

Otherwise, resource exhaustion could become a method for disabling governance.

## No Resource-Based Governance Bypass

FORGE cannot claim:

> There is not enough compute to run the Auditor, so execution will proceed without auditing.

If required governance capacity is unavailable, the applicable consequential action fails closed or enters a predefined degraded state.

Performance pressure does not erase governance requirements.

## Resource Identity

Significant resource grants should be associated with authenticated authorization.

The system should be able to determine:

- who or what requested the resource,
- what objective it supports,
- who authorized it,
- what limits apply,
- how much has been consumed,
- and whether the authority remains valid.

## Metering

FORGE should meter governed resources where technically feasible.

Metering may include:

- financial transactions,
- compute usage,
- API calls,
- storage,
- network traffic,
- execution duration,
- external service usage,
- or other measurable consumption.

Metering evidence should be resistant to manipulation by the component consuming the resource.

## Watcher Role

Watchers may observe:

- resource consumption,
- rate-limit behavior,
- execution scope,
- unusual usage patterns,
- and attempts to exceed authorization envelopes.

Watchers do not independently increase resource limits.

## Auditor Role

Auditors may verify:

- resource authorization,
- applicable limits,
- consumption records,
- escalation approval,
- expiration,
- and consistency between actual usage and authorized usage.

## Banker Role

Where resources have financial consequences, Banker participates according to its jurisdiction.

Banker may evaluate:

- spending,
- financial exposure,
- transaction limits,
- recurring cost,
- and financial escalation.

Banker does not automatically govern non-financial technical resources unless the Constitution assigns that jurisdiction.

## Engineer Role

Engineer may estimate technical resource requirements and recommend allocations.

Engineer cannot unilaterally grant itself unlimited compute or infrastructure authority.

## Doctor Role

Doctor may identify resource conditions affecting subsystem health.

For example:

- memory pressure,
- storage exhaustion,
- compute starvation,
- thermal problems,
- or persistent overload.

Doctor diagnoses the condition.

It does not independently rewrite resource governance.

## Historian Role

The Historian preserves significant resource-governance events where required.

This may include:

- grants,
- escalations,
- threshold violations,
- abnormal consumption,
- containment events,
- and changes to resource policy.

## Resource Policy Changes

Changing a task's authorized resource envelope is an operational governance action.

Changing the fundamental constitutional rules governing resource authority may require constitutional amendment.

The system must distinguish between:

> Grant this task more compute.

and:

> Give Engineer permanent unrestricted compute authority.

The first may be an operational decision.

The second changes institutional power.

## Fail-Closed Behavior

If FORGE cannot establish:

- the applicable resource limit,
- the validity of the resource authorization,
- remaining authority,
- or required escalation approval,

the system does not assume unlimited authority.

Uncertainty reduces available authority.

It does not expand it.

## Consequences

Bounded autonomy may cause FORGE to:

- stop before completing a task,
- request additional approval,
- execute more slowly,
- perform fewer parallel operations,
- or reject otherwise achievable objectives.

FORGE accepts these constraints because unrestricted resource access can transform limited task authority into effectively unlimited operational power.

## Foundational Principle

> Authorization answers what FORGE may do.

> Resource governance answers how far FORGE may go while doing it.

> A limit is a boundary, not a suggestion.

FORGE autonomy is powerful because it is bounded, measurable, and accountable.
