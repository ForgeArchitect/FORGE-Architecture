# ADR-041: Institution Template Package and Numbered Layers

**Status:** Proposed
**Date:** 2026-10-09
**Architecture:** FORGE
**Decision Type:** Proposed specification / not a constitutional amendment
**Source decision queue:** DQ-001, DQ-004, DQ-008, DQ-017, DQ-019, DQ-020, DQ-021
**Related canonical ADRs:** ADR-001, ADR-002, ADR-003, ADR-005, ADR-006, ADR-007, ADR-009, ADR-010, ADR-012, ADR-015, ADR-017, ADR-020, ADR-021, ADR-024, ADR-025, ADR-026, ADR-027, ADR-029, ADR-032, ADR-033, ADR-038, ADR-040
**Constitutional approval:** Pending

The decision-queue items cited above are unratified handoff candidates. They are not authority for this record. ADR-001 through ADR-040 remain the canonical baseline. This ADR does not amend them.

## Context

FORGE needs a reusable description of an institution that Codex, or another implementer, can check before any institution is admitted to a registry. The public repository currently contains the constitutional record and no institution registry, dispatcher, Gatekeeper, validator, or staged-update runtime.

ADR-040 already numbers ten constitutional architecture layers. ADR-032 numbers consequence tiers. Those two numberings are different things. DQ-001 describes a director, departments, and specialist agents inside an institution. That internal rank is not numbered in the accepted ADRs.

## Problem

An implementer can otherwise invent a second governance path, treat routing as approval, or place specialists on the execution layer. The repository also has no machine-checkable institution package that fails closed on authority expansion, bad hashes, or activation without citations.

## Proposed decision

Adopt, only as a proposed specification, one institution-template package:

- Identity, authority, startup material, interfaces, memory, learning, isolation, failure behavior, lifecycle, and package metadata are explicit fields.
- Every element declares exactly one layer number and the ADR-040 name for that number, or a proposed extension number.
- Layers 1 through 10 keep the ADR-040 numbers and names exactly.
- Layers 11 and 12 are a proposed, unapproved extension for an institution department and a specialist agent. The institutional lead remains on canonical Layer 4 (Authorization) and is not a new layer.
- Authority-bearing delegation inside the template may move only from a lower layer number to a higher layer number, and only by attenuation.
- The package in this repository is an example. Its lifecycle is `validated`. It is not approved, not staged for activation, and not active.
- A static validator checks the package. It is not a Gatekeeper and it does not grant authority.

## Alternatives considered

- Leave institution shape entirely to a future runtime. Rejected for this handoff because Codex would have no checkable contract in the repository.
- Renumber ADR-040 so that Layer 0 is the constitution and specialists receive the next integers. Rejected because ADR-040 already assigns Layers 1–10.
- Treat ADR-032 tiers as the institution layers. Rejected. ADR-032 says a tier does not grant authority.
- Treat Layers 7–10 as subordinates of Layer 6 because their numbers are higher. Rejected. That reading would contradict Watcher, Auditor, Historian, and Doctor independence.

## Jurisdiction and authority boundaries

Institutions prepare, review, and sign proposals. FORGE alone performs approved external execution through protected adapters. The dispatcher routes and grants no authority. A lead's delegated approval does not grant execution. Layers 7–10 are not delegation targets. No element in this template may occupy Layer 1, Layer 3, Layer 5, Layer 6, or Layers 7–10.

Cross-institution and cross-layer communication is mediated by the dispatcher and Gatekeepers. Direct lateral access is prohibited.

## Security and privacy

The example contains no credentials, keys, signatures, or domain secrets. Missing approval and competence records stay `PENDING`. `PENDING` is not approval. Historical evidence stays distinct from current instructions. Case context is isolated and is archived with the Historian before it is cleared. Resource figures stay `PENDING_LIMIT` ceilings, not spending authority.

## Failure modes

If a required institution is unavailable, dependent work waits. Silence is not approval. Evidence is preserved. HARD STOP and governed RESET/RESUME remain the ADR-007 mechanisms. This package cannot resume work and cannot restore from the Historian.

The validator rejects missing fields, execution capability, dispatcher-granted authority, delegation that exceeds the delegator, upward or sideways delegation, direct institution access, a specialist claim to director approval, unknown or duplicate layer numbers, hash and dependency mismatches, and admission of any lifecycle other than `draft` or `validated`.

## Invariants and tests

The machine-checkable statement lives in `institution-template/validator/validator.py`. Tests live in `institution-template/tests/test_institution_template.py`. They are ordinary unit tests. They are not a constitutional certification and they do not create approval records.

## Compatibility with frozen baseline

This record is compatible with ADR-040 only if Layers 1–10 stay unchanged and Layers 11–12 remain proposed. It does not replace the ADR-026 request lifecycle or the ADR-038 environment names. The institution-package lifecycle (`draft`, `validated`, `approved`, `staged`, `active`, `suspended`, `retired`) is a proposed package lifecycle, not a statement that those transitions have been authorized.

## Open questions

- Should Layers 11 and 12 be adopted, rejected, or replaced with a different internal numbering that a human chooses?
- Should the institutional lead remain Layer 4, or should a human assign the lead a distinct proposed number?
- How should the proposed package lifecycle map onto ADR-026 and ADR-038 once a runtime exists?
- Which owner identity occupies `identity.owner`? The example keeps that reference `PENDING`.

## Approval record (pending)

No Root Human approval, Auditor attestation, Doctor finding, or registry admission is recorded. `constitutional_approval_granted` is false. Activation is not activated.
