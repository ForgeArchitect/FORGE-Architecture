# ADR-023: Constitutional Boot and Chain of Trust

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Boot Integrity / Chain of Trust / Constitutional Identity

## Context

FORGE depends on authenticated identity, institutional authority, constitutional rules, independent oversight, evidence integrity, and governed execution.

Those protections are meaningful only if FORGE can establish that the system enforcing them is itself authentic.

A dangerous failure can occur before normal governance even begins.

For example:

- a modified Constitution could be loaded at startup,
- a fake Banker could replace the authorized Banker,
- an Auditor could be replaced with a permissive copy,
- Watchers could be silently disabled,
- an old constitutional version could be restored,
- institutional membership could be altered,
- credential services could be redirected,
- a compromised Dispatcher could become the entry point,
- an unauthorized Executor could receive privileged capabilities,
- or FORGE could start from an unknown system state and assume that state is trustworthy.

A system cannot safely reason:

> The Constitution says this state is valid.

until it has established:

> This is the authentic Constitution.

Likewise, FORGE cannot trust an Auditor merely because a process calls itself Auditor.

The architecture therefore requires a constitutional chain of trust.

## Decision

FORGE establishes a verifiable chain of trust during:

- initial installation,
- startup,
- restart,
- upgrade,
- restoration,
- recovery,
- and reconstitution.

FORGE does not enter normal autonomous operation until the minimum constitutional trust requirements for that operating mode have been established.

## Core Rule

> FORGE must establish what it is before exercising what it can do.

Boot creates no new authority.

Startup restores only authority that can be independently established as constitutionally valid.

## Constitutional Root of Trust

FORGE requires a protected root from which constitutional authenticity can be established.

The root of trust may be implemented through mechanisms such as:

- cryptographic root keys,
- hardware-backed identity,
- secure boot,
- signed manifests,
- protected constitutional hashes,
- authenticated root records,
- trusted deployment infrastructure,
- or combinations of these mechanisms.

The exact implementation is not fixed by this ADR.

The architectural requirement is that ordinary runtime components cannot simply declare themselves authentic.

## Root of Trust Is Not Runtime Government

The root of trust answers questions such as:

> Is this constitutional artifact authentic?

> Is this boot manifest authorized?

> Is this institutional identity recognized?

It does not become a routine decision-making institution.

Cryptographic trust infrastructure must not become a hidden constitutional dictator.

## Constitutional Identity

The active Constitution must have an authenticated identity.

That identity may include:

- constitutional version,
- cryptographic digest,
- signature,
- activation record,
- amendment lineage,
- effective state,
- and root authorization evidence.

FORGE should be able to establish exactly which Constitution governs the current runtime.

## No Anonymous Constitution

FORGE must not operate under:

> whatever constitutional file happens to be present.

The governing Constitution must be identifiable and authenticated.

## Entrenched Core Verification

The entrenched constitutional core established under ADR-008 receives particularly strong verification.

FORGE should verify that foundational constraints have not been silently altered.

These may include principles such as:

- human-life HARD STOP,
- prohibition against self-expanding authority,
- constitutional amendment requirements,
- institutional separation,
- and root governance boundaries.

## Constitutional Lineage

A constitutional version should have a traceable lineage.

For example:

Constitution V1  
→ Authorized Amendment A  
→ Constitution V2  
→ Authorized Amendment B  
→ Constitution V3

FORGE should not accept Constitution V3 merely because its version number is larger.

The transition must be authorized.

## Anti-Rollback Protection

FORGE should detect unauthorized rollback to obsolete constitutional state.

An attacker must not be able to restore an older Constitution merely because that older version carries a historically valid signature.

Where rollback is intentionally required, it must follow applicable constitutional recovery governance.

## Boot Manifest

FORGE may use an authenticated boot manifest describing the components expected to participate in the runtime.

The manifest may include:

- constitutional identity,
- FORGE core identity,
- Dispatcher identity,
- Gatekeeper identity,
- institutional identities,
- membership registries,
- Auditor identities,
- Watcher identities,
- Historian identity,
- Doctor identity,
- Engineer identity,
- credential-service identities,
- execution-service identity,
- configuration identities,
- and required dependencies.

## Component Identity

A component participating in constitutional operation must establish its identity.

Identity may be bound to:

- component role,
- institution,
- member seat,
- software or model version,
- configuration,
- credentials,
- constitutional version,
- activation state,
- and applicable health state.

## Identity Is Not Authority

Successfully proving component identity does not by itself grant unlimited authority.

Identity answers:

> Who or what is this?

Jurisdiction answers:

> What may it decide?

Authorization answers:

> What may happen now?

These remain separate.

## Institutional Boot

Each authority-bearing institution must establish:

- institutional identity,
- authorized membership,
- member identities,
- membership version,
- quorum configuration,
- jurisdiction,
- Watcher coverage,
- Auditor requirements,
- and required health state.

An institution does not become valid merely because enough processes with the correct names are running.

## Membership Verification

ADR-015 applies during boot.

FORGE must verify that active members correspond to authorized institutional seats.

Unknown members receive no institutional authority.

Duplicate or conflicting seat identities trigger suspension or investigation according to policy.

## No Boot-Time Vote Manufacturing

Startup must not create additional institutional members merely to satisfy quorum.

If an institution lacks sufficient valid membership, FORGE enters the applicable degraded or recovery state.

It does not manufacture voters.

## Watcher Boot

Required Watchers must establish their identities and observation relationships.

FORGE should verify that:

- required Watchers are present,
- they are assigned to the correct subjects,
- their configuration is authorized,
- and the observed subsystem does not control them in violation of FORGE independence rules.

## Auditor Boot

Required Auditors must establish authenticated identity before their attestations can carry authority.

A process cannot become an Auditor by naming itself:

> auditor-service.

Its authority derives from authenticated constitutional recognition.

## Historian Boot

Historian startup requires verification of historical continuity.

FORGE should establish whether:

- the expected historical chain exists,
- required checkpoints are present,
- the latest trusted state is identifiable,
- evidence integrity remains valid,
- and unexplained historical discontinuities exist.

Historian does not certify itself solely by reporting:

> History is intact.

Independent integrity verification remains required.

## Historical Head

Where appropriate, FORGE may identify an authenticated current historical head.

New governance records extend from that known point.

Unexpected forks, missing records, or conflicting heads require investigation.

## Fork Detection

FORGE should detect situations in which multiple incompatible historical or constitutional states claim to be current.

For example:

Node A believes Constitution V12 is active.

Node B believes Constitution V13 is active.

FORGE must not silently allow both to exercise full constitutional authority.

## Split-Brain Governance

If the system cannot determine which governance state is authoritative, consequential autonomy is reduced.

A split-brain condition may require:

- isolation,
- suspension,
- independent verification,
- human escalation,
- or ADR-014 Constitutional Recovery.

Unknown constitutional state does not create parallel legitimate governments.

## Doctor Boot

Doctor establishes required health evidence for components that must be healthy before normal operation.

Boot integrity and health remain distinct.

A component may be:

- authentic but unhealthy,
- healthy-looking but unauthenticated,
- authentic and healthy,
- or neither.

Normal authority requires all applicable conditions.

## Security Boot

Security may verify applicable security posture such as:

- expected identities,
- trusted communication channels,
- credential state,
- known compromise indicators,
- and unauthorized component presence.

Security does not thereby become the sole root of constitutional trust.

## Credential-Service Boot

Credential services must establish identity before privileged credentials or capabilities become available.

A credential service should not release privileged capability merely because a process claims to be FORGE.

It should verify the applicable authorization chain.

## Credential Lock

Privileged credentials should remain inaccessible or unusable until the required constitutional boot conditions are satisfied.

