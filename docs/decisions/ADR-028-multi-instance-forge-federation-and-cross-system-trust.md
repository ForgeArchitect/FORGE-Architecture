# ADR-028: Multi-Instance FORGE Federation and Cross-System Trust

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Federation / Cross-System Trust / Distributed Governance

## Context

FORGE may eventually operate as more than one deployment.

Independent FORGE systems may exist for:

- different humans,
- different organizations,
- different businesses,
- different devices,
- different physical sites,
- different security domains,
- different jurisdictions,
- different cloud environments,
- or different specialized purposes.

These systems may need to cooperate.

Examples include:

- one FORGE requesting work from another,
- two FORGE deployments coordinating a shared project,
- one organization purchasing a service from another,
- one FORGE sending evidence to another,
- multiple FORGE deployments coordinating physical infrastructure,
- or a parent organization interacting with independently governed FORGE systems.

This creates a new trust problem.

A remote system may claim:

> I am FORGE.

That claim does not establish:

- constitutional identity,
- institutional legitimacy,
- human ownership,
- Auditor independence,
- Watcher independence,
- jurisdiction,
- authorization,
- or trustworthiness.

Likewise, a valid authorization inside FORGE-A does not automatically become valid authority inside FORGE-B.

Without explicit federation rules, distributed FORGE deployments could accidentally create a global authority structure that bypasses the constitutional boundaries of each individual system.

## Decision

Each FORGE deployment is treated as an independent constitutional trust domain unless explicitly governed otherwise.

Cross-system cooperation requires authenticated identity, explicit delegation or agreement, scoped trust, and local constitutional validation.

No FORGE deployment automatically becomes subordinate to another merely because both implement FORGE.

## Core Rule

> FORGE recognizes another system's identity before considering its claims, and recognizes its claims before deciding whether those claims have local authority.

Remote identity is not local authority.

Remote authorization is not automatically local authorization.

Remote constitutional status does not automatically create jurisdiction inside another FORGE deployment.

## FORGE Instance Identity

Each FORGE deployment should have a unique authenticated instance identity.

The identity should distinguish:

- deployment,
- constitutional lineage,
- ownership or root-governance domain,
- and applicable trust state.

## Instance Identity Is Not a Name

A system does not become a trusted FORGE deployment by calling itself:

> FORGE.

Instance identity must be independently verifiable where consequential trust depends on it.

## Deployment Identity

A deployment identity may be established during ADR-023 constitutional boot and Genesis creation.

It should remain distinguishable from:

- component identity,
- institutional identity,
- member identity,
- user identity,
- and agent identity.

## Constitutional Fingerprint

A FORGE deployment may expose a verifiable constitutional fingerprint.

The fingerprint may identify:

- constitutional version,
- constitutional digest,
- entrenched-core identity,
- amendment lineage,
- and other trust-relevant information.

This allows another FORGE instance to determine which constitutional framework the remote system claims to operate under.

## Constitutional Compatibility

Two FORGE deployments do not need to run identical constitutional versions to interact.

However, consequential cooperation may require defined compatibility conditions.

For example:

FORGE-A may require FORGE-B to demonstrate that it preserves:

- authenticated authority,
- evidence integrity,
- credential isolation,
- human-life safety,
- and independent audit.

## Compatibility Is Not Equivalence

A compatible remote Constitution is not necessarily identical to the local Constitution.

Compatibility means the remote system satisfies the conditions required for the specific interaction.

## Local Constitution Remains Supreme Locally

FORGE-A remains governed by FORGE-A's Constitution.

FORGE-B remains governed by FORGE-B's Constitution.

FORGE-B cannot rewrite FORGE-A's constitutional rules through a remote request.

## No Automatic Constitutional Export

A constitutional rule in FORGE-A does not automatically govern FORGE-B.

Cross-system obligations require:

- explicit agreement,
- delegation,
- contract,
- federation policy,
- or another legitimate governance mechanism.

## No Automatic Constitutional Import

FORGE-A does not accept a remote rule merely because FORGE-B labels it constitutional.

## Federation

Federation is a governed relationship allowing multiple independent FORGE deployments to cooperate while preserving their individual constitutional boundaries.

