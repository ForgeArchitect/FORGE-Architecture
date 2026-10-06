# ADR-015: Institutional Identity, Membership, and Succession

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Institutional Governance / Identity

## Context

FORGE distributes authority across institutions rather than concentrating authority in a single component.

Institutions may contain multiple independent members.

Examples include:

- Banker,
- Engineer,
- Doctor,
- Teacher,
- Auditor,
- Watcher,
- constitutional governance bodies,
- and other authority-bearing institutions.

This creates a fundamental identity question:

> What makes a process a legitimate member of an institution?

If FORGE can arbitrarily create new institutional members, then quorum governance can be defeated.

For example, if three Bankers reject a transaction, FORGE must not be able to create five new Bankers that approve it.

Likewise, an attacker must not be able to start a process named:

> Banker-4

and automatically gain Banker authority.

Institutional membership must therefore be independently authenticated, governed, and historically traceable.

## Decision

FORGE establishes explicit institutional identity and membership governance.

Authority belongs to constitutionally recognized institutional roles and authenticated members occupying authorized institutional positions.

Running software does not acquire institutional authority merely by claiming an institutional name.

Institutional membership must be established through an authorized membership process.

## Institutional Identity

Each authority-bearing institution has a unique institutional identity.

The identity defines the institution's:

- constitutional role,
- jurisdiction,
- membership structure,
- quorum rules,
- applicable Watchers,
- applicable Auditors,
- health requirements,
- and governance constraints.

The institution exists independently of any individual member currently occupying it.

## Member Identity

Each institutional member receives a unique authenticated identity.

A member identity should be bound to information sufficient to establish:

- institution,
- member position or seat,
- authorized software or model identity,
- configuration,
- applicable constitutional version,
- credential material where appropriate,
- activation state,
- and other relevant integrity properties.

The exact identity mechanism may vary by implementation.

## Authority Belongs to the Institution

Individual members do not personally own the authority of their institution.

For example:

A Banker member participates in Banker's institutional decision.

The member does not independently possess all Banker authority outside the institutional process.

This establishes the rule:

> The institution holds jurisdiction.

> Members participate in exercising that jurisdiction.

## Institutional Seats

Where useful, FORGE may define institutional membership using authorized seats.

For example:

Banker Institution:

- Banker Seat 1
- Banker Seat 2
- Banker Seat 3
- Banker Seat 4
- Banker Seat 5

The seat represents an authorized position in the institution.

A process may exercise the authority associated with that seat only after valid assignment and authentication.

## Fixed Membership Rules

Membership rules must be established independently of the outcome of a particular vote.

FORGE cannot alter membership merely because the current institution is producing an inconvenient decision.

For example:

> Banker rejected the transaction, so add three new Bankers.

is prohibited.

Membership changes require their own governed process.

## No Vote Manufacturing

FORGE must not create additional voting members for the purpose of changing an institutional outcome.

This includes:

- spawning new members,
- duplicating approving members,
- cloning an existing member,
- creating temporary voters,
- replacing dissenting members,
- or modifying membership thresholds after voting begins.

A governance system whose voters can be manufactured by the system being governed does not provide meaningful governance.

## Independent Members

Multiple members should represent meaningful independent evaluation.

Running the exact same deterministic process five times does not necessarily create five independent authorities.

Where practical, institutional design should reduce shared failure domains through differences such as:

- execution context,
- model instance,
- reasoning process,
- infrastructure,
- evidence access,
- initialization,
- or other relevant independence mechanisms.

The appropriate degree of diversity depends on risk.

## Membership Creation

Creating a new authority-bearing member is a governed event.

The process should establish:

1. Why the member is required.
2. Which institution it will join.
3. Which authorized seat it will occupy.
4. Whether creation changes institutional capacity.
5. Whether quorum rules are affected.
6. Whether required software and configuration are authentic.
7. Whether the member is healthy.
8. Whether required Watcher coverage exists.
9. Whether required Auditor verification exists.
10. Whether activation has been authorized.

Only after these conditions are satisfied does the member receive institutional authority.

## Member Activation

A newly created member does not automatically receive authority merely because initialization completed successfully.

Activation is a distinct state transition.

A conceptual lifecycle may include:

Candidate  
→ Provisioned  
→ Identity Verified  
→ Health Verified  
→ Governance Verified  
→ Activated  
→ Active Member

Authority begins only at the constitutionally defined activation stage.

## Member Removal

Removing an authority-bearing member is also a governed event.

A member may require removal because of:

- health failure,
- compromise,
- retirement,
- persistent malfunction,
- constitutional change,
- infrastructure migration,
- or another legitimate reason.

Removal must not be used as punishment for a valid DENY vote.

## Dissent Is Not Failure

A member is not unhealthy merely because it disagrees with FORGE or other institutional members.

For example:

A Banker returning DENY is performing its role.

FORGE cannot classify that Banker as failed solely because FORGE wanted APPROVE.

Doctor health determinations must be based on health criteria rather than desired voting outcome.

## Suspension

A member may be temporarily suspended when its integrity or health is uncertain.

Suspension removes or limits its ability to exercise institutional authority according to predefined rules.

Suspension does not automatically change quorum requirements.

The applicable quorum behavior must already be constitutionally defined.

## Quarantine

Potentially compromised members may enter a quarantine state.

A quarantined member:

- does not participate in normal authority,
- cannot cast valid new votes,
- remains available for investigation where safe,
- and cannot restore itself to active status.

Re-entry requires the appropriate governed process.

## Succession

Institutions may maintain predefined succession rules for unavailable or retired members.

A successor does not inherit the predecessor's decision.

The successor receives the authenticated request and independently evaluates it.

This establishes the rule:

> A seat may be inherited.

> A vote may not.

## Replacement of Unavailable Members

When a member is legitimately unavailable, an authorized redundant member may occupy the applicable seat or participate according to predefined redundancy rules.

The replacement process must verify:

- unavailability of the original member,
- identity of the replacement,
- eligibility,
- health,
- institutional configuration,
- and applicable authorization.

Replacement cannot be invoked merely because the original member returned DENY.

## No Approval Shopping

FORGE cannot repeatedly replace members until it obtains a desired result.

A member that successfully evaluates a request and returns DENY is not considered unavailable.

A member that returns an inconvenient answer remains a functioning member.

## Pending Votes During Succession

If membership changes while a request is being evaluated, the applicable governance rules must define whether:

- the existing vote remains valid,
- the request must be reevaluated,
- or the institutional decision must restart.

For high-risk actions, membership changes during deliberation may require reevaluation to ensure that the final quorum reflects a valid institutional state.

## Member Expiration

Some institutional assignments may be temporary.

Temporary membership must include explicit expiration.

Expiration removes the member's authority.

Expired membership cannot continue participating because the process remains technically online.

## Member Credentials

Institutional credentials should be scoped to the member's role.

A member credential should not automatically provide unrestricted access to:

- other institutional identities,
- root governance,
- external credentials,
- constitutional modification,
- or unrelated privileged systems.

Compromise of one member should not automatically compromise the entire institution.

## Credential Rotation

Member authentication material may require rotation.

Rotation changes the mechanism proving identity.

It does not create a new institutional authority unless membership itself changes.

Identity continuity and credential continuity are separate concepts.

## Cloning

Cloning an authority-bearing member requires special consideration.

A copy of an authorized member does not automatically become another authorized voting member.

For example:

Copying Banker Seat 1 into another runtime does not create Banker Seat 6.

The clone has no institutional voting authority unless separately admitted through the governed membership process.

## Process Restart

Restarting an authorized member does not necessarily create a new member.

The system must be able to distinguish:

- legitimate restart of the same institutional identity,

from:

- creation of a new authority-bearing identity.

Reactivation may require integrity and health verification depending on risk.

## Institutional Membership Registry

FORGE should maintain an authenticated record of valid institutional membership.

The registry may contain:

- institution identity,
- authorized seats,
- current occupants,
- member status,
- activation state,
- suspension state,
- membership version,
- credential references,
- and relevant integrity information.

The registry itself is governance-critical state.

## Membership Version

Membership configuration should have an authenticated version or state identity.

Consequential authorization can therefore be associated with the institutional configuration that produced it.

This allows FORGE to determine:

> Which institution actually approved this request?

rather than merely:

> Something claiming to be Banker approved it.

## Quorum Binding