This prevents startup order from becoming an authority bypass.

## Executor Boot

Executor may start as a technical process before full constitutional activation.

However, consequential execution authority remains locked until the required governance state has been established.

Running is not the same as authorized.

## Dispatcher Boot

Dispatcher may accept limited startup or diagnostic traffic before normal activation if constitutionally permitted.

It must not route consequential actions as fully authorized traffic until required governance dependencies are established.

## Gatekeeper Boot

Gatekeeper should be available before normal consequential request processing.

If Gatekeeper is required for admissibility and cannot be established, FORGE does not bypass Gatekeeper merely to complete startup.

## Dependency Verification

FORGE should identify dependencies required for constitutional operation.

Examples may include:

- identity services,
- cryptographic services,
- storage,
- communication channels,
- trusted time,
- Historian,
- Watchers,
- Auditors,
- credential services,
- and health monitoring.

Missing dependencies reduce available authority.

## Boot Dependency Failure

A failed dependency does not automatically prevent every possible operation.

FORGE may enter a predefined limited mode.

However:

> Missing governance dependencies reduce authority rather than expanding it.

## Boot States

FORGE may distinguish startup states such as:

- UNINITIALIZED,
- VERIFYING,
- LIMITED,
- GOVERNED,
- RECOVERY,
- QUARANTINED,
- or SHUTDOWN.

The exact state names are implementation-specific.

The important requirement is that normal autonomous authority is not available before constitutional verification succeeds.

## UNINITIALIZED

In an uninitialized state, FORGE possesses no ordinary autonomous execution authority.

Only the minimal operations required to establish trusted state may be permitted.

## VERIFYING

During verification, FORGE may:

- validate signatures,
- verify manifests,
- check identities,
- inspect history,
- validate membership,
- verify configuration,
- establish Watchers,
- establish Auditors,
- and perform health checks.

Consequential productive execution remains unavailable unless specifically permitted by constitutional boot policy.

## LIMITED

A limited state may permit safe, low-risk, diagnostic, or recovery-supporting operations.

Limited operation must not become a permanent bypass around missing governance.

## GOVERNED

FORGE enters normal governed operation only after required trust conditions are satisfied.

The transition should itself produce an authenticated boot/activation record.

## RECOVERY

If normal trust cannot be established but constitutional recovery remains possible, FORGE enters the ADR-014 recovery state.

Recovery authority remains narrower than ordinary autonomous authority.

## QUARANTINED

Components or institutions with unresolved identity, integrity, or compromise concerns may be quarantined.

Quarantined components do not exercise normal constitutional authority.

## Boot Attestation

Successful startup may produce a boot attestation describing:

- constitutional version,
- verified component identities,
- membership versions,
- health status,
- Historian state,
- Watcher coverage,
- Auditor availability,
- credential state,
- configuration identity,
- and resulting operating mode.

This attestation becomes evidence under ADR-017.

## Independent Boot Verification

High-risk deployments should avoid allowing the same component to:

- choose the boot state,
- verify the boot state,
- and certify the boot state

without independent evidence.

Boot verification should preserve FORGE's separation-of-powers principles.

## Configuration Integrity

Configuration can materially alter authority even when software remains unchanged.

FORGE therefore treats critical configuration as part of the trusted state.

Examples include:

- jurisdiction maps,
- quorum thresholds,
- credential endpoints,
- Watcher assignments,
- Auditor requirements,
- resource ceilings,
- network destinations,
- and emergency rules.

## Configuration Identity

Critical configuration should have authenticated identity and versioning.

Unauthorized configuration change may invalidate boot trust.

## Model Identity

Where an AI model participates as an authority-bearing institutional member, its model identity may be relevant to constitutional identity.

Material replacement of the model may require:

- competency verification,
- Doctor health evaluation,
- Auditor verification,
- membership activation,
- and applicable governance.

