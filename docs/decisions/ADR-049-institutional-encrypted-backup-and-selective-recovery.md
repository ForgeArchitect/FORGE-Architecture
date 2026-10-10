# ADR-049: Institutional Encrypted Backup and Selective Recovery

**Status:** Proposed
**Date:** 2026-10-10
**Source:** Bundle draft filed as ADR-054 on 2026-10-10. Conversation-derived. The bundle assumed the repository ended at ADR-039. That assumption was false. This record is the reconciled proposal.
**Related canonical ADRs:** ADR-005, ADR-014, ADR-016, ADR-017, ADR-020, ADR-028, ADR-029, ADR-040
**Constitutional approval:** Pending

## Context

ADR-005 gives Historian custody of authenticated checkpoints and withholds restoration authority. A checkpoint is not safe merely because it exists. Recovery authorization is bound to the selected checkpoint and the affected scope. Where technically possible, FORGE prefers the smallest recovery scope that can resolve the failure. Whole-system restoration remains a highest-risk governed action.

ADR-014 refuses to trust a checkpoint solely because Historian labels it known-good, and it requires independent verification where Historian itself may be compromised. ADR-020 keeps backups that contain sensitive information inside data governance. Replication of protected information is exposure. Restoring a checkpoint must not restore revoked access, deleted credentials, expired permissions, or obsolete sharing. ADR-028 keeps each FORGE deployment its own trust domain unless federation is governed.

The bundle draft adds a pattern the accepted records do not require: separately protected institution-scoped checkpoints, replication into an owner-approved encrypted recovery vault, selective restore of an affected domain only when isolation is verified, and a cross-institution recovery manifest. No vault, checkpoint store, or restore implementation exists in this repository.

## Problem

A single shared checkpoint store lets compromise or custody of one institution's recovery data expose another institution. An ungoverned extra copy violates ADR-020 even when the copy is called a backup. A selective restore that proceeds without a verified isolation boundary can put a clean component back into a still-shared failure domain. A hash of the backup can be mistaken for proof that the checkpoint was clean when it was taken.

## Proposed decision

1. Institution-scoped checkpoints are protected separately. Access, custody, or credentials for one institution's checkpoint are not access to another institution's checkpoint. ADR-020 compartmentalization applies to the backup copy as well as to the live data.
2. Those checkpoints may be replicated to an owner-approved encrypted recovery vault. Replication is allowed only under that owner approval. Inside an already approved vault policy, later checkpoints may replicate without a new approval for each copy. If no vault has been approved, this ADR authorizes no replication. This record does not name a product, an encryption algorithm, or a key hierarchy.
3. The vault is a recovery store. It is not a second Historian and not an executor. Historian may preserve evidence that a replica exists. Historian does not restore from the vault. Authorized restoration remains the FORGE execution process under ADR-005 and ADR-014.
4. Selective restoration is limited to the affected domain, and only when isolation of that domain has been verified. In this ADR, that domain is the institution or component whose boundary was checked. It is not another FORGE deployment under ADR-028. If isolation cannot be verified, this ADR does not authorize selective restore. Whole-system and catastrophic recovery under ADR-005 and ADR-014 remain available. A shared vault does not federate deployments and does not transfer authority across trust domains.
5. A recovery manifest may record which institution-scoped checkpoints are compatible for one recovery action. This ADR does not define the manifest's fields. Possession of a manifest is not authorization to restore. Changing the checkpoint or the scope still requires renewed authorization under ADR-005.
6. A valid backup hash shows that the stored bits match the hash. It does not prove the checkpoint was uncompromised when taken, and it does not prove the checkpoint is safe to restore. ADR-005 and ADR-014 already refuse to treat existence, or a Historian "known good" label, as sufficient trust. ADR-017 still governs integrity and custody of the backup as evidence.

Automatic replication is the approved policy operating, not an exception to attribution. Each replica remains attributable under ADR-020. This ADR does not weaken retention, deletion, or the rule that a backup of a secret is still exposure.

## Alternatives considered

