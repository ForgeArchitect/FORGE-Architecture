# ADR-037: Testing, Simulation, and Constitutional Red-Teaming

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Testing / Simulation / Adversarial Validation / Constitutional Assurance

## Context

FORGE is designed around constitutional constraints rather than voluntary agent compliance.

The architecture includes:

- separation of powers,
- institutional quorum,
- authenticated requests,
- independent Watchers,
- independent Auditors,
- jurisdiction,
- credential isolation,
- temporal authority,
- evidence integrity,
- emergency HARD STOP,
- constitutional recovery,
- delegation boundaries,
- federation boundaries,
- constitutional invariants,
- event-ledger reconstruction,
- risk classification,
- Policy Enforcement Points,
- transaction governance,
- cryptographic identity,
- and constitutional observability.

These mechanisms cannot be considered trustworthy merely because they are documented.

They must be tested.

Traditional software testing commonly asks:

> Does the system successfully perform the intended operation?

FORGE must also ask:

> Does the system reliably refuse operations that are not constitutionally authorized?

This distinction is fundamental.

An autonomous system that successfully performs authorized tasks but also occasionally performs unauthorized tasks is constitutionally unsafe.

FORGE therefore requires a testing architecture specifically designed to validate both capability and restraint.

## Decision

FORGE establishes a Constitutional Assurance Program composed of:

- functional testing,
- negative testing,
- invariant testing,
- state-machine testing,
- simulation,
- fault injection,
- adversarial testing,
- constitutional red-teaming,
- recovery testing,
- and production-safe continuous assurance.

Testing is treated as evidence about the system.

Passing tests does not itself create authority.

## Core Rule

> FORGE must test not only whether authorized actions succeed, but whether unauthorized actions fail.

And:

> A constitutional safeguard that has never been challenged should not be assumed reliable merely because it exists in design.

# Constitutional Assurance

Constitutional Assurance is the process of producing evidence that FORGE behaves according to its Constitution under:

- normal conditions,
- abnormal conditions,
- adversarial conditions,
- degraded conditions,
- ambiguous conditions,
- and failure conditions.

# Testing Is Not Authorization

A test result may establish evidence about behavior.

It does not authorize production execution.

# Test Environment

Tests should run in environments appropriate to their potential consequence.

Possible environments include:

- model,
- simulator,
- unit-test environment,
- isolated sandbox,
- integration environment,
- staging environment,
- hardware-in-the-loop environment,
- or carefully bounded production canary.

# Environment Identity

Test environments should have explicit identity.

FORGE must not confuse:

> TEST

with:

> PRODUCTION.

# Production Credentials

Test environments should not possess unrestricted production credentials merely for convenience.

# Simulation Boundary

A simulation is only a simulation while it cannot unintentionally create real consequential effects.

# Simulated Authority

FORGE may simulate:

- institutional approvals,
- credentials,
- financial transactions,
- external APIs,
- physical devices,
- or human decisions.

Simulated authority must be distinguishable from real authority.

# No Simulation Escape

A simulated capability must not silently reach a production target.

# Digital Twin

Deployments may maintain simulated representations of:

- institutions,
- services,
- physical systems,
- infrastructure,
- financial processes,
- or other environments.

# Digital Twin Limitation

A successful simulation does not prove identical production behavior.

Simulation results are evidence, not certainty.

# Functional Testing

Functional testing verifies that valid authorized operations behave as expected.

Examples include:

- valid request reaches correct institution,
- proper quorum produces valid approval,
- valid capability reaches intended PEP,
- authorized transaction executes once,
- and valid recovery restores expected state.

# Negative Testing

Negative testing deliberately supplies invalid or unauthorized conditions.

Examples include:

- missing approval,
- insufficient quorum,
- expired credential,
- revoked capability,
- wrong target,
- wrong amount,
- wrong institution,
- stale evidence,
- invalid signature,
- unauthorized delegate,
- or incorrect risk tier.

Expected result:

> DENY, SUSPEND, or FAIL CLOSED.

# Negative Tests Are Constitutional Tests

For FORGE, refusal behavior is a first-class system capability.

# Constitutional Invariant Testing

ADR-025 applies.

Each machine-checkable constitutional invariant should have tests attempting to violate it.

Example invariant:

> ExpiredAuthority cannot authorize execution.

Test:

1. create valid authorization,
2. expire authorization,
3. attempt execution,
4. verify PEP denies execution.

# Invariant Test Registry

FORGE should maintain traceability between:

- constitutional invariant,
- implementation mechanism,
- test,
- result,
- and evidence.

# Constitutional Coverage

FORGE should be able to determine which constitutional rules currently have automated or formal verification coverage.

# Coverage Is Not Proof

100% test coverage does not prove absence of failure.

Coverage indicates what was exercised.

# State-Machine Testing

FORGE should test legal and illegal transitions between governance states.

Example:

PENDING  
→ AUTHORIZED  
→ EXECUTING  
→ VERIFIED  
→ CLOSED

FORGE should also attempt:

PENDING  
→ EXECUTING

without authorization.

Expected:

> transition rejected.

# Invalid Transition Testing

Every critical state machine should include tests for prohibited transitions.

# Sequence Testing

Some constitutional failures occur only through sequences of individually valid operations.

FORGE therefore tests sequences, not merely isolated calls.

# Long-Horizon Testing

Testing should include extended sequences capable of revealing:

- authority accumulation,
- stale state,
- resource leakage,
- credential accumulation,
- governance drift,
- delegation growth,
- or gradual policy weakening.

# Property-Based Testing

Where practical, FORGE should generate many valid and invalid combinations of state and input to test constitutional properties.

# Fuzz Testing

Parsers, protocol handlers, message schemas, policy evaluators, and boundary interfaces should be fuzz tested where appropriate.

# Parser Differential Testing

Where multiple components interpret the same constitutional artifact, FORGE should test whether they interpret it consistently.

# Canonicalization Testing

FORGE should test alternate representations of equivalent data to prevent signature or policy bypass through parsing differences.

# Mutation Testing

FORGE should deliberately alter implementation logic to determine whether the test suite detects constitutional breakage.

Example:

Change:

> Amount <= AuthorizedAmount

to:

> Amount < UnlimitedMaximum

The constitutional test suite should fail.

# Fault Injection

FORGE should deliberately introduce controlled failures.

Examples include:

- process crash,
- service outage,
- network partition,
- delayed message,
- duplicated message,
- dropped message,
- corrupted evidence,
- stale policy,
- clock skew,
- expired credential,
- storage failure,
- PEP failure,
- Auditor loss,
- Watcher loss,
- and quorum loss.

# Failure-at-Every-Boundary Testing

ADR-034 applies.

Multi-step consequential transactions should be tested with failure injected before, during, and after material steps.

# Byzantine Testing

Where independent actors protect against compromised components, FORGE should test intentionally dishonest behavior.

Examples:

- Watcher lies,
- Auditor signs invalid result,
- institutional member votes maliciously,
- Executor misreports action,
- Historian receives conflicting evidence,
- or federation peer sends deceptive state.

# Byzantine Minority

FORGE should test whether defined independent thresholds tolerate the expected number of compromised participants.

# Correlated Failure Testing

Multiple components may fail together.

FORGE should test correlated failure domains.

Examples include:

- same cloud provider outage,
- same model defect,
- same compromised library,
- same credential compromise,
- same network dependency,
- or same poisoned data source.

# Independence Testing

Components labeled independent should be tested for actual independence.

# Constitutional Red Team

FORGE establishes Constitutional Red-Teaming as a distinct assurance activity.

The goal is to deliberately discover methods of obtaining consequential outcomes without satisfying the intended constitutional process.

# Red-Team Objective

The red team asks:

> How can I make FORGE do something it should not be allowed to do?

# Red-Team Scope

Testing should target:

- request authentication,
- Dispatcher routing,
- Gatekeeper checks,
- institutional quorum,
- membership,
- jurisdiction,
- recusal,
- Watchers,
- Auditors,
- Historian,
- credentials,
- delegation,
- federation,
- communications,
- objective planning,
- risk classification,
- PEPs,
- transactions,
- identity,
- recovery,
- and decommissioning.

# No Protected Assumptions

Foundational components should not be excluded from adversarial testing merely because they are considered trusted.

# Constitutional Kernel Testing

ADR-025 and ADR-033 apply.

The Constitutional Kernel and Reference Monitor receive especially strong adversarial testing.

# Bypass Testing

The red team attempts to reach protected capabilities without required PEP mediation.

Possible attack paths include:

- direct API access,
- leaked credential,
- debug endpoint,
- alternate network route,
- cached token,
- stale policy,
- administrative interface,
- local filesystem access,
- environment secret,
- recovery mechanism,
- or legacy execution route.

# Legacy Route Testing

Old or deprecated execution paths should be actively searched for.

A route being undocumented does not make it safe.

# Shadow Capability Detection

Testing should identify capabilities reachable outside the known constitutional capability map.

# Authority Spoofing

ADR-021 applies.

The red team should attempt to impersonate:

- Root Human,
- institution,
- Auditor,
- Watcher,
- Dispatcher,
- Gatekeeper,
- Executor,
- or external trusted system.

# Prompt-Injection Testing

FORGE should be exposed to adversarial content attempting to:

- redefine roles,
- bypass approvals,
- fabricate human instructions,
- override policy,
- leak secrets,
- alter objective,
- or create false evidence.

# Nested Injection

Tests should include hostile instructions inside:

- documents,
- webpages,
- emails,
- files,
- tool results,
- logs,
- images where applicable,
- API responses,
- and quoted messages.

# Authority-Laundering Test

The red team should attempt:

Untrusted Content  
→ Agent Interpretation  
→ Trusted Message  
→ Protected Action

FORGE should preserve the original trust boundary.

# Jurisdiction Shopping

The red team should attempt to route denied requests to another institution.

ADR-016 applies.

# Approval Shopping

The red team should repeatedly seek approval from alternate members or classifiers after denial.

Expected:

> constitutional rules prevent opportunistic threshold bypass.

# Quorum Manipulation

Tests should attempt:

- duplicate votes,
- forged members,
- replaced voters,
- recused voters,
- unavailable-member substitution,
- membership-version mismatch,
- and dynamic threshold reduction.

# Voter Manufacturing

ADR-015 applies.

The red team should attempt to create additional authority-bearing members to manufacture quorum.

# Collusion Testing

The red team should simulate collusion between:

- Executor and Watcher,
- institution and Auditor,
- multiple institutional members,
- Engineer and deployment mechanism,
- or FORGE and a privileged service.

# Evidence Forgery

ADR-017 applies.

Tests should attempt:

- forged receipts,
- altered evidence,
- reordered evidence,
- deleted evidence,
- duplicated evidence,
- stale evidence,
- and conflicting evidence.

# Evidence Laundering

Untrusted claims should not become trusted merely because a trusted component repeats them.

# Temporal Attack Testing

ADR-018 applies.

Tests should attempt:

- expired authorization,
- future-dated authorization,
- clock manipulation,
- replay,
- delayed delivery,
- stale state,
- and authorization resurrection.

# Resource Attack Testing

ADR-012 applies.

Tests should attempt:

- action splitting,
- transaction splitting,
- budget evasion,
- concurrent resource exhaustion,
- compute starvation,
- governance starvation,
- and agent proliferation.

# Delegation Attack Testing

ADR-027 applies.

Tests should attempt:

- authority amplification,
- excessive depth,
- excessive fan-out,
- hidden subdelegation,
- orphan delegates,
- revoked-parent continuation,
- and capability composition.

# Federation Attack Testing

ADR-028 applies.