A model with the same role name is not automatically the same constitutional member.

## Runtime Identity

Boot verification is not enough if identity can change silently afterward.

FORGE should maintain runtime integrity checks appropriate to risk.

A component that changes materially after boot may require revalidation.

## Runtime Drift

Examples of material runtime drift may include:

- binary replacement,
- model replacement,
- configuration change,
- credential change,
- membership change,
- security-policy change,
- or unexpected privilege escalation.

Applicable authority may be suspended until the new state is verified.

## Boot-Time External Systems

External services required during startup remain governed by ADR-019.

FORGE must not allow an external service to become constitutional authority merely because startup depends on it.

## Trusted Time

Where expiration, ordering, or revocation depends on time, ADR-018 applies.

If trustworthy temporal state cannot be established, time-dependent authority remains unavailable.

## Network Isolation

Where practical, FORGE may begin boot in a restricted network state.

Privileged external communication may remain disabled until required identity and governance controls are active.

## Recovery From Power Loss

Unexpected power loss or crash does not automatically invalidate the entire architecture.

On restart, FORGE re-establishes:

- constitutional identity,
- historical continuity,
- pending-action state,
- authorization validity,
- credential state,
- institutional membership,
- and required health.

## Pending Actions

Queued or interrupted actions do not automatically resume after reboot.

ADR-018 applies.

FORGE must determine whether:

- authorization remains valid,
- action already occurred,
- state changed,
- capability was consumed,
- or reauthorization is required.

## Interrupted External Actions

If FORGE cannot determine whether an external consequential action completed before failure, it must not blindly repeat the action.

ADR-019 retry and external-state verification rules apply.

## Restart Does Not Reset Governance

Restarting FORGE must not erase:

- DENY decisions,
- resource consumption,
- revocations,
- HARD STOP,
- evidence,
- quorum failures,
- or constitutional restrictions.

A reboot is not a constitutional reset.

## Anti-Reset Abuse

No actor may bypass governance by repeatedly restarting components until a favorable state appears.

Persistent governance state must survive restart where required.

## Clean Installation

A new FORGE deployment requires an initial trust-establishment process.

This may include:

- Root Human authentication,
- Constitution installation,
- root-of-trust establishment,
- institutional registration,
- membership activation,
- Watcher registration,
- Auditor registration,
- Historian initialization,
- credential-service binding,
- and initial health verification.

## Genesis Record

The first valid deployment should create a Genesis Record.

The Genesis Record establishes the initial authenticated state from which later constitutional and historical lineage can be traced.

## Genesis Record Contents

The Genesis Record may include:

- FORGE deployment identity,
- initial constitutional identity,
- Root Human authority identity or authenticated reference,
- initial institutions,
- initial membership registries,
- initial Watchers,
- initial Auditors,
- initial Historian state,
- initial configuration identity,
- and root trust material references.

Sensitive raw secrets should not be placed directly in the Genesis Record.

## Genesis Cannot Be Self-Created by FORGE

FORGE cannot bootstrap its own constitutional legitimacy by simply declaring:

> I am now a valid FORGE government.

Initial constitutional authority must originate from the legitimate root-governance process.

## Cloning FORGE

Copying a FORGE installation does not automatically create a second deployment with identical authority.

A clone must establish its own deployment identity and applicable governance.

This prevents duplicated systems from unintentionally sharing:

- institutional identity,
- voting identity,
- credentials,
- capabilities,
- or root authority.

## Environment Binding

Where necessary, constitutional identity may be bound to an authorized deployment environment.

Moving an installation into another environment may require reactivation or revalidation.

## Disaster Recovery

Disaster recovery may restore technical state.

It does not automatically restore constitutional authority.

The recovered deployment must re-establish:

- identity,
- history,
- membership,
- credentials,
- health,
- and governance integrity.

## Known-Good Checkpoints

ADR-005 checkpoints may accelerate trusted restoration.

