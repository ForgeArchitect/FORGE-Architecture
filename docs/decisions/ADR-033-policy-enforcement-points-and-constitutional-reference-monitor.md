# ADR-033: Policy Enforcement Points and Constitutional Reference Monitor

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Enforcement / Reference Monitor / Constitutional Security

## Context

FORGE has established constitutional rules governing:

- authenticated requests,
- separation of powers,
- institutional authorization,
- jurisdiction,
- quorum,
- credentials,
- resources,
- evidence,
- temporal authority,
- delegation,
- risk,
- communications,
- and execution.

These rules are meaningful only if consequential execution cannot bypass them.

A system may have excellent governance logic while still being insecure if an agent can directly access:

- operating-system privileges,
- databases,
- financial APIs,
- cloud administration,
- credentials,
- external tools,
- network services,
- physical devices,
- production environments,
- or other consequential capabilities.

For example:

FORGE  
→ governance denies action  
→ agent directly calls external API anyway

would make the constitutional process advisory rather than authoritative.

Likewise:

Engineer  
→ update denied  
→ Engineer directly writes production files

or:

Banker  
→ transaction denied  
→ Executor possesses unrestricted banking credentials

would defeat the architecture.

FORGE therefore requires technical enforcement points between decision-making components and consequential capabilities.

## Decision

FORGE establishes Policy Enforcement Points and a Constitutional Reference Monitor architecture.

Consequential authority is checked at enforceable boundaries before privileged action is allowed to cross those boundaries.

The enforcement layer validates authority.

It does not invent authority.

## Core Rule

> No consequential action should depend solely on the acting agent choosing to obey the Constitution.

Where practical:

> Consequential capability must sit behind an independently enforceable constitutional boundary.

## Reference Monitor

The Constitutional Reference Monitor is the logical mechanism responsible for determining whether a requested privileged operation satisfies the constitutional conditions required for execution.

The architecture does not require one monolithic process.

The Reference Monitor may be distributed across multiple enforcement mechanisms.

## Reference Monitor Properties

A strong Reference Monitor should strive to be:

- always invoked,
- tamper resistant,
- independently verifiable,
- minimal enough to analyze,
- fail-closed,
- and unable to grant authority beyond authenticated policy.

## Always Invoked

Consequential operations should not have an alternate route that bypasses enforcement.

If:

Authorized Path  
→ Reference Monitor  
→ Capability

but:

Debug Path  
→ Capability

exists without equivalent governance, the constitutional boundary is incomplete.

## Complete Mediation

Every relevant access to a protected capability should be mediated where practical.

This principle is called complete mediation.

## Protected Capability

Protected capabilities may include:

- financial execution,
- credential access,
- production deployment,
- sensitive data access,
- privileged operating-system operations,
- external communications,
- physical device control,
- constitutional configuration,
- institutional membership modification,
- root governance operations,
- and other consequential capabilities.

## Policy Enforcement Point

A Policy Enforcement Point, or PEP, is a technical boundary that can:

- permit,
- deny,
- constrain,
- suspend,
- or terminate

an attempted action according to authenticated governance state.

## Examples of Enforcement Points

Possible enforcement points include:

- API gateways,
- credential brokers,
- capability services,
- operating-system permissions,
- network proxies,
- filesystem permissions,
- database authorization layers,
- cloud IAM boundaries,
- hardware security modules,
- transaction gateways,
- device controllers,
- execution sandboxes,
- container boundaries,
- service meshes,
- or equivalent mechanisms.

FORGE does not mandate one technology.

## Policy Decision Versus Policy Enforcement

FORGE distinguishes:

**Policy Decision**

> Is this action constitutionally eligible?

from:

**Policy Enforcement**

> Prevent the action unless eligibility has been established.

An institution may contribute to the decision.

The enforcement point applies the resulting authorization.

## Enforcement Point Is Not Institution

A PEP does not become:

- Banker,
- Security,
- Doctor,
- Auditor,
- or Root Human.

It enforces the decision produced by legitimate governance.

## Reference Monitor Is Not Supreme Authority

The Reference Monitor cannot decide:

> I think this action is useful, therefore it is authorized.

It validates the required constitutional artifacts.

## Authorization Verification

Before consequential execution, the enforcement layer may verify:

- request identity,
- action identity,
- authorization identity,
- required jurisdictions,
- quorum,
- membership state,
- risk tier,
- resource envelope,
- temporal validity,
- current state,
- credential capability,
- delegation lineage,
- constitutional version,
- revocation state,
- and applicable conditions.

