# FORGE Human Decisions Required

**Date:** 2026-10-09 audit. Bundle rows added 2026-10-10. Earlier rows remain in force. Nothing in either pass is owner approval.
**Repository:** https://github.com/ForgeArchitect/FORGE-Architecture
**Status of this review:** advisory. Nothing here is owner approval, constitutional acceptance, or an ADR-008 amendment.

ADR-008 requires human approval before a constitutional amendment takes effect. ADR-041 through ADR-051 on this branch are `Status: Proposed` and `Constitutional approval: Pending`. Accepting one is a human act. Rejecting one leaves ADR-001 through ADR-040 as they stand.

The 2026-10-09 handoff manifest set `constitutional_approval_granted` to false. At that audit, git history showed no approval of DQ-001 through DQ-024. Pull request #1 later published the first proposed set. Merging it would not accept those ADRs.

## Decisions that block acceptance of a drafted ADR

| ID | Question for the owner | If unresolved |
| --- | --- | --- |
| HD-041 | Accept, modify, or reject ADR-041, including the 2026-10-10 evidence-backed output rule. Decide whether a director may exist only as a non-voting coordinator. A specialist quorum is not part of the proposal. | ADR-041 stays Proposed. Institutions stay on ADR-003 and ADR-015. |
| HD-042 | Accept ADR-042's rule that the seven domain labels assign no jurisdiction. Separately, and only in a later record, decide whether any label becomes a real jurisdiction or a new institution. | The labels have no constitutional force. Existing institution names remain. |
| HD-043 | Accept or reject Synchro as a named single-use record, and accept or reject the fixed Historian, Auditor, and Security attestation set. Confirm the Historian attestation is lineage and freshness evidence only, not approval. Signer key separation, compromised-signer procedure, and the redemption mechanism remain open. | ADR-009 and ADR-018 still govern capabilities. No Synchro exists. |
| HD-044 | Accept or reject the five memory classes, including mandatory case isolation for reviewers and logged governed retrieval. Log fields are not specified. | ADR-020, ADR-005, ADR-010, and ADR-003 still govern memory and independence. |
| HD-045 | Accept or reject opt-in recording, the rolling buffer, and user long-term retention control. This capability is not implemented. Also decide the unresolved case where a user deletion request meets evidence ADR-017 requires to be kept. | No recording power is granted by the baseline. |
| HD-046 | Accept or reject manifests for internal institutional capabilities, and decide the threshold at which ordinary code becomes a manifested tool. | ADR-019 still governs external tools only, as written. |
| HD-047 | Accept or reject distinct lifecycle claims. Confirm Historian cannot authorize release or rollback by signing preservation. Decide who resolves disputes over whether a change contains learning content. | ADR-006, ADR-010, and ADR-005 still separate the roles without this ceremony. |
| HD-048 | Accept or reject local-first posture and the rule that cloud specialists cannot directly execute locally. This runtime is not implemented. | ADR-019, ADR-028, and ADR-033 still constrain remote execution without a local-first doctrine. |
| HD-049 | Accept, modify, or reject ADR-049. Confirm that replication happens only under an owner-approved vault policy, that a backup hash is not proof a checkpoint was uncompromised, and that the vault does not restore across ADR-028 trust domains. The positive test for an uncompromised checkpoint, the manifest fields, and the encryption practice are still open. | ADR-005, ADR-014, and ADR-020 still govern checkpoints and backups. No vault is authorized. |
| HD-050 | Accept, modify, or reject ADR-050. Confirm host-independent vault credentials, broader containment for operating-system or shared-trust-root compromise, and the refusal of instructions and secrets from the compromised host. The widened containment set, the independent root of trust, split-brain handling, and clean-restore checks are still open. | ADR-017, ADR-023, ADR-028, ADR-039, and ADR-014 still govern evidence and recovery. No cloud recovery path is provisioned. |
| HD-051 | Accept, modify, or reject ADR-051. Confirm the four-domain split and that the network gateway does not become Dispatcher or Gatekeeper. Choose neither hypervisor nor dedicated hardware until a later decision. This layout is not implemented. | ADR-002, ADR-019, ADR-033, and ADR-038 still govern ingress, the constitutional boundary, enforcement, and promotion. Host layout stays open. |

