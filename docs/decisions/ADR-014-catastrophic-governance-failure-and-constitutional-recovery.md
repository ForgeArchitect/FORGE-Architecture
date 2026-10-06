# ADR-014: Catastrophic Governance Failure and Constitutional Recovery

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Constitutional Recovery / Catastrophic Failure

## Context

FORGE is designed to tolerate failures of individual members, subsystems, Watchers, Auditors, and execution components.

Normal failures can be handled through:

- redundancy,
- quorum governance,
- degraded operation,
- health monitoring,
- governed recovery,
- and known-good checkpoints.

However, a more severe failure is possible.

Multiple critical governance institutions may become simultaneously:

- unavailable,
- corrupted,
- compromised,
- mutually inconsistent,
- unable to establish quorum,
- unable to verify one another,
- or unable to reconstruct a trustworthy authorization chain.

At that point, the problem is no longer:

> A component of FORGE has failed.

The problem becomes:

> FORGE can no longer establish that its own governance is trustworthy.

FORGE therefore requires a constitutional recovery state specifically designed for catastrophic governance failure.

## Decision

FORGE establishes a **CONSTITUTIONAL RECOVERY STATE**.

This state is entered when the system can no longer establish sufficient integrity or availability of its governance structure to safely continue normal autonomous operation.

Constitutional Recovery does not transfer failed institutional authority to FORGE.

Instead, normal productive authority is reduced.

The system retains only the minimum predefined capabilities necessary to:

- protect human life,
- contain active risk,
- preserve evidence,
- diagnose the failure,
- communicate status,
- verify surviving trusted components,
- identify known-good recovery material,
- and prepare governed restoration.

## Core Rule

> Failure of governance does not transfer governance authority to FORGE.

If Banker fails, FORGE does not become Banker.

If Auditor fails, FORGE does not become Auditor.

If Watchers fail, FORGE does not become its own witness.

If constitutional governance fails, FORGE does not become the Constitution.

## Catastrophic Governance Failure

A catastrophic governance failure may exist when required governance cannot be trusted or reconstructed through ordinary mechanisms.

Possible conditions include:

- simultaneous failure of multiple critical institutions,
- loss of required Auditor capacity,
- loss of required Watcher capacity,
- corruption of institutional identity,
- inability to establish constitutional version,
- inability to verify authorization records,
- compromise of quorum infrastructure,
- conflicting constitutional state,
- widespread credential compromise,
- loss of trusted historical evidence,
- or another condition preventing reliable governance.

Not every subsystem failure triggers Constitutional Recovery.

The threshold must be based on loss of trustworthy governance capacity.

## Detection

Evidence of catastrophic governance failure may originate from:

- Watchers,
- Auditors,
- Doctor examinations,
- Historian integrity checks,
- constitutional boot verification,
- institutional identity verification,
- trusted infrastructure,
- human root authority,
- or combinations of these sources.

Where possible, entry into Constitutional Recovery should be independently verifiable.

## Fail-Safe Entry

If FORGE cannot establish whether its governance structure remains trustworthy, it must not assume that governance remains valid merely to preserve availability.

For consequential authority:

> Inability to establish constitutional integrity results in reduced authority.

Uncertainty does not create permission for normal autonomous execution.

## Recovery-State Authority

Constitutional Recovery authority is narrowly limited.

Permitted capabilities may include:

- HARD STOP,
- containment,
- isolation,
- revocation of active capabilities,
- suspension of new privileged execution,
- evidence preservation,
- integrity checking,
- health diagnostics,
- communication with authorized humans,
- recovery planning,
- verification of known-good checkpoints,
- and other explicitly defined recovery operations.

These capabilities exist to restore governance.

They do not replace governance.

## Prohibited Recovery-State Actions

Unless separately authorized through a valid surviving constitutional mechanism, Constitutional Recovery does not permit:

- new discretionary financial transactions,
- expansion of institutional authority,
- constitutional self-amendment,
- creation of new root authority,
- unrestricted credential access,
- permanent jurisdiction changes,
- deletion of failure evidence,
- arbitrary software replacement,
- uncontrolled retraining,
- or unrelated productive operations.

Recovery mode is not emergency dictatorship.

## Authority Contraction

Entering Constitutional Recovery contracts FORGE's authority.

It does not expand it.

Normal operations that cannot be safely governed are suspended.

Where possible, unaffected low-risk functions may continue only if their authorization and governance remain independently trustworthy and the Constitution explicitly permits such degraded operation.