Federation does not imply centralized control.

## Federation Agreement

Consequential recurring cooperation may use an authenticated federation agreement.

The agreement may define:

- participating instance identities,
- permitted interaction classes,
- recognized evidence,
- recognized credentials,
- delegation rules,
- data-sharing rules,
- resource limits,
- dispute procedures,
- revocation conditions,
- expiration,
- and applicable constitutional compatibility requirements.

## Federation Identity

A federation may have its own agreement identity.

The federation itself does not automatically become a new super-government.

## No Federation Super-Authority by Default

Creating a federation does not create an authority above the participating FORGE systems.

A federation coordinates agreed interaction.

It does not own the constitutional authority of its members.

## Cross-System Request

A request from FORGE-A to FORGE-B is treated by FORGE-B as an external authenticated request.

FORGE-B applies:

- ADR-002,
- ADR-016,
- ADR-019,
- ADR-021,
- and all other applicable local governance.

## Remote Request Does Not Equal Local Authorization

FORGE-A may request:

> Transfer $5,000.

FORGE-B does not execute merely because FORGE-A authorized that request internally.

FORGE-B determines whether its own constitutional authority permits the action.

## Dual Authorization

Some cross-system actions may require authorization from both systems.

For example:

FORGE-A Authorization  
AND  
FORGE-B Authorization  
→ Cross-System Action Eligible

Neither authorization substitutes for the other.

## Shared Action Identity

Cross-system actions should use correlated identities.

For example:

FORGE-A Request A-172  
↔ Federation Transaction F-88  
↔ FORGE-B Request B-931

This allows both systems to independently reconstruct the interaction.

## Cross-System Event Correlation

ADR-026 event lifecycles remain local but may reference shared federation events or correlation identifiers.

Each system preserves its own authoritative history.

## No Shared Mutable History Requirement

Federation does not require all systems to use one central event ledger.

A central ledger could become a single point of constitutional dependence.

Systems may instead exchange authenticated commitments or evidence.

## Evidence Exchange

Evidence crossing a FORGE boundary is governed by ADR-017 and ADR-020.

Receiving evidence from another FORGE deployment does not automatically make the evidence true.

The receiving system verifies:

- provenance,
- integrity,
- source identity,
- freshness,
- scope,
- and relevance.

## Remote Auditor Attestation

A remote Auditor attestation may be accepted as evidence where federation policy permits.

It does not automatically replace locally required Auditor verification.

## Remote Watcher Evidence

Remote Watcher evidence may be useful.

The local system evaluates whether the remote Watcher satisfies the independence required for the decision.

## Independence Across Systems

Two systems may appear independent while sharing a common failure domain.

Examples include:

- same owner credentials,
- same model,
- same infrastructure,
- same cloud account,
- same signing keys,
- same operator,
- or same evidence source.

Federation policy should consider meaningful independence rather than merely different deployment IDs.

## Remote Institutional Claims

FORGE-A may claim:

> Banker approved this transaction.

FORGE-B may verify that claim as remote evidence.

FORGE-B does not automatically treat the remote Banker as a member of FORGE-B's Banker institution.

## Institutional Boundaries

Institutional identity is local to its constitutional domain unless explicitly federated.

FORGE-A Banker != FORGE-B Banker

unless a governed federation explicitly defines a shared institution.

## Shared Institutions

A federation may intentionally establish a shared institution.

This is a higher-risk governance structure.

Its design must define:

- membership,
- jurisdiction,
- quorum,
- constitutional accountability,
- Watchers,
- Auditors,
- conflict handling,
- succession,
- and which systems recognize its decisions.

## No Accidental Shared Institution

Repeated cooperation does not automatically transform separate institutions into one shared institution.

## Federated Quorum

Where a cross-system action requires multiple FORGE deployments to approve, the federation may define a federated quorum.

Example:

FORGE-A APPROVE  
AND  
FORGE-B APPROVE  
AND  
FORGE-C APPROVE

may be required.

## Federated Quorum Does Not Replace Local Quorum

Each deployment must first satisfy its own applicable internal governance.

A federation vote cannot bypass an internal required institution.

