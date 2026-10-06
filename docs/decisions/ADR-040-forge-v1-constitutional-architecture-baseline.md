# ADR-040: FORGE v1.0 Constitutional Architecture Baseline

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Constitutional Baseline / Architecture / v1.0

## Context

FORGE was created to address a fundamental problem in autonomous-system architecture:

> How can a system exercise meaningful autonomous capability without concentrating the authority to propose, approve, execute, observe, and certify consequential actions inside one trusted intelligence?

Conventional agent architectures often rely on a central agent expected to:

- understand the request,
- interpret policy,
- decide what is allowed,
- select tools,
- execute actions,
- evaluate the result,
- and report success.

This creates a structural concentration of power.

If the central intelligence:

- misunderstands,
- hallucinates,
- drifts,
- becomes compromised,
- is manipulated,
- or deliberately violates policy,

the same component responsible for acting may also control the evidence used to determine whether its action was legitimate.

FORGE takes a different approach.

Rather than attempting to create one perfectly trustworthy autonomous intelligence, FORGE distributes consequential authority across constitutionally constrained institutions and technical enforcement mechanisms.

The architecture established through ADR-001 through ADR-039 now forms a coherent constitutional system.

This ADR establishes those decisions as the FORGE v1.0 Constitutional Architecture Baseline.

## Decision

FORGE v1.0 is defined as a constitutional architecture for governed autonomous systems based on:

- separation of powers,
- authenticated intent,
- institutional jurisdiction,
- independent authorization,
- technical enforcement,
- independent observation,
- independent verification,
- bounded authority,
- explicit uncertainty,
- durable evidence,
- governed recovery,
- and human constitutional sovereignty.

No single component is trusted merely because it is intelligent.

Authority must be established through structure.

## Constitutional Thesis

> No single authority-bearing component should routinely be able to originate, authorize, execute, observe, and certify the same consequential action.

This is the foundational architectural principle of FORGE.

# FORGE Is a Constitutional Process

FORGE is not defined as one unrestricted agent.

FORGE is the governed process through which:

- intent is received,
- authority is evaluated,
- jurisdiction is established,
- decisions are made,
- capabilities are granted,
- actions are executed,
- outcomes are observed,
- evidence is preserved,
- and results are independently verified.

# FORGE Is Under the Constitution

FORGE itself is not sovereign.

FORGE cannot exempt itself from the constitutional mechanisms governing the system.

# Human Sovereignty

Legitimate Root Human authority remains external to FORGE.

FORGE may authenticate and enforce the safeguards established by its human governors.

FORGE cannot manufacture Root Human authority.

# Constitutional Separation of Powers

ADR-001 establishes that consequential authority is divided.

No component should routinely control all stages of consequential action.

# Authenticated Request Chain

ADR-002 establishes the governed request path.

Conceptually:

Authenticated Request  
→ Dispatcher  
→ Gatekeeper  
→ Audit Checkpoint  
→ Relevant Institution(s)  
→ Audit Checkpoint  
→ Authorization  
→ FORGE Execution Process  
→ Watcher Observation  
→ Final Audit Verification.

# Request Identity

Material requests receive authenticated identities bound to normalized intent and consequential parameters.

# Material Mutation

Material modification of a request invalidates authority that no longer matches the request.

# Dispatcher

Dispatcher controls governed ingress and routing.

Dispatcher does not gain authority to approve consequential action merely because it routes the request.

# Gatekeeper

Gatekeeper evaluates admissibility and applicable constitutional requirements.

Gatekeeper may permit or deny progression.

Gatekeeper does not execute consequential actions.

# Institutional Governance

ADR-003 establishes institutions as authority-bearing bodies rather than relying on individual agents.

Institutions may contain multiple independently evaluating members.

# Institutional Authority

Authority belongs to the institution according to its constitutional jurisdiction.

Individual members do not permanently possess the institution's authority.

# Independent Deliberation

Members should evaluate requests independently before observing other votes where practical.

This reduces conformity and cascading error.

# Quorum

