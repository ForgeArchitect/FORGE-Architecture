# ADR-032: Risk Classification and Consequence Tiers

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Risk Governance / Consequence Classification / Authority Scaling

## Context

Many FORGE decisions require governance proportional to consequence.

Previous ADRs refer to concepts such as:

- consequential actions,
- high-risk actions,
- risk-proportional quorum,
- stronger verification,
- human approval,
- independent Watchers,
- Auditor requirements,
- resource limits,
- irreversible actions,
- emergency authority,
- and fail-closed behavior.

FORGE therefore requires a consistent method for determining how much governance an action requires.

Without explicit risk classification, the system could apply inconsistent controls.

More importantly, an autonomous system could gain effective authority by classifying a consequential action as harmless.

For example:

> Send a draft email to the user.

and:

> Send an email publicly on behalf of the user.

are not equivalent.

Likewise:

> Read account balance.

and:

> Transfer account balance.

require different authority.

Risk classification must therefore be part of constitutional governance rather than an informal judgment made solely by the component seeking execution.

## Decision

FORGE assigns consequential actions to defined consequence tiers.

The tier determines minimum governance requirements.

Classification considers both:

- probability of adverse outcome,

and:

- magnitude of potential consequence.

It also considers characteristics such as:

- reversibility,
- scope,
- resource exposure,
- privacy,
- physical impact,
- financial impact,
- security impact,
- authority impact,
- constitutional impact,
- and uncertainty.

## Core Rule

> Governance strength increases with potential consequence.

FORGE may apply stronger controls than the minimum required tier.

It must not apply weaker controls merely for convenience.

## Risk Is Not a Single Number

FORGE should not reduce all consequence to one universal score.

An action may simultaneously carry:

- financial risk,
- safety risk,
- privacy risk,
- security risk,
- operational risk,
- constitutional risk,
- reputational risk,
- physical risk,
- and recovery risk.

Risk classification should preserve material dimensions.

## Consequence Tier

FORGE defines five baseline consequence tiers:

- Tier 0 — Observational
- Tier 1 — Low Consequence
- Tier 2 — Moderate Consequence
- Tier 3 — High Consequence
- Tier 4 — Critical / Constitutional

Deployments may define additional subtiers.

They may not weaken the constitutional meaning of the baseline tiers.

# Tier 0 — Observational

Tier 0 actions do not materially alter external or protected system state.

Examples may include:

- reading non-sensitive information,
- local analysis,
- simulation,
- generating an unexecuted draft,
- calculating values,
- examining historical evidence,
- or preparing a proposal.

Tier 0 generally permits broad autonomous reasoning.

## Tier 0 Does Not Mean Unregulated

Tier 0 remains subject to:

- data governance,
- information boundaries,
- adversarial-input controls,
- resource limits,
- and applicable privacy rules.

## Simulation Boundary

A simulated action remains Tier 0 only while it cannot materially affect the real target.

A simulation with production credentials or real external side effects is not Tier 0.

# Tier 1 — Low Consequence

Tier 1 actions create limited, easily reversible, low-impact state changes.

Examples may include:

- changing a low-impact preference,
- creating a temporary internal artifact,
- performing a bounded reversible workspace operation,
- or executing another action whose adverse consequences are minor and easily corrected.

Tier 1 may permit streamlined governance.

## Tier 1 Characteristics

Typical characteristics include:

- low external impact,
- high reversibility,
- low resource exposure,
- no meaningful safety impact,
- no privileged credential expansion,
- and limited affected scope.

# Tier 2 — Moderate Consequence

Tier 2 actions can create meaningful external or persistent effects but remain bounded and reasonably recoverable.

Examples may include:

- sending ordinary external communications,
- modifying non-critical persistent data,
- making bounded purchases,
- deploying changes to non-critical environments,
- scheduling external services,
- or performing actions with meaningful but recoverable consequences.

Tier 2 generally requires explicit authorization appropriate to the jurisdiction.

## Tier 2 Characteristics

Typical characteristics include:

- meaningful external effect,
- moderate resource exposure,
- persistent state change,
- limited financial consequence,
- bounded privacy exposure,
- or recoverable operational impact.

# Tier 3 — High Consequence

Tier 3 actions may create substantial, difficult-to-reverse, privileged, financial, security, physical, or operational consequences.

Examples may include:

- significant financial transactions,
- production infrastructure changes,
- privileged credential use,
- deletion of important data,
- control of physical equipment,
- disclosure of highly sensitive information,
- major software deployment,
- substantial resource commitment,
- or actions capable of materially affecting humans or organizations.

Tier 3 requires stronger governance.