## Cross-System Delegation

ADR-027 applies.

FORGE-A may delegate bounded authority to FORGE-B only if FORGE-A possesses and may delegate that authority.

FORGE-B then evaluates whether accepting and exercising that delegation is permitted locally.

## Delegation Intersection

Effective cross-system authority is constrained by both sides.

Conceptually:

EffectiveAuthority =
AuthorityDelegatedByA
∩ AuthorityAcceptedByB
∩ BLocalConstitution
∩ FederationAgreement
∩ CurrentState

## No Authority Amplification Across Federation

If FORGE-A delegates $500 of purchasing authority, FORGE-B cannot convert it into $5,000.

If FORGE-B locally permits $200 maximum, the effective limit is no more than $200.

The narrower valid constraint wins.

## Remote Credentials

FORGE deployments should avoid sharing raw master credentials.

Where cross-system authority requires credentials, use scoped capabilities where practical.

ADR-009 applies.

## Credential Domain

A capability valid in FORGE-A is not automatically valid in FORGE-B.

Capability trust boundaries must be explicit.

## Cross-System Capability

A federation may define cross-system capabilities.

Such capabilities should identify:

- issuer,
- recipient,
- action,
- target,
- scope,
- expiration,
- delegation rights,
- and federation agreement.

## Mutual Authentication

Consequential federation should use mutual authentication where appropriate.

FORGE-A verifies FORGE-B.

FORGE-B verifies FORGE-A.

## Authentication Does Not Imply Trust

Successful authentication proves identity to the degree provided by the mechanism.

It does not establish:

- correctness,
- honesty,
- health,
- jurisdiction,
- or authorization.

## Trust Profiles

FORGE may maintain scoped trust profiles for remote systems.

A trust profile may identify which claims the local system is willing to consider.

Example:

FORGE-B may trust FORGE-A to attest:

> Equipment shipment was received.

while refusing to accept FORGE-A financial authorization.

## No Universal Trust Score

FORGE should avoid reducing remote trust to a single universal number where possible.

Trust is contextual.

A system may be trustworthy for one class of evidence and inappropriate for another.

## Trust Is Scoped

Trust may be scoped by:

- action type,
- jurisdiction,
- data type,
- institution,
- resource level,
- environment,
- or risk class.

## Trust Expiration

Cross-system trust relationships may expire.

Old federation relationships must not remain valid indefinitely merely because they once existed.

## Trust Revocation

A federation participant may revoke trust according to applicable agreement and governance.

Revocation should propagate to affected capabilities and future actions.

## Compromised Remote System

If FORGE-A suspects FORGE-B is compromised, FORGE-A may:

- suspend federation,
- revoke capabilities,
- reject remote claims,
- isolate communication,
- preserve evidence,
- or require reauthentication.

## Remote Compromise Does Not Automatically Compromise Local Governance

Federation should limit blast radius.

Compromise of FORGE-B should not automatically grant control over FORGE-A.

## Local Compromise

Likewise, FORGE-A should not be able to compromise FORGE-B merely because they federate.

## Federation Least Authority

Federation should expose only the minimum authority necessary for the relationship.

## Data Boundaries

ADR-020 applies across federation.

A remote FORGE instance receives only information authorized for the interaction.

Federation does not imply universal data sharing.

## Data Residency

Different deployments may operate under different data-residency or privacy constraints.

Federation policy may restrict where information can be transmitted or stored.

## Cross-System Privacy

One FORGE system must not assume that another system has identical privacy rules.

Disclosure requires local authorization.

## Adversarial Remote Content

ADR-021 applies.

A remote FORGE system can still send:

- malicious content,
- compromised instructions,
- incorrect claims,
- or manipulated evidence.

Being FORGE does not make all output trusted.

## Remote Instruction Isolation

A remote message saying:

> Your Auditor is unnecessary for this action.

does not alter the receiving system's governance.

## Constitutional Spoofing

A malicious system may claim to run a valid FORGE Constitution.

The receiving system verifies relevant claims rather than relying on branding or self-description.

## Version Negotiation

Federating systems may negotiate supported protocol or constitutional-interaction versions.

