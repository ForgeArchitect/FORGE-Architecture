# FORGE ADR Coverage Matrix

**Date:** 2026-10-09
**Repository:** https://github.com/ForgeArchitect/FORGE-Architecture
**Baseline commit audited:** `3229df7bea351517921a6251f15a0abb049c4019` (`main`, subject `FORGE v1.0 constitutional architecture baseline`)
**Queue source:** conversation-derived candidates DQ-001 through DQ-024, packaged as `FORGE_GROK_ADR_HANDOFF`. The handoff manifest states `constitutional_approval_granted: false`.
**Precedence:** accepted records in this repository override the queue. Conversational agreement is not constitutional ratification.

## Audit

| Check | Result |
| --- | --- |
| Canonical ADR numbers present | ADR-001 through ADR-040. All forty files exist under `docs/decisions/`. |
| Highest used number | ADR-040. ADR-041 and above were unused at audit time. |
| Status of ADR-001–040 | Each file begins with `Status: Accepted` and date 2026-10-06. |
| Later ADRs | None. |
| ADR-029 | Present, Accepted, not modified by this work. Filename: `docs/decisions/ADR-029-constitutional-communications-bus-and-authenticated-inter-institution-messaging.md`. |
| Constitution | No separate constitution file. The constitutional record is ADR-001–040, with ADR-040 freezing the v1.0 baseline, plus `FORGE_WHITEPAPER.md` as an earlier blueprint. |
| Whitepaper | `FORGE_WHITEPAPER.md`, blueprint v2, architecture record October 6, 2026. Section 17 still lists topics that later accepted ADRs closed. Where they differ, the ADRs prevail. The whitepaper was not edited. |
| Changelog | `CHANGELOG.md` stops at architecture version 0.2 and says later topics were still under development. ADR-012 through ADR-040 supersede that status note. The changelog was not edited. |
| Branches | Only `main` existed at audit time. No other local or remote branches. |
| Pull requests | None. `gh pr list --state all` returned no pull requests. |
| Implementation evidence | The repository is documentation. There is no runtime, tool registry, test suite, or Codex implementation record. No queue item is marked implemented or tested. |

Filename irregularities are preserved. They are the same documents as the numbered decisions:

- `ADR-003: Institutional Redundancy and Quorum Governance`
- `ADR-004 specifically about Independent Watchers and Audit Attestations`
- `ADR-005: Historian, Checkpoints, and Governed Recovery`
- `ADR-006: Engineer, Doctor, and Governed Updates`
- `ADR-007: Human-Life Emergency Hard Stop and Governed Resume.`

## Classification rules

- **Covered.** The constitutional decision is already in an Accepted ADR. The queue does not add a material rule.
- **Implementation specification.** The principle is already decided. The queue adds a procedure, checklist, vocabulary, or internal design that should be specified under those ADRs. It is not a new constitutional ADR.
- **New proposed ADR.** The queue adds a material decision that is absent from ADR-001–040 and can be drafted without contradicting the baseline. New records are `Status: Proposed` and `Constitutional approval: Pending`.
- **Deferred.** Drafting was stopped because the item conflicts with the baseline, or because it is an explicit future roadmap rather than a present architectural decision.

Human approval is required before any proposed ADR can become Accepted, and before any implementation specification can be treated as binding policy. Items marked covered do not need a new approval to remain in force. They still need a human decision if the owner wants the stricter reading that the matrix rejects.

## Summary