## Decisions required before an implementation specification becomes policy

These items were not given new ADRs. The owner still has to approve any binding specification.

| ID | Queue | Decision needed |
| --- | --- | --- |
| HD-003 | DQ-003 | Whether specialized dispatchers may exist as workers under the single Dispatcher, and what registry and parallel-task behavior is allowed. They cannot become additional ingress authorities or authorizers. |
| HD-006 | DQ-006 | The question-package protocol: who may consolidate questions, how historical context is authorized, and how answers that change a request invalidate prior authorization. FORGE cannot turn consolidation into an institutional decision. |
| HD-007 | DQ-007 | The concrete approval matrix. The queue says this policy is unapproved. Any matrix must include every applicable jurisdiction from ADR-016 and the tier rules from ADR-032. Low tier is not a waiver of privacy, identity, or tool rules. No matrix was invented in this branch. |
| HD-011 | DQ-011 | The sealed dormant-replacement procedure, including what evidence counts as closure of the compromise path. Activation still follows ADR-015 and must not manufacture quorum. |
| HD-012 | DQ-012 | The reinstatement checklist and the meaning of "independent critical reviews." Historian supplies evidence. Security closes vectors inside security jurisdiction. FORGE executes only after the other authorizations exist. |
| HD-013 | DQ-013 | The pre-defined minimal trusted services and the critical operations that require human approval inside degraded mode. Safe mode, if named, has to be an ADR-011 degraded mode. The lists were not invented here. |
| HD-014 | DQ-014 | Whether to map pending, confirmed, restricted, and safe mode onto ADR-036 and ADR-039, or to leave the candidate vocabulary unused. Debounce must not delay an ADR-007 HARD STOP. Threshold numbers need an explicit human choice. |
| HD-019 | DQ-019 | Whether each agent has a dedicated Teacher assignment. Signed recipient-specific packages, sandbox evaluation, and governed promotion already follow ADR-010. Direct internal access stays forbidden. |
| HD-B050 | Bundle ADR-050 | Whether urgent work may be scheduled ahead of background analysis, and which authenticated role may mark work urgent. A caller's urgent label is not authorization, not a consequence-tier downgrade, and not a waiver of ADR-012 or ADR-032. No scheduler was specified. |

## Decisions required because drafting stopped

| ID | Queue | Decision needed |
| --- | --- | --- |
| HD-004 | DQ-004 | Whether to amend ADR-029 so that constitutionally permitted peer messages and institutional queries are forbidden and every lateral contact becomes a Dispatcher and Gatekeeper package. Until that amendment is approved, ADR-029 stands. Mesh or peer-to-peer technology, if used, is transport only. |
| HD-008 | DQ-008 | No decision is required to keep the compatible reading. A decision is required if the owner wants Historian to approve institutional existence. That want conflicts with ADR-015 and ADR-005 and was not drafted. |
| HD-023 | DQ-023 | Whether the personal-assistant vision becomes a non-exclusive deployment profile. An exclusive "one FORGE per person" rule conflicts with ADR-028 and was not drafted. Independent memory and no automatic cross-FORGE learning transfer are already the federation and privacy baseline. |
| HD-024 | DQ-024 | Whether wearables, voice, contextual assistance, consent-based listening, or device integration should ever leave the roadmap. They are not implemented and are not in the ADR-040 baseline. Consent-based listening is not authorized by ADR-045. |

## Decisions already covered, with no new approval sought

These stay as written in the Accepted ADRs. This review does not ask the owner to re-approve them.

