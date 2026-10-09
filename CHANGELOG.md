# FORGE Architecture Changelog

This document records significant architectural decisions and changes to FORGE: A Constitutional Architecture for Governed Autonomous AI Systems.

The changelog is intended to preserve the evolution of the architecture alongside Git's immutable commit history.

---

## [0.2] - 2026-10-06

### Constitutional Architecture

- Established FORGE as a governed constitutional architecture based on separation of powers and distributed authority.
- Established that no single authority-bearing component should routinely be capable of proposing, authorizing, executing, observing, and validating the same consequential action.
- Established that FORGE itself operates under the Constitution rather than above it.

### Request Integrity

- Established the governed request chain:

  Request → Dispatcher → Gatekeeper → Auditor Checkpoint → Subsystem Institutions → Auditor Checkpoint → Authorization → FORGE Execution → Watchers → Final Auditor Verification.

- Established authenticated request identities to preserve original intent throughout the execution chain.
- Established independent verification of request identity at multiple stages.
- Established that changed actions cannot reuse previous authorization.

### Institutional Subsystems

- Defined subsystems as governed institutions rather than individual agents.
- Established redundant members within institutions such as Banker, Teacher, Engineer, Doctor, Security, Historian, and Auditor.
- Established independent voting and constitutionally defined quorum requirements.
- Established that silence or subsystem failure does not constitute approval.

### Watchers

- Established independent Watchers for authority-bearing subsystems.
- Established independent execution-level Watchers.
- Established that a subsystem cannot control, retrain, disable, or modify the Watchers responsible for observing it.
- Watchers provide independent evidence of behavior and outcomes.

### Auditors

- Established multiple independent Auditors for FORGE and subsystem institutions.
- Auditors independently produce integrity attestations rather than deliberating as a governing body.
- Established quorum-based audit verification.
- Auditors verify request identity, authorization integrity, execution evidence, and consistency between authorized intent and observed outcomes.

### Historian

- Established the Historian as FORGE's institutional memory.
- Historian maintains append-only architectural and operational history.
- Historian preserves signed known-good checkpoints, constitutional versions, configuration states, health records, and recovery evidence.
- Historian cannot independently perform a rollback or restoration.
- System rollback is treated as a highest-risk governed action requiring the defined whole-system unanimous authorization process.

### Engineer and Updates

- Established the Engineer as the institution responsible for building, packaging, testing, and proposing subsystem-specific updates.
- Engineer cannot unilaterally deploy privileged updates.
- Rejected a universal one-size-fits-all update mechanism in favor of subsystem-specific update tracks.
- Established staged deployment to limit cascading failures.

### Doctor

- Established the Doctor as FORGE's diagnostic and system-health institution.
- Doctor performs health examinations before and after subsystem updates.
- Doctor establishes signed pre-update health baselines.
- Doctor may prescribe controlled preparation or remediation but cannot independently execute arbitrary repairs.

### Periodic Subsystem Health Monitoring

- Expanded the Doctor's responsibilities to include periodic proactive health examinations of every FORGE subsystem.
- Doctor performs scheduled stress tests, diagnostics, performance evaluation, behavioral consistency checks, resource-health analysis, and related examinations.
- Health monitoring is intended to identify degradation, instability, drift, or latent failure before an operational incident occurs.
- Historian preserves health results to establish longitudinal health baselines.
- Each subsystem may maintain a role-specific health profile appropriate to its responsibilities and operational boundaries.
- Detected health problems enter FORGE's governed remediation process rather than being independently repaired by the Doctor.

### Emergency Doctrine

- Established preservation of human life as a top-level constitutional hard constraint.
- A credible imminent threat to human life triggers a HARD STOP.
- Emergency authority is subtractive only and may halt, freeze, isolate, contain, or revoke authority.
- Emergency authority cannot create unrelated objectives or expand system authority.
- Removal of a hazard does not automatically resume execution.
- Resume requires a governed RESET/RESUME process and verification of a safe state.

### Constitutional Amendments

- Distinguished constitutional amendments from ordinary software updates.
- Established a bicameral amendment concept consisting of a House-like proposal body and Senate-like constitutional review body.
- Institutions cannot independently expand their own authority.
- Human approval is required before constitutional amendments take effect.
- Certain foundational constitutional constraints may be permanently entrenched and unavailable to ordinary amendment procedures.

### Credentials and Privileged Access

- Established that FORGE does not possess standing universal credentials.
- Privileged credentials remain within jurisdiction-specific protected services.
- Authorized actions may receive narrow, short-lived capabilities bound to the exact approved action.
- Permanent raw credentials are not provided to FORGE during normal execution.

### Training and Jurisdiction

- Established separation between improving subsystem capability and changing subsystem jurisdiction.
- Runtime requests cannot silently redefine an institution's constitutional role.
- Controlled teaching and update processes may improve capability while jurisdiction remains constitutionally governed.

### Recovery

- Established governed recovery from known-good Historian checkpoints.
- Recovery authority remains separated from historical recordkeeping.
- Watchers observe restoration.
- Auditors verify restored state.
- Failed and intermediate states remain part of the historical record rather than being erased.

---

## [Unreleased] - Proposed only

### Institution template

- Added a proposed institution-template package under `institution-template/`.
- Added ADR-041 with status Proposed. It is not Accepted and it does not amend ADR-001 through ADR-040.
- The example institution is non-production and its lifecycle is `validated`. It is not approved and not activated.
- Layers 1–10 are the ADR-040 numbers and names. Layers 11–12 are an unapproved proposed extension.

## Status

FORGE remains under active architectural development.

Version 0.2 represents the documented architecture as of October 6, 2026. Additional governance mechanisms, failure modes, resource governance, Teacher governance, human authority boundaries, and adversarial testing remain under development.
