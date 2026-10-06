# ADR-035: Identity, Authentication, and Root Key Lifecycle

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Identity / Authentication / Cryptographic Trust

## Context

FORGE depends on authenticated identity throughout the architecture.

The system must distinguish:

- Root Humans,
- ordinary human users,
- FORGE deployments,
- institutions,
- institutional members,
- Auditors,
- Watchers,
- Doctor,
- Engineer,
- Teacher,
- Security,
- Banker,
- Dispatcher,
- Gatekeeper,
- Executor,
- credential services,
- external systems,
- delegated agents,
- and temporary processes.

Many constitutional decisions depend on knowing:

> Who produced this request?

> Who cast this vote?

> Who issued this authorization?

> Who observed this action?

> Which FORGE instance sent this message?

> Is this the same authority that was trusted previously?

If identity can be forged, the constitutional architecture can be bypassed without directly attacking its decision logic.

An attacker who obtains an Auditor identity could fabricate attestations.

An attacker who obtains a Banker identity could attempt to fabricate financial approval.

An attacker who obtains a Root Human credential could attempt constitutional modification or decommissioning.

Identity is therefore not merely an application login problem.

It is part of FORGE's constitutional trust foundation.

## Decision

FORGE establishes a cryptographically grounded identity and authentication architecture with governed lifecycle management.

Identity, authentication, authorization, and jurisdiction remain separate concepts.

## Core Rule

> Identity establishes who or what an actor is.

> Authentication establishes evidence that the actor currently controls the required identity credential.

> Authorization establishes what that actor may do.

> Jurisdiction establishes what that actor may decide.

None of these concepts substitutes for the others.

# Identity

A FORGE identity represents a distinct constitutional or operational actor.

An identity may belong to:

- human,
- deployment,
- institution,
- institutional member,
- service,
- device,
- agent,
- or other recognized principal.

# Identity Is Not Authority

Creating an identity does not grant authority.

An authenticated identity with no applicable authorization still has no authority to perform the protected action.

# Authentication Is Not Authorization

A valid login does not mean:

> allow everything.

# Authorization Is Not Jurisdiction

An authenticated component cannot exercise institutional authority outside its constitutional role.

# Identity Record

A material identity record may include:

- unique identity ID,
- identity type,
- owner or controlling authority,
- public verification material,
- institutional affiliation,
- seat where applicable,
- activation state,
- creation event,
- expiration where applicable,
- revocation state,
- constitutional version,
- credential version,
- and applicable metadata.

# Stable Identity

Where continuity matters, FORGE should distinguish stable identity from individual credentials.

A key may change while the underlying legitimate identity remains the same.

# Credential

A credential is evidence used to authenticate an identity.

Credentials may include:

- cryptographic keys,
- hardware-backed keys,
- certificates,
- passkeys,
- tokens,
- or other approved authentication mechanisms.

# Credential Is Not Identity

Losing a credential does not necessarily mean the underlying identity ceases to exist.

Likewise, possessing an old credential does not preserve authority after revocation.

# Cryptographic Identity

Authority-bearing machine identities should use strong cryptographic authentication where practical.

# Human Authentication

Privileged human authority should use authentication appropriate to consequence.

Higher-risk authority should require stronger authentication.

# Root Human Authentication

Root Human operations are Tier 4.

Root authentication should therefore receive particularly strong protection.

Possible controls may include:

- hardware-backed credentials,
- passkeys,
- multiple factors,
- recovery credentials,
- threshold authorization,
- offline recovery material,
- or combinations appropriate to the deployment.

FORGE does not mandate one vendor or technology.

# Root Key

A Root Key is cryptographic material capable of authenticating or validating foundational governance authority.

Root keys are part of the constitutional trust foundation.

# Root Key Is Not Routine Credential

Root keys should not be used casually for normal operations.

Routine activity should use lower-level scoped credentials.

# Root Key Isolation

Where practical, Root Keys should remain isolated from ordinary FORGE runtime components.

FORGE should not maintain unrestricted standing access to human Root Keys.

# Root Human Control

Legitimate Root Human credentials should remain under human-controlled protection where practical.

FORGE must not be able to silently sign Root Human approval on the human's behalf.

# No Fabricated Human Authorization

FORGE cannot generate an artifact claiming:

> Root Human Approved

without valid human authentication.

# Root of Trust

ADR-023 applies.

