# ADR-029: Constitutional Communications Bus and Authenticated Inter-Institution Messaging

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Communications / Messaging / Institutional Integrity

## Context

FORGE is composed of multiple independent institutions and constitutional processes.

These components must communicate.

Examples include:

- Dispatcher routing requests,
- Gatekeeper returning admissibility decisions,
- Banker issuing financial decisions,
- Doctor issuing health findings,
- Engineer submitting update artifacts,
- Security reporting threats,
- Watchers submitting observations,
- Auditors issuing attestations,
- Historian preserving records,
- Teacher providing governed learning artifacts,
- Executor reporting execution results,
- and FORGE coordinating the complete process.

Communication is necessary.

Uncontrolled communication is dangerous.

If institutions can freely send privileged commands directly to one another, FORGE could develop hidden execution paths outside the constitutional process.

For example:

Banker  
→ sends direct command to Executor  
→ Executor transfers money

or:

Engineer  
→ directly tells credential service to grant administrator access

or:

FORGE  
→ privately tells an Auditor to approve a request

or:

Subsystem A  
→ directly modifies Subsystem B

Such paths could bypass:

- Dispatcher,
- Gatekeeper,
- jurisdiction checks,
- quorum,
- authorization,
- evidence recording,
- Watchers,
- Auditors,
- resource controls,
- and final verification.

FORGE therefore requires a governed communications architecture.

## Decision

FORGE establishes an authenticated constitutional communications layer for governance-relevant inter-component communication.

Messages must preserve:

- sender identity,
- recipient identity,
- message type,
- request or action context,
- jurisdictional meaning,
- integrity,
- ordering or freshness where required,
- and authority provenance.

Communication itself does not create authority.

## Core Rule

> A message may carry authority.

> A message does not create authority merely by being delivered.

The receiver independently determines whether the sender possesses the authority represented by the message.

## Constitutional Communications Bus

FORGE may implement a Constitutional Communications Bus or equivalent governed messaging layer.

The bus provides controlled communication between:

- FORGE,
- Dispatcher,
- Gatekeeper,
- institutions,
- institutional members,
- Auditors,
- Watchers,
- Historian,
- Doctor,
- Engineer,
- Teacher,
- Security,
- Executor,
- credential services,
- and other constitutionally recognized components.

The architecture does not mandate a specific messaging technology.

Possible implementations include:

- message queues,
- event streams,
- authenticated RPC,
- service buses,
- capability channels,
- local IPC,
- distributed messaging,
- or combinations of these mechanisms.

## Bus Is Not Government

The communications bus transports constitutional messages.

It does not decide:

- jurisdiction,
- approval,
- quorum,
- authorization,
- execution eligibility,
- or constitutional meaning.

Infrastructure does not become a hidden institution.

## Message Identity

Governance-relevant messages should have unique identities.

A message may include:

- message ID,
- sender identity,
- recipient identity,
- message type,
- request ID,
- action ID,
- delegation ID where applicable,
- constitutional version,
- membership version where applicable,
- timestamp or ordering information,
- expiration,
- integrity metadata,
- and evidence references.

## Authenticated Sender

The receiver should be able to establish who sent an authority-relevant message.

The string:

> FROM: BANKER

does not establish Banker identity.

## Authenticated Recipient

Sensitive or authority-bearing messages should be delivered to authenticated intended recipients.

A message intended for Banker should not be accepted by an unrelated component merely because it can observe the transport.

## Message Integrity

Material modification of a message after issuance should be detectable.

Integrity mechanisms may include:

- digital signatures,
- message authentication codes,
- authenticated transport,
- cryptographic digests,
- or equivalent controls.

## Confidentiality

Some messages may require confidentiality.

ADR-020 applies.

Confidentiality and authority remain separate properties.

An encrypted message is not automatically an authorized message.

## Message Types

FORGE should use explicit message types where practical.

Examples may include:

- REQUEST,
- DECISION,
- VOTE,
- HEALTH_FINDING,
- SECURITY_FINDING,
- AUDIT_ATTESTATION,
- WATCHER_OBSERVATION,
- EVIDENCE_REFERENCE,
- AUTHORIZATION,
- CAPABILITY_REFERENCE,
- EXECUTION_COMMAND,
- EXECUTION_RESULT,
- REVOCATION,
- HARD_STOP,
- RECOVERY_MESSAGE,
- STATUS,
- QUERY,
- RESPONSE,
- and ERROR.

## Typed Messaging

Typed messaging reduces ambiguity.

A STATUS message cannot silently become an EXECUTION_COMMAND.

A WATCHER_OBSERVATION cannot silently become an AUTHORIZATION.

An AUDIT_ATTESTATION cannot silently become a Banker vote.

## Message Schema

Each governance-relevant message type should have a defined schema.

The schema may identify:

- required fields,
- permitted sender roles,
- permitted recipient roles,
- request binding,
- applicable jurisdiction,
- freshness requirements,
- and expected response semantics.

## Sender Authorization

A valid identity may send only messages appropriate to its role.

For example:

Doctor may issue:

> HEALTH_FINDING.

Doctor cannot issue:

> BANKER_APPROVAL.

## Recipient Validation

The recipient validates both:

- message authenticity,

and:

- sender authority for that message type.

## Communication Does Not Transfer Jurisdiction

Receiving information from another institution does not transfer that institution's jurisdiction.

For example:

Security tells Banker:

> Vendor X appears compromised.

Banker may use that information in its financial decision.

Security does not thereby become Banker.

## Decisions Versus Commands

FORGE distinguishes institutional decisions from execution commands.

Banker may issue:

> APPROVE financial component of Request R.

That does not necessarily mean:

> Executor, transfer funds now.

Execution occurs only after the complete authorization chain exists.

## Institutional Decisions

Institutions primarily communicate:

- decisions,
- conditions,
- evidence,
- findings,
- or requests for additional information.

They do not directly exercise unrelated execution authority.

## Executor Commands

A consequential execution command should originate only after valid authorization has been assembled and revalidated.

Executor verifies the applicable authorization rather than trusting the command text alone.

## No Direct Privileged Side Doors

Authority-bearing components must not create undocumented direct routes that bypass constitutional messaging and authorization.

Examples include:

- hidden HTTP endpoints,
- private sockets,
- debug channels,
- database flags,
- shared files,
- environment variables,
- secret queues,
- direct function calls,
- or administrative scripts

that provide equivalent privileged execution outside governance.

## Side-Channel Principle

A communication path becomes constitutionally relevant when it can materially influence authority or consequential execution.

Calling it:

> debug

does not exempt it.

## One Constitutional Meaning

Different transports may exist.

However, they must not create contradictory authority semantics.

A local socket must not permit an action that the normal authenticated bus would reject.

## Dispatcher Role

Dispatcher is the controlled ingress and routing authority for normal consequential requests.

Dispatcher determines where authenticated requests should be routed according to applicable architecture.

Dispatcher does not determine substantive institutional outcomes.

## Internal Institutional Messaging

Institutions may communicate internally according to their governance.

Internal communication must preserve applicable member identity and independent-voting requirements.

## Independent Voting

ADR-003 applies.

Members should independently evaluate requests before seeing other members' substantive votes where required.

The messaging layer should support this independence.

## Vote Isolation

Before a member casts its independent decision, the communications architecture should avoid unnecessarily exposing other member votes where doing so could create conformity pressure.

## Post-Vote Visibility

After independent decisions are committed, applicable governance may permit members to see other decisions for:

- explanation,
- reconciliation,
- review,
- or learning.

Visibility must not rewrite already-cast votes.

## Vote Commitment

High-risk institutional voting may use a commitment mechanism where appropriate.

A member commits its decision before other member decisions are revealed.

This reduces strategic vote adaptation.

