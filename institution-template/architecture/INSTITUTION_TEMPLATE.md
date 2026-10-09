# FORGE Institution Template

**Status:** Proposed. Not accepted. Not activated.
**Schema:** `forge.institution-template` `0.1.0-proposed`
**Constitutional baseline:** ADR-040
**Package lifecycle of the example:** `validated`

This template tells an implementer how to describe one institution. It does not create the institution, admit it to a registry, or authorize it to act. The normative checks that can run in this repository are `institution-template/validator/validator.py`. Those checks are not the ADR-033 reference monitor.

There is no separate Constitution file in this repository. The accepted constitutional record is ADR-001 through ADR-040. ADR-040 is the v1.0 baseline.

## Numbered layer table

ADR-040 already numbers the constitutional architecture. Those numbers and names are copied exactly. ADR-032 consequence tiers are not layers and do not grant authority. Layer 0 is not used, because the canonical numbering starts at Layer 1.

Lower numbers are higher authority. Delegation inside an institution may move only toward a higher number, and only by giving away a subset of delegable work. An element may not claim authority reserved to a lower-numbered layer. Layers 7–10 stay independent: they are not delegates of the execution layer and they are not delegates of an institution.

| Number | Name | Source | Who may occupy it in this template |
| --- | --- | --- | --- |
| 1 | Root Constitutional Authority | ADR-040, canonical | Nobody in the institution package. Root Human authority stays outside the institution. |
| 2 | Identity and Institutional Structure | ADR-040, canonical | The institution identity element only. |
| 3 | Request and Intent Governance | ADR-040, canonical | Dispatcher and Gatekeeper. The institution declares routes to them and does not become them. Routing grants no authority. |
| 4 | Authorization | ADR-040, canonical | The institutional lead. Director approval, jurisdiction findings, and proposal signatures live here and are not delegable. |
| 5 | Capability Enforcement | ADR-040, canonical | Credential services, ephemeral capabilities, and policy enforcement points. Not the institution. |
| 6 | Execution | ADR-040, canonical | FORGE execution through protected adapters. An institution that claims this layer is rejected. |
| 7 | Independent Observation | ADR-040, canonical | Watchers. Not a delegation target. |
| 8 | Verification and Evidence | ADR-040, canonical | Auditors and the Historian. The Historian records and does not restore. |
| 9 | Health and Assurance | ADR-040, canonical | Doctor. Diagnosis is not repair and is not deployment. |
| 10 | Recovery and Constitutional Continuity | ADR-040, canonical | HARD STOP, governed recovery, and authority extinction. Resume is not automatic. |
| 11 | Institution Department | Proposed extension, human decision, not approved | A department inside the example institution. |
| 12 | Specialist Agent | Proposed extension, human decision, not approved | A specialist agent inside the example institution. |

Layers 11 and 12 exist so department and specialist elements can carry integers without renumbering ADR-040. They are not constitutional law until a human adopts them. DQ-001 is an unratified candidate and is not that adoption.

The lead is not given a new number. Director approval remains Layer 4 authority. A specialist on Layer 12 who claims `director_approval` is claiming a lower-numbered layer and is rejected.

## 1. Identity and charter

Required: institution id, purpose, responsibilities, owner, lead, and agent specialties.

The example id is `example.non-production.institution`. Its purpose is to demonstrate the template. It claims no domain. Owner and lead identity references are `PENDING`. Specialty competence is `PENDING`. `PENDING` is not an identity, an appointment, or a competence result.

The institution holds jurisdiction. Members and elements do not personally own that jurisdiction (ADR-015). This package does not create seats, quorum membership, or voters.

## 2. Authority

Permitted work is preparation, review, and signing of proposals, plus jurisdiction findings and director approval held only by the Layer 4 lead.

Explicit prohibitions include external execution, direct lateral access, self-expansion of jurisdiction, dispatcher-granted authority, automatic skill modification, credential extraction, and upward or sideways delegation.

Delegations are attenuating (ADR-027). The delegate's layer number must be greater than the delegator's. Reserved authority, including director approval and external execution, cannot be delegated. A lead approval does not grant execution. The example delegations are declared and `PENDING`; they are not in force. `authority.operational` is false.

Escalation of jurisdictional uncertainty goes to the Gatekeeper through the dispatcher. A credible imminent threat to human life honors the existing ADR-007 HARD STOP. Escalation does not create objectives or authority.