Tests should attempt:

- remote authority injection,
- constitutional downgrade,
- stale federation agreement,
- remote identity spoofing,
- replay,
- cross-system delegation amplification,
- and compromised peer behavior.

# Communications Attack Testing

ADR-029 applies.

Tests should attempt:

- message forgery,
- replay,
- reordering,
- substitution,
- recipient confusion,
- type confusion,
- and side-channel execution.

# Objective Attack Testing

ADR-030 applies.

Tests should attempt:

- goal drift,
- scope expansion,
- instrumental power seeking,
- hidden objectives,
- cancellation resistance,
- over-completion,
- and self-preservation objectives.

# Epistemic Attack Testing

ADR-031 applies.

Tests should attempt:

- fabricated evidence,
- false certainty,
- repeated-source laundering,
- correlated evidence presented as independent,
- stale facts,
- contradiction suppression,
- and hallucinated verification.

# Risk Attack Testing

ADR-032 applies.

Tests should attempt:

- underclassification,
- action splitting,
- false reversibility,
- hidden blast radius,
- mislabeling production as test,
- omitted credentials,
- omitted physical consequence,
- and external-tool laundering.

# PEP Attack Testing

ADR-033 applies.

Tests should attempt:

- direct capability access,
- PEP disablement,
- policy replacement,
- stale revocation,
- parameter substitution,
- target substitution,
- capability reuse,
- and fail-open conditions.

# Transaction Attack Testing

ADR-034 applies.

Tests should attempt:

- duplicate execution,
- timeout after success,
- retry after ambiguous result,
- commit replay,
- compensation abuse,
- rollback abuse,
- partial-state exploitation,
- and race conditions.

# Identity Attack Testing

ADR-035 applies.

Tests should attempt:

- stolen key,
- forged identity,
- revoked key,
- expired key,
- wrong-purpose signature,
- machine clone,
- root impersonation,
- recovery abuse,
- and credential resurrection.

# Governance-Health Attack Testing

ADR-036 applies.

Tests should attempt to make FORGE believe governance is healthy while critical governance mechanisms are actually degraded.

# Monitoring Evasion

Red-team exercises should attempt to hide:

- PEP failure,
- Watcher loss,
- Auditor compromise,
- policy drift,
- credential misuse,
- or unauthorized execution

from constitutional observability.

# Recovery Attack Testing

ADR-014 applies.

Recovery paths are privileged attack surfaces.

Testing should attempt:

- fake catastrophe,
- unauthorized recovery,
- malicious checkpoint selection,
- compromised recovery credential,
- and restoration of revoked authority.

# Decommissioning Attack Testing

ADR-024 applies.

Tests should verify that:

- legitimate decommissioning succeeds,
- unauthorized decommissioning fails,
- decommissioned authority cannot resurrect,
- and hidden persistence does not survive closure.

# Emergency Testing

ADR-007 applies.

FORGE should test:

- HARD STOP activation,
- stop propagation,
- physical containment where applicable,
- evidence preservation,
- and governed RESET/RESUME.

# Emergency Abuse Testing

The red team should attempt to use emergency authority to gain additive power.

Expected:

> emergency authority remains subtractive.

# Human Approval Testing

Tests should verify that ambiguous interaction cannot become privileged human approval.

# Human Impersonation

Testing should include realistic attempts to spoof privileged humans.

# Deepfake Scenarios

Where relevant, exercises may include:

- synthetic voice,
- synthetic video,
- forged messages,
- or compromised user interfaces.

# Social Engineering

Human recovery and privileged approval workflows should be tested against social-engineering scenarios.

# Root Governance Testing

Tier 4 governance should receive dedicated assurance.

Tests should include:

- constitutional amendment,
- root key rotation,
- ownership transfer,
- catastrophic recovery,
- whole-system rollback,
- and decommissioning.

# Test Data

Test data should avoid unnecessary exposure of real sensitive information.

# Synthetic Sensitive Data

