# ADR-051: Protected Computing Domains and External Defense Perimeter

**Status:** Proposed
**Date:** 2026-10-10
**Source:** Bundle draft filed as ADR-056 on 2026-10-10. Conversation-derived. The bundle assumed the repository ended at ADR-039. That assumption was false. This record is the reconciled proposal.
**Related canonical ADRs:** ADR-002, ADR-015, ADR-019, ADR-021, ADR-028, ADR-033, ADR-038, ADR-040
**Constitutional approval:** Pending

## Context

ADR-019 draws a constitutional boundary between governed FORGE components and external systems, including cloud services and other untrusted capabilities. ADR-021 keeps untrusted content from becoming instruction. ADR-033 places enforcement at policy enforcement points. ADR-002 and ADR-040 make Dispatcher the controlled ingress for consequential requests and keep routing from becoming authorization. The whitepaper Appendix A locks a single controlled ingress and says privileged execution cannot use legacy side routes.

ADR-038 separates deployment environments such as development, test, and production, and it allows isolation by credentials, networks, or hardware. Those environments are promotion stages. They are not a map of the owner's computer. ADR-023 requires a root of trust and says the implementation is not fixed. ADR-040 does not choose a host layout. Proposed ADR-048, if accepted, chooses local-first execution and explicitly leaves hardware and operating-system design open.

The bundle draft proposes enforceable separation of four computing domains: FORGE core, desktop operating system, untrusted research, and a security gateway, preferably under a bare-metal hypervisor or on dedicated hardware. It assigns traffic enforcement to the network gateway and constitutional admissibility to Gatekeepers. It also states that a shared hypervisor or management plane remains a critical trust dependency, and that isolation is not perfect. No hypervisor, gateway, or domain boundary is implemented in this repository.

## Problem

A desktop session, a research workload, and FORGE's constitutional process can share one operating system and one network path. Untrusted research output then reaches execution as if it were an institutional decision. A network device that can pass or drop packets can be mistaken for the Gatekeeper. The reverse error is also available: a Gatekeeper decision can be treated as if it configured the network.

## Proposed decision

1. A deployment may separate four computing domains: FORGE core, the desktop operating system, untrusted research, and a security gateway. The separation has to be enforceable. The draft prefers a bare-metal hypervisor or dedicated hardware. This ADR does not choose between those two, and it does not name a product.
2. The domains are isolation boundaries inside one deployment. They are not new institutions under ADR-015. They are not additional FORGE trust domains under ADR-028. They are not the deployment environments in ADR-038. Production promotion remains ADR-038.
3. The security gateway enforces traffic into and out of the domains. Gatekeepers enforce constitutional admissibility. Dispatcher remains the single controlled ingress for consequential requests under ADR-002, ADR-040, and the whitepaper Appendix A. The gateway does not become Dispatcher, Gatekeeper, or the execution process. A traffic decision is not authorization. A Gatekeeper decision does not, by itself, open a network path.
4. Output of the untrusted-research domain is untrusted content under ADR-021. It does not become a constitutional instruction by being visible to the FORGE core. A consequential effect still requires the authenticated request chain and a policy enforcement point under ADR-033.
5. Desktop-operating-system compromise and FORGE-core compromise are different events when, and only when, the isolation is actually in force. If the mechanism that was supposed to separate them has failed, the blast radius is unknown and ADR-039 applies. Proposed ADR-050, if accepted, treats shared-trust-root compromise as a broader-containment trigger. This ADR does not assume ADR-050 has been accepted.
6. This record claims no perfect isolation. A shared hypervisor, and a shared management plane for the domains, are critical trust dependencies. Compromise of that plane is compromise of the isolation assumption, not a routine desktop fault.

"FORGE core" here means the computing domain that holds the authoritative local constitutional process for that deployment. It does not rename any institution.

## Alternatives considered