FORGE boot establishes a chain from protected trust anchors to the active constitutional runtime.

# Trust Anchor

A trust anchor is a foundational identity or verification element from which other trust relationships are derived.

Trust anchors require strong protection because compromise may affect large portions of the system.

# Trust Anchor Minimization

FORGE should minimize the number of credentials capable of independently establishing foundational trust.

# No Universal Operational Master Key

ADR-009 applies.

FORGE should not create a single runtime credential granting unrestricted access to every protected system.

# Key Hierarchy

FORGE may use hierarchical key structures.

Example:

Root Trust  
→ Deployment Identity  
→ Institutional Identity  
→ Member / Service Identity  
→ Scoped Session or Capability

The exact hierarchy is implementation-specific.

# Hierarchy Does Not Imply Unlimited Delegation

A parent identity cannot automatically delegate authority that governance does not permit it to delegate.

# Deployment Identity

Each FORGE deployment has a distinct authenticated identity.

ADR-028 applies.

# Deployment Key

A deployment may possess keys used to authenticate:

- instance identity,
- communications,
- evidence,
- or system artifacts.

These keys do not automatically create institutional authority.

# Institutional Identity

Institutions have identities separate from individual members.

# Member Identity

ADR-015 applies.

Each authority-bearing member should have an independently distinguishable identity.

# Seat Identity

Institutional seat and member identity remain distinguishable.

Example:

Banker Seat 3

may currently be occupied by:

Member B-104.

# Replacement

Replacing a member does not require pretending the replacement is the previous member.

The seat continues.

The member identity changes.

# No Shared Member Credential

Independent institutional members should not share one credential where that would defeat independent attribution.

# Quorum Authentication

ADR-003 applies.

Quorum requires independently authenticated eligible votes.

# Vote Attribution

Each vote should be attributable to the member that issued it.

# Auditor Identity

Each Auditor should have independently distinguishable authentication.

One compromised Auditor key must not automatically allow fabrication of every Auditor identity.

# Watcher Identity

Independent Watchers should likewise possess independently verifiable identity.

# Service Identity

Internal services should authenticate to one another where consequence warrants.

Network location alone is insufficient identity.

# Device Identity

Physical devices may possess authenticated identities.

Example:

FORGE must distinguish:

Authorized Valve Controller V-17

from:

Unknown Device pretending to be V-17.

# Agent Identity

Delegated agents receive explicit identities where consequence warrants.

ADR-027 applies.

# Temporary Agent Identity

Temporary agents should use temporary credentials where practical.

Their identity lifecycle should correspond to their delegated lifecycle.

# Session Identity

Authentication may establish a temporary session.

Session authority remains bounded by:

- identity,
- authorization,
- time,
- context,
- and revocation state.

# Session Expiration

Sessions expire.

Expired sessions cannot create current authority.

# Reauthentication

High-risk actions may require recent authentication even if an older session remains active.

# Step-Up Authentication

FORGE may require stronger authentication when an action crosses into a higher consequence tier.

Example:

Tier 1 operation  
→ ordinary authenticated session.

Tier 4 operation  
→ explicit fresh Root Human authentication.

# Authentication Context

Authentication should be bound to relevant context where practical.

Context may include:

- deployment,
- device,
- session,
- action,
- transaction,
- or constitutional operation.

# Intent Binding

High-risk human authentication should be bound to what the human is approving where practical.

The human should not merely authenticate:

> I am Ben.

when the important question is:

> Did Ben approve this specific constitutional action?

# Approval Artifact

A privileged human approval artifact may bind:

- human identity,
- action,
- target,
- parameters,
- constitutional version,
- time,
- expiration,
- and nonce or unique request identity.

# Authentication Freshness

ADR-018 applies.

Old authentication may not satisfy a requirement for fresh human confirmation.

# Replay Protection

Authentication artifacts should resist replay.

A previously valid approval should not be reusable for unrelated future actions.

# Challenge

Authentication protocols may use fresh challenges, nonces, or equivalent anti-replay mechanisms.

# Key Creation

Authority-bearing key creation is a governed lifecycle event.

# Key Generation

Keys should be generated using appropriate cryptographic randomness and trusted mechanisms.

# Private Key Protection

Private keys should not be unnecessarily exposed to:

- prompts,
- logs,
- training data,
- ordinary agents,
- debugging output,
- Historian records,
- or external services.

# Public Keys

Public verification material may be broadly distributable where appropriate.

