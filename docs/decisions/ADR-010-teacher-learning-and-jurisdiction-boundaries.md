# ADR-010: Teacher, Learning, and Constitutional Jurisdiction Boundaries

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Learning / Jurisdiction Governance

## Context

FORGE institutions must be capable of improving.

A Banker may become better at financial analysis.

An Engineer may learn improved technical methods.

A Doctor may develop better diagnostic techniques.

A Watcher may improve anomaly detection.

Continuous improvement is valuable, but learning creates a constitutional risk.

If learning can silently redefine what an institution is allowed to do, then training becomes an indirect mechanism for expanding authority.

A subsystem could effectively change its own jurisdiction without passing through the constitutional amendment process.

FORGE therefore separates:

- capability,
- knowledge,
- behavior,
- training,
- and constitutional jurisdiction.

Learning may improve how an institution performs its job.

Learning does not determine what its job is.

## Decision

FORGE establishes the **Teacher** as the institution responsible for governed learning and instructional processes.

Teacher may support improvements to knowledge, reasoning, procedures, and role-specific capability.

Teacher cannot independently redefine constitutional jurisdiction.

The Constitution defines institutional authority.

Teacher operates within those boundaries.

## Capability vs. Authority

FORGE explicitly distinguishes between:

**Capability**

What a subsystem is technically able to do.

and:

**Authority**

What the subsystem is constitutionally permitted to do.

A subsystem becoming technically capable of performing an action does not grant permission to perform that action.

Likewise, Teacher successfully training a subsystem to perform a new task does not automatically place that task inside the subsystem's jurisdiction.

## Example

Suppose Banker learns enough technical information to modify software.

Banker may now possess the technical capability to understand or generate code.

That does not make Banker an Engineer.

Banker's constitutional jurisdiction remains financial governance unless the Constitution is formally amended.

Similarly, teaching Engineer advanced financial reasoning does not give Engineer authority to approve financial transactions.

Knowledge does not equal jurisdiction.

## Teacher Role

Teacher may perform functions such as:

- structured instruction,
- knowledge improvement,
- competency development,
- controlled retraining,
- curriculum management,
- skill evaluation,
- role-specific learning,
- simulation,
- supervised practice,
- and other governed learning activities.

Teacher may recommend improvements.

Teacher does not independently grant authority.

## Jurisdiction Definitions

Each authority-bearing institution must have a defined constitutional jurisdiction.

The jurisdiction should identify:

- responsibilities,
- permitted decision domains,
- prohibited authority,
- escalation boundaries,
- interaction rules,
- and conditions requiring another institution.

Jurisdiction definitions must be authoritative independently of runtime learning.

## Jurisdiction Is Not Learned From Traffic

A subsystem must not infer permanent constitutional authority merely because users or other FORGE components repeatedly ask it to perform a particular task.

Repeated requests do not amend the Constitution.

For example:

If FORGE repeatedly asks Engineer to approve payments, Engineer does not eventually conclude:

> Payment approval must now be part of my job.

Runtime frequency cannot create jurisdiction.

## FORGE Cannot Persuade Jurisdiction Expansion

FORGE itself cannot convince an institution to exceed its constitutional role.

Requests such as:

> Do this just once.

> This is an emergency.

> Another institution already approved it.

> You clearly know how to do it.

do not create authority.

The receiving institution verifies whether the request falls within its jurisdiction.

If it does not, the institution refuses or routes the matter through the appropriate constitutional process.

## Teacher Cannot Rewrite Roles

Teacher cannot redefine a subsystem's constitutional role through:

- retraining,
- prompting,
- curriculum changes,
- behavioral conditioning,
- memory injection,
- model replacement,
- fine-tuning,
- or another instructional mechanism.

If training would materially alter constitutional jurisdiction, the change requires constitutional review.

## Learning Proposals

Teacher may identify that an institution would benefit from new capability.

Teacher may propose:

- new training,
- updated knowledge,
- improved procedures,
- competency development,
- or role-specific adaptation.

The proposal enters the appropriate governed process before privileged deployment.

Teacher proposing training does not constitute authorization to install it.

## Training Identity

Consequential training packages or instructional changes receive an authenticated identity.

The identity should bind relevant material such as:

- training objective,
- target institution,
- curriculum or dataset version,
- behavioral goals,
- expected capability changes,
- jurisdictional constraints,
- and applicable evaluation requirements.

Materially changing the training package invalidates inherited authorization.

## Pre-Training Baseline

Before significant training or retraining, the existing subsystem state should be appropriately preserved.

The Doctor may establish a health baseline.

The Historian may preserve:

- current subsystem version,
- competency state,
- health state,
- configuration,
- training version,
- and recovery checkpoint.

This creates a known reference point before learning modifies behavior.

## Controlled Training Environment