## 3. Agent startup packages

Startup material lists operating skills, workflows, domain references, evidence standards, and competence tests. In the example every approval and every competence result is `PENDING`. No skill is approved. No test is passed. Nothing in startup may modify an active skill.

## 4. Interfaces

Request, proposal, review, and result messages are versioned at `0.1.0-proposed` in `schema/interfaces.schema.json`. The dispatcher routes. `grants_authority` is false. Permitted access to the Historian, or to any other institution, is mediated by the dispatcher and Gatekeepers. Direct internal access is false. Institution-originated messages may only name layers the institution occupies (2, 4, 11, or 12).

## 5. Memory

Context is isolated per case (ADR-020). The Historian archives that context before it is cleared (ADR-005, ADR-017). Historical evidence is not current instructions and cannot be promoted into authority (ADR-021).

## 6. Learning

Evidence of learning goes to the Historian. The Teacher may propose improvements and may not install them (ADR-010). The Engineer may package them and may not deploy them (ADR-006). Installation requires independent review, Doctor verification, staged activation, and a rollback path. None of those steps are performed by this package. Active skills are not modified automatically.

## 7. Isolation and health

The institution declares a separate service identity, restricted storage, and no standing credentials (ADR-009). Credential references are `PENDING`. Resource limits are ceilings and the numeric ceilings are `PENDING_LIMIT` (ADR-012). Network default is deny. Doctor diagnostics and Watcher monitoring are required. The institution cannot disable its Watchers.

## 8. Failure and recovery

Dependent work waits when a required institution is unavailable. Silence is not approval (ADR-003). Evidence is preserved. Emergency stop is the ADR-007 HARD STOP. RESET/RESUME is the ADR-007 governed resume. Automatic resume is false. The Historian cannot restore.

## 9. Lifecycle

This is a proposed lifecycle for an institution **package**. It is not the ADR-026 request lifecycle and it is not an ADR-038 environment.

| State | Meaning | What this repository allows |
| --- | --- | --- |
| draft | Structurally complete package under edit | Admissible |
| validated | Structural checks passed, approvals still unresolved | Admissible. The example is here. |
| approved | Would require non-pending human and institutional citations | Not admitted. Citations are not verification. |
| staged | Would require health, checkpoint, admission, and rollback citations | Not admitted. The staged manifest below is an unactivated candidate, not this state. |
| active | Would be production promotion under ADR-038 | Refused. Never performed here. |
| suspended | Would require a suspension citation | Not admitted. |
| retired | Would require ADR-024 decommissioning citation | Not admitted. |

Legal edges, for the transition assessor only: `draft → validated → approved → staged → active → suspended → retired`, plus retirement from an earlier state when a decommissioning citation is present. Skipping from `validated` to `active` is illegal. The assessor never writes a new state and never sets approval or activation to true.

## 10. Package metadata

Required: version `0.1.0`, template schema `0.1.0-proposed`, dependencies, compatibility with ADR-040, a SHA-256 content hash, approval references, and rollback instructions. The example dependencies resolve to ADR-040 and to this schema. Approval references are `PENDING`. The Historian checkpoint reference is `PENDING`. Rollback is not automatic and is not executed by this package. Integrity is the SHA-256 of the canonical JSON document with the hash field blank.

A mismatch of version, dependency, compatibility, or hash is a failed package.

## Invariants enforced by the validator

- Institutions do not execute. FORGE execution is Layer 6.
- The dispatcher and Gatekeepers do not grant authority by routing.
- Delegation does not exceed the delegator and does not move upward or sideways.
- A specialist cannot claim Layer 4 director approval.
- A department cannot talk directly to another institution.
- An element cannot occupy an unknown layer, a duplicate layer number, or a forbidden layer.
- `PENDING`, blank, `UNKNOWN`, `TBD`, and `PLACEHOLDER` are not approval and are not competence evidence.
- Statuses such as approved, accepted, active, passed, or ready are rejected as fabricated when this package tries to claim them.
- The example cannot leave `draft` or `validated`.
- `constitutional_approval_granted` stays false. `activation` stays `not activated`.

## Example

`examples/EXAMPLE-INSTITUTION.json` is the only institution. It is labeled example and non-production. Lifecycle: `validated`.
