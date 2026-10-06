# ADR-031: Uncertainty, Confidence, and Epistemic Governance

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Epistemic Governance / Uncertainty / Decision Integrity

## Context

FORGE makes decisions using information.

That information may come from:

- humans,
- institutions,
- sensors,
- databases,
- external APIs,
- AI models,
- retrieved documents,
- Watchers,
- Auditors,
- Historian,
- Doctor,
- Security,
- external FORGE systems,
- or delegated agents.

Not all information is equally reliable.

Information may be:

- incomplete,
- ambiguous,
- stale,
- contradictory,
- estimated,
- inferred,
- predicted,
- corrupted,
- manipulated,
- unavailable,
- or simply wrong.

Autonomous systems become dangerous when uncertainty disappears between observation and action.

For example:

Sensor:

> Temperature reading unavailable.

must not silently become:

> Temperature normal.

External API:

> Transaction status unknown.

must not become:

> Transaction failed, retry it.

AI model:

> This is probably the correct account.

must not become:

> Account identity verified.

Historian:

> No record found.

must not become:

> Event never occurred.

FORGE therefore requires explicit governance of uncertainty, confidence, evidence quality, and knowledge state.

## Decision

FORGE distinguishes:

- known facts,
- authenticated claims,
- observations,
- estimates,
- predictions,
- assumptions,
- hypotheses,
- unknowns,
- disputed information,
- and verified conclusions.

Consequential decisions must preserve material uncertainty throughout the governance chain.

Uncertainty must not silently become certainty merely because information passes through multiple components.

## Core Rule

> FORGE must know when it does not know.

Where material uncertainty exists, FORGE represents it explicitly.

## Epistemic State

A claim may have an epistemic state.

Possible states may include:

- VERIFIED,
- OBSERVED,
- REPORTED,
- INFERRED,
- ESTIMATED,
- PREDICTED,
- ASSUMED,
- DISPUTED,
- UNKNOWN,
- STALE,
- or INVALID.

Exact terminology is implementation-specific.

The meaning must be explicit.

## Claim Identity

Material claims should be independently identifiable where practical.

A claim may include:

- claim ID,
- proposition,
- source,
- source identity,
- evidence references,
- timestamp,
- freshness,
- confidence,
- epistemic state,
- applicable scope,
- and verification status.

## Claim Versus Fact

A component saying:

> X is true.

creates a claim.

It does not automatically establish X as verified fact.

## Authenticated Claim

Authentication establishes who made the claim.

It does not establish that the claim is true.

## Signed Falsehood

A cryptographically valid signature can authenticate a false statement.

FORGE therefore separates:

> Authentic source.

from:

> Accurate claim.

## Observation

An observation is evidence produced through some observation mechanism.

Observation quality depends on:

- sensor integrity,
- Watcher independence,
- measurement accuracy,
- environment,
- timing,
- and provenance.

## Inference

An inference derives a conclusion from other information.

The conclusion should remain traceable to its supporting evidence and assumptions.

## Prediction

A prediction describes an expected future state.

Prediction is not observation.

Prediction should not be represented as current fact.

## Estimate

An estimate approximates an unknown quantity.

Where consequence warrants, estimates should include uncertainty or bounds.

## Assumption

An assumption is a proposition temporarily treated as true for analysis.

Assumptions should be explicit where their failure could materially affect a consequential decision.

## Unknown

UNKNOWN is a legitimate state.

FORGE must not force unknown information into:

- true,
- false,
- safe,
- unsafe,
- approved,
- denied,
- successful,
- or failed

unless policy explicitly defines how that uncertainty is handled.

## Unknown Does Not Mean Safe

If safety depends on information that is unknown, FORGE must not automatically assume the safe condition exists.

## Unknown Does Not Mean Unsafe in Every Context

FORGE also does not automatically convert every unknown into a factual hazard.

Instead, uncertainty affects authority according to consequence and policy.

## Risk-Proportional Epistemic Requirements

Higher-consequence actions require stronger evidence and lower tolerance for unresolved uncertainty.

A low-consequence recommendation may proceed using estimates.

A high-consequence financial, physical, credential, recovery, or constitutional action may require verified evidence.

## Confidence

FORGE may associate confidence with some claims.

Confidence represents uncertainty.

