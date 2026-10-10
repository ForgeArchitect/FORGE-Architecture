# ADR-044: Memory Class Boundaries

**Status:** Proposed
**Date:** 2026-10-09
**Revision:** 2026-10-10 bundle reconciliation. The exact change is in the approval record.
**Source decision queue:** DQ-017. Bundle draft filed as ADR-051 on 2026-10-10 is the same memory-class decision and is reconciled here.
**Related canonical ADRs:** ADR-003, ADR-005, ADR-010, ADR-020, ADR-026, ADR-027, ADR-030, ADR-040
**Constitutional approval:** Pending

## Context

ADR-020 governs institutional memory, retention, and context isolation. It requires that information from one request not automatically enter unrelated requests, and that memory follow applicable policy. ADR-005 assigns long-term institutional history to Historian and withholds restoration and execution authority from that role. ADR-010 separates durable competence from jurisdiction. ADR-003 requires independent evaluation, including limits on when members see one another's substantive positions.

DQ-017 distinguishes persistent professional competence, expiring case working memory, case-isolated reviewers, Historian long-term history, and governed retrieval. The accepted ADRs state the principles. They do not define these classes as an explicit set.

No runtime memory implementation is present in this repository.

## Problem

A single memory store lets case facts become permanent competence, lets reviewers inherit the caseworker’s context, and lets retrieval from Historian function as a silent grant of the original authority. Those collapses defeat information boundaries and independent review.

## Proposed decision

FORGE memory used by institutions is divided into the following classes.

1. Professional competence. Durable, role-scoped capability and procedure that an institution may retain under ADR-010. Competence is not case evidence and does not expand jurisdiction.
2. Case working memory. Facts, drafts, and intermediate reasoning for one case. This class expires with the case authorization, the applicable retention policy, or an earlier revocation, whichever comes first. Expiration removes it from working use. Governance-critical evidence that must be retained follows ADR-017 and ADR-020 rather than remaining in working memory.
3. Case-isolated review context. A reviewer, Auditor, Watcher, or independent member receives a governed review view. The review view contains what that role needs. It does not automatically include another member's unshared deliberation when ADR-003 requires independent evaluation first.
4. Historian long-term history. Append-oriented institutional history under ADR-005. Historian preserves this class. Historian does not execute from it and does not approve current actions by returning it.
5. Governed retrieval. Reading any class is an access decision under ADR-020. Retrieval is mediated and purpose-limited. It is logged. This ADR does not define log fields. ADR-020 access auditing and ADR-026 apply where the access is governance-relevant. Retrieval for a consequential use is bound to the current authenticated request under ADR-002 and ADR-030. Retrieved history is evidence or context. It is not a reusable authorization. Case-isolated reviewers do not carry another case's memory into a new decision. Cross-case reading requires its own access decision.

Cross-class promotion is governed. A case fact becomes professional competence only through the learning path in ADR-010, not by remaining in a context window. A working-memory item becomes long-term history only when a preservation rule says it is governance evidence.

## Alternatives considered

- Rely on ADR-020's general memory and context-isolation rules without named classes. Rejected as the proposal because the queue's failure mode is specifically the collapse of competence, case memory, review context, and history into one store.
- Give every reviewer the full case working memory in the name of completeness. Rejected where it would defeat ADR-003 independent evaluation or ADR-020 least information.
- Let institutions keep case memory indefinitely because it may be useful later. Rejected. Long-term retention of governance evidence belongs to Historian policy, not to unbounded working memory.

## Jurisdiction and authority boundaries

Each institution may use competence and working memory inside its own jurisdiction. Review isolation applies to institutional members, Auditors, and Watchers. Historian is the long-term history authority for preservation and authenticated retrieval of preserved records. Retrieval does not move Historian into the approving or executing role.

FORGE may request governed retrieval for coordination. FORGE may not treat retrieved memory as fresh authorization.

## Security and privacy

ADR-020 classification, purpose limitation, and multi-principal isolation apply inside every class. Working memory is not a covert copy of another principal's data. Review views are minimized. Historian retrieval is logged as evidence access when the information is governance-relevant under ADR-017 and ADR-026.

Professional competence must not embed secrets, raw credentials, or another principal's case facts. ADR-009 keeps raw secrets out of general memory.

## Failure modes

- Case working memory survives the case and is retrieved as if it were competence. Required response: class violation; the material is not authority; containment follows ADR-039 if sensitive data leaked across cases.
- A reviewer is seeded with the advocate's hidden reasoning and then counted as independent. The vote or review fails the ADR-003 independence requirement.
- Historian retrieval is presented as a current approval. ADR-029 and ADR-005: replayed history is not current authorization.
- Expiration of working memory deletes evidence that ADR-017 requires to be preserved. Preservation and working-memory expiration are separate operations. Evidence required for accountability is committed to the history class before working-memory expiry.

## Invariants and tests

These invariants are proposed and have not been executed in this repository.

- Competence contains no live case payload and grants no jurisdiction.
- Working memory for case A is unreadable from case B without a separate governed access decision.
- Independent reviewers do not receive prohibited peer deliberation before their own evaluation.
- A Historian read cannot satisfy an authorization check.
- Tests to require before any later acceptance: cross-case retrieval; review seeded with another member's vote; authorization attempted from a retrieved checkpoint; competence store inspected for raw credentials and foreign case data.

## Compatibility with frozen baseline

This proposal specializes ADR-020, ADR-005, ADR-010, and ADR-003. It does not amend ADR-040. Retention periods, legal holds, and deletion procedure remain with ADR-020 and ADR-017. This ADR does not set those periods.

## Open questions

- Which case types require case-isolated reviewers as a mandatory control, and which may use ordinary independent members only.
- The default lifetime of case working memory when a case goes idle.
- Whether professional competence is per institution, per seat, or per model artifact, and how ADR-015 succession treats it.
- How this class model relates to opt-in conversation retention in ADR-045. Conversation buffers are not Historian history unless a preservation rule promotes them.
- The 2026-10-10 bundle asks to distinguish long-term professional skills from raw episodic memory. That distinction is the class split in items 1 and 2. What remains open is the earlier question of whether professional competence is kept per institution, per seat, or per model artifact.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

2026-10-10 revision, from the bundle draft numbered ADR-051: governed retrieval is logged, and case-isolated reviewers do not carry case memory into a new decision. Log fields were not invented. The competence-versus-episodic distinction was already this ADR's class split. No accepted ADR was edited.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The decision-queue source is a conversation candidate, not a ratification record
- This repository does not show an implementation or a passing test of these memory classes
