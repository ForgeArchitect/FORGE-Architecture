# ADR-046: Institutional Tool Manifests

**Status:** Proposed
**Date:** 2026-10-09
**Revision:** 2026-10-10 bundle reconciliation. The exact change is in the approval record.
**Source decision queue:** DQ-020. Bundle draft filed as ADR-053 on 2026-10-10 is the same manifest decision and is reconciled here.
**Related canonical ADRs:** ADR-006, ADR-009, ADR-012, ADR-019, ADR-026, ADR-032, ADR-033, ADR-036, ADR-037, ADR-040
**Constitutional approval:** Pending

## Context

ADR-019 requires external tools to be registered before privileged use. A tool definition may identify identity, provider, operations, credentials, jurisdiction, risk, resource limits, data boundaries, side effects, reversibility, and Watcher coverage. Discovering a tool does not authorize it. ADR-009 separates credentials from authorization. ADR-033 places enforcement at policy enforcement points rather than in an agent's willingness to comply. ADR-006 and ADR-036 give Doctor and governance-health functions a role in operational health, without giving Doctor unilateral repair authority.

DQ-020 extends the declaration duty from external tools to every institution: declared tool manifests, permissions, validation, evidence output, and health checks. The baseline does not state that every institution's internal tools carry such a manifest. This repository has no tool registry and no health-check implementation.

## Problem

An institution can reach a consequential capability through an internal helper, library, or connector that never passed the external-tool registration in ADR-019. The helper then becomes an undeclared execution path. Health of that path can also be invisible to Doctor and to ADR-036 observability.

## Proposed decision

Every institution that can invoke a tool, connector, or other consequential capability maintains a declared manifest for that capability before use.

A manifest identifies, at a minimum:

- capability identity and version,
- owning institution,
- permitted operations,
- permission and credential references under ADR-009,
- validation method,
- evidence the capability must emit when used,
- health-check definition,
- jurisdiction, risk tier input, data boundaries, and resource bounds sufficient for ADR-012, ADR-019, ADR-020, and ADR-032.

Use of an unmanifested consequential capability fails closed at the enforcement boundary in ADR-033.

A manifest is a declaration. It is not authorization to invoke the capability. Invocation still requires the authenticated request chain, applicable institutional decisions, and a policy enforcement point.

Validation evidence and health-check results are evidence. A simulation of a capability is evidence under ADR-037. A passing simulation is not proof of real-world safety and is not authorization to invoke the capability. ADR-032's simulation boundary still applies: a simulation with real side effects is not observational. Doctor may report health. Doctor does not disable or replace a capability by fiat, and does not execute repairs. ADR-006 applies. Failed health restricts or suspends use through the ordinary containment and degraded-operation rules in ADR-011 and ADR-039.

Manifest changes that materially change permissions, reach, or risk invalidate prior authorization to invoke the old manifest, under ADR-002 and ADR-018.

## Alternatives considered

- Limit manifests to external tools, as ADR-019 already requires. Rejected as the proposal because internal helpers are a practical bypass of that boundary. The owner may still reject the extension. ADR-019 would remain in force either way.
- Treat a complete manifest as permission to call the tool. Rejected because it would collapse registration into authorization, which ADR-019 already forbids for external tools.
- Let each institution self-certify its manifest with no independent evidence. Rejected for consequential capabilities. Evidence output and independent observation follow ADR-004, ADR-017, and ADR-019 where risk warrants.

## Jurisdiction and authority boundaries

The owning institution declares the capabilities it uses inside its jurisdiction. Declaration does not extend that jurisdiction. Engineer may build or package a capability and still may not authorize its consequential use. ADR-006 applies.

Gatekeeper and policy enforcement points enforce the presence of a valid manifest. They do not gain the tool's authority. Dispatcher routing to a tool is not authorization. ADR-002 applies.

Historian may preserve manifest versions and health history. Historian does not approve a tool by storing the manifest.

## Security and privacy

Manifests list permission references rather than raw secrets. ADR-009 applies. Data boundaries on the manifest are enforceable limits under ADR-020, not advisory text.

A compromised tool is contained under ADR-019 and ADR-039, including suspension of authority delegated through it. The manifest makes the blast radius enumerable. It does not, by itself, remove the compromise.

## Failure modes

- A capability is invoked with no manifest or with a stale manifest. The enforcement point denies the invocation.
- A manifest declares narrower permissions than the underlying integration actually has. Required response: the integration is non-conformant and is not cleared for consequential use until the effective permission and the manifest match.
- Health checks pass while evidence output is missing. The capability is not treated as healthy for consequential use.
- An institution adds operations to a manifest during an in-flight request. The in-flight authorization is not silently widened.

## Invariants and tests

These invariants are proposed and have not been executed in this repository.

- Consequential invocation of an unmanifested capability is denied.
- A manifest hash or version is part of the evidence for the invocation.
- Raw credentials do not appear in manifest documents.
- Health failure cannot be overridden by the owning institution's desire to proceed.
- Tests to require before any later acceptance: call an internal helper with no manifest; widen a manifest after authorization; invoke a tool whose live credentials exceed the manifest; suppress evidence output and confirm the invocation is not accepted as complete.

## Compatibility with frozen baseline

External-tool rules in ADR-019 remain authoritative for external systems. This proposal extends the declaration duty to institutional capabilities that ADR-019 does not expressly cover. It does not weaken external-tool registration, credential isolation, or enforcement points. If this proposal is rejected, ADR-019 still governs external tools.

## Open questions

- The threshold at which an internal function is a "tool" that needs a manifest, as opposed to ordinary library code with no consequential effect.
- Who may approve a manifest for use in production. ADR-038 production promotion is implicated and is not replaced here.
- How often health checks run, and which failures force ADR-011 degraded operation versus ADR-039 containment.
- Whether Watcher coverage is mandatory for every manifest or only above a consequence tier.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

2026-10-10 revision, from the bundle draft numbered ADR-053: simulations are recorded as ADR-037 evidence, not as proof of real-world safety and not as invocation authority. The manifest duty itself is unchanged. No accepted ADR was edited.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The decision-queue source is a conversation candidate, not a ratification record
- This repository does not show a tool manifest registry or a health-check implementation