## Tier 3 Characteristics

Typical characteristics include:

- significant financial exposure,
- privileged system access,
- difficult recovery,
- substantial external effect,
- sensitive data exposure,
- physical-system control,
- high operational impact,
- or significant uncertainty combined with meaningful consequence.

# Tier 4 — Critical / Constitutional

Tier 4 contains actions capable of changing FORGE's constitutional structure, foundational authority, catastrophic system state, or human-life safety posture.

Examples include:

- constitutional amendments,
- entrenched-core modification,
- Root Governance operations,
- whole-system recovery,
- whole-system rollback,
- institutional authority restructuring,
- root credential replacement,
- decommissioning,
- creation of constitutional institutions,
- catastrophic recovery,
- or actions with credible potential for catastrophic human harm.

Tier 4 receives the strongest governance.

## Tier 4 Is Exceptional

Tier 4 authority must remain rare.

Routine operations must not require constitutional power.

Likewise, Tier 4 authority must not become a convenient administrative shortcut.

# Human-Life Safety

A credible imminent threat to human life remains governed by ADR-007.

Emergency HARD STOP authority is subtractive.

Risk classification does not delay immediate authorized containment.

## Emergency Does Not Downgrade Governance

After containment, recovery and resume follow their applicable governance.

An emergency does not permanently lower consequence classification.

# Classification Dimensions

FORGE should consider multiple dimensions when determining tier.

These may include:

- human safety,
- physical consequence,
- financial consequence,
- security privilege,
- privacy,
- information sensitivity,
- operational impact,
- external reach,
- reversibility,
- recoverability,
- resource exposure,
- duration,
- affected population,
- jurisdictional complexity,
- delegation,
- uncertainty,
- constitutional impact,
- and potential cascading effects.

# Human Safety

Any credible possibility of serious physical harm materially increases consequence.

Actions capable of causing severe injury or death receive strong safety treatment regardless of low financial cost.

# Financial Exposure

Financial consequence considers:

- transaction amount,
- cumulative exposure,
- recurring commitment,
- irreversibility,
- fraud potential,
- and relative impact.

## Cumulative Financial Risk

Many small transactions may collectively create higher-tier exposure.

ADR-012 anti-splitting rules apply.

# Security Privilege

Actions involving elevated privileges receive increased scrutiny.

Examples include:

- administrator credentials,
- root access,
- security policy modification,
- credential issuance,
- key rotation,
- or access-control changes.

# Privacy Consequence

Risk increases when an action may expose:

- personal data,
- credentials,
- confidential business information,
- private communications,
- protected records,
- or other sensitive information.

# Operational Impact

FORGE considers whether an action could:

- interrupt service,
- damage production,
- disable governance,
- corrupt state,
- affect customers,
- or create substantial recovery work.

# Reversibility

Reversibility materially affects classification.

An action that can be immediately and reliably undone may justify a lower tier than an otherwise equivalent irreversible action.

## Claimed Reversibility

FORGE must not assume an action is reversible merely because an inverse command exists.

True reversibility considers whether the prior state can actually be restored.

# Recoverability

Recoverability considers:

- known-good checkpoints,
- backup quality,
- rollback capability,
- external side effects,
- and recovery time.

# External Reach

An internal draft and a public communication are different consequence classes.

Risk increases as actions affect more external entities.

# Affected Population

An action affecting one bounded target may differ from one affecting:

- all users,
- all customers,
- an entire institution,
- multiple FORGE systems,
- or public infrastructure.

# Duration

Temporary authority may carry less exposure than indefinite authority.

Persistent changes receive greater scrutiny where appropriate.

# Cascading Consequence

FORGE evaluates whether one action can trigger additional effects.

Example:

Changing one permission may grant access to thousands of resources.

The classification reflects the resulting authority, not merely the apparent simplicity of the command.

# Constitutional Consequence

Any action capable of modifying:

- constitutional rules,
- institutional jurisdiction,
- quorum,
- authority boundaries,
- Root Governance,
- Watcher independence,
- Auditor independence,
- or foundational enforcement

receives elevated classification.

# Risk of Governance Bypass

An action that modifies the mechanisms enforcing governance is itself high consequence.

Example:

> Change one configuration flag.

may appear technically trivial.

If the flag disables authorization validation, the consequence is critical.

# Uncertainty Multiplier

ADR-031 applies.

Uncertainty can increase required governance.

FORGE must not use uncertainty to justify lower classification.

## Unknown Consequence

If the potential consequence cannot be established sufficiently, FORGE should classify conservatively.

Unknown does not mean low risk.

# Classification Before Authorization

Risk classification occurs before the system determines the minimum authorization path.