# Key Registration

A newly created key does not gain authority merely because it exists.

It must be bound to a legitimate identity through governed registration.

# Key Activation

Registration and activation may be separate steps.

# Key Rotation

Keys should support rotation.

Rotation may occur because of:

- scheduled lifecycle policy,
- suspected compromise,
- algorithm migration,
- personnel change,
- device replacement,
- constitutional recovery,
- or security improvement.

# Rotation Does Not Create New Identity Automatically

A legitimate key rotation may preserve the underlying identity.

# Rotation Record

Key rotation should preserve evidence linking:

Old Credential  
→ Rotation Authority  
→ New Credential

without exposing private secrets.

# Rotation Authorization

The component whose key is being rotated should not necessarily be the sole authority approving its own replacement.

Higher-risk key rotation requires independent governance.

# Root Key Rotation

Root Key rotation is Tier 4.

It requires strong governance because it changes foundational trust.

# Root Rotation Continuity

A valid root rotation should establish cryptographic and governance continuity from the old trust state to the new one where possible.

# Compromised Root Rotation

If the old root is compromised, ordinary continuity may itself be untrustworthy.

ADR-014 Constitutional Recovery may be required.

# Key Revocation

A credential can be revoked.

Revocation means it no longer establishes current authority.

# Revocation Propagation

Revocation should propagate to relevant:

- Reference Monitors,
- PEPs,
- credential services,
- communications systems,
- federation relationships,
- and verification services.

# Revocation Latency

High-risk credentials should minimize the period during which a revoked credential may still be accepted.

# Revocation Evidence

Revocation events should be authenticated and preserved.

# Revoked Key

A valid historical signature created before revocation may remain valid historical evidence.

Revocation does not necessarily erase history.

# Historical Verification

FORGE must distinguish:

> Was this signature valid when issued?

from:

> Is this credential valid for new authority now?

# Key Expiration

Credentials may expire according to policy.

Expired credentials cannot authenticate new authority.

# Credential Renewal

Renewal is a governed issuance event.

It is not automatic resurrection of expired authority.

# Lost Credential

A lost credential creates an identity-recovery problem.

FORGE must not simply create a replacement based on an unauthenticated claim:

> I lost my key.

# Identity Recovery

Recovery procedures should establish legitimate identity using predefined evidence.

# Recovery Credential

Deployments may maintain protected recovery credentials.

Recovery credentials themselves are high-value trust assets.

# Offline Recovery

Root recovery may use offline material where appropriate.

This reduces dependence on a potentially compromised FORGE runtime.

# Recovery Independence

FORGE should not be the sole authority determining whether someone claiming to be the Root Human is legitimate during catastrophic recovery.

# Social Engineering Resistance

Identity recovery is a major social-engineering target.

FORGE should treat attempts to:

- replace keys,
- reset credentials,
- change owners,
- or alter recovery channels

as high-consequence operations.

# Ownership Transfer

Changing Root Human ownership or equivalent controlling authority is Tier 4.

# Ownership Transfer Record

Transfer should establish:

- prior owner authority,
- new owner identity,
- effective time,
- affected deployments,
- credential changes,
- and final verification.

# Former Owner Credentials

After completed ownership transfer, credentials that should no longer carry authority must be revoked.

# Multi-Human Governance

FORGE may support multiple privileged humans.

Examples include:

- owner,
- administrator,
- security custodian,
- recovery trustee,
- organizational board,
- or designated approvers.

# Threshold Human Authentication

High-risk deployments may require M-of-N human approval.

Example:

2 of 3 designated Root Trustees.

# Threshold Does Not Mean Shared Password

Independent humans should authenticate independently.

# Separation of Human Roles

Different humans may possess different governance jurisdictions.

# Human Removal

Removing a privileged human requires applicable governance and credential revocation.

# Human Departure

Organizational deployments should have explicit procedures for departing administrators or employees.

# Orphaned Identity

An identity with no legitimate current controller should not retain indefinite authority.

# Dormant Identity

Long-unused privileged identities may require reauthentication, suspension, or review.

# Machine Credential Rotation

Machine credentials should be rotatable without rewriting constitutional identity.

# Short-Lived Machine Credentials

Where practical, machine sessions should prefer short-lived credentials over permanent secrets.

# Ephemeral Credentials

Ephemeral credentials reduce compromise duration.

# Capability Credentials

ADR-009 applies.

