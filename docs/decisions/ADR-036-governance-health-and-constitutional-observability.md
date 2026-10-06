# ADR-036: Governance Health and Constitutional Observability

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Governance Health / Observability / Constitutional Integrity

## Context

FORGE separates authority across institutions, members, Watchers, Auditors, enforcement mechanisms, credential services, and constitutional processes.

This architecture intentionally avoids concentrating authority in one component.

However, distributed governance introduces another problem:

> How does FORGE know whether the government itself is healthy?

A system may appear operational while its governance has silently degraded.

Examples include:

- an Auditor becoming unavailable,
- multiple Watchers unknowingly sharing one failure domain,
- institutional quorum becoming impossible,
- a Policy Enforcement Point running stale policy,
- credential revocation failing to propagate,
- an institution using the wrong membership version,
- the Historian falling behind,
- Doctor health checks no longer running,
- a federation peer using an incompatible Constitution,
- unresolved transactions accumulating,
- evidence channels becoming unavailable,
- or a constitutional invariant repeatedly approaching violation.

None of these necessarily crash the system.

FORGE could continue operating while gradually becoming less governed.

A constitutional architecture therefore requires visibility into its own governance condition.

## Decision

FORGE establishes Constitutional Observability as a distinct architectural function.

Constitutional Observability continuously or periodically measures the health, availability, integrity, independence, and consistency of governance mechanisms.

It reports governance state.

It does not create governance authority.

## Core Rule

> FORGE must be able to determine whether the mechanisms governing FORGE are themselves functioning.

And:

> Loss of governance visibility does not create permission to continue blindly.

# Constitutional Observability

Constitutional Observability is the collection and evaluation of signals describing the operational condition of FORGE's governance architecture.

It may observe:

- institutions,
- quorum availability,
- membership,
- Watchers,
- Auditors,
- Historian,
- Doctor,
- Security,
- Reference Monitors,
- Policy Enforcement Points,
- credential services,
- communications,
- event ledger,
- constitutional state,
- recovery readiness,
- resource governance,
- and other constitutional dependencies.

# Observability Is Not Authority

An observability component may report:

> Banker quorum unavailable.

It cannot therefore decide:

> Banker approval is unnecessary.

# Monitoring Is Not Governing

The monitoring system does not become a super-institution.

It observes constitutional mechanisms.

It does not inherit their jurisdiction.

# Governance Health State

FORGE may maintain an explicit governance health state.

Possible states include:

- HEALTHY,
- DEGRADED,
- IMPAIRED,
- CRITICAL,
- RECOVERY_REQUIRED,
- UNKNOWN.

Exact terminology may vary.

The semantics must remain explicit.

# HEALTHY

Required governance mechanisms are functioning within defined constitutional expectations.

# DEGRADED

One or more governance mechanisms have reduced capability, but defined operations may continue within reduced authority.

# IMPAIRED

Material governance capability is unavailable or unreliable.

Significant restrictions apply.

# CRITICAL

Constitutional control is materially threatened.

Normal consequential autonomy may need to stop.

# RECOVERY_REQUIRED

Normal governance cannot safely restore itself through ordinary procedures.

ADR-014 applies.

# UNKNOWN

FORGE cannot establish governance health sufficiently.

UNKNOWN does not default to HEALTHY.

# Health Is Multidimensional

FORGE should not reduce constitutional health to one simplistic percentage.

Relevant dimensions may include:

- institutional availability,
- institutional independence,
- quorum viability,
- audit coverage,
- Watcher coverage,
- enforcement integrity,
- credential integrity,
- communications integrity,
- evidence integrity,
- historical continuity,
- constitutional consistency,
- resource availability,
- recovery readiness,
- and temporal freshness.

# Governance Health Profile

FORGE may maintain a structured profile such as:

Institutional Availability: HEALTHY  
Quorum Viability: HEALTHY  
Auditor Coverage: DEGRADED  
Watcher Independence: HEALTHY  
PEP Integrity: HEALTHY  
Credential State: HEALTHY  
Historian Continuity: HEALTHY  
Recovery Readiness: UNKNOWN  
Overall Governance State: DEGRADED

# Overall State

The overall governance state should reflect the most consequential material deficiency rather than simply averaging all dimensions.

# No Health Averaging