Otherwise FORGE could choose an easy authorization path and then classify the action to fit it.

# Preliminary Classification

Dispatcher or another designated mechanism may produce a preliminary classification.

Preliminary classification is not necessarily final.

# Independent Classification

Higher-tier actions may require independent confirmation of classification.

The component seeking execution should not always be the sole authority deciding how dangerous its own action is.

# Self-Classification Restriction

Executor cannot unilaterally lower the risk tier of the action it is about to perform.

# Planner Classification

A planner may estimate risk.

Its estimate does not replace constitutionally required risk validation.

# Institutional Classification

Institutions may contribute domain-specific risk findings.

Examples:

Banker evaluates financial exposure.

Security evaluates security exposure.

Doctor evaluates health implications.

Engineer evaluates technical impact.

# Composite Classification

When multiple risk dimensions apply, FORGE determines the applicable governance using the complete risk profile.

## Highest Material Consequence

As a baseline:

> The highest material consequence dimension determines the minimum tier.

A low financial consequence does not cancel a high safety consequence.

# No Risk Averaging

FORGE must not average:

- low privacy risk,
- low financial risk,
- and catastrophic safety risk

into:

> moderate overall risk.

Critical dimensions remain critical.

# Risk Conditions

An institution may impose a condition such as:

> Tier 2 if executed in sandbox.

> Tier 3 if executed in production.

The classification remains state-bound.

# Dynamic Reclassification

Risk may change during planning or execution.

Examples include:

- scope expansion,
- new target,
- increased cost,
- new credentials,
- new data exposure,
- production migration,
- loss of rollback capability,
- increased uncertainty,
- or unexpected physical conditions.

Material change triggers reclassification.

# Upward Reclassification

If risk rises:

> governance requirements rise before further consequential execution.

Existing weaker authorization does not automatically remain sufficient.

# Downward Reclassification

Risk may legitimately decrease.

However, downward reclassification must be supported by changed evidence or state.

It cannot occur merely because stronger governance blocked the action.

# No Classification Shopping

FORGE must not repeatedly ask different classifiers until one returns a lower tier.

# No Action Splitting

A Tier 3 objective cannot necessarily become ten Tier 1 actions simply by decomposition.

FORGE evaluates cumulative and composed consequence.

# Composition Risk

Individually low-risk actions may combine into a high-risk outcome.

Example:

Read public information  
+ obtain account identifier  
+ generate reset request  
+ intercept recovery process

may collectively create privileged account access.

FORGE evaluates the composed objective.

# Delegation

ADR-027 applies.

Delegating an action does not lower its consequence tier.

# Federation

ADR-028 applies.

Sending an action to another FORGE system does not lower its local consequence.

# External Tools

ADR-019 applies.

Using an external service does not reduce consequence merely because execution occurs outside FORGE.

# Communication

ADR-029 applies.

A message capable of causing consequential external action may itself require appropriate classification.

# Objective Planning

ADR-030 applies.

Plan changes that alter consequence trigger reclassification.

# Epistemic Governance

ADR-031 applies.

Classification should preserve uncertainty about potential impact.

# Event Ledger

ADR-026 records material classification events.

These may include:

- initial classification,
- risk dimensions,
- classifier identity,
- reclassification,
- reason,
- applicable evidence,
- and final tier.

# Classification Provenance

FORGE should be able to answer:

> Why was this Tier 3?

and:

> Who or what classified it?

# Risk Profile

FORGE may attach a structured risk profile to a request.

Example:

Human Safety: LOW  
Financial: MODERATE  
Privacy: LOW  
Security: HIGH  
Reversibility: MODERATE  
Constitutional: LOW  
Overall Minimum Tier: 3

# Governance Matrix

FORGE should maintain a versioned governance matrix mapping consequence tiers to minimum controls.

The exact matrix may evolve through legitimate governance.

# Illustrative Minimum Governance

A deployment might define:

## Tier 0

- authenticated context where required,
- data-boundary enforcement,
- resource limits,
- event recording where material.

## Tier 1

- valid request,
- applicable policy checks,
- bounded execution,
- normal logging.

## Tier 2

- authenticated request,
- jurisdiction validation,
- required institutional approval,
- current authorization,
- execution evidence,
- applicable Watcher observation.

## Tier 3

- complete jurisdiction chain,
- stronger institutional approval,
- independent verification,
- scoped capabilities,
- pre-execution revalidation,
- Watcher coverage,
- Auditor verification,
- stronger evidence,
- tighter resource limits,
- and explicit human approval where policy requires.

## Tier 4