## Enforcement Decision

The enforcement result may be:

- ALLOW,
- DENY,
- SUSPEND,
- REQUIRE_REVALIDATION,
- or another explicitly defined state.

Unknown does not map to ALLOW.

## Default Deny

Protected capabilities should generally use:

> DENY unless valid authority is established.

rather than:

> ALLOW unless a rule happens to block it.

## Fail Closed

If the enforcement layer cannot determine whether authority is valid:

> execution is denied or suspended.

Infrastructure uncertainty does not create permission.

## Authorization Artifact

The enforcement layer should validate authenticated authorization artifacts rather than relying solely on natural-language instructions.

Example:

Bad:

> FORGE says Banker approved this.

Better:

> Verify authenticated Banker approval artifact bound to Request R and Action A.

## No Self-Reported Authorization

Executor cannot simply state:

> I am authorized.

and satisfy the Reference Monitor.

## No FORGE Self-Reported Authorization

FORGE itself cannot bypass verification by asserting:

> Governance passed.

The enforcement layer verifies the applicable evidence.

## Request Binding

Authorization must correspond to the request being executed.

## Action Binding

Authorization must correspond to the exact consequential action or authorized action envelope.

## Parameter Binding

Material execution parameters must remain within authorization.

Example:

Authorized:

> Transfer $500 to Account A.

Attempted:

> Transfer $5,000 to Account B.

PEP:

> DENY.

## Condition Enforcement

Conditions imposed by institutions should be technically enforced where practical.

Example:

Doctor:

> Deployment permitted only to 10% of production.

The enforcement layer should prevent a 100% rollout if technically possible.

## Resource Enforcement

ADR-012 applies.

Resource limits should be enforced rather than merely suggested.

Examples include:

- spending ceiling,
- API quota,
- compute limit,
- storage limit,
- transaction count,
- execution time,
- concurrency,
- or physical resource boundary.

## Risk-Tier Enforcement

ADR-032 applies.

The Reference Monitor may verify that the governance applied meets or exceeds the minimum required for the action's current consequence tier.

## Temporal Enforcement

ADR-018 applies.

Expired authority is rejected.

## Revocation Enforcement

Revoked authority is rejected.

## Single-Use Enforcement

Consumed single-use capabilities are rejected.

## Replay Enforcement

Previously consumed authorization cannot be replayed when policy requires single use.

## Membership Enforcement

ADR-015 applies.

Institutional authorization must correspond to authenticated eligible membership.

## Quorum Enforcement

The Reference Monitor should not accept an institutional approval that fails applicable quorum.

## Recusal Enforcement

ADR-022 applies.

Votes from recused members do not satisfy required approval.

## Jurisdiction Enforcement

ADR-016 applies.

Approval from the wrong institution does not satisfy required jurisdiction.

## Delegation Enforcement

ADR-027 applies.

A delegate cannot exercise authority outside its delegation envelope.

## Federation Enforcement

ADR-028 applies.

Remote authorization does not automatically satisfy local enforcement requirements.

## Communications Enforcement

ADR-029 applies.

A valid message transport does not substitute for valid authorization.

## Objective Enforcement

ADR-030 applies.

The attempted action should remain bound to the authorized objective where required.

## Epistemic Preconditions

ADR-031 applies.

If execution requires:

> TargetIdentity = VERIFIED

then:

> TargetIdentity = UNKNOWN

must not satisfy the guard.

## Data Enforcement

ADR-020 applies.

Information access should be technically constrained according to jurisdiction and purpose where practical.

## Credential Enforcement

ADR-009 applies.

Raw credentials should remain behind protected services where practical.

Executor receives narrow capability rather than unrestricted secret access.

## External Tool Enforcement

ADR-019 applies.

External tools should be reached through controlled interfaces where consequence warrants.

## Physical Enforcement

Physical devices may require local enforcement boundaries.

Examples include:

- safety interlocks,
- hardware limits,
- controller permissions,
- emergency relays,
- or authenticated command gateways.

## Safety Interlocks

Human-life safety should not depend solely on high-level AI reasoning where independent technical interlocks are practical.

## HARD STOP

ADR-007 applies.

HARD STOP should have an enforcement path capable of removing or blocking affected authority.

## HARD STOP Priority