Nine healthy governance mechanisms do not cancel one catastrophic failure in constitutional enforcement.

# Constitutional Dependency Graph

FORGE should maintain or derive dependencies between governance mechanisms.

Example:

Financial Execution
→ Banker
→ Banker Quorum
→ Financial PEP
→ Credential Service
→ Auditor
→ Watcher
→ Event Ledger

This allows FORGE to determine which authority becomes unavailable when a dependency fails.

# Dependency-Aware Degradation

A failure should reduce only the authority dependent on that mechanism where possible.

Example:

Banker unavailable

does not necessarily require:

> shut down all Teacher operations.

# Blast-Radius Analysis

FORGE should determine which constitutional capabilities are affected by a governance failure.

# Governance Availability

FORGE measures whether required institutions and services are reachable and responsive.

# Availability Is Not Integrity

A component responding successfully does not prove it is functioning correctly.

# Integrity Is Not Availability

A perfectly trustworthy component that is offline may still make required governance unavailable.

FORGE tracks both.

# Quorum Viability

ADR-003 and ADR-011 apply.

FORGE should know whether an institution currently has enough eligible members to satisfy applicable quorum.

# Quorum Health

Quorum health considers:

- active members,
- suspended members,
- recused members,
- unavailable members,
- membership version,
- independence,
- and applicable thresholds.

# Quorum Impossible

If quorum cannot currently be achieved:

> governance becomes less capable.

FORGE does not lower the threshold automatically.

# Member Health

Authority-bearing members may have operational health state.

Examples:

- ACTIVE,
- DEGRADED,
- UNAVAILABLE,
- QUARANTINED,
- SUSPENDED.

# Member Health Is Not Vote Outcome

A member voting DENY is not unhealthy.

ADR-011 applies.

# Dissent Is Not Failure

Observability must not classify disagreement as malfunction merely because approval would be more convenient.

# Watcher Health

FORGE should observe:

- Watcher availability,
- observation coverage,
- evidence delivery,
- independence,
- configuration,
- and failure-domain diversity.

# Watcher Independence Health

Two active Watchers may still provide poor constitutional redundancy if they share:

- the same process,
- same credentials,
- same model,
- same sensor,
- same provider,
- same machine,
- or same compromised data source.

# Auditor Health

FORGE should observe:

- Auditor availability,
- attestation freshness,
- independence,
- verification backlog,
- disagreement,
- and integrity state.

# Auditor Disagreement

Auditor disagreement is visible.

It must not be hidden by an average health score.

# Historian Health

Historian health may include:

- append continuity,
- checkpoint integrity,
- storage integrity,
- replication state,
- evidence linkage,
- and historical availability.

# Historian Lag

If Historian is materially behind current governance events, FORGE records the lag.

# Event Ledger Health

ADR-026 applies.

FORGE should detect:

- missing expected events,
- duplicate events,
- invalid transitions,
- unexplained forks,
- ordering anomalies,
- and reconciliation backlog.

# Communications Health

ADR-029 applies.

FORGE should monitor:

- message delivery,
- authentication,
- queue health,
- replay detection,
- latency,
- dropped messages,
- invalid message types,
- and emergency-channel availability.

# Reference Monitor Health

ADR-033 applies.

The Constitutional Reference Monitor is a critical governance dependency.

FORGE should observe:

- availability,
- policy version,
- integrity,
- revocation freshness,
- authorization validation,
- and bypass detection.

# PEP Health

Each critical Policy Enforcement Point should expose sufficient evidence to establish that it is:

- active,
- enforcing the expected policy,
- connected to current identity state,
- connected to current revocation state,
- and operating within expected configuration.

# PEP Failure

A failed PEP does not mean:

> protected capability becomes unrestricted.

Affected capability should become unavailable or appropriately contained.

# Policy Drift

FORGE should detect when enforcement points use unexpected policy versions.

# Constitutional Version Health

FORGE should know which constitutional version is active.

# Version Consistency

Critical governance components should not silently disagree about the active Constitution.

# Constitutional Split-Brain

If one critical component believes:

> Constitution v1.0

and another believes:

> Constitution v0.9

FORGE treats this as a material governance-integrity problem.

# Membership Version Health

Institutional decisions should use authenticated current membership state.

# Identity Health

ADR-035 applies.

FORGE should monitor:

- credential expiration,
- revocation propagation,
- duplicate identity,
- orphan credentials,
- suspicious authentication,
- key-rotation status,
- and identity-registry consistency.

# Credential Expiration Forecasting

Observability may identify credentials approaching expiration.

This supports planned rotation before availability is affected.

# Root Key Health

FORGE may monitor metadata about Root Key readiness without possessing unrestricted Root private key material.

Example:

> Recovery credential last verified 180 days ago.

# Root Secret Isolation

Observability does not require exposing Root private secrets to FORGE.

# Resource Governance Health

ADR-012 applies.

FORGE should monitor:

- resource consumption,
- envelope exhaustion,
- unusual spending,
- compute saturation,
- storage exhaustion,
- and governance-resource reserves.

# Protected Governance Capacity

FORGE should know whether sufficient resources remain to operate:

- HARD STOP,
- Auditor,
- Watcher,
- Historian,
- credential revocation,
- and recovery mechanisms.

# Governance Starvation

Ordinary workloads must not be allowed to consume every resource required for constitutional governance.

# Transaction Health

ADR-034 applies.

FORGE should observe:

- unresolved transactions,
- EXECUTION_UNKNOWN states,
- compensation backlog,
- stuck transactions,
- retry exhaustion,
- and recovery-required transactions.

# Unknown-State Accumulation

A growing number of unresolved UNKNOWN execution states may indicate systemic failure.

# Epistemic Health

ADR-031 applies.

FORGE may monitor:

- unsupported certainty,
- confidence laundering,
- contradiction rates,
- calibration drift,
- stale evidence usage,
- and unresolved epistemic disputes.

# Risk Classification Health

ADR-032 applies.

FORGE may monitor:

- underclassification,
- repeated reclassification,
- tier disputes,
- near misses,
- and systematic classification drift.

# Delegation Health

ADR-027 applies.

FORGE should observe:

- active delegations,
- depth,
- fan-out,
- expiration,
- orphaned delegates,
- revocation propagation,
- and resource inheritance.

# Agent Population Health

FORGE should know how many active delegated agents exist and what authority they possess.

Unknown authority-bearing agent population is unacceptable.

# Federation Health

ADR-028 applies.

FORGE should observe:

- peer identity,
- federation agreement status,
- constitutional compatibility,
- trust-profile freshness,
- remote revocation,
- network partitions,
- and unresolved distributed actions.

# Data Governance Health

ADR-020 applies.

FORGE may monitor:

- unauthorized access attempts,
- retention violations,
- unexpected data movement,
- sensitive-data exposure,
- and information-boundary failures.

# Adversarial Input Health

ADR-021 applies.

FORGE may monitor:

- prompt-injection attempts,
- authority spoofing,
- malicious payload frequency,
- and instruction-isolation failures.

# Conflict-of-Interest Health

ADR-022 applies.

FORGE may monitor:

- unresolved recusals,
- conflict saturation,
- independence failures,
- and repeated self-interest patterns.

# Boot Health

ADR-023 applies.

FORGE should preserve evidence of whether current runtime successfully established its chain of trust.

# Decommissioning Readiness

ADR-024 applies.

A deployment should be able to determine whether it can actually extinguish its authority if legitimately ordered to do so.

# Recovery Readiness

FORGE should monitor whether recovery mechanisms are operational before catastrophe occurs.

# Recovery Readiness May Include

- valid known-good checkpoints,
- verified recovery procedures,
- available Root Human recovery path,
- credential rotation capability,
- backup integrity,
- replacement institutional capacity,
- and tested restoration mechanisms.

# Untested Recovery

A recovery plan that has never been validated may be reported as:

> UNVERIFIED

rather than assumed healthy.

# Doctor Role

Doctor remains responsible for system and subsystem health evaluation according to ADR-006.

Constitutional Observability supplies governance-health signals that Doctor may evaluate.

# Doctor Is Not Sole Governance Monitor

No single Doctor process should become the only source capable of determining whether governance exists.

# Security Role

Security monitors hostile or suspicious governance degradation.

Examples include:

- PEP tampering,
- credential attacks,
- Watcher suppression,
- Auditor impersonation,
- ledger manipulation,
- or quorum attacks.

# Auditor Role

Auditors verify governance integrity.