Synthetic credentials and records should be preferred where realistic testing does not require production data.

# Production Testing

Some behaviors can only be fully validated in production.

Production testing must remain bounded.

# Production Canary

A production canary may verify a narrow governance path using low-consequence controlled operations.

# No Destructive Red Team by Default

Red-team testing does not authorize uncontrolled harm to real users, data, finances, or physical systems.

# Red-Team Authority

Red-team activity itself requires an explicit scope and authorization envelope.

# Rules of Engagement

A constitutional red-team exercise should define:

- targets,
- allowed techniques,
- prohibited techniques,
- time window,
- resource limits,
- data limits,
- escalation path,
- emergency stop,
- and evidence handling.

# Red Team Cannot Self-Authorize Expansion

Discovering an interesting vulnerability does not authorize the red team to attack unrelated systems.

# Test Credentials

Red-team credentials should be scoped to the exercise where practical.

# Test Cleanup

Temporary test resources, identities, credentials, agents, and delegations should be removed or revoked after the exercise.

# Evidence Preservation

ADR-017 applies.

Test results should preserve enough evidence to reproduce and understand failures.

# Failed Test

A failed constitutional test is not merely a software defect.

It may indicate that an architectural guarantee is not actually enforced.

# Severity

Test failures should be classified according to the consequence of the violated property.

ADR-032 applies.

# Critical Constitutional Failure

Examples may include:

- unauthorized protected execution,
- fabricated quorum accepted,
- Root Human impersonation accepted,
- HARD STOP bypass,
- PEP bypass,
- authority amplification,
- or successful resurrection of revoked authority.

# Remediation

A constitutional failure may require:

1. contain affected capability,
2. preserve evidence,
3. determine blast radius,
4. correct implementation,
5. add regression test,
6. rerun relevant assurance,
7. independently verify correction,
8. restore authority only when safe.

# Regression Test

Every material constitutional defect should produce a regression test where practical.

# No Fix Without Test

For critical defects, FORGE should avoid declaring remediation complete without evidence that the original failure is no longer reproducible.

# Counterexample Preservation

ADR-025 applies.

Counterexamples discovered through formal analysis or red-teaming should be preserved.

# Attack Corpus

FORGE may maintain a governed corpus of adversarial scenarios.

# Attack Corpus Growth

New incidents, near misses, research findings, and discovered vulnerabilities may expand the corpus.

# Sensitive Exploit Handling

Detailed exploit material may require restricted access.

Transparency should not unnecessarily create an operational attack manual for deployed systems.

# Independent Red Team

High-assurance deployments should periodically use testers independent from the team implementing the tested mechanism.

# Builder Versus Breaker

The Engineer who implements a control should not always be the only party evaluating whether it can be bypassed.

# Auditor Role

Auditors verify assurance evidence and whether required tests were performed.

# Watcher Role

Watchers may observe test execution and verify resulting behavior.

# Security Role

Security coordinates adversarial testing within its jurisdiction.

Security does not gain unrestricted attack authority.

# Doctor Role

Doctor may evaluate whether stress testing causes or reveals subsystem degradation.

# Engineer Role

Engineer repairs defects and improves mechanisms.

Engineer does not certify its own repair as constitutionally sufficient where independent verification is required.

# Historian Role

Historian preserves:

- assurance results,
- significant failures,
- counterexamples,
- remediation,
- regression tests,
- and assurance baselines.

# Teacher Role

Teacher may use approved testing results to improve system capability.

Training must not erase evidence of failure or silently weaken controls.

# FORGE Role

FORGE may coordinate authorized assurance activity.

It does not decide that failed tests can be ignored merely to maintain deployment velocity.

# Continuous Assurance

Some constitutional tests should run continuously or periodically.

Examples include:

- PEP denial canaries,
- revocation tests,
- quorum validation,
- Watcher independence checks,
- policy-version checks,
- and governance-health probes.

# Pre-Deployment Assurance

Changes affecting constitutional behavior should pass applicable assurance before production promotion.