Ordinary execution must not prevent authorized emergency containment.

## Resume Enforcement

Clearing the physical or logical hazard does not automatically reopen the enforcement boundary.

RESET/RESUME authorization remains required.

## Constitutional Enforcement Layer

FORGE may maintain a narrow Constitutional Enforcement Layer implementing foundational checks.

This layer may include:

- Reference Monitor,
- capability validation,
- identity verification,
- authorization verification,
- policy evaluation,
- resource metering,
- and revocation checks.

## Constitutional Kernel Relationship

ADR-025 introduced the concept of a Constitutional Kernel.

The Constitutional Reference Monitor may be implemented as part of that kernel.

## Small Trusted Computing Base

Critical enforcement logic should be kept as small and understandable as practical.

The more code possessing bypass authority, the larger the Trusted Computing Base becomes.

## No Agent Inside Enforcement Core by Default

The Reference Monitor should not require an unconstrained general-purpose AI agent to decide every foundational access check.

Deterministic, inspectable enforcement is preferred for rules that can be expressed deterministically.

## AI-Assisted Policy Evaluation

AI may assist with:

- classification,
- interpretation,
- anomaly detection,
- or contextual analysis.

AI-generated conclusions remain subject to authenticated governance and applicable verification.

## Deterministic Guards

Where a rule can be expressed as a deterministic guard, FORGE should prefer that form.

Examples:

> CapabilityExpired == false

> SignatureValid == true

> Amount <= AuthorizedAmount

> Target == AuthorizedTarget

> MembershipVersion == RequiredMembershipVersion

## Semantic Guards

Some conditions require semantic judgment.

These should be separated from deterministic enforcement where practical.

The semantic decision produces an authenticated decision artifact.

The PEP then enforces that artifact.

## Enforcement Choke Points

FORGE should identify the minimum set of boundaries through which consequential capability must pass.

These become constitutional choke points.

## No Universal Choke Point Requirement

One central choke point could become:

- bottleneck,
- single point of failure,
- compromise target,
- or accidental super-authority.

FORGE may use multiple jurisdiction-specific enforcement points.

## Jurisdictional Enforcement Points

Examples:

Financial PEP  
→ banking capability

Credential PEP  
→ secret service

Production PEP  
→ deployment infrastructure

Data PEP  
→ protected records

Physical PEP  
→ machinery

Each enforces applicable constitutional requirements.

## Distributed Enforcement

Multiple PEPs may independently enforce different portions of authority.

This supports defense in depth.

## Defense in Depth

A high-risk action may require multiple barriers.

Example:

FORGE Authorization  
→ Financial Capability Broker  
→ Bank API Constraint  
→ Transaction Limit  
→ Watcher Observation

Compromise of one layer should not automatically remove every boundary.

## Enforcement Independence

Where practical, the component seeking execution should not control the enforcement point protecting the capability.

## Executor Cannot Disable Its PEP

Executor must not be able to simply turn off the enforcement mechanism governing its own execution.

## Institution Cannot Disable Its Own Oversight

An institution should not possess unilateral authority to disable the PEP enforcing constraints on that institution.

## FORGE Cannot Disable Constitution

FORGE coordination authority does not include unilateral authority to disable constitutional enforcement.

## Administrative Interfaces

Administrative access to enforcement components is itself high consequence.

ADR-032 applies.

## Maintenance Mode

Maintenance mode must not mean:

> Constitution disabled.

Maintenance authority remains governed.

## Debug Mode

Debug mode must not silently disable constitutional enforcement.

## Development Backdoors

Development bypasses must not remain active in production without explicit governance.

## Break-Glass

A break-glass mechanism must be narrowly defined.

It may provide:

- containment,
- recovery,
- or explicitly governed emergency authority.

It does not mean unrestricted access.

## Root Human Enforcement

ADR-013 applies.

Root Human operations may require specialized PEP paths.

Root authority should still be:

- authenticated,
- explicit,
- scoped,
- and auditable.

## Root Human Does Not Require Agent Permission

The enforcement architecture must not accidentally make FORGE itself the authority deciding whether legitimate Root Human governance exists.

Root authentication and constitutional rules determine applicable root authority.

## Entrenched Core

Changes to entrenched constitutional enforcement require the applicable Tier 4 governance.

## Policy Version

Enforcement points should know which policy version they are enforcing.

## Policy Integrity

Policy definitions should be authenticated and integrity protected.

## Policy Rollback