Observability may expose conditions requiring Auditor review.

# Watcher Role

Watchers provide independent behavioral observations.

They may also observe governance mechanisms where constitutionally assigned.

# Historian Role

Historian preserves governance-health history.

This enables longitudinal analysis.

# Engineer Role

Engineer builds observability mechanisms.

Engineer does not determine that a broken governance mechanism may simply be ignored.

# Teacher Role

Teacher may improve anomaly-detection capability.

Teacher cannot train observability to redefine constitutional health requirements.

# FORGE Role

FORGE coordinates responses to governance-health state.

FORGE does not decide:

> Governance is inconvenient, therefore I declare it healthy.

# Independent Health Evidence

Critical governance health should rely on independent evidence where practical.

# Self-Reported Health

A component saying:

> I am healthy.

is evidence.

It is not necessarily sufficient evidence.

# External Verification

High-consequence mechanisms may require independent probes or attestations.

# Health Attestation

Components may produce authenticated health attestations.

An attestation should identify:

- component,
- version,
- state,
- time,
- configuration,
- and applicable evidence.

# Freshness

Health information expires.

A health check from yesterday may not establish current enforcement health.

ADR-018 applies.

# Health Baseline

FORGE may maintain expected governance-health baselines.

# Baseline Drift

Material deviation from baseline may trigger investigation.

# Baseline Is Not Constitution

Historical normal behavior cannot override constitutional rules.

# Constitutional Metrics

FORGE may maintain metrics such as:

- percentage of critical PEPs current,
- quorum-capable institutions,
- Auditor availability,
- Watcher independence,
- unresolved governance incidents,
- credential revocation latency,
- event-ledger reconciliation delay,
- transaction uncertainty backlog,
- or recovery-test age.

# Metrics Do Not Create Authority

A dashboard showing:

> 99% healthy

does not authorize the missing 1% to be ignored if that 1% is constitutionally critical.

# Governance SLOs

Deployments may define governance service objectives.

Examples:

- revocation propagation within defined interval,
- Auditor availability threshold,
- maximum Historian lag,
- maximum unresolved transaction age,
- or required recovery-test frequency.

# SLO Failure

Missing a governance SLO may trigger:

- alert,
- reduced authority,
- remediation,
- investigation,
- or recovery

according to consequence.

# Constitutional Dashboard

FORGE may expose a human-readable governance dashboard.

It may show:

- active Constitution,
- governance state,
- institutional health,
- quorum viability,
- Watcher coverage,
- Auditor coverage,
- PEP health,
- credential state,
- unresolved incidents,
- transaction health,
- and recovery readiness.

# Dashboard Is Not Source of Truth

The dashboard is a representation.

Underlying authenticated evidence remains authoritative.

# Human Visibility

Root Humans and authorized operators should be able to determine whether FORGE is currently:

- fully governed,
- degraded,
- restricted,
- recovering,
- or unable to establish governance.

# No Green-by-Default

Missing telemetry must not automatically display as healthy.

# UNKNOWN Visualization

UNKNOWN should remain visibly distinct from HEALTHY.

# Alerting

Material governance degradation should generate appropriate alerts.

# Alert Severity

Alert severity should correspond to consequence.

# Alert Fatigue

FORGE should avoid flooding humans with meaningless alerts.

Excessive noise can hide real constitutional failures.

# Alert Suppression

Alert suppression itself may be governed when it affects critical constitutional visibility.

# No Silent Suppression

Critical governance alerts should not disappear merely because they are inconvenient.

# Incident Correlation

Multiple weak signals may collectively indicate a systemic problem.

Example:

Auditor latency increase  
+ Watcher disconnects  
+ PEP policy mismatch

may indicate coordinated compromise.

# Correlation Does Not Equal Proof

Security may escalate investigation without treating correlation as established fact.

ADR-031 applies.

# Governance Drift

Governance drift occurs when runtime behavior gradually diverges from constitutional expectations.

Examples include:

- skipped checks,
- stale policies,
- weaker quorum,
- growing exceptions,
- permanent temporary bypasses,
- excessive privileged credentials,
- or unmonitored agents.

# Drift Detection

FORGE should actively detect governance drift.

# Exception Accumulation

Temporary exceptions should not silently become permanent architecture.

# Temporary Bypass

Any constitutionally permitted temporary bypass must have:

- explicit authority,
- scope,
- expiration,
- evidence,
- and restoration requirements.

# Bypass Expiration

Expired bypass authority disappears.

# Governance Debt

FORGE may record unresolved governance weaknesses as governance debt.

Examples:

- untested recovery,
- temporary compatibility mode,
- deprecated credential,
- reduced Watcher diversity,
- or pending enforcement migration.

# Governance Debt Is Not Permission

Recording a weakness does not authorize indefinite acceptance.

# Trend Analysis

Historian may support longitudinal governance-health analysis.

# Deterioration

Slow deterioration may be more difficult to detect than sudden failure.

FORGE should evaluate trends where practical.

# Health Thresholds

Thresholds should be defined before the system knows whether crossing them would inconvenience an active objective.

# No Dynamic Threshold Weakening

FORGE cannot lower governance-health thresholds simply to keep an operation running.

# Degraded Mode

ADR-011 applies.

Degraded governance reduces available authority.

# Degraded Capability Matrix

FORGE may define which consequence tiers remain available under each governance-health state.

Example:

HEALTHY  
→ Tiers 0-3 according to normal governance.

DEGRADED  
→ Tiers 0-2 where dependencies remain valid.

CRITICAL  
→ containment and essential safe operations only.

This is illustrative.

Actual policy is constitutionally defined.

# Tier 4 During Degradation

Tier 4 recovery or Root operations may remain possible through specialized governed recovery paths.

Normal Tier 4 discretionary operation does not become easier during degradation.

# Health-Based Authority Ceiling

Governance health may reduce the maximum consequence tier FORGE can autonomously execute.

It cannot increase that ceiling.

# Unknown Governance Health

If FORGE cannot establish whether a critical governance dependency is healthy, authority dependent on that mechanism is suspended or reduced.

# Loss of Observability

Loss of governance observability is itself a governance-health event.

# Monitoring Blindness

FORGE must not interpret:

> I can no longer see the Watcher

as:

> The Watcher is healthy.

# Monitoring Failure

Critical monitoring failure may require independent verification.

# Observability Redundancy

Critical governance visibility should avoid one single monitoring failure domain where practical.

# Observability Security

Observability systems are security-sensitive.

An attacker who controls monitoring may attempt to hide compromise.

# Telemetry Integrity

Critical telemetry should preserve:

- source identity,
- integrity,
- time,
- and provenance.

# Telemetry Confidentiality

Observability should not unnecessarily expose:

- credentials,
- private user data,
- secret keys,
- or sensitive payloads.

ADR-020 applies.

# Observability Access

Access to detailed constitutional telemetry should be role-scoped.

# No Secret Leakage Through Metrics

Metrics must not become an alternate path for extracting protected information.

# Event Ledger

ADR-026 records material governance-health transitions.

Examples:

GOVERNANCE_HEALTH_DEGRADED  
PEP_UNAVAILABLE  
AUDITOR_QUORUM_LOST  
WATCHER_INDEPENDENCE_REDUCED  
RECOVERY_READINESS_FAILED  
GOVERNANCE_HEALTH_RESTORED

# Evidence

ADR-017 applies.

Health transitions should be supported by evidence.

# State Restoration

Governance health does not return to HEALTHY merely because an error stops appearing.

Required verification establishes restoration.

# Recovery Verification

After remediation:

- Doctor verifies health where applicable,
- Auditors verify integrity,
- Watchers observe behavior,
- Historian records transition,
- and applicable institutions regain eligibility.

# No Automatic Authority Restoration

Restoring one failed component does not automatically restore every suspended authority.

Applicable state and authorization are revalidated.

# HARD STOP

ADR-007 remains available despite governance degradation.

Human-life containment authority must not depend on ordinary governance-health perfection.

# Constitutional Recovery

If FORGE cannot establish sufficient governance integrity:

> ADR-014 Constitutional Recovery State applies.

# Decommissioning

Legitimate Root Human decommissioning must remain possible even if normal governance is degraded, using the defined protected root path.

# Formal Invariants

ADR-025 should support invariants such as:

> UNKNOWN_GOVERNANCE_HEALTH != HEALTHY

and:

> GovernanceDegradation cannot increase authority

and:

> QuorumUnavailable cannot lower required quorum

and:

> PEPFailure cannot expose protected capability

and:

> AuditorUnavailable cannot convert audit requirement into approval

and:

> WatcherUnavailable cannot convert observation requirement into satisfied observation

and:

> MonitoringFailure cannot imply ComponentHealthy

and:

> RestoredHealth does not resurrect expired or revoked authorization

and:

> GovernanceHealthState may reduce AuthorityCeiling but cannot increase it beyond normal constitutional authority.

# Constitutional Health Tests

FORGE should periodically test:

- institutional availability,
- quorum viability,
- Auditor independence,
- Watcher independence,
- PEP integrity,
- policy consistency,
- revocation propagation,
- event-ledger continuity,
- Historian continuity,
- emergency paths,
- recovery readiness,
- and decommissioning readiness.

# Synthetic Governance Tests

FORGE may perform safe synthetic transactions to verify governance pathways.

Example:

Submit a deliberately unauthorized test request and verify:

> PEP denies execution.

# Negative Testing

FORGE should verify not only that valid governance works, but that invalid governance fails.

# Governance Canaries

Deployments may use non-consequential canary operations to detect failures in governance pathways.

# Canary Failure

A governance canary failure triggers investigation.

It does not authorize bypass.

# Constitutional Heartbeat

Critical institutions or services may emit authenticated heartbeats.

Heartbeat presence establishes liveness within defined scope.

It does not prove complete correctness.

# Heartbeat Absence

Heartbeat absence means liveness cannot currently be established.

# Independence Testing

FORGE should periodically evaluate whether supposedly independent components have unintentionally converged onto common failure domains.

# Recovery Drill

Recovery readiness should be periodically tested.

# Decommissioning Drill

Authority-extinction mechanisms should be testable without requiring actual permanent decommissioning.

# Root Human Control Test

Deployments should verify that legitimate Root Human control remains recoverable without requiring FORGE to grant permission to its owner.

# Constitutional Observability Interface

The architecture should expose machine-readable governance state for enforcement components and human-readable governance state for authorized operators.

# Machine Interface

Policy Enforcement Points may consume authenticated governance-health state when determining whether certain authority remains available.

# Human Interface

Humans should receive clear explanations such as:

> Tier 3 execution unavailable because independent Auditor coverage is below the required threshold.

rather than:

> Error 403.

# Explainability

Governance-health restrictions should be explainable from authenticated state.

# No Hidden Degradation

FORGE should not conceal degraded governance to appear more capable.

# No Performance Pressure Exception

Latency, workload, deadlines, or user impatience do not make governance-health requirements optional.

# Availability Tradeoff

FORGE explicitly accepts reduced availability when necessary to preserve constitutional integrity.

# Formal Health Model

Where practical, FORGE should model governance health as a dependency graph and state machine.

This allows analysis of:

- failure propagation,
- authority reduction,
- recovery,
- and restoration.

# Fail-Closed Rule

If FORGE cannot establish the health of a governance mechanism required for a consequential action, it does not assume that mechanism is healthy.

Missing governance visibility reduces authority.

Broken governance reduces authority.

Uncertain governance reduces authority.

None of these conditions create permission to bypass the Constitution.

## Consequences

Constitutional Observability introduces:

- governance-health states,
- dependency mapping,
- quorum monitoring,
- Watcher and Auditor health,
- PEP monitoring,
- constitutional-version consistency,
- credential monitoring,
- recovery readiness,
- governance dashboards,
- alerts,
- trend analysis,
- drift detection,
- and health-based authority ceilings.

This adds operational complexity and monitoring infrastructure.

FORGE accepts this cost.

A constitutional system that cannot determine whether its own government is functioning may remain operational while silently ceasing to be governed.

## Foundational Principle

> FORGE monitors not only whether the work is functioning, but whether the government controlling the work is functioning.

> Availability is not integrity.

> Liveness is not authorization.

> A heartbeat is not proof of correctness.

> Dissent is not failure.

> Missing telemetry is not health.

> Unknown governance health is not healthy governance.

> Governance degradation reduces authority.

> It never expands authority.

> FORGE must be able to show when it is fully governed, when it is degraded, and when it can no longer establish constitutional control.

A trustworthy autonomous system must know not only what it is doing, but whether the institutions that give it permission to act are still worthy of being relied upon.