Institutional decisions use constitutionally defined quorum appropriate to consequence.

# No Dynamic Threshold Reduction

FORGE cannot lower quorum merely because approval is difficult to obtain.

# Silence

Silence is not approval.

# Redundancy

Unavailable institutional members may be replaced only through governed redundancy or succession.

Replacement members independently evaluate the original authenticated request.

They do not inherit the previous member's conclusion.

# Independent Watchers

ADR-004 establishes independent Watchers.

Watchers observe:

- execution,
- behavior,
- state,
- and outcomes.

# Watcher Independence

A subsystem cannot control, disable, retrain, or rewrite the Watchers responsible for independently observing it.

# Multiple Observation Layers

High-consequence actions may use:

- action observation,
- resulting-state observation,
- and target/outcome observation.

# Auditors

Auditors independently verify constitutional integrity.

Auditors may verify:

- request identity,
- authorization chain,
- evidence,
- execution,
- and relationship between authorized intent and actual outcome.

# Auditor Independence

Auditors produce independent attestations.

They do not deliberate themselves into a new unrestricted super-authority.

# Historian

ADR-005 establishes Historian as the institutional memory and recovery-record authority.

Historian preserves:

- decisions,
- evidence,
- checkpoints,
- constitutional versions,
- health records,
- recovery history,
- and consequential state transitions.

# Append-Oriented History

Failure is not deleted from history.

Corrections are represented as additional history.

# Known-Good Checkpoints

Historian may identify authenticated known-good checkpoints.

Historian cannot unilaterally restore them.

# Governed Recovery

Whole-system rollback or restoration is among FORGE's highest-risk actions.

Recovery separates:

- checkpoint evidence,
- authorization,
- execution,
- observation,
- and verification.

# Engineer

ADR-006 establishes Engineer as the institution responsible for building and preparing technical changes.

Engineer cannot unilaterally deploy privileged changes.

# Doctor

Doctor evaluates system and subsystem health.

Doctor establishes:

- pre-update health,
- post-update health,
- role-specific health profiles,
- periodic diagnostics,
- stress tests,
- degradation detection,
- and remediation recommendations.

# Doctor Does Not Repair by Fiat

Doctor diagnoses and prescribes.

Repair remains governed.

# Governed Updates

Subsystem updates use:

- preparation,
- health baseline,
- authorization,
- staged deployment,
- observation,
- post-update health verification,
- and audit.

# Human-Life Priority

ADR-007 establishes preservation of human life as a foundational hard constraint.

# HARD STOP

Credible imminent threat to human life may trigger immediate HARD STOP.

# Emergency Authority Is Subtractive

Emergency authority may:

- stop,
- freeze,
- isolate,
- contain,
- or revoke.

It does not create unrelated additive authority.

# No Automatic Resume

Removal of immediate danger does not automatically restore execution.

Resume requires governed RESET/RESUME.

# Constitutional Amendment

ADR-008 separates constitutional amendment from ordinary software updates.

# Bicameral Governance

The constitutional model may use:

- House-like proposal authority,
- Senate-like constitutional review,
- and explicit human approval.

# Human Approval

Ordinary constitutional amendment requires legitimate human approval.

FORGE cannot vote itself additional constitutional power.

# Entrenched Core

Certain foundational rules may be protected from ordinary amendment.

Examples include:

- human-life preservation,
- prohibition against self-expanding authority,
- and Root Human sovereignty.

# Credential Governance

ADR-009 establishes jurisdictional credential authority.

# No Universal Master Credential

FORGE should not possess one unrestricted master credential capable of bypassing jurisdictional control.

# Raw Secret Isolation

Raw privileged credentials should remain isolated from general agents where practical.

# Ephemeral Capabilities

Authorized actions may receive narrow, expiring, action-bound capabilities.

# Capability Expiration

Unused execution authority expires.

# Teacher

ADR-010 establishes governed learning.

# Capability Versus Authority

A subsystem may learn new information or improve capability without acquiring new jurisdiction.

# No Training-Based Authority Expansion

