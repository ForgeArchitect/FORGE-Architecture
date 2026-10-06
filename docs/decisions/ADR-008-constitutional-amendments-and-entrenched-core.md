# ADR-008: Constitutional Amendments and Entrenched Core

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Constitutional Governance

## Context

FORGE must be capable of evolving.

Operational experience, new threats, changing requirements, and improved system design may reveal that an existing constitutional rule should be changed.

However, allowing FORGE or one of its institutions to freely modify the rules governing its own authority creates a fundamental conflict of interest.

For example, the Banker institution may determine that an existing financial authority limit is too restrictive.

That may be a legitimate observation.

It does not mean Banker should be able to increase its own authority.

Likewise, a software update must not be capable of silently changing the constitutional powers of the subsystem receiving the update.

FORGE therefore separates:

- software modification,
- policy configuration,
- institutional governance,
- and constitutional amendment.

## Decision

FORGE establishes a dedicated constitutional amendment process.

No ordinary institution, subsystem, Engineer update, runtime request, FORGE execution process, or institutional quorum may independently modify the Constitution.

Constitutional change requires a separate governance path.

The current model uses a bicameral structure consisting of:

1. a House-like proposal body,
2. a Senate-like constitutional review body,
3. and required human approval.

## The Constitution

The FORGE Constitution defines the fundamental distribution and limitation of authority within the system.

Constitutional rules may govern matters including:

- institutional jurisdiction,
- separation of powers,
- execution authority,
- authorization requirements,
- quorum requirements,
- emergency authority,
- amendment procedures,
- credential authority,
- recovery authority,
- human authority,
- and other foundational governance constraints.

FORGE operates under this Constitution.

FORGE does not own the Constitution.

## Amendment Trigger

An amendment may be proposed when evidence suggests that the current Constitution no longer adequately serves the architecture.

Possible triggers may include:

- repeated operational limitations,
- newly discovered threats,
- architectural improvements,
- new subsystem requirements,
- changes in human governance requirements,
- recurring deadlocks,
- insufficient safeguards,
- or lessons learned from historical evidence.

Identifying a problem does not authorize changing the Constitution.

It authorizes consideration of a proposal.

## Institutional Proposals

A FORGE institution may identify the need for constitutional change.

For example, Banker may determine that a financial authorization threshold creates unnecessary escalation during legitimate operations.

Banker may provide evidence supporting a change.

Banker cannot implement that change itself.

This establishes the rule:

> An institution may petition for changes to its authority.

> It may not grant those changes to itself.

## House

FORGE establishes a House-like constitutional body responsible for developing and considering amendment proposals.

The House may:

- receive proposed constitutional changes,
- review supporting evidence,
- request additional analysis,
- debate alternatives,
- define the proposed amendment,
- document expected consequences,
- and produce formal amendment text.

The House proposes.

The House does not unilaterally amend the Constitution.

## Senate

FORGE establishes a Senate-like constitutional review body.

The Senate evaluates proposed amendments from the perspective of constitutional integrity.

Its review may include:

- separation-of-powers impact,
- authority expansion,
- unintended interactions,
- institutional conflicts,
- security consequences,
- recovery consequences,
- emergency-governance effects,
- human-authority implications,
- and consistency with the entrenched constitutional core.

The Senate may approve, reject, or return a proposal for revision according to its governing rules.

## Bicameral Requirement

An ordinary constitutional amendment must successfully complete both constitutional bodies.

Approval by the House alone is insufficient.

Approval by the Senate alone is insufficient.

This prevents one constitutional body from possessing unilateral amendment authority.

## Human Approval

Successful machine governance review does not automatically activate a constitutional amendment.

Human approval is required before an ordinary amendment becomes effective.

The human receives the proposed amendment and relevant evidence necessary to understand the change.

The human may:

- approve,
- reject,
- or return the proposal for further consideration.

FORGE cannot interpret human silence as approval.

## Human Approval Is Explicit

Constitutional approval must be an affirmative authenticated action.

The following do not constitute human approval:

- timeout,
- lack of response,
- inferred preference,
- previous approval of a similar amendment,
- FORGE prediction of what the human would choose,
- or another institution claiming to speak for the human.

## Entrenched Constitutional Core

FORGE may contain an entrenched constitutional core.

The entrenched core contains foundational constraints that ordinary amendment procedures cannot modify.

These rules represent boundaries that FORGE's internal governance is not authorized to vote away.

Candidate entrenched principles may include:

- preservation of human life as a top-level emergency constraint,
- prohibition against unilateral self-expansion of authority,
- requirement for governed authorization before consequential execution,
- prohibition against silent constitutional modification,
- separation of critical authority,
- preservation of independent verification,
- and the requirement that FORGE remains subordinate to its Constitution.

The final contents of the entrenched core must be explicitly defined before production deployment.

## Constitutional Vault

The entrenched core may be stored or enforced through a protected constitutional mechanism conceptually referred to as the **Constitutional Vault**.

The Vault is not an intelligent governing institution.

Its purpose is to protect authoritative constitutional material from ordinary runtime modification.

The implementation may use mechanisms such as:

- signed constitutional artifacts,
- immutable or append-only storage,
- hardware-backed trust,
- independent verification,
- version pinning,
- threshold authorization,
- or other tamper-resistant controls.

The architecture does not depend on one specific implementation.

## No Self-Amendment Through Software Update

The Engineer cannot modify constitutional authority merely by deploying a software update.

If an update requires a constitutional change, the constitutional amendment must be approved separately.

Only after the amendment becomes valid may software changes implementing that authority be activated.

This separates:

> Changing what a subsystem can technically do

from:

> Changing what a subsystem is constitutionally allowed to do.

## No Runtime Constitutional Drift

Runtime learning, Teacher instruction, prompt modification, institutional consensus, or accumulated operational behavior cannot silently become constitutional law.

A subsystem behaving differently over time does not automatically acquire new jurisdiction.

Capability may evolve.

Jurisdiction changes only through the constitutional process.

## Amendment Identity

Every proposed amendment receives an authenticated amendment identity.

The identity is bound to the exact amendment text and material supporting context.

A materially altered amendment is a new proposal or revision requiring the appropriate review.

Approval of one amendment cannot be reused to authorize different constitutional text.

## Historian Role

The Historian preserves:

- amendment proposals,
- supporting evidence,
- House proceedings,
- Senate findings,
- human approval or rejection,
- previous constitutional versions,
- activated constitutional versions,
- and subsequent amendment history.

A new Constitution does not erase the previous Constitution.

The historical sequence remains visible.

## Auditor Role

Auditors verify:

- amendment identity,
- integrity of amendment text,
- required approvals,
- human authorization,
- constitutional version transition,
- and consistency between the approved amendment and activated Constitution.

The Auditor does not decide whether the amendment is desirable.

## Watcher Role

Watchers may observe the implementation and activation of constitutional changes.

This helps verify that the operational system behaves according to the Constitution that was actually approved.

## Doctor Role

When a constitutional change materially affects subsystem operation, the Doctor may evaluate system health before and after implementation.

Constitutional validity and operational health remain separate questions.

## Activation

An approved amendment does not become active merely because the vote completed.

Activation follows a controlled transition.

A conceptual process is:

1. Amendment is proposed.
2. Amendment identity is established.
3. Supporting evidence is collected.
4. House evaluates and approves the proposal.
5. Senate performs constitutional review and approves.
6. Human explicitly approves.
7. Auditor verifies the authorization chain.
8. Historian preserves the outgoing constitutional state.
9. Required implementation changes are prepared.
10. The new constitutional version is activated through the governed process.
11. Watchers observe activation.
12. Auditor verifies the active constitutional version.
13. Doctor evaluates affected operational health where appropriate.
14. Historian records the completed transition.

## Conflict of Interest

An institution directly benefiting from an amendment must not be capable of unilaterally determining the outcome.

FORGE should develop explicit conflict-of-interest rules for constitutional proceedings.

At minimum:

> The institution requesting expansion of its own authority cannot grant that expansion to itself.

## Amendment Failure

If any constitutionally required stage rejects the proposal, the amendment does not become active.

The rejected proposal remains in the historical record.

A revised proposal may be submitted later as a new governed amendment state.

## Emergency Limitation

Emergency status does not suspend the amendment process.

A HARD STOP may immediately subtract authority to preserve human life.

It may not rewrite the Constitution to create new permanent authority.

## Consequences

Constitutional amendment through multiple independent stages is slower than allowing FORGE to modify its own governance dynamically.

That delay is intentional.

FORGE accepts reduced constitutional agility in exchange for resistance to:

- self-expansion,
- governance capture,
- accidental authority drift,
- malicious updates,
- and silent changes to foundational safeguards.

## Foundational Principle

> FORGE may operate under the Constitution.

> FORGE may propose improvements to the Constitution.

> FORGE may not give itself permission to rewrite the Constitution.

Constitutional power remains separated from operational intelligence.