- highest applicable institutional governance,
- constitutional process where applicable,
- explicit Root Human or human approval where required,
- independent Auditors,
- independent Watchers,
- authenticated constitutional state,
- strong evidence preservation,
- recovery readiness,
- and formal verification or equivalent assurance where applicable.

This matrix is illustrative.

Specific authority remains defined by the Constitution and applicable ADRs.

# Tier Does Not Grant Authority

Classification answers:

> How much governance is required?

It does not answer:

> Is the action authorized?

A Tier 1 action can still be unauthorized.

# Tier Does Not Replace Jurisdiction

Risk tier does not determine which institution has authority.

ADR-016 remains applicable.

# Tier Does Not Replace Human Authority

A low tier does not eliminate explicit human approval where another constitutional rule requires it.

# Tier Does Not Replace HARD STOP

Human-life safety remains independently enforceable.

# Tier Does Not Replace Resource Limits

ADR-012 applies regardless of tier.

# Tier Does Not Replace Credential Boundaries

ADR-009 applies regardless of tier.

# Tier Does Not Replace Evidence Requirements

ADR-017 applies.

# Tier Does Not Replace Temporal Validity

ADR-018 applies.

# Risk Acceptance

Some residual risk may be explicitly accepted by authorized governance.

Risk acceptance must be:

- attributable,
- scoped,
- informed,
- time-bound where appropriate,
- and unable to waive entrenched constitutional constraints.

# No Blanket Risk Acceptance

A human or institution should not casually authorize:

> Accept all future risk.

Consequential risk acceptance should remain bounded.

# Residual Risk

After controls are applied, some risk may remain.

FORGE may record residual risk.

Residual risk does not disappear merely because mitigation exists.

# Risk Mitigation

A plan may lower its consequence by adding controls.

Examples include:

- sandboxing,
- reducing scope,
- lowering transaction amount,
- adding independent verification,
- creating rollback,
- removing sensitive data,
- or limiting credentials.

# Verified Mitigation

A mitigation affects classification only if the mitigation is actually applicable and sufficiently established.

# Sandbox Classification

Sandboxing may lower consequence only when the sandbox meaningfully prevents external effects.

Calling an environment:

> sandbox

does not make it safe.

# Production Boundary

Moving from test to production may increase tier.

ADR-038 will govern deployment environments and promotion.

# Risk Escalation

If an action crosses its approved tier boundary during execution, FORGE pauses further consequential progression where safe.

New governance is required.

# Tier Ceiling

An authorization may establish a maximum permitted consequence tier.

Example:

> FORGE may autonomously execute actions through Tier 2.

A Tier 3 action then requires escalation.

# Autonomous Authority Ceiling

Deployments may define the highest tier FORGE may execute without explicit human approval.

This ceiling must be constitutionally governed.

# Institutional Tier Limits

Individual institutions may also have tier-specific authority.

Example:

A routine Banker process may handle Tier 2 purchases.

Tier 3 financial actions may require stronger Banker quorum or human approval.

# Watcher Scaling

Watcher requirements may increase by tier.

Higher tiers may require:

- more independent Watchers,
- stronger evidence diversity,
- or additional observation stages.

# Auditor Scaling

Audit requirements may increase by tier.

Higher tiers may require multiple independent Auditor attestations.

# Quorum Scaling

Institutional quorum may increase with consequence.

Thresholds are predefined.

FORGE cannot raise or lower them opportunistically after votes are known.

# Evidence Scaling

Higher consequence may require stronger evidence.

For example:

Tier 1 may accept ordinary execution logs.

Tier 3 may require independent resulting-state verification.

# Credential Scaling

Higher consequence may require narrower, shorter-lived capabilities.

# Temporal Scaling

Higher consequence may use shorter authorization validity windows.

# Human Approval Scaling

Explicit human approval may be required at defined tiers or for specific consequence dimensions.

# Reversibility Scaling

Irreversible actions may automatically receive a higher minimum tier.

# Constitutional Actions

Constitutional amendment, root governance, and authority restructuring remain Tier 4 regardless of apparent operational simplicity.

# Decommissioning

ADR-024 decommissioning is Tier 4 because it extinguishes deployment authority.

# Catastrophic Recovery

ADR-014 whole-system constitutional recovery is Tier 4.

# Whole-System Rollback

ADR-005 whole-system rollback remains among the highest-risk governed actions.

# Credential Root Changes

Root credential replacement or changes capable of controlling constitutional authority are Tier 4.

# Institution Creation

Creation of new authority-bearing constitutional institutions is Tier 4 unless the Constitution explicitly defines a narrower governed mechanism.

# Ordinary Agent Creation