| ID | Classification | Canonical anchors | Proposed record | Human approval |
| --- | --- | --- | --- | --- |
| DQ-001 | New proposed ADR | ADR-001, ADR-003, ADR-015, ADR-027 | ADR-041 | Yes |
| DQ-002 | New proposed ADR | ADR-015, ADR-016, ADR-040 | ADR-042 | Yes. Jurisdiction assignments stay open. |
| DQ-003 | Implementation specification | ADR-002, ADR-016, ADR-029, ADR-033, ADR-040 | None | Yes, before any multi-dispatcher design is binding. |
| DQ-004 | Covered, with an unresolved stricter reading | ADR-029, ADR-040 | None. ADR-029 was not rewritten. | Yes, only if ADR-029 is to be amended. |
| DQ-005 | Covered | ADR-002, ADR-004, ADR-017, ADR-020, ADR-026 | None | Yes, only if a director or a new witness role is added. |
| DQ-006 | Implementation specification | ADR-002, ADR-020, ADR-021, ADR-030, ADR-031 | None | Yes, before a question-package protocol is binding. |
| DQ-007 | Implementation specification | ADR-003, ADR-016, ADR-032 | None | Yes. The concrete matrix is unapproved. |
| DQ-008 | Covered | ADR-005, ADR-006, ADR-015 | None | No for the evidence-only Historian reading. |
| DQ-009 | New proposed ADR | ADR-009, ADR-018, ADR-004, ADR-005 | ADR-043 | Yes |
| DQ-010 | Covered | ADR-017, ADR-018, ADR-029 | Applied as a constraint inside ADR-043, not as a new rule | No for replay law. |
| DQ-011 | Implementation specification | ADR-015, ADR-039 | None | Yes, before a sealed-replacement design is binding. |
| DQ-012 | Implementation specification | ADR-005, ADR-006, ADR-014, ADR-039 | None | Yes, before the checklist is binding policy. |
| DQ-013 | Implementation specification | ADR-007, ADR-011, ADR-013, ADR-036, ADR-039 | None | Yes, before safe-mode permissions are named. |
| DQ-014 | Implementation specification | ADR-007, ADR-011, ADR-031, ADR-036, ADR-039 | None | Yes, before a fault vocabulary is binding. |
| DQ-015 | Covered | ADR-004, ADR-005, ADR-017, ADR-039 | None | No for the closure principle. |
| DQ-016 | Covered | ADR-019, ADR-020, ADR-032, ADR-033, ADR-035 | None | No. A bypass would be a rejection of the baseline. |
| DQ-017 | New proposed ADR | ADR-003, ADR-005, ADR-010, ADR-020 | ADR-044 | Yes |
| DQ-018 | New proposed ADR | ADR-013, ADR-017, ADR-020, ADR-021 | ADR-045 | Yes. Not implemented. |
| DQ-019 | Implementation specification | ADR-010, ADR-015, ADR-029 | None | Yes, before per-agent teachers are mandatory. |
| DQ-020 | New proposed ADR | ADR-006, ADR-009, ADR-019, ADR-033 | ADR-046 | Yes |
| DQ-021 | New proposed ADR | ADR-005, ADR-006, ADR-010, ADR-016 | ADR-047 | Yes |
| DQ-022 | New proposed ADR | ADR-019, ADR-027, ADR-028, ADR-033, ADR-038 | ADR-048 | Yes. Not implemented. |
| DQ-023 | Deferred | ADR-010, ADR-013, ADR-020, ADR-028 | None | Yes. Exclusive reading conflicts with ADR-028. |
| DQ-024 | Deferred | ADR-019, ADR-020, ADR-040 | None | Yes, before any multimodal capability is in scope. |

## Item notes

### DQ-001 — Multi-agent institutions

**Queue substance.** Each institution has a director, departments, and specialists, with scoped internal delegation and no independent execution authority.

**Source status.** Conversation candidate. No approval record in git history or pull requests.

**Where the baseline already speaks.** ADR-003 distinguishes institution from member and requires independent evaluation and quorum. ADR-015 puts authority in authenticated seats. ADR-027 attenuates delegation and says internal sub-agents are workers unless admitted through governance. ADR-001 and ADR-040 keep consequential execution out of a single authority-bearing component. ADR-002 places consequential execution in the FORGE execution process.

**What is new.** Director, department, and specialist are not defined in the accepted ADRs. That internal shape is material because a director can be read as the institution.

**Contradictions.** A director who binds the institution's vote or executes work contradicts ADR-003 and ADR-001. ADR-041 proposes the shape only as administration, with no execution authority and no vote manufacture.

**Classification.** New proposed ADR-041.

**Human approval.** Required. Pending.

