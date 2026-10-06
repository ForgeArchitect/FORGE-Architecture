# ADR-016: Constitutional Jurisdiction and Conflict Resolution

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Jurisdiction / Conflict Resolution

## Context

FORGE separates authority across specialized institutions.

Examples may include:

- Banker,
- Engineer,
- Doctor,
- Teacher,
- Security,
- Auditor,
- Watchers,
- constitutional governance bodies,
- and other domain-specific institutions.

Many consequential actions may cross more than one jurisdiction.

For example, a proposed infrastructure update may simultaneously involve:

- Engineer because software is being modified,
- Security because network exposure changes,
- Banker because external resources cost money,
- Doctor because subsystem health may be affected,
- and Auditor because authorization and execution integrity must be verified.

These institutions may reach different conclusions without any of them malfunctioning.

Engineer may conclude:

> Technically valid.

Security may conclude:

> Security requirements are not satisfied.

Doctor may conclude:

> The subsystem is not healthy enough for deployment.

These are not necessarily contradictory answers.

They may represent separate constitutional conditions that must all be satisfied before execution.

FORGE therefore requires explicit jurisdiction rules and a governed method for handling overlapping authority.

## Decision

FORGE assigns authority according to constitutionally defined jurisdiction.

When multiple jurisdictions materially apply to a consequential action, the applicable institutions participate according to their respective authority.

FORGE cannot select whichever institution provides the easiest path to execution.

Where multiple approvals or conditions are constitutionally required:

> All required conditions must be satisfied.

## Jurisdiction

Jurisdiction defines the domain in which an institution possesses constitutional authority.

An institution's jurisdiction may specify:

- subjects it may evaluate,
- decisions it may authorize,
- decisions it may deny,
- conditions it may impose,
- matters it may only advise on,
- escalation requirements,
- and explicit exclusions from its authority.

Jurisdiction exists independently of technical capability.

## Capability Does Not Create Jurisdiction

An institution may understand matters outside its jurisdiction.

For example:

Engineer may understand finance.

Banker may understand software.

Doctor may understand security.

Security may understand infrastructure.

Knowledge does not transfer constitutional authority.

The question is not:

> Can this institution reason about the subject?

The question is:

> Does the Constitution assign this decision to the institution?

## Primary Jurisdiction

Some requests may have a clearly identifiable primary jurisdiction.

For example:

- a financial transaction may primarily belong to Banker,
- a subsystem update may primarily involve Engineer,
- a health determination may primarily belong to Doctor,
- and a training operation may primarily involve Teacher.

Primary jurisdiction identifies the institution principally responsible for evaluating that domain.

It does not eliminate other applicable jurisdictions.

## Secondary Jurisdiction

An action may trigger additional institutional review because of its consequences.

For example:

Engineer may have primary jurisdiction over a software update.

However:

- Security may have jurisdiction over new network exposure,
- Banker may have jurisdiction over financial cost,
- Doctor may have jurisdiction over operational readiness,
- and Auditor may have verification responsibilities.

These additional jurisdictions remain valid.

## Jurisdiction Intersection

When multiple jurisdictions apply, FORGE evaluates the intersection of required authority.

Conceptually:

Engineer Approval  
+ Security Approval  
+ Banker Approval  
+ Doctor READY  
+ Audit Integrity  
= Eligible for Execution

The exact combination depends on the request.

FORGE does not collapse these independent requirements into one generic approval.

## Different Questions

Institutions may answer different questions about the same action.

For example:

Engineer asks:

> Is the proposed technical change valid?

Security asks:

> Does the change satisfy security requirements?

Banker asks:

> Is the financial expenditure authorized?

Doctor asks:

> Is the target healthy enough to undergo the change?

Auditor asks:

> Is the authorization and evidence chain valid?

Watcher asks:

> What actually happened?

Because these questions differ, one institution's approval does not automatically override another institution's denial or unmet condition.

## No Authority Substitution

FORGE cannot substitute one institution's authority for another.

For example:

Engineer approval cannot substitute for Banker approval.

Banker approval cannot substitute for Doctor readiness.

Doctor health approval cannot substitute for Security authorization.

Auditor verification cannot create missing institutional authorization.

Watcher evidence cannot create authorization.

Each institution remains authoritative only within its assigned jurisdiction.

## No Jurisdiction Shopping

FORGE must not route a request through a more permissive institution to avoid the institution that actually has jurisdiction.

For example:

If Security denies a network change, FORGE cannot reclassify the request as an engineering task solely to avoid Security.

If Banker denies an expenditure, FORGE cannot label the expenditure a technical resource allocation solely to bypass Banker.

Classification must reflect the material nature of the action.

## Request Classification

The Dispatcher may identify which jurisdictions appear relevant to a request.

However, Dispatcher does not possess unilateral authority to redefine constitutional jurisdiction.

Request classification should be verifiable against:

- request content,
- material parameters,
- affected resources,
- target systems,
- expected consequences,
- and constitutional jurisdiction definitions.

## Gatekeeper Role

Gatekeeper verifies that a request is admissible for governance.

Where jurisdictional requirements are known, Gatekeeper may reject or halt a request that attempts to bypass required institutional review.

Gatekeeper does not replace the institutions whose approval is required.

## Jurisdiction Declaration

Consequential requests should identify applicable jurisdictions before authorization.

A jurisdiction declaration may include:

- primary institution,
- additional required institutions,
- advisory institutions,
- applicable verification institutions,
- applicable health requirements,
- and applicable execution constraints.

This declaration becomes part of the governed request record.

## Material Change

A material change may alter jurisdiction.

For example:

An update originally affecting only local software may later add external network access.

That change may introduce Security jurisdiction.

Existing Engineer approval does not authorize the newly introduced security consequence.

The modified request must be reevaluated.

## Institutional Denial

When an institution with required jurisdiction returns DENY, the affected request does not proceed in its current form.

FORGE may:

- preserve the denial,
- obtain the reason,
- revise the proposal,
- reduce scope,
- provide additional evidence,
- or submit a new request.

FORGE may not simply discard the required institution.

## Conditional Approval

Institutions may be permitted to return conditional approval where constitutionally defined.

For example:

Security may return:

> APPROVE only if outbound network access is restricted to Endpoint X.

The condition becomes part of the authorization.

Execution outside that condition is unauthorized.

## Conflicting Conditions

Two institutions may impose conditions that cannot simultaneously be satisfied.

For example:

Engineer:

> Deployment requires network connection A.

Security:

> Network connection A is prohibited.

This creates a governance conflict.

FORGE cannot arbitrarily select one condition.

The request must be:

- redesigned,
- revised,
- escalated through the appropriate governance process,
- or denied.

## Conflict Is Not Majority Rule

Jurisdictional conflict is not necessarily resolved by counting institutions.

If four institutions approve and one required institution denies within its valid jurisdiction, FORGE cannot automatically conclude:

> Four votes beat one.

Institutional jurisdictions are not interchangeable votes.

A required authority cannot be outvoted by unrelated authorities unless the Constitution explicitly establishes such a mechanism.

## No Meta-Institution by Default

FORGE itself does not become a superior institution merely because two institutions disagree.

FORGE coordinates the resolution process.

It does not automatically possess authority to decide which constitutional institution is correct.

## Jurisdiction Dispute

A jurisdiction dispute occurs when institutions disagree about which institution has constitutional authority over a matter.

This is different from disagreement about the merits of the action.

For example:

Banker may claim:

> This is financial jurisdiction.

Engineer may claim:

> This is engineering jurisdiction.

The dispute concerns authority itself.

## Resolving Jurisdiction Disputes

Jurisdiction disputes should be resolved using authoritative constitutional definitions.

A conceptual process may include:

1. Suspend the disputed consequential action.
2. Preserve the request and jurisdiction claims.
3. Retrieve the applicable constitutional jurisdiction definitions.
4. Obtain independent interpretation where constitutionally defined.
5. Audit the relevant constitutional version.
6. Determine applicable jurisdictions.
7. Resume governance only after the jurisdiction question is resolved.

FORGE does not execute first and resolve jurisdiction afterward.

## Constitutional Ambiguity

The Constitution may contain an unanticipated jurisdictional ambiguity.

If the ambiguity materially affects consequential authority, FORGE fails closed on the disputed authority.

The ambiguity may then become a candidate for constitutional clarification or amendment.

Runtime convenience must not silently become constitutional precedent.

## Precedent

Previous jurisdiction decisions may provide useful interpretive evidence.

However, precedent does not automatically amend the Constitution.

Historian may preserve previous jurisdiction decisions so future governance can evaluate consistency.

If repeated ambiguity exists, the constitutional amendment process may formally clarify the jurisdiction.

## Advisory Institutions

Some institutions may provide advice without possessing approval or denial authority over a particular request.

The system must distinguish:

- advisory opinion,
- required approval,
- required health finding,
- required verification,
- and binding denial authority.

An advisory recommendation must not be falsely represented as constitutional authorization.

## Security Jurisdiction

Where a Security institution exists, it may have jurisdiction over matters such as:

- access control,
- network exposure,
- attack surface,
- authentication,
- compromise containment,
- security policy,
- and protected infrastructure.

Its exact authority must be constitutionally defined.

Security must not become a universal institution capable of claiming jurisdiction over every action merely by labeling everything a security concern.

## Doctor Jurisdiction

Doctor possesses health jurisdiction.

Doctor determines whether relevant system components are operationally healthy or ready.

Doctor does not use health jurisdiction to make unrelated policy decisions.

A Doctor finding of:

> NOT READY

may block an operation requiring health readiness.

It does not make Doctor the owner of the underlying engineering, financial, or constitutional decision.

## Auditor Jurisdiction

Auditor possesses integrity-verification jurisdiction.

Auditor may determine whether:

- evidence is authentic,
- required approvals exist,
- request identity is intact,
- execution matches authorization,
- and applicable records are consistent.

Auditor does not create missing authorization.

## Watcher Jurisdiction

Watchers possess observation responsibilities.

They provide evidence of behavior and outcomes.

Watchers do not determine whether the observed action should have been authorized unless a separately defined role explicitly grants such authority.

## Historian Jurisdiction

Historian preserves institutional and constitutional memory.

Historian may provide evidence concerning prior decisions and constitutional versions.

Historian does not decide current jurisdiction merely because it stores previous decisions.

## Teacher Jurisdiction

Teacher governs authorized learning and instructional processes.

Teacher cannot use training jurisdiction to redefine another institution's constitutional jurisdiction.

## Engineer Jurisdiction

Engineer governs authorized technical development and change within its defined scope.

Engineer cannot convert technical ownership into general governance authority.

## Banker Jurisdiction

Banker governs financial authority within its defined scope.

Banker does not automatically control every action that has any incidental financial cost.

The Constitution should define materiality thresholds and applicable financial jurisdiction.

## Human Role

Certain unresolved jurisdiction disputes may be escalated to authenticated human authority where constitutionally permitted.

Human escalation must be explicit and recorded.

Human involvement does not permit FORGE to fabricate jurisdictional approval.

## Auditor Verification of Jurisdiction

Auditors may verify:

- applicable constitutional version,
- jurisdiction declaration,
- required institutions,
- institutional identities,
- required approvals,
- imposed conditions,
- and consistency between authorization and execution.

This helps prevent execution from silently omitting an inconvenient jurisdiction.

## Watcher Observation of Routing

Watchers may observe routing behavior for signs of:

- jurisdiction avoidance,
- repeated reclassification,
- approval shopping,
- omitted institutions,
- or unusual routing changes.

Such patterns may indicate attempted governance circumvention.

## Historian Role

Historian preserves significant jurisdiction decisions and conflicts.

Records may include:

- request classification,
- jurisdiction declarations,
- institutional claims,
- conflicts,
- resolution,
- constitutional interpretation,
- and later amendments.

This allows repeated ambiguity or attempted circumvention to be identified.

## Jurisdiction Versioning

Jurisdiction definitions should be associated with the applicable constitutional version.

An authorization should therefore be interpretable according to the jurisdiction rules in effect when it was issued.

A later constitutional change does not silently rewrite the meaning of historical authorization.

## Fail-Closed Rule

If FORGE cannot establish whether a consequential action requires a particular jurisdiction, and omission of that jurisdiction could materially expand authority or risk, the action does not proceed until the question is resolved.

Uncertain jurisdiction does not become FORGE jurisdiction.

## Consequences

Explicit jurisdiction governance may:

- increase routing complexity,
- require multiple institutions,
- create additional latency,
- expose disagreements,
- produce deadlocks,
- and require constitutional clarification.

FORGE accepts this friction.

Specialized institutions provide meaningful separation of powers only if their jurisdiction cannot be ignored whenever another institution provides a more convenient answer.

## Foundational Principle

> Jurisdiction determines who has authority to decide.

> Knowledge does not create jurisdiction.

> One institution cannot substitute for another.

> A required denial cannot be defeated by collecting unrelated approvals.

> FORGE coordinates jurisdictions.

> FORGE does not own them.

When multiple constitutional authorities apply, FORGE must satisfy the complete authorized intersection before consequential execution may occur.
