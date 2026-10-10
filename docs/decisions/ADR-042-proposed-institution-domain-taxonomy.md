# ADR-042: Proposed Institution Domain Taxonomy

**Status:** Proposed
**Date:** 2026-10-09
**Revision:** 2026-10-10 bundle reconciliation. The exact change is in the approval record.
**Source decision queue:** DQ-002
**Related canonical ADRs:** ADR-001, ADR-003, ADR-005, ADR-015, ADR-016, ADR-040
**Constitutional approval:** Pending

## Context

Accepted records name institutions by role. Examples that appear throughout ADR-001 through ADR-040 include Banker, Engineer, Doctor, Teacher, Security, Historian, Auditor, Watchers, Dispatcher, and Gatekeeper. ADR-016 assigns authority by constitutionally defined jurisdiction. ADR-040 freezes that model as the v1.0 baseline. Those records do not adopt a closed seven-domain taxonomy.

DQ-002 proposes these domain labels: Engineering and Technology; Health; Financial Services; Information and Knowledge Management; Education and Learning; Security; Coordination and Dispatch. The queue states that jurisdiction assignments remain proposed.

## Problem

Implementers can treat a new label as a new institution, or treat Coordination and Dispatch as an authorizer because it routes. They can also treat Information and Knowledge Management as a rename of Historian that adds approval power. None of those consequences is authorized by the baseline.

## Proposed decision

The seven labels are a proposed, non-exhaustive vocabulary for grouping discussion of institutional work. This ADR does not assign constitutional jurisdiction, create an institution, rename an institution, or retire a name already used in ADR-001 through ADR-040.

Until a later human-approved record says otherwise:

1. Engineer remains the technical-change institution under ADR-006. "Engineering and Technology" is a label, not a second institution.
2. Doctor remains the health institution under ADR-006. "Health" is a label.
3. Banker remains the financial institution named in the baseline. "Financial Services" is a label.
4. Teacher remains the learning institution under ADR-010. "Education and Learning" is a label.
5. Security remains the security institution named in the baseline.
6. Dispatcher remains routing ingress under ADR-002 and ADR-040. "Coordination and Dispatch" does not gain authority by routing. Gatekeeper remains admissibility evaluation and does not execute.
7. Historian remains institutional memory under ADR-005. "Information and Knowledge Management" does not rename Historian and does not give Historian execution authority or universal approval authority. A distinct knowledge institution, if ever created, requires ADR-015 membership governance and a separate approved decision.
8. Auditor and Watcher functions remain independent under ADR-004. They are not absorbed into Security or into Information and Knowledge Management by this taxonomy.
9. A 2026-10-10 bundle draft would have an Information and Knowledge Management institution maintain the institutional registry through Historian, and would have a Librarian supply derived knowledge to learners. Neither name becomes an institution here. Registry custody stays with Historian under ADR-015 and ADR-005. That custody is evidence and registry validation. It is not approval of institutional existence and it is not activation. A Librarian institution, or an Information and Knowledge Management institution that holds registry authority, would be a new institution under item 7 and is not created by this record.

Jurisdiction assignments for these labels stay unapproved. ADR-016 remains the rule for which institutions must participate in a consequential action.

## Alternatives considered

- Adopt the seven labels as the closed constitutional institution set and map each label to exclusive jurisdiction now. Rejected because DQ-002 says the assignments are still proposed, and because that adoption would collide with Auditor, Watcher, Gatekeeper, and Historian roles that the labels do not name.
- Refuse to record the vocabulary at all. Rejected as the proposed decision because unlabeled reuse of these phrases in later design work is likely to be read as if the assignments were already constitutional.

## Jurisdiction and authority boundaries

ADR-016 controls jurisdiction. This taxonomy does not.

Creating an institution under any label requires the membership, activation, health, audit, and human-approval rules in ADR-015. FORGE may propose. Engineer may prepare software. Activation is a separate governed transition. Historian may preserve and validate registry evidence. Historian does not appoint the institution.

## Security and privacy

A domain label is not a data-access grant. ADR-020 still limits information to jurisdictional need. A Financial Services label does not entitle that work to health information. A Security label does not entitle Security to universal authority during incidents. ADR-039 states that limit for Security specifically.

## Failure modes

- A new process starts under one of the seven names and claims institutional authority. ADR-015: a name is not membership.
- Dispatch routing is recorded as approval. ADR-002 and ADR-040: routing is not authorization.
- Knowledge-management work rewrites historical records or restores a checkpoint. ADR-005: Historian preserves evidence and does not restore by itself.
- The taxonomy is used to skip Auditor or Watcher review because those names are absent from the seven labels. ADR-004 still applies.

## Invariants and tests

These invariants are proposed and have not been executed in this repository.

- No domain label is sufficient evidence of institutional identity.
- Routing under Coordination and Dispatch cannot satisfy an authorization requirement.
- Information and Knowledge Management cannot approve execution, restore state, or certify quorum.
- Tests to require before any later acceptance: spawn a process named for each label and confirm it has no seat; attempt to treat a Dispatcher route as Banker approval; attempt to treat a Historian registry check as activation.

## Compatibility with frozen baseline

This proposal does not amend ADR-040. Existing institutional names and jurisdictions remain as written in the accepted ADRs. Any future assignment of exclusive jurisdiction to these labels is a further decision and, where it changes constitutional authority, follows ADR-008, including human approval.

## Open questions

- Whether Information and Knowledge Management should ever be a separate institution from Historian, Teacher, and Auditor.
- Whether Coordination and Dispatch should remain a function of Dispatcher and Gatekeeper rather than an institution with members and quorum.
- Which human-approved record, if any, will assign jurisdictions. This ADR does not do that.
- How bicameral amendment bodies in ADR-008 relate to the seven labels. They are not mapped here.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

2026-10-10 revision: item 9 records that the bundle's registry-holder reading of Information and Knowledge Management, and its Librarian supplier, are not adopted. Jurisdiction assignments remain unapproved. No accepted ADR was edited.

- Owner approval: Pending
- Jurisdiction assignments: still unapproved
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The decision-queue source is a conversation candidate, not a ratification record
- This repository does not show an implementation or a passing test of this decision
