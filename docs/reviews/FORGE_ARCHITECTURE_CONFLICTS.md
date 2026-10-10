# FORGE Architecture Conflicts

**Date:** 2026-10-09 audit. Bundle conflicts added 2026-10-10. Sections 1 through 9 are unchanged history.
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

## 10. Bundle ADR-040 duplicates the Accepted baseline

The bundle's ADR-040 would restate the v1.0 freeze as a proposed record and says it supersedes nothing automatically. Accepted ADR-040 already freezes ADR-001 through ADR-040. Writing the bundle file at that path would overwrite the Accepted record.

**Drafting decision.** The bundle file was not added. ADR-040 on `main` and on this branch remains the Accepted text from commit `3229df7bea351517921a6251f15a0abb049c4019`.

## 11. Bundle ADR-043 reopens the ADR-029 peer-message conflict

**Bundle rule.** Cross-institution requests and results travel as typed authenticated packages through Dispatcher and Gatekeepers. The draft also forbids unrestricted direct memory, filesystem, sandbox, credential, or RPC access, and it asks to reconcile peer-mesh language so that transport is not internal access.

**Accepted rule.** Section 1 of this file. ADR-029 permits constitutionally allowed peer communication and jurisdictional queries. Those messages still do not execute. ADR-020 forbids the unrestricted internal access. The whitepaper Appendix A locks a single controlled ingress.

**Reconciliation that does not amend ADR-029.** Unrestricted internal access stays forbidden. Consequential requests still enter through Dispatcher. Gatekeeper still judges admissibility. Specialized dispatchers, if any, are workers of that one ingress and do not authorize. That is the DQ-003 constraint in section 5.

**Unresolved remainder.** A requirement that every result and every lateral query also pass Dispatcher and Gatekeeper would amend the peer-communication and query sections of ADR-029. That amendment was not drafted. See HD-004 and HD-B043.

## 12. Bundle ADR-042 and the Librarian name versus ADR-015

**Bundle rule.** An Information and Knowledge Management institution maintains registry evidence through Historian. FORGE proposes institutions, engineering designs, other jurisdictions attest, and FORGE executes authorized activation. A later bundle draft, numbered ADR-052, has Librarian and Historian supply derived knowledge.

**Accepted rule.** ADR-015 governs membership creation and keeps activation distinct from provisioning. Engineer does not appoint. Historian preserves membership history and does not appoint. ADR-005 limits Historian to evidence. Section 2 of this file already rejects Historian as the approver of creation.

**Treatment.** Proposed ADR-042 item 9, added in this pass, refuses both the registry-holder institution and Librarian. The compatible reading, Historian as evidence custodian, stays covered. If the owner wants Historian or a new knowledge institution to approve existence, that choice conflicts with ADR-015 and ADR-005 and requires ADR-008. It was not drafted. See HD-008 and HD-B042.

## 13. Bundle ADR-047 dormant replacement versus ADR-015

**Bundle rule.** Prepare a dormant clean replacement and do not activate it until the compromise path is addressed and a clean baseline is verified. Quarantine scope expands if a shared trust boundary cannot be established.

**Accepted rule.** ADR-015 quarantine: a quarantined member cannot restore itself, and re-entry is governed. ADR-015 forbids vote manufacturing. ADR-015 activation is a distinct transition. ADR-039 sets recovery preconditions and forbids assuming the smallest blast radius when it is unknown.

**Conflict if misread.** Activating the replacement without the membership process, or activating it to replace a dissenting quorum, amends ADR-015. An automatic expansion rule with an invented scope list would also be new policy.

**Treatment.** No new ADR. The pattern remains an implementation specification. The widened set was not invented. See HD-011 and HD-B047.

## 14. Bundle ADR-048 reinstatement versus ADR-005

**Bundle rule.** Historian attests recovery evidence, and FORGE alone executes authorized restoration. Health, Security, Engineering, and Auditor each verify their own question. Critical cases require multiple independent reviews.

**Accepted rule.** ADR-005: Historian does not restore. ADR-014 and ADR-039 already split recovery duties. ADR-004 supplies independent review. ADR-035 and ADR-014 cover fresh keys. "Multiple" is not quantified in the draft.

**Treatment.** No new ADR. The checklist remains DQ-012. Historian's attestation is evidence only. No review count was invented. See HD-012 and HD-B048.

## 15. Bundle ADR-049 fault vocabulary versus ADR-036, ADR-039, and ADR-011

The bundle repeats section 4. Pending, confirmed, restricted, and safe mode are not adopted as constitutional states. Safe mode, if the owner later names it, has to be an ADR-011 degraded mode. Threshold numbers are not in the draft and were not invented. Immediate containment of a critical active threat fits ADR-039. A debounce that delayed an ADR-007 HARD STOP would conflict with ADR-007. The bundle draft does not propose that debounce. See HD-013, HD-014, and HD-B049.