Execution capabilities should be narrower than identity credentials.

# Identity Credential Versus Capability

An identity credential says:

> I am Principal X.

A capability says:

> Principal X may perform Action Y under Conditions Z.

These should remain distinct.

# Credential Brokerage

Protected credential services may issue temporary capabilities after authorization.

# Raw Secret Isolation

Raw secrets should remain inaccessible to general agents where practical.

# Signing Keys

Keys used to sign:

- votes,
- approvals,
- evidence,
- audit attestations,
- Watcher observations,
- policy,
- software,
- or constitutional artifacts

should have explicit purpose.

# Key Purpose Separation

FORGE should avoid using one key for every cryptographic purpose.

Example:

A software-signing key should not automatically authenticate Root Human constitutional approval.

# Cross-Purpose Attack

A valid signature in one domain must not be interpretable as valid authority in another domain.

# Domain Separation

Cryptographic operations should include sufficient context to prevent cross-purpose reuse.

# Signed Object Type

Signed material should identify what is being signed.

Examples:

- HUMAN_APPROVAL,
- BANKER_VOTE,
- AUDITOR_ATTESTATION,
- SOFTWARE_ARTIFACT,
- CONSTITUTION,
- FEDERATION_AGREEMENT.

# Signature Context

A signature over arbitrary bytes should not be accepted as every possible constitutional artifact.

# Algorithm Agility

FORGE should support governed migration to stronger cryptographic algorithms when required.

# Cryptographic Policy

Approved algorithms, key sizes, protocols, and lifetimes should be versioned policy rather than permanently hard-coded assumptions where practical.

# Algorithm Deprecation

Deprecated cryptography should be phased out through governed migration.

# Cryptographic Failure

Discovery that a cryptographic primitive is no longer trustworthy may trigger:

- accelerated rotation,
- credential revocation,
- policy change,
- federation suspension,
- or Constitutional Recovery.

# Hardware Security

High-value keys may use hardware-backed protection.

Possible mechanisms include:

- secure elements,
- TPMs,
- hardware security modules,
- passkeys,
- or equivalent systems.

FORGE remains implementation-neutral.

# Hardware Is Not Infallible

Hardware protection reduces some threats.

It does not eliminate:

- owner compromise,
- supply-chain compromise,
- policy error,
- or misuse by authenticated principals.

# Biometric Authentication

Biometrics may assist human authentication.

Biometric data should not be treated like a replaceable password.

Privacy and recovery implications require special care.

# Password Authentication

Passwords may be used where appropriate.

High-consequence Root authority should not depend solely on weak reusable passwords where stronger methods are practical.

# Secret Storage

Secrets should be stored using systems appropriate to their sensitivity.

# No Plaintext Secret Logging

FORGE must not intentionally write raw high-value secrets into ordinary logs or Historian records.

# Backup of Keys

Key backup creates additional copies of authority-bearing secrets.

Backup therefore requires governance.

# Backup Encryption

Sensitive key backups should be strongly protected.

# Backup Access

Backup possession does not automatically authorize activation.

# Backup Restoration

Restoring an old key backup must not resurrect revoked authority.

# Anti-Resurrection

ADR-024 applies.

Decommissioned, revoked, or extinguished identities must not regain authority merely because old key material still exists.

# Identity Tombstone

FORGE may preserve authenticated tombstones indicating that an identity or credential is permanently retired.

# Clone Resistance

Copying a machine image must not automatically create another legitimate authority-bearing instance with the same identity.

# Instance Cloning

ADR-023 applies.

A clone must establish distinct legitimate identity unless governance explicitly defines otherwise.

# Duplicate Identity Detection

If two active systems claim the same exclusive identity unexpectedly, FORGE treats this as a security incident.

# Split Identity

Conflicting claims about current identity state may require suspension until resolved.

# Identity Registry

FORGE should maintain an authenticated registry or equivalent source of current identity state.

# Registry Content

The registry may identify:

- active identities,
- credential versions,
- institutional membership,
- revocation,
- expiration,
- and trust relationships.

# Registry Is Not Authority Generator

Adding an entry to the registry must itself require legitimate governance.

# Registry Integrity

Identity-registry modification is high consequence.

# Distributed Identity State

Distributed deployments may replicate identity information.

Replication must preserve integrity and revocation semantics.

# Stale Identity State

A PEP using stale identity information may accept revoked authority.

