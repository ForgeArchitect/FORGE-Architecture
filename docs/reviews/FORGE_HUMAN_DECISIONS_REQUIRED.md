# FORGE Human Decisions Required

**Date:** 2026-10-09
**Repository:** https://github.com/ForgeArchitect/FORGE-Architecture
**Status of this review:** advisory. Nothing here is owner approval, constitutional acceptance, or an ADR-008 amendment.

ADR-008 requires human approval before a constitutional amendment takes effect. Every new ADR in this branch is `Status: Proposed` and `Constitutional approval: Pending`. Accepting one is a human act. Rejecting one leaves ADR-001 through ADR-040 as they stand.

The handoff manifest set `constitutional_approval_granted` to false. Git history and the empty pull-request list show no later approval of DQ-001 through DQ-024.

## Decisions that block acceptance of a drafted ADR

| ID | Question for the owner | If unresolved |
| --- | --- | --- |
| HD-041 | Accept, modify, or reject ADR-041. In particular, decide whether a director may exist only as a non-voting coordinator. | ADR-041 stays Proposed. Institutions stay on ADR-003 and ADR-015. |
| HD-042 | Accept ADR-042's rule that the seven domain labels assign no jurisdiction. Separately, and only in a later record, decide whether any label becomes a real jurisdiction or a new institution. | The labels have no constitutional force. Existing institution names remain. |
| HD-043 | Accept or reject Synchro as a named single-use record, and accept or reject the fixed Historian, Auditor, and Security attestation set. Confirm Historian's attestation is lineage evidence only. | ADR-009 and ADR-018 still govern capabilities. No Synchro exists. |
| HD-044 | Accept or reject the five memory classes, including mandatory case isolation for reviewers. | ADR-020, ADR-005, ADR-010, and ADR-003 still govern memory and independence. |
| HD-045 | Accept or reject opt-in recording, the rolling buffer, and user long-term retention control. This capability is not implemented. Also decide the unresolved case where a user deletion request meets evidence ADR-017 requires to be kept. | No recording power is granted by the baseline. |
| HD-046 | Accept or reject manifests for internal institutional capabilities, and decide the threshold at which ordinary code becomes a manifested tool. | ADR-019 still governs external tools only, as written. |
| HD-047 | Accept or reject distinct lifecycle claims. Confirm Historian cannot authorize release or rollback by signing preservation. Decide who resolves disputes over whether a change contains learning content. | ADR-006, ADR-010, and ADR-005 still separate the roles without this ceremony. |
| HD-048 | Accept or reject local-first posture and the rule that cloud specialists cannot directly execute locally. This runtime is not implemented. | ADR-019, ADR-028, and ADR-033 still constrain remote execution without a local-first doctrine. |

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