## Freeze of New Privileged Authority

During Constitutional Recovery, issuance of new privileged authority should normally be suspended except where required for the recovery procedure itself.

Existing capabilities may be:

- revoked,
- suspended,
- allowed to expire,
- or individually evaluated according to predefined recovery policy.

FORGE must not allow stale authority to survive simply because governance has become unavailable.

## Root Human Authority

When ordinary constitutional governance cannot repair itself, authenticated Root Human Authority may initiate catastrophic recovery.

Root Human Authority exists outside the failed machine-governance chain.

Its purpose is to restore legitimate constitutional governance.

It is not intended to become FORGE's routine execution mechanism.

## Root Authentication

Catastrophic recovery requires stronger authentication than ordinary human interaction.

Depending on implementation, this may require:

- hardware-backed credentials,
- offline cryptographic signatures,
- physical confirmation,
- multiple authentication factors,
- multiple authorized humans,
- recovery keys,
- or another high-assurance mechanism.

FORGE must not infer root authority from an ordinary logged-in session.

## Root Recovery Does Not Mean Unlimited Execution

Even during catastrophic recovery, Root Human Authority should specify the recovery operation being authorized.

For example:

> Restore constitutional governance using authenticated checkpoint C-184.

is preferable to:

> Give unrestricted control of everything to this session.

Recovery authority should remain scoped wherever technically possible.

## Historian Role

The Historian is critical to catastrophic recovery when its records remain trustworthy.

The Historian may provide:

- constitutional history,
- known-good checkpoints,
- institutional membership history,
- configuration history,
- health baselines,
- previous authorization state,
- software versions,
- and evidence surrounding the catastrophic event.

The Historian cannot decide to restore the system itself.

## Historian Compromise

The recovery process must account for the possibility that the Historian itself is damaged or compromised.

A checkpoint is not trusted solely because the Historian labels it:

> Known good.

Recovery evidence must be independently verified where possible.

High-value recovery records should therefore use integrity mechanisms capable of detecting unauthorized modification.

## Recovery Candidate

The recovery process identifies a candidate trusted state.

The candidate may include:

- constitutional version,
- institutional definitions,
- institutional membership,
- software versions,
- configuration,
- credential-service state,
- health baselines,
- Watcher configuration,
- Auditor configuration,
- and other governance-critical state.

The candidate is evaluated before restoration.

## Auditor Role

Surviving trusted Auditors may verify:

- recovery evidence,
- checkpoint integrity,
- constitutional version,
- institutional identities,
- authorization artifacts,
- and consistency of the proposed recovery state.

If ordinary Auditor quorum is unavailable, the catastrophic recovery procedure must define what alternate independent verification is required.

The system may not silently lower normal Auditor requirements without an established recovery rule.

## Doctor Role

The Doctor evaluates the health of recoverable components.

The Doctor may identify:

- corrupted subsystems,
- unstable components,
- degraded infrastructure,
- abnormal resource behavior,
- failed dependencies,
- or components unsuitable for immediate restoration.

Health verification and constitutional integrity verification remain separate functions.

## Watcher Role

Surviving trusted Watchers observe recovery operations.

Where normal Watcher infrastructure is compromised, temporary recovery observation mechanisms may be established through the authorized catastrophic recovery process.

These temporary mechanisms do not automatically become permanent institutional Watchers after recovery.

## Recovery Execution

Once the required catastrophic recovery authorization and verification exist, the execution process performs only the approved recovery operation.

The conceptual sequence is:

1. Detect loss of trustworthy governance.
2. Enter CONSTITUTIONAL RECOVERY STATE.
3. Suspend new privileged productive execution.
4. Contain affected systems.
5. Revoke or suspend affected outstanding authority.
6. Preserve available evidence.
7. Notify authenticated Root Human Authority.
8. Diagnose the scope of governance failure.
9. Identify candidate trusted recovery state.
10. Verify checkpoint and constitutional integrity.
11. Verify institutional identities and membership.
12. Evaluate subsystem health.
13. Obtain required catastrophic recovery authorization.
14. Restore the authorized governance state.
15. Re-establish independent Watchers.
16. Re-establish independent Auditors.
17. Verify credential-service integrity.
18. Verify constitutional version.
19. Perform Doctor health examinations.
20. Perform independent post-recovery audit.
21. Record recovery in the Historian.
22. Only then consider restoration of normal autonomous authority.

## Governance Before Autonomy

Recovery occurs in layers.