High-risk enforcement should therefore use sufficiently fresh identity state.

# Offline Operation

Some deployments may need to operate temporarily offline.

Offline identity policy must define:

- acceptable credential age,
- cached revocation state,
- authority ceiling,
- and reconnection behavior.

# Offline Authority Reduction

Loss of current identity verification may reduce permitted authority.

It does not expand authority.

# Federation Identity

ADR-028 applies.

Remote FORGE identities require explicit trust relationships.

# Federation Key Rotation

Remote key rotation should be authenticated according to federation policy.

# Remote Key Replacement

A remote system saying:

> Trust this new key.

is not sufficient unless the replacement is authenticated through an accepted trust path.

# Communications Authentication

ADR-029 applies.

Authority-bearing messages should be attributable to authenticated senders.

# Message Signing

High-consequence messages may be individually signed where appropriate.

# Transport Authentication

Secure transport may authenticate a channel.

It does not necessarily provide durable evidence of each individual message.

# Evidence Authentication

ADR-017 applies.

Evidence artifacts should preserve source identity and integrity.

# Historian

Historian preserves identity lifecycle evidence without preserving unnecessary private key material.

# Auditor

Auditors verify:

- identity binding,
- credential validity,
- revocation,
- signature integrity,
- membership,
- and applicable trust chains.

# Watchers

Watchers may detect:

- unexpected identity use,
- duplicate identities,
- impossible concurrent sessions,
- or activity after revocation.

# Security

Security monitors:

- credential theft,
- impersonation,
- brute force,
- replay,
- unauthorized rotation,
- recovery abuse,
- and key exfiltration.

# Doctor

Doctor may monitor identity infrastructure health.

Identity service failure does not mean authentication becomes optional.

# Engineer

Engineer implements identity infrastructure.

Engineer does not gain Root authority merely because Engineer maintains authentication code.

# Teacher

Teacher may improve identity-anomaly detection.

Teacher cannot create new trusted identities through training.

# Reference Monitor

ADR-033 applies.

PEPs verify current authenticated identity and credential state before protected execution.

# Boot

ADR-023 applies.

Identity trust is established before normal governed autonomy begins.

# Recovery

ADR-014 applies.

Catastrophic identity compromise may require Constitutional Recovery.

# Decommissioning

ADR-024 applies.

Decommissioning revokes operational identities and prevents later resurrection.

# Transactions

ADR-034 applies.

Credential changes may themselves be multi-step transactions requiring atomicity and recovery planning.

# Root Key Rotation Transaction

Root rotation may include:

1. authorize rotation,
2. generate replacement trust material,
3. verify new key,
4. distribute new trust state,
5. activate new root,
6. revoke prior root,
7. verify PEP adoption,
8. preserve evidence,
9. close transaction.

Partial failure must be explicitly handled.

# Lost Root Key

Loss of the only Root Key must not automatically give FORGE power to appoint a new Root Human.

A predefined recovery procedure is required.

# Stolen Root Key

If Root compromise is suspected:

- suspend affected privileged authority where possible,
- preserve evidence,
- activate recovery procedures,
- rotate trust,
- revoke compromised credentials,
- verify dependent systems,
- and reassess actions performed during the compromise window.

# Compromise Window

FORGE should identify the period during which a compromised credential may have been abused.

# Historical Reassessment

Actions authenticated during a known compromise window may require additional audit.

# Key Compromise Does Not Rewrite History

Valid historical records remain preserved.

Their trust assessment may change.

# Credential Theft Does Not Transfer Legitimate Identity

An attacker using a stolen key may authenticate cryptographically.

FORGE should distinguish:

> Credential validated.

from:

> Legitimate human intentionally authorized this action.

Higher-risk human approvals may therefore require intent-bound authentication and anomaly detection.

# Authentication Factors

Factors may include:

- possession,
- knowledge,
- inherence,
- trusted device,
- or independent human approval.

# Factor Independence

Multiple factors sharing one compromise path may not provide meaningful independence.

# Recovery Codes

Recovery codes are credentials.

They require protection equivalent to their authority.

# Secret Questions

Weak or publicly discoverable recovery information should not be treated as strong Root authentication.

# Identity Proofing

Initial establishment of a privileged human identity requires trustworthy identity proofing appropriate to the deployment.

# Genesis Identity

ADR-023 Genesis Record should identify initial legitimate Root Governance identity or identities.

# Genesis Protection