- Leave backups entirely to ADR-005, ADR-014, and ADR-020, with no per-institution protection rule and no vault. Acceptable if the owner rejects this ADR. It was not selected as the proposal because a shared checkpoint store is a practical way to collapse the information boundaries those ADRs already require.
- Require a fresh human approval for every checkpoint copy. Rejected as the proposal because the draft's rule is an owner-approved vault with replication inside that approval. The owner may still choose the stricter cadence. This ADR does not.
- Treat a matching hash as proof the checkpoint is clean. Rejected. The draft states the opposite, and ADR-014 already rejects label-only trust.

## Jurisdiction and authority boundaries

Historian preserves checkpoint evidence and may identify candidate recovery points. Historian does not approve or perform the restore. Auditor verification of integrity remains Auditor work under ADR-005 and ADR-014. Doctor health findings remain Doctor work. The institutions whose state would be restored participate under ADR-016 when the consequence requires them. FORGE executes only the authorized restoration.

The vault operator, if distinct from Historian, receives no institutional jurisdiction by holding ciphertext. Owner approval of a vault is not Root Human authority to restore, and it is not an ADR-008 amendment.

## Security and privacy

Vault contents stay under the classification of the data they copy. ADR-020 applies. Encryption is not authorization. ADR-029's rule that an encrypted message is not automatically an authorized message is the same kind of limit: secrecy of the copy does not make the copy trustworthy or permitted.

Replicas of credentials follow ADR-009 and ADR-035. Raw long-lived secrets are not given a broader audience because they sit in a recovery vault.

A vault that cannot explain which institution a checkpoint belongs to is not separately protected, and this ADR does not treat it as compliant.

## Failure modes

- One institution's checkpoint credentials read another institution's checkpoint. Required response: the separation has failed; selective restore from that store is not authorized until the boundary is re-established.
- Replication starts with no owner-approved vault. Required response: stop. Copies already made are governed exposures under ADR-020, not an implicit approval.
- Selective restore runs while isolation is unverified. Required response: deny under this ADR. A larger governed recovery may still be requested under ADR-005 or ADR-014.
- A hash match is offered as the only evidence that the checkpoint is uncompromised. Required response: insufficient. Integrity of the bits and trustworthiness of the contents are different questions.
- A restore from the vault reintroduces revoked credentials or expired sharing. ADR-020 forbids that outcome. The restore is not successful.
- The vault is used to restore one deployment into another deployment's authority. ADR-028: remote or copied state does not become local authority. This ADR does not authorize that restore.

## Invariants and tests

These invariants are proposed and have not been executed in this repository. There is no vault and no checkpoint implementation here.

- Institution-scoped checkpoint access is partitioned by institution.
- Replication without an owner-approved vault policy is denied.
- A hash match cannot satisfy a "checkpoint was uncompromised" check.
- Selective restore without a verified isolation boundary is denied.
- Historian cannot execute the restore by possessing the replica.
- Tests to require before any later acceptance: cross-institution checkpoint read; replication with no owner approval; restore authorized for institution A and attempted against institution B; hash-only trust decision; restore that revives a revoked credential.

## Compatibility with frozen baseline

This proposal specializes ADR-005, ADR-014, and ADR-020. It does not amend them. It does not amend ADR-028. If the owner rejects the vault or the per-institution split, the baseline checkpoint and backup rules still stand.

ADR-040 does not require this pattern. Accepting this ADR would be a further decision, not a silent change to the v1.0 baseline.

## Open questions

- Who besides the owner may approve the vault policy, and whether that approval is institutional, Root Human, or both. This ADR says the vault is owner-approved and does not further specify the seat.
- How separate protection is enforced when checkpoints share a host. ADR-051, if accepted, is a related isolation proposal and is not assumed here.
- The manifest fields, the replication cadence, and the encryption and key-custody practice. None of these are specified in the draft or the accepted ADRs, and none are invented here.
- Which evidence, beyond a hash, is sufficient to decide that a checkpoint was uncompromised at creation. The negative rule is decided above. The positive test is open.
- How ADR-020 deletion and ADR-017 retention apply to vault copies when the live data is deleted.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The bundle source is a conversation candidate, not a ratification record
- This repository does not show a recovery vault, an encrypted backup, or a selective-restore test