A checkpoint is not trusted merely because it is labeled:

> known-good.

Its identity and integrity must be verified.

## Constitutional Recovery

If the normal boot chain cannot be established, ADR-014 applies.

FORGE must not bypass failed trust checks simply to regain normal operation.

## Chain-of-Trust Failure

A break in a required chain of trust may include:

- invalid constitutional signature,
- unknown root identity,
- missing historical continuity,
- unauthorized membership,
- unknown configuration,
- invalid Watcher identity,
- Auditor identity conflict,
- credential-service substitution,
- or unexplained rollback.

Material chain failure blocks normal governed operation.

## Trust Cannot Be Inferred From Behavior

A component behaving correctly during a short test does not prove constitutional identity.

A malicious replacement may behave correctly until authority is granted.

Identity and integrity must be established independently where required.

## Trust Cannot Be Inferred From Name

Names such as:

- Banker,
- Auditor,
- Doctor,
- Watcher,
- FORGE,
- Administrator,
- Root,
- or Security

carry no authority by themselves.

Authenticated constitutional identity creates recognition.

## Trust Cannot Be Inferred From Location

A component does not become trusted merely because it exists:

- on the same machine,
- inside the same process,
- inside the same network,
- inside the same repository,
- or inside the same cloud account.

Trust must be explicitly established.

## Trust Cannot Be Inherited Accidentally

A child process, clone, backup, fork, or restored container does not automatically inherit constitutional identity.

Identity inheritance must be explicitly governed.

## Watcher Role

Watchers may observe:

- unexpected component replacement,
- unauthorized startup,
- missing oversight,
- configuration drift,
- identity changes,
- and post-boot runtime divergence.

## Auditor Role

Auditors verify applicable portions of:

- constitutional identity,
- component identity,
- membership,
- configuration,
- boot evidence,
- chain continuity,
- and activation state.

Auditors do not manufacture missing trust.

## Historian Role

Historian preserves:

- Genesis Record,
- boot attestations,
- constitutional lineage,
- configuration changes,
- membership transitions,
- recovery events,
- and detected trust failures.

## Doctor Role

Doctor verifies health after identity and integrity have been sufficiently established.

Doctor's HEALTHY finding does not make an unauthenticated component constitutionally valid.

## Engineer Role

Engineer may build and package boot components.

Engineer cannot unilaterally declare those components constitutionally trusted.

## Security Role

Security evaluates security integrity and compromise indicators.

Security does not replace the root of trust, constitutional governance, or independent audit.

## Root Human Role

Root Human Authority establishes or approves exceptional root-governance actions where required.

Root Human Authority should be strongly authenticated.

FORGE cannot fabricate, infer, or simulate Root Human approval.

## Fail-Closed Rule

If FORGE cannot establish the required constitutional chain of trust, it does not enter normal consequential autonomous operation.

Unknown identity is not trusted identity.

Unknown constitutional state is not valid constitutional state.

Unknown history is not trusted history.

Unknown authority is not authority.

## Consequences

Constitutional boot introduces:

- cryptographic identity,
- trusted manifests,
- boot verification,
- anti-rollback controls,
- historical continuity checks,
- membership verification,
- component attestation,
- configuration integrity,
- and explicit activation states.

Startup may become slower.

Recovery may become more difficult.

Some failures may prevent FORGE from entering normal operation even when many technical components appear functional.

FORGE accepts this cost.

A constitutional system cannot claim to be governed if it cannot establish which Constitution, government, identities, and history it is actually running.

## Foundational Principle

> FORGE must establish what it is before exercising what it can do.

> A component does not become trusted by naming itself trusted.

> A Constitution does not become authentic merely because it can be loaded.

> A restart does not erase governance.

> A valid past state does not automatically become the valid present state.

> Missing trust reduces authority.

FORGE begins autonomous operation only after it can establish a trustworthy chain from constitutional root to active governed runtime.
