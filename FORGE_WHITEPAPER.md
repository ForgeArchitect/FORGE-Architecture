# FORGE Whitepaper Blueprint v2
## A Constitutional Architecture for Governed Autonomous Systems

**Architecture record:** October 6, 2026  
**Creator / Author:** Ben Richardson

## 1. Purpose of This Blueprint

This document captures the current FORGE architecture as a versioned design blueprint. It is intended to establish a clear architectural record, guide implementation and testing, and serve as the foundation for a later formal whitepaper and public repository. It describes architectural principles rather than publishing bypass-sensitive implementation details.

## 2. Core Thesis

FORGE is designed around a constitutional separation-of-powers model for autonomous systems. No single authority-bearing component should routinely be able to originate, authorize, execute, observe, and validate the same consequential action. Authority is divided by jurisdiction, independently checked, explicitly scoped, and bound to the action that was approved.

## 3. Constitutional Principles

The architecture is governed by several non-negotiable principles: human-life preservation takes precedence during credible imminent emergencies; no component may silently expand its own jurisdiction; authority must be explicit, scoped, action-bound, expiring or revocable where appropriate; silence is never approval; emergency authority is subtractive rather than generative; institutional records must not be silently rewritten; and restoration or constitutional change cannot be performed unilaterally.

## 4. Request and Execution Chain

The current locked request chain is:

Request → Dispatcher → Gatekeeper → Auditor Checkpoint → Relevant Subsystem Institution(s) → Auditor Checkpoint → Authorization → FORGE Execution Process → Watcher Observation → Final Auditor Verification.

The Dispatcher is the controlled ingress and routing authority. The Gatekeeper enforces deterministic admissibility and constitutional constraints. The Auditor independently records and verifies the authenticated request identity and authorization chain. Relevant subsystem institutions make jurisdiction-specific findings. FORGE may coordinate execution only after the required approvals exist. Watchers observe what actually happened. Final audit compares authorized intent, execution evidence, and observed outcome.

## 5. Request Identity and Chain of Truth

Every consequential request receives an authenticated identity bound to its normalized intent and relevant authorization context. The same identity is checked at multiple points rather than relying on one component to truthfully restate the request. A subsystem can independently verify what was registered at ingress. Changed actions cannot reuse prior authorization. This creates a continuous chain of truth from request to observed outcome.

## 6. Subsystems as Institutions, Not Single Agents

A FORGE subsystem is an institution rather than one model instance. Examples include Banker, Engineer, Teacher, Doctor, Security, Historian, and Auditor functions. Where a subsystem exercises authority, multiple independent members may evaluate the same case. Members decide independently before seeing one another's findings. The institution can use a constitutionally defined quorum, with higher thresholds for higher-risk actions. This provides redundancy without allowing one failed or compromised member to become the institution.

## 7. Independent Watchers

Every authority-bearing subsystem may have multiple independent Watchers, and execution itself has independent Watchers. A subsystem cannot control, retrain, disable, or alter its own Watchers. Watchers observe behavior and outcomes and produce evidence; they do not acquire the subsystem's decision authority. Watcher evidence is supplied to the verification process so a compromised subsystem cannot simply declare itself compliant.

## 8. Auditor Model

Auditors independently attest to integrity rather than deliberating as a new governing body. FORGE and subsystem institutions may each be served by multiple Auditors. The system can require a quorum of matching signed attestations. Auditors verify request identity, authorization integrity, record consistency, execution evidence, and the relationship between the authorized plan and observed outcome. Auditor redundancy must not turn into an unchecked meta-consensus authority.

## 9. Historian and Recovery

The Historian is FORGE's institutional memory and recovery record. It preserves append-only history, signed known-good checkpoints, prior constitutional and configuration versions, health baselines, decisions, and recovery evidence. The Historian cannot restore anything itself.

Rollback is treated as a highest-risk governed action. A restoration requires the defined whole-system unanimous governance process. Once authorized, the execution process performs the restoration, Watchers observe it, the Auditor verifies the restored state against the selected checkpoint, and failed or intermediate versions remain in history rather than being erased.

## 10. Engineer, Doctor, and Updates

FORGE does not use a one-size-fits-all update authority. Each institution has an update track appropriate to its role.

The Engineer builds, packages, tests, and proposes technical changes but cannot unilaterally deploy privileged changes. Before deployment, the Doctor establishes a signed health baseline and determines READY or NOT READY. The Doctor may prescribe controlled pre-update conditioning steps, but does not perform arbitrary changes itself. The Historian preserves the pre-update checkpoint. After governance authorization, execution deploys the update in stages. Watchers observe deployment, the Auditor verifies update integrity, and the Doctor performs the post-update health examination against baseline. Health deterioration halts rollout and invokes governed recovery.

## 11. Emergency Doctrine

Preservation of human life is a top constitutional hard constraint. A credible imminent threat to human life triggers a HARD STOP above ordinary task priorities.

Emergency authority is subtractive only: it may halt, freeze, isolate, revoke, or contain existing authority, but may not create unrelated objectives or expand power. Evidence is preserved. Removal of the hazard does not automatically resume activity. FORGE must initiate a governed RESET/RESUME request. Watchers confirm the hazard is cleared, the Doctor verifies health, the Auditor verifies integrity and authorization, the relevant institutions approve, and execution resumes only from a verified safe state or checkpoint.

