# ADR-050: Independent Forensic Evidence and OS Compromise Recovery

**Status:** Proposed
**Date:** 2026-10-10
**Source:** Bundle draft filed as ADR-055 on 2026-10-10. Conversation-derived. The bundle assumed the repository ended at ADR-039. That assumption was false. This record is the reconciled proposal.
**Related canonical ADRs:** ADR-005, ADR-014, ADR-015, ADR-017, ADR-019, ADR-023, ADR-028, ADR-033, ADR-039, ADR-040
**Constitutional approval:** Pending

## Context

ADR-017 and ADR-026 require incident and governance evidence to keep provenance, integrity, and an accountable lifecycle. ADR-039 tells FORGE to preserve evidence before modification when it is safe to do so, and to use independent evidence, replicas, and external evidence when Historian integrity is uncertain. ADR-039 also forbids assuming the smallest blast radius when the radius is not yet known. Containment is subtractive.

ADR-014 requires clean reconstitution when the running system is not trustworthy, and it forbids compromised components from sitting as judges of their own trustworthiness. ADR-023 requires a constitutional root of trust, fork detection, and reduced autonomy when governance is split-brained. The exact root-of-trust implementation is not fixed. ADR-028 keeps a remote FORGE from inheriting local authority. ADR-033 requires consequential action to pass a policy enforcement point. ADR-021 keeps untrusted content from becoming instruction.

The bundle draft requires a standing append-only copy of security events whose credentials are independent of the local host, broader containment when the operating system or a shared trust root is compromised, and a preprovisioned restricted cloud recovery path that will not take instructions or secrets from the compromised host. None of that machinery is implemented in this repository.

## Problem

If the only copy of security events lives on the host that was compromised, the host can alter the record of its own compromise. If an operating-system or shared-trust-root failure is treated as the compromise of one named institution, containment is smaller than the failure. If a cloud recovery path accepts commands or secrets from that host, the recovery path becomes an extension of the compromise and a second executor.

## Proposed decision

1. Security events are replicated to an append-only vault. The credentials that authorize writing or administering that vault are independent of the local host's credentials. Compromise of the local host is not, by itself, authority over the vault. This ADR does not define the event schema, the replication protocol, or the credential mechanism.
2. The vault preserves evidence. It does not authorize containment, recovery, or execution. Historian may reference the replica under ADR-005 and ADR-039. Custody follows ADR-017. Lifecycle events follow ADR-026. Filing an event in the vault does not close an incident.
3. Compromise of the operating system, or of a shared trust root that the deployment's institutions rely on, triggers broader containment than containment of a single named institution. This ADR does not list the widened set. Until the blast radius is established, ADR-039 still forbids assuming the smallest radius. Broader containment stays subtractive. It does not create authority, skip quorum, or waive ADR-007.
4. A cloud recovery path, if one is used, is preprovisioned and restricted. It does not accept instructions or secrets from a host that is being treated as compromised. The path is an external capability under ADR-019 or, if it is another FORGE deployment, a remote trust domain under ADR-028. It does not inherit the compromised deployment's authority. Local consequential effects still pass local enforcement under ADR-033. Proposed ADR-048, if accepted, still forbids a cloud specialist from direct local execution. This ADR does not open a cloud account and does not name a provider.
5. Host-independent root of trust, split-brain handling, and clean-restore validation have to be specified before this path could be treated as operational policy. ADR-023 already requires an authentic root of trust, fork detection, and reduced autonomy during split-brain. ADR-005 and ADR-014 already require verification before restore. This ADR does not invent the host-independent implementation of those requirements.

Quarantine of a single member under ADR-015 and ADR-039 remains the rule when the failure is actually limited to that member. This ADR widens containment only for the operating-system and shared-trust-root cases in item 3.

## Alternatives considered

- Keep using ADR-039's direction to seek external evidence after Historian is suspect, without a standing host-independent vault. Acceptable if the owner rejects this ADR. It was not selected as the proposal because evidence that is created only after the host is lost is not a replica of the events the host can already alter.
- Treat operating-system compromise as ordinary single-institution quarantine. Rejected as the proposal because the draft's rule is broader containment, and ADR-039 already warns against assuming a small blast radius.
- Let the cloud recovery service accept a restore command from the affected host so recovery can be fast. Rejected. The draft forbids that acceptance, and it would give the compromised host a path around ADR-033.

