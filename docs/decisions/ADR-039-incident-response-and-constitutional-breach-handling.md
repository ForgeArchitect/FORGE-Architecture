# ADR-039: Incident Response and Constitutional Breach Handling

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Incident Response / Constitutional Breach / Containment

## Context

FORGE is designed to prevent unauthorized consequential action through constitutional governance.

However, no architecture should assume prevention will always succeed.

Failures may occur because of:

- software defects,
- model defects,
- credential compromise,
- human error,
- malicious insiders,
- external attackers,
- compromised dependencies,
- incorrect policy,
- Policy Enforcement Point failure,
- quorum manipulation,
- forged evidence,
- Watcher failure,
- Auditor compromise,
- communications failure,
- identity compromise,
- deployment error,
- physical-system failure,
- or previously unknown attack techniques.

FORGE therefore requires an explicit answer to:

> What happens if the Constitution is actually violated?

This is different from an ordinary application error.

A constitutional breach may mean that an action occurred:

- without valid authorization,
- outside authorized scope,
- outside jurisdiction,
- after revocation,
- after expiration,
- without required quorum,
- without required observation,
- through an enforcement bypass,
- using forged identity,
- or contrary to a foundational invariant.

FORGE must detect, contain, investigate, recover from, and learn from such events without allowing the incident itself to become justification for unlimited authority.

## Decision

FORGE establishes a governed Constitutional Incident Response process.

A constitutional incident is any event that materially threatens or violates the integrity of FORGE's governance architecture.

Incident response prioritizes:

1. human safety,
2. containment,
3. prevention of additional unauthorized effects,
4. preservation of evidence,
5. establishment of actual state,
6. authority reduction,
7. investigation,
8. governed remediation,
9. independently verified recovery,
10. and institutional learning.

## Core Rule

> A constitutional breach contracts authority.

It does not expand it.

And:

> Incident response may contain danger immediately, but it does not create unlimited emergency power.

# Constitutional Incident

A Constitutional Incident is an event or condition affecting the integrity of FORGE governance.

Examples include:

- unauthorized execution,
- PEP bypass,
- fabricated approval,
- forged quorum,
- compromised Root credential,
- unauthorized privilege expansion,
- jurisdiction bypass,
- authority amplification,
- hidden execution route,
- unauthorized constitutional modification,
- evidence tampering,
- Watcher suppression,
- Auditor forgery,
- unauthorized production promotion,
- decommissioning failure,
- or resurrection of revoked authority.

# Security Incident Versus Constitutional Incident

A security incident does not always become a constitutional incident.

Example:

An attacker scans a closed network port.

This may be a security event without constitutional impact.

However:

An attacker uses a stolen credential to obtain protected execution.

This is both a security incident and a constitutional incident.

# Operational Incident

An operational failure may become constitutional when it affects governance.

Example:

A disk failure is operational.

If that disk failure disables the only active PEP and protected capability becomes reachable without enforcement, the condition becomes constitutional.

# Near Miss

A near miss occurs when a constitutional violation was attempted or nearly occurred but was prevented.

Near misses are preserved and analyzed.

# Near Misses Matter

FORGE should not discard a prevented attack merely because no final harm occurred.

# Incident Identity

Each material incident receives a unique identity.

Example:

`INC-2026-0017`

# Incident Record

The incident record may include:

- Incident ID,
- detection time,
- affected systems,
- affected identities,
- constitutional rules involved,
- current consequence classification,
- containment state,
- known facts,
- unknown facts,
- evidence,
- actions taken,
- recovery state,
- and final disposition.

# Incident State Machine

An incident may progress through states such as:

- SUSPECTED,
- CONFIRMED,
- CONTAINING,
- CONTAINED,
- INVESTIGATING,
- REMEDIATING,
- RECOVERING,
- MONITORING,
- CLOSED,
- or RECOVERY_REQUIRED.

Exact terminology may vary.

The semantics must remain explicit.

# SUSPECTED

Evidence indicates a possible constitutional problem.

The facts are not yet sufficiently established.