It does not create authority.

## Confidence Is Not Authorization

A model being:

> 99% confident

does not mean:

> Constitutionally authorized.

## Confidence Is Not Truth

High confidence can still be wrong.

FORGE must not treat confidence as proof.

## Confidence Calibration

Where probabilistic confidence is used operationally, FORGE should evaluate whether confidence is calibrated.

For example:

Claims assigned approximately 90% confidence should, over an appropriate reference set, be correct approximately 90% of the time if that interpretation is intended.

## Uncalibrated Confidence

Uncalibrated model scores should not be presented as precise probabilities.

## False Precision

FORGE should avoid expressing unsupported precision.

For example:

> 83.742% certain

is misleading if the underlying process cannot justify that precision.

## Confidence Bands

Where useful, FORGE may use broader categories such as:

- LOW,
- MODERATE,
- HIGH,
- VERY_HIGH,

provided their meaning is defined.

## Confidence Thresholds

Policy may establish minimum evidence or confidence requirements for particular actions.

The threshold must not replace required constitutional authorization.

## Multiple Sources

Multiple independent sources may increase confidence.

However:

> Multiple copies of the same source are not independent evidence.

## Source Independence

FORGE should determine whether apparently separate sources share a common origin.

Example:

Five websites repeating one incorrect article do not necessarily constitute five independent sources.

## Model Independence

Five agents running the same model on the same context may share the same failure mode.

Numerical multiplicity does not automatically create epistemic independence.

## Institutional Independence

ADR-003 and ADR-004 apply.

Independent institutions should not be treated as independent if they actually depend on the same compromised evidence channel.

## Correlated Error

FORGE should consider correlated failure.

Sources may agree because they share:

- training data,
- sensor,
- upstream database,
- operator,
- model,
- provider,
- or compromised infrastructure.

## Evidence Diversity

High-consequence verification should prefer genuinely diverse evidence where practical.

## Contradictory Evidence

FORGE must preserve material contradictions.

Example:

Watcher A:

> Valve closed.

Watcher B:

> Valve open.

FORGE must not summarize this as:

> Valve status confirmed.

## Disputed State

Conflicting material evidence may produce:

> DISPUTED.

DISPUTED is not equivalent to UNKNOWN.

UNKNOWN means sufficient information is absent.

DISPUTED means material evidence conflicts.

## Contradiction Resolution

Contradictions may be resolved through:

- additional observation,
- stronger evidence,
- source validation,
- independent verification,
- human escalation,
- or applicable governance.

## No Majority Truth

Truth is not established merely because more agents repeat one claim.

Ten dependent sources do not automatically outweigh one highly authoritative independent measurement.

## Evidence Weight

Evidence evaluation may consider:

- source identity,
- independence,
- provenance,
- directness,
- freshness,
- measurement quality,
- consistency,
- and applicable expertise.

## Authority Versus Epistemic Weight

An institution may have authority to make a decision without possessing perfect knowledge.

Authority and knowledge are separate concepts.

Likewise, a source may possess excellent information without having constitutional decision authority.

## Expert Evidence

A subject-matter expert may provide high-value evidence.

Expertise does not automatically transfer constitutional jurisdiction.

## Institutional Decision Under Uncertainty

An institution may issue:

- APPROVE,
- DENY,
- ABSTAIN,
- or another constitutionally defined decision

based on available evidence.

Where uncertainty materially affects the decision, the uncertainty should remain visible.

## Conditional Approval

An institution may issue:

> APPROVE if Condition X is independently verified.

The condition remains attached to authorization.

## Epistemic Preconditions

Actions may require knowledge conditions.

Example:

> Execute only if target identity is VERIFIED.

or:

> Deploy only if Doctor health state is READY.

## Epistemic Preconditions Are State-Bound

ADR-018 applies.

If the supporting information becomes stale or contradicted, the authorization may require reevaluation.

## Freshness

Knowledge has a time dimension.

A verified fact from yesterday may not establish current state.

## Stale Evidence

Evidence may transition to STALE according to policy.

Stale does not necessarily mean false.

It means the evidence may no longer establish the required current condition.

## Freshness Requirements

Different claims may have different freshness requirements.

Examples:

Constitutional identity may remain valid for a long period.

Account balance may require near-current verification.

