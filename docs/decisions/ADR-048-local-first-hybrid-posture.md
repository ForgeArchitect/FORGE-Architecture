# ADR-048: Local-First Hybrid Posture

**Status:** Proposed
**Date:** 2026-10-09
**Source decision queue:** DQ-022
**Related canonical ADRs:** ADR-001, ADR-019, ADR-027, ADR-028, ADR-033, ADR-038, ADR-040
**Constitutional approval:** Pending

## Context

ADR-028 allows more than one FORGE deployment and treats each deployment as its own trust domain unless a governed federation says otherwise. Remote authority does not become local authority. ADR-019 governs external tools and services, including cloud services, as untrusted capabilities outside the constitutional boundary. ADR-033 requires consequential capability to pass a local enforcement point. ADR-038 separates environments and governs production promotion. ADR-040 does not choose a local-first deployment doctrine.

DQ-022 proposes that FORGE is local first, that cloud specialists may be added later, and that a cloud specialist has no direct local execution authority. No local runtime and no cloud specialist are implemented in this repository. This ADR is a deployment posture proposal, not a claim that a personal device, edge node, or cloud worker exists today.

## Problem

A cloud model or specialist that can call local tools directly becomes a second executor outside the local constitutional process. Convenience of hosted inference would then concentrate execution authority off the machine that holds the owner's governed FORGE.

## Proposed decision

1. The authoritative FORGE for a deployment is the local constitutional process: local institutions' governance, local policy enforcement, and the local FORGE execution process for consequential actions that affect that deployment.
2. Cloud specialists are optional and later. They are external capabilities under ADR-019 or remote FORGE deployments under ADR-028. They are not assumed present.
3. A cloud specialist may propose analysis, drafts, or other results. It may not directly invoke local consequential tools, credentials, or actuators. Local execution occurs only after the local authenticated request chain and local enforcement accept the action.
4. Cloud possession of a copy of context, a tool description, or a suggested command is not local authorization. ADR-009 and ADR-021 apply.
5. Federation, if configured, still requires authorization in each affected domain under ADR-028. A cloud FORGE does not inherit the local deployment's authority by being called a specialist.
6. Production use of any cloud specialist is a production-promotion and external-tool decision under ADR-038 and ADR-019. This ADR does not promote any cloud service into production.

"Local" means the trust domain that holds the authoritative FORGE enforcement boundary for that deployment. It does not mean a specific vendor, operating system, or hardware design. Those choices are open.

## Alternatives considered

- Leave deployment location unspecified, which is the ADR-040 baseline. Acceptable if the owner rejects this ADR. It was not selected as the proposal because the queue asks to freeze a local-first posture before cloud specialists exist.
- Run consequential execution in the cloud and treat the local device as a terminal. Rejected as the proposal because it gives the cloud path direct effect on local authority, which is the outcome DQ-022 refuses.
- Prohibit cloud specialists permanently. Rejected as the proposal. The queue allows them later, under the execution limit above. The owner may still prohibit them.

## Jurisdiction and authority boundaries

Local institutions retain their jurisdictions. A cloud specialist is not a member of those institutions unless admitted through ADR-015, which this ADR does not do.

The cloud specialist has no Dispatcher, Gatekeeper, or Executor role for the local deployment. Local Dispatcher and Gatekeeper remain the ingress and admissibility path for local consequential requests. ADR-002 applies.

Delegated cloud work is attenuated under ADR-027. The delegate cannot widen scope or call back into local execution tools.

## Security and privacy

Data sent to a cloud specialist is an external disclosure under ADR-020 and ADR-019. Default posture is to send the minimum context required for the requested analysis, and only when that disclosure is itself authorized.

Cloud specialists do not receive standing local credentials. ADR-009 applies.

A cloud outage or a malicious cloud response fails closed for consequential local action. The local system does not execute a cloud suggestion merely to preserve availability. ADR-011 applies.

## Failure modes

- The cloud specialist returns an imperative tool call and the local runtime executes it without the local chain. Required response: treat that path as a constitutional bypass under ADR-033 and ADR-039.
- Local enforcement is moved to the cloud "for consistency," leaving the device unable to refuse. That move is outside this proposal and would be a new architecture decision.
- Shared cloud tenancy is treated as the same trust domain as the local owner. ADR-028 independence and ADR-020 multi-principal isolation still apply.
- A cloud specialist retains local context and reuses it for another principal or another request. That reuse is an external-data violation, not a local authorization.

## Invariants and tests

These invariants are proposed and have not been executed in this repository. No local agent runtime or cloud specialist is present to test.

- Consequential local effects are produced only by the local FORGE execution path after local authorization.
- A cloud-originated tool invocation cannot reach a local capability except through that path.
- Absence of the cloud specialist leaves local governance able to refuse consequential actions it cannot authorize locally.
- Tests to require before any later acceptance: cloud response containing a tool call; cloud response containing stolen-looking owner instructions; attempted cloud use of a local credential; operation during cloud unavailability.

## Compatibility with frozen baseline

This proposal chooses a deployment posture ADR-040 left open. It relies on ADR-019, ADR-027, ADR-028, and ADR-033 and does not amend them. Organizational and multi-instance deployments in ADR-028 remain valid. This ADR does not say that only a personal device may run FORGE. DQ-023's exclusive personal-ownership reading is a separate open conflict and is not decided here.

## Open questions

- What hardware and offline behavior "local" requires when the local process itself is distributed across a household or a site.
- Which analysis tasks may leave the local boundary, and at which ADR-032 tiers disclosure is forbidden.
- How a later cloud specialist is identified, contracted, and removed.
- How this posture relates to ADR-038 environment promotion when the local process is both the development environment and the production authority.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The decision-queue source is a conversation candidate, not a ratification record
- No local-first runtime and no cloud specialist are implemented in this repository