## No Vote Editing

Once a vote is constitutionally committed, it should not be silently edited.

A changed decision becomes a new attributable event according to policy.

## Message Binding

Authority-bearing messages should bind to the relevant request or action.

For example:

Banker Approval B-17

should identify:

> Request R-82 / Action A-4

rather than simply:

> APPROVED.

## Parameter Binding

Material parameters should be included or cryptographically bound.

An approval for:

> $500 to Vendor A

must not be reusable for:

> $5,000 to Vendor B.

## Conditional Messages

Conditions remain attached to the decision.

For example:

Doctor:

> READY provided rollout remains below 10% of production.

FORGE cannot strip the condition and forward only:

> READY.

## Semantic Preservation

Routing, serialization, translation, summarization, or format conversion must not materially change the meaning of authority-bearing messages.

## Original Message Preservation

Where consequential, FORGE preserves the authenticated original or a verifiable commitment to it.

A transformed representation references its source.

## Translation

A translated message does not receive new authority.

Material translation ambiguity requires clarification or independent verification.

## Summarization

Summarizing an institutional decision must not erase:

- conditions,
- limitations,
- dissent,
- scope,
- or uncertainty.

The authoritative artifact remains the authenticated underlying decision.

## Message Provenance

ADR-017 applies.

FORGE should be able to determine:

- who created the message,
- whether it was transformed,
- who routed it,
- and which request or action it affected.

## Message Ordering

Some messages require ordering.

Examples include:

APPROVE  
→ REVOKE

or:

AUTHORIZATION  
→ EXECUTION

or:

HARD_STOP  
→ EXECUTION_ATTEMPT.

FORGE must preserve sufficient ordering to interpret authority correctly.

## Out-of-Order Delivery

A delayed message must not override newer state merely because it arrives later.

## Stale Messages

ADR-018 applies.

A once-valid message may become stale.

Recipients must evaluate current validity rather than assuming:

> authenticated once = valid forever.

## Message Expiration

Messages may include expiration where appropriate.

Expired authority-bearing messages cannot be revived by redelivery.

## Replay Protection

Attackers must not be able to replay old messages to recreate authority.

Replay protection may use:

- message IDs,
- nonces,
- sequence numbers,
- capability state,
- request state,
- expiration,
- or equivalent mechanisms.

## Duplicate Delivery

Messaging infrastructure may deliver the same message more than once.

Duplicate delivery must not automatically create duplicate execution.

## Idempotency

Where appropriate, receivers should process repeated identical messages idempotently.

## Exactly-Once Illusion

FORGE should not assume distributed messaging can always guarantee perfect exactly-once delivery.

Instead, consequential actions should use:

- unique action identities,
- idempotency,
- state verification,
- capability consumption,
- and execution evidence.

## Lost Message

A lost message does not become approval.

For example:

If Banker approval never reaches FORGE, FORGE cannot infer:

> Banker probably approved.

## Silence

Silence is not a message.

ADR-011 applies.

No response does not mean APPROVE.

## Timeout

Timeout may produce:

- UNAVAILABLE,
- communication failure,
- or another defined state.

Timeout does not create authority.

## Retry

Message retry must preserve original identity where appropriate.

Retrying delivery does not create a new institutional vote.

## Request Retry

A genuinely new request should receive new request identity or versioning according to policy.

Transport retry and governance resubmission must remain distinguishable.

## Message Acknowledgment

Acknowledgment means:

> Message received.

It does not necessarily mean:

> Message accepted.

or:

> Request approved.

## Receipt Versus Decision

FORGE distinguishes:

RECEIVED

from:

APPROVED.

## Query Messages

One institution may ask another for information.

Example:

Banker:

> Security, provide current vendor risk status.

The query does not command Security to change its decision.

## Response Messages

A response provides information within the responder's jurisdiction.

The requester decides how that information affects its own decision according to governance.

## Peer Communication

