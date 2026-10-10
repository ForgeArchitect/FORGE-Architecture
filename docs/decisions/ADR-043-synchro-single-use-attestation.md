# ADR-043: Synchro Single-Use Attestation Record

**Status:** Proposed
**Date:** 2026-10-09
**Revision:** 2026-10-10 bundle reconciliation. The exact change is in the approval record.
**Source decision queue:** DQ-009. DQ-010 is applied only as already-accepted replay and provenance law; it is not an independent new decision. Bundle draft filed as ADR-046 on 2026-10-10 is the same Synchro decision and is reconciled here.
**Related canonical ADRs:** ADR-002, ADR-004, ADR-005, ADR-009, ADR-017, ADR-018, ADR-029, ADR-035, ADR-039
**Constitutional approval:** Pending

## Context

ADR-009 requires narrow, short-lived, action-bound capabilities and states that possession of a secret is not authorization. ADR-018 requires expiration, state binding, and consumption of single-use authority. ADR-017 and ADR-029 require detectable integrity, authenticated provenance, and replay resistance. ADR-004 separates audit attestation from authorization. ADR-005 limits Historian to memory and evidence.

DQ-009 proposes a named record, Synchro: a single-use, short-lived, request-bound and action-bound object carrying distinct Historian, Auditor, and Security attestations, consumed atomically. The word Synchro does not appear in ADR-001 through ADR-040. No implementation of Synchro is present in this repository.

DQ-010 proposes checks of issuance lineage, exact scope, actor, nonce, expiration, and signatures, plus quarantine of replays and preservation of non-redeemable evidence. Those checks restate ADR-017, ADR-018, and ADR-029. This ADR applies them to the proposed Synchro record. It does not create a second constitutional rule for replay.

## Problem

A capability can be copied, delayed, or presented with a substituted scope if the attestation, the action binding, and the consumption event are separable. A combined signature can also be misread as if Historian, Auditor, or Security had approved the underlying action.

## Proposed decision

FORGE may use a Synchro record for a consequential capability only under the following proposed rules.

1. A Synchro is bound to one authenticated request and one exact action scope, including the actor authorized to present it, a nonce, an expiration, and the issuance lineage. For a consequential redemption, that actor is the FORGE execution process. An institution does not redeem the Synchro by holding it. The binding is to one immutable payload. Substituting the payload produces a different object.
2. It is single-use. Atomic consumption invalidates any further presentation of that Synchro. A consumed, expired, revoked, or mismatched Synchro is non-redeemable evidence. Historian may preserve that evidence under ADR-005 and ADR-017. Preservation does not redeem it. ADR-029 already states that Historian does not create current authorization by replaying old records.
3. The three attestations are distinct claims:
   - Historian attests evidence, registry lineage, and the freshness of that lineage evidence. Freshness means the lineage evidence is current as evidence. It is not a second expiration rule. Expiration remains ADR-018. The attestation is not approval of the action and is not execution authority.
   - Auditor attests process integrity of the record and its binding to the authorization chain. An audit attestation is not the substantive institutional decision. ADR-004 applies.
   - Security may attest that the security conditions for issuance were satisfied, and attests the security posture relevant to scope, compromise status, and presentation, within Security's jurisdiction. That issuance attestation does not make Security the source of governing authority. Security does not gain universal authority. ADR-039 applies.
4. Jurisdictional authorization remains necessary. A Synchro does not replace Banker, Engineer, Doctor, or any other institution required by ADR-016 and ADR-032. It does not replace Gatekeeper admissibility or the FORGE execution process.
5. Presentation checks fail closed when lineage, scope, actor, nonce, expiration, or signatures do not match. Replay and mismatch are quarantined as evidence. They are not retried into success.
6. Material change to scope, actor, request, or target produces a different action and requires a new Synchro. ADR-002 and ADR-018 apply.

Synchro is a proposed binding record. It is not a new institution and not a standing credential.

## Alternatives considered

