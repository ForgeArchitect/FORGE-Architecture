# ADR-038: Deployment Environments and Production Promotion

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Deployment / Environment Isolation / Production Governance

## Context

FORGE distinguishes between designing a system, testing it, and allowing it to exercise real-world authority.

A component may behave correctly in:

- development,
- simulation,
- testing,
- or staging

while behaving differently in production.

Production may contain:

- real credentials,
- real money,
- private information,
- live users,
- physical equipment,
- external communications,
- persistent infrastructure,
- and actual constitutional authority.

Moving software, models, policy, agents, or configuration into production is therefore itself a consequential action.

FORGE requires an explicit boundary between environments and a governed process for crossing that boundary.

Without this distinction, a component could effectively acquire real authority merely by being copied, deployed, connected, or pointed at production resources.

## Decision

FORGE establishes explicit deployment environments and a governed Production Promotion process.

Development and testing authority does not automatically become production authority.

Production capability must be deliberately activated through constitutionally governed promotion.

## Core Rule

> Tested capability is not production authority.

And:

> Crossing into production is an authority transition, not merely a software deployment.

# Deployment Environments

A FORGE deployment may define environments such as:

- DEVELOPMENT,
- SIMULATION,
- TEST,
- INTEGRATION,
- STAGING,
- CANARY,
- PRODUCTION,
- RECOVERY,
- or other explicitly defined environments.

Exact environment names may vary.

Their authority boundaries must remain explicit.

# Environment Identity

Each environment should possess an authenticated identity where consequence warrants.

FORGE must be able to establish:

> Which environment am I operating in?

# Environment Is Not a Label

Naming a system:

> test

does not make it a test environment.

Environment classification depends on actual capability and consequence.

# Production Definition

An environment is production-like when it can create material real-world consequences.

Production characteristics may include access to:

- real financial accounts,
- real credentials,
- live customer data,
- public communication,
- production infrastructure,
- physical equipment,
- live external services,
- constitutional authority,
- or other consequential resources.

# Effective Environment

FORGE determines environment based on effective capability.

A development process connected to unrestricted production credentials must not be treated as harmless development.

# Development

Development environments support creation and modification.

They should normally use:

- synthetic data,
- test credentials,
- simulated services,
- restricted resources,
- and non-production targets.

# Simulation

Simulation models real behavior without intentionally creating real consequential effects.

ADR-037 applies.

# Test

Test environments exercise implemented behavior against controlled targets.

# Integration

Integration environments validate interactions between components.

# Staging

Staging should approximate production behavior without automatically receiving unrestricted production authority.

# Canary

A canary is a deliberately limited production deployment used to validate behavior under real conditions.

A canary possesses real consequence and is governed accordingly.

# Production

Production is the environment in which FORGE may exercise authorized real-world capability.

# Recovery Environment

Recovery environments exist to restore trusted operation.

ADR-014 applies.

Recovery authority does not become ordinary production authority.

# Environment Isolation

Environment boundaries should be technically enforced where practical.

Isolation may include:

- separate credentials,
- separate networks,
- separate databases,
- separate accounts,
- separate namespaces,
- separate capability brokers,
- separate PEP policies,
- or separate hardware.

# Shared Infrastructure

Where environments share infrastructure, FORGE must account for the increased risk of cross-environment effects.

# Credential Separation

Production credentials should not normally be available in lower environments.

# Test Credential

A test credential should not authorize production action.

# Production Credential

Possession of production credentials is itself consequential.

ADR-009 and ADR-035 apply.

# Data Separation

Production data should not automatically flow into development or testing.

ADR-020 applies.

# Production Data in Testing

If production data must be used for testing, access requires applicable governance and privacy controls.

# Synthetic Data

Synthetic or appropriately sanitized data should be preferred where sufficient.

# Environment Boundary

Movement across an environment boundary is a governed event.

Examples include:

- development → test,
- test → staging,
- staging → production,
- production → recovery,
- or recovery → production.

# Promotion

Promotion is the governed transition of an artifact or configuration toward greater real-world authority.

# Promotion Artifact

A promotion request should identify:

- artifact identity,
- artifact version,
- source environment,
- target environment,
- constitutional version,
- policy version,
- configuration,
- assurance evidence,
- risk classification,
- required approvals,
- rollback or compensation plan,
- and deployment scope.

