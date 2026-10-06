# ADR-017: Evidence Integrity and Chain of Custody

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Evidence / Integrity / Accountability

## Context

FORGE depends on evidence.

Authorization alone establishes what an action is permitted to do.

It does not establish what actually happened.

FORGE therefore uses independent Watchers, Auditors, the Historian, Doctor, institutions, and execution records to create and evaluate evidence.

This creates another constitutional problem:

> How does FORGE know that the evidence being evaluated is the same evidence that was originally produced?

An execution component could perform one action and report another.

A compromised Watcher could alter its observation.

Evidence could be modified after creation.

Records from two different requests could be combined.

A legitimate observation could be replayed as evidence for another action.

Timestamps could be manipulated.

Evidence unfavorable to an action could be omitted.

An Auditor could receive only a carefully selected subset of the available evidence.

FORGE therefore requires authenticated evidence provenance and a verifiable chain of custody.

## Decision

Consequential evidence in FORGE must carry sufficient provenance and integrity information to establish:

- what produced it,
- which request it belongs to,
- which action or state it describes,
- when it was produced,
- which constitutional and institutional state applied,
- whether it has been modified,
- how it moved through the system,
- and what other evidence it depends upon.

Evidence used to authorize, verify, audit, recover, or certify consequential actions must not depend solely on an unauthenticated description of that evidence.

## Core Rule

> Evidence must be attributable, bound, and verifiable.

A statement about evidence is not equivalent to the evidence itself.

## Evidence Artifact

A consequential observation should produce an identifiable evidence artifact.

An evidence artifact may include:

- observation,
- measurement,
- event record,
- state snapshot,
- decision,
- vote,
- health result,
- execution receipt,
- authorization record,
- external response,
- recovery record,
- or another governance-relevant fact.

Each artifact should receive a unique evidence identity.

## Evidence Identity

Evidence identity should bind the artifact to relevant context.

Depending on the evidence type, this may include:

- evidence ID,
- request ID,
- action ID,
- authorization ID,
- institution identity,
- member identity,
- Watcher identity,
- Auditor identity,
- execution identity,
- target identity,
- timestamp or trusted sequence information,
- constitutional version,
- membership version,
- state identity,
- and cryptographic digest.

The exact representation is implementation-specific.

The constitutional requirement is that evidence cannot be silently detached from its origin and reused as though it described another event.

## Cryptographic Integrity

Where technically appropriate, consequential evidence should use cryptographic integrity mechanisms.

These may include:

- hashes,
- digital signatures,
- authenticated logs,
- chained records,
- signed manifests,
- trusted hardware attestations,
- or equivalent mechanisms.

The purpose is not merely encryption.

The purpose is to establish whether the evidence has changed since it was created.

## Evidence Signing

Authority-bearing components should authenticate evidence they produce where appropriate.

A signature means:

> This identified source produced or attested to this evidence.

A signature does not mean:

> The evidence is automatically true.

Authenticity and truth are separate questions.

A compromised but validly authenticated component may still produce false evidence.

This is why FORGE also requires independent evidence sources.

## Provenance

Evidence provenance records where evidence came from.

FORGE should be able to determine:

- original producer,
- relevant institutional role,
- request association,
- collection mechanism,
- transformations applied,
- storage history,
- and verification history.

Evidence with unknown provenance has reduced or no authority depending on the applicable policy.

## Chain of Custody

When evidence moves between components, FORGE preserves a verifiable chain of custody.

Conceptually:

Original Observation  
→ Evidence Artifact  
→ Authenticated Transfer  
→ Historian Record  
→ Auditor Review  
→ Final Attestation

Each stage should preserve the identity of the original evidence.

Intermediate systems must not silently replace the artifact with an unauthenticated summary.

## Transformation

Some evidence may require transformation.

Examples include:

- normalization,
- compression,
- format conversion,
- aggregation,
- redaction,
- feature extraction,
- summarization,
- or privacy filtering.

