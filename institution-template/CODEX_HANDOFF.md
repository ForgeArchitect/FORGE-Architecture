# Codex handoff — FORGE institution template v1

This package is a proposed contract for the live FORGE system. It is not constitutional approval and it is not an activation order.

`constitutional_approval_granted`: false
`activation`: not activated

Do not merge it to main as an accepted amendment. Do not mark it Accepted. Do not call a production promotion, registry activation, or update-admission commit.

## What to integrate

Read, in this order:

1. `architecture/INSTITUTION_TEMPLATE.md` — numbered layers, the ten template sections, lifecycle, invariants.
2. `architecture/ADR-041-institution-template-and-numbered-layers.md` — Proposed only. In the git repository the same text is `docs/decisions/ADR-041-institution-template-and-numbered-layers.md`.
3. `schema/institution-template.schema.json`, `schema/layer-registry.schema.json`, and `schema/interfaces.schema.json`.
4. `validator/validator.py` — the checks that actually run.
5. `examples/EXAMPLE-INSTITUTION.json` — the only institution. Example, non-production, lifecycle `validated`.
6. `staging/candidate-manifest.json` and `manifest.json` — SHA-256 hashes. Both say not activated.
7. `UNRESOLVED_INTEGRATION.md` — runtime pieces this repository does not contain.

## How this maps onto FORGE

Use existing mechanisms. Do not build a second dispatcher, a second Gatekeeper, or a second registry beside the ones that already exist in the live system.

- **Dispatcher (ADR-002, ADR-040 Layer 3).** Register the institution id as routing metadata only. Routing does not approve, quorum, or execute. Reject any template whose `dispatcher_grants_authority` or `grants_authority` flag is true.
- **Gatekeepers (ADR-002, ADR-033).** When a Gatekeeper implementation is available, run `validate_package` as a deterministic admissibility check before a package can move past `validated`. A passing check is not an institutional vote and not Root Human approval. Fail closed on every validator error.
- **Institution registry / institution ledger.** This repository has no registry implementation. The Windows zip named `FORGE_INSTITUTION_LEDGER_V1` is not in the repository. If that ledger exists in the live system, submit this package as a candidate record at lifecycle `validated`, with approval references still `PENDING`. Do not write an active or approved row.
- **Staged update admission, artifact verification, and staging custody.** The live names `FORGE_GOVERNED_UPDATE_ADMISSION_V1`, `FORGE_STAGED_ARTIFACT_VERIFICATION_V1`, and `FORGE_STAGING_CUSTODY_CANDIDATE_V2` are not in this repository. The candidate manifest is the artifact those components should be given if they exist: status `STAGED_NOT_ACTIVATED`, SHA-256 of every listed file, self-hash of the manifest, activation not performed. Do not invent their internal APIs. If they are absent, stop and ask the owner. Do not activate.
- **Learning packages.** Teacher proposes, Engineer packages, Doctor verifies, activation stays staged and reversible (ADR-006, ADR-010). `FORGE_LEARNING_PACKAGE_CONTRACTS_V1` is not in this repository. Do not modify active skills from this template.
- **Doctor schedule and emergency runtime.** `FORGE_DOCTOR_SCHEDULE_V1` / `V2` and `FORGE_EMERGENCY_V1` are not in this repository. Health findings and HARD STOP stay on those existing paths. This template only cites ADR-007. It does not issue a Doctor READY and it does not resume anything.
- **Execution.** External execution remains FORGE through protected adapters after the existing authorization chain. No element in the example occupies Layer 6.

## Layer rule to preserve

Use ADR-040 Layers 1–10 with those exact numbers and names. Layers 11 and 12 are proposed and require a human decision before the live system treats them as constitutional. Until that decision, keep them labeled proposed and do not let them occupy Layer 6 or claim Layer 4 director approval.

Authority moves only from a lower number to a higher number, by bounded delegation. It does not move upward or sideways. Layers 7–10 are independent and are not delegation children of Layer 6. That reading is required so this package does not rewrite Watcher, Auditor, Historian, or Doctor independence. A human should confirm it.

## What a passing test means

`python3 -m unittest discover -s tests -v` from this directory (or `python3 -m unittest discover -s institution-template/tests -v` from the git root) means the example matches the proposed checks. It does not mean an owner approved the institution, a competence test was passed, or a package was activated.

## Rollback of this handoff

Do not activate the candidate. Discarding the unactivated candidate leaves the live system unchanged. There is no runtime rollback executor in this repository. `package.rollback.historian_checkpoint_ref` is `PENDING`.