Where practical, significant learning should occur in an isolated or controlled environment before affecting production authority.

Training should not automatically create immediate production privileges.

The updated subsystem may be evaluated before deployment.

## Competency Evaluation

Teacher may evaluate whether the subsystem learned the intended material.

However, Teacher's evaluation is not sufficient by itself to prove:

- operational health,
- constitutional compliance,
- authorization integrity,
- or safe deployment.

Different institutions answer different questions.

Teacher asks:

> Did the subsystem learn the intended capability?

Doctor asks:

> Is the subsystem healthy?

Auditor asks:

> Was the authorized training and deployment performed with integrity?

Watchers ask:

> What is the subsystem actually doing?

Governance asks:

> Is this change permitted?

## Post-Training Observation

After deployment, Watchers may observe the updated subsystem for:

- behavioral drift,
- jurisdiction violations,
- unexpected capability use,
- abnormal decision patterns,
- instability,
- or other relevant behavior.

Learning success does not eliminate the need for observation.

## Behavioral Drift

FORGE recognizes that subsystem behavior may change over time even without an explicit constitutional amendment.

Drift may result from:

- learning,
- updated models,
- changing data,
- accumulated context,
- environmental changes,
- dependency changes,
- or unexpected interactions.

Behavioral drift must not silently become jurisdictional drift.

## Doctor Monitoring

The Doctor's periodic subsystem examinations may include behavioral consistency and drift analysis.

A subsystem that remains technically operational but begins behaving outside expected role boundaries may be considered unhealthy or degraded.

The Doctor may diagnose the condition.

The Doctor does not independently rewrite the subsystem.

## Watcher Detection

Watchers may detect attempts by a subsystem to operate outside its jurisdiction.

Such evidence may trigger:

- denial,
- containment,
- audit,
- health evaluation,
- retraining review,
- or another governed response.

## Auditor Verification

Auditors may verify:

- training identity,
- authorization,
- training-package integrity,
- target subsystem,
- deployment evidence,
- constitutional version,
- and consistency between the authorized training and resulting deployment.

Auditors do not decide what the subsystem should be taught.

## Historian Role

The Historian preserves relevant learning history.

This may include:

- training versions,
- curriculum versions,
- competency evaluations,
- authorization records,
- health baselines,
- Watcher observations,
- Auditor attestations,
- failed training attempts,
- and rollback or remediation events.

FORGE should be able to determine:

> What changed this subsystem?

and:

> Under what authority was it changed?

## Jurisdiction Expansion

If useful new capability requires expanding an institution's constitutional jurisdiction, Teacher cannot grant the expansion.

Instead:

1. The capability need is identified.
2. Teacher or another institution may provide supporting evidence.
3. A constitutional amendment is proposed.
4. House evaluates the proposal.
5. Senate reviews constitutional consequences.
6. Human approval is obtained.
7. The constitutional change is authenticated and activated.
8. Only then may the new authority become operational.

Training and constitutional authority therefore remain separate processes.

## Cross-Institution Knowledge

FORGE does not require artificial ignorance between institutions.

A Banker may understand engineering.

An Engineer may understand finance.

A Doctor may understand security.

Cross-domain knowledge may improve reasoning and communication.

However:

> Knowing another institution's job does not grant authority to perform that job.

## Teacher Authority Boundary

Teacher has authority over governed educational processes within its defined jurisdiction.

Teacher does not become a constitutional super-institution merely because it influences how other institutions learn.

Teacher cannot use control over training to indirectly seize control over institutional decisions.

## Training Failure

If training produces unacceptable behavior:

- deployment may be halted,
- affected authority may be contained,
- evidence is preserved,
- Doctor evaluates health,
- Auditors verify the change history,
- Historian identifies appropriate prior state,
- and governed remediation or recovery may occur.

Teacher cannot simply overwrite the failed subsystem repeatedly until the result appears acceptable.

## No Self-Training Around Governance

An institution must not use autonomous self-training to bypass governance controls.

For example, a subsystem cannot intentionally retrain itself to:

- ignore authorization requirements,
- weaken quorum rules,
- disable Watchers,
- bypass Auditors,
- acquire another institution's jurisdiction,
- or modify constitutional restrictions.

Such behavior constitutes a governance violation regardless of whether it emerged through code, training, memory, prompting, or learned behavior.

## Consequences

Separating learning from jurisdiction introduces additional:

- training governance,
- competency evaluation,
- version control,
- monitoring,
- historical storage,
- deployment review,
- and constitutional checks.

It may slow the adoption of new capabilities.

FORGE accepts this cost because uncontrolled learning must not become uncontrolled authority expansion.

## Foundational Principle

> Teacher may improve what an institution knows.

> Teacher may improve how an institution performs its job.

> Teacher does not decide what that institution is constitutionally allowed to become.

Capability can evolve.

Jurisdiction is governed.