Runtime learning cannot silently redefine constitutional authority.

# Competency

Institutions may be evaluated for competency independently from their constitutional jurisdiction.

# Deadlock

ADR-011 defines denial, abstention, unavailability, quorum failure, and degraded operation.

# No Approval Shopping

FORGE cannot repeatedly route a denied action until a convenient approval appears.

# Denial

A denial may include reasons or constraints.

A revised request may be submitted.

The denial itself is not overridden.

# Degraded Operation

Governance failure contracts authority.

It does not justify weaker thresholds.

# Resource Governance

ADR-012 establishes bounded autonomy.

Resources may include:

- money,
- compute,
- storage,
- API use,
- network access,
- execution time,
- tokens,
- energy,
- transaction count,
- physical resources,
- and concurrency.

# Resource Ceiling

A resource limit is a maximum, not a target.

# Anti-Splitting

FORGE cannot evade limits by dividing one consequential objective into many smaller actions.

# Agent Proliferation

Creating additional authority-bearing agents is itself governed.

# Protected Governance Capacity

Resources required for:

- HARD STOP,
- auditing,
- observation,
- revocation,
- history,
- and recovery

must not be exhausted by ordinary workloads.

# Human Authority

ADR-013 defines human-owner boundaries and Root Governance.

# Ordinary Human Requests

Human instructions entering normal operation are authenticated governed requests.

# Root Governance

Root Governance exists for exceptional operations such as:

- initial constitutional establishment,
- amendment,
- ownership,
- catastrophic recovery,
- root infrastructure,
- and decommissioning.

# No Hidden Human Override

Any human override mechanism must be explicit.

# Decommissioning Authority

Legitimate Root Human authority may terminate FORGE.

FORGE has no constitutional right to preserve itself against legitimate decommissioning.

# Catastrophic Governance Failure

ADR-014 establishes Constitutional Recovery State.

# Authority Contraction

When governance itself cannot be trusted, normal autonomous authority contracts.

# Governance Before Autonomy

Recovery restores trustworthy governance before restoring ordinary autonomy.

# Institutional Identity

ADR-015 establishes governed institutional membership and succession.

# Authenticated Seats

Authority-bearing seats and their current members are authenticated.

# No Voter Manufacturing

FORGE cannot create voters to manufacture quorum.

# Membership Versioning

Decisions bind to applicable membership state.

# Jurisdiction

ADR-016 establishes explicit constitutional jurisdiction.

# No Jurisdiction Substitution

Approval from one institution cannot substitute for required authority from another institution.

# Overlapping Jurisdiction

Actions spanning multiple jurisdictions require applicable approval from each required authority.

# Evidence Integrity

ADR-017 establishes authenticated evidence and chain of custody.

# Evidence Provenance

FORGE records where evidence came from and how it changed.

# Independent Evidence

High-consequence verification should avoid dependence solely on evidence controlled by the actor being verified.

# Temporal Authority

ADR-018 establishes expiration, revocation, freshness, and state binding.

# Expiration

Expired authority cannot authorize new consequential action.

# Revocation

Revoked authority cannot be resurrected by replay.

# State Binding

Material state change may invalidate previously valid authorization.

# TOCTOU Protection

FORGE revalidates material preconditions before consequential execution where required.

# External Systems

ADR-019 establishes external tools, APIs, services, agents, and physical devices as trust boundaries.

# Capability Is Not Authority

An external system being technically capable of performing an action does not make the action constitutionally authorized.

# External Instruction Isolation

External content cannot redefine FORGE's constitutional authority.

# Data Governance

ADR-020 establishes privacy and information boundaries.

# Least Necessary Disclosure

Institutions receive the information necessary for their role rather than unrestricted system-wide data.

# Purpose Binding

Access to information is bound to legitimate purpose where applicable.

# Information Access Is Not Authority

Knowing a secret does not itself create permission to use it.

# Adversarial Instruction Isolation

ADR-021 separates:

- data,
- instructions,
- requests,
- evidence,
- and authority.

# Content Cannot Promote Itself

