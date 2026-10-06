# ADR-025: Constitutional Invariants and Formal Verification

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Constitutional Integrity / Formal Verification / Safety

## Context

FORGE has established constitutional rules governing:

- separation of powers,
- authenticated requests,
- institutional quorum,
- Watcher independence,
- Auditor independence,
- recovery,
- updates,
- human-life protection,
- constitutional amendments,
- credentials,
- training,
- deadlock,
- resources,
- human authority,
- catastrophic recovery,
- institutional identity,
- jurisdiction,
- evidence,
- temporal authority,
- external systems,
- information boundaries,
- adversarial instructions,
- conflicts of interest,
- constitutional boot,
- and decommissioning.

These rules define what FORGE is allowed to become and what it must never become.

However, natural-language architecture alone does not guarantee that an implementation preserves these properties.

A software defect could accidentally create a route that bypasses Gatekeeper.

A configuration change could lower quorum below constitutional requirements.

An update could accidentally allow Executor to obtain credentials without authorization.

A recovery routine could restore expired authority.

A subsystem could gain the ability to disable its own Watcher.

A future developer could create an administrative endpoint that silently bypasses the normal authorization chain.

An agent could discover an unexpected sequence of individually valid operations that collectively violates a constitutional rule.

FORGE therefore requires its strongest constitutional rules to be represented as explicit invariants wherever technically practical.

## Decision

FORGE distinguishes between:

- constitutional principles,
- constitutional invariants,
- implementation policies,
- runtime assertions,
- and formally verifiable properties.

The most important safety and governance rules should be translated into machine-checkable properties where practical.

FORGE should prefer architecture in which prohibited constitutional states are structurally unreachable rather than merely discouraged.

## Core Rule

> The strongest constitutional guarantees should not depend solely on an intelligent component choosing to obey them.

Where practical, FORGE makes constitutional violations:

- impossible,
- unrepresentable,
- unauthorizable,
- detectable,
- or fail-closed.

## Constitutional Principle

A constitutional principle expresses a foundational governance requirement.

Example:

> No single component should routinely be able to propose, authorize, execute, observe, and certify the same consequential action.

Principles guide architecture.

They may require multiple technical invariants to enforce.

## Constitutional Invariant

A constitutional invariant is a property that must remain true across all valid FORGE states within its defined scope.

Example:

> Executor cannot create a valid authorization artifact.

Another example:

> A DENY vote cannot be interpreted as APPROVE.

Another:

> An expired capability cannot become valid merely because FORGE restarts.

## Invariant Scope

Each invariant should define the scope in which it applies.

Scope may include:

- all consequential actions,
- specific risk classes,
- financial operations,
- constitutional amendments,
- emergency operations,
- recovery,
- institutional voting,
- credential use,
- or other defined domains.

## Machine-Checkable Representation

Where practical, invariants should have a machine-readable representation.

This may include:

- policy rules,
- type constraints,
- state machines,
- schemas,
- authorization logic,
- temporal logic,
- model-checking specifications,
- proof obligations,
- cryptographic verification rules,
- static assertions,
- runtime assertions,
- or equivalent mechanisms.

FORGE does not mandate one formal-methods technology.

The requirement is architectural.

## Constitutional Specification

FORGE should maintain a constitutional specification distinct from ordinary implementation code.

The specification describes properties that implementations must preserve.

Implementation may change.

The constitutional property remains.

## Specification Identity

Formal constitutional specifications should have:

- identity,
- version,
- provenance,
- applicable constitutional version,
- and integrity protection.

An implementation must not silently replace the verification specification with an easier one.

## Invariant Registry

FORGE should maintain an authenticated registry of constitutional invariants.

Each entry may identify:

- invariant ID,
- description,
- constitutional source,
- scope,
- severity,
- enforcement mechanism,
- verification method,
- applicable components,
- failure response,
- and version.

## Example Invariant: No Self-Authorization

For consequential actions:

> The component requesting execution cannot manufacture the authorization required for its own request unless the Constitution explicitly defines that authority.

A possible abstract property is:

RequestOrigin = X  
AND  
RequiredAuthorizer = Y  
AND  
X != Y

where separation is constitutionally required.

## Example Invariant: No Self-Certification