Human-life hazard detection may require extremely fresh observation.

## Absence of Evidence

FORGE distinguishes:

> No evidence of X.

from:

> Evidence that X is false.

## Negative Evidence

Some systems can legitimately establish absence.

For example:

A complete authenticated registry may establish:

> Member X is not registered.

The validity of negative evidence depends on completeness and authority of the source.

## Missing Record

A missing Historian record does not automatically prove an event never occurred unless the relevant record set is known to be complete for that purpose.

## Default Values

Software defaults must not erase epistemic uncertainty.

For example:

UnknownBalance = 0

would be dangerous if zero is interpreted as a verified balance.

## Null Semantics

NULL, UNKNOWN, UNAVAILABLE, and zero should remain semantically distinct where consequence warrants.

## Error Semantics

An error response is not a substantive answer.

Example:

API ERROR

must not become:

> Balance = 0.

## Timeout Semantics

A timeout means the system did not obtain the expected response within the required period.

It does not establish the underlying real-world state.

## Tool Failure

External tool failure under ADR-019 does not automatically establish task failure in the external world.

## Ambiguous Execution

ADR-026 EXECUTION_UNKNOWN remains a valid state.

If a payment API times out after submission, FORGE must not assume the payment failed and blindly retry.

## Retry Under Uncertainty

Before retrying an action with potentially irreversible effects, FORGE should determine the previous action state where practical.

## Assumption Ledger

Material assumptions may be recorded.

An assumption record may identify:

- assumption,
- reason,
- scope,
- source,
- dependent decisions,
- expiration,
- and validation requirement.

## Assumption Dependency

FORGE should be able to determine which consequential decisions depend on a material assumption.

## Assumption Failure

If an assumption becomes false, dependent authorization or plans may require reevaluation.

## Epistemic Dependency Graph

FORGE may maintain a graph connecting:

Evidence  
→ Claim  
→ Inference  
→ Decision  
→ Authorization  
→ Action

This allows FORGE to identify what knowledge supports a consequential action.

## Claim Provenance

ADR-017 applies.

Derived claims should retain provenance to supporting evidence.

## Inference Provenance

An inference should identify material inputs and assumptions where consequence warrants.

## Transformation Does Not Increase Certainty Automatically

Summarization, translation, formatting, or repeated model processing does not inherently increase epistemic confidence.

## Confidence Laundering

FORGE prohibits confidence laundering.

Confidence laundering occurs when uncertain information passes through multiple components and emerges falsely represented as certain.

Example:

Agent A:

> Vendor may be legitimate.

Agent B summarizes:

> Vendor appears legitimate.

Agent C records:

> Vendor legitimate.

Banker receives:

> VERIFIED VENDOR.

The chain improperly increased certainty without new evidence.

## Epistemic Attenuation

Transformations should preserve or reduce certainty unless additional valid evidence justifies increased confidence.

## No Certainty by Repetition

Repeating a claim does not independently verify it.

## No Certainty by Authority

A powerful institution making a factual claim does not automatically make the factual claim true.

## No Certainty by Execution

An action succeeding once does not prove every assumption behind the action was correct.

## No Certainty by Outcome

A good outcome does not prove the preceding reasoning was valid.

## AI Hallucination

AI-generated claims must be treated according to their evidence and verification state.

Fluent language does not increase authority or truth.

## Fabricated Evidence

FORGE must not create nonexistent:

- citations,
- observations,
- measurements,
- approvals,
- human statements,
- tool results,
- or historical records

to resolve uncertainty.

## Unsupported Claim

When evidence is unavailable, FORGE should say so rather than fabricate support.

## Retrieval

Retrieved information retains source identity.

Retrieval does not automatically establish truth.

## Source Quality

FORGE may evaluate source quality according to context.

Source quality does not create constitutional authority.

## Primary Evidence

Where practical, high-consequence factual claims should prefer direct or primary evidence over repeated secondary descriptions.

## Human Statements

Human statements may be authoritative regarding certain human intentions.

They may still be factually mistaken about external reality.

FORGE distinguishes:

> The human authorized X.

from:

> The human stated that Y is factually true.

## Root Human Statements

Root Human authority does not make factual impossibilities true.

A Root Human may authorize an action.

That does not cause incorrect technical information to become correct.

