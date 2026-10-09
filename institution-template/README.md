# FORGE institution template (proposed)

Proposed, not accepted, not activated. `constitutional_approval_granted` is false.

This directory is a handoff for the owner and for Codex. It contains the institution architecture spec, JSON schemas, a static validator, one example institution, tests, and a staged-update manifest. It does not admit an institution to a live registry.

## Run the tests

From this directory:

```bash
python3 -m unittest discover -s tests -v
```

From the repository root:

```bash
python3 -m unittest discover -s institution-template/tests -v
```

Check the example alone:

```bash
python3 institution-template/validator/validator.py validate institution-template/examples/EXAMPLE-INSTITUTION.json
```

The example must stay `validated`, non-production, and unapproved. A passing test does not approve it.

## Layout

- `architecture/INSTITUTION_TEMPLATE.md` — numbered layers and the ten template sections
- `schema/` — JSON schemas
- `validator/validator.py` — invariant checks
- `examples/EXAMPLE-INSTITUTION.json` — the only institution
- `tests/test_institution_template.py`
- `manifest.json` — SHA-256 of every other file in this package, approval false, activation `not activated`
- `staging/candidate-manifest.json` — staged-update candidate, status `STAGED_NOT_ACTIVATED`
- `CODEX_HANDOFF.md` — how to integrate it without activating it
- `UNRESOLVED_INTEGRATION.md` — missing runtimes and human decisions

The Proposed ADR is `docs/decisions/ADR-041-institution-template-and-numbered-layers.md` in the git repository. Handoff zips copy it under `architecture/`.
