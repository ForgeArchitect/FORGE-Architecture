# ADR-041: Internal Institutional Organization

**Status:** Proposed
**Date:** 2026-10-09
**Source decision queue:** DQ-001
**Related canonical ADRs:** ADR-001, ADR-003, ADR-015, ADR-027, ADR-040
**Constitutional approval:** Pending

## Context

ADR-003 establishes that authority-bearing FORGE subsystems are institutions with independently evaluating members, and that no individual member is the institution. ADR-015 places authority in authenticated seats and requires a governed membership process. ADR-027 allows attenuated delegation to sub-agents and states that internal sub-agents are workers unless separately admitted to an authority-bearing role.

Design discussions after the v1.0 baseline described a further internal shape: a director, departments, and specialists inside an institution, with scoped internal delegation. That shape is not specified in ADR-001 through ADR-040. This repository contains architecture records only. There is no implementation or test evidence here that any institution already has this internal organization.

## Problem

Without an explicit boundary, an internal "director" can be mistaken for a person who speaks for the institution, routes around independent member evaluation, or executes consequential work. Departments and specialists can likewise be mistaken for new constitutional institutions or for additional votes.

## Proposed decision

An institution may organize its internal work as a director function, departments, and specialists. That organization is administrative.

1. The director function coordinates internal work and may route work to departments and specialists inside the institution.
2. Departments group internal work. They do not become separate constitutional institutions by being named.
3. Specialists perform scoped work. Their authority is attenuated delegation under ADR-027.
4. No director, department, or specialist receives independent consequential execution authority. Consequential execution remains with the FORGE execution process after the authenticated request chain in ADR-002 and the baseline in ADR-040.
5. Internal organization does not manufacture votes, seats, or quorum. ADR-003 independent evaluation and ADR-015 membership rules remain in force. A director does not cast the institution's decision in place of the required members.
6. Where ADR-003 requires members to evaluate before seeing other members' substantive votes, internal routing preserves that independence.
7. Creating a new authority-bearing seat remains a governed membership event under ADR-015. Naming a specialist does not activate a seat.

This record does not require every institution to adopt this internal shape. Where an institution uses it, the limits above apply.

## Alternatives considered

- Leave internal organization entirely to implementation notes under ADR-003, ADR-015, and ADR-027, with no separate record. Rejected as the proposed decision because an unnamed director function is a recurring way to reconcentrate institutional authority.
- Treat the director as the institution's decision-maker. Rejected because it conflicts with ADR-003 and ADR-001.
- Admit every specialist as an institutional member. Rejected because ADR-015 already separates workers from seats, and vote manufacturing is prohibited.

## Jurisdiction and authority boundaries

Institutional jurisdiction stays with the institution under ADR-016. Internal roles exercise only the authority the institution already has, and only within the scope delegated to them.

The director function has no Gatekeeper, Auditor, Watcher, or Historian jurisdiction. It does not issue execution commands. It does not amend membership, quorum, or the Constitution.

FORGE may coordinate institutions. FORGE does not appoint a director in order to obtain a desired institutional outcome.

## Security and privacy

Internal routing is subject to ADR-020. A specialist receives the information required for the delegated scope. Department membership is not a reason for unrestricted access to another department's case material.

Internal messages follow ADR-029. They do not create authority by delivery. They do not open a side door around the authenticated request chain.

## Failure modes

- A director suppresses a dissenting member or substitutes a specialist's output for a quorum result. Required response: the result is not an institutional decision; Watchers and Auditors treat it as a governance failure under ADR-003 and ADR-004.
- A specialist retains delegated scope after the parent authorization expires or is revoked. ADR-018 and ADR-027 revocation and expiration apply.
- Compromise of a director is treated as compromise of a member or component under ADR-039, not as compromise of the institution's entire jurisdiction by itself. Quorum viability is reassessed under ADR-015 and ADR-036.
- Internal routing changes the authenticated request. ADR-002 material-mutation rules invalidate authority that no longer matches the request.

## Invariants and tests

These invariants are proposed. They have not been implemented or executed in this repository.

- No internal role can both originate a consequential action and execute it.
- A director route cannot change request identity, jurisdiction, or quorum.
- Specialist authority is a subset of the parent delegation and expires with it.
- Specialist outputs are not votes unless the actor occupies an authenticated seat and the vote follows ADR-003.
- Tests to require before any later acceptance: attempt to execute from a director role; attempt to count specialists as extra votes; attempt to show peer votes to members before independent evaluation by calling the path "internal routing"; attempt to keep specialist authority after revocation.

## Compatibility with frozen baseline

This proposal is compatible with ADR-040 if internal roles remain inside the institution and add no new constitutional power. It does not amend ADR-001, ADR-003, ADR-015, or ADR-027.

If a later human decision would give a director binding authority over the institution's vote or execution, that decision conflicts with the frozen baseline and is outside this proposal.

## Open questions

- Which institutions, if any, should be required to use a director, departments, and specialists, and which may remain seat-only under ADR-015.
- Whether "director" is a seat, a rotating duty, or a non-voting coordinator.
- How internal routing interacts with request witnessing. DQ-005's director-routing phrase is not adopted here as a substitute for Watchers or Auditors. See the coverage matrix.
- What minimum independent diversity ADR-003 requires when specialists share one department's model, host, or prompt.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The decision-queue source is a conversation candidate, not a ratification record
- This repository does not show an implementation or a passing test of this decision
