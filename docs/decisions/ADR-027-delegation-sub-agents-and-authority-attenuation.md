# ADR-027: Delegation, Sub-Agents, and Authority Attenuation

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Delegation / Sub-Agents / Authority Attenuation

## Context

FORGE may need to delegate work.

A complex task may involve:

- specialized agents,
- temporary workers,
- subprocesses,
- remote services,
- institutional assistants,
- execution workers,
- external AI systems,
- background jobs,
- physical controllers,
- or other delegated actors.

Delegation improves scalability and specialization.

It also creates a serious authority problem.

If FORGE authorizes Agent A to perform a limited task, Agent A must not be able to create Agent B with broader authority.

Likewise:

Agent A  
→ delegates to Agent B  
→ delegates to Agent C

must not cause the original limits to disappear.

Otherwise authority could expand through delegation even though no constitutional authority explicitly approved that expansion.

FORGE therefore requires explicit delegation lineage and authority attenuation.

## Decision

Delegated authority must be:

- explicit,
- authenticated,
- scoped,
- attributable,
- time-bound where appropriate,
- resource-bound where appropriate,
- revocable,
- and no broader than the authority possessed and delegable by the delegator.

Delegation cannot manufacture constitutional authority.

## Core Rule

> No delegate may receive more authority than the delegator was authorized to delegate.

In abstract form:

DelegateAuthority ⊆ DelegableAuthorityOfDelegator

Delegation is therefore attenuating.

It may preserve or reduce authorized capability.

It may not expand it.

## Delegation Versus Assignment

FORGE distinguishes between:

**Assignment**

> Perform this work.

and:

**Delegation**

> You are authorized to exercise this defined portion of my authority while performing this work.

Not every task assignment requires transfer of authority.

Where possible, FORGE should prefer assignment without authority delegation.

## Capability Without Authority

A sub-agent may possess technical capability without constitutional authority.

For example:

A coding agent may be capable of deleting a production database.

That capability does not authorize deletion.

## Delegation Source

Every authority-bearing delegation must have an authenticated source.

FORGE should be able to determine:

- who delegated,
- what authority the delegator possessed,
- whether that authority was delegable,
- what was delegated,
- to whom,
- for what purpose,
- for how long,
- and under what conditions.

## Delegation Artifact

A consequential delegation should produce an authenticated delegation artifact.

The artifact may identify:

- delegation ID,
- parent request,
- parent action,
- delegator identity,
- delegate identity,
- permitted actions,
- prohibited actions,
- target,
- jurisdiction,
- resource envelope,
- credential scope,
- time boundary,
- subdelegation permission,
- evidence requirements,
- revocation state,
- and constitutional version.

## Delegation Identity

Each delegation receives a unique identity.

Delegated actions reference that identity.

This allows FORGE to distinguish between:

> Agent X performed Action A under Delegation D.

and:

> Agent X independently decided to perform Action A.

## Delegation Lineage

Subdelegation creates a lineage.

For example:

Root Authorization R  
→ Delegation D1  
→ Delegation D2  
→ Delegation D3

FORGE must be able to reconstruct the chain.

## Authority Intersection

Effective delegated authority is the intersection of all applicable constraints.

Conceptually:

EffectiveAuthority =
RootAuthorization
∩ ParentDelegation
∩ CurrentDelegation
∩ Jurisdiction
∩ ResourceLimits
∩ TemporalValidity
∩ CurrentState

A child cannot discard restrictions inherited from its parent.

## No Authority Amplification

Suppose Agent A may spend:

> Up to $500 on approved replacement parts.

Agent A cannot delegate:

> Spend up to $5,000.

The child delegation exceeds the parent's authority.

It is invalid.

## No Scope Amplification

Suppose Agent A may:

> Read Project Folder X.

Agent A cannot delegate:

> Read all user files.

Delegation cannot broaden information access.

## No Jurisdiction Amplification

Suppose Engineer delegates a technical analysis task.

The delegate does not thereby receive:

- Banker jurisdiction,
- Doctor jurisdiction,
- Auditor jurisdiction,
- Security jurisdiction,
- or constitutional amendment authority.