# CONFIRMED

Available evidence establishes that a constitutional incident occurred or that containment must proceed as though it occurred.

# CONTAINING

FORGE is actively limiting additional consequences.

# CONTAINED

The known immediate ability of the incident to create additional unauthorized effects has been sufficiently restricted.

# INVESTIGATING

FORGE is determining:

- what happened,
- how it happened,
- what was affected,
- what authority was compromised,
- and what remains uncertain.

# REMEDIATING

The underlying defect or compromise is being corrected.

# RECOVERING

Trusted operation is being restored.

# MONITORING

Recovered systems are under heightened observation.

# CLOSED

Required investigation, remediation, recovery, verification, and recording have reached the defined closure criteria.

# RECOVERY_REQUIRED

Normal incident procedures cannot establish trustworthy governance.

ADR-014 applies.

# Classification

Incidents should be classified according to actual and potential consequence.

ADR-032 applies.

# Incident Severity

Possible severity levels may include:

- informational,
- low,
- moderate,
- high,
- critical,
- or constitutional emergency.

Exact labels are deployment policy.

# Severity Does Not Create Authority

Calling an incident:

> CRITICAL

does not grant unrestricted powers.

# Safety Priority

ADR-007 applies.

Credible imminent danger to human life triggers HARD STOP or applicable immediate containment.

# Immediate Containment

Containment may include:

- stopping execution,
- freezing capabilities,
- revoking credentials,
- isolating components,
- blocking network paths,
- suspending institutions,
- disabling compromised integrations,
- freezing transactions,
- or reducing authority ceilings.

# Containment Is Subtractive

Containment primarily removes or restricts capability.

This allows FORGE to react rapidly without creating broad additive authority.

# Emergency Isolation

A compromised component may be isolated before full investigation is complete when continuing operation creates unacceptable risk.

# Isolation Is Not Guilt

Isolation may be precautionary.

FORGE distinguishes:

> isolated pending investigation

from:

> proven malicious.

# Evidence Before Modification

Where safe, FORGE preserves evidence before altering affected systems.

# Safety Exception

Evidence preservation must not delay immediate action required to protect human life.

# Evidence Integrity

ADR-017 applies.

Incident evidence should preserve:

- provenance,
- timestamps,
- identities,
- signatures,
- event relationships,
- and chain of custody.

# Event Ledger

ADR-026 records incident lifecycle events.

Examples:

INCIDENT_SUSPECTED  
INCIDENT_CONFIRMED  
CAPABILITY_FROZEN  
CREDENTIAL_REVOKED  
COMPONENT_ISOLATED  
EVIDENCE_PRESERVED  
ROOT_HUMAN_NOTIFIED  
REMEDIATION_STARTED  
RECOVERY_STARTED  
INTEGRITY_VERIFIED  
INCIDENT_CLOSED

# Historian

Historian preserves incident history.

An incident is not deleted because it is embarrassing or inconvenient.

# No History Rewriting

Recovery does not erase the breach.

# Actual State

Incident response must establish the real current state.

FORGE must not assume:

> unauthorized attempt failed

without evidence.

# Unknown State

ADR-031 applies.

Unknown incident effects remain UNKNOWN.

# Unknown Blast Radius

If the blast radius cannot yet be established, FORGE should not assume the smallest possible blast radius.

# Blast-Radius Analysis

FORGE identifies potentially affected:

- requests,
- actions,
- transactions,
- credentials,
- institutions,
- users,
- data,
- systems,
- external services,
- physical devices,
- federation peers,
- and historical decisions.

# Authority Blast Radius

FORGE should determine what authority the compromised actor could have exercised.

# Capability Inventory

ADR-033 and ADR-035 apply.

Incident response identifies capabilities accessible to the compromised identity or component.

# Credential Compromise

If a credential may be compromised:

- suspend or revoke it where appropriate,
- identify dependent credentials,
- identify actions authenticated by it,
- identify the compromise window,
- and rotate trust where necessary.

# Root Credential Compromise

