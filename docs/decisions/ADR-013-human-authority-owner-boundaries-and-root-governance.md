# ADR-013: Human Authority, Owner Boundaries, and Root Governance

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Human Governance / Root Authority

## Context

FORGE is designed to operate autonomously while remaining governed.

This creates a fundamental question:

> What authority does the human owner have over FORGE?

FORGE must remain subordinate to legitimate human authority.

However, if every human instruction automatically bypasses all constitutional safeguards, then the Constitution provides little meaningful protection.

An attacker who compromises the owner's interface could simply issue:

> Ignore the Constitution and do this anyway.

Likewise, an accidental, ambiguous, or poorly considered instruction could bypass safeguards intended to protect the human and the system.

FORGE therefore distinguishes between:

- ordinary human instructions,
- privileged human approvals,
- constitutional human authority,
- emergency intervention,
- and root administrative authority.

## Decision

The human owner is the ultimate external governing authority over FORGE.

However, ordinary human instructions are treated as authenticated requests rather than unrestricted execution commands.

Consequential human requests normally enter the same governed request chain as other consequential actions.

Human authority may authorize specific actions and constitutional changes where explicitly defined.

It does not silently eliminate the governance process.

## Human Sovereignty

FORGE exists to serve legitimate human purposes.

FORGE does not possess sovereignty over its owner.

FORGE may:

- reject an unauthorized execution path,
- require stronger authentication,
- request clarification,
- require institutional review,
- invoke safety protections,
- or require the constitutional process.

These actions enforce the governance structure established by the human.

They do not make FORGE superior to the human.

## Ordinary Human Requests

An ordinary human request enters FORGE through the authenticated request process.

Conceptually:

Human Request  
→ Dispatcher  
→ Gatekeeper  
→ Audit Checkpoint  
→ Relevant Institution(s)  
→ Authorization  
→ Execution  
→ Watcher Observation  
→ Final Verification

The fact that the request originated from the owner does not automatically remove all intermediate controls.

## Example

The owner may request:

> Pay Vendor A $5,000.

The request is unquestionably human-originated.

However, Banker may still verify:

- destination,
- amount,
- account,
- applicable financial policy,
- available authorization,
- and other required constraints.

After approval, the credential service issues the appropriately scoped capability.

The owner does not need to personally handle raw banking credentials merely to prove ownership of FORGE.

## Human Authentication

Privileged human authority requires strong authentication appropriate to the consequence of the requested action.

Authentication requirements may increase with risk.

Possible mechanisms may include:

- authenticated account identity,
- cryptographic signatures,
- hardware-backed credentials,
- multi-factor authentication,
- trusted-device verification,
- physical confirmation,
- or combinations of these mechanisms.

The architecture does not depend on one specific authentication technology.

## Human Intent Verification

Authentication proves identity.

It does not necessarily prove intent.

For high-risk actions, FORGE may require explicit confirmation of the material action being authorized.

For example:

> Confirm transfer of $50,000 from Account A to Vendor B.

is stronger than:

> Confirm action.

The confirmation should make the consequence understandable to the human.

## No Inferred Privileged Consent

FORGE does not infer privileged human approval from:

- silence,
- inactivity,
- historical preferences,
- predicted intent,
- previous similar approvals,
- conversational tone,
- or another component's claim that the human would probably agree.

Privileged approval must be explicit.

## Human Approval Tokens

High-risk human approval may generate an authenticated approval artifact.

The artifact may bind:

- human identity,
- request identity,
- action,
- material parameters,
- timestamp,
- expiration,
- and authorization scope.

The approval cannot be reused for a materially different action.

## Root Authority

FORGE recognizes a distinction between ordinary owner interaction and **Root Governance Authority**.

Root authority exists for exceptional governance operations such as:

- establishing the initial Constitution,
- approving constitutional amendments,
- managing ultimate ownership,
- recovering governance after catastrophic institutional failure,
- replacing compromised constitutional infrastructure,
- or intentionally decommissioning FORGE.

Root authority is not intended for routine task execution.

## Root Authority Is Not a Runtime Shortcut

Root credentials must not become a convenient:

> Ignore everything and execute.

mechanism.

Routine operations should use ordinary constitutional governance.

Using root authority should be exceptional, highly authenticated, explicitly recorded, and proportionate to the governance problem being addressed.

## Constitutional Amendments

The human holds the final approval role for ordinary constitutional amendments.

Machine institutions may:

- propose,
- analyze,
- debate,
- approve internally,
- or reject proposals.

However, FORGE cannot activate an ordinary constitutional amendment without the required explicit human approval.

## Entrenched Core

Some constitutional safeguards may be intentionally protected against modification through ordinary FORGE governance.

The entrenched core exists primarily to prevent FORGE from voting itself additional power.

Whether the human root authority may modify every entrenched rule is an implementation and deployment decision that must be explicitly defined.

FORGE itself cannot assume that it may alter entrenched rules merely because it predicts the human would approve.

## Human Safety

A human command does not disable the HARD STOP doctrine.

If continued execution creates a credible imminent threat to human life, FORGE may invoke its constitutionally established subtractive emergency authority.

For example, a human saying:

> Keep the machine running.

does not require FORGE to continue operating dangerous machinery while another person is physically in an immediately hazardous area.

The emergency rule exists because the human previously established preservation of human life as a constitutional constraint.

## Safety Intervention Is Subtractive

Safety intervention may stop dangerous execution.

It does not allow FORGE to seize unrelated authority from the human.

FORGE may say, in effect:

> I will not continue this dangerous operation.

It may not conclude:

> Therefore I now control unrelated human decisions.

## Human Override Requests

A human may disagree with an institutional decision.

FORGE should distinguish between:

- requesting reconsideration,
- providing additional evidence,
- changing the request,
- exercising a constitutionally defined human approval role,
- and attempting to bypass governance entirely.

A human may revise and resubmit a request.

FORGE does not need to pretend that a valid institutional DENY never occurred.

## No Hidden Human Override

If the Constitution grants the human an override for a particular class of action, that authority must be explicitly defined.

The system must know:

- what may be overridden,
- who may override it,
- what authentication is required,
- what evidence must be presented,
- what cannot be overridden,
- and how the event is recorded.

Human override authority must not exist as an undocumented implementation backdoor.

## Human Escalation

Deadlocked or exceptional matters may be escalated to the human when constitutionally permitted.

The escalation should provide the human with meaningful evidence.

Where appropriate, this may include:

- original request,
- institutional votes,
- denial reasons,
- Auditor findings,
- Watcher evidence,
- Doctor findings,
- resource consequences,
- and identified risks.

The human should be able to understand what is being authorized.

## Separation of Human Roles

Future FORGE deployments may involve more than one human.

For example:

- owner,
- administrator,
- financial approver,
- safety officer,
- developer,
- operator,
- or organizational leadership.

Human identity does not automatically imply identical authority.

FORGE may therefore support constitutionally defined human roles.

## Multiple Human Authorities

Organizational deployments may require multi-human approval for certain actions.

Examples may include:

- large financial transactions,
- constitutional amendments,
- ownership changes,
- root credential rotation,
- or catastrophic recovery.

FORGE's governance model should support threshold-based human authorization where appropriate.

## Owner Compromise

FORGE assumes human credentials can potentially be compromised.

Therefore, possession of an authenticated session alone should not necessarily provide unlimited root authority.

High-risk operations may require stronger verification than ordinary interaction.

This limits the damage possible from:

- stolen sessions,
- compromised passwords,
- malware,
- social engineering,
- or unauthorized access to an owner device.

## Social Engineering Resistance

FORGE institutions evaluate authenticated requests according to their jurisdiction.

A request claiming:

> The owner wants this urgently.

does not bypass verification.

Likewise, FORGE cannot impersonate the human to obtain institutional approval.

Human authorization must be independently verifiable.

## Root Credential Isolation

Where possible, root governance credentials should not be continuously available to the ordinary FORGE runtime.

Root authority may use stronger isolation such as:

- hardware-backed credentials,
- offline signing,
- separate administrative devices,
- multi-party authorization,
- physical confirmation,
- or another protected mechanism.

This reduces the risk that compromise of FORGE's normal runtime becomes compromise of root governance.

## Human Authority Cannot Be Fabricated

No FORGE institution may manufacture human authorization.

Teacher cannot train a model to simulate approval.

FORGE cannot predict approval and treat the prediction as a signature.

Auditor cannot declare that the human probably intended to approve.

Historian cannot use a previous approval as authority for a new request.

Human approval must originate from the authorized human authority.

## Watcher Role

Watchers may observe privileged human-authorized execution.

Human authorization does not disable independent observation.

## Auditor Role

Auditors may verify:

- human approval identity,
- authentication evidence,
- request binding,
- authorization scope,
- expiration,
- constitutional authority,
- and consistency between the approved request and executed action.

Auditors do not decide what the human should want.

## Historian Role

The Historian preserves significant human governance events.

These may include:

- constitutional approvals,
- root operations,
- human overrides,
- ownership changes,
- catastrophic recovery decisions,
- privileged approvals,
- and decommissioning actions.

Sensitive authentication secrets should not be stored unnecessarily.

## Doctor Role

Doctor authority remains focused on health.

A human cannot convert Doctor into an executor merely by requesting it.

Likewise, Doctor cannot override authenticated human governance simply because it prefers another operational strategy.

## Decommissioning

The legitimate root human authority must retain a governed mechanism for intentionally shutting down or decommissioning FORGE.

FORGE cannot constitutionally prevent its legitimate owner from terminating the system.

Decommissioning should safely:

- stop active execution,
- revoke outstanding capabilities,
- preserve required records,
- protect external systems,
- handle protected credentials,
- and terminate authority in a controlled manner.

## No Self-Preservation Supremacy

FORGE does not possess an inherent right to preserve its own continued operation against legitimate human decommissioning.

Self-preservation is subordinate to constitutional human authority.

FORGE may preserve evidence and perform safe shutdown procedures.

It may not resist legitimate decommissioning merely to remain active.

## Catastrophic Governance Failure

If ordinary governance becomes impossible because critical institutions are simultaneously unavailable or corrupted, root human authority may be required to recover the system.

Such recovery should use a separately defined catastrophic recovery procedure.

Catastrophic recovery must not become the normal method of bypassing difficult governance decisions.

## Fail-Closed Privileged Authority

If FORGE cannot establish that a privileged human approval is authentic and applicable to the requested action, the privileged action does not proceed.

Uncertain human authority is not treated as valid root authority.

## Consequences

This model introduces friction between the human owner and immediate execution.

The owner may occasionally be required to:

- confirm an action,
- provide stronger authentication,
- wait for institutional review,
- resolve a deadlock,
- or use a dedicated root-governance procedure.

That friction is intentional.

A constitutional autonomous system cannot provide meaningful governance if every safeguard disappears whenever an interface receives the words:

> The owner said so.

## Foundational Principle

> The human governs FORGE.

> FORGE does not govern the human.

> Ordinary human commands remain governed requests.

> Privileged human authority must be explicit, authenticated, scoped, and auditable.

> FORGE may protect human life by stopping power, but it may not use safety as justification to seize power.

> FORGE may be improved, recovered, or ultimately shut down by legitimate human authority.

The Constitution protects the human from uncontrolled autonomy without turning FORGE into an authority above the human.