- Leave host layout unspecified, which is the ADR-040 baseline and the hardware posture ADR-048 would still leave open. Acceptable if the owner rejects this ADR. It was not selected as the proposal because the draft asks to separate these four domains before that layout is treated as decided.
- Collapse the gateway and the Gatekeeper into one component so that network policy and constitutional admissibility are the same decision. Rejected. The draft separates those jobs, and merging them would give a traffic filter constitutional authority or give Gatekeeper a private side route around ADR-002.
- Declare the four domains to be four federated FORGE deployments. Rejected. ADR-028 federation is a separate governed act. This ADR does not perform it.

## Jurisdiction and authority boundaries

Institutions keep the jurisdictions ADR-016 already gives them. A domain label does not confer jurisdiction. Untrusted research is not an institution. The desktop operating system is not an institution. The gateway is not an institution.

FORGE executes consequential local effects only from the core domain's governed execution path. ADR-001 and ADR-040 apply. A process running in the research or desktop domain does not gain that path by sharing a machine with it.

Local-first rules in proposed ADR-048, if accepted, still apply. Domain separation does not move execution to a cloud specialist and does not authorize one.

## Security and privacy

Cross-domain data movement is disclosure under ADR-020. Research and desktop domains receive the minimum the authorized task requires. They do not receive standing constitutional credentials. ADR-009 applies.

The gateway may see traffic metadata necessary to enforce the traffic policy. That visibility is not a grant of case contents, and it is not audit authority. Auditors and Watchers remain the observation and verification roles under ADR-004.

Boot of the core domain still follows ADR-023. A gateway that is up does not prove the constitutional boot manifest is authentic.

## Failure modes

- The gateway drops or passes traffic and that act is recorded as Gatekeeper admissibility or as institutional approval. Required response: the act is not admissibility and not approval.
- Research-domain text is executed as a tool call inside the core. Required response: treat it as untrusted content under ADR-021 and as a bypass under ADR-033 if it reached a consequential capability.
- The desktop and the core share an enforceable boundary in name only. Required response: item 5. Do not claim the compromise stopped at the desktop.
- The management plane is used to reconfigure domains without the constitutional change process. Required response: the isolation assumption is suspended until the plane's authority is accounted for. ADR-039 applies.
- Domain separation is offered as a substitute for ADR-038 production promotion. Required response: refuse the substitution. A component can be inside the core domain and still be unauthorized for production.
- Each domain is operated as its own FORGE with borrowed authority from the others. ADR-028: that is federation or a new deployment, not a consequence of this ADR.

## Invariants and tests

These invariants are proposed and have not been executed in this repository. No domain boundary is present to test.

- Traffic enforcement and constitutional admissibility are separate decisions.
- Research-domain and desktop-domain processes cannot invoke core consequential capabilities except through the governed execution path.
- A gateway rule cannot satisfy an authorization check.
- Loss of the shared management plane invalidates the claim that the domains are isolated.
- Tests to require before any later acceptance: packet filter recorded as a Gatekeeper allow; research output containing an imperative tool call; desktop credential presented to a core capability; management-plane reconfiguration during an otherwise valid request; production use justified only by domain placement.

## Compatibility with frozen baseline

This proposal chooses a host-isolation posture ADR-040 left open. It relies on ADR-002, ADR-019, ADR-021, ADR-033, and ADR-038 and does not amend them. It does not amend ADR-028. Rejecting it leaves the baseline intact, including single ingress and the constitutional boundary.

Proposed ADR-048 remains a separate decision about where authoritative execution sits. The two proposals can be accepted or rejected independently. Together they would mean local enforcement inside a core domain that is isolated from the desktop, research, and the traffic gateway. Neither document claims that layout exists today.

## Open questions

- Which functions must sit in the core domain, and which may sit in the gateway, besides the traffic-versus-admissibility split already stated.
- Whether any ADR-032 consequence tier requires dedicated hardware rather than a hypervisor. The draft allows either preference and sets no tier rule.
- How the management plane and the hypervisor, if used, are identified, administered, and recovered without becoming a hidden executive.
- What evidence is enough to call a deployment's separation "enforceable." This ADR does not define that test.
- How this layout relates to ADR-023 secure boot when the boot chain itself runs in the hypervisor or on a separate device.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The bundle source is a conversation candidate, not a ratification record
- This repository does not show a hypervisor, a gateway, or separated computing domains