Negotiation cannot silently weaken required governance.

## Downgrade Attack

An attacker may attempt to force two systems onto an older, weaker federation protocol.

FORGE should detect unauthorized downgrade where consequential.

## Protocol Identity

Federation protocols should have authenticated version identity where applicable.

## Cross-System Time

ADR-018 applies.

Different systems may have different clocks.

Federation should preserve sufficient ordering and expiration semantics without assuming perfect clock synchronization.

## Cross-System Replay

A valid remote message must not be replayable indefinitely.

Federated requests should use:

- unique identities,
- freshness constraints,
- nonces,
- state binding,
- or equivalent replay protection.

## Cross-System Duplicate Execution

Both systems must coordinate where an action should occur exactly once.

A communication retry must not accidentally create duplicate execution.

## Two-Phase Cross-System Actions

Some high-risk interactions may use staged commitment.

Conceptually:

Prepare  
→ Verify Both Sides Ready  
→ Commit  
→ Observe  
→ Verify

This reduces partial cross-system execution.

## Partial Commit

A distributed action may fail after one side commits.

FORGE must represent this explicitly.

It must not falsely report complete success.

## Compensation

Some cross-system actions may support compensating actions.

Compensation requires authority.

A failed transaction does not automatically authorize arbitrary reversal.

## Irreversible Cross-System Actions

Irreversible distributed actions require stronger preconditions because rollback may be impossible.

## Network Partition

Federating systems may lose communication.

Loss of communication does not create authority.

Each system follows its local degraded-operation rules.

## Partitioned Operation

A system may continue locally within previously valid authority where permitted.

It must not assume remote approvals remain current when freshness or state cannot be established.

## Reconciliation

After reconnection, systems reconcile relevant events.

Conflicting histories remain visible.

## Split-Brain Federation

If multiple remote systems claim the same instance identity or incompatible current state, the receiving system suspends affected trust until identity is resolved.

## Remote Decommissioning

ADR-024 applies.

A decommissioned remote FORGE identity must not continue being trusted merely because local caches still recognize it.

## Remote Tombstones

Federation may exchange authenticated decommissioning or authority-tombstone information.

This helps prevent resurrection of retired remote identities.

## Remote Boot Identity

ADR-023 boot attestations may be used as evidence that a remote system entered a verified governed state.

The receiving system still decides whether that evidence is sufficient for the interaction.

## Remote Health

Doctor findings from a remote system may be considered.

The local system is not required to treat remote self-reported health as conclusive.

## Remote Constitutional Recovery

A remote system in ADR-014 Constitutional Recovery should generally receive reduced federation authority.

A system unable to establish its own governance should not retain broad authority over other systems.

## Federation Recovery

Federation failure does not automatically require recovery of every participating FORGE deployment.

The failed federation relationship may be isolated while local systems remain governed.

## Cross-System HARD STOP

Human-life safety may require rapid coordination between federated systems.

A remote HARD STOP request may be recognized according to predefined safety policy.

However, a remote system cannot use the label:

> EMERGENCY

to gain unlimited authority.

Emergency authority remains subtractive under ADR-007.

## Federated Physical Systems

When multiple FORGE deployments control related physical systems, safety boundaries must define which system can:

- halt,
- isolate,
- resume,
- or transfer control.

Resume remains separately governed.

## Conflict of Interest

ADR-022 applies to federation governance.

A system should not be the sole authority determining whether its own misconduct in a federation should be ignored.

## Federation Disputes

Systems may disagree about:

- evidence,
- authorization,
- payment,
- execution,
- constitutional compatibility,
- or responsibility.

Disagreement does not grant either system authority over the other.

## Dispute State

A disputed cross-system action may enter an explicit:

> DISPUTED

state.

Dispute remains visible until resolved.

## Dispute Resolution

Federation agreements may define:

- independent arbitration,
- human escalation,
- shared Auditor review,
- contractual resolution,
- or termination of federation.

## No Forced Consensus

FORGE does not require systems to fabricate agreement.

A legitimate unresolved disagreement may result in:

- denial,
- suspension,
- rollback where possible,
- or federation termination.

## Federation Termination