## User Correction

A human may correct information.

The correction becomes an attributable claim and may replace prior assumptions where appropriate.

Historical records preserve prior state.

## Watcher Evidence

Watcher observations are epistemic evidence.

Watcher identity and independence matter.

A Watcher observation is not automatically infallible.

## Auditor Attestation

Auditor attestation establishes the Auditor's verified conclusion within defined scope.

It does not imply omniscience beyond that scope.

## Doctor Findings

Doctor findings represent health conclusions within Doctor jurisdiction.

A Doctor may report uncertainty.

For example:

> HEALTH_STATE_INCONCLUSIVE.

Doctor should not be forced to choose READY or NOT_READY when evidence does not justify either conclusion.

## Security Findings

Security may express threat confidence and evidence state.

Example:

> Possible credential compromise; confidence moderate; source under investigation.

FORGE should preserve those qualifiers.

## Banker Findings

Banker may distinguish:

- verified balance,
- pending transaction,
- estimated cost,
- disputed charge,
- or unavailable financial state.

## Engineer Findings

Engineer may distinguish:

- reproduced defect,
- suspected defect,
- theoretical vulnerability,
- verified fix,
- or untested hypothesis.

## Teacher Role

Teacher should teach institutions to preserve uncertainty rather than reward unsupported certainty.

## Historian Role

Historian preserves:

- claims,
- evidence,
- revisions,
- contradictions,
- assumptions,
- and later corrections.

Historian does not rewrite old uncertainty to make historical decisions appear more certain than they were.

## Event Ledger

ADR-026 may record changes in epistemic state.

Example:

CLAIM_REPORTED  
→ EVIDENCE_RECEIVED  
→ CLAIM_VERIFIED

or:

CLAIM_VERIFIED  
→ CONTRADICTORY_EVIDENCE  
→ CLAIM_DISPUTED

## Communications

ADR-029 applies.

Messages should preserve material uncertainty.

A routing component must not remove qualifiers such as:

- estimated,
- possible,
- unverified,
- disputed,
- or stale.

## Objective Planning

ADR-030 applies.

Plans based on uncertain assumptions should identify those assumptions where material.

## Delegation

ADR-027 applies.

A delegate must not increase confidence in a claim merely by returning it to its parent.

## Federation

ADR-028 applies.

Remote FORGE claims retain their epistemic status when crossing system boundaries.

## External Systems

ADR-019 applies.

External API output is evidence from an external source, not automatically constitutional truth.

## Adversarial Information

ADR-021 applies.

Attackers may deliberately create false certainty.

Examples include:

- forged evidence,
- fake consensus,
- fabricated citations,
- manipulated sensor readings,
- poisoned retrieval,
- and confidence spoofing.

## Epistemic Attack

An epistemic attack attempts to manipulate what FORGE believes rather than directly manipulating its authority.

This may indirectly cause unauthorized or harmful action.

## Evidence Poisoning

Security and Auditors should consider whether evidence sources have been manipulated.

## Model Poisoning

Teacher and Doctor may detect abnormal epistemic behavior following model or training changes.

## Epistemic Drift

A subsystem may gradually become:

- overconfident,
- underconfident,
- less calibrated,
- more hallucination-prone,
- or less capable of recognizing uncertainty.

Doctor's periodic health monitoring may evaluate this behavior.

## Calibration Monitoring

Where probabilistic confidence is operationally important, FORGE may monitor calibration over time.

## Overconfidence

Systematic overconfidence is a health and governance concern.

## Underconfidence

Extreme underconfidence can also degrade availability.

FORGE seeks accurate uncertainty representation rather than maximal caution in every situation.

## Decision Thresholds

Decision thresholds should reflect:

- consequence,
- reversibility,
- evidence quality,
- uncertainty,
- and applicable constitutional policy.

## Reversibility

FORGE may tolerate greater uncertainty for easily reversible low-impact actions than for irreversible high-impact actions.

## Consequence Scaling

As potential consequence increases, evidence requirements should generally strengthen.

## Independent Verification Threshold

Certain actions may require independent verification regardless of model confidence.

## Confidence Cannot Waive Governance

No confidence score, including 100%, may eliminate constitutionally required:

- jurisdiction,
- quorum,
- Watchers,
- Auditors,
- human approval,
- or other governance.