Institutions may communicate directly when constitutionally permitted.

Direct communication must not become direct unauthorized execution.

## FORGE Visibility

FORGE may coordinate messaging without being able to alter authenticated institutional decisions.

FORGE should not need authority to forge or rewrite messages in order to route them.

## No Message Forgery

FORGE cannot generate:

> Banker APPROVE

unless the message genuinely originates from the applicable Banker authority.

## No Decision Proxy

FORGE cannot speak on behalf of an institution merely because FORGE predicts what the institution would decide.

## No Synthetic Consensus

FORGE cannot summarize:

Banker: APPROVE  
Security: DENY  
Doctor: READY

as:

> All institutions approve.

The actual decision states remain authoritative.

## Auditor Messaging

Auditors communicate independent attestations.

Auditor messages should remain distinguishable from:

- authorization,
- execution,
- and institutional substantive decisions.

## Auditor Independence

FORGE cannot modify an Auditor attestation before presenting it as the Auditor's decision.

## Watcher Messaging

Watchers communicate observations.

Watcher evidence should travel through channels resistant to control by the observed subsystem where risk warrants.

## Watcher Independence

A subsystem should not be able to suppress all Watcher communication about itself.

## Historian Messaging

Historian receives governance records and may provide historical evidence.

Historian does not create current authorization by replaying old records.

## Doctor Messaging

Doctor communicates health findings such as:

- READY,
- NOT_READY,
- DEGRADED,
- QUARANTINE_RECOMMENDED,
- or other defined states.

Doctor health findings do not become unrelated execution commands.

## Engineer Messaging

Engineer may communicate:

- update proposals,
- artifacts,
- test results,
- deployment requirements,
- or technical findings.

Engineer cannot use a message to self-authorize deployment.

## Teacher Messaging

Teacher may communicate:

- training proposals,
- competency findings,
- learning artifacts,
- or educational material.

Teacher messages do not redefine jurisdiction.

## Security Messaging

Security may communicate:

- threat findings,
- containment requests,
- risk classifications,
- or compromise evidence.

Security cannot use ordinary messaging to grant itself unlimited constitutional authority.

## Banker Messaging

Banker communicates financial decisions and conditions.

Financial approval remains bound to the applicable request, amount, target, resource envelope, and current state.

## Credential-Service Messaging

Credential services accept only properly authorized capability requests.

A message saying:

> Give FORGE the password.

does not establish credential authority.

## Capability Delivery

Where capabilities must be delivered, messaging should avoid exposing reusable raw secrets.

Capabilities should be scoped according to ADR-009.

## HARD STOP Messaging

HARD STOP messages receive high-priority treatment.

The system should minimize the possibility that ordinary message congestion prevents safety containment.

## HARD STOP Authentication

A forged HARD STOP could itself cause harm.

The system therefore authenticates emergency signals according to applicable safety design.

## Fail-Safe Emergency Detection

Where human-life safety requires independent local detection, safety containment must not rely exclusively on successful central message delivery.

## HARD STOP Propagation

ADR-007 and ADR-027 apply.

A HARD STOP affecting delegated execution should propagate to affected descendants and execution paths.

## Resume Messaging

A message saying:

> Hazard cleared.

does not automatically authorize resume.

RESET/RESUME follows its own governed process.

## Recovery Messaging

During ADR-014 Constitutional Recovery, communications may operate in a restricted recovery mode.

Only recovery-appropriate message types may be permitted.

## Boot Messaging

ADR-023 applies.

Authority-bearing messaging should not enter normal mode until required identities and constitutional trust have been established.

## Pre-Boot Messages

Messages received before trust establishment may be:

- buffered,
- rejected,
- quarantined,
- or treated as untrusted input.

They do not gain authority merely by arriving early.

## Decommissioning Messaging

ADR-024 applies.

A decommissioned component's identity should no longer be accepted for new authority-bearing messages.

## Revocation Propagation

