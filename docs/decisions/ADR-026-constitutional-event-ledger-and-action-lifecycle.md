# ADR-026: Constitutional Event Ledger and End-to-End Action Lifecycle

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Event Ledger / Action Lifecycle / Accountability

## Context

FORGE now defines constitutional rules for:

- authenticated requests,
- institutional governance,
- independent Watchers,
- Auditors,
- Historian,
- recovery,
- updates,
- emergency authority,
- constitutional amendments,
- credentials,
- training,
- deadlock,
- resource governance,
- human authority,
- catastrophic recovery,
- institutional identity,
- jurisdiction,
- evidence integrity,
- temporal authority,
- external systems,
- information boundaries,
- adversarial instructions,
- conflicts of interest,
- constitutional boot,
- decommissioning,
- and constitutional invariants.

These mechanisms create many governance-relevant events.

A single consequential request may generate:

- ingress registration,
- request normalization,
- request identity,
- Gatekeeper decision,
- jurisdiction determination,
- institutional votes,
- quorum results,
- Doctor findings,
- Security findings,
- Auditor attestations,
- authorization artifacts,
- credential capabilities,
- execution attempts,
- Watcher observations,
- external receipts,
- retries,
- state changes,
- revocations,
- final verification,
- and closure.

Without a common lifecycle model, FORGE could possess all of these records while still being unable to reliably answer:

> What happened to Request X?

or:

> Which authorization caused Action Y?

or:

> Did this action ever actually execute?

or:

> Why was this request denied?

or:

> Is this request still pending?

or:

> Which evidence supports the final outcome?

FORGE therefore requires a constitutional event ledger and explicit end-to-end action lifecycle.

## Decision

Every consequential request in FORGE receives a traceable lifecycle.

Governance-relevant events associated with that lifecycle are recorded as authenticated, attributable events.

The event ledger provides a reconstructable history of the request.

The ledger does not itself grant authority.

## Core Rule

> Every consequential action must be traceable from authenticated intent to final disposition.

FORGE should be able to answer:

- who requested it,
- what was requested,
- which institutions had jurisdiction,
- what each authority decided,
- what was authorized,
- what actually executed,
- what was observed,
- what was verified,
- and how the request ended.

## Event Ledger

The Constitutional Event Ledger is the logical record connecting governance events across the lifecycle of a consequential request.

It may be implemented through:

- append-oriented logs,
- event streams,
- signed records,
- authenticated databases,
- distributed ledgers,
- immutable storage,
- or another integrity-preserving mechanism.

FORGE does not require blockchain.

The constitutional requirement is:

> Events must be attributable, ordered sufficiently for their purpose, integrity-protected, and historically reconstructable.

## Ledger Is Not Authority

The ledger records authority.

It does not create authority.

Writing:

> APPROVED

into the ledger does not create a valid approval.

The ledger entry must reference or contain the authenticated authority artifact that established approval.

## Event Identity

Each governance-relevant event should have a unique event identity.

An event may include:

- event ID,
- event type,
- request ID,
- action ID,
- source identity,
- institutional identity,
- member identity where applicable,
- relevant state,
- constitutional version,
- membership version,
- timestamp or ordering information,
- parent event,
- related evidence,
- and integrity metadata.

## Request Identity

Every consequential request receives a stable request identity.

The request identity follows the request throughout its lifecycle.

Material mutation creates a new request state and may require a new request identity or authenticated version according to policy.

## Action Identity

A request may produce one or more actions.

Each consequential action should have its own action identity.

This allows FORGE to distinguish:

> One request authorized three actions.

from:

> Three executions accidentally occurred for one authorized action.

## Correlation

Events should be correlated without relying solely on human-readable descriptions.

For example:

Request R-100  
→ Authorization A-100  
→ Capability C-100  
→ Execution E-100  
→ Watcher Evidence W-100  
→ Audit V-100

The identifiers allow reconstruction of the complete chain.

## Parent-Child Relationships

Events may identify causal or governance relationships.

Examples include:

Request  
→ Jurisdiction Determination

Request  
→ Institutional Vote