- Keep using ADR-009 capabilities and ADR-018 single-use rules with no Synchro name and no fixed three-party attestation set. This remains acceptable if the owner rejects Synchro. It was not selected as the proposal because the queue asks for distinct attestations on one consumed object, and leaving that ceremony unnamed invites a combined "approved" signature.
- Make Historian a required approver of every Synchro-gated action. Rejected. That would assign Historian universal approval authority, which conflicts with ADR-005 and with the v1.0 baseline.
- Allow a Synchro to be replayed when the underlying request is unchanged. Rejected because ADR-018 consumes single-use authority and ADR-029 forbids reviving expired authority-bearing messages by redelivery.

## Jurisdiction and authority boundaries

Historian jurisdiction on a Synchro is evidence and registry validation. Auditor jurisdiction is integrity attestation. Security jurisdiction is security posture for the presented scope. The institution that owns the underlying domain still makes the substantive decision. FORGE executes only after the full authorization chain exists. The presenter of a Synchro is not authorized merely because the presenter holds the record.

## Security and privacy

Synchro material is credential-adjacent. ADR-009 and ADR-035 apply. Raw long-lived secrets are not placed inside the Synchro. The record carries references, bindings, and signatures sufficient to verify scope.

ADR-020 applies to lineage data. Verifiers receive the fields required to check the presentation. They do not receive unrelated case history because a Synchro is being checked.

Failed presentations are preserved as security evidence under ADR-017 and ADR-039. Quarantine is subtractive.

## Failure modes

- Partial consumption, where a duplicate presentation races the first. Required behavior: atomic consume; uncertain high-risk outcome is treated as consumed until the outcome is known, as ADR-018 already requires for single-use authority.
- A signature set is stripped down to one attestor. Required behavior: fail closed. Missing required attestations do not default to valid.
- Historian lineage is unavailable. Required behavior: fail closed for Synchro presentation. Unavailability is not approval and does not authorize FORGE to skip the check.
- Security attestation is stale relative to a new compromise. ADR-018 state binding and ADR-039 revocation apply. An old Security attestation does not outlive the compromise state it described.
- Replay after quarantine. The quarantined object stays non-redeemable.

## Invariants and tests

These invariants are proposed and have not been executed in this repository.

- One Synchro, one request, one action scope, one successful consumption.
- Historian signature absence and Historian signature presence are both incapable of executing the action.
- Replay, expired presentation, actor substitution, nonce reuse, and scope mutation fail closed and leave preservable evidence.
- Tests to require before any later acceptance: concurrent double presentation; presentation after revocation; presentation with a valid Auditor signature and a missing Historian or Security attestation; presentation of a Historian-preserved copy after consumption.

## Compatibility with frozen baseline

This proposal implements ADR-009 and ADR-018 in a named record. It does not amend them. If the owner rejects the fixed Historian, Auditor, and Security attestation set, the baseline capability rules still stand without Synchro.

DQ-010's replay and provenance checks are already baseline law. Accepting or rejecting Synchro does not reopen that law.

## Open questions

- Whether every consequence tier in ADR-032 requires a Synchro, or only tiers above a human-approved threshold. This ADR does not set that threshold.
- Whether failed attempts always consume a Synchro at every tier. ADR-018 already distinguishes high-risk uncertainty from ordinary policy. The tier mapping is open.
- Which key-management practice under ADR-035 signs each attestation, and how those signer keys are separated. The 2026-10-10 bundle asks for that separation to be specified. It is not specified here.
- What additional response follows compromise of a signer. Revocation, stale Security attestations, and ADR-039 already apply. The operational procedure beyond those rules is open. This ADR does not invent one.
- How atomic redemption is implemented. The rule remains atomic consumption, including the partial-consumption failure mode already stated. The mechanism is not specified here.
- Whether additional jurisdictional signatures are required on the same object. This ADR does not forbid them and does not make the three attestations a complete authorization set.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

2026-10-10 revision, from the bundle draft numbered ADR-046: consequential redemption is bound to the FORGE execution process; Historian's attestation includes freshness of lineage evidence and still is not approval; Security may attest issuance conditions without becoming the governing authority; open questions now include signer key separation, compromised-signer procedure, and the atomic-redemption mechanism. No accepted ADR was edited. Replay law is unchanged.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The decision-queue source is a conversation candidate, not a ratification record
- This repository does not show an implementation or a passing test of Synchro
