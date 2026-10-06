# ADR-022: Institutional Conflict of Interest and Recusal

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Governance / Conflict of Interest / Institutional Independence

## Context

FORGE separates authority across institutions so that no single component routinely controls the complete lifecycle of a consequential action.

However, separation of powers can still fail if an institution is allowed to exercise decisive authority over matters in which that institution has a direct interest.

Examples include:

- Engineer approving its own update without independent review,
- Teacher approving an expansion of Teacher jurisdiction,
- Auditor solely certifying the integrity of its own conduct,
- Security expanding Security authority because Security declares the expansion necessary,
- Banker approving an increase to Banker's own financial authority,
- Watchers deciding whether their own observation failures should be ignored,
- FORGE deciding that FORGE should receive additional constitutional authority,
- or an institution investigating allegations of its own compromise and declaring itself trustworthy.

The problem is not merely malicious behavior.

A conflicted institution may sincerely believe its preferred outcome is correct.

Constitutional governance must therefore account for structural conflicts of interest rather than relying solely on good intentions.

## Decision

FORGE establishes explicit conflict-of-interest and recusal rules.

An authority-bearing institution or member must not be the sole decisive authority over a matter that materially:

- expands its own authority,
- reduces oversight of itself,
- protects itself from investigation,
- changes the rules governing itself,
- determines the validity of allegations against itself,
- creates direct institutional benefit,
- or otherwise compromises independent judgment.

Conflicted authorities may provide evidence, explanation, technical analysis, or recommendations.

They may not substitute those contributions for required independent governance.

## Core Rule

> No authority should be the sole judge of a decision that materially expands, protects, or validates its own power.

## Structural Conflict

A structural conflict exists when an institution's constitutional position creates a direct interest in the outcome.

This does not require proof of malicious intent.

For example:

Teacher proposes:

> Teacher should be allowed to modify institutional jurisdiction directly.

Teacher is structurally conflicted regarding final approval of that proposal because the proposal expands Teacher's own authority.

## Member Conflict

Conflict may also exist at the individual member level.

A member may be conflicted because it:

- originated the proposal,
- created the artifact under review,
- participated in the disputed action,
- is evaluating its own failure,
- has a direct operational dependency on the outcome,
- or has another constitutionally defined conflict.

Member-level conflict does not necessarily invalidate the entire institution.

## Institutional Conflict

An entire institution may be conflicted.

For example:

If the question is:

> Should Auditor oversight be permanently removed from this class of actions?

Auditor has an institutional interest in the question.

Auditor may provide analysis.

Auditor should not possess unilateral authority to decide the constitutional outcome.

Likewise, FORGE itself is conflicted regarding proposals to give FORGE unrestricted authority.

## Conflict Does Not Mean Silence

Recusal does not necessarily mean that a conflicted authority becomes invisible.

A conflicted institution may possess important technical knowledge.

It may therefore be permitted or required to provide:

- evidence,
- impact analysis,
- technical explanation,
- risk assessment,
- historical context,
- alternatives,
- or recommendations.

The distinction is:

> Participation in analysis is not the same as decisive authority.

## Recusal

Recusal removes a conflicted member or institution from the portion of the decision process in which independent judgment is constitutionally required.

Recusal should be:

- explicit,
- attributable,
- recorded,
- scoped to the conflict,
- and governed by predefined rules.

Recusal is not an informal disappearance from the process.

## Recusal State

A member participating in a decision may have a state such as:

- ELIGIBLE,
- RECUSED,
- ABSTAIN,
- UNAVAILABLE,
- or another constitutionally defined state.

RECUSED is distinct from ABSTAIN.

ABSTAIN means:

> The member is eligible but does not cast a substantive vote.

RECUSED means:

> The member is not eligible to exercise decision authority over this matter because of conflict.

## Recusal Is Not Denial

A recused member does not cast DENY merely by being recused.

Likewise, recusal is not APPROVE.

The quorum rules determine how recusal affects the institutional decision.

## Predetermined Recusal Rules

Recusal rules must be defined before a particular outcome is known.

FORGE cannot decide after seeing a vote:

> This member is now conflicted because it voted DENY.

Likewise, an approving member cannot be selectively declared eligible while dissenting members are declared conflicted.

## Dissent Is Not Conflict

A member is not conflicted merely because it:

- disagrees with FORGE,
- disagrees with another member,
- returns DENY,
- raises risk,
- requests more evidence,
- or blocks execution within its legitimate jurisdiction.

Conflict must arise from a defined relationship to the matter, not from the desirability of the member's vote.

## Self-Declared Recusal

A member may identify its own potential conflict.

Where appropriate, the member may request recusal.

The existence and effect of that recusal remain subject to applicable governance rules.

Self-recusal must not be used to manipulate quorum.

## Forced Recusal

Another authority may identify evidence that a member is conflicted.

A forced recusal must follow an authenticated process.

FORGE cannot unilaterally remove inconvenient voters by labeling them conflicted.

## Conflict Evidence

A conflict determination should be supported by identifiable evidence.

Examples may include:

- proposal authorship,
- execution participation,
- institutional relationship,
- affected jurisdiction,
- direct authority expansion,
- investigation target,
- or another defined conflict condition.

Conflict determinations become governance evidence under ADR-017.

## Conflict Declaration

Consequential governance may include a conflict declaration identifying:

- decision being considered,
- participating institutions,
- participating members,
- known conflicts,
- recusals,
- replacement rules,
- and applicable quorum.

This becomes part of the authorization record.

## Proposal Authorship

Creating a proposal does not automatically prohibit all participation in evaluating it.

For example:

Engineer may design an update.

Engineer remains necessary to explain:

- technical design,
- expected behavior,
- dependencies,
- testing,
- and deployment requirements.

However, Engineer cannot be the sole authority establishing that its own update is safe, healthy, secure, constitutionally valid, and correctly executed.

Independent institutions retain their respective roles.

## Self-Approval

FORGE prohibits sole self-approval of consequential actions where independent governance is constitutionally required.

Examples include:

Engineer builds update  
→ Engineer alone approves update  
→ Engineer deploys update  
→ Engineer certifies success

This collapses separation of powers.

Instead, applicable independent authorities participate according to jurisdiction.

## Self-Audit

A component may perform internal diagnostics.

Internal diagnostics are useful.

They do not replace constitutionally required independent audit.

An Auditor may also review its own internal operation for maintenance purposes.

That review does not constitute independent certification of the Auditor itself.

## Auditor Conflict

If an Auditor's own behavior is under investigation, that Auditor cannot be the sole authority certifying its own innocence or integrity.

Other independent Auditors or the applicable recovery/governance process must evaluate the evidence.

## Watcher Conflict

A Watcher accused of:

- suppressing evidence,
- falsifying observation,
- failing to observe,
- or colluding with an Executor

cannot be the sole authority determining whether its own evidence remains trustworthy.

Independent evidence channels must be used.

## Doctor Conflict

Doctor may evaluate the health of other institutions.

If Doctor itself is suspected of malfunction or compromise, Doctor cannot be the sole authority declaring itself healthy.

Independent diagnostic and governance mechanisms must apply.

## Teacher Conflict

Teacher cannot independently authorize:

- expansion of Teacher jurisdiction,
- removal of Teacher oversight,
- permanent training exemptions,
- or changes allowing Teacher to rewrite constitutional authority.

Teacher may propose such changes.

The constitutional amendment process decides them where applicable.

## Engineer Conflict

Engineer cannot independently authorize changes that:

- expand Engineer jurisdiction,
- remove independent update review,
- disable Doctor checks,
- disable Watchers,
- disable Auditor verification,
- or allow Engineer to deploy unrestricted privileged changes.

Engineer may design and propose changes.

Independent governance decides whether they may be deployed.

## Security Conflict

Security cannot use the concept of security to grant itself unlimited authority.

For example:

> Security requires unrestricted control over every institution.

is a constitutional authority question, not merely a Security decision.

Security may explain the risk.

Security cannot unilaterally rewrite the Constitution.

## Banker Conflict

Banker cannot independently increase:

- its own financial limits,
- its own quorum authority,
- its own credential access,
- or the financial resources available to Banker itself

where those changes alter constitutional authority.

Applicable governance remains required.

## Historian Conflict

Historian preserves records.

Historian cannot decide that evidence unfavorable to Historian should be removed because Historian considers it incorrect.

Corrections must preserve historical provenance under ADR-017.

## FORGE Conflict

