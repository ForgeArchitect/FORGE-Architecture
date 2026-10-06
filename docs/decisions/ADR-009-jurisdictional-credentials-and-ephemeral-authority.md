# ADR-009: Jurisdictional Credentials and Ephemeral Execution Authority

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Security / Credential Governance

## Context

FORGE may eventually interact with privileged external systems such as:

- financial accounts,
- cloud infrastructure,
- business systems,
- private databases,
- communication services,
- physical devices,
- administrative systems,
- and other protected resources.

A conventional autonomous agent may be given permanent API keys, passwords, tokens, or account credentials.

That creates a dangerous concentration of authority.

If FORGE possesses standing credentials, compromising FORGE may immediately provide access to every system represented by those credentials.

It also allows possession of a credential to become equivalent to authorization.

FORGE rejects this model.

Possessing the technical ability to perform an action must not automatically mean the action is constitutionally authorized.

## Decision

FORGE does not maintain a universal vault of unrestricted credentials available to the central execution process.

Privileged access is divided according to institutional jurisdiction.

The institution responsible for a jurisdiction participates in authorization of access to protected resources within that jurisdiction.

After the required authorization chain is satisfied, the credential system may issue a narrowly scoped, temporary capability permitting only the approved operation.

FORGE receives the capability necessary to perform the authorized action.

It does not receive unrestricted permanent authority over the underlying account.

## Jurisdictional Credential Services

Protected resources are associated with credential services appropriate to their jurisdiction.

Examples may include:

- Banker → financial systems,
- Security → protected security infrastructure,
- Engineer → approved engineering infrastructure,
- communications institution → protected communication systems,
- or other constitutionally defined relationships.

This does not mean an individual institutional member receives raw credentials.

The institution governs authorization to the credential service.

## No Universal Master Key

FORGE must not accumulate a universal credential set that allows unrestricted access to every connected system.

There is no ordinary:

> FORGE master password

or:

> FORGE master API key

that bypasses institutional authorization.

Compromise of the central orchestration layer should therefore not automatically expose every protected external resource.

## Institution Does Not Equal Credential

Institutional authority and possession of secrets remain separate.

For example, the Banker institution may determine whether a financial transaction is authorized.

That does not require individual Banker members to know:

- the bank password,
- account recovery secrets,
- unrestricted API credentials,
- or other reusable authentication material.

The institution authorizes access.

The protected credential service performs credential handling.

## Raw Credential Isolation

Where technically possible, raw reusable credentials remain inside the protected credential service.

They are not returned to:

- FORGE,
- the requesting subsystem,
- institutional members,
- Watchers,
- Auditors,
- or the execution process.

Instead, the service uses those credentials internally to create or facilitate the approved scoped capability.

## Ephemeral Execution Capability

After all required approvals are satisfied, the credential service may issue a temporary execution capability.

The capability is bound to the authorized action.

It may include constraints such as:

- specific account,
- specific destination,
- maximum amount,
- permitted operation,
- approved resource,
- execution deadline,
- request identity,
- authorization identity,
- execution identity,
- permitted endpoint,
- or other material restrictions.

## Example

Suppose FORGE proposes:

> Transfer $500 from Account A to approved Vendor B.

The Banker institution evaluates the authenticated request.

After the required Banker quorum and other constitutional approvals are satisfied, the financial credential service may issue a capability representing:

> Transfer no more than $500 from Account A to Vendor B for Request X before Time Y.

The capability does not mean:

> FORGE may access the bank account however it wants.

The execution process receives only the authority required for the approved transaction.

## Capability Binding

A capability must be cryptographically or otherwise securely bound to the authorization it represents.

Where technically possible, it should be bound to:

- authenticated request identity,
- authorization identity,
- permitted action,
- target resource,
- material parameters,
- validity period,
- and execution context.

Changing a material parameter invalidates inherited authority.

## Expiration

Ephemeral capabilities expire.

The validity period should be no longer than reasonably necessary to complete the authorized action.

An expired capability cannot be treated as continuing permission.

If the authorized action still needs to occur after expiration, the appropriate authorization process must issue a new valid capability.

## Single-Use Authority

Where practical, consequential capabilities should be single-use.

Successful execution consumes the capability.

A previously completed transaction cannot be repeated merely by replaying the same authorization artifact.

## Replay Protection

The credential architecture must provide replay resistance appropriate to the protected resource.

Possible mechanisms may include:

- single-use identifiers,
- nonces,
- execution receipts,
- transaction state,
- expiration,
- capability consumption records,
- destination binding,
- request-state binding,
- or combinations of these mechanisms.

The exact implementation depends on the external system.

## Least Authority

Credential delegation follows the principle of least authority.

The execution process receives:

> Only the authority necessary for the approved action, for only as long as necessary.

FORGE does not receive broader authority merely because broader authority would be technically convenient.

## Authorization Is Not Execution

The institution controlling authorization cannot necessarily perform the external action itself.

For example:

Banker may approve a transaction.

Banker does not automatically become the transaction executor.

This maintains separation between:

- request,
- authorization,
- credential delegation,
- execution,
- observation,
- and verification.

## Execution Is Not Authorization

Likewise, FORGE's execution process may technically interact with an external service using an approved capability.

That does not give execution authority to create new financial decisions.

The executor may perform the authorized transaction.

It may not decide:

> Since I can transfer $500, I will transfer $750 instead.

The capability should make such expansion technically impossible where feasible.

## Material Mutation

If the requested action materially changes after authorization, the existing credential capability is invalid for the changed action.

Examples include changing:

- recipient,
- amount,
- account,
- resource,
- action type,
- timing outside authorized bounds,
- or another authorization-relevant parameter.

Changed action means changed authorization requirement.

## Credential Service Authority

The credential service itself is not a policy-making institution.

It enforces already established authorization requirements.

It should not independently decide:

> This request seems reasonable, so I will issue access.

The service verifies that the required authorization evidence exists before issuing the constrained capability.

## Watcher Observation

Relevant Watchers may observe:

- capability issuance,
- execution attempt,
- external interaction,
- resulting state,
- capability consumption,
- and unexpected behavior.

Watchers do not receive raw credentials merely because they observe credential use.

## Auditor Verification

Auditors may verify:

- request identity,
- institutional authorization,
- capability identity,
- capability scope,
- execution evidence,
- expiration state,
- consumption state,
- and consistency between the approved request and completed action.

The Auditor does not require unrestricted possession of the underlying credential to verify the chain.

## Historian Role

The Historian preserves appropriate records of:

- authorization,
- capability issuance,
- execution,
- consumption or expiration,
- Watcher evidence,
- Auditor attestations,
- and relevant resulting state.

Raw reusable secrets should not be unnecessarily stored in historical records.

History preserves evidence of authority.

It does not become a credential archive.

## Revocation

Where technically possible, capabilities may be revoked before expiration.

Revocation may occur because of:

- HARD STOP,
- detected compromise,
- authorization withdrawal,
- changed system state,
- Doctor health finding,
- security incident,
- or another constitutionally defined condition.

Revocation removes authority.

It does not create replacement authority.

## Emergency Behavior

A HARD STOP may revoke or suspend outstanding capabilities within its defined safety scope.

Emergency authority may prevent a privileged action from continuing.

It cannot use the revoked credential authority to initiate a different action.

## Credential Rotation

Reusable credentials maintained inside credential services should support secure rotation.

Rotation must not silently alter constitutional authorization rules.

Changing the secret used to access a service is an operational security action.

Changing who is allowed to authorize use of that service is a governance action.

These are separate concerns.

## Credential Failure

If a credential service cannot establish that required authorization exists, it does not issue the capability.

If capability integrity cannot be verified, execution does not proceed.

If a capability is expired, consumed, revoked, malformed, or inconsistent with the requested action, execution fails closed.

Credential uncertainty does not become authorization.

## Compromise Containment

The architecture should be designed so compromise of one jurisdiction does not automatically compromise unrelated jurisdictions.

For example, compromise of a financial capability should not automatically provide access to:

- engineering infrastructure,
- constitutional records,
- security systems,
- or unrelated external accounts.

Jurisdictional separation therefore provides both governance separation and security containment.

## Consequences

This architecture introduces additional:

- credential services,
- authorization checks,
- capability issuance,
- cryptographic verification,
- expiration management,
- replay protection,
- logging,
- and integration complexity.

It may also make some external systems difficult to integrate when those systems support only long-lived unrestricted credentials.

FORGE accepts this complexity because permanent centralized credentials would create an authority structure fundamentally inconsistent with constitutional autonomy.

## Foundational Principle

> Possession of a secret is not authorization.

> Authorization does not require disclosure of the secret.

> Execution receives a capability, not a kingdom.

FORGE receives the minimum authority required to perform the specific action that was actually approved.