A transformed artifact must not pretend to be the untouched original.

The transformation should identify:

- source artifact,
- transformation performed,
- component performing it,
- resulting artifact identity,
- and integrity relationship to the source.

## Original Evidence Preservation

Where feasible and appropriate, FORGE preserves the original evidence or a verifiable commitment to it.

A summary may assist reasoning.

It must not erase the existence of the underlying source.

## Request Binding

Evidence used for a consequential action must be bound to the applicable request.

Evidence from Request A cannot be presented as though it belongs to Request B merely because the requests appear similar.

This prevents cross-request evidence substitution.

## Authorization Binding

Execution evidence should identify the authorization under which the action occurred.

This allows an Auditor to compare:

Authorized Action  
vs.  
Observed Action

without relying solely on FORGE's description of either.

## State Binding

Where system or external state materially affects evidence, the artifact should identify the relevant state.

For example:

A balance check used to authorize a transaction may become stale if the account state changes.

A health check may become stale after a subsystem update.

Evidence must therefore be interpreted within its applicable state context.

## Evidence Freshness

Some evidence has limited validity over time.

Evidence policy may define:

- expiration,
- maximum age,
- required refresh conditions,
- state-change invalidation,
- or event-based invalidation.

Old evidence does not remain valid indefinitely merely because it was once authentic.

## Replay Protection

Evidence artifacts must not be reused in contexts where they are no longer valid.

A valid health result from yesterday cannot automatically prove health today.

A valid Watcher observation from one execution cannot prove another execution occurred correctly.

A valid authorization receipt cannot prove an unrelated request was authorized.

Replay detection should use evidence identity and contextual binding.

## Independent Evidence

For high-risk actions, FORGE should prefer evidence from multiple independent sources.

For example:

Execution reports:

> Transaction completed for $500.

Watcher A observes:

> $500 request transmitted.

Watcher B observes:

> External account decreased by $500.

External receipt reports:

> Transaction ID X settled for $500.

These evidence channels collectively provide stronger assurance than the Executor's own report.

## Evidence Diversity

Multiple copies of the same evidence are not necessarily independent evidence.

For example:

Five Watchers reading the same potentially corrupted log may represent one underlying evidence source.

FORGE should distinguish:

- number of observers,

from:

- number of independent evidence channels.

## Evidence Independence

Evidence independence should consider whether sources share:

- software,
- sensors,
- logs,
- network paths,
- credentials,
- infrastructure,
- data providers,
- or other common failure domains.

The required independence level should scale with consequence and risk.

## Executor Evidence

The Executor may produce execution records.

These records are useful.

They are not sufficient by themselves to prove correct execution.

The component performing an action cannot be the sole source certifying that the action occurred correctly.

## Watcher Evidence

Watchers independently observe actions and outcomes.

Watcher evidence should identify:

- Watcher identity,
- observation point,
- request,
- action,
- observed state,
- relevant time or sequence,
- and evidence integrity information.

A Watcher does not gain execution authority by observing execution.

## Multiple Watchers

Where risk warrants, FORGE may use multiple Watchers at different stages.

For example:

Watcher 1 observes command issuance.

Watcher 2 observes target-system behavior.

Watcher 3 observes resulting external state.

This makes collusion or false reporting more difficult.

## Auditor Evidence

Auditors produce attestations about integrity.

An Auditor may attest that:

- evidence identity is valid,
- required evidence exists,
- signatures are valid,
- request binding is correct,
- authorization binding is correct,
- evidence is internally consistent,
- and observed execution corresponds to authorized execution.

Auditor attestation is itself an evidence artifact.

## No Audit Self-Certification

An Auditor should not be the sole authority certifying the integrity of its own audit evidence where independent audit requirements apply.

Multiple independent Auditor attestations may be required according to risk.

## Doctor Evidence

Doctor health findings are evidence artifacts.

They should identify:

- evaluated component,
- health profile,
- tests performed,
- applicable baseline,
- resulting health state,
- relevant time,
- and Doctor identity.

A health conclusion should remain distinguishable from the underlying health evidence.

## Institutional Decisions as Evidence

Institutional votes and decisions are also evidence artifacts.

A decision should be bound to:

- request identity,
- member identity,
- institution identity,
- membership version,
- decision state,
- conditions,
- applicable constitutional version,
- and relevant time or sequence.

This prevents a vote from being detached and reused.

## Quorum Evidence

A quorum result should be independently reconstructable from authenticated member decisions where appropriate.

FORGE should not rely solely on a statement such as:

> Banker approved 4-to-1.

The underlying valid votes should be traceable.

## Human Approval Evidence

Privileged human approval is an evidence artifact.

It should be bound to:

- authenticated human identity,
- requested action,
- scope,
- applicable conditions,
- time or expiration,
- and relevant constitutional process.

A screenshot, message, document, or external text claiming human approval is not equivalent to authenticated human authorization.

## Historian Role

The Historian preserves evidence and its provenance.

Historian records should be append-oriented.

Later evidence may:

- supplement,
- contradict,
- invalidate,
- or correct an earlier interpretation.

The original historical artifact remains visible.

## No Historical Rewriting

FORGE must not silently rewrite prior evidence because later information changes the conclusion.

For example:

If an early Watcher reported success and a later Watcher proves failure, the record should show both.

It should not rewrite history to make the early Watcher appear to have reported failure.

## Corrections

Corrections are new evidence.

A corrected record should reference the artifact being corrected.

The original artifact remains part of the historical chain.

## Contradictory Evidence

FORGE must be capable of representing contradictory evidence.

Contradiction does not authorize FORGE to select whichever artifact supports the desired outcome.

Material contradiction may require:

- additional observation,
- Auditor review,
- investigation,
- request suspension,
- recovery,
- or fail-closed behavior.

## Missing Evidence

Missing required evidence is not positive evidence.

If a consequential action requires independent execution observation and that observation is unavailable, FORGE cannot assume:

> No evidence of failure means success.

Absence of required evidence leaves the verification requirement unsatisfied.

## Evidence Silence

Silence from a Watcher, Auditor, Doctor, institution, or evidence source is not an affirmative result.

No response does not mean:

- healthy,
- approved,
- successful,
- safe,
- or verified.

## Evidence Selection

FORGE must not selectively hide material evidence from an authority responsible for evaluating a request.

Where relevant evidence exists, the evaluation process should have access to the evidence required by policy.

Intentional omission of known material evidence is an integrity failure.

## Evidence Manifest

Consequential actions may maintain an evidence manifest.

The manifest may identify:

- request evidence,
- authorization evidence,
- institutional decisions,
- health evidence,
- execution evidence,
- Watcher evidence,
- Auditor attestations,
- external receipts,
- and resulting state evidence.

The manifest itself should be authenticated.

## Evidence Graph

FORGE may represent evidence as a graph rather than a flat log.

For example:

Request  
→ Institutional Decisions  
→ Authorization  
→ Execution  
→ Watcher Observations  
→ Resulting State  
→ Auditor Attestations

Each node has an identity.

Each relationship is explicit.

This allows FORGE to reconstruct why a consequential action was considered valid.

## Evidence Retention

Evidence retention depends on risk, privacy, legal requirements, resource constraints, and constitutional policy.

Not all evidence must necessarily be retained forever.

However, deletion of governance-critical evidence must follow applicable retention and deletion policy.

## Evidence Deletion

Where evidence may be deleted, deletion itself should be attributable and governed.

Deletion must not be used to erase evidence of:

- failure,
- unauthorized behavior,
- governance disagreement,
- security incidents,
- or constitutional violations.

## Privacy

Evidence integrity does not require universal disclosure.

Sensitive evidence may be:

- compartmentalized,
- encrypted,
- redacted,
- access-controlled,
- or represented through privacy-preserving verification.

However, privacy controls must not permit false claims about what evidence proves.

## External Evidence

Evidence originating outside FORGE may have different trust properties.

Examples include:

- bank receipts,
- API responses,
- sensor readings,
- external logs,
- signed third-party records,
- and human-provided documents.

External evidence should be classified according to its provenance and authentication strength.

FORGE must not treat all external data as equally trustworthy.

## Evidence From Untrusted Sources

Untrusted evidence may still be informative.

It does not automatically become authoritative.

For example:

A webpage may claim:

> Transaction completed.

That statement alone is not necessarily trustworthy execution evidence.

The system evaluates evidence according to source, authentication, independence, and context.

## Evidence Channel Compromise

If an evidence channel is known or suspected to be compromised, evidence from that channel receives the appropriate reduced trust or quarantine treatment.

Previously produced evidence may require reevaluation if the compromise could have affected it.

## Compromised Watcher

A compromised Watcher does not automatically invalidate every other independent Watcher.

Likewise, a healthy Watcher does not automatically rehabilitate compromised evidence.

The system evaluates the affected evidence graph.

## Evidence Quarantine

Suspicious evidence may be quarantined.

Quarantined evidence remains preserved for investigation but does not satisfy normal verification requirements unless later restored to trusted status through the appropriate process.

## Chain Break

If FORGE cannot establish a required portion of the evidence chain, the chain is considered incomplete.

For consequential execution:

> An incomplete required evidence chain cannot be silently treated as complete.

Depending on the stage, the system may:

- halt before execution,
- refuse final certification,
- enter investigation,
- initiate recovery,
- or fail closed.

## Final Verification

Final Auditor verification should evaluate the relationship between:

- authenticated request,
- applicable jurisdictions,
- institutional approvals,
- conditions,
- authorization,
- execution,
- Watcher evidence,
- resulting state,
- and relevant external evidence.

The goal is not merely to determine whether an action occurred.

The goal is to determine whether:

> The authorized action is the action that actually occurred.

## Certification

A successful final verification may produce a certification artifact.

That artifact should identify the evidence on which certification depends.

Certification does not erase the underlying evidence.

## Failed Certification

If final verification cannot establish the required relationship between authorization and execution, the action is not certified as constitutionally verified.

This remains true even if the practical outcome appears successful.

A successful outcome does not retroactively create valid authorization or evidence.

## Recovery Evidence

Recovery operations are subject to evidence requirements.

Recovery should preserve evidence showing:

- why recovery was initiated,
- who authorized it,
- which checkpoint was selected,
- what was restored,
- which credentials were changed,
- which institutions were re-established,
- and how post-recovery integrity was verified.

## Constitutional Evidence

Constitutional amendments, jurisdiction definitions, institutional membership changes, and other governance-critical state should have authenticated historical provenance.

FORGE must be able to establish which constitutional state governed an action.

## Evidence Failure and Constitutional Recovery

Widespread loss of trustworthy evidence may become a governance integrity failure.

If FORGE can no longer establish the evidence required to trust its constitutional state, ADR-014 Constitutional Recovery may apply.

## Consequences

Strong evidence integrity introduces:

- storage overhead,
- cryptographic operations,
- evidence indexing,
- identity management,
- chain-of-custody records,
- additional Watchers,
- retention requirements,
- and verification latency.

FORGE accepts this cost.

A constitutional architecture cannot meaningfully separate authorization, execution, observation, and audit if the evidence connecting those functions can be silently modified.

## Foundational Principle

> Authorization establishes what may happen.

> Execution attempts the authorized action.

> Watchers provide evidence of what happened.

> Auditors verify the relationship between authorization and evidence.

> The Historian preserves the record.

> Evidence must remain attributable from creation through verification.

FORGE does not trust a claim about what happened when it can independently preserve and verify evidence of what happened.