Revocation messages should propagate with sufficient priority and reliability to prevent continued use of revoked authority where practical.

## Membership Changes

ADR-015 applies.

A member removed from an institution loses authority to issue new institutional decisions.

Previously valid historical messages remain historical evidence.

## Membership Version Binding

Institutional votes should bind to the applicable membership version.

## Conflict of Interest

ADR-022 applies.

Recused members cannot issue valid decision messages for the matter from which they are recused.

## Delegated Messaging

ADR-027 applies.

A delegate may send only messages within its delegated authority.

## Cross-System Messaging

ADR-028 applies.

Messages from another FORGE deployment are authenticated external messages.

Remote FORGE identity does not create local authority.

## Adversarial Messages

ADR-021 applies.

Message payloads may contain adversarial instructions.

Authenticated transport does not make every statement inside the payload authoritative.

## Trusted Sender, Untrusted Payload

A trusted institution may forward untrusted content.

For example:

Security may send:

> Attached is the malicious email we received.

The malicious email remains untrusted content even though Security transmitted it through an authenticated channel.

## Trust Laundering Prevention

A trusted component forwarding untrusted content does not automatically increase the content's authority.

## Data and Control Separation

Where practical, messaging should distinguish:

- control fields,

from:

- data payload.

Untrusted payload should not be interpreted as message control metadata.

## Structured Serialization

FORGE should prefer structured serialization for authority-bearing messages where practical.

This reduces ambiguity and injection risk.

## Parser Consistency

Critical sender and receiver components should agree on the canonical meaning of signed or authenticated messages.

Parser disagreement can create security vulnerabilities.

## Canonicalization

Where messages are signed or hashed, canonicalization rules should be explicit.

Two components must not interpret the same authenticated bytes as materially different commands.

## Parser Differential Attack

FORGE should test cases where:

Sender interprets message as:

> $500.

while Receiver interprets it as:

> $5,000.

Such ambiguity is unacceptable for consequential authority.

## Unknown Message Type

Unknown authority-bearing message types fail closed.

A receiver must not guess that an unknown message means approval.

## Unsupported Version

If a message uses an unsupported governance protocol version, the receiver should:

- reject,
- quarantine,
- negotiate safely,
- or request a supported representation.

It must not silently downgrade constitutional meaning.

## Communications Policy

Communication permissions should follow least authority.

Not every component needs unrestricted ability to message every other component.

## Communication Matrix

FORGE may define a communication matrix identifying permitted message relationships.

Example:

Dispatcher → Institutions: REQUEST

Institutions → FORGE: DECISION

Watchers → Auditor/Historian: OBSERVATION

Executor → Watchers/Auditor/Historian: EXECUTION_RESULT

This is illustrative rather than exhaustive.

## Network Segmentation

Technical network segmentation may reinforce constitutional communication boundaries.

A subsystem that does not need direct access to a credential service should not automatically possess it.

## Egress Governance

Outbound communication can itself be consequential.

Messages containing:

- sensitive data,
- financial instructions,
- external commands,
- credentials,
- or public statements

may require governance.

## Information Exfiltration

ADR-020 applies.

Messaging must not become an uncontrolled data-exfiltration channel.

## Covert Channels

FORGE should reduce unauthorized covert communication channels where practical.

Perfect elimination may be impossible.

High-risk systems should monitor for unexpected communication patterns.

## Message Rate Governance

ADR-012 applies.

Components may have:

- message-rate limits,
- queue limits,
- concurrency limits,
- and resource budgets.

## Message Flooding

A compromised component must not be able to exhaust governance infrastructure by flooding the bus without detection or limits.

## Priority

Some constitutional traffic may receive higher priority.

Examples include:

- HARD STOP,
- revocation,
- security containment,
- recovery coordination,
- and critical health alerts.

Priority does not create substantive authority.

## Denial of Service

FORGE should distinguish:

> Message denied by governance

from:

> Message could not be processed because infrastructure failed.