A quorum result should be bound to the applicable institutional membership state.

For example:

A valid 4-of-5 Banker approval should identify which five-member institutional configuration governed the vote.

Changing membership after approval may require revalidation depending on the action and applicable policy.

## Doctor Role

Doctor evaluates member health.

Doctor may determine that a member is:

- healthy,
- degraded,
- unhealthy,
- unstable,
- or unsuitable for participation.

Doctor does not independently appoint the replacement member.

Health authority and membership authority remain separate.

## Auditor Role

Auditors may verify:

- member identity,
- institutional membership,
- seat assignment,
- activation authority,
- membership version,
- quorum eligibility,
- succession events,
- suspension,
- and removal.

Auditors do not appoint institutional members.

## Watcher Role

Watchers may observe institutional members for:

- unexpected behavior,
- identity anomalies,
- unauthorized participation,
- jurisdiction violations,
- duplicate identities,
- abnormal voting behavior,
- or attempts to bypass membership governance.

Watcher evidence may trigger investigation.

It does not automatically rewrite membership.

## Historian Role

The Historian preserves institutional membership history.

The historical record may include:

- member creation,
- activation,
- suspension,
- quarantine,
- succession,
- replacement,
- credential rotation,
- removal,
- retirement,
- and membership-version transitions.

A removed member does not disappear from history.

## Teacher Role

Teacher may train or prepare candidate members.

Successful training does not grant membership.

Teacher may establish competence.

Governance establishes authority.

## Engineer Role

Engineer may build, configure, or deploy software used by institutional members.

Engineer does not decide whether the resulting process receives institutional voting authority.

Building a Banker does not appoint a Banker.

## FORGE Role

FORGE may coordinate membership procedures.

FORGE does not possess unilateral appointment authority unless a specific constitutional rule explicitly grants a narrowly defined administrative function.

FORGE cannot create voters to control the institutions governing FORGE.

## Human Role

Root Human Authority may participate in membership governance according to the Constitution.

High-impact changes to institutional structure may require explicit human approval.

This is especially relevant when changes affect:

- quorum,
- institutional size,
- constitutional bodies,
- Auditors,
- Watchers,
- or root governance.

## Institutional Expansion

Increasing an institution from five members to seven may alter its governance characteristics.

Therefore, structural expansion is distinct from replacing an unavailable member in an already authorized seat.

Changes to institutional structure must follow the appropriate governance process.

If the change alters constitutional quorum or authority, constitutional amendment may be required.

## Institutional Contraction

Likewise, reducing institutional membership must not be used to make quorum easier to obtain.

Removing two dissenting members from a five-member institution to create a three-member unanimous institution is prohibited unless the structural change itself has been independently authorized.

## Identity Conflict

If two active processes claim the same exclusive institutional identity or seat, the identity enters a conflicted state.

Neither claimant should automatically be trusted.

Affected authority may be suspended until identity integrity is re-established.

## Unknown Member

A process that cannot prove valid institutional membership has no institutional authority.

It may provide information.

It may not cast an authority-bearing vote merely because its output appears reasonable.

## Membership Failure

If FORGE cannot establish:

- who the valid members are,
- which membership version applies,
- whether a member is active,
- whether a seat is duplicated,
- or whether the membership registry is authentic,

affected consequential governance fails closed.

Identity uncertainty does not become voting authority.

## Catastrophic Membership Failure

If institutional identity becomes broadly untrustworthy, FORGE may enter Constitutional Recovery according to ADR-014.

Normal governance should not continue using identities that cannot be authenticated.

## Consequences

Explicit membership governance introduces additional:

- identity infrastructure,
- cryptographic verification,
- lifecycle management,
- health checks,
- membership records,
- succession logic,
- and administrative complexity.

It may make replacement of failed components slower.

FORGE accepts this cost because institutional redundancy has little constitutional value if the system can manufacture, replace, or impersonate the voters whenever their decisions become inconvenient.

## Foundational Principle

> Authority belongs to the institution.

> Membership is governed.

> A process does not become an authority by naming itself an authority.

> A replacement inherits a seat, not a vote.

> Dissent is not failure.

> FORGE cannot manufacture voters to manufacture consent.

Institutional identity must remain independently verifiable before institutional decisions can carry constitutional authority.