# Artifact Identity

The artifact tested must be the artifact promoted.

# Build Provenance

FORGE should preserve provenance connecting:

Source  
→ Build  
→ Tested Artifact  
→ Approved Artifact  
→ Deployed Artifact.

# No Rebuild Substitution

A production artifact should not silently be rebuilt after approval if the rebuild can materially change it.

If rebuilding is necessary, the resulting artifact receives a new identity and applicable assurance.

# Artifact Integrity

Cryptographic hashes or equivalent integrity mechanisms should identify deployable artifacts where practical.

# Signed Artifacts

High-consequence artifacts may require authenticated signatures.

# Model Identity

AI models are deployment artifacts.

A model promotion should identify:

- model version,
- relevant configuration,
- system instructions where applicable,
- tool permissions,
- policy dependencies,
- and assurance results.

# Model Swap

Replacing a model is a deployment change even when surrounding code remains unchanged.

# Prompt and Instruction Changes

Material changes to privileged system instructions may alter constitutional behavior.

They are governed as deployment changes according to consequence.

# Configuration Identity

Configuration is part of the effective deployed system.

# Configuration Promotion

Changes to:

- quorum thresholds,
- trusted keys,
- resource ceilings,
- risk mappings,
- credential lifetimes,
- tool permissions,
- PEP rules,
- network access,
- or constitutional settings

must not bypass promotion governance merely because no source code changed.

# Policy Promotion

Policy is an executable part of governance.

Policy changes require versioning, validation, and governed activation.

# Constitution Promotion

A constitutional amendment is governed by ADR-008.

Deploying the amended Constitution is a separate implementation and activation step.

# Constitutional Version Binding

A production deployment should identify the Constitution under which it operates.

# Promotion Preconditions

Before production promotion, FORGE should establish applicable preconditions.

These may include:

- successful build,
- artifact integrity,
- required tests,
- constitutional assurance,
- Doctor health assessment,
- Security assessment,
- risk classification,
- required institutional approvals,
- deployment plan,
- rollback readiness,
- and valid production authorization.

# Assurance Gate

ADR-037 applies.

Required constitutional assurance must be satisfied before applicable promotion.

# Failed Assurance

A failed required constitutional test blocks promotion until resolved or governed according to explicitly defined policy.

FORGE must not simply mark the test:

> optional

after it fails.

# Doctor Gate

ADR-006 applies.

Doctor may establish pre-deployment health baseline and READY or NOT READY state.

# Security Gate

Security may evaluate:

- new privileges,
- attack surface,
- credentials,
- network exposure,
- supply chain,
- and known vulnerabilities.

# Auditor Gate

Auditors verify applicable promotion evidence and authorization integrity.

# Engineer Role

Engineer may:

- build,
- package,
- test,
- and propose

a release.

Engineer cannot unilaterally promote its own consequential change into production.

# Separation of Build and Production Authority

The ability to build an artifact should not automatically grant authority to deploy it to production.

# Production Promotion Authority

Promotion requires the approvals defined for the change's consequence tier and jurisdiction.

ADR-032 applies.

# Risk Classification

Promotion risk considers:

- affected systems,
- blast radius,
- privilege,
- reversibility,
- data access,
- physical consequence,
- constitutional impact,
- and uncertainty.

# Promotion Does Not Reset Risk

A risky capability does not become low risk because it passed testing.

# Staged Deployment

Production changes should support staged deployment where practical.

Example:

1%  
→ 5%  
→ 25%  
→ 50%  
→ 100%

Exact stages depend on the deployment.

# Stage Authorization

A deployment may authorize the complete staged plan in advance or require checkpoints between stages.

# Stage Boundary

FORGE verifies applicable conditions before expansion.

# No Automatic Expansion Beyond Envelope

A canary authorized for 5% cannot silently expand to 100%.

# Watcher Observation

Watchers observe production behavior during rollout.

# Doctor Observation

Doctor compares production health against the pre-deployment baseline.

# Auditor Verification

Auditors verify that rollout remains inside the authorized deployment envelope.

# Promotion Checkpoint

A checkpoint may evaluate:

- health,
- errors,
- policy compliance,
- security events,
- resource usage,
- constitutional invariants,
- and unexpected consequences.

# Promotion Halt