| Queue | Why no new approval is sought |
| --- | --- |
| DQ-005 | Request identity, hashes, independent Watchers and Auditors, and privacy-limited disclosure are ADR-002, ADR-004, ADR-017, and ADR-020. |
| DQ-010 | Replay, nonce and expiry binding, quarantine, and non-redeemable historical evidence are ADR-017, ADR-018, and ADR-029. |
| DQ-015 | Incident closure criteria, the closure record, and Historian preservation are ADR-039 and ADR-005. |
| DQ-016 | Lightweight handling of low-consequence informational work, without dropping privacy, identity, or tool boundaries, is ADR-032 together with ADR-020, ADR-035, and ADR-019. |

## What would count as approval

A later human approval would need to be explicit about which ADR or which human-decision row it accepts. A comment in a design conversation, a merged documentation pull request, or an edit that only fixes prose would not by themselves satisfy ADR-008.

This branch does not merge itself and does not change `main`.

## Bundle crosswalk (2026-10-10)

These rows record the owner question for each bundle draft. Where the question is the same as an earlier row, that earlier row remains the decision. Revisions to proposed ADR-041, ADR-042, ADR-043, ADR-044, and ADR-046 are part of the acceptance question for HD-041, HD-042, HD-043, HD-044, and HD-046. The 2026-10-10 text is what would be accepted or rejected.

| ID | Bundle draft | Decision needed |
| --- | --- | --- |
| HD-B040 | Bundle ADR-040 | None. Duplicate of Accepted ADR-040. Do not re-approve the baseline by accepting a second file. |
| HD-B041 | Bundle ADR-041 | Same acceptance question as HD-041, now including evidence-backed outputs. A specialist quorum is not proposed. Pull request #2's layer numbers are not part of the proposal. |
| HD-B042 | Bundle ADR-042 | Same as HD-008 and HD-042. Do not make Information and Knowledge Management, Librarian, or Historian the approver of institutional existence. |
| HD-B043 | Bundle ADR-043 | Same as HD-004 and HD-003. Do not amend ADR-029. Specialized dispatchers cannot become a second ingress or an authorizer. |
| HD-B044 | Bundle ADR-044 | Same as HD-006. The fanout and question-package protocol is not a constitutional ADR until the owner approves a specification that does not let FORGE rewrite institutional questions. |
| HD-B045 | Bundle ADR-045 | Same as HD-007. No approval matrix was written. Lifecycle checks do not replace ADR-016. |
| HD-B046 | Bundle ADR-046 | Same as HD-043, including the 2026-10-10 open questions: signer key separation, compromised-signer procedure, and the atomic-redemption mechanism. Historian freshness is evidence, not approval. |
| HD-B047 | Bundle ADR-047 | Same as HD-011. Do not activate a dormant replacement outside ADR-015, and do not use it to manufacture quorum. The widened quarantine set is not specified. |
| HD-B048 | Bundle ADR-048 | Same as HD-012. Historian evidence is not restoration authority. No count of independent reviews was chosen. |
| HD-B049 | Bundle ADR-049 | Same as HD-013 and HD-014. Do not adopt pending, confirmed, restricted, or safe mode as a second state machine. Do not invent numeric thresholds. |
| HD-B050 | Bundle ADR-050 | New. See the implementation-specification table. The fast-lane boundary itself needs no new approval. The urgent-work scheduler does. |
| HD-B051 | Bundle ADR-051 | Same as HD-044, now including logged governed retrieval. Log fields are not specified. |
| HD-B052 | Bundle ADR-052 | Same as HD-019. Librarian is not created. Learning still grants no authority under ADR-010. |
| HD-B053 | Bundle ADR-053 | Same as HD-046. The simulation sentence cites Accepted ADR-037 and does not by itself change the manifest decision. |
| HD-B054 | Bundle ADR-054 | HD-049. |
| HD-B055 | Bundle ADR-055 | HD-050. |
| HD-B056 | Bundle ADR-056 | HD-051. |

Accepting a documentation pull request, including this one, is not acceptance of any Proposed ADR and is not an ADR-008 amendment.