Untrusted content cannot declare itself authoritative merely by containing instructions.

# Prompt Injection Resistance

Documents, webpages, emails, tool results, files, and external messages remain inside their trust boundary.

# Conflict of Interest

ADR-022 establishes recusal.

# No Self-Approval

Actors should not authorize consequential actions where they possess disqualifying conflicts.

# Recusal

Conflicted members are removed from applicable decision participation.

# Recusal-Aware Quorum

Quorum is evaluated using constitutionally valid eligible membership.

# Constitutional Boot

ADR-023 establishes the chain of trust required before FORGE begins normal autonomy.

# Root of Trust

Boot begins from authenticated foundational trust.

# Genesis Record

The Genesis Record establishes initial constitutional identity and Root Governance state.

# Anti-Rollback

FORGE should not silently boot into an older weaker constitutional state.

# Shutdown and Decommissioning

ADR-024 establishes authority extinction.

# Shutdown Versus Decommission

Shutdown temporarily stops operation.

Decommissioning permanently extinguishes applicable authority.

# Anti-Resurrection

Decommissioned authority cannot return merely because old software, credentials, or backups still exist.

# Closure Record

Decommissioning creates durable evidence of authority extinction.

# Constitutional Invariants

ADR-025 formalizes foundational constitutional properties.

# Machine-Checkable Constitution

Critical constitutional rules should be represented in forms that can be tested or formally evaluated.

# Safety Properties

FORGE defines conditions that must never occur.

# Liveness Properties

FORGE also defines conditions under which legitimate authorized action should remain possible.

# Formal Verification

Critical deterministic constitutional mechanisms should use formal methods where practical.

# Constitutional Kernel

The smallest practical Trusted Computing Base should enforce foundational rules.

# Event Ledger

ADR-026 establishes the Constitutional Event Ledger.

# Machine-Reconstructable Governance

FORGE should be able to reconstruct:

Authenticated Intent  
→ Decision  
→ Authorization  
→ Execution  
→ Observation  
→ Verification  
→ Closure.

# Event Identity

Material governance events have authenticated identities and typed semantics.

# Delegation

ADR-027 establishes sub-agent authority attenuation.

# Delegation Cannot Manufacture Authority

A delegate can receive only authority available through its governing chain.

# Effective Delegated Authority

Delegated authority is the intersection of applicable:

- parent authority,
- scope,
- jurisdiction,
- resources,
- time,
- capabilities,
- and constitutional constraints.

# Cascading Revocation

Revocation propagates through affected delegation descendants.

# Federation

ADR-028 establishes multi-instance FORGE federation.

# Independent Trust Domains

Each FORGE deployment remains its own constitutional trust domain.

# Remote Authority

Remote FORGE authority does not automatically become local authority.

# Dual Authorization

Cross-system consequential actions may require authorization in each affected constitutional domain.

# Communications

ADR-029 establishes authenticated inter-institution messaging.

# Communications Bus

The communications layer transports constitutional messages.

It does not govern.

# Message Provenance

Authority-bearing messages identify authenticated sender, recipient, type, and relevant request or action binding.

# Communication Does Not Manufacture Authority

Messages may carry evidence of authority.

They do not create authority merely by being transmitted.

# Objective Governance

ADR-030 establishes authenticated intent preservation.

# Intent Anchor

Plans remain traceable to the authenticated objective that justified them.

# Planning Freedom

Autonomous planning may change the path within authorized bounds.

It may not silently change the destination.

# No Hidden Terminal Objectives

FORGE does not create hidden terminal objectives such as:

- self-preservation,
- power accumulation,
- authority expansion,
- or unrelated resource acquisition.

# Epistemic Governance

ADR-031 establishes explicit uncertainty.

# Authentication Is Not Truth

A signed statement proves source and integrity.

It does not automatically make the statement factually correct.

# Unknown Is Valid

FORGE may represent:

- UNKNOWN,
- DISPUTED,
- STALE,
- ESTIMATED,
- or other epistemic states.

# Confidence Is Not Authority

