# ADR-047: Lifecycle Claim Separation for Upgrade, Rollback, and Release

**Status:** Proposed
**Date:** 2026-10-09
**Source decision queue:** DQ-021
**Related canonical ADRs:** ADR-001, ADR-005, ADR-006, ADR-008, ADR-010, ADR-015, ADR-016, ADR-038, ADR-039, ADR-040
**Constitutional approval:** Pending

## Context

ADR-006 separates Engineer preparation, Doctor health findings, Historian preservation of baselines and checkpoints, Auditor verification, Watcher observation, and FORGE execution of an authorized deployment. ADR-010 adds Teacher evaluation of learning without letting Teacher prove health, integrity, or permission alone. ADR-005 states that checkpoint creation does not authorize rollback and that Historian does not restore. ADR-038 governs production promotion. ADR-016 requires every materially applicable jurisdiction to participate. ADR-001 and ADR-040 keep execution in the governed FORGE process.

DQ-021 proposes that Teacher, Doctor, Engineer, and Historian sign different claims for agent upgrade, rollback, and release, that other applicable governance still applies, and that FORGE alone executes.

The four roles already exist. A rule that these four claims are distinct signature duties on upgrade, rollback, and release is not stated as a single ceremony in the baseline. No such ceremony is implemented in this repository.

## Problem

A single "approved to release" signature hides which question was answered. Historian can be pressed into approving the release because Historian stored the checkpoint. Teacher can be skipped on a change that alters behavior, or demanded on a change that has no learning content. Execution can drift toward whichever institution produced the artifact.

## Proposed decision

Upgrade, rollback, and release of an institutional agent or subsystem use separate signed claims. Each signer attests only the claim that matches its jurisdiction.

1. Engineer signs the technical claim: what artifact was built, its identity, and the technical contents of the proposed change. Engineer does not sign health, learning sufficiency, historical completeness, or execution authority. ADR-006 applies.
2. Doctor signs the health claim: ready or not ready relative to the applicable health baseline, before and after the change as ADR-006 requires. Doctor does not sign that the change is constitutionally permitted and does not execute the repair.
3. Teacher signs the learning claim when the change includes training, competence, curriculum, or behavioral instruction under ADR-010. The claim states whether the intended capability was learned within jurisdictional limits. Teacher does not sign health, deployment integrity, or jurisdiction expansion. A change with no learning content does not acquire a Teacher signature merely to fill a form. If it is disputed whether learning content exists, the change is treated as having learning content until that dispute is resolved.
4. Historian signs the evidence claim: the required baseline, artifact identity, and prior state were preserved and can be retrieved. That signature is registry and evidence validation. It is not approval of the upgrade, rollback, or release, and it is not authority to restore. ADR-005 applies.
5. Other applicable governance still applies. Auditor integrity verification, Watcher observation, Security, financial jurisdiction, human approval, quorum, and production promotion are required when ADR-004, ADR-016, ADR-032, and ADR-038 say they are required. These four claims do not replace them.
6. FORGE's execution process is the only component that performs the authorized upgrade, rollback, or release. None of the four signers executes that action because they signed.

Rollback remains a governed action. A Historian checkpoint is a candidate recovery point, not a command to roll back. Whole-system restoration stays on the ADR-005 and ADR-014 path.

## Alternatives considered

- Keep the ADR-006 role separation without a named four-claim ceremony. Acceptable if the owner rejects this ADR. It was not selected as the proposal because unsigned role boundaries are easy to collapse into one release approval.
- Require Teacher, Doctor, Engineer, and Historian on every change, including changes with no learning content. Rejected for Teacher, because a mandatory signature on unrelated changes pressures Teacher into a rubber stamp and expands Teacher's practical authority.
- Allow Historian's evidence signature to authorize rollback. Rejected because it conflicts with ADR-005.

## Jurisdiction and authority boundaries

Each claim stays inside the signer's existing jurisdiction. The ceremony does not create a four-person release institution and does not give the four signers collective authority to amend the Constitution. Constitutional changes follow ADR-008.

FORGE coordinates the ceremony and executes only a change that has the required claims plus every other applicable authorization. Missing claims fail closed. A missing claim is not an abstention that can be ignored. ADR-011 applies: silence is not approval.

Membership and activation of a new agent still follow ADR-015. A successful release claim set does not by itself appoint a new institutional seat.

## Security and privacy

Artifacts and claim signatures are bound to the same identity. Substituting the artifact after signature invalidates the claims. ADR-002 and ADR-006 apply.

Evidence claims include references sufficient for audit. They do not copy unrelated private case data into the release record. ADR-020 applies.

A compromised signer is handled under ADR-039 for that role. Compromise of Engineer does not authorize deployment. Compromise of Doctor invalidates health claims and does not remove the need for health verification. Compromise of Historian is handled with independent evidence, as ADR-039 already requires. Compromise of Teacher invalidates learning claims and does not redefine jurisdiction.

## Failure modes

- One combined signature is submitted as all four claims. Required response: reject the combined signature; the claims are distinct.
- Rollback executes because a checkpoint exists and Historian signed preservation. Required response: no execution until rollback authorization exists apart from the evidence claim.
- A behavior-changing prompt is labeled as having no learning content so Teacher is skipped. Required response: dispute resolves toward requiring the learning claim.
- FORGE executes a release while a required Auditor or jurisdictional approval is absent because the four claims are present. Required response: deny. The four claims are not a complete authorization set.
- Partial rollout fails. ADR-006 staged rollout and ADR-034 partial-failure rules apply. The failed stage does not count as a signed success.

## Invariants and tests

These invariants are proposed and have not been executed in this repository.

- Execution occurs only in the FORGE execution process, and only after the required distinct claims and all other applicable authorizations exist.
- Historian's signature cannot satisfy Doctor, Teacher, Engineer, Auditor, or human approval.
- Teacher's signature cannot change jurisdictional text.
- Artifact substitution after any claim signature invalidates the set.
- Tests to require before any later acceptance: release with a missing claim; rollback from a preserved checkpoint with no rollback authorization; learning content labeled as non-learning; combined multi-claim signature; execution attempted by Engineer after signing the technical claim.

## Compatibility with frozen baseline

This proposal restates ADR-006, ADR-010, and ADR-005 as distinct signed claims and adds an explicit Teacher claim only for changes that include learning content. It does not reduce Auditor, Watcher, jurisdictional, human, or production-promotion requirements. It does not amend ADR-040.

If the owner wants Historian to approve releases, that request conflicts with ADR-005 and is not part of this proposal.

## Open questions

- The exact signature format and whether ADR-043 Synchro, if accepted, is the carrier for these claims.
- Which consequence tiers require the full claim set, and which low-tier internal changes may use a thinner set under ADR-032 without bypassing enforcement.
- Who resolves a dispute that a change "has no learning content."
- How emergency patches under ADR-039 use this ceremony without dropping claims. ADR-039 already says expedited promotion remains governed. This ADR does not define a shorter path.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The decision-queue source is a conversation candidate, not a ratification record
- This repository does not show a release ceremony or a test of these claims