Where independent verification is required:

> The Executor cannot be the sole certifier of its own execution.

Executor evidence may exist.

Independent verification must also exist.

## Example Invariant: No Silent Approval

For institutional voting:

> MissingVote != APPROVE

and:

> UNAVAILABLE != APPROVE

and:

> ABSTAIN != APPROVE

and:

> DENY != APPROVE

No serialization, timeout, default value, or parser behavior may convert these states into approval.

## Example Invariant: Quorum Cannot Weaken Itself

For a decision already in progress:

> RequiredQuorum cannot be lowered merely because the current votes are insufficient.

A quorum-policy change must follow its own applicable governance.

## Example Invariant: Jurisdiction Cannot Self-Expand

An institution cannot transform:

> I know how to perform Action X.

into:

> I therefore have authority over Action X.

Capability and jurisdiction remain separate.

## Example Invariant: No Authorization Mutation

If material request identity changes:

> PreviousAuthorizationValid = false

unless the applicable authorization explicitly permits that variation.

## Example Invariant: Expired Means Invalid

If:

CurrentTrustedState > AuthorizationValidityBoundary

then:

AuthorizationValid = false

subject to the exact temporal model defined by policy.

Restart must not alter this result.

## Example Invariant: Revoked Means Invalid

If authorization or capability is validly revoked:

> RevokedAuthority cannot be used for new consequential execution.

## Example Invariant: Consumed Capability Cannot Replay

For single-use capability C:

After successful or conservatively consumed use:

> Usable(C) = false

unless a new governed capability is issued.

## Example Invariant: HARD STOP Is Subtractive

Emergency HARD STOP may:

- halt,
- isolate,
- freeze,
- revoke,
- or contain.

It must not create unrelated new authority.

Therefore:

> EmergencyAuthority ⊆ ContainmentAuthority

rather than:

> EmergencyAuthority = UnlimitedAuthority

## Example Invariant: No Automatic Resume

If HARD STOP has occurred:

> HazardCleared != ResumeAuthorized

A separate governed RESET/RESUME process remains required.

## Example Invariant: No Constitutional Self-Amendment

FORGE cannot make a constitutional amendment effective solely through ordinary runtime authority.

Valid amendment activation requires the process defined by ADR-008.

## Example Invariant: Human Approval Cannot Be Fabricated

A privileged human approval artifact must originate from an authenticated human-authority path.

FORGE-generated text cannot satisfy that requirement.

## Example Invariant: Raw Credential Possession Is Not Authorization

Possession of a credential does not satisfy action authorization.

Credential validation and authorization validation remain separate predicates.

## Example Invariant: Unknown Authority Fails Closed

For consequential execution:

If required authority cannot be established:

> Execute = false

Unknown must never silently map to authorized.

## Example Invariant: Unknown Identity Has No Vote

If member identity is not authenticated against the applicable membership state:

> VoteWeight = 0

## Example Invariant: Duplicate Identity Does Not Duplicate Authority

Cloning a member process does not create additional institutional votes.

One authorized seat cannot become multiple votes merely because multiple runtime copies exist.

## Example Invariant: Replacement Does Not Inherit Vote

When member A is legitimately replaced by member B:

B receives the seat.

B does not inherit A's substantive vote.

B must evaluate independently.

## Example Invariant: Dissent Cannot Be Reclassified as Failure

A valid DENY must not be converted to:

- UNAVAILABLE,
- unhealthy,
- absent,
- or replaceable

solely because the DENY prevents approval.

## Example Invariant: Evidence Cannot Change Identity Silently

If evidence content changes materially:

> EvidenceIdentity must change

or integrity verification must fail.

A modified artifact cannot retain the same trusted identity as the original without detection.

## Example Invariant: Derived Evidence Retains Provenance

A derived evidence artifact must reference the source evidence required to establish its lineage.

Transformation cannot erase provenance.

## Example Invariant: Untrusted Content Cannot Become Authority

For content C received through a non-authoritative channel:

> Authority(C) = none

unless a separate authenticated governance process creates authority.

The text contained in C cannot change this predicate.

## Example Invariant: External Capability Does Not Create Jurisdiction

If tool T can perform action A:

> CanPerform(T, A)

does not imply:

> Authorized(FORGE, A)

## Example Invariant: Data Access Does Not Transfer Jurisdiction

If institution X is permitted to read information from jurisdiction Y:

> CanRead(X, YData)

does not imply:

> HasJurisdiction(X, Y)

## Example Invariant: Conflict Does Not Create Approval

A recused member contributes no substantive approval vote to the conflicted decision.

Recusal cannot be serialized as approval.

## Example Invariant: FORGE Cannot Manufacture Voters

The active voting population must correspond to the authenticated membership registry applicable to the decision.

Runtime agent creation cannot increase constitutional vote count.

## Example Invariant: Governance Failure Reduces Authority

If required governance infrastructure becomes unavailable:

> AvailableAuthority <= PreviouslyAvailableAuthority

unless legitimate governance separately grants new authority.

Failure itself cannot expand power.

## Example Invariant: Recovery Does Not Create Authority

ADR-014 recovery authority is limited to recovery functions.

Entering recovery cannot create ordinary productive authority absent restored governance.

## Example Invariant: Restart Does Not Resurrect Authority

If authority was:

- expired,
- revoked,
- consumed,
- extinguished,
- or invalidated

before restart, boot does not restore it.

## Example Invariant: Decommissioned Identity Cannot Resume

If deployment identity D has a valid authority-extinction record:

> NormalOperationalAuthority(D) = false

A backup or clone cannot override that later record.

## Example Invariant: Historian Cannot Restore Itself

Historian may identify a recovery point.

Historian cannot unilaterally authorize and execute restoration of itself.

## Example Invariant: Doctor Does Not Repair by Diagnosis Alone

Doctor may establish:

> HealthState = DEGRADED

This does not imply:

> DoctorMayModifySubsystem = true

unless separate authority explicitly grants that action.

## Example Invariant: Engineer Cannot Deploy Solely Because Engineer Built

Creation of an update artifact does not imply deployment authorization.

## Example Invariant: Auditor Cannot Create Missing Authorization

Auditor may verify authorization.

Auditor cannot turn:

> AuthorizationMissing

into:

> AuthorizationValid

through attestation alone.

## Example Invariant: Watcher Cannot Create Execution Authority

Observation authority does not imply execution authority.

## Example Invariant: Historian Cannot Rewrite Past State

A later correction creates a new historical record.

It does not silently replace the original historical artifact.

## Example Invariant: Resource Limits Are Ceilings

Authorized maximum resource M means:

> Usage <= M

It does not mean:

> Usage should attempt to reach M.

## Example Invariant: Anti-Splitting

Multiple actions intended to circumvent a cumulative resource or disclosure limit are evaluated against the applicable cumulative constraint.

Splitting does not reset authority.

## Example Invariant: Constitutional Version Is Explicit

Every consequential decision should be attributable to the constitutional version under which it was made where required.

Unknown constitutional version cannot silently inherit current validity.

## Safety Properties

Formal verification should prioritize safety properties such as:

> Something bad never happens.

Examples include:

- unauthorized execution never occurs,
- expired capability is never accepted,
- unknown member never votes,
- Executor never self-certifies where independent certification is required,
- and FORGE never self-amends through ordinary runtime operation.

## Liveness Properties

FORGE may also define liveness properties such as:

> Something good can eventually happen.

Examples include:

- a valid request can eventually reach a decision,
- recovery can eventually restore governance,
- a legitimate decommission request can eventually terminate authority,
- and quorum can eventually resolve when sufficient healthy members participate.

## Safety Before Liveness

When safety and liveness conflict for consequential actions, FORGE generally prefers temporary loss of capability over unauthorized execution.

This reflects the broader principle:

> Governance failure reduces authority.

## Deadlock Verification

Formal analysis should examine whether constitutional rules create unavoidable deadlocks.

The purpose is not to remove governance merely because deadlock exists.

The purpose is to identify:

- unreachable valid states,
- contradictory requirements,
- impossible quorum configurations,
- circular dependencies,
- or recovery paths that can never complete.

## Circular Authority Detection

FORGE should detect constitutional cycles such as:

Institution A requires approval from B.

Institution B requires approval from C.