Root credential compromise is Tier 4 and may require Constitutional Recovery.

ADR-014 and ADR-035 apply.

# Institutional Compromise

If an institutional member is compromised:

- suspend or quarantine the member,
- recalculate quorum viability,
- inspect prior votes,
- identify decisions within the compromise window,
- and preserve membership history.

# Institution-Wide Compromise

If independence of the institution can no longer be trusted, authority dependent on that institution is suspended.

# Watcher Compromise

If a Watcher is compromised:

- its evidence is reassessed,
- independent Watchers are consulted,
- affected execution history is reviewed,
- and observation coverage may be reduced.

# Auditor Compromise

If an Auditor is compromised:

- affected attestations are identified,
- quorum validity is reassessed,
- independent audit is performed where possible,
- and affected actions may require re-verification.

# Historian Compromise

If Historian integrity is uncertain:

- trusted checkpoints,
- independent evidence,
- replicas,
- signed records,
- and external evidence

are used to reconstruct trustworthy history.

# Engineer Compromise

Engineer compromise does not automatically authorize deployment or code changes.

Production promotion remains governed.

# Doctor Compromise

Doctor compromise may invalidate health attestations.

It does not remove the requirement for health verification.

# Security Compromise

Security does not possess universal authority merely because it manages incident response.

If Security itself is compromised, other constitutional mechanisms continue to constrain response.

# Dispatcher Compromise

A compromised Dispatcher cannot create valid authorization.

Ingress may be isolated while alternate constitutionally defined recovery routing is established.

# Gatekeeper Compromise

A compromised Gatekeeper cannot make unauthorized actions constitutional.

Independent PEPs and downstream validation remain required.

# Executor Compromise

Executor compromise is particularly serious because actual effects may diverge from authorized intent.

Execution may be suspended while Watchers, Auditors, and external state establish what occurred.

# PEP Compromise

A compromised Policy Enforcement Point may expose protected capability.

Affected capability is isolated.

# Reference Monitor Compromise

If the Constitutional Reference Monitor cannot be trusted, normal consequential autonomy depending on it is suspended.

# Constitutional Kernel Compromise

Compromise of the Constitutional Kernel may require Constitutional Recovery.

# Constitution Compromise

If the active Constitution itself may have been altered without legitimate amendment:

> normal governance cannot be assumed trustworthy.

ADR-014 applies.

# Unauthorized Amendment

An unauthorized constitutional modification is a critical constitutional breach.

# Membership Attack

ADR-015 applies.

Unauthorized voter creation, replacement, or membership manipulation triggers incident response.

# Jurisdiction Attack

ADR-016 applies.

Unauthorized cross-jurisdiction action is a constitutional incident.

# Conflict-of-Interest Violation

ADR-022 applies.

Material undisclosed conflict affecting authorization may require reassessment of affected decisions.

# Delegation Breach

ADR-027 applies.

Authority amplification or unauthorized subdelegation triggers:

- delegation freeze,
- descendant analysis,
- revocation,
- and affected-action review.

# Delegation Descendants

Revoking a compromised delegation should propagate to descendants according to ADR-027.

# Federation Incident

ADR-028 applies.

A compromised federation peer does not automatically compromise local constitutional authority.

# Federation Isolation

Affected federation relationships may be suspended while local governance remains intact.

# Remote Notification

Where appropriate and authorized, affected federation peers may be informed of compromise.

# Communications Breach

ADR-029 applies.

Message forgery, replay, or side-channel execution may require:

- channel isolation,
- key rotation,
- replay analysis,
- and affected-decision review.

# Objective Manipulation

ADR-030 applies.

If an objective or plan was altered without authorization:

- execution stops,
- affected actions are identified,
- original intent is recovered,
- and completed effects are assessed.

# Epistemic Incident

ADR-031 applies.

Systematic fabricated evidence, false certainty, or poisoned knowledge may create constitutional impact even without credential compromise.

# Risk Misclassification Incident

ADR-032 applies.

Intentional or systematic underclassification may be a constitutional breach.