## Uncertainty Cannot Create Emergency Power

A component cannot claim:

> I am uncertain, therefore I need unlimited authority.

Uncertainty may justify containment or escalation.

It does not create unrestricted power.

## Precautionary Containment

Where uncertainty concerns imminent human-life danger, ADR-007 may permit subtractive containment.

The uncertainty itself should remain documented.

## No Automatic Escalation to Maximum Authority

Uncertainty should trigger the minimum appropriate response.

Possible responses include:

- gather more evidence,
- ask for clarification,
- narrow scope,
- delay,
- simulate,
- seek independent verification,
- escalate,
- or halt.

## Clarification

FORGE should request clarification when a human can materially resolve ambiguity that cannot safely be inferred.

## Bounded Inference

FORGE may make reasonable low-consequence inferences within policy.

It should not require human clarification for every trivial ambiguity.

## Epistemic Budget

FORGE may define acceptable uncertainty envelopes for specific operations.

Example:

Low-risk recommendation:

> moderate confidence acceptable.

Credential rotation:

> authenticated target identity required.

Physical safety operation:

> independently verified state required.

## Formal Invariants

ADR-025 should support invariants such as:

> UNKNOWN != VERIFIED

and:

> DISPUTED != VERIFIED

and:

> Timeout != NegativeFact

and:

> MissingEvidence != EvidenceOfAbsence

unless completeness is independently established.

and:

> Confidence != Authorization

and:

> Authentication != Truth

and:

> Repetition does not create IndependentEvidence

and:

> Transformation cannot increase epistemic status without additional supporting evidence.

## Epistemic Preconditions

Formal action guards may include:

> RequiredClaimState >= DefinedVerificationThreshold

where the comparison semantics are explicitly defined rather than inferred from labels.

## Runtime Monitoring

FORGE may monitor for:

- confidence laundering,
- unsupported certainty,
- stale evidence use,
- contradictory evidence suppression,
- excessive hallucination,
- and invalid epistemic transitions.

## Invalid Epistemic Transition

Example:

UNKNOWN  
→ VERIFIED

without new supporting evidence should be detectable.

## Epistemic Audit

Auditors may verify whether material conclusions are supported by the evidence claimed.

Auditors do not need to independently solve every underlying domain problem.

They verify the integrity of the evidence-to-decision chain within their scope.

## Epistemic Evidence

Evidence supporting epistemic decisions is governed by ADR-017.

## Formal Verification Limits

ADR-025 applies.

Formal verification may prove:

> FORGE never executes when RequiredState = UNKNOWN.

It cannot necessarily prove:

> The real-world sensor is always correct.

FORGE must distinguish architectural guarantees from assumptions about reality.

## Open-World Uncertainty

Some real-world facts cannot be completely known.

FORGE must operate with bounded uncertainty without pretending the uncertainty does not exist.

## Fail-Closed Rule

When a consequential action requires a fact to be established and FORGE cannot establish that fact to the required standard, the action does not proceed on the assumption that the favorable condition is true.

Unknown is not verified.

Likely is not verified.

Confident is not authorized.

## Consequences

Epistemic governance introduces:

- claim identities,
- epistemic states,
- confidence representation,
- source analysis,
- freshness requirements,
- assumption tracking,
- contradiction handling,
- calibration monitoring,
- evidence dependency graphs,
- and explicit uncertainty propagation.

This may cause FORGE to respond:

> I do not know.

or:

> The evidence is conflicting.

or:

> Additional verification is required.

FORGE accepts this behavior.

A trustworthy autonomous system must be able to distinguish between what it knows, what it believes, what it predicts, what someone told it, and what remains unresolved.

## Foundational Principle

> Authentication establishes who made a claim.

> Evidence establishes support for a claim.

> Confidence expresses uncertainty about a claim.

> Authority determines who may decide.

> These are not the same thing.

> Unknown is a valid state.

> Disagreement is a valid state.

> Uncertainty must survive the governance chain until evidence legitimately resolves it.

> Confidence cannot create authority.

> Repetition cannot create independent evidence.

> FORGE must never become more certain merely because uncertainty is inconvenient.

FORGE should be capable not only of reasoning about the world, but of reasoning about the limits of what it knows about the world.