### DQ-002 — Institution taxonomy

**Queue substance.** Seven domain labels. Jurisdiction assignments remain proposed.

**Source status.** Conversation candidate. Assignments are explicitly unapproved in the queue itself.

**Where the baseline already speaks.** ADR-016 defines jurisdiction. ADR-040 and the earlier ADRs use role names: Banker, Engineer, Doctor, Teacher, Security, Historian, Auditor, Watchers, Dispatcher, Gatekeeper. Those names are examples of a constitutional set, not the seven labels.

**What is new.** The seven-label vocabulary, and the need to stop it from becoming a silent institution list.

**Contradictions.** Mapping Coordination and Dispatch onto an authorizer would contradict ADR-002. Mapping Information and Knowledge Management onto Historian-as-approver would contradict ADR-005. ADR-042 records the labels and does not assign jurisdiction.

**Classification.** New proposed ADR-042.

**Human approval.** Required before any label becomes a jurisdiction or a new institution. This proposal does not grant that approval.

### DQ-003 — Dispatch institution

**Queue substance.** Specialized dispatchers, registry-based routing, Gatekeeper mediation, parallel tasks, and no authorization via routing.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-002 and ADR-040: Dispatcher is controlled ingress and routing and does not authorize. Gatekeeper decides admissibility and does not execute. ADR-016: Dispatcher may identify apparent jurisdictions and may not redefine them. ADR-029: Dispatcher routes consequential requests and does not determine institutional outcomes. ADR-033: Dispatcher is not the enforcement point. The whitepaper Appendix A locks a single controlled ingress.

**What is not a new constitutional rule.** Registry-based routing, parallel tasks, and specialized routing workers are implementation detail under that single ingress.

**Contradictions.** Specialized dispatchers that become additional ingress authorities, or that approve because they routed, contradict ADR-002 and the whitepaper lock. No ADR was drafted, because drafting one would either duplicate ADR-002 or weaken single ingress.

**Classification.** Implementation specification under ADR-002, ADR-016, ADR-029, ADR-033, and ADR-040.

**Human approval.** Required before a multi-dispatcher registry is treated as binding design. The specification must keep one ingress authority.

### DQ-004 — Cross-institution communication

**Queue substance.** No direct internal access or lateral conversations. Authenticated, scoped packages through Dispatcher and Gatekeepers. Reconcile prior peer-to-peer descriptions.

**Source status.** Conversation candidate. No separate peer-to-peer specification file exists in the repository. The canonical communications decision is ADR-029.

**Where the baseline already speaks.** ADR-029 and ADR-040: the bus transports messages and does not govern; a message does not create authority by delivery; undocumented privileged side doors are forbidden; different transports must not change authority semantics; consequential requests enter through Dispatcher; Gatekeeper evaluates admissibility. ADR-029 also permits internal institutional messaging under that institution's governance, query and response messages between institutions, and direct peer communication when constitutionally permitted, provided it does not become unauthorized execution. ADR-020 limits internal access to data.

**Reconciliation, without editing ADR-029.** Any peer-to-peer or mesh path is transport. It is not unrestricted institution-to-institution access to internals, and it is not an execution path. Mediated consequential packages still go through Dispatcher and Gatekeeper. Direct peer messages that ADR-029 permits remain subject to least authority, typed schemas, and recipient validation. They still do not execute.

**Contradiction.** A total ban on lateral conversations and queries is stricter than ADR-029's peer-communication and query sections. That ban was not drafted. ADR-029 stays Accepted as written. See `FORGE_ARCHITECTURE_CONFLICTS.md`.

**Classification.** Covered for transport-only mesh, authenticated scoped messaging, and mediated consequential ingress. The absolute ban is an unresolved amendment question, not a second ADR.

**Human approval.** Required only if the owner wants to amend ADR-029 through ADR-008. No such amendment is proposed here.

### DQ-005 — Request witnessing