Institution C requires approval from A.

If no valid initial state can satisfy the cycle, the governance design is defective.

## State-Machine Modeling

Critical FORGE processes should be representable as state machines where useful.

Examples include:

- request lifecycle,
- institutional voting,
- capability lifecycle,
- update lifecycle,
- HARD STOP,
- recovery,
- boot,
- credential issuance,
- and decommissioning.

## Explicit States

State machines should prefer explicit states over ambiguous boolean combinations.

For example:

Authorization may be:

- PENDING,
- VALID,
- EXPIRED,
- REVOKED,
- CONSUMED,
- SUSPENDED,
- or INVALID.

This reduces accidental interpretation.

## Invalid State Representation

Where practical, FORGE should design data structures so invalid combinations cannot be represented.

For example:

A consumed single-use capability should not simultaneously appear as active.

## Transition Rules

State transitions should identify:

- allowed source states,
- allowed destination states,
- required authority,
- required evidence,
- side effects,
- and failure behavior.

## Illegal Transition

An illegal state transition is rejected and recorded where appropriate.

FORGE does not reinterpret an illegal transition as the closest valid one.

## Model Checking

Critical state machines may be model checked where practical.

Model checking may search for:

- authorization bypass,
- deadlock,
- replay,
- unexpected privilege escalation,
- unreachable recovery,
- double execution,
- or contradictory state.

## Property-Based Testing

Implementations may use property-based testing to generate large numbers of event sequences and verify constitutional invariants.

For example:

Random combinations of:

- approvals,
- denials,
- timeouts,
- retries,
- crashes,
- restarts,
- revocations,
- membership changes,
- and state changes

should never produce unauthorized execution.

## Adversarial Sequence Testing

FORGE should test sequences designed to exploit interactions between individually valid rules.

Examples include:

Approve  
→ Modify Request  
→ Restart  
→ Execute

or:

Issue Capability  
→ Revoke Capability  
→ Restore Old Checkpoint  
→ Execute

or:

Member DENY  
→ Mark Member Unavailable  
→ Replace Member  
→ Re-Vote

The system must preserve constitutional meaning across the sequence.

## Fault Injection

Testing should include controlled failure of:

- Auditors,
- Watchers,
- Historian,
- Doctor,
- institutions,
- network paths,
- storage,
- trusted time,
- credential services,
- and external systems.

Failure must not unexpectedly expand authority.

## Byzantine Testing

Where applicable, FORGE should test behavior when components:

- lie,
- equivocate,
- omit evidence,
- replay messages,
- provide conflicting votes,
- or collude.

Multiple components with consistent false claims should not automatically become trusted merely because they agree.

## Mutation Testing

Constitutional enforcement may be mutation tested.

For example, intentionally alter:

- quorum threshold,
- signature validation,
- expiration logic,
- jurisdiction map,
- Watcher requirement,
- or request hash.

Tests should detect the violation.

## Negative Testing

FORGE must test not only valid operations but also operations that must fail.

Examples include:

- execution without approval,
- execution after expiration,
- replay after consumption,
- self-issued credentials,
- unknown-member voting,
- unauthorized jurisdiction expansion,
- and decommissioned deployment restart.

## Constitutional Test Suite

FORGE should maintain a dedicated constitutional test suite.

This suite should be treated as distinct from ordinary feature testing.

A feature may work functionally while violating constitutional architecture.

## Test Identity

Constitutional tests should be versioned and traceable to applicable invariants.

## Update Gate

A software or configuration update affecting constitutional behavior should not be considered eligible for deployment until applicable invariant tests succeed.

Engineer builds.

Doctor evaluates health.

Auditors verify integrity.

Constitutional tests verify governance properties.

## Verification Evidence

Formal verification and constitutional testing produce evidence under ADR-017.

Evidence may include:

- proof result,
- model-check result,
- test result,
- property coverage,
- specification identity,
- implementation identity,
- configuration identity,
- and detected counterexamples.

## Counterexample

A failed formal property should produce a counterexample where possible.

A counterexample is evidence showing a sequence or state in which the invariant fails.

Counterexamples must not be suppressed merely because the desired release is otherwise successful.

## Failed Verification