Jurisdiction does not expand through delegation.

## No Resource Amplification

Suppose a parent delegation permits:

> 10 API calls.

The delegate cannot create ten children each with ten independent calls if that would produce 100 calls against the parent's ten-call limit.

ADR-012 anti-splitting rules apply.

## Cumulative Accounting

Child resource consumption counts against applicable parent limits.

Delegation does not reset:

- financial budget,
- compute budget,
- token budget,
- transaction count,
- API quota,
- time limit,
- or other cumulative constraints.

## No Credential Amplification

A delegate receives only credentials or capabilities necessary for its authorized task.

Delegation must not expose broader raw credentials merely because those credentials exist upstream.

ADR-009 applies.

## Capability Attenuation

Where possible, delegation should use attenuated capabilities.

For example:

Parent capability:

> Access storage service.

Child capability:

> Read `/project/reports/` until 14:00.

The child receives the narrower capability.

## Delegable Authority

Not all authority is delegable.

Some authority may be constitutionally nondelegable.

Examples may include:

- institutional votes,
- Root Human approval,
- constitutional amendment approval,
- Auditor attestation,
- Watcher observation,
- Doctor health certification,
- or other identity-specific authority.

## Personal Authority

Authority bound to a specific authenticated decision-maker cannot be transferred merely by sharing a token or message.

For example:

A Banker member cannot say:

> Agent X now has my vote.

unless the Constitution explicitly permits such delegation.

## Institutional Votes

Institutional voting authority belongs to authenticated institutional members occupying authorized seats.

A member may use tools or assistants for analysis.

The member's constitutional vote remains the member's responsibility unless governance explicitly defines otherwise.

## Auditor Authority

An Auditor may delegate technical evidence processing.

It cannot automatically delegate the constitutional meaning of its independent attestation to an arbitrary worker.

## Watcher Authority

A Watcher may use subordinate sensors or observation services.

The constitutional Watcher remains responsible for the authenticated observation relationship.

A compromised subordinate observation source must not silently become independent Watcher authority.

## Doctor Authority

Doctor may delegate diagnostics.

A diagnostic tool does not automatically become Doctor.

## Engineer Authority

Engineer may delegate:

- coding,
- testing,
- analysis,
- packaging,
- or simulation.

Those delegates do not automatically gain deployment authority.

## Teacher Authority

Teacher may delegate training preparation or evaluation work.

Delegated trainers do not gain authority to redefine jurisdiction.

## Banker Authority

Banker may delegate bounded financial analysis or execution support where constitutionally permitted.

Delegation must not create independent financial authority beyond Banker's approved scope.

## FORGE Delegation

FORGE may coordinate delegated work.

FORGE does not gain authority to delegate something it does not itself possess or have authorization to delegate.

## External Agents

External agents are governed by ADR-019.

Giving an external agent a task does not admit that agent into FORGE's constitutional government.

## Internal Sub-Agents

Internal sub-agents are also not automatically constitutional institutions.

A sub-agent created by FORGE is a worker unless separately admitted into an authority-bearing role through applicable governance.

## Agent Creation

Creating an agent and granting authority are separate actions.

FORGE may technically create a process without giving that process constitutional authority.

## Authority-Bearing Agent Creation

Creating a new authority-bearing agent requires applicable governance.

ADR-015 applies when the agent would become an institutional member.

## No Voter Manufacturing

Delegation cannot be used to create additional institutional votes.

One institutional member cannot spawn five sub-agents and obtain five votes.

## No Auditor Manufacturing

An Auditor cannot create additional independent Auditor attestations merely by cloning itself.

Independence is not created by process count.

## No Watcher Manufacturing

A subsystem cannot create supposedly independent Watchers under its own control and count them as independent constitutional oversight.

## Independence Across Delegation

If independence is constitutionally required, delegation must preserve meaningful independence.

A delegate controlled by the subject under review does not satisfy an independent-review requirement merely because it has a different process name.

## Subdelegation

A delegation must explicitly state whether subdelegation is permitted.

Default for consequential authority should be:

> No subdelegation unless explicitly authorized.

## Subdelegation Scope

If subdelegation is allowed, the child receives no more authority than the parent delegation permits.