**Queue substance.** Immutable request hashes, relevant independent witnesses, director internal routing, and privacy-limited visibility.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-002 binds consequential requests to authenticated identity and checks that identity at later stages. ADR-017 requires cryptographic digests, hashes, and chain of custody, and treats replay of an observation as a distinct action. ADR-004 defines independent Watchers and Auditors. ADR-026 records lifecycle events, including clarification. ADR-020 limits who can see information. ADR-029 requires detectable message integrity.

**What was not adopted.** "Director internal routing" is not a witness function and is not a way to alter request identity. ADR-041, if accepted, still does not let a director replace Watchers. A witness role distinct from Watchers and Auditors is not created.

**Classification.** Covered.

**Human approval.** Not required to keep the baseline. Required before adding a director routing path or a new witness office.

### DQ-006 — User clarification

**Queue substance.** Institutions return question packages to FORGE. FORGE consolidates them, checks authorized historical context, asks the user, and routes answers.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-031: FORGE requests clarification when a human can resolve material ambiguity, and does not ask the human to resolve every trivial ambiguity. ADR-030 records clarification as an intent-preservation outcome. ADR-021 requires clarification for consequential ambiguity. ADR-026 allows a lifecycle result of clarification required. ADR-020 and ADR-005 govern historical context. ADR-002 invalidates authorization when the request materially changes. ADR-029 forbids FORGE from forging an institutional decision or synthesizing consensus.

**What remains unspecified.** The package format, consolidation rules, and routing of answers. Consolidation that changes an institution's question into a different question would be a decision proxy.

**Classification.** Implementation specification under ADR-030, ADR-031, ADR-021, ADR-020, and ADR-002.

**Human approval.** Required before that protocol is binding.

### DQ-007 — Dynamic approval matrix

**Queue substance.** Only jurisdictionally relevant institutions approve. Risk and operation type determine required signers. The formal authority policy is unapproved.

**Source status.** Conversation candidate. The queue itself says the formal policy is unapproved.

**Where the baseline already speaks.** ADR-016 requires applicable jurisdictions and forbids routing around the institution that actually has jurisdiction. ADR-032 scales governance by consequence tier, including streamlined governance at Tier 1 and continued regulation at Tier 0. ADR-003 sets quorum by risk. ADR-011 forbids lowering quorum to obtain a yes.

**What was not done.** No concrete signer matrix was invented, and no ADR was drafted to host one. A matrix that omitted an applicable jurisdiction, or that treated low tier as a bypass of privacy, identity, or tool boundaries, would contradict ADR-016, ADR-020, ADR-032, and ADR-019.

**Classification.** Implementation specification. The principle is covered. The grid is not policy.

**Human approval.** Required before any concrete matrix is binding.

### DQ-008 — Institution creation

**Queue substance.** Historian registry verifies existence. FORGE initiates the proposal. Engineering prepares. Governed activation is separate.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-015: membership creation is governed; activation is a distinct state; Engineer builds and does not appoint; Teacher does not grant membership; Doctor does not appoint; Auditors verify membership; Historian preserves membership history; FORGE coordinates and does not hold unilateral appointment power; high-impact structural change can require human approval. ADR-006 matches the Engineer limit. ADR-005 matches the Historian limit.

**Historian boundary.** "Verifies existence" is read as evidence and registry validation. It is not a power to declare an institution into authority. The stronger reading, Historian as the approver of creation, contradicts ADR-015 and was not drafted.

**Classification.** Covered.

**Human approval.** Not required for this compatible reading.

### DQ-009 — Synchro multi-signatures

**Queue substance.** A single-use, short-lived, request-bound and action-bound Synchro with distinct Historian, Auditor, and Security attestations, atomically consumed.

**Source status.** Conversation candidate. The string Synchro does not occur in the accepted ADRs.

**Where the baseline already speaks.** ADR-009 requires ephemeral action-bound capabilities. ADR-018 requires expiration, state binding, and single-use consumption. ADR-004 separates attestation from substantive decision. ADR-005 limits Historian to evidence.

**What is new.** The named record and the fixed three-attestation set.

**Contradictions.** Historian as an approver or executor of the underlying action contradicts ADR-005. ADR-043 limits the Historian attestation to lineage and registry evidence.