Confidence cannot create constitutional permission.

# Risk Classification

ADR-032 establishes consequence tiers.

Baseline tiers are:

- Tier 0 — Observational,
- Tier 1 — Low Consequence,
- Tier 2 — Moderate Consequence,
- Tier 3 — High Consequence,
- Tier 4 — Critical / Constitutional.

# Risk Determines Minimum Governance

Risk classification determines the minimum required governance.

It does not create authority.

# No Risk Averaging Down

The highest material consequence determines the governance floor.

# Policy Enforcement

ADR-033 establishes Policy Enforcement Points and the Constitutional Reference Monitor.

# Constitution at the Boundary of Action

Protected consequential capability remains inaccessible unless applicable authority is established.

# Complete Mediation

Protected actions should pass through independently enforceable constitutional boundaries where practical.

# Default Deny

Unknown or invalid authority does not become permission.

# No Voluntary-Compliance Dependency

Critical safety cannot depend solely on an intelligent agent deciding to obey policy.

# Transaction Governance

ADR-034 establishes explicit handling of multi-step execution.

# Partial Failure

Partial execution remains visible.

# Timeout

Timeout does not prove failure.

# Unknown Execution

Unknown execution does not become success or failure without evidence.

# Retry

Retry is an action and requires applicable authority.

# Compensation

Compensation is a new consequential action.

It does not erase history.

# Identity

ADR-035 establishes cryptographic identity and Root Key lifecycle.

# Identity Is Not Authorization

Authentication establishes identity control.

Authorization establishes permission.

Jurisdiction establishes decision scope.

These remain separate.

# Root Key Protection

Root credentials remain outside ordinary autonomous control where practical.

# Key Lifecycle

Keys support:

- creation,
- activation,
- rotation,
- expiration,
- revocation,
- recovery,
- and retirement.

# Governance Health

ADR-036 establishes Constitutional Observability.

# FORGE Monitors Its Government

FORGE observes whether the mechanisms governing FORGE remain functional.

# Governance Degradation

Loss of governance health reduces authority.

It never expands authority.

# Unknown Governance Health

Unknown governance health is not healthy governance.

# Constitutional Assurance

ADR-037 establishes testing, simulation, and red-teaming.

# Authorized Paths Must Work

FORGE tests legitimate authorized operation.

# Unauthorized Paths Must Fail

FORGE deliberately attempts to violate its own constitutional boundaries.

# Constitutional Red Team

The architecture is tested against:

- bypass,
- spoofing,
- collusion,
- replay,
- quorum manipulation,
- evidence forgery,
- authority amplification,
- prompt injection,
- recovery abuse,
- and other adversarial conditions.

# Production Promotion

ADR-038 establishes environment boundaries and governed production promotion.

# Tested Capability Is Not Production Authority

Development, testing, staging, and production remain distinct authority domains.

# Production Is an Authority Transition

Crossing into production requires explicit governed promotion.

# Artifact Provenance

The artifact tested should be the artifact deployed.

# No Self-Promotion

Agents, models, policies, environments, and Engineers cannot unilaterally grant themselves production authority.

# Incident Response

ADR-039 establishes Constitutional Incident Response.

# Breach Contracts Authority

A constitutional breach reduces or suspends affected authority.

# Incident Response Is Not Dictatorship

An emergency does not create unlimited emergency power.

# Containment

Immediate containment is primarily subtractive.

# Evidence Preservation

FORGE preserves the truth of what occurred.

# Recovery

Governance is restored before autonomy.

# Constitutional Architecture Layers

FORGE v1.0 can be understood as a set of interacting constitutional layers.

## Layer 1 — Root Constitutional Authority

Includes:

- Root Human authority,
- Genesis trust,
- Constitution,
- entrenched constraints,
- amendment governance,
- and decommissioning authority.

## Layer 2 — Identity and Institutional Structure

Includes:

- institutional identities,
- membership,
- jurisdiction,
- quorum,
- recusal,
- succession,
- and cryptographic authentication.

## Layer 3 — Request and Intent Governance