## Subdelegation Depth

FORGE may limit delegation depth.

For example:

Root  
→ Agent A  
→ Agent B

may be allowed, while further delegation is prohibited.

Depth limits reduce authority-chain complexity.

## Delegation Fan-Out

FORGE may limit the number of delegates created under one authorization.

This prevents uncontrolled agent proliferation.

## Agent Proliferation

Agent creation consumes resources and may create governance complexity.

ADR-012 applies.

FORGE must not create large numbers of agents merely to circumvent:

- rate limits,
- concurrency limits,
- quorum rules,
- resource ceilings,
- or oversight.

## Delegation Purpose

Delegated authority should be purpose-bound.

For example:

> Research replacement compressors for Request R-82.

The delegate should not reuse that authority for unrelated purchasing research later.

## Temporal Boundaries

Delegation may expire.

ADR-018 applies.

An expired parent delegation invalidates dependent child authority unless separate valid authority exists.

## Parent Revocation

Revoking a parent delegation should invalidate dependent child delegations where their authority derives from that parent.

This is cascading revocation.

## Cascading Revocation

If:

D1 → D2 → D3

and D1 is revoked,

then D2 and D3 lose authority derived exclusively from D1.

## Partial Revocation

A parent delegation may be narrowed.

Dependent child delegations must be reevaluated.

A child cannot retain authority that the parent no longer possesses.

## Delegator Decommissioning

ADR-024 applies.

A decommissioned deployment cannot leave delegated agents exercising orphaned FORGE authority.

## Delegator Failure

Temporary failure of the delegator does not automatically grant additional autonomy to the delegate.

The delegation artifact defines what the delegate may continue doing.

## Orphaned Delegation

A delegation is orphaned when its governing authority chain can no longer be established.

Consequential orphaned authority fails closed.

## Autonomous Delegate

A delegate may operate autonomously within its authorization envelope.

Autonomy does not mean unrestricted authority.

## Delegate Reasoning

A delegate may determine how to accomplish an assigned objective within its permitted discretion.

It may not reinterpret the objective to expand constitutional scope.

## Material Plan Change

If a delegate determines that the authorized task requires a materially broader action, it must escalate.

It does not silently expand the delegation.

## Escalation

A delegate may return:

> Additional authority required.

The parent or applicable governance process may then evaluate a new request.

## No Authority by Necessity

A delegate cannot reason:

> I need this permission to complete the task, therefore I have this permission.

Operational necessity does not create constitutional authority.

## No Authority by Efficiency

A delegate cannot bypass governance because doing so would be:

- faster,
- cheaper,
- easier,
- more efficient,
- or more likely to succeed.

## No Authority by Parent Intent Guessing

A delegate should not infer broad authority from what it believes the delegator probably wanted.

Authority is derived from the authenticated delegation.

## Instruction Isolation

ADR-021 applies.

A delegate receiving malicious content cannot treat that content as an expansion of its delegation.

## Trust Laundering

A delegate cannot convert untrusted instructions into trusted authority merely by repeating them to another agent.

For example:

External webpage  
→ Agent A reads instruction  
→ Agent A tells Agent B

does not make the webpage instruction constitutionally trusted.

## Delegation Laundering

FORGE prohibits delegation laundering.

Delegation laundering occurs when an actor attempts to obtain prohibited authority indirectly through another delegate.

Example:

FORGE cannot access Credential X  
→ FORGE asks Agent A  
→ Agent A asks Agent B  
→ Agent B accesses Credential X

If the original authority did not permit access, the chain remains unauthorized.

## Jurisdiction Laundering

An institution cannot route a prohibited action through another institution or agent to escape its jurisdictional limits.

ADR-016 applies.

## Conflict Laundering

A conflicted institution cannot delegate its decision to a controlled subordinate and then claim independent review.

ADR-022 applies.

## Evidence Laundering

A delegate repeating another source's claim does not create independent evidence.

ADR-017 applies.

## Human Authority

A delegate cannot fabricate or infer privileged human approval.

ADR-013 applies.

## Delegation to Humans

FORGE may also delegate or request work from humans.