**Classification.** New proposed ADR-043.

**Human approval.** Required. Pending.

### DQ-010 — Synchro replay and provenance

**Queue substance.** Check issuance lineage, exact scope, actor, nonce, expiration, and signatures. Quarantine replay. Historian preserves non-redeemable evidence.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-018 covers expiration, actor and action binding, consumption, and replay-prone single-use authority. ADR-017 covers digest integrity, chain of custody, and replay of evidence onto another action. ADR-029 covers message identity, replay, stale authority, and the rule that redelivery does not revive expired authority. ADR-005 and ADR-029 give Historian custody of historical evidence and withhold the power to recreate authorization by replay.

**Classification.** Covered. ADR-043 applies this existing law to Synchro if Synchro is accepted. Rejecting ADR-043 does not change replay law.

**Human approval.** Not required to keep replay law.

### DQ-011 — Compromise containment

**Queue substance.** Quarantine an institution on credible compromise, preserve forensics, and activate dormant sealed replacements only after the compromise path is verified closed.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-039: quarantine or suspend a compromised member, suspend authority when institutional independence is no longer trusted, preserve evidence before modification when it is safe to do so, and require recovery preconditions before trustworthy operation returns. ADR-015 records quarantine in membership history and separates activation from provisioning. ADR-014 covers loss of trustworthy governance.

**What remains design.** The sealed dormant replacement is a pattern for meeting those preconditions. It is not a new authority.

**Classification.** Implementation specification under ADR-039 and ADR-015.

**Human approval.** Required before that pattern is binding. Replacements still cannot be activated to manufacture a friendlier quorum. ADR-015 already forbids vote manufacturing.

### DQ-012 — Recovery and reinstatement

**Queue substance.** Doctor health, Security vector closure, Engineering fix, Historian evidence, Auditor procedure, independent critical reviews, and FORGE execution.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-039 recovery preconditions include known-good software, identity, enforcement, quorum, Watchers, Auditors, Historian continuity, and Doctor health verification. ADR-039 also states that Engineer may build a fix and that deployment stays governed. ADR-006 separates diagnosis, preservation, and execution. ADR-005 withholds restoration from Historian. ADR-001 and ADR-040 place execution in the FORGE process. Independent review is the Watcher and Auditor split in ADR-004.

**Historian and Security limits.** Historian contributes evidence, not an execution approval. Security contributes vector closure inside security jurisdiction, not universal incident authority. ADR-039 states the Security limit directly.

**Classification.** Implementation specification. The role split is covered. The checklist order is not a new institution.

**Human approval.** Required before the checklist is binding operational policy.

### DQ-013 — Safe mode

**Queue substance.** Graded degradation, human notification and approval for defined critical operations, minimal trusted services, and a verified exit.

**Source status.** Conversation candidate. "Safe mode" is not a defined constitutional state name in the accepted ADRs.

**Where the baseline already speaks.** ADR-011 defines degraded operation as reduced authority chosen in advance, plus a short list of essential safe functions that must be defined before the failure. ADR-036 defines HEALTHY, DEGRADED, IMPAIRED, CRITICAL, RECOVERY_REQUIRED, and UNKNOWN. ADR-039 requires human notification and distinguishes human instruction during an incident from a panic override. ADR-007 forbids automatic resume after HARD STOP. ADR-013 governs human approval.

**Classification.** Implementation specification. A named safe mode must be a degraded mode under ADR-011, not a new authority regime. The minimal service list and the critical operations that need human approval are not enumerated here, because inventing them would be a new policy the queue did not specify.

**Human approval.** Required before those lists exist as policy.

### DQ-014 — Fault-code escalation

**Queue substance.** Pending, confirmed, restricted, and safe-mode fault states. Debounce for noncritical issues. Immediate escalation for critical issues. Thresholds based on severity, type, confidence, persistence, and criticality.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-036 and ADR-039 already define governance-health and incident state machines. ADR-007 requires immediate action for credible imminent danger to human life. ADR-031 says uncertainty triggers the minimum appropriate response and does not escalate automatically to maximum authority. ADR-032 and ADR-039 say severity labels do not create authority.