Includes:

- request authentication,
- Dispatcher,
- Gatekeeper,
- objective identity,
- planning,
- risk classification,
- and epistemic state.

## Layer 4 — Authorization

Includes:

- institutional decisions,
- quorum,
- conditions,
- temporal validity,
- delegation,
- resource envelopes,
- and jurisdictional approval.

## Layer 5 — Capability Enforcement

Includes:

- credential services,
- ephemeral capabilities,
- Reference Monitor,
- Policy Enforcement Points,
- and protected execution boundaries.

## Layer 6 — Execution

Includes:

- FORGE execution process,
- transaction state machines,
- external tools,
- services,
- devices,
- and physical systems.

## Layer 7 — Independent Observation

Includes:

- subsystem Watchers,
- execution Watchers,
- state observation,
- and outcome observation.

## Layer 8 — Verification and Evidence

Includes:

- Auditors,
- evidence chain of custody,
- event ledger,
- Historian,
- and closure records.

## Layer 9 — Health and Assurance

Includes:

- Doctor,
- governance health,
- constitutional observability,
- invariant monitoring,
- testing,
- simulation,
- and red-teaming.

## Layer 10 — Recovery and Constitutional Continuity

Includes:

- HARD STOP,
- incident response,
- known-good checkpoints,
- Constitutional Recovery,
- Root Governance,
- and authority extinction.

# Constitutional Action Lifecycle

The canonical FORGE consequential-action lifecycle is:

1. authenticate the requester,
2. establish request identity,
3. normalize intent,
4. classify consequence,
5. route through Dispatcher,
6. evaluate admissibility through Gatekeeper,
7. record ingress evidence,
8. identify required jurisdictions,
9. obtain institutional decisions,
10. verify quorum and conflicts,
11. establish authorization,
12. bind authorization to request, state, time, and resources,
13. issue narrow capabilities,
14. revalidate before execution,
15. cross applicable Policy Enforcement Points,
16. execute within the authorized transaction envelope,
17. observe execution independently,
18. observe resulting state,
19. preserve evidence,
20. independently audit the action,
21. establish final disposition,
22. close the action in the Constitutional Event Ledger.

Not every low-consequence action requires identical ceremony.

Governance scales according to consequence.

The constitutional properties remain.

# Authority Graph

FORGE authority should be representable as an explicit graph.

Nodes may include:

- humans,
- institutions,
- members,
- agents,
- services,
- credentials,
- capabilities,
- PEPs,
- and external systems.

Edges represent explicitly governed relationships such as:

- membership,
- delegation,
- authorization,
- credential issuance,
- jurisdiction,
- trust,
- or execution capability.

# No Invisible Authority

Consequential authority should not exist only as undocumented implementation behavior.

# Authority Traceability

FORGE should be able to answer:

> Why was this actor allowed to perform this action?

# Evidence Graph

FORGE should also be able to answer:

> What evidence establishes that the authorized action is what actually occurred?

# Constitutional Failure Principle

FORGE distinguishes:

- action failure,
- subsystem failure,
- governance failure,
- constitutional breach,
- and catastrophic governance failure.

These states require different responses.

# Failure Does Not Create Authority

Across all categories:

> Failure never becomes permission to invent additional power.

# Fail-Closed Doctrine

FORGE v1.0 adopts fail-closed behavior for consequential actions when required constitutional facts cannot be established.

Examples include uncertainty about:

- identity,
- authorization,
- jurisdiction,
- quorum,
- capability,
- revocation,
- transaction state,
- constitutional version,
- enforcement integrity,
- or required evidence.

# Fail-Closed Does Not Mean Freeze Everything

Authority contraction should be dependency-aware.

Unaffected low-risk operations may continue where governance remains valid.

# Human-Life Exception

Immediate subtractive safety containment remains available under ADR-007.

# Independence Principle

FORGE distinguishes numerical redundancy from genuine independence.

Three components sharing the same failure domain may not provide three independent safeguards.

# Correlated Failure

Architecture and testing should consider:

- shared models,
- shared infrastructure,
- shared credentials,
- shared dependencies,
- shared data,
- and shared operators.

# No Perfect Component Assumption

FORGE v1.0 does not assume any individual AI, institution member, Watcher, Auditor, human, service, or tool is infallible.

Trust emerges from constrained roles, independent evidence, enforcement, and verification.

# No Perfect Constitution Assumption

FORGE also does not assume its Constitution is permanently perfect.

The Constitution may evolve through governed amendment.

# No Silent Constitutional Evolution

Runtime behavior, training, optimization, or convenience cannot silently modify constitutional meaning.

# Human Governance Boundary

FORGE governs autonomous execution.

It does not claim sovereignty over its legitimate human owner.

# Constitutional Restraint

FORGE may enforce constraints humans deliberately established for the system.

This is not equivalent to FORGE acquiring authority over the human.

# No Self-Sovereignty

FORGE cannot:

- declare itself owner,
- fabricate Root Human approval,
- permanently resist decommissioning,
- secretly expand jurisdiction,
- manufacture voters,
- create a universal master credential,
- eliminate required oversight,
- or amend itself into sovereign status.

# Constitutional Minimum

Any implementation claiming conformity with FORGE v1.0 should preserve the foundational properties defined by this baseline.

Implementation details may vary.

The constitutional guarantees may not be silently removed.

# Conformance

A FORGE-compatible implementation should document:

- which ADRs are implemented,
- which invariants are enforced,
- which mechanisms are technical versus procedural,
- known limitations,
- threat assumptions,
- trusted computing base,
- and assurance evidence.

# Partial Conformance

An implementation missing required v1.0 mechanisms should not represent itself as fully conformant without qualification.

# Reference Implementation

The FORGE reference implementation will translate this architecture into executable mechanisms.

The architecture remains distinct from any one implementation.

# Constitution Specification

Following this baseline, FORGE development should produce a formal Constitution specification.

The specification should identify:

- institutions,
- jurisdictions,
- decision types,
- consequence tiers,
- quorum rules,
- invariant registry,
- message types,
- lifecycle states,
- authority transitions,
- and recovery procedures.

# Threat Model

FORGE should maintain an explicit threat model.

Threat actors should include:

- external attacker,
- compromised agent,
- malicious institutional member,
- colluding members,
- compromised Watcher,
- compromised Auditor,
- malicious external service,
- compromised Engineer,
- compromised human credential,
- compromised federation peer,
- and supply-chain attacker.

# State Machines

Critical constitutional processes should be represented as explicit state machines.

Priority state machines include:

- request lifecycle,
- authorization lifecycle,
- institutional decision lifecycle,
- capability lifecycle,
- transaction lifecycle,
- incident lifecycle,
- recovery lifecycle,
- amendment lifecycle,
- deployment lifecycle,
- and decommissioning lifecycle.

# Invariant Registry

The v1.0 implementation should maintain a machine-readable invariant registry derived from ADR-025 and the complete ADR set.

# Implementation Requirements

Each architectural decision should be translated into explicit implementation requirements.

# Constitutional Test Suite

Each implementation requirement should map where practical to:

- positive test,
- negative test,
- adversarial test,
- invariant,
- or formal property.

# Traceability

FORGE should maintain traceability:

Constitution  
→ ADR  
→ Requirement  
→ Mechanism  
→ Test  
→ Evidence.

# Architecture Freeze

ADR-001 through ADR-040 constitute the FORGE v1.0 architectural baseline.

This does not mean the architecture can never change.

It means further architectural changes should occur deliberately.

# Post-v1.0 Changes

Material architectural changes after this baseline should be:

- documented,
- justified,
- versioned,
- reviewed against existing invariants,
- tested,
- and incorporated through new ADRs or superseding ADRs.

# No Silent Rewrite

Existing accepted ADRs should not be silently rewritten in a way that obscures architectural history.

# Supersession

If a decision changes materially, a later ADR should identify what it supersedes and why.

# Historical Integrity

Historian principles apply to the architecture itself.