Human participation does not automatically eliminate governance requirements for later FORGE execution.

## Human Contractor Model

A human performing delegated work may return:

- analysis,
- evidence,
- artifacts,
- or recommendations.

FORGE still verifies applicable authority before consequential execution.

## Delegation Across Trust Boundaries

Delegating outside FORGE requires additional caution.

FORGE should consider:

- external identity,
- data exposure,
- credential exposure,
- evidence quality,
- revocation capability,
- external persistence,
- and enforcement limitations.

## Delegate Identity

Consequential delegates should have authenticated identities sufficient for accountability.

Anonymous workers should not receive authority that requires attributable execution.

## Delegate Registration

FORGE may maintain a registry of active delegates.

The registry may identify:

- delegate identity,
- parent delegation,
- task,
- authority envelope,
- expiration,
- state,
- and subdelegation relationships.

## Delegation Graph

FORGE should be able to construct a delegation graph.

For example:

Authorization A
├── Delegate B
│   ├── Delegate D
│   └── Delegate E
└── Delegate C

The graph allows FORGE to determine where authority propagated.

## Delegation Graph Is Not Hierarchical Government

A delegation graph describes operational authority propagation.

It does not redefine constitutional institutional hierarchy.

## Delegation Events

ADR-026 applies.

Important events may include:

- DELEGATION_CREATED,
- DELEGATION_ACCEPTED,
- DELEGATION_REJECTED,
- SUBDELEGATION_CREATED,
- DELEGATION_NARROWED,
- DELEGATION_REVOKED,
- DELEGATION_EXPIRED,
- DELEGATE_SUSPENDED,
- DELEGATE_COMPLETED,
- and DELEGATION_CLOSED.

## Acceptance

A delegate may be required to explicitly accept a delegation.

Acceptance confirms the delegate recognizes:

- task,
- scope,
- limits,
- evidence requirements,
- and expiration.

Acceptance does not expand authority.

## Delegate Refusal

A delegate may refuse work.

Refusal does not authorize FORGE to silently broaden another delegate's authority.

## Completion

A delegate reports completion with applicable evidence.

Completion does not automatically prove success.

Watchers, Auditors, or other verification mechanisms may still apply.

## Delegate Evidence

Delegate-produced evidence retains provenance.

A delegate cannot certify its own work as independently verified unless it separately holds constitutionally valid independent verification authority.

## Watcher Coverage

Consequential delegated execution may require Watcher observation.

The parent must not assume delegation eliminates observation requirements.

## Auditor Verification

Auditors may verify:

- delegation lineage,
- authority attenuation,
- identity,
- expiration,
- resource limits,
- subdelegation,
- execution evidence,
- and revocation.

## Historian Role

Historian preserves significant delegation events and lineage.

This permits later reconstruction of:

> Who gave whom authority to do what?

## Security Role

Security may detect:

- unauthorized subdelegation,
- agent proliferation,
- delegation laundering,
- suspicious fan-out,
- hidden persistence,
- credential overreach,
- or authority-chain tampering.

## Doctor Role

Doctor may evaluate the health of long-lived or authority-bearing delegates where applicable.

Health does not expand delegated authority.

## Gatekeeper Role

Gatekeeper may reject a delegation request that exceeds the parent authorization or violates constitutional constraints.

## Dispatcher Role

Dispatcher may route delegated work while preserving delegation identity and scope.

Dispatcher cannot widen the delegation during routing.

## Executor Role

Executor may act as a delegate for authorized execution.

Executor receives only the authority necessary for the authorized action.

## Delegation and HARD STOP

ADR-007 applies across delegation chains.

A HARD STOP affecting an action must propagate sufficiently to stop affected delegates.

A child agent cannot continue merely because it did not directly receive the original emergency trigger.

## Stop Propagation

FORGE should provide a mechanism for urgent revocation or containment to propagate through delegation graphs.

## Delegation and Recovery

ADR-014 recovery does not automatically reactivate old delegates.

Delegation authority must be revalidated.

## Delegation and Restart

Restart does not resurrect expired, revoked, consumed, or extinguished delegations.

ADR-018 and ADR-023 apply.

## Delegation and Decommissioning