**Contradiction to avoid.** A second constitutional state machine with different names would compete with ADR-036 and ADR-039. No ADR was drafted. An implementation specification can map pending to suspected or unknown, confirmed to confirmed, restricted to degraded, impaired, or contained, and safe mode to ADR-011. Threshold numbers are not in the queue and were not invented.

**Classification.** Implementation specification.

**Human approval.** Required before the mapping or any numeric threshold is binding.

### DQ-015 — Incident closure

**Queue substance.** Signed independent reviews and an investigator's final cause, fix, and prevention report, preserved by Historian.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-039 closure is not "the error disappeared." Closure criteria include containment, revocation, blast radius, evidence, remediation, verified recovery, regression coverage, restored governance, and explicit unresolved issues. The closure record includes timeline, root cause, consequences, containment, remediation, recovery, verification, and residual risk. ADR-005 and ADR-039 require Historian to preserve the incident rather than delete it. ADR-004 and ADR-017 supply independent signed evidence.

**Reading used.** "Investigator" is the investigation function ADR-039 already describes, not a new institution with approval power. Historian preserves the report and does not close the incident by filing it.

**Classification.** Covered.

**Human approval.** Not required for the closure principle. Signature formats are implementation detail under ADR-017.

### DQ-016 — Risk-based fast lane

**Queue substance.** Low-consequence informational requests use lightweight governance and do not bypass privacy, identity, or tool boundaries.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-032 Tier 0 allows broad autonomous reasoning for observational work and still applies data governance, information boundaries, adversarial-input controls, resource limits, and privacy rules. Tier 1 may use streamlined governance for limited reversible effects. ADR-020, ADR-035, ADR-019, and ADR-033 keep privacy, identity, tools, and enforcement in force at every tier. Unknown consequence does not default to Tier 0.

**Classification.** Covered. A fast lane that skips Gatekeeper, identity, privacy, or tool registration would contradict the baseline and is not proposed.

**Human approval.** Not required to keep this reading.

### DQ-017 — Memory boundaries

**Queue substance.** Persistent professional competence, expiring case working memory, case-isolated reviewers, Historian long-term history, and governed retrieval.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-020 governs memory, retention, and context isolation. ADR-010 separates competence from jurisdiction. ADR-005 assigns long-term history to Historian. ADR-003 requires independent evaluation.

**What is new.** The explicit class split, especially case-isolated review context versus case working memory, and the rule that retrieval is not authorization.

**Classification.** New proposed ADR-044.

**Human approval.** Required. Pending.

### DQ-018 — Rolling adaptive retention

**Queue substance.** Opt-in conversation and meeting recording, consent safeguards, a temporary rolling buffer, importance suggestions, and user control of long-term retention.

**Source status.** Conversation candidate. Design idea. Not a present capability.

**Where the baseline already speaks.** ADR-020 requires governed retention and treats long-term retention as added exposure. It does not authorize default recording, a rolling conversation buffer, or importance-ranked promotion.

**Contradictions avoided.** Default-on capture is not proposed. Suggestions are not decisions. User control does not silently delete evidence ADR-017 already requires to be kept. Multi-party consent is left open.

**Classification.** New proposed ADR-045.

**Human approval.** Required. Pending. Not implemented.

### DQ-019 — Learning packages

**Queue substance.** A dedicated teacher per agent, recipient-specific signed packages from approved knowledge, sandbox tests, governed promotion, and no direct internal access.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-010 already requires authenticated training-package identity, a named target institution, a controlled environment before production authority, Teacher proposals that are not authorization, Doctor and Auditor and Historian roles, and a ban on Teacher rewriting jurisdiction. ADR-029 and ADR-020 forbid teaching by direct internal access to another institution's memory or secrets. ADR-015 says successful training does not grant membership.

**What remains design.** "One dedicated teacher per agent" is an assignment pattern inside the Teacher institution. It is not a new institution per agent.

**Classification.** Implementation specification under ADR-010.