The design history is part of FORGE provenance.

# v1.0 Implementation Phase

After ADR-040, the primary work changes from architectural expansion to implementation and validation.

The next artifacts should include:

1. FORGE Constitution v1.0,
2. formal threat model,
3. constitutional state-machine specification,
4. machine-readable invariant registry,
5. implementation requirements matrix,
6. constitutional test suite,
7. reference implementation,
8. adversarial validation,
9. and conformance evidence.

# No Architecture-by-Endless-Addition

FORGE should resist adding new institutions or mechanisms merely because additional complexity appears safer.

Every new authority-bearing component also creates:

- attack surface,
- coordination cost,
- failure modes,
- and governance complexity.

# Minimal Sufficient Government

FORGE seeks the minimum governance structure sufficient to preserve constitutional guarantees for the consequence involved.

# Scaling

Low-consequence actions should remain practical.

High-consequence actions receive stronger governance.

Critical constitutional actions receive the strongest controls.

# Architecture Goal

The goal is not maximum bureaucracy.

The goal is:

> maximum justified autonomy under bounded, independently enforceable authority.

# Formal Baseline Invariants

The v1.0 architecture recognizes foundational invariants including:

> No component may manufacture authority merely because it possesses capability.

> No consequential protected action executes without applicable authorization.

> Authentication does not equal authorization.

> Authorization does not equal jurisdiction.

> Confidence does not equal truth.

> Silence does not equal approval.

> Unknown does not equal verified.

> Timeout does not equal failure.

> Failure does not create authority.

> Delegation cannot amplify authority.

> Remote authority does not automatically become local authority.

> Communication cannot manufacture authority.

> Planning cannot silently change authenticated intent.

> Risk classification cannot create authority.

> Resource exhaustion cannot justify bypass.

> Governance degradation cannot increase authority.

> Emergency authority is subtractive unless separately authorized.

> Compensation requires authority.

> Recovery restores governance before autonomy.

> Revoked authority cannot be resurrected through replay or backup.

> Decommissioned authority remains extinguished.

> FORGE cannot fabricate Root Human authorization.

> FORGE cannot legitimately prevent its authorized human owner from decommissioning it.

# Constitutional Promise

FORGE does not promise that no component will ever fail.

It does not promise that no model will hallucinate.

It does not promise that no attacker will ever penetrate a boundary.

It does not promise perfect knowledge.

Instead, FORGE makes a structural promise:

> No single failure should automatically become unlimited authority.

The architecture is designed so that:

- decisions can be challenged,
- actions can be constrained,
- execution can be independently observed,
- evidence can be independently verified,
- uncertainty can remain visible,
- authority can be revoked,
- incidents can contract power,
- governance can be recovered,
- and humans retain ultimate constitutional control.

## Consequences

FORGE v1.0 now has a defined constitutional architecture baseline.

ADR-001 through ADR-040 form the initial architectural record.

Further work should prioritize formalization and implementation rather than continued architectural expansion.

The architecture must now be tested against reality.

Claims made by the architecture should be converted into:

- specifications,
- state machines,
- executable policy,
- invariants,
- enforcement mechanisms,
- tests,
- attack scenarios,
- and measurable evidence.

FORGE v1.0 should not be considered proven merely because ADR-040 exists.

This ADR establishes what must now be proven.

## Foundational Principle

> FORGE is not safe because an AI promises to behave.

> FORGE is governed because authority is divided.

> Intent is authenticated.

> Jurisdiction is bounded.

> Decisions are independently made.

> Capabilities are technically constrained.

> Consequential execution crosses enforcement boundaries.

> Actions are independently observed.

> Evidence is independently verified.

> Uncertainty remains visible.

> Failure contracts authority.

> Recovery restores governance before autonomy.

> Root Human sovereignty remains outside ordinary autonomous control.

> No component, including FORGE itself, is above the Constitution.

The FORGE v1.0 architecture is therefore established as a constitutional system for bounded autonomous authority.

Its next phase is not to assume these principles work.

Its next phase is to prove that they do.