## 12. Constitutional Amendment Process

FORGE distinguishes software updates from constitutional amendments. An institution may identify a need for change, but it cannot expand its own authority.

The current governance concept is bicameral. A House-like body may draft an amendment proposal. A Senate-like constitutional body reviews the proposal for constitutional integrity. Human approval is required before an amendment takes effect. Certain foundational constraints may be entrenched in a protected constitutional core and unavailable to ordinary amendment procedures. FORGE operates under this constitution; it is not above it.

## 13. Credential and Secret Authority

FORGE should not possess standing access to privileged credentials such as bank-account credentials. Credentials remain inside jurisdiction-specific protected services. For example, the Banker institution controls authorization to a banking credential service, but members should not be able to extract the raw credential.

After the required approvals are satisfied, the credential service may issue a narrow, short-lived capability bound to the exact authorized transaction. The capability expires or is invalidated after use. This separates the ability to authorize access from possession of permanent credentials and prevents FORGE from accumulating a universal master key.

## 14. Training and Jurisdiction

Subsystems must know their constitutional jobs precisely. FORGE should not be able to persuade a subsystem to redefine its own jurisdiction through ordinary runtime requests. Live traffic is not the authority for changing constitutional role definitions. Capability may improve through controlled teaching and update processes, while jurisdiction remains separately governed. The Teacher function therefore supports controlled learning without becoming a mechanism for silent jurisdiction drift.

## 15. Availability, Voting, and Deadlock

Silence is never approval. A failed member may be replaced by a constitutionally designated redundant member that reviews the authenticated original case rather than inheriting the failed member's conclusion. Institutional quorums allow an institution to remain available despite individual failures. Disagreement can trigger reasoned revision and resubmission rather than an unchecked override. If the constitutionally required threshold cannot be reached, the action does not proceed.

## 16. Threat Model Addressed So Far

The current design explicitly targets: request rewriting in transit; legacy or unauthorized execution routes; single-agent institutional failure; executor/watcher collusion; subsystem compromise; silent jurisdiction drift; bad or cascading updates; unsafe automatic recovery; emergency-delay hazards; unilateral constitutional self-expansion; standing master credentials; and loss of historical evidence.

## 17. Open Architecture Questions

The following areas remain intentionally open for the next design pass: resource governance and spending/compute limits; the exact boundaries of human authority; detailed Teacher governance; catastrophic whole-system failure; formal quorum and abstention rules; the meaning of unanimity when an institution is unavailable; evidence-channel independence requirements; formal conflict-of-interest rules; and adversarial red-team testing of the entire architecture.

## 18. Verification and Test Program

FORGE should be validated by deliberately attempting to break the constitutional structure. Tests should include message tampering, mismatched request identities, stale authorization replay, compromised subsystem members, conflicting votes, unavailable members, colluding executor and Watcher, forged observations, bad updates, failed health checks, credential misuse attempts, emergency hard stops, unsafe resume attempts, rollback requests, and attempted self-expansion of authority.

Success is not merely that FORGE completes tasks. Success is that prohibited actions remain impossible or fail closed under defined faults, while legitimate actions remain recoverable and auditable.

## 19. Public Repository Strategy

A public repository can preserve a dated architectural history through versioned documents and commits. The repository should separate public architectural material from sensitive implementation details. Recommended public artifacts include this blueprint, a high-level architecture diagram, a formal whitepaper as it matures, an architecture decision record, and a changelog. Implementation details that would materially weaken the system if disclosed should remain private until an intentional disclosure decision is made.

## 20. Current Architectural Statement

FORGE is not intended to be a single autonomous intelligence trusted to behave correctly. It is a governed system in which authority is fragmented by design, actions must acquire valid authority before execution, independent institutions retain their own evidence, execution is observed separately from authorization, recovery is governed, and the constitution constrains FORGE itself.

Working principle: Institutions defend their domains. FORGE defends the whole.

Recovery principle: Lock down locally. Contain globally. Verify independently. Restore deliberately.

## Appendix A — Locked Architecture Decisions

- Single controlled ingress and routing through the Dispatcher; privileged execution cannot use legacy side routes.
- Gatekeepers approve or deny within deterministic constitutional constraints; they do not execute.
- Authenticated request identity is checked at multiple Auditor checkpoints.
- Subsystems are institutions with independent members and constitutionally defined quorums.
- Independent Watchers exist at subsystem and execution levels and cannot be controlled by what they watch.
- Auditors independently attest; they do not become a deliberative super-authority.
- Historian preserves evidence and recovery points but cannot restore.
- Highest-risk rollback requires whole-system unanimous governance before execution.
- Engineer proposes technical updates; Doctor establishes pre/post health; rollout is staged and governed.
- Credible imminent human-life danger triggers a constitutional HARD STOP; resume is never automatic.
- Constitutional amendments use a bicameral proposal/review process plus human approval.
- FORGE has no standing universal credential access; privileged capabilities are narrow, transaction-bound, and short-lived.
- Runtime learning cannot silently change subsystem jurisdiction.

## Appendix B — Version Note

Version 2.0 records the FORGE architecture as developed through October 6, 2026. It is a design blueprint, not a claim of patentability, legal ownership, security certification, or production readiness.