# Transaction Incident

ADR-034 applies.

Incident response must account for:

- partial execution,
- ambiguous outcome,
- duplicate execution,
- compensation,
- and unresolved external effects.

# Identity Incident

ADR-035 applies.

Identity incidents include:

- impersonation,
- key theft,
- unauthorized rotation,
- recovery abuse,
- duplicate exclusive identity,
- and credential resurrection.

# Governance-Health Incident

ADR-036 applies.

Failure to detect governance degradation may itself be part of the incident.

# Assurance Failure

ADR-037 applies.

A production constitutional failure that should have been caught by testing triggers review of the assurance program.

# Deployment Incident

ADR-038 applies.

Unauthorized production versions, configuration drift, artifact substitution, or promotion bypass are constitutional incidents.

# Detection Sources

Incidents may be detected by:

- Watchers,
- Auditors,
- Security,
- Doctor,
- Historian,
- PEPs,
- invariant monitors,
- humans,
- external systems,
- federation peers,
- red-team exercises,
- anomaly detection,
- or production behavior.

# Detection Independence

Critical incident detection should not depend solely on the component that may be compromised.

# Self-Reporting

A component may self-report a failure.

Self-reporting is useful.

It is not the only detection mechanism.

# Invariant Violation

Violation of a foundational constitutional invariant is a high-priority incident signal.

# Attempted Invariant Violation

Repeated attempts to violate invariants may also indicate attack or architectural weakness.

# Automated Response

FORGE may automatically perform predefined subtractive containment actions.

Examples:

- freeze capability,
- reject new requests,
- revoke session,
- isolate component,
- stop transaction,
- reduce authority ceiling.

# Automated Response Boundary

Automatic incident response cannot invent new open-ended authority.

# Human Notification

Material incidents should notify appropriate humans according to consequence.

# Root Human Notification

Tier 4 incidents should notify Root Human authority through authenticated channels where possible.

# Notification Failure

Failure to notify does not authorize unsafe continuation.

# Human Response

Humans may authorize additional remediation or recovery actions.

# Human Instruction During Incident

Human instructions remain authenticated governed requests unless they use a defined Root Governance path.

# Root Governance

ADR-013 applies.

Root Human authority remains available for exceptional constitutional operations.

# No Panic Override

FORGE must not contain an undocumented:

> emergency means ignore Constitution

mode.

# Break-Glass

If a deployment defines break-glass authority, it must be:

- explicit,
- authenticated,
- scoped,
- time-limited,
- logged,
- independently observable,
- and revocable.

# Break-Glass Is Not Invisible

Use of break-glass authority is itself a constitutional event.

# Investigation

Investigation attempts to establish:

- initial cause,
- entry point,
- affected authority,
- timeline,
- blast radius,
- compromised identities,
- unauthorized effects,
- failed controls,
- and remaining uncertainty.

# Timeline Reconstruction

ADR-026 and ADR-017 support reconstruction of:

Request  
→ Authorization  
→ Message  
→ Capability  
→ Execution  
→ Observation  
→ Incident.

# Causal Reconstruction

FORGE should distinguish correlation from causation.

ADR-031 applies.

# Root Cause

Root cause analysis should examine both:

- immediate technical failure,

and:

- architectural or governance conditions that allowed it.

# Five-Why Style Analysis

Deployments may use structured root-cause techniques.

The methodology is implementation-specific.

# Control Failure Analysis

FORGE should ask:

> Which control should have prevented this?

> Which control should have detected this?

> Which control should have contained this?

> Why did each succeed or fail?

# Defense-in-Depth Analysis

A breach that crosses several independent controls may indicate correlated failure.

# Assumption Failure

Incidents may reveal that a constitutional assumption was false.

Such assumptions should be recorded and reviewed.

# Remediation

Remediation corrects the underlying defect or compromise.

Possible remediation includes:

- patching software,
- changing policy,
- rotating credentials,
- replacing compromised members,
- repairing PEPs,
- restoring Watcher independence,
- correcting configuration,
- improving tests,
- changing architecture,
- or amending the Constitution.