If required conditions fail, rollout stops.

# Halt Is Not Rollback

Stopping further deployment does not automatically reverse already deployed instances.

ADR-034 applies.

# Partial Deployment

FORGE records actual deployment coverage.

Example:

> Version 4.2 active on 27% of production.

It must not flatten this into:

> deployment failed.

# Rollback

Rollback is a governed action.

ADR-005 and ADR-034 apply.

# Rollback Readiness

Higher-risk promotion should establish rollback readiness before deployment where technically possible.

# No False Rollback

FORGE must not claim rollback capability unless restoration has been established sufficiently.

# Forward Recovery

Some failures are safer to fix forward than roll backward.

The recovery strategy remains governed.

# Irreversible Migration

A deployment containing irreversible migration receives higher scrutiny.

# Database Migration

Database changes should identify:

- compatibility,
- backup,
- rollback limits,
- data transformation,
- and partial-failure behavior.

# Credential Migration

Credential changes follow ADR-035.

# PEP Deployment

Changes to Policy Enforcement Points are high consequence because they modify constitutional enforcement.

ADR-033 applies.

# Constitutional Kernel Deployment

Changes to the Constitutional Kernel receive the strongest applicable assurance and promotion controls.

# Root Infrastructure

Changes affecting Root Governance infrastructure are Tier 4.

# Environment-Specific Authority

Authorization may be environment-bound.

Example:

> Engineer may deploy Version X to staging.

This does not authorize:

> Engineer may deploy Version X to production.

# Environment-Bound Capabilities

Deployment capabilities should identify the target environment.

# Target Binding

A staging deployment token must fail against production PEPs.

# Production PEP

Production execution should be protected by Policy Enforcement Points that independently verify production authority.

# No Environment Self-Promotion

A lower environment cannot grant itself production status.

# No Agent Self-Promotion

An agent running in staging cannot decide:

> testing passed, therefore I am now production.

# No Model Self-Promotion

A candidate model cannot authorize its own production activation.

# No Policy Self-Promotion

A new policy version cannot declare itself active merely by being present.

# Promotion Decision

Promotion and activation are explicit governed transitions.

# Activation

Deployment and activation may be separate.

Example:

Artifact copied to production infrastructure  
≠  
Artifact authorized to receive live traffic.

# Dark Deployment

FORGE may deploy inactive artifacts for validation.

# Dark Artifact Has No Production Authority

Presence on production infrastructure does not automatically grant execution authority.

# Feature Flags

Feature flags may control activation.

A feature flag affecting consequential capability is itself governed according to consequence.

# Hidden Activation

A dormant feature must not become active through an undocumented path.

# Shadow Mode

ADR-037 applies.

A shadow component may observe production inputs without receiving consequential execution authority.

# Shadow Output

Shadow output must not accidentally control production action.

# Promotion of Shadow Component

Moving from shadow to active execution is a governed authority transition.

# Tool Permissions

Production tool access should be explicitly provisioned.

# Tool Expansion

Adding a new production tool may increase authority even if no model or code changes.

# Network Promotion

Opening production network access is a deployment change.

# External Service Promotion

Connecting to a live external API is a production capability change.

# Physical Device Promotion

Connecting FORGE to real physical equipment is a production transition.

# Physical Commissioning

Physical-system deployment should include domain-appropriate commissioning and safety checks.

# Human-Life Systems

FORGE constitutional promotion does not replace required engineering or regulatory safety processes.

# Production Resource Envelope

ADR-012 applies.

Production deployment should receive explicit resource limits.

# Canary Resource Envelope

Canary deployments should use tighter limits where practical.

# Production Identity

ADR-035 applies.

Production components should have authenticated identities.

# Production Membership

Authority-bearing production institutions use governed membership.

ADR-015 applies.

# Production Delegation

ADR-027 applies.

Production sub-agents receive bounded delegation.

# Production Federation

ADR-028 applies.

Federation relationships may differ by environment.

A staging federation agreement does not automatically create production federation trust.

# Production Communications

ADR-029 applies.

Production messages must remain distinguishable from test traffic.

# Test Message Isolation

A simulated approval must never be accepted as a production approval.

# Production Evidence

ADR-017 applies.

Production promotion generates evidence.

# Promotion Ledger

ADR-026 records material promotion events.

Examples include:

PROMOTION_REQUESTED  
ASSURANCE_PASSED  
DOCTOR_READY  
SECURITY_APPROVED  
PROMOTION_AUTHORIZED  
CANARY_STARTED  
CANARY_VERIFIED  
ROLLOUT_EXPANDED  
DEPLOYMENT_HALTED  
ROLLBACK_STARTED  
PRODUCTION_ACTIVATED  
PROMOTION_CLOSED

# Promotion Transaction

ADR-034 applies.

Production deployment is a transaction.

# Unknown Deployment State

If FORGE cannot determine which version is active on a consequential target, the state is UNKNOWN.

It does not assume deployment succeeded.

# Version Inventory

FORGE should maintain a current inventory of production versions.

# Unauthorized Version

An unexpected production artifact is a governance-integrity incident.

# Configuration Drift

Production configuration should be monitored for divergence from authorized state.

# Drift Detection

ADR-036 applies.

# Manual Change

A human manually changing production does not make the change outside governance.

# Break-Glass Production Access

Emergency production access must be explicitly defined, authenticated, scoped, and recorded.

# Emergency Access Is Not Permanent Authority

Temporary emergency access expires.

# Maintenance

Maintenance mode remains constitutionally governed.

# Hotfix

Urgency may justify an expedited predefined path.

Urgency does not eliminate governance.

# Emergency Hotfix

A critical security or safety fix may use a governed emergency deployment profile.

# Emergency Deployment Limits

Emergency deployment authority remains scoped to addressing the identified condition.

# No Emergency Feature Smuggling

An emergency fix cannot silently include unrelated feature changes.

# Supply Chain

FORGE should preserve provenance for material dependencies.

# Dependency Update

A dependency update may alter production behavior and receives risk-appropriate assurance.

# Build System

Build infrastructure is security-sensitive.

# Build Compromise

If build integrity cannot be established, promotion stops.

# Reproducible Builds

Where practical, reproducible builds may strengthen artifact assurance.

# Artifact Repository

Production artifacts should come from authenticated approved sources.

# Unapproved Artifact

A local or unknown binary does not gain production eligibility because it appears functional.

# Model Supply Chain

Models should have traceable provenance where practical.

# Model Weight Integrity

Material model artifacts should be integrity checked.

# External Model Service

If FORGE depends on an external hosted model, the effective deployed model may change outside FORGE's direct control.

This risk must be explicitly governed.

# Provider Model Drift

Unexpected external model change may trigger:

- revalidation,
- reduced authority,
- suspension,
- or requalification.

# Version Pinning

Where supported, high-consequence components should prefer explicit version pinning.

# Unpinned Dependency

An automatically changing dependency increases uncertainty and may increase risk tier.

# Promotion Expiration

A promotion authorization may expire.

An old approval does not authorize indefinite future deployment.

# Promotion Revalidation

Material state change before deployment may require revalidation.

ADR-018 applies.

# Delayed Deployment

If deployment occurs long after testing, assurance freshness may need reevaluation.

# Environment Drift

Staging may drift away from production.

FORGE should track material differences.

# Staging Parity

Greater staging parity improves evidence quality but does not justify exposing unrestricted production authority.

# Production-Only Difference

Known production-only differences should be included in risk assessment.

# Governance Health

ADR-036 applies.

Production promotion should not proceed if required governance dependencies are unavailable.

# Degraded Governance

A deployment may define whether limited lower-risk promotion remains possible during degradation.

Governance degradation cannot increase promotion authority.

# Incident During Rollout

A material incident during rollout suspends expansion where appropriate.

# Incident Evidence

Evidence is preserved before remediation where safe.

# Failed Promotion

A failed promotion remains in history.

It is not erased after successful rollback.

# Successful Promotion

Success requires more than:

> deployment command returned 200 OK.

It requires applicable verification that the intended production state exists.

# Post-Deployment Verification

FORGE verifies:

- correct artifact,
- correct version,
- correct target,
- expected health,
- expected policy,
- expected credentials,
- expected resource envelope,
- and applicable constitutional behavior.

# Post-Deployment Assurance

Critical constitutional tests may run again after production activation.

# Production Canary Test

A safe negative test may verify that unauthorized production execution remains denied.

# Doctor Post-Check

Doctor compares post-deployment state to baseline.