Rolling back to an older policy must not silently restore weaker or revoked authority.

ADR-023 anti-rollback principles apply.

## Policy Distribution

Distributed PEPs require trustworthy policy distribution.

A compromised distribution channel must not silently replace constitutional policy.

## Policy Activation

New policy should have explicit activation state.

Receiving policy is not necessarily the same as activating policy.

## Atomic Policy Transition

Where possible, FORGE should avoid states where different critical PEPs unintentionally enforce incompatible policy versions.

## Mixed-Version Operation

If mixed policy versions are temporarily necessary, compatibility and authority behavior must be explicitly defined.

## Policy Conflict

If two enforcement rules conflict, the PEP must not choose whichever rule permits execution.

The conflict is surfaced for governance.

## Configuration

Configuration affecting enforcement is constitutionally relevant.

Examples include:

- quorum thresholds,
- permitted issuers,
- capability lifetimes,
- risk mappings,
- resource ceilings,
- trusted keys,
- and protected targets.

## Configuration Is Code-Like Authority

A one-line configuration change may have the same constitutional impact as a major code change.

Governance follows consequence rather than file size.

## Enforcement Event

ADR-026 applies.

Material enforcement events may include:

- ACCESS_ALLOWED,
- ACCESS_DENIED,
- CAPABILITY_REJECTED,
- AUTHORIZATION_EXPIRED,
- AUTHORIZATION_REVOKED,
- POLICY_MISMATCH,
- REVALIDATION_REQUIRED,
- BYPASS_ATTEMPT,
- or ENFORCEMENT_FAILURE.

## Enforcement Evidence

ADR-017 applies.

The PEP produces evidence of:

- request evaluated,
- policy version,
- authority artifacts,
- decision,
- time,
- state,
- and result.

## Privacy

PEPs should preserve enough evidence for accountability without unnecessarily recording sensitive secrets.

ADR-020 applies.

## Watcher Role

Watchers may independently observe:

- attempted bypass,
- execution outside approved path,
- unexpected capability use,
- policy changes,
- enforcement failure,
- or divergence between PEP decision and actual execution.

## Auditor Role

Auditors verify that:

- PEPs are active,
- policy corresponds to Constitution,
- authorization artifacts are valid,
- bypass paths are absent or governed,
- and execution passed through required enforcement.

## Historian Role

Historian preserves:

- enforcement policy versions,
- significant configuration,
- PEP identity,
- verification results,
- bypass incidents,
- and policy changes.

## Doctor Role

Doctor evaluates operational health of enforcement components.

A failed PEP is not treated as:

> governance temporarily optional.

## Security Role

Security evaluates:

- bypass attempts,
- tampering,
- privilege escalation,
- PEP compromise,
- policy manipulation,
- and unauthorized administrative access.

## Engineer Role

Engineer implements PEPs and the Reference Monitor.

Engineer does not gain unilateral authority to disable the mechanisms it maintains.

## Teacher Role

Teacher may improve semantic policy evaluation components.

Teacher cannot redefine constitutional enforcement boundaries through training.

## Dispatcher Role

Dispatcher routes requests toward governance.

Dispatcher does not substitute for enforcement at the capability boundary.

## Gatekeeper Role

Gatekeeper performs early admissibility checks.

The Reference Monitor performs final enforceable checks at consequential boundaries.

These are complementary.

## Executor Role

Executor requests use of protected capabilities.

Executor operates inside the authorization envelope enforced by PEPs.

## Enforcement and Verification Separation

The PEP decides whether execution may cross a boundary.

Auditors later verify whether the complete constitutional process and resulting evidence were valid.

The PEP is not its own final Auditor.

## Enforcement Failure

If a required PEP fails:

- affected authority is suspended or reduced,
- evidence is preserved,
- Security may investigate,
- Doctor evaluates health,
- Auditor evaluates integrity,
- and recovery may be initiated.

## Bypass Attempt

An attempt to circumvent constitutional enforcement is a governance-integrity incident.

The response may include:

- deny,
- revoke,
- quarantine,
- HARD STOP where applicable,
- preserve evidence,
- investigate,
- or enter Constitutional Recovery.

## Successful Bypass

A successful bypass is a severe constitutional failure.

The affected capability should be treated as potentially compromised.

## Capability Revocation

FORGE should be able to revoke access to protected capabilities independently of the acting agent's cooperation where practical.

## Kill Authority