## 16. Bundle ADR-054 vault versus ADR-020 and ADR-028

**Bundle rule.** Automatically replicate each institution's checkpoints to an owner-approved encrypted recovery vault. Restore only the affected trust domain when isolation is verified. Keep cross-institution compatible recovery manifests. A valid backup hash does not prove the checkpoint is uncompromised.

**Accepted constraints.** ADR-020: replication is exposure and should be intentional and attributable. Backups remain governed. ADR-028: deployments do not share authority unless federation is governed. ADR-005 and ADR-014: a checkpoint's existence or label is not sufficient trust, and Historian does not restore. ADR-005 also prefers the smallest safe scope and binds authorization to that scope.

**Nature of the conflict.** Ungoverned automatic copying would contradict ADR-020. A vault that restores one deployment with another's authority would contradict ADR-028. A hash-only trust decision would contradict ADR-005 and ADR-014. A rule that forbade whole-system recovery would contradict ADR-005 and ADR-014.

**Treatment.** This one was drafted, because a compatible rule exists. Proposed ADR-049 allows replication only inside an owner-approved vault policy, partitions checkpoints by institution, refuses cross-deployment authority, refuses hash-only trust, and leaves whole-system recovery in place when isolation is not verified. The manifest schema, algorithm, and positive uncompromised-checkpoint test are open. If the owner wants ungoverned replication or cross-deployment restore, ADR-049 cannot be accepted as written.

## 17. Bundle ADR-055 cloud recovery versus ADR-028 and local authority

**Bundle rule.** Replicate security events to an append-only vault with credentials independent of the local host. Operating-system or shared-trust-root compromise triggers broader containment. Cloud recovery is preprovisioned and restricted, and it cannot accept instructions or secrets from the compromised host.

**Accepted constraints.** ADR-028: a remote deployment does not inherit local authority. ADR-001, ADR-033, and ADR-040: consequential execution stays in the governed FORGE path. ADR-021: untrusted content is not instruction. ADR-023: split-brain reduces autonomy and does not create parallel governments. ADR-039: do not assume the smallest blast radius. ADR-014: compromised components do not clear themselves.

**Nature of the conflict.** A cloud recovery path that takes commands or secrets from the compromised host, or that executes as the local FORGE because it holds a copy, contradicts those rules. Treating operating-system compromise as a single institution's quarantine contradicts ADR-039 when the blast radius is unknown.

**Treatment.** Proposed ADR-050 states the host-independent replica, the broader-containment trigger, and the refusal of compromised-host instructions and secrets. It does not provision a cloud provider, does not list the widened containment set, and does not invent the independent root of trust, the split-brain procedure, or the clean-restore checks the draft says are still required. Proposed ADR-048, unchanged in this pass, still forbids direct cloud execution against the local deployment if that ADR is accepted.

## 18. Bundle ADR-056 domains versus single ingress and ADR-028

**Bundle rule.** Separate FORGE core, desktop operating system, untrusted research, and a security gateway. The network gateway enforces traffic. Gatekeepers enforce constitutional authority. Preference is a bare-metal hypervisor or dedicated hardware. Shared hypervisor and management plane remain trust dependencies. Isolation is not perfect.

**Accepted constraints.** ADR-002, ADR-040, and the whitepaper Appendix A: one controlled ingress. Dispatcher routes and does not authorize. Gatekeeper judges admissibility and does not execute. ADR-028: another FORGE is another trust domain unless federation is governed. ADR-015: a name is not an institution. ADR-038: environment promotion is its own governed boundary.

**Nature of the conflict.** A gateway that authorizes because it passed traffic would be a second ingress and a second Gatekeeper. Four domains operated as four FORGE deployments would be federation without an ADR-028 agreement. Domain placement is not production promotion.

**Treatment.** Proposed ADR-051 keeps traffic enforcement and constitutional admissibility apart, preserves the single ingress, and keeps the domains inside one deployment. It creates no institution and no federation. It chooses neither hypervisor nor dedicated hardware. Rejecting it leaves host layout open, including under proposed ADR-048.

## 19. What the bundle did not reopen

The bundle does not repeat DQ-023's exclusive one-FORGE-per-person rule. Section 3 stands. ADR-028 is not narrowed.

The bundle does not supply the concrete signer matrix DQ-007 left unapproved. No matrix was added to proposed ADR-047 or written as a new ADR.

Closed pull request #2's department and specialist layer numbers are not part of proposed ADR-041. That pull request was not merged and is not a constitutional record.