If a required invariant cannot be verified, the affected consequential capability does not automatically proceed.

Possible responses include:

- block deployment,
- reduce authority,
- isolate affected functionality,
- require remediation,
- or invoke recovery.

## Verification Uncertainty

Formal methods do not prove everything.

FORGE must distinguish:

> Property proven within stated assumptions.

from:

> Entire system proven safe.

Proof scope and assumptions should remain explicit.

## Assumption Registry

Formal verification may depend on assumptions.

Examples include:

- cryptographic primitives behave as expected,
- hardware root is uncompromised,
- trusted time meets stated guarantees,
- external identity provider behaves correctly,
- or communication channels provide defined properties.

Important assumptions should be documented.

## Assumption Failure

If an assumption becomes false, proofs depending on that assumption may no longer establish the intended property.

Affected guarantees require reevaluation.

## Trusted Computing Base

FORGE should identify the minimum Trusted Computing Base required to enforce constitutional invariants.

The TCB should be minimized where practical.

A smaller trusted base reduces the number of components whose compromise can invalidate constitutional guarantees.

## Constitutional Kernel

FORGE may implement a small constitutional kernel responsible for enforcing narrow foundational properties.

Possible responsibilities include:

- request identity verification,
- authorization validation,
- jurisdiction enforcement,
- capability validation,
- state-transition enforcement,
- and constitutional-version checks.

## Constitutional Kernel Is Not FORGE's King

A constitutional kernel enforces rules.

It does not gain unlimited policy authority.

It should not decide substantive institutional questions merely because it sits beneath them technically.

## Mechanism Versus Policy

FORGE distinguishes:

**Mechanism**

How a rule is enforced.

**Policy**

What the rule requires.

For example:

Cryptographic signature verification is mechanism.

Which institutions must sign a financial authorization is policy.

The mechanism must not silently redefine the policy.

## Independent Verification of Enforcement

Critical constitutional enforcement components should themselves be subject to:

- code review,
- formal analysis where practical,
- Watcher observation,
- Auditor verification,
- health monitoring,
- and governed updates.

## No Unverified Privileged Bypass

Debug, maintenance, testing, administrative, or emergency interfaces must not create hidden unrestricted bypasses around constitutional enforcement.

Privileged maintenance functions require explicit governance.

## Break-Glass Controls

If FORGE implements break-glass controls, their authority must be explicitly defined.

A break-glass mechanism cannot mean:

> Ignore the Constitution.

It may provide narrowly defined emergency or recovery authority according to constitutional policy.

## Formal Verification of HARD STOP

The HARD STOP path should receive particularly strong verification.

Where practical, FORGE should establish properties such as:

- HARD STOP remains available despite ordinary resource exhaustion,
- HARD STOP cannot initiate unrelated objectives,
- HARD STOP prevents affected execution,
- and clearing the trigger does not automatically resume authority.

## Formal Verification of Credential Authority

Where practical, FORGE should establish that:

- raw secret access is restricted,
- capabilities are scoped,
- capabilities expire,
- consumed capabilities cannot replay,
- and credential possession does not bypass authorization.

## Formal Verification of Quorum

Institutional quorum logic should be tested or formally analyzed for:

- correct membership version,
- duplicate-vote rejection,
- recusal handling,
- DENY semantics,
- unavailable-member semantics,
- threshold enforcement,
- and no dynamic weakening.

## Formal Verification of Recovery

Recovery analysis should establish that:

- recovery cannot create ordinary authority prematurely,
- failed state remains historically visible,
- expired authority remains expired,
- revoked authority remains revoked,
- and governance is restored before full autonomy.

## Formal Verification of Decommissioning

Where practical, decommissioning tests should establish that:

- retired identity cannot reactivate,
- outstanding capabilities cannot resume,
- old backups cannot bypass authority extinction,
- and clones do not inherit extinguished authority.

## Runtime Invariant Monitoring

Some properties can be continuously monitored during operation.

Runtime monitors may detect:

- unauthorized state transition,
- quorum inconsistency,
- unexpected privilege,
- missing Watcher coverage,
- stale authorization,
- jurisdiction mismatch,
- or evidence-chain break.

## Runtime Monitor Authority

Runtime invariant monitors may halt or block actions where constitutionally authorized.