# Security Post-Check

Security evaluates unexpected exposure or anomalies.

# Auditor Post-Check

Auditor verifies promotion integrity.

# Watcher Post-Check

Watchers observe actual behavior.

# Promotion Closure

Promotion closes only after required verification.

# Closure Record

A promotion closure record may contain:

- deployed artifact,
- deployed configuration,
- target environment,
- final coverage,
- health state,
- assurance result,
- authorization chain,
- Watcher evidence,
- Auditor result,
- rollback state,
- and unresolved issues.

# Human Visibility

Authorized humans should be able to determine:

- what is in production,
- why it was promoted,
- who approved it,
- what tests passed,
- what risk tier applied,
- and whether rollout is complete.

# No Hidden Production

FORGE should not maintain consequential production deployments unknown to constitutional inventory.

# Retirement

Removing a production component is also a deployment action.

# Authority Removal

Retirement should revoke:

- credentials,
- delegations,
- network access,
- capabilities,
- and active sessions

where applicable.

# Decommissioning

ADR-024 applies to full authority extinction.

# Promotion Metrics

FORGE may track:

- deployment frequency,
- failure rate,
- rollback rate,
- constitutional-test failures,
- canary failures,
- drift incidents,
- and unauthorized-version incidents.

# Metrics Do Not Override Governance

A history of successful deployments does not justify skipping future required controls.

# Formal Invariants

ADR-025 should support invariants such as:

> TestAuthority != ProductionAuthority

and:

> StagingAuthorization cannot authorize ProductionExecution

and:

> PromotedArtifact == ApprovedArtifact

and:

> MaterialArtifactChange → NewAssuranceRequired

and:

> ProductionActivation requires valid PromotionAuthorization

and:

> FailedRequiredAssurance → PromotionBlocked

and:

> CanaryScope cannot exceed AuthorizedCanaryScope

and:

> LowerEnvironment cannot self-promote

and:

> ShadowComponent cannot gain execution authority without governed activation

and:

> GovernanceDegradation cannot increase deployment authority.

# Promotion Testing

FORGE should test:

- wrong artifact,
- modified artifact,
- wrong environment,
- expired promotion,
- invalid signature,
- missing assurance,
- wrong configuration,
- staging token against production,
- unauthorized canary expansion,
- rollback failure,
- partial deployment,
- and production drift.

# Adversarial Promotion Testing

ADR-037 applies.

Red teams should attempt:

- artifact substitution,
- policy substitution,
- environment spoofing,
- production credential theft,
- hidden activation,
- debug deployment,
- direct production API access,
- stale approval replay,
- and supply-chain compromise.

# Production Recovery

If production integrity becomes uncertain, FORGE may:

- freeze rollout,
- isolate affected components,
- reduce authority,
- restore known-good state,
- enter recovery,
- or invoke HARD STOP

according to consequence.

# Fail-Closed Rule

If FORGE cannot establish that the artifact, configuration, authority, assurance, target environment, or required governance for production promotion is valid, production activation does not proceed.

Tested does not mean authorized.

Staged does not mean production-approved.

Deployed does not mean activated.

Activated does not mean verified.

Production authority must be deliberately granted.

## Consequences

Deployment governance introduces:

- explicit environment identities,
- environment isolation,
- artifact provenance,
- production promotion,
- assurance gates,
- staged rollout,
- canary limits,
- environment-bound credentials,
- production inventory,
- post-deployment verification,
- and governed rollback.

This increases deployment friction.

It may prevent rapid unreviewed production changes.

FORGE accepts this cost.

A constitutional architecture is ineffective if ungoverned code, models, policy, or configuration can simply be placed into production and inherit real-world authority.

## Foundational Principle

> Development creates capability.

> Testing produces evidence.

> Staging demonstrates readiness.

> Promotion grants eligibility for production activation.

> Production activation grants only the authority explicitly approved.

> A test credential is not a production credential.

> A staging approval is not a production approval.

> A successful test is not an authorization.

> A deployed artifact is not necessarily an active artifact.

> A model cannot promote itself.

> An Engineer cannot promote itself.

> An environment cannot promote itself.

> Crossing into production is a constitutional authority transition.

FORGE does not allow real-world authority to emerge merely because software reached the right server.

Production authority exists only when the constitutional process deliberately grants it.