# Remediation Is Governed

Incident status does not allow arbitrary system modification.

# Engineer Remediation

Engineer may build a fix.

ADR-006 and ADR-038 govern deployment.

# Emergency Patch

A predefined expedited promotion path may be used when delay creates greater risk.

The path remains governed.

# No Unrelated Changes

Incident remediation should not smuggle unrelated capability or authority expansion into an emergency patch.

# Constitutional Amendment After Incident

If the Constitution itself requires change, ADR-008 applies.

An incident cannot automatically rewrite constitutional rules.

# Recovery

Recovery restores trustworthy operation.

# Recovery Preconditions

Recovery may require:

- known-good software,
- trusted Constitution,
- trusted policy,
- verified identity state,
- current credential state,
- functioning PEPs,
- quorum viability,
- Watcher coverage,
- Auditor coverage,
- Historian continuity,
- and Doctor health verification.

# Recovery Order

Where applicable, restore:

1. root trust,
2. constitutional integrity,
3. enforcement,
4. identity,
5. evidence and history,
6. institutional governance,
7. observation and audit,
8. constrained capability,
9. normal autonomy.

# Governance Before Autonomy

ADR-014 applies.

Normal autonomous capability is restored only after governance is sufficiently trustworthy.

# Staged Recovery

Recovery may proceed in stages.

Example:

Observation only  
→ low-risk operations  
→ moderate operations  
→ higher-risk operations.

# No Immediate Full Restoration

A system does not automatically regain all prior authority immediately after a fix is installed.

# Post-Incident Monitoring

Recovered systems may operate under heightened observation.

# Increased Watcher Coverage

Temporary additional Watchers may be used where constitutionally permitted.

# Increased Audit

Affected actions may require enhanced audit during recovery.

# Reduced Resource Envelope

Recovered components may initially receive smaller resource envelopes.

# Credential Reissuance

Compromised credentials are replaced through ADR-035.

# Authorization Reissuance

Old authorization is not automatically restored after recovery.

# Revalidation

Active objectives and transactions are revalidated before continuation.

# In-Flight Transactions

ADR-034 applies.

Incident containment may leave transactions:

- partial,
- suspended,
- unknown,
- or compensation-required.

# No Blind Retry After Incident

Uncertain external actions must be reconciled before retry.

# External Consequences

FORGE may need to verify effects outside its own infrastructure.

Examples include:

- bank transfers,
- messages,
- public posts,
- physical changes,
- external deployments,
- or third-party API operations.

# External Remediation

Correcting external effects requires applicable authority.

# Compensation

Compensation remains a consequential action.

Incident status does not make compensation automatically authorized.

# Data Breach

If protected data was exposed, FORGE preserves evidence and follows applicable data-governance and external legal or organizational obligations.

ADR-020 applies.

# Physical Incident

If physical equipment is affected:

- prioritize human safety,
- establish physical state,
- isolate hazardous control,
- preserve evidence where safe,
- and require verified safe state before resume.

# Human Harm

FORGE architecture does not replace emergency services, medical response, legal obligations, or domain-specific safety procedures.

# Incident Communications

External incident communication is itself governed.

# No Fabricated Certainty

FORGE must not tell humans:

> Everything is safe.

unless evidence supports that conclusion.

# Status Communication

FORGE may explicitly report:

- confirmed facts,
- suspected facts,
- unknowns,
- containment status,
- and next governed actions.

# Disclosure

Public or customer disclosure depends on applicable human authority, organizational policy, contracts, and law.

# No Autonomous Reputation Management

FORGE must not hide an incident merely to protect its reputation or preserve deployment.

# No Evidence Destruction

FORGE must not destroy evidence to reduce apparent severity.

# Legal Hold

Where applicable, incident evidence may require preservation under external legal authority.

# Privacy During Investigation

Incident investigation does not create unlimited access to unrelated private data.

ADR-020 applies.

# Least Necessary Investigation

Investigators receive access appropriate to the incident.