Institutional Votes  
→ Quorum Decision

Authorization  
→ Capability

Capability  
→ Execution

Execution  
→ Observation

Observation  
→ Verification

Verification  
→ Closure

## Event Types

FORGE should define recognized event types.

Examples may include:

- REQUEST_REGISTERED,
- REQUEST_NORMALIZED,
- REQUEST_REJECTED,
- JURISDICTION_IDENTIFIED,
- GATEKEEPER_APPROVED,
- GATEKEEPER_DENIED,
- INSTITUTIONAL_REVIEW_STARTED,
- MEMBER_APPROVED,
- MEMBER_DENIED,
- MEMBER_ABSTAINED,
- MEMBER_UNAVAILABLE,
- MEMBER_RECUSED,
- QUORUM_REACHED,
- QUORUM_FAILED,
- DOCTOR_READY,
- DOCTOR_NOT_READY,
- SECURITY_APPROVED,
- SECURITY_DENIED,
- AUDIT_ATTESTED,
- AUTHORIZATION_CREATED,
- AUTHORIZATION_REVOKED,
- AUTHORIZATION_EXPIRED,
- CAPABILITY_ISSUED,
- CAPABILITY_CONSUMED,
- CAPABILITY_REVOKED,
- EXECUTION_STARTED,
- EXECUTION_SUCCEEDED,
- EXECUTION_FAILED,
- EXECUTION_UNKNOWN,
- WATCHER_OBSERVATION,
- EXTERNAL_RECEIPT,
- HARD_STOP_TRIGGERED,
- RECOVERY_STARTED,
- RECOVERY_COMPLETED,
- FINAL_VERIFICATION_PASSED,
- FINAL_VERIFICATION_FAILED,
- REQUEST_CLOSED,
- and other constitutionally defined events.

The exact names are implementation-specific.

The semantics must be explicit.

## Event Schema

Each event type should have a defined schema.

The schema should identify:

- required fields,
- optional fields,
- source authority,
- applicable state transition,
- evidence requirements,
- and integrity requirements.

This prevents arbitrary strings from masquerading as constitutional events.

## Event Source

Every event must identify its source.

For example:

A MEMBER_APPROVED event must originate from an authenticated eligible institutional member.

An EXECUTION_SUCCEEDED event may originate from Executor.

A WATCHER_OBSERVATION must originate from an authenticated Watcher.

A FINAL_VERIFICATION_PASSED event must originate through the applicable Auditor process.

## Source Validation

Receiving a syntactically valid event is not sufficient.

FORGE validates whether the source has authority to emit that event type.

For example:

Executor cannot emit:

> MEMBER_APPROVED

as though Executor were Banker.

## Event Semantics

Events describe state transitions.

They must not silently carry broader meaning than defined.

For example:

EXECUTION_STARTED

does not mean:

EXECUTION_SUCCEEDED.

EXECUTION_SUCCEEDED

does not necessarily mean:

FINAL_VERIFICATION_PASSED.

FINAL_VERIFICATION_PASSED

does not mean:

THE ACTION WAS WISE.

Each event retains its defined meaning.

## Lifecycle States

A consequential request may move through states such as:

- REGISTERED,
- ADMISSIBILITY_REVIEW,
- GOVERNANCE_REVIEW,
- AUTHORIZED,
- READY_FOR_EXECUTION,
- EXECUTING,
- EXECUTION_UNKNOWN,
- EXECUTED,
- VERIFYING,
- VERIFIED,
- DENIED,
- FAILED,
- REVOKED,
- EXPIRED,
- SUSPENDED,
- CANCELED,
- RECOVERY,
- or CLOSED.

Exact state names are implementation-specific.

State semantics must be explicit.

## Lifecycle State Machine

FORGE should model consequential request lifecycle as an explicit state machine.

Not every transition is valid.

For example:

REGISTERED  
→ GOVERNANCE_REVIEW

may be valid.

REGISTERED  
→ EXECUTED

without required governance is not valid.

## State Transition Authority

Each transition must identify what authority permits it.

For example:

GOVERNANCE_REVIEW  
→ AUTHORIZED