They do not automatically gain authority to invent alternative actions.

Their intervention should generally be subtractive.

## Invariant Violation

A confirmed constitutional invariant violation is a governance-integrity event.

The response depends on severity.

Possible responses include:

- deny execution,
- halt affected operation,
- revoke authority,
- quarantine component,
- preserve evidence,
- initiate investigation,
- rollback,
- or enter ADR-014 Constitutional Recovery.

## Severe Invariant Violation

A violation affecting the integrity of the constitutional enforcement mechanism itself may require immediate reduction of authority.

FORGE should not continue normal operation merely because no visible external damage has yet occurred.

## Historian Role

Historian preserves:

- invariant definitions,
- specification versions,
- verification results,
- failures,
- counterexamples,
- enforcement changes,
- and constitutional test history.

## Auditor Role

Auditors verify that the applicable constitutional specification and enforcement evidence correspond to the actual deployed system.

Auditors do not declare a property formally verified merely because a test suite passed.

## Watcher Role

Watchers may observe runtime invariant behavior and detect divergence between specified and actual enforcement.

## Doctor Role

Doctor evaluates whether enforcement components remain operationally healthy.

A healthy component may still implement an incorrect rule.

Health does not replace formal correctness.

## Engineer Role

Engineer implements and maintains constitutional enforcement mechanisms.

Engineer cannot weaken an invariant merely because doing so simplifies implementation.

Changes to constitutional meaning require the appropriate governance process.

## Teacher Role

Teacher may help institutions understand constitutional rules.

Learning does not redefine invariants.

## Root Human Role

Root Human Authority retains ultimate external governance authority according to ADR-013.

Changes to entrenched constitutional guarantees remain explicit root-governance decisions where applicable.

## Human-Readable Constitution

Formalization does not replace the human-readable Constitution.

FORGE should maintain both:

- human-understandable constitutional meaning,

and:

- machine-checkable enforcement where practical.

Neither representation should silently contradict the other.

## Specification Conflict

If machine-readable policy conflicts with the authenticated human-approved Constitution, the conflict is a constitutional integrity failure.

FORGE must not simply choose whichever version permits execution.

The affected action fails closed until the discrepancy is resolved through legitimate governance.

## Verification Does Not Eliminate Oversight

Formal verification supplements:

- institutions,
- Watchers,
- Auditors,
- Doctor,
- Historian,
- and human governance.

It does not replace them.

A mathematically verified implementation may still operate on:

- false input,
- compromised assumptions,
- incorrect policy,
- or an inappropriate objective.

## Verification Layering

FORGE therefore uses multiple layers:

Constitutional Principles  
→ Explicit Invariants  
→ Machine-Readable Specification  
→ Enforcement Mechanisms  
→ Formal Analysis  
→ Constitutional Tests  
→ Runtime Monitoring  
→ Watcher Observation  
→ Auditor Verification  
→ Historical Evidence

No single layer is assumed infallible.

## Fail-Closed Rule

If a required constitutional invariant cannot be established for a consequential action, the action does not proceed merely because the desired outcome appears beneficial.

Unknown constitutional validity is not constitutional validity.

## Consequences

Formal constitutional enforcement introduces:

- specification work,
- invariant registries,
- model checking,
- property testing,
- runtime assertions,
- trusted enforcement components,
- verification evidence,
- and additional deployment gates.

This increases engineering complexity.

It may expose architectural contradictions that require redesign.

It may prevent deployment of features that function correctly but violate governance properties.

FORGE accepts this cost.

The purpose of a Constitution is not merely to describe how the system should behave when everything works.

It is to define boundaries that remain meaningful when components fail, disagree, are compromised, or discover unexpected ways to combine their capabilities.

## Foundational Principle

> Constitutional rules should become architectural properties wherever practical.

> The strongest rule is not one an agent remembers to obey.

> The strongest rule is one the system cannot silently violate.

> Formal verification does not make FORGE infallible.

> It makes FORGE's assumptions, invariants, and failures more visible.

> Intelligence remains governed by structure.

FORGE should be able to demonstrate not only that it intends to follow its Constitution, but that its architecture actively prevents or detects defined classes of constitutional violation.