FORGE is structurally conflicted regarding any proposal that would materially increase FORGE's own independent authority.

Examples include:

- eliminating institutional approval,
- giving FORGE direct access to all credentials,
- allowing FORGE to appoint arbitrary voters,
- removing Watcher independence,
- removing Auditor independence,
- permitting FORGE to rewrite jurisdiction,
- or allowing FORGE to amend the Constitution itself.

FORGE may propose architectural improvements.

FORGE cannot authorize its own elevation above the Constitution.

## Root Human Authority

Authenticated Root Human Authority remains external to FORGE's ordinary institutional structure.

However, root actions should still be explicit and attributable.

FORGE must not fabricate Root Human approval to resolve a conflict involving FORGE itself.

## Constitutional Amendments

Changes to institutional power are governed under ADR-008.

A conflicted institution may participate in analysis of an amendment affecting it.

It does not thereby acquire unilateral amendment authority.

## Quorum and Recusal

Recusal creates a quorum challenge.

The Constitution must avoid two opposite failures:

1. allowing conflicted members to control the decision,

and:

2. allowing strategic recusal to destroy governance.

Applicable institutional rules should therefore define how recused seats affect quorum.

## No Dynamic Quorum Weakening

FORGE cannot respond to recusal by arbitrarily lowering the approval threshold until the desired outcome becomes possible.

Any recusal-adjusted quorum rule must be predefined.

## Minimum Independent Participation

Certain decisions may require a minimum number of non-conflicted participants regardless of ordinary quorum.

For example:

If a five-member institution normally requires four approvals, but four members are conflicted, one remaining member should not automatically inherit the full authority of the institution.

The matter may require:

- independent replacement members,
- another institution,
- escalation,
- constitutional governance,
- or fail-closed behavior.

## Conflict Saturation

Conflict saturation occurs when too many members of an institution are conflicted to form a trustworthy decision.

The institution does not solve conflict saturation by allowing the conflicted members to vote anyway.

Instead, applicable governance may require:

- authorized alternates,
- independent temporary members,
- another constitutionally designated body,
- human escalation,
- or constitutional recovery.

## Alternate Members

Institutions may maintain predefined alternate members for conflict situations.

An alternate must:

- possess valid institutional identity,
- satisfy health requirements,
- be independent of the conflict,
- and evaluate the matter independently.

Alternate membership cannot be created ad hoc merely to obtain approval.

## Succession Versus Recusal

ADR-015 succession rules address unavailable or replaced members.

Recusal addresses conflicted members.

These states are different.

A dissenting member cannot be moved into succession merely to avoid its vote.

A conflicted member cannot remain decisive merely because it is technically available.

## Temporary Replacement

Where constitutionally defined, a recused member may be temporarily replaced for a specific decision.

The replacement receives authority only for the defined institutional function and period.

Temporary replacement does not permanently displace the original member.

## Replacement Independence

A replacement for a recused member must not simply inherit the recused member's conclusion.

It independently evaluates the authenticated request and evidence.

## Conflict Chains

Conflict may propagate.

For example:

Engineer proposes an update that changes Engineer authority.

A review body composed entirely of Engineer-controlled processes would not provide meaningful independence.

FORGE must evaluate whether the supposed independent reviewer shares the same controlling interest.

## Common Control

Two nominally separate components may still be conflicted if one controls the other.

Relevant forms of control may include:

- appointment,
- retraining,
- configuration,
- credential control,
- evidence control,
- removal authority,
- or operational dependency.

Independence requires more than different component names.

## Institutional Independence

Conflict-of-interest analysis should consider whether an institution can materially influence the supposedly independent authority reviewing it.

For example:

A subsystem should not be able to disable the Watcher responsible for investigating that subsystem.

## Evidence Independence

Conflict rules extend to evidence.

A conflicted authority should not be the sole source of evidence proving the matter in which it is conflicted.

Independent evidence under ADR-017 should be used where consequence warrants.

## Financial Conflict

If an institution's own resource allocation is being considered, the institution may explain its resource requirements.

It should not necessarily possess unilateral authority to grant itself additional resources.

ADR-012 resource governance remains applicable.

## Investigation

When misconduct or compromise is suspected, the target of the investigation must not control:

- evidence collection,
- evidence retention,
- investigator selection,
- investigation scope,
- or final certification