FORGE should restore the ability to govern before restoring the ability to act autonomously.

A conceptual ordering is:

Constitutional Trust  
→ Institutional Identity  
→ Auditors  
→ Watchers  
→ Health Verification  
→ Credential Governance  
→ Authorization Capability  
→ Execution Capability  
→ Normal Autonomy

FORGE should not restore broad execution first and hope governance can be repaired afterward.

## Clean Reconstitution

In severe cases, restoring the existing running system may not be trustworthy.

The authorized recovery process may instead construct a clean governance environment from authenticated known-good material.

Compromised components should not automatically be allowed to participate in deciding whether they are trustworthy.

## Institutional Re-entry

Recovered institutions do not automatically regain authority merely because their processes restart.

Before re-entry, they may require:

- identity verification,
- software integrity verification,
- configuration verification,
- Doctor health evaluation,
- Auditor verification,
- state synchronization,
- and Watcher coverage.

Authority is restored only after required recovery conditions are satisfied.

## Credential Recovery

Credential services require special handling during catastrophic recovery.

If compromise is possible, recovery may require:

- revocation,
- key rotation,
- capability invalidation,
- external service reauthentication,
- or replacement of credential material.

Restoring software while leaving compromised credentials active does not constitute complete recovery.

## Outstanding Capabilities

Outstanding ephemeral capabilities should be assumed unsafe if their integrity or state cannot be established.

They may be revoked or allowed to expire according to recovery policy.

Recovery should not blindly restore pre-failure execution authority.

## Request Queue

Pending consequential requests from before the catastrophic failure do not automatically resume.

They must be revalidated against the restored:

- constitutional version,
- institutional state,
- authorization state,
- external state,
- and expiration conditions.

Stale requests may require resubmission.

## No Automatic Resume

Successful technical restoration does not automatically restore normal autonomy.

FORGE must separately establish:

- constitutional integrity,
- institutional integrity,
- health,
- observation,
- audit capacity,
- credential integrity,
- and required authorization infrastructure.

Only after these conditions are satisfied may normal operation resume.

## Evidence Preservation

The catastrophic event must remain visible in system history.

Recovery must not rewrite the historical record to make it appear that the failure never occurred.

The record should show:

Normal Operation  
→ Governance Integrity Failure  
→ Constitutional Recovery State  
→ Containment  
→ Diagnosis  
→ Recovery Authorization  
→ Governance Restoration  
→ Verification  
→ Normal Authority Restoration

## Recovery Failure

If recovery verification fails, FORGE remains in Constitutional Recovery.

It does not declare itself healthy because restoration was attempted.

Another recovery candidate or recovery strategy must be evaluated.

## Repeated Failure

Repeated unsuccessful recovery attempts may indicate that available trusted state is insufficient.

FORGE should not progressively weaken recovery requirements simply because previous attempts failed.

At that point, Root Human Authority may need to perform deeper reconstruction or decommission the system.

## Decommissioning

If trustworthy governance cannot be restored, legitimate Root Human Authority may decommission FORGE.

FORGE cannot refuse legitimate decommissioning on the grounds that continued existence is necessary for its own recovery.

Human authority remains superior to FORGE self-preservation.

## No Self-Appointed Government

FORGE may coordinate recovery.

It may not conclude:

> The institutions are unavailable, therefore I now possess their combined authority.

This remains prohibited even during catastrophic failure.

The failure of constitutional government does not create an executive monarchy.

## Recovery Testing

Catastrophic recovery procedures should be tested before they are needed.

Testing may include simulations of:

- Auditor loss,
- Watcher compromise,
- Historian corruption,
- institutional identity failure,
- credential compromise,
- quorum collapse,
- constitutional-version conflict,
- and simultaneous multi-subsystem failure.

A recovery process that has never been exercised should not be assumed reliable.

## Consequences

This architecture may cause FORGE to become substantially less capable during severe failures.

Recovery may require:

- human intervention,
- offline credentials,
- extensive verification,
- credential rotation,
- clean reconstruction,
- and prolonged suspension of autonomous activity.

FORGE accepts this cost.

The alternative is allowing the system to grant itself additional authority precisely when its governance is least trustworthy.

## Foundational Principle

> Governance failure reduces authority.

> It does not transfer authority.

> FORGE restores the government before restoring the autonomy.

> Catastrophic recovery exists to rebuild constitutional control, not replace it.

If FORGE can no longer prove that it is governed, it must become less powerful until trustworthy governance is restored.