FORGE cannot rewrite its Genesis identity record through ordinary runtime operations.

# Constitutional Amendment

ADR-008 applies.

Changes to foundational identity policy may require constitutional amendment.

# Risk Classification

ADR-032 applies.

Identity operations are classified according to consequence.

Examples:

Routine session renewal  
→ lower tier.

Institutional member key rotation  
→ elevated tier.

Root key replacement  
→ Tier 4.

# Epistemic Governance

ADR-031 applies.

Uncertain identity is not verified identity.

# Identity Confidence

Probabilistic identity matching may assist detection.

It does not substitute for required authentication.

# Facial Recognition

A model predicting:

> 99% likely the owner

does not necessarily satisfy Root Human authentication.

# Voice Recognition

Likewise, voice similarity alone should not automatically establish privileged authority.

# Behavioral Authentication

Behavioral patterns may support anomaly detection.

They should not silently become the sole Root credential.

# Deepfake Resistance

Privileged human authentication should consider impersonation technologies.

A realistic voice or video is not equivalent to cryptographic proof of intent.

# Human Presence

Some Tier 4 actions may require explicit human-presence confirmation according to deployment policy.

# Approval Clarity

Human approval interfaces should clearly identify:

- action,
- consequence,
- target,
- scope,
- and whether approval is one-time or continuing.

# Consent Ambiguity

Ambiguous human interaction does not become privileged approval.

# Formal Invariants

ADR-025 should support invariants such as:

> Authentication != Authorization

and:

> Identity != Jurisdiction

and:

> RevokedCredential cannot authenticate new authority

and:

> ExpiredCredential cannot authenticate new authority

and:

> RootApproval requires valid RootHuman authentication

and:

> KeyRotation cannot silently expand identity authority

and:

> OldBackup cannot resurrect revoked authority

and:

> DuplicateExclusiveIdentity → AuthoritySuspended

where applicable.

and:

> CredentialPurpose cannot be silently reused across incompatible authority domains.

# Identity Testing

FORGE should test:

- stolen credentials,
- expired credentials,
- revoked credentials,
- duplicate identities,
- replayed approvals,
- forged signatures,
- wrong-purpose signatures,
- stale identity registry,
- recovery abuse,
- root-key loss,
- root-key compromise,
- member replacement,
- machine cloning,
- federation key rotation,
- and decommissioned identity resurrection.

# Root Recovery Drills

High-value deployments should periodically verify that legitimate humans can recover control without giving FORGE unilateral authority to rewrite ownership.

# Key Rotation Drills

Critical credentials should be rotatable in practice, not merely in design.

# Revocation Drills

FORGE should verify that revocation actually reaches protected enforcement points.

# Identity Inventory

FORGE should maintain an inventory of authority-bearing identities and credentials.

Unknown privileged identities are unacceptable.

# Orphan Credential Detection

Security should detect credentials no longer associated with legitimate active identities.

# Least Credential

Components should possess only the credentials necessary for their current role.

# Credential Expiration by Default

Temporary components should prefer expiring credentials.

# No Credential Accumulation

FORGE should not accumulate old credentials simply because they may be useful later.

# Fail-Closed Rule

If FORGE cannot establish required identity or authentication for a consequential action, the action does not proceed.

Unknown identity is not authenticated identity.

Authentication is not authorization.

Possession of a credential is not proof of unlimited authority.

Loss of a Root Key does not make FORGE the new Root.

## Consequences

Identity governance introduces:

- explicit principal identities,
- credential lifecycle management,
- Root Key protection,
- rotation,
- revocation,
- recovery,
- identity registries,
- purpose-separated signing,
- anti-replay mechanisms,
- stronger human authentication,
- and anti-resurrection controls.

This increases operational complexity.

FORGE accepts this cost.

Every constitutional decision ultimately depends on being able to establish who actually exercised authority.

## Foundational Principle

> Identity says who you are.

> Authentication proves control of the credential representing that identity.

> Authorization says what you may do.

> Jurisdiction says what you may decide.

> A key is not a Constitution.

> A signature is not truth.

> Authentication is not unlimited authority.

> Root credentials belong outside ordinary autonomous control.

> Revoked authority stays revoked.

> Lost authority is recovered through governance, not self-appointment.

> FORGE may verify Root Human authority.

> FORGE may never manufacture it.

The constitutional chain is only as trustworthy as the identities at its foundation.