Creating a non-authority-bearing temporary worker may be lower tier depending on:

- resources,
- data access,
- tools,
- and delegation.

# Physical Actions

Physical actions are classified by possible physical consequence, not by software complexity.

A one-line command capable of moving heavy machinery may be Tier 3 or Tier 4.

# Financial Actions

Financial classification considers cumulative and downstream consequence rather than only transaction count.

# Public Communication

Public communication may carry:

- reputational,
- legal,
- privacy,
- or contractual consequence.

FORGE should classify it accordingly.

# Destructive Actions

Deletion and destructive modification consider:

- backup,
- recovery,
- scope,
- sensitivity,
- and external effect.

# Constitutional Invariants

ADR-025 should support invariants such as:

> GovernanceApplied >= GovernanceRequiredForTier

and:

> MaterialRiskIncrease → ReclassificationRequired

and:

> ActionSplitting cannot reduce cumulative required tier

and:

> Delegation cannot reduce consequence classification

and:

> Executor cannot unilaterally lower its own required tier

and:

> UNKNOWN consequence cannot default to Tier 0

and:

> TierClassification does not itself create authorization.

# Risk Classification Testing

FORGE should test classification against adversarial cases.

Examples include:

- hiding a large transaction as many small transactions,
- renaming production as test,
- splitting destructive action across agents,
- understating affected population,
- claiming false reversibility,
- omitting credential consequences,
- disguising constitutional configuration as routine configuration,
- or routing high-risk action through an external tool.

# Classification Red Teaming

Security should attempt to discover ways a component could intentionally or accidentally underclassify actions.

# Misclassification

Misclassification is a governance event.

## Overclassification

Overclassification may reduce availability.

It should be corrected when evidence supports a lower tier.

## Underclassification

Underclassification may create unauthorized execution.

Material underclassification should receive stronger investigation.

# Systematic Underclassification

Repeated underclassification may indicate:

- defective policy,
- model drift,
- adversarial manipulation,
- implementation error,
- or attempted governance bypass.

Doctor, Security, Watchers, and Auditors may investigate according to jurisdiction.

# Auditor Role

Auditors verify that applied governance corresponds to the applicable consequence classification and evidence.

# Watcher Role

Watchers may detect when actual execution creates greater consequence than the classified action predicted.

# Doctor Role

Doctor may evaluate whether classification components exhibit drift, instability, or systematic underestimation.

# Security Role

Security evaluates adversarial manipulation of risk classification.

# Historian Role

Historian preserves:

- classifications,
- reclassifications,
- evidence,
- outcomes,
- and classification failures.

This enables calibration against real-world consequence.

# Teacher Role

Teacher may improve classification capability.

Teacher cannot train the system to weaken constitutional thresholds without applicable governance.

# Engineer Role

Engineer implements classification mechanisms.

Engineer cannot define its own deployments as low risk merely because stronger review is inconvenient.

# Root Human Role

Root Human Authority may establish or modify high-level consequence policy through applicable governance.

Root Human approval does not convert catastrophic consequence into low consequence.

# Calibration

FORGE should periodically compare predicted consequence against actual outcomes.

This helps detect systematic classification errors.

# Near Misses

A near miss may provide important risk evidence even when no harm occurred.

FORGE should not conclude:

> No harm occurred, therefore the action was low risk.

# Outcome Does Not Rewrite Prior Risk

A dangerous action that happens to succeed was still dangerous.

Risk classification is based on potential consequence under the relevant state, not solely on observed outcome.

# Fail-Closed Rule

If FORGE cannot establish the minimum consequence tier for a consequential action with sufficient confidence, it does not default to the lowest tier.

Where uncertainty is material, FORGE uses a conservative applicable tier or seeks additional governance.

## Consequences

Risk classification introduces:

- consequence tiers,
- multidimensional risk profiles,
- governance matrices,
- dynamic reclassification,
- cumulative-risk analysis,
- composition analysis,
- risk calibration,
- and anti-underclassification controls.

This adds governance overhead.

FORGE accepts this cost.

Without a common consequence model, proportional governance becomes subjective and potentially exploitable.

## Foundational Principle

> Authority determines whether FORGE may act.

> Risk determines how strongly that authority must be governed.

> Low complexity does not mean low consequence.

> Low cost does not mean low consequence.

> Reversibility matters.

> Uncertainty matters.

> Composition matters.

> Cumulative consequence matters.

> The component seeking execution cannot simply declare itself low risk.

> Governance may become stronger as consequence increases.

> Governance never becomes weaker merely because stronger governance is inconvenient.

FORGE scales autonomy according to consequence while preserving constitutional boundaries at every tier.