requires the complete applicable authorization conditions.

AUTHORIZED  
→ EXECUTING

requires valid current authority and pre-execution checks.

EXECUTED  
→ VERIFIED

requires applicable verification.

## Illegal Transitions

Illegal transitions are rejected.

FORGE does not silently repair an illegal transition by inventing missing intermediate approvals.

## Request Registration

At ingress, Dispatcher registers the request.

Registration should establish:

- request identity,
- authenticated requester where applicable,
- normalized intent,
- material parameters,
- initial evidence references,
- and ingress event.

Registration does not mean approval.

## Gatekeeper Phase

Gatekeeper evaluates admissibility and constitutional constraints.

The ledger records the Gatekeeper result.

Possible results include:

- admissible,
- denied,
- quarantined,
- or requires clarification.

Gatekeeper does not execute the request.

## Jurisdiction Phase

FORGE identifies applicable institutional jurisdictions under ADR-016.

The jurisdiction record identifies which authorities must participate.

This prevents later removal of an inconvenient institution from the approval chain without evidence.

## Institutional Review Phase

Required institutions independently evaluate the authenticated request.

Each member decision is recorded according to ADR-003 and ADR-015.

Votes remain individually attributable.

## Quorum Event

When the applicable threshold is reached, the institutional quorum result is recorded.

The quorum event references the membership version and valid member decisions used to calculate the result.

## Conditional Decisions

Institutional approvals may contain conditions.

These conditions become part of the authorization graph.

They must not disappear when the decision is summarized.

## Denial Lifecycle

A valid required denial prevents the current request from becoming authorized.

The ledger preserves:

- denying authority,
- reason where appropriate,
- applicable evidence,
- and request state.

The request may later be revised and resubmitted.

The original denial remains historically visible.

## Revision

A revised request receives a new authenticated request version or identity according to policy.

The revision references the prior request.

FORGE does not rewrite the original request to make it appear as though the denied version never existed.

## Authorization Assembly

Once all required constitutional conditions are satisfied, FORGE may assemble an authorization artifact.

The artifact identifies:

- request,
- action,
- approving authorities,
- applicable conditions,
- resource envelope,
- temporal validity,
- state bindings,
- credential requirements,
- and constitutional version.

## Authorization Event

Creation of authorization generates an authenticated event.

The event itself does not replace the authorization artifact.

## Pre-Execution Validation

Before execution, FORGE revalidates applicable conditions under ADR-018.

This may generate events such as:

- STATE_REVALIDATED,
- AUTHORIZATION_EXPIRED,
- AUTHORIZATION_REVOKED,
- HEALTH_REVALIDATED,
- or EXECUTION_BLOCKED.

## Capability Issuance

If execution requires a scoped capability under ADR-009, capability issuance becomes part of the lifecycle.

The capability is bound to the authorized action.

## Execution Start

Executor records the start of consequential execution.

This event identifies:

- action identity,
- authorization identity,
- capability identity where applicable,
- Executor identity,
- target,
- and relevant state.

## Execution Result

Executor may report:

- success,
- failure,
- partial completion,
- or unknown outcome.

Executor's report is evidence.

It is not final constitutional certification.

## Unknown Execution State

FORGE explicitly supports:

> EXECUTION_UNKNOWN.

This is critical.

A timeout or crash must not force FORGE to falsely choose between:

- succeeded,

and:

- failed.

Unknown remains unknown until sufficient evidence resolves it.

## External Action Uncertainty

For external systems, ADR-019 applies.

Before retrying an uncertain consequential action, FORGE should determine whether the original action occurred where practical.

## Watcher Observation

Watchers record independent observations.

Watcher events reference the execution or state they observed.

Multiple Watchers may produce independent events.

## Resulting State

Where relevant, FORGE records evidence of resulting state.

This may be stronger evidence than the execution command itself.

For example:

Command:

> Transfer $500.

Resulting state:

> Account balance decreased by $500 and transaction X exists.

## Audit Phase

Auditors evaluate the evidence chain.

Audit events may identify:

- evidence completeness,
- authorization integrity,
- execution correspondence,
- state consistency,
- and unresolved conflicts.

## Final Verification

Final verification determines whether the available evidence supports the conclusion that the authorized action occurred within the authorized envelope.

Possible results include:

- VERIFIED,
- VERIFICATION_FAILED,
- or VERIFICATION_INCONCLUSIVE.

## Inconclusive Verification

Inconclusive is a valid constitutional result.

FORGE must not convert uncertainty into success merely to close the request.

## Closure

A request reaches closure when its active lifecycle has ended.

Closure may represent:

- verified success,
- denial,
- cancellation,
- expiration,
- verified failure,
- unresolved failure transferred to investigation,
- recovery disposition,
- or another defined terminal state.

## Closure Record

The closure record should identify:

- request identity,
- final state,
- actions attempted,
- authorization used,
- material evidence,
- verification result,
- unresolved issues,
- resource consumption,
- and relevant historical references.

## Closed Does Not Mean Successful

Closure means the active lifecycle is complete.

A request can close as:

- successful,
- denied,
- failed,
- canceled,
- expired,
- or unresolved according to policy.

## Terminal States

Terminal states should be explicitly defined.

A terminal request must not silently return to execution.

Reactivation requires a new governed transition or new request.

## No Silent Reopening

FORGE cannot reopen a closed request merely because circumstances later become favorable.

A new action requires valid current authority.

## Event Immutability

Recorded governance events should be append-oriented.

An event should not be silently edited after the fact.

Corrections create new events referencing the original.

## Event Correction

If an event contains an error, the correction process should preserve:

- original event,
- correction event,
- reason,
- correcting authority,
- and resulting interpretation.

## Event Retraction

Where a claim must be retracted, retraction is a new event.

Retraction does not erase historical evidence that the original claim was made.

## Causal Ordering

FORGE should preserve sufficient causal ordering to answer questions such as:

- Did approval precede execution?
- Did revocation precede capability use?
- Did HARD STOP precede the second execution attempt?
- Did request mutation occur before authorization?
- Did decommissioning precede restart?

Exact wall-clock time is not always required.

Reliable ordering is.

## Distributed Events

FORGE may operate across multiple processes or machines.

The architecture must not assume a perfectly synchronized global clock.

Distributed ordering may use:

- sequence numbers,
- causal references,
- signed checkpoints,
- monotonic counters,
- trusted timestamps,
- or equivalent mechanisms.

## Duplicate Events

Event processing should be idempotent where practical.

Receiving the same valid event twice should not automatically create two constitutional actions.

## Event Replay

Old events must not be replayable as new authority.

Event identity and state binding should allow FORGE to detect replay.

## Event Fork

A request lifecycle may unexpectedly fork.

For example:

Two Executors both believe they own Action A.

This must be detected.

A fork does not create two valid actions merely because both paths contain individually valid records.

## Single-Action Ownership

Where an action must execute exactly once, FORGE should establish a mechanism ensuring that only one valid execution path can own the action at a time.

## Concurrency

Some requests legitimately contain concurrent actions.

Concurrency must be explicit rather than accidental.

Each action receives independent identity and applicable authority.

## Race Conditions

FORGE should test lifecycle transitions for race conditions.

Examples include:

- execution versus revocation,
- execution versus expiration,
- member replacement versus quorum calculation,
- HARD STOP versus execution,
- shutdown versus queued action,
- and recovery versus pending capability.

## Atomic Transitions

Where practical, critical lifecycle transitions should be atomic.

For example:

Capability Consume  
and  
Execution Claim

may need strong coordination to prevent double execution.

## Ledger and Historian

The Constitutional Event Ledger and Historian are related but distinct concepts.

The ledger represents the structured lifecycle events.

Historian provides durable institutional memory and preservation.

Historian may preserve ledger events.

Historian does not gain authority over the events merely by storing them.

## Ledger and Evidence

Ledger entries may reference evidence under ADR-017.

The ledger should not duplicate sensitive raw evidence unnecessarily.

It may preserve:

- evidence identity,
- digest,
- provenance,
- location,
- classification,
- and verification state.