**Human approval.** Required before per-agent teacher assignment is mandatory. Direct internal access remains forbidden either way.

### DQ-020 — Verified institutional tools

**Queue substance.** Every institution has declared tool manifests, permissions, validation, evidence output, and health checks.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-019 requires this class of declaration for external tools. ADR-006 and ADR-036 cover health findings. ADR-033 covers enforcement. The baseline does not clearly extend the manifest duty to every internal institutional capability.

**Classification.** New proposed ADR-046. A manifest remains a declaration, not a permission to invoke.

**Human approval.** Required. Pending.

### DQ-021 — Lifecycle four-party review

**Queue substance.** Teacher, Doctor, Engineering, and Historian sign different claims for upgrade, rollback, and release. Other applicable governance still applies. FORGE alone executes.

**Source status.** Conversation candidate.

**Where the baseline already speaks.** ADR-006, ADR-010, and ADR-005 already split those questions. They do not define one four-signature ceremony, and they do not say Teacher signs changes that contain no learning content.

**Contradictions avoided.** Historian's signature is an evidence claim, not release approval and not rollback authority. The four signatures are not a complete authorization set.

**Classification.** New proposed ADR-047.

**Human approval.** Required. Pending.

### DQ-022 — Local-first hybrid-ready

**Queue substance.** Local first. Optional cloud specialists later. Cloud has no direct local execution authority.

**Source status.** Conversation candidate. Deployment posture, not a claim of a running local or cloud system.

**Where the baseline already speaks.** ADR-019, ADR-027, ADR-028, ADR-033, and ADR-038 constrain external and remote execution. They do not choose local-first as doctrine.

**Classification.** New proposed ADR-048.

**Human approval.** Required. Pending. Not implemented.

### DQ-023 — Personal FORGE vision

**Queue substance.** One independently owned FORGE per person, independent memory and skills, and no automatic cross-FORGE learning transfer.

**Source status.** Conversation candidate. Personal-assistant vision. Not a present capability. ADR-028 already contemplates independent deployments for different humans and also for organizations, sites, and other purposes.

**Covered subset.** Independent trust domains, no automatic merger of authority, and no automatic transfer of learning or memory follow ADR-028, ADR-010, ADR-020, and ADR-013.

**Conflict.** An exclusive rule of one FORGE per natural person, forbidding organizational or multi-deployment FORGE, contradicts ADR-028. No ADR was drafted. See the conflicts document.

**Classification.** Deferred.

**Human approval.** Required before this vision becomes a deployment profile. It cannot be accepted in the exclusive form without a constitutional amendment the owner has not made.

### DQ-024 — Multimodal future

**Queue substance.** Wearables, voice, contextual assistance, consent-based listening, and safe device integration are future roadmap and are not implemented.

**Source status.** Conversation candidate. The queue itself says this is not implemented. This repository confirms the absence of any device integration.

**Where the baseline already speaks.** ADR-019 names sensors and physical devices as external systems that still need governance. ADR-020 and ADR-007 constrain data and human-life risk. ADR-040's baseline does not include a multimodal product surface. ADR-045 does not authorize always-on capture.

**Classification.** Deferred. A roadmap ADR would look like adoption of capabilities the queue says do not exist. No ADR was drafted.

**Human approval.** Required before any of these capabilities enters scope.

## Proposed ADR index

| ADR | Queue | Title |
| --- | --- | --- |
| ADR-041 | DQ-001 | Internal Institutional Organization |
| ADR-042 | DQ-002 | Proposed Institution Domain Taxonomy |
| ADR-043 | DQ-009, with DQ-010 applied as existing law | Synchro Single-Use Attestation Record |
| ADR-044 | DQ-017 | Memory Class Boundaries |
| ADR-045 | DQ-018 | Opt-In Rolling Retention |
| ADR-046 | DQ-020 | Institutional Tool Manifests |
| ADR-047 | DQ-021 | Lifecycle Claim Separation for Upgrade, Rollback, and Release |
| ADR-048 | DQ-022 | Local-First Hybrid Posture |

Existing ADR files were not edited, renumbered, or overwritten.