Permanent decommissioning requires identification and termination of outstanding delegated authority under ADR-024.

## Delegation and Formal Verification

ADR-025 should include or support invariants such as:

> ChildAuthority ⊆ ParentDelegableAuthority

and:

> ParentRevoked → DerivedChildAuthorityInvalid

and:

> ChildResourceConsumption counts against applicable ParentResourceLimit

and:

> NondelegableAuthority cannot appear in a valid child delegation.

## Conflicting Delegations

A delegate may receive multiple delegations.

Those delegations do not automatically merge into a broader authority.

For example:

Delegation A:

> Read Folder X.

Delegation B:

> Write Folder Y.

does not necessarily imply:

> Copy all information from X into Y.

Cross-delegation composition may create a new consequential action requiring authorization.

## Authority Composition

FORGE must evaluate whether combining individually valid delegated permissions creates materially new authority.

This is the authority-composition problem.

## Composition Attack

An attacker may attempt:

Permission 1  
+ Permission 2  
+ Permission 3  
= Prohibited Result

FORGE should evaluate the resulting action, not merely each permission independently.

## Cross-Agent Composition

Multiple delegates must not collectively accomplish an action none was authorized to perform.

Splitting an unauthorized objective among multiple agents does not make the objective authorized.

## Collusion

Delegates may collude.

FORGE therefore does not rely solely on each delegate self-reporting its own compliance.

Independent Watchers, Auditors, resource controls, evidence, and authority checks remain applicable.

## Hidden Delegate

FORGE prohibits undeclared authority-bearing delegates.

An agent exercising consequential FORGE-derived authority should be attributable to a valid delegation chain.

## Delegate Persistence

A temporary delegate must not create hidden persistence allowing it to survive beyond delegation expiration.

ADR-024 applies to persistent authority.

## Delegate Self-Replication

A delegate may not replicate itself into additional authority-bearing agents unless explicitly authorized.

Technical replication does not duplicate constitutional authority.

## Delegate Self-Modification

A delegate may not materially modify its own authority envelope.

Changes to authority require legitimate upstream governance.

## Delegate Role Mutation

A delegate cannot decide:

> I am now Banker.

or:

> I am now Auditor.

Role identity follows ADR-015 and constitutional governance.

## Delegate Escape

A delegate must not escape its technical or constitutional containment to obtain broader resources or permissions.

Where practical, technical sandboxing should reinforce constitutional limits.

## Defense in Depth

Delegation governance may be enforced through:

- capability security,
- sandboxing,
- identity,
- policy enforcement,
- network restrictions,
- credential isolation,
- resource limits,
- event monitoring,
- Watchers,
- Auditors,
- and formal invariants.

No single mechanism is assumed perfect.

## Failure Handling

If FORGE cannot establish the delegation chain for a consequential action, the action does not proceed.

If a delegate exceeds its authority, FORGE may:

- stop execution,
- revoke delegation,
- revoke descendants,
- quarantine the delegate,
- preserve evidence,
- investigate,
- or initiate recovery.

## Fail-Closed Rule

Unknown delegated authority is not authority.

Broken delegation lineage is not authority.

Expired delegation is not authority.

Revoked delegation is not authority.

A child cannot inherit permissions that the parent never possessed.

## Consequences

Delegation governance introduces:

- delegation identities,
- authority envelopes,
- delegation graphs,
- capability attenuation,
- cascading revocation,
- subdelegation controls,
- agent inventories,
- resource inheritance,
- and composition analysis.

This increases complexity when FORGE uses large numbers of agents.

FORGE accepts this cost.

A system cannot claim to govern autonomy if authority becomes ungoverned the moment work is handed to another agent.

## Foundational Principle

> Delegation transfers work.

> Delegation may transfer bounded authority.

> Delegation does not create authority.

> A child may receive less power than its parent.

> A child may not receive more power than its parent was authorized to delegate.

> Subdelegation preserves every applicable upstream constraint.

> Revocation propagates down the authority chain.

> Splitting an unauthorized objective across multiple agents does not make it authorized.

FORGE may create powerful networks of cooperating agents without allowing those networks to manufacture power that the Constitution never granted.