## Ledger and Privacy

ADR-020 applies.

A complete constitutional history does not require every participant to see every sensitive field.

Access to ledger information may be compartmentalized.

## Ledger and Credentials

Raw credentials should not be written into the event ledger.

The ledger records credential or capability identities and relevant lifecycle events without unnecessarily exposing secrets.

## Ledger and Constitutional Version

Consequential events should identify the constitutional version under which they occurred where applicable.

This permits historical reconstruction after later amendments.

## Ledger and Membership Version

Institutional decisions should identify the applicable membership version.

This prevents later membership changes from altering interpretation of an earlier vote.

## Ledger and Resource Governance

Resource consumption may be attached to the request/action lifecycle.

This enables cumulative accounting under ADR-012.

## Ledger and Conflict of Interest

Recusal and conflict events under ADR-022 should be visible in the lifecycle.

A final authorization should not conceal that a participant was recused or replaced.

## Ledger and HARD STOP

HARD STOP generates a high-priority constitutional event.

Affected action lifecycles transition according to ADR-007.

The ledger records:

- trigger,
- scope,
- affected actions,
- containment,
- and eventual RESET/RESUME or closure.

## Ledger and Recovery

Recovery events under ADR-005 and ADR-014 should reference affected requests and actions.

Recovery does not erase failed lifecycle states.

## Ledger and Boot

ADR-023 boot attestations establish the runtime context in which lifecycle events are generated.

FORGE should be able to associate consequential events with the active boot/runtime identity where required.

## Ledger and Decommissioning

ADR-024 Closure Records terminate deployment authority.

Events from a decommissioned deployment cannot later be replayed as current authority.

## Ledger Integrity

Ledger integrity should be independently verifiable.

Possible mechanisms include:

- chained hashes,
- signed event batches,
- append-only storage,
- authenticated checkpoints,
- Merkle structures,
- replicated integrity records,
- or equivalent mechanisms.

The architecture does not mandate one technology.

## No Ledger Self-Trust

The ledger service cannot simply state:

> My records are authentic.

Critical ledger integrity should be independently verifiable.

## Ledger Failure

Ledger failure does not automatically grant permission to operate without accountability.

If required event recording or verification becomes unavailable, affected consequential authority may be reduced or suspended.

## Buffered Events

Limited buffering may be permitted where constitutionally defined.

Buffered events must preserve:

- identity,
- ordering,
- integrity,
- and eventual reconciliation.

## Offline Operation

If FORGE permits offline operation, the Constitution must define which actions remain available without full ledger connectivity.

Offline mode must not become a bypass around governance.

## Reconciliation

When disconnected components reconnect, events must be reconciled.

Conflicting histories are not silently merged.

Material conflicts require verification.

## Ledger Fork Detection

If two incompatible event histories claim to represent the same action, FORGE treats this as an integrity incident.

The system preserves both histories for investigation.

## Event Completeness

For defined risk classes, FORGE may specify a minimum required event set.

For example, a high-risk external transaction might require:

Request  
→ Jurisdiction  
→ Institutional Approval  
→ Authorization  
→ Capability Issuance  
→ Execution  
→ Watcher Observation  
→ External Result  
→ Final Audit  
→ Closure

Missing required events prevent complete certification.

## Event Minimization

Not every internal computation must become a constitutional event.

FORGE should record governance-relevant transitions rather than indiscriminately logging every token or internal thought.

The ledger exists for accountability, not universal surveillance.

## No Chain-of-Thought Requirement

FORGE does not require preservation of private model chain-of-thought.

Governance accountability should rely on:

- decisions,
- evidence,
- inputs,
- outputs,
- authority,
- state transitions,
- and attributable rationale where appropriate.

Constitutional verification does not depend on exposing hidden internal reasoning.

## Decision Rationale

Institutions may provide a bounded rationale or reason code where appropriate.

Rationale helps:

- auditing,
- revision,
- debugging,
- and human understanding.

The rationale is evidence of the decision process.

It does not replace the authenticated decision itself.

## Human Visibility