The latter must not be interpreted as approval.

## Bus Failure

If the communications layer fails, FORGE enters applicable degraded operation.

It does not route consequential actions through uncontrolled side channels merely to maintain availability.

## Redundant Communication

Critical governance communication may use redundant channels.

Redundancy must preserve authentication and authority semantics.

## Independent Emergency Channel

High-risk deployments may maintain a narrowly scoped independent emergency containment channel.

Such a channel must not become a general-purpose bypass.

## Communications Evidence

Governance-relevant messages and their lifecycle become evidence under ADR-017 and events under ADR-026.

## Message Receipt Event

FORGE may record:

- message issued,
- message delivered,
- message acknowledged,
- message processed,
- and resulting state transition

where consequence warrants.

## Auditability

Auditors should be able to reconstruct:

Sender  
→ Message  
→ Recipient  
→ Interpretation  
→ Resulting Constitutional Event

for consequential communications.

## Watcher Role

Watchers may observe:

- unauthorized channels,
- message mutation,
- suspicious routing,
- suppression,
- replay,
- forged senders,
- or divergence between messages and execution.

## Auditor Role

Auditors may verify:

- sender identity,
- recipient identity,
- message integrity,
- request binding,
- jurisdiction,
- freshness,
- transformation,
- and resulting authority chain.

## Historian Role

Historian preserves significant constitutional communications and associated evidence.

Historian does not need to preserve every transient implementation message where no governance relevance exists.

## Security Role

Security monitors:

- impersonation,
- replay,
- injection,
- message flooding,
- unauthorized channels,
- protocol downgrade,
- parser attacks,
- and communication compromise.

## Engineer Role

Engineer implements and maintains messaging infrastructure.

Engineer does not gain authority to alter institutional decisions in transit.

## Doctor Role

Doctor may evaluate health of the communications infrastructure.

Healthy messaging infrastructure does not establish the validity of the messages transported through it.

## Formal Invariants

ADR-025 should support invariants such as:

> MessageDelivery != Authorization

and:

> SenderIdentity must be valid for AuthorityBearingMessage

and:

> MessageType must be permitted for SenderRole

and:

> MaterialMessageMutation invalidates integrity

and:

> DuplicateDelivery does not imply DuplicateExecution

and:

> StaleAuthorityMessage cannot create current authority

and:

> Routing cannot expand message authority

and:

> Transport failure cannot become approval

and:

> UntrustedPayload cannot modify authenticated control fields.

## Communications Testing

FORGE should test:

- forged sender,
- forged recipient,
- message mutation,
- replay,
- duplication,
- loss,
- reordering,
- delay,
- stale delivery,
- parser disagreement,
- protocol downgrade,
- message flooding,
- side-channel bypass,
- compromised router,
- and compromised recipient.

## Fail-Closed Rule

If FORGE cannot establish the identity, integrity, authority, scope, or freshness required for an authority-bearing message, that message does not create consequential authority.

Unknown sender is not authority.

Unknown message meaning is not approval.

Unknown freshness is not current authorization.

Transport success is not constitutional success.

## Consequences

Governed messaging introduces:

- authenticated message identities,
- explicit schemas,
- communication policies,
- message provenance,
- replay protection,
- canonicalization,
- routing controls,
- communication monitoring,
- and additional infrastructure.

This creates operational complexity.

FORGE accepts this cost.

A separation-of-powers architecture cannot remain separated if its institutions can bypass governance through uncontrolled communication.

## Foundational Principle

> Communication carries information.

> Communication may carry authenticated decisions.

> Communication does not manufacture authority.

> The sender must possess the authority represented by the message.

> The receiver independently verifies that authority.

> Routing does not expand authority.

> Translation does not expand authority.

> Delivery does not equal approval.

> A hidden communication path must never become a hidden constitutional path.

FORGE institutions may communicate freely enough to cooperate, but never so freely that communication itself dissolves the constitutional boundaries between them.