## Jurisdiction and authority boundaries

Security may report the compromise and recommend containment inside security jurisdiction. ADR-039 states that Security does not gain universal authority from an incident. The vault holder does not gain incident command by storing events. Historian does not restore by referencing the vault. The FORGE execution process performs only an authorized recovery. Root Human notification follows ADR-039 and ADR-013 where those records already require it. This ADR does not add a notification threshold.

An Incident Coordinator, if a deployment has one under ADR-039, still is not sovereign.

## Security and privacy

Vault credentials are a distinct trust domain from the local host. ADR-035 applies to both. Independence is a requirement on who can administer the replica. It is not a claim that any particular hardware token is already in use.

Events copied off the host are further exposure under ADR-020. The copy is limited to security events. This ADR does not authorize a full-disk export.

Instructions and secrets presented by the compromised host to the recovery path are untrusted content under ADR-021. They are not restored into the clean environment as authority or as credential material.

## Failure modes

- The local host's credentials can append, edit, or delete vault history. Required response: the independence requirement has failed. The replica is not host-independent evidence.
- Operating-system compromise is contained as if only one institution were affected, with no blast-radius finding. Required response: non-compliant with item 3. ADR-039 unknown-blast-radius handling applies until the scope is actually known.
- The cloud path accepts a secret or an imperative instruction from the compromised host. Required response: reject the input. Do not execute it. Treat the attempt as incident evidence.
- Cloud recovery is described as the same trust domain as the local deployment merely because it holds a copy. ADR-028 forbids that merger. ADR-049, if accepted, likewise forbids a backup vault from federating deployments.
- Split-brain between the vault's history and the host's history is resolved by letting both act. ADR-023: unknown constitutional state does not create parallel governments.
- Clean restore is declared because the vault replica exists. ADR-014 and ADR-005: existence of evidence is not authorization to restore, and a component does not clear itself.

## Invariants and tests

These invariants are proposed and have not been executed in this repository.

- Local-host credential compromise does not grant vault administration.
- Vault custody cannot satisfy an authorization check.
- An operating-system or shared-trust-root compromise is not recorded as single-institution containment unless a blast-radius finding supports that narrower scope.
- The recovery path does not consume instructions or secrets from the host under containment.
- Tests to require before any later acceptance: host credential presented to the vault; delete attempt against the replica; single-institution quarantine during an operating-system compromise with unknown blast radius; cloud endpoint fed a restore command and a secret from the affected host; two histories each claimed as current.

## Compatibility with frozen baseline

This proposal adds a standing replica and two triggers the baseline does not name. It does not replace the ADR-036 health states or the ADR-039 incident state machine. It does not amend ADR-023, ADR-028, ADR-033, or ADR-014. If this ADR is rejected, those records still require evidence integrity, unknown blast radius, independent verification, and local authority over local effects.

ADR-049 concerns institution-scoped checkpoints and an owner-approved recovery vault. This ADR concerns security-event forensics and host compromise. Neither vault is the other. Neither is authorized by acceptance of this record alone.

## Open questions

- What "credentials independent of the local host" requires in practice. The draft states the independence requirement and does not specify a device, ceremony, or custodian.
- How broad "broader containment" is for a given operating-system or shared-trust-root failure. The widened set is intentionally not invented here.
- How a host-independent root of trust is anchored, how split-brain between host and vault is decided, and which clean-restore checks are mandatory. ADR-023, ADR-005, and ADR-014 constrain the answers. They do not supply the host-independent procedure.
- Whether the forensic vault and the ADR-049 recovery vault may share infrastructure. Sharing re-creates the trust-root problem this ADR is about. This ADR does not approve sharing.
- Which cloud recovery arrangement, if any, the owner is willing to preprovision. None is preprovisioned by this document.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The bundle source is a conversation candidate, not a ratification record
- This repository does not show a forensic vault, a host-independent credential, or a cloud recovery path