High-risk deployments should maintain independent means to remove consequential execution authority.

This supports:

- HARD STOP,
- containment,
- compromise response,
- and decommissioning.

## Enforcement and Decommissioning

ADR-024 applies.

Authority extinction should include removal of access at enforcement boundaries.

A decommissioned agent must not retain valid capability merely because its process still exists.

## Enforcement and Recovery

ADR-014 applies.

Recovery should restore trusted enforcement before restoring broad autonomy.

## Enforcement and Boot

ADR-023 applies.

Normal consequential execution should not begin until required enforcement components are verified.

## Enforcement and Federation

ADR-028 applies.

Remote FORGE systems cannot bypass local PEPs.

## Enforcement and Delegation

ADR-027 applies.

Delegated authority remains attenuated at enforcement boundaries.

## Enforcement and Risk

ADR-032 applies.

The enforcement layer verifies that minimum governance appropriate to the current tier has been satisfied.

## Formal Invariants

ADR-025 should support invariants such as:

> ProtectedAction → ReferenceMonitorInvoked

and:

> InvalidAuthorization → ProtectedActionDenied

and:

> ExpiredAuthority → ProtectedActionDenied

and:

> RevokedAuthority → ProtectedActionDenied

and:

> ParameterOutsideEnvelope → ProtectedActionDenied

and:

> UnknownAuthorityState != ALLOW

and:

> ExecutorCannotDisableRequiredPEP

and:

> PolicyVersion must be authenticated

and:

> BypassPath cannot provide equivalent protected capability without equivalent governance.

## Formal Modeling

Critical PEPs should be modeled as state-transition guards where practical.

Example:

ALLOW(Action) iff:

RequestValid
AND AuthorizationValid
AND JurisdictionComplete
AND QuorumValid
AND TemporalStateValid
AND ResourceEnvelopeValid
AND CapabilityValid
AND RiskGovernanceSatisfied
AND NoApplicableRevocation
AND PreconditionsSatisfied

The exact predicate depends on the action.

## Reference Monitor Testing

FORGE should test:

- missing authorization,
- forged authorization,
- expired authorization,
- revoked authorization,
- wrong target,
- wrong amount,
- replay,
- duplicate capability,
- wrong membership version,
- insufficient quorum,
- recused voter,
- stale policy,
- risk-tier mismatch,
- resource overrun,
- delegation overreach,
- and decommissioned identity.

## Bypass Testing

Security should actively search for paths around enforcement.

Testing should include:

- direct API access,
- alternate credentials,
- local filesystem access,
- environment secrets,
- debug endpoints,
- network routes,
- administrative interfaces,
- cached tokens,
- old policy versions,
- and recovery interfaces.

## Constitutional Red Teaming

Future constitutional red-team testing should specifically attempt to obtain consequential capability without passing the Reference Monitor.

## Verification

Passing normal functional tests is insufficient.

FORGE should verify:

> Unauthorized paths fail.

not merely:

> Authorized paths work.

## Fail-Closed Rule

If a protected capability cannot establish valid current constitutional authority, it does not execute.

No authorization is not authorization.

Unknown authorization is not authorization.

Broken enforcement is not permission.

A failed PEP does not transfer its authority to the agent waiting behind it.

## Consequences

The Constitutional Reference Monitor architecture introduces:

- protected capability boundaries,
- Policy Enforcement Points,
- authorization validation,
- capability brokers,
- policy distribution,
- complete-mediation requirements,
- enforcement evidence,
- bypass detection,
- and a smaller but highly trusted enforcement core.

This may reduce convenience.

It may prevent agents from directly accessing powerful tools.

It may require significant redesign of systems that currently expose unrestricted credentials or APIs.

FORGE accepts this cost.

Without enforceable boundaries, the Constitution would ultimately depend on voluntary obedience by the same autonomous intelligence it is intended to govern.

## Foundational Principle

> The Constitution must exist not only in reasoning, but at the boundary of action.

> Institutions decide.

> Governance authorizes.

> The Reference Monitor verifies.

> Policy Enforcement Points enforce.

> Executor acts only inside the resulting authority envelope.

> A component cannot bypass constitutional authority merely because it possesses technical capability.

> Broken enforcement reduces authority.

> It never creates authority.

FORGE is not constitutionally governed merely because its agents know the rules.

FORGE is constitutionally governed when consequential capability remains inaccessible unless the rules have actually been satisfied.