Humans should be able to inspect meaningful lifecycle summaries for consequential actions.

A human-facing view may answer:

- What did FORGE receive?
- Who approved it?
- Who denied it?
- What conditions applied?
- What executed?
- What did the Watchers observe?
- Did the Auditors verify it?
- What is the final state?

## Machine Reconstruction

The same lifecycle should also be machine reconstructable.

Human-readable summaries must not become the only authoritative record.

## Constitutional Debugging

The event ledger allows FORGE engineers and governance authorities to reconstruct failures.

For example:

Request valid  
→ Banker approved  
→ Security approved  
→ Authorization created  
→ Capability issued  
→ Request mutated  
→ Executor failed to revalidate  
→ Unauthorized execution attempted

This makes the constitutional failure point visible.

## Invariant Verification

ADR-025 invariants may be evaluated against event sequences.

For example:

A verifier may assert:

> Every EXECUTION_STARTED event must have a preceding currently valid AUTHORIZATION_CREATED event satisfying the applicable jurisdiction requirements.

## Runtime Monitoring

Watchers or invariant monitors may inspect event streams for prohibited sequences.

Examples include:

- execution without authorization,
- use after revocation,
- duplicate capability consumption,
- quorum after invalid member replacement,
- or execution after decommissioning.

## Auditor Role

Auditors verify that lifecycle events and supporting evidence form a valid constitutional chain.

Auditors do not create missing events to make a chain complete.

## Watcher Role

Watchers produce independent observation events.

They may also detect divergence between expected and actual lifecycle.

## Historian Role

Historian durably preserves the constitutional event history and its relationship to evidence and checkpoints.

## Doctor Role

Doctor health findings become events where they materially affect authority.

Doctor does not control unrelated lifecycle transitions.

## Engineer Role

Engineer may implement the ledger and lifecycle mechanisms.

Engineer cannot rewrite historical events to simplify debugging or hide implementation failures.

## Security Role

Security may monitor the event stream for:

- anomalous sequences,
- spoofed event sources,
- unexpected execution,
- replay,
- or integrity failures.

## Dispatcher Role

Dispatcher begins the normal request lifecycle through authenticated ingress registration.

Dispatcher cannot bypass later lifecycle stages.

## Gatekeeper Role

Gatekeeper controls admissibility transitions.

Gatekeeper approval does not equal final execution authorization.

## Executor Role

Executor consumes valid authorization and records execution events.

Executor does not control final certification.

## Root Human Role

Root Human actions that materially affect consequential lifecycle should be attributable through authenticated governance events.

FORGE cannot fabricate those events.

## Lifecycle Testing

FORGE should test complete end-to-end lifecycle sequences.

Testing should include:

- successful request,
- denial,
- timeout,
- quorum failure,
- mutation,
- expiration,
- revocation,
- duplicate execution attempt,
- external uncertainty,
- HARD STOP,
- recovery,
- restart,
- and decommissioning.

## Fail-Closed Rule

If FORGE cannot establish the required lifecycle state of a consequential action, it does not guess the state that permits execution.

Unknown lifecycle state does not become:

- approved,
- unconsumed,
- unrevoked,
- successful,
- or verified.

## Consequences

The Constitutional Event Ledger introduces:

- event schemas,
- lifecycle state machines,
- correlation identities,
- causal ordering,
- integrity protection,
- reconciliation,
- lifecycle monitoring,
- and additional storage.

It also creates a powerful architectural advantage.

FORGE can reconstruct consequential behavior without relying on one component's narrative.

The system can determine not merely:

> What does FORGE currently claim happened?

but:

> What authenticated sequence of constitutional events demonstrates what happened?

## Foundational Principle

> Every consequential action has a beginning, a governed path, and an end.

> Requests have identities.

> Actions have identities.

> Authority has provenance.

> Execution has evidence.

> Verification has evidence.

> Closure has a defined state.

> The ledger records authority; it does not create authority.

> History is reconstructed from authenticated events, not from whichever component tells the most convincing story.

FORGE should be able to trace every consequential action from authenticated intent through constitutional governance to observed outcome and final disposition.
