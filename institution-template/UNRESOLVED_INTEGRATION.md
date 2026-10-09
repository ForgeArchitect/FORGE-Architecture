# Unresolved integration and human decisions

This file records what the repository does not contain. None of these gaps are filled by inventing an approved runtime.

## Not in this repository

The git tree is the constitutional document set (ADR-001 through ADR-040), the whitepaper, the changelog, and this proposed template. A search of the tree found no institution registry, dispatcher, Gatekeeper, Historian service, Teacher service, Engineer service, Doctor service, update admitter, staging custody store, or prior test runner.

The owner's Windows download list names release zips that are not present here. Integration with them is unresolved. No contract from inside those zips was available to target. Where an accepted ADR already states the rule, the template cites the ADR instead of guessing the zip's API.

| Named release zip (not in this repo) | Cited constitutional rule | Integration status |
| --- | --- | --- |
| FORGE_GOVERNED_UPDATE_ADMISSION_V1 | ADR-006 update authorization; ADR-038 promotion artifact | UNRESOLVED_NOT_IN_REPOSITORY |
| FORGE_STAGED_ARTIFACT_VERIFICATION_V1 | ADR-006 auditor checks the deployed bytes; ADR-017 integrity | UNRESOLVED_NOT_IN_REPOSITORY |
| FORGE_STAGING_CUSTODY_CANDIDATE_V1 and V2 | ADR-038 staging is not production authority | UNRESOLVED_NOT_IN_REPOSITORY |
| FORGE_LEARNING_PACKAGE_CONTRACTS_V1 | ADR-010 training identity and jurisdiction boundary | UNRESOLVED_NOT_IN_REPOSITORY |
| FORGE_INSTITUTION_LEDGER_V1 | ADR-015 institutional identity; ADR-026 ledger is not authority | UNRESOLVED_NOT_IN_REPOSITORY |
| FORGE_EMERGENCY_V1 | ADR-007 HARD STOP and governed RESET/RESUME | UNRESOLVED_NOT_IN_REPOSITORY |
| FORGE_DOCTOR_SCHEDULE_V1 and V2 | ADR-006 periodic health examinations | UNRESOLVED_NOT_IN_REPOSITORY |

Also unresolved, because they are not implemented in this repository: protected execution adapters, jurisdictional credential services, quorum voting, Watcher processes, and the constitutional reference monitor. The template assumes those roles as ADR text, not as callable code.

## Conflicts with canonical ADRs

These are recorded so they are not silently "fixed" by this package.

1. **ADR-040 Layers 1–10 are interacting layers, not a chain of command.** Applying "higher number means subordinate delegate" to Layers 7–10 would make Watchers, Auditors, the Historian, and the Doctor subordinates of execution. This template refuses delegation into or out of Layers 7–10 instead. A human should confirm that refusal.
2. **ADR-032 tiers are not these layer numbers.** Tier 0 through Tier 4 classify consequence. A tier does not grant authority. The template does not reuse them.
3. **ADR-026 request states are not the package lifecycle.** `REGISTERED`, `AUTHORIZED`, `EXECUTING`, and the rest govern consequential requests. The package states `draft` through `retired` are proposed and unapproved.
4. **ADR-038 environment names are not package states.** `STAGING` and `PRODUCTION` are environments. `staged` and `active` in this template are proposed package states. The candidate manifest's `STAGED_NOT_ACTIVATED` means the bytes are hashed and not promoted.
5. **ADR-023 boot states and ADR-024 retirement** remain the constitutional account of boot and decommissioning. This package does not boot an institution and does not retire one.
6. **DQ-001 through DQ-024 are not ratified.** The internal department and specialist ranks come from the owner's request to number roles ADR-040 does not number. They are Proposed.
7. **There is no standalone Constitution file.** Accepted ADRs are the constitutional record. This template does not add one and does not claim to be one.
8. **No Layer 0.** The owner's fallback numbering (Layer 0 as highest) was not used because ADR-040 already numbers layers, starting at 1.

## Human decisions required

- Adopt, reject, or replace proposed Layers 11 (Institution Department) and 12 (Specialist Agent).
- Confirm that the institutional lead stays on canonical Layer 4 rather than receiving a new number.
- Confirm that Layers 7–10 are outside institution delegation.
- Choose whether the proposed package lifecycle should later be mapped onto ADR-026 and ADR-038 or kept as its own state machine.
- Name the Root Human owner. The example reference is `PENDING`.
- Decide whether any real institution, other than this labeled example, should ever be written in this repository.
- Point Codex at the live admission, custody, ledger, learning, emergency, and Doctor-schedule implementations if they exist outside this git tree. Do not treat this handoff as those implementations.