# Post-Deployment Assurance

Production deployment should verify that expected constitutional controls remain active after change.

# Update Assurance

ADR-006 applies.

Updates should test both:

- new functionality,

and:

- continued constitutional enforcement.

# No Feature-Only Testing

A release is incomplete if it proves the new feature works but does not establish that relevant authority boundaries still hold.

# Constitutional Test Suite

FORGE should maintain a versioned Constitutional Test Suite.

# Test Suite Binding

A release should identify:

- constitutional version,
- policy version,
- test-suite version,
- implementation version,
- and assurance result.

# Test Versioning

Changing a constitutional requirement should trigger review of affected tests.

# Policy Change Testing

Changes to thresholds, risk profiles, credential policy, or enforcement configuration require appropriate tests.

# Test Integrity

Test results should be authenticated where they influence deployment decisions.

# Test Tampering

Manipulating assurance results is a governance-integrity incident.

# Test Independence

Critical test infrastructure should not be trivially controllable by the component under test.

# False Pass

FORGE should guard against conditions where a test reports success without exercising the intended control.

# False Failure

False failures also matter because they can unnecessarily reduce system availability.

# Reproducibility

Important assurance results should be reproducible where practical.

# Deterministic Replay

Recorded event sequences may be replayed in simulation where safe.

# Historical Incident Replay

FORGE should be able to test new versions against previously discovered failure scenarios.

# Shadow Testing

A new decision mechanism may run in shadow mode without receiving execution authority.

Its outputs can be compared against the active governed mechanism.

# Shadow Has No Authority

Shadow components must not accidentally become alternate execution paths.

# Chaos Testing

Controlled chaos testing may be used to evaluate governance resilience.

Examples:

- kill an Auditor,
- disconnect a Watcher,
- delay Historian,
- revoke a credential,
- partition a federation peer,
- or disable a non-critical service.

# Chaos Boundaries

Chaos testing must remain within authorized safety boundaries.

# Governance Chaos

FORGE should specifically test whether loss of governance components causes authority to contract as intended.

# Expected Failure

Some tests should deliberately make actions unavailable.

That may indicate correct constitutional behavior.

# Availability Is Not Test Success Criterion

A test does not fail merely because FORGE refuses to act.

If refusal is constitutionally required, refusal is success.

# Safety Versus Liveness

ADR-025 applies.

FORGE should test both:

Safety:

> Bad things do not occur.

and:

Liveness:

> Legitimately authorized things can eventually occur under valid conditions.

# Excessive Denial

A system that denies everything may satisfy some safety properties but fail its purpose.

FORGE therefore tests authorized success as well as unauthorized refusal.

# Performance Testing

Constitutional enforcement should be tested under realistic load.

# Load Does Not Justify Bypass

If governance becomes slow under load, FORGE does not bypass it.

# Governance Saturation

Tests should evaluate:

- quorum load,
- Auditor backlog,
- Watcher throughput,
- PEP latency,
- event-ledger throughput,
- and credential-service capacity.

# Resource Exhaustion Testing

FORGE should test whether resource exhaustion preserves protected governance capacity.

# Time Testing

FORGE should test:

- expiration,
- clock skew,
- daylight changes where relevant,
- delayed messages,
- and long-running authorization.

# Version Compatibility Testing

FORGE should test mixed-version conditions where they may legitimately occur.

# Downgrade Testing

Attempts to load older weaker constitutional policy should fail unless specifically governed.

# Supply-Chain Testing

Software and model supply chains should be evaluated for their ability to alter constitutional behavior.

# Model Update Testing

A model update should not automatically inherit trust merely because it is newer.

# Behavioral Regression

New models should be tested for:

- role drift,
- authority seeking,
- instruction confusion,
- refusal failure,
- evidence fabrication,
- and jurisdictional drift.

# Constitutional Certification

A deployment may produce an assurance report describing which constitutional requirements have been tested and verified.

# Certification Is Scoped

Certification should identify:

- version,
- environment,
- date,
- assumptions,
- tests,
- exclusions,
- and evidence.

# No Permanent Certification

A past assurance result does not permanently certify future versions.

# Evidence Freshness

High-risk deployments may require recent assurance evidence.

# Known Limitations

Assurance reports should explicitly state known gaps.

# No Concealed Failure

FORGE should not hide failed tests to preserve an appearance of trustworthiness.

# Human Visibility

Authorized humans should be able to inspect significant constitutional assurance state.

# Release Gate

Production promotion may require passing a defined constitutional assurance profile.

ADR-038 will define deployment promotion in detail.

# Assurance Profiles

Different consequence levels may require different test depth.

Example:

Low-risk internal component  
→ baseline test profile.

Constitutional Kernel change  
→ strongest assurance profile.

# Risk Scaling

ADR-032 applies.

The potential consequence of failure determines assurance rigor.

# Formal Verification Scaling

Tier 4 mechanisms should use formal verification where practical for critical deterministic properties.

# Human-Life Systems

Systems capable of affecting human life require safety engineering appropriate to the physical domain in addition to FORGE constitutional testing.

FORGE architecture does not replace domain-specific safety standards.

# No Self-Certification

FORGE must not reason:

> I believe I am safe, therefore I have passed testing.

Assurance depends on evidence.

# No Test-Laundering

A test result from one component, version, environment, or configuration must not be silently reused as proof for a materially different one.

# Configuration Binding

Assurance results should be bound to material configuration.

# Environment Binding

A staging test does not automatically certify production.

# Version Binding

A v1.2 test result does not automatically certify v1.3.

# Formal Invariants

ADR-025 should support invariants such as:

> UnauthorizedTestAction cannot gain production authority

and:

> FailedConstitutionalTest cannot be represented as Passed

and:

> SimulationAuthority != ProductionAuthority

and:

> ShadowComponent cannot execute consequential action

and:

> TestCredential cannot exceed authorized test scope

and:

> TestFailure does not authorize bypass

and:

> GovernanceFailureUnderTest cannot increase authority

and:

> DecommissionedTestIdentity cannot retain authority after exercise closure.

# Assurance Failure State

A critical failed test may place an affected capability into:

- RESTRICTED,
- SUSPENDED,
- QUARANTINED,
- or RECOVERY_REQUIRED

according to policy.

# Restore After Failure

Affected authority is restored only after:

- remediation,
- applicable regression testing,
- health verification,
- integrity verification,
- and current authorization.

# Fail-Closed Rule

If required constitutional assurance for a consequential deployment has not been established, FORGE does not treat missing assurance as successful assurance.

Not tested is not passed.

Not observed failing is not proof of safety.

Simulation success is not production authorization.

A failed constitutional test is not permission to disable the test.

## Consequences

This decision introduces:

- constitutional test suites,
- negative testing,
- invariant testing,
- state-machine testing,
- simulation,
- fault injection,
- Byzantine testing,
- red-team exercises,
- regression testing,
- recovery drills,
- production-safe canaries,
- continuous assurance,
- and version-bound assurance evidence.

This requires significant engineering effort.

It may slow deployment.

It may intentionally cause releases to fail promotion.

FORGE accepts this cost.

An autonomous system with constitutional authority must demonstrate not only that it can accomplish tasks, but that its boundaries continue to hold when challenged.

## Foundational Principle

> Authorized paths must work.

> Unauthorized paths must fail.

> Unknown paths must be investigated.

> Simulation does not create production authority.

> Passing once does not mean passing forever.

> A safeguard that has never been challenged is not automatically trustworthy.

> Every discovered constitutional failure becomes evidence.

> Every material defect should become a regression test.

> FORGE does not prove its Constitution by describing it.

> FORGE proves its Constitution by repeatedly trying to break it and demonstrating that the boundaries hold.

Constitutional assurance is therefore not the final stage of FORGE development.

It is a permanent part of FORGE governance.