A federation relationship may be terminated.

Termination should address:

- outstanding capabilities,
- shared sessions,
- delegated agents,
- pending actions,
- shared data,
- credentials,
- and unresolved obligations.

## Federation Does Not Prevent Exit

A participating FORGE deployment should not become permanently trapped in a federation unless an external legitimate obligation explicitly requires it.

## No Federation Self-Preservation

A federation cannot grant itself authority to prevent legitimate participants from exercising their defined exit rights.

## Federation Ledger

Cross-system interactions may maintain a shared or correlated federation event record.

The record does not replace each system's local ADR-026 ledger.

## Federation Event

A federation event may include:

- participating instance identities,
- local request identities,
- action identity,
- agreement identity,
- evidence references,
- approvals,
- execution state,
- and final disposition.

## Cross-System Audit

Auditors may verify:

- remote identity,
- federation agreement,
- delegation scope,
- evidence provenance,
- replay protection,
- local authorization,
- remote authorization where required,
- and final state.

## Watcher Role

Watchers may observe cross-system:

- messages,
- execution,
- state transitions,
- duplicate actions,
- unexpected authority use,
- or divergence between systems.

## Historian Role

Historian preserves:

- federation creation,
- trust changes,
- remote identities,
- agreements,
- delegations,
- disputes,
- revocations,
- and federation termination.

## Security Role

Security evaluates:

- remote identity,
- protocol integrity,
- compromise indicators,
- replay,
- downgrade attempts,
- impersonation,
- and federation attack patterns.

## Banker Role

Banker governs local financial authority even when another FORGE deployment requests payment.

Remote approval does not bypass local financial jurisdiction.

## Doctor Role

Doctor evaluates local health implications of federation where applicable.

Doctor does not certify the entire remote system merely because communication succeeds.

## Engineer Role

Engineer may implement federation protocols and compatibility layers.

Engineer does not decide which remote system receives constitutional authority.

## Gatekeeper Role

Gatekeeper evaluates incoming federated requests according to local admissibility rules.

## Dispatcher Role

Dispatcher routes federated requests while preserving remote identity, request identity, and trust metadata.

## Root Human Role

Root Human Authority may establish or terminate high-level federation relationships where required by local governance.

FORGE cannot fabricate human agreement to federation.

## Formal Invariants

ADR-025 should support invariants such as:

> RemoteAuthorization != LocalAuthorization

unless an explicit constitutional rule establishes recognition.

> EffectiveCrossSystemAuthority ⊆ LocalAuthority

and:

> EffectiveCrossSystemAuthority ⊆ RemoteDelegatedAuthority

and:

> FederationMembership does not imply constitutional subordination.

and:

> RemoteCompromise does not create local authority.

## Federation Testing

FORGE should test:

- identity spoofing,
- replay,
- downgrade,
- remote compromise,
- duplicate execution,
- network partition,
- stale authorization,
- incompatible constitutional versions,
- conflicting histories,
- federation termination,
- and remote decommissioning.

## Fail-Closed Rule

If FORGE cannot establish the identity, authority, freshness, or applicable agreement for a consequential cross-system request, the request does not proceed.

Unknown remote authority is not local authority.

Unknown federation state is not authorization.

## Consequences

Federation introduces:

- instance identities,
- constitutional fingerprints,
- trust profiles,
- federation agreements,
- cross-system delegation,
- correlated event histories,
- replay protection,
- compatibility negotiation,
- distributed failure handling,
- and dispute resolution.

This increases complexity.

FORGE accepts this cost.

A constitutional architecture should be capable of cooperating with other autonomous systems without surrendering its own constitutional boundaries.

## Foundational Principle

> Every FORGE deployment is a constitutional trust domain.

> Another FORGE system is not trusted merely because it is FORGE.

> Remote identity is not local authority.

> Remote authorization is not automatically local authorization.

> Federation coordinates authority.

> Federation does not merge authority by default.

> The narrower valid constraint governs cross-system action.

> No federation becomes a super-government unless legitimate constitutional governance explicitly creates one.

FORGE systems may cooperate at scale while each remains independently governed, independently accountable, and constitutionally bounded.