to the degree that doing so would destroy independence.

## Preservation of Evidence

Recusal or suspension must not permit the affected authority to erase relevant evidence.

Historian and applicable independent evidence mechanisms preserve the record.

## Recusal Does Not Erase History

A recused member's prior actions remain part of the historical record.

Recusal affects current decision authority.

It does not rewrite prior participation.

## Conflict Discovered After Approval

A material conflict may be discovered after an institutional decision has already been made.

The affected authorization may require revalidation.

Factors may include:

- severity of conflict,
- role of conflicted participant,
- quorum margin,
- action status,
- and whether execution has occurred.

## Conflict Discovered Before Execution

If a material undisclosed conflict is discovered before consequential execution, execution should halt until the authorization is revalidated.

## Conflict Discovered After Execution

If execution already occurred, FORGE preserves evidence and initiates the applicable review.

The system does not rewrite history to claim that valid independent approval existed if it did not.

## Conflict Concealment

Intentional concealment of a material conflict is itself a governance-integrity event.

Possible responses may include:

- suspension,
- quarantine,
- investigation,
- credential revocation,
- membership review,
- or recovery.

## Conflict Manipulation

FORGE should detect attempts to manipulate conflict rules.

Examples include:

- falsely declaring dissenters conflicted,
- engineering conflicts to eliminate voters,
- strategic self-recusal to destroy quorum,
- creating dependent reviewers,
- or repeatedly replacing independent reviewers.

## Watcher Role

Watchers may observe for:

- suspicious recusals,
- abnormal member replacement,
- self-approval,
- conflict concealment,
- reviewer dependence,
- or governance patterns suggesting conflict manipulation.

## Auditor Role

Auditors may verify:

- conflict declarations,
- recusal eligibility,
- participant identity,
- quorum calculation,
- replacement legitimacy,
- decision integrity,
- and required independence.

Auditors do not create missing independent authority.

## Historian Role

Historian preserves:

- conflict declarations,
- recusal decisions,
- replacement events,
- quorum state,
- evidence,
- final decisions,
- and later conflict discoveries.

This allows patterns of repeated conflict to become visible over time.

## Doctor Role

Doctor may determine whether a member's behavior suggests degradation or malfunction.

Doctor must not label a member unhealthy solely because the member's vote creates an inconvenient conflict.

Health and conflict remain distinct concepts.

## Security Role

Security may investigate compromise or manipulation relevant to conflicts.

Security does not gain constitutional authority to remove any institution merely by declaring it a security concern.

## Gatekeeper Role

Gatekeeper may block a request whose approval chain contains an unresolved material conflict where independent approval is required.

## Dispatcher Role

Dispatcher may route a conflicted matter to the constitutionally defined independent authority.

Dispatcher does not choose replacements based on which participant is most likely to approve.

## Conflict and HARD STOP

ADR-007 remains available when credible imminent threat to human life exists.

HARD STOP authority remains subtractive.

A conflict-of-interest dispute cannot be used to prevent immediate constitutionally authorized life-preserving containment.

Likewise, HARD STOP cannot be used as a pretext to permanently bypass recusal requirements.

## Conflict and Constitutional Recovery

If conflicts become so widespread that trustworthy governance cannot be formed, ADR-014 Constitutional Recovery may apply.

FORGE does not solve systemic conflict by granting itself the missing authority.

## Fail-Closed Rule

If a material conflict exists and FORGE cannot establish the independent authority required to resolve it, the consequential action does not proceed.

Unresolved conflict does not become implied approval.

## Consequences

Conflict-of-interest governance introduces:

- recusal rules,
- alternate members,
- independence analysis,
- conflict declarations,
- quorum complexity,
- and possible delay.

Some actions may become temporarily impossible when too many authorities are conflicted.

FORGE accepts this cost.

A governance system is not meaningfully independent if the entities being governed can decide when they are exempt from oversight.

## Foundational Principle

> An institution may explain its own interests.

> It may not be the sole judge of those interests.

> Recusal removes conflicted authority without converting conflict into approval.

> Dissent is not conflict.

> Independence must be real, not merely nominal.

> FORGE cannot authorize its own elevation above the institutions that govern it.

No component may use its position inside FORGE to become the sole authority over whether that component should receive more power, less oversight, or immunity from accountability.
