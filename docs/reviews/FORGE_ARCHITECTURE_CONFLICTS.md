# FORGE Architecture Conflicts

**Date:** 2026-10-09
**Repository:** https://github.com/ForgeArchitect/FORGE-Architecture
**Baseline:** ADR-001 through ADR-040, all Accepted, frozen as the v1.0 baseline by ADR-040. Commit `3229df7bea351517921a6251f15a0abb049c4019`.

The decision queue is a set of conversation candidates. It is not a constitutional amendment. Where a candidate cannot be reconciled with an Accepted ADR, this file records the conflict and no draft pretends to resolve it. Independent candidates were still drafted. ADR-029 was not edited.

## 1. ADR-029 peer communication versus a total ban on lateral conversation

**Queue item.** DQ-004.

**Accepted rule.** ADR-029, "Peer Communication," says institutions may communicate directly when constitutionally permitted, and that direct communication must not become direct unauthorized execution. ADR-029, "Query Messages" and "Response Messages," allows one institution to ask another for information inside the responder's jurisdiction. ADR-029, "Internal Institutional Messaging," allows internal communication that preserves member identity and independent voting. ADR-040 restates the bus as transport that does not govern, and restates that communication does not manufacture authority.

**Candidate rule.** No direct internal access and no lateral conversations. All cross-institution contact is an authenticated scoped package through Dispatcher and Gatekeepers.

**Reconciliation that does not amend ADR-029.**

- A peer-to-peer or mesh implementation is transport. ADR-029 already says the architecture does not mandate a messaging technology, and that transports must not invent a second authority semantics.
- Transport is not access to another institution's internal memory, tools, credentials, or execution surface. ADR-020 and ADR-029 network segmentation already limit that access.
- Consequential requests still enter through Dispatcher. Gatekeeper still judges admissibility. A delivered package is not an approval and not an execution command.
- Side doors that execute outside the bus remain forbidden.

**Unresolved remainder.** A prohibition on all lateral queries and all constitutionally permitted peer messages is an amendment of ADR-029, not a reading of it. No proposed ADR makes that amendment. ADR-008 would require a separate amendment path and human approval before such a prohibition could take effect.

**Drafting decision.** Stopped for the unresolved ban. The covered transport reading is recorded in the coverage matrix. Work on other queue items continued.

## 2. Historian authority

Several candidates place Historian on a critical path. The accepted limit is ADR-005 and the ADR-040 restatement: Historian preserves evidence, checkpoints, membership history, and recovery records, and does not restore or execute. ADR-015 gives Historian custody of membership history and gives appointment authority to the governed membership process. ADR-029 says Historian does not create current authorization by replaying old records. ADR-039 uses Historian continuity as a recovery precondition, not as a grant of incident command.

| Candidate phrase | Reading used | Reading rejected |
| --- | --- | --- |
| DQ-008, Historian registry verifies existence | Evidence and registry validation of membership records | Historian approves creation or activates an institution |
| DQ-009, Historian attestation on a Synchro | Attestation of issuance lineage and registry evidence | Historian approves or executes the underlying action |
| DQ-010, Historian preserves non-redeemable evidence | Already required by ADR-005, ADR-017, and ADR-029 | Preservation redeems or replays the evidence into authority |
| DQ-012, Historian evidence during reinstatement | Supply preserved evidence for the decision | Historian signs the system back into service |
| DQ-015, Historian preserves the closure report | Append the report to history | Filing the report is closure authority |
| DQ-021, Historian signs a lifecycle claim | Evidence claim that the baseline and artifact were preserved | The signature authorizes upgrade, rollback, or release |

ADR-043 and ADR-047 use only the evidence reading. If the owner wants Historian to approve execution, creation, closure, or release, that choice conflicts with ADR-005. Those drafts would have to stop, and an ADR-008 amendment would be required. That choice is not proposed.

## 3. Exclusive personal FORGE versus federation

**Queue item.** DQ-023.

**Accepted rule.** ADR-028 allows independent FORGE deployments for different humans, organizations, businesses, devices, sites, security domains, and specialized purposes. Each deployment is its own trust domain unless federation is explicitly governed. ADR-013 recognizes an owner and Root Human authority. ADR-020 isolates principals. ADR-010 prevents learning from silently moving jurisdiction.

**Compatible subset.** A person's FORGE can be an independently owned trust domain. Its memory and skills do not automatically transfer to another FORGE. Federation does not merge constitutions.