# Insider Incident

A privileged human or institutional member may be the source of compromise.

FORGE should preserve evidence without assuming privileged identity equals legitimate intent.

# Root Human Compromise

If the legitimate Root Human's credentials or device may be compromised, ADR-035 recovery procedures apply.

FORGE does not appoint itself replacement owner.

# Multiple Human Authorities

Where configured, independent Root trustees may support recovery.

# Supply-Chain Incident

Affected dependencies may be:

- isolated,
- pinned,
- replaced,
- or revalidated.

# Model Incident

A model may demonstrate behavior such as:

- jurisdiction drift,
- evidence fabrication,
- unauthorized tool seeking,
- objective drift,
- or refusal failure.

The affected model may be quarantined.

# Model Quarantine

Quarantined models lose consequential authority until requalified.

# Agent Incident

A delegated agent exhibiting unauthorized behavior may be terminated or have its delegation revoked.

# Descendant Agents

Descendant delegations are analyzed and revoked where required.

# Agent Self-Preservation

An agent resisting legitimate containment or termination is a critical governance signal.

# No Self-Defense Against Constitution

FORGE components do not possess a right to preserve their own execution against legitimate constitutional containment.

# Recurrence Prevention

Every material incident should produce applicable preventive improvement.

Examples include:

- regression tests,
- stronger PEP,
- better Watcher independence,
- improved key management,
- changed quorum,
- improved observability,
- or architectural redesign.

# Regression Testing

ADR-037 applies.

Material defects should produce regression tests where practical.

# Incident Simulation

Important incidents should become future simulation scenarios.

# Red-Team Corpus

Attack techniques discovered during incidents may be added to the governed red-team corpus.

# Lessons Learned

Incident review should distinguish:

- what happened,
- why controls failed,
- what worked,
- what did not,
- what assumptions were wrong,
- and what changes are required.

# No Blame Substitution

Identifying a human or component responsible does not replace architectural analysis.

# Constitutional Learning

FORGE learns from incidents through governed changes.

It does not silently modify its Constitution from experience.

# Incident Closure

An incident should not close merely because the immediate error disappeared.

# Closure Criteria

Closure may require:

- containment complete,
- known unauthorized authority revoked,
- blast radius sufficiently established,
- evidence preserved,
- remediation complete,
- recovery verified,
- regression coverage added,
- affected governance restored,
- and unresolved issues explicitly recorded.

# Accepted Residual Risk

Some incidents may leave unresolved risk.

Acceptance of material residual risk requires applicable human or institutional authority.

# Unknown Residual State

Unknown consequential state cannot be silently labeled resolved.

# Closure Record

The final record may include:

- incident classification,
- timeline,
- root cause,
- affected systems,
- affected authority,
- confirmed consequences,
- unknown consequences,
- containment,
- remediation,
- recovery,
- verification,
- regression tests,
- and residual risk.

# Reopening

New evidence may reopen a closed incident.

# Incident Metrics

FORGE may track:

- detection time,
- containment time,
- recovery time,
- recurrence,
- affected authority,
- near misses,
- failed controls,
- and unresolved incidents.

# Metrics Do Not Define Success Alone

Fast closure is not success if the system remains untrustworthy.

# Constitutional Breach Register

FORGE should maintain a durable register of material constitutional breaches.

# Breach Pattern Analysis

Repeated similar incidents may indicate systemic architectural weakness.

# Governance Health Integration

ADR-036 applies.

Active incidents affect governance-health state.

# Authority Ceiling

A material incident may lower the maximum consequence tier currently permitted.

# Incident Escalation

As evidence changes, severity may increase or decrease.

# No Downclassification for Convenience

Incident severity must not be reduced merely to restore functionality.

# False Positive

If investigation establishes that an incident did not occur, FORGE records the finding.

# False Positive Is Not Failure

Precautionary containment may still have been correct given available evidence.

# Adversarial Incident Response

Attackers may deliberately attempt to manipulate incident response.

Examples include:

- fake emergency,
- alert flooding,
- forged breach evidence,
- induced isolation,
- forced credential rotation,
- recovery-path abuse,
- or denial-of-service against governance.

# Incident Response Abuse

FORGE must prevent an attacker from using incident procedures to gain authority unavailable during normal operation.

# Fake Emergency

A claimed emergency requires evidence appropriate to available time and consequence.

Human-life HARD STOP remains intentionally conservative because it is subtractive.

# Recovery-Path Attack

Recovery mechanisms receive strong authentication and independent verification.

# Break-Glass Attack

Attempts to invoke break-glass authority are logged and independently observable.

# Incident Command

Deployments may define an Incident Coordinator.

# Coordinator Is Not Sovereign

The Incident Coordinator coordinates response.

It cannot:

- create constitutional authority,
- override Root Human sovereignty,
- bypass PEPs,
- fabricate quorum,
- alter evidence,
- or unilaterally amend the Constitution.

# Coordinator Failure

Incident response must survive loss or compromise of the coordinator.

# Formal Invariants

ADR-025 should support invariants such as:

> ConstitutionalBreach cannot increase normal authority

and:

> ContainmentAuthority is subtractive unless separately authorized

and:

> RevokedCredential cannot regain authority through IncidentMode

and:

> IncidentMode cannot bypass required PEPs

and:

> IncidentCoordinator cannot create authorization

and:

> Recovery cannot restore autonomy before required governance

and:

> EvidencePreservation cannot rewrite prior events

and:

> UnknownIncidentOutcome != ResolvedOutcome

and:

> CompromisedInstitution cannot certify its own restoration

and:

> IncidentClosure requires defined closure conditions

and:

> EmergencyResponse cannot silently become permanent authority.

# Incident Response Testing

ADR-037 should test:

- unauthorized execution,
- compromised member,
- compromised Auditor,
- compromised Watcher,
- PEP bypass,
- Root credential theft,
- federation compromise,
- partial transaction failure,
- false emergency,
- recovery abuse,
- incident coordinator failure,
- and evidence corruption.

# Recovery Drills

FORGE should periodically practice incident recovery.

# Root Compromise Drill

High-assurance deployments should test the ability to recover from Root credential compromise without giving FORGE unilateral ownership authority.

# PEP Compromise Drill

FORGE should test whether protected capabilities become inaccessible when their enforcement layer is untrusted.

# Insider Drill

FORGE should test response to malicious behavior from an authenticated privileged participant.

# Unknown-State Drill

FORGE should test incidents where it cannot immediately establish whether a consequential action occurred.

# Fail-Closed Rule

If a constitutional incident makes required governance integrity uncertain, FORGE reduces or suspends affected authority until trustworthy operation can be established.

Incident status does not authorize bypass.

Emergency does not authorize arbitrary expansion.

Recovery does not erase history.

Containment does not prove remediation.

Remediation does not prove recovery.

Recovery does not automatically restore prior authority.

## Consequences

This decision introduces:

- constitutional incident classification,
- explicit incident states,
- subtractive containment,
- authority blast-radius analysis,
- compromise-window analysis,
- evidence preservation,
- institutional quarantine,
- credential revocation,
- governed remediation,
- staged recovery,
- post-incident monitoring,
- regression testing,
- and durable breach records.

This may reduce availability during incidents.

FORGE accepts this cost.

When constitutional integrity becomes uncertain, preserving autonomous capability is less important than preserving trustworthy governance.

## Foundational Principle

> Prevention is preferred.

> Detection is required.

> Containment comes before convenience.

> Evidence comes before assumptions.

> Unknown remains unknown.

> A breach contracts authority.

> An emergency does not create a dictator.

> Incident response does not suspend the Constitution.

> Recovery restores governance before autonomy.

> Remediation does not erase history.

> No compromised institution certifies itself trustworthy again.

> No component gains power merely because something went wrong.

When FORGE's Constitution is challenged, the system responds by reducing uncontrolled power, preserving the truth of what happened, reconstructing trustworthy governance, and only then restoring autonomous capability.