**Conflict.** "One independently owned FORGE per person" as an exclusive rule would forbid the organizational, multi-site, and multi-purpose deployments ADR-028 already accepts. The queue also frames this as a personal-assistant vision. This repository has no personal assistant implementation.

**Drafting decision.** Stopped. No ADR proposes to repeal or narrow ADR-028. A non-exclusive personal deployment profile can be written later if the owner asks for it and keeps organizational federation intact.

## 4. Competing fault and health vocabularies

**Queue item.** DQ-014, with DQ-013's "safe mode."

**Accepted vocabularies.**

- ADR-036 governance health: HEALTHY, DEGRADED, IMPAIRED, CRITICAL, RECOVERY_REQUIRED, UNKNOWN.
- ADR-039 incidents: SUSPECTED, CONFIRMED, CONTAINING, CONTAINED, INVESTIGATING, REMEDIATING, RECOVERING, MONITORING, CLOSED, RECOVERY_REQUIRED.
- ADR-011: degraded operation as reduced, pre-defined authority.

**Candidate vocabulary.** Pending, confirmed, restricted, safe mode.

**Nature of the conflict.** This is a terminology collision, not yet a contradiction of authority. It becomes a constitutional conflict if the new names are adopted as a second state machine with different powers, especially if safe mode expands authority or if debounce delays a human-life HARD STOP required by ADR-007.

**Drafting decision.** No ADR adds the new names. An implementation specification may map them onto the accepted states. Numeric thresholds are not in the baseline and were not invented. See human decision HD-014.

## 5. Single ingress versus specialized dispatchers

**Queue item.** DQ-003.

**Accepted rule.** ADR-002 and ADR-040 define Dispatcher as the controlled routing authority. The whitepaper Appendix A records a single controlled ingress and says privileged execution cannot use legacy side routes.

**Candidate addition.** Specialized dispatchers and parallel tasks.

**Nature of the conflict.** Specialization is compatible only when those dispatchers are workers of the one ingress authority and cannot authorize. It conflicts if each specialty is its own constitutional ingress or its own Gatekeeper.

**Drafting decision.** No ADR. Recorded as an implementation constraint. See human decision HD-003.

## 6. Director role versus independent institutional decision

**Queue item.** DQ-001, and the director-routing phrase in DQ-005.

**Accepted rule.** ADR-003: no individual member is the institution; members evaluate independently where required; quorum is constitutional. ADR-001: execution is separated from institutional decision.

**Risk.** A director who routes, witnesses, and decides is a single internal authority.

**Treatment.** This one was drafted, not stopped, because a compatible rule exists: ADR-041 proposes director, departments, and specialists as administration, with no execution authority and no power to replace quorum or Watchers. The incompatible rule, a binding director, is an open question. If the owner wants that incompatible rule, ADR-041 cannot be accepted as written and the conflict falls under ADR-008.

## 7. Four signatures versus complete authorization

**Queue item.** DQ-021.

**Risk.** Readers can treat Teacher, Doctor, Engineer, and Historian as a sufficient release board, omitting Auditor, applicable jurisdictions, human approval, and production promotion.

**Treatment.** ADR-047 states that the four claims are distinct and incomplete. Historian's claim is evidence only, which keeps item 2 above intact. The draft does not reduce ADR-016 or ADR-038.

## 8. Documentary lag that is not a constitutional conflict

These records are older or narrower than ADR-040. They were not edited. Accepted ADRs govern.

| Record | Lag |
| --- | --- |
| `FORGE_WHITEPAPER.md` section 17 | Lists resource governance, human-authority boundaries, Teacher governance, catastrophic failure, quorum rules, conflicts of interest, and red-team testing as open. ADR-012, ADR-013, ADR-010, ADR-014, ADR-011, ADR-022, and ADR-037 later accepted those topics. |
| `FORGE_WHITEPAPER.md` Appendix B | Calls the blueprint a design record as of October 6, 2026, not a certification or a production system. That limitation is still accurate. |
| `CHANGELOG.md` status note | Describes version 0.2 and says later governance was still under development. ADR-012 through ADR-040 are the later development. |

## 9. Implementation claims

No queue item is an implemented fact in this repository. There is no application code, no test run, and no deployment. Proposed ADRs that describe local-first operation, recording, Synchro, tool manifests, or internal directors describe design. They do not describe a running FORGE.

ADR-029's historical text was left unchanged on purpose. Reconciliation for the mesh-as-transport reading is in section 1 of this file and in the coverage matrix. It is not a silent rewrite.
