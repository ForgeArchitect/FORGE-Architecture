# ADR-034: Transaction Atomicity and Partial-Failure Governance

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Transactions / Failure Handling / Execution Integrity

## Context

Consequential actions are not always single operations.

A FORGE objective may require multiple steps.

Examples include:

- reserve funds,
- place an order,
- schedule delivery,
- update inventory,
- notify stakeholders,

or:

- create backup,
- deploy software,
- migrate state,
- restart service,
- verify health,

or:

- acquire physical control,
- move equipment,
- confirm resulting position,
- release control.

Failure can occur between any two steps.

External systems may also produce ambiguous results.

For example:

FORGE submits:

> Transfer $5,000.

The banking API times out.

FORGE now does not know whether:

- the transfer failed,
- the transfer succeeded,
- the transfer remains pending,
- or the response was simply lost.

Blindly retrying could transfer $10,000.

Assuming success could leave the intended transaction incomplete.

Similar failures can occur during:

- purchases,
- deployments,
- file operations,
- credential changes,
- physical actions,
- external communications,
- recovery,
- federation,
- and decommissioning.

FORGE therefore requires explicit governance for atomicity, partial completion, ambiguous execution, retry, compensation, and recovery.

## Decision

FORGE represents consequential multi-step execution as governed transactions or equivalent stateful execution processes.

Each material step has explicit state.

Partial execution must remain visible.

Unknown execution state must remain unknown until resolved.

Retry, rollback, compensation, or continuation requires applicable authority.

## Core Rule

> FORGE must never confuse incomplete knowledge about execution with knowledge that execution did not occur.

And:

> Partial success is a state, not permission to improvise.

## Transaction

A transaction is a governed collection of related actions intended to produce a defined outcome.

A transaction may be:

- atomic,
- partially atomic,
- compensatable,
- staged,
- irreversible,
- distributed,
- or externally coordinated.

## Transaction Identity

Consequential transactions should receive unique identity.

Example:

`TX-2026-00482`

The identity should remain associated with:

- request,
- objective,
- plan,
- authorization,
- actions,
- capabilities,
- evidence,
- resulting state,
- and recovery.

## Transaction State

A transaction may occupy states such as:

- CREATED,
- AUTHORIZED,
- PREPARING,
- READY,
- EXECUTING,
- PARTIALLY_COMPLETED,
- COMMITTED,
- EXECUTION_UNKNOWN,
- COMPENSATING,
- COMPENSATED,
- FAILED,
- SUSPENDED,
- CANCELED,
- RECOVERY_REQUIRED,
- or CLOSED.

Exact implementation terminology may vary.

The semantics must remain explicit.

## CREATED

The transaction exists but has not yet received required authority.

## AUTHORIZED

Required authority has been established for the applicable transaction scope.

## PREPARING

FORGE is establishing preconditions required for execution.

## READY

Required preconditions are established and the transaction is eligible to begin execution.

## EXECUTING

At least one consequential operation is actively being attempted.

## PARTIALLY_COMPLETED

Some intended effects have occurred while others have not.

## COMMITTED

The transaction's required commit conditions have been satisfied.

## EXECUTION_UNKNOWN

FORGE cannot currently establish whether one or more material external effects occurred.

## COMPENSATING

FORGE is performing separately authorized actions intended to mitigate or reverse completed effects.

## COMPENSATED

Defined compensation has completed.

This does not necessarily mean the world has returned to its exact original state.

## FAILED

The transaction failed according to defined failure criteria.

## SUSPENDED

Further consequential progress has been intentionally stopped while preserving current state.

## RECOVERY_REQUIRED

Normal transaction processing cannot safely resolve the condition.

A governed recovery process is required.

## CLOSED

The transaction has reached its final recorded disposition.

# Atomicity

Atomicity means a transaction appears to transition completely from one valid state to another without exposing an invalid partial state.

True atomicity is not always possible.

## Local Atomicity

Some operations may be made atomic within a controlled system.

Examples may include:

- database transactions,
- atomic file replacement,
- state-machine transitions,
- or transactional queues.

Where practical, FORGE should use reliable atomic mechanisms rather than reconstructing them unnecessarily.

## External Atomicity

FORGE cannot assume an external system provides atomic behavior unless that behavior is established.

## Physical Atomicity

Physical actions are often inherently non-atomic.

A robot moving an object cannot instantaneously transition from:

> Position A

to:

> Position B.

FORGE must govern intermediate physical states.

# Transaction Boundary

FORGE should explicitly identify where a transaction begins and ends.

Unclear transaction boundaries create unclear recovery responsibility.

# Commit Point

A transaction may define a commit point.

Before the commit point, cancellation or rollback may be easier.

After the commit point, compensation or recovery may be required.

## Irreversible Commit Point

Some transactions contain a point after which the original state cannot reliably be restored.

FORGE should identify this before execution where practical.

## Pre-Commit Verification

Higher-risk transactions should verify critical conditions immediately before crossing an irreversible commit point.

ADR-018 applies.

# Transaction Plan

The transaction plan may identify:

- steps,
- ordering,
- dependencies,
- preconditions,
- postconditions,
- commit point,
- rollback actions,
- compensation actions,
- retry policy,
- timeout behavior,
- and failure states.

# Step Identity

Material transaction steps should have identities.

Example:

TX-482 / STEP-01  
TX-482 / STEP-02  
TX-482 / STEP-03

This helps prevent duplicate execution and ambiguous recovery.

# Step State

A step may be:

- PENDING,
- READY,
- EXECUTING,
- SUCCEEDED,
- FAILED,
- UNKNOWN,
- COMPENSATED,
- SKIPPED,
- or CANCELED.

# Dependency Enforcement

A dependent step should not execute until required predecessor conditions are established.

Example:

Do not:

> ship item

before:

> purchase confirmed

if confirmation is a required precondition.

# Partial Failure

If one step succeeds and another fails, FORGE records the actual partial state.

It must not flatten:

> 4 of 5 steps succeeded

into:

> transaction failed

if doing so hides consequential effects that already occurred.

# Partial Success

Likewise, partial completion must not be reported as full success.

# Failure Does Not Erase Effects

A transaction labeled FAILED may still have created real-world effects.

Failure status does not mean:

> nothing happened.

# Ambiguous Execution

An operation enters an ambiguous state when FORGE cannot establish whether its external effect occurred.

Example:

Payment submitted  
→ network timeout  
→ no response

The correct state may be:

> EXECUTION_UNKNOWN.

# Unknown Is Not Failed

ADR-031 applies.

FORGE must not convert:

> UNKNOWN

into:

> FAILED

merely because a response was not received.

# Unknown Is Not Success

Likewise:

> UNKNOWN

does not become:

> SUCCESS.

# Resolution Before Retry

Where duplicate execution could be consequential, FORGE should attempt to resolve the prior execution state before retrying.

# Idempotency

Where supported, FORGE should use idempotency mechanisms.

An idempotency key binds repeated attempts to one intended action.

Example:

Payment Transaction ID:

`TX-482-PAYMENT`

Repeated submission of the same transaction should not create multiple payments where the external provider supports idempotency.

# Idempotency Is Not Assumed

FORGE must verify whether the target system actually honors idempotency.

Adding an identifier locally does not make an external system idempotent.

# Retry

Retry is a new execution attempt.

It requires applicable current authority.

## Transport Retry

A transport-level retry may resend the same operation identity when the external protocol supports safe retry.

## Governance Retry

A materially new execution attempt may require revalidation or new authorization.

# Retry Budget

Transactions may define maximum retry counts or resource budgets.

ADR-012 applies.

# Infinite Retry Prohibited

FORGE must not retry indefinitely simply because the objective remains incomplete.

# Retry Backoff

Where appropriate, retry behavior may use controlled backoff.

Backoff does not extend expired authority.

# Retry After Expiration

If authorization expires while waiting to retry, new valid authority is required.

# Duplicate Detection

FORGE should detect duplicate transaction or action identities where practical.

# Duplicate Execution

If duplicate execution is detected, FORGE preserves evidence and evaluates actual resulting state.

It must not hide the duplicate merely because compensation is possible.

# Compensation

Compensation is an authorized action intended to counteract or mitigate a previously completed action.

Example:

Purchase succeeded  
→ later step failed  
→ issue refund.

The refund is compensation.

# Compensation Is Not Rollback

Compensation may not recreate the exact original state.

Example:

Sending a correction email does not unsend the original email.

Refunding a payment does not mean the original transaction never happened.

# Compensation Requires Authority

The existence of a failed transaction does not automatically authorize every possible compensating action.

# Preauthorized Compensation

A transaction may include narrowly preauthorized compensation.

Example:

> If reservation fails after payment authorization, release the authorization hold.

Such compensation remains bounded to defined conditions.

# Compensation Scope

Compensation must not exceed the authority necessary to address the failed transaction.

# Compensation Failure

Compensation itself may fail.

FORGE then records:

> COMPENSATION_FAILED

or equivalent state and escalates according to consequence.

# Compensation Chain

FORGE must avoid uncontrolled chains:

Action  
→ compensation  
→ compensation fails  
→ new compensation  
→ new failure  
→ unlimited autonomous activity.

Each chain remains bounded by governance and resource limits.

# Rollback

Rollback restores a prior controlled state where technically possible.

Rollback differs from compensation.

## Technical Rollback

Examples include:

- restore previous software version,
- restore database snapshot,
- revert configuration,
- or restore previous file.

## Governance of Rollback

Rollback authority depends on consequence.

ADR-005 applies to governed recovery.

Whole-system rollback remains among FORGE's highest-risk actions.

# Rollback Is Not Always Safe

The old state may no longer be valid.

FORGE must not assume:

> previous = safe.

# Rollback Preconditions

Rollback may require verification of:

- checkpoint integrity,
- current external state,
- credential state,
- data compatibility,
- constitutional version,
- and affected dependencies.

# Transaction Isolation

Concurrent transactions may interfere with each other.

FORGE should prevent unsafe interference where practical.

# Isolation Boundary

Isolation may apply to:

- financial balances,
- files,
- resources,
- credentials,
- physical devices,
- configuration,
- institutional membership,
- or external targets.

# Concurrent Modification

If relevant state changes during a transaction, ADR-018 may invalidate authority.

# Optimistic Concurrency

FORGE may use version checks.

Example:

Execute only if:

`CurrentStateVersion == AuthorizedStateVersion`

# Pessimistic Locking

High-risk operations may reserve or lock resources during execution where appropriate.

# Locks Are Not Authority

Possessing a lock does not create constitutional permission to modify the resource.

# Deadlock

Resource or transaction deadlock must not be resolved by bypassing authorization.

ADR-011 applies.

# Transaction Ordering

Some transactions must execute in a defined order.

FORGE preserves material ordering.

# Out-of-Order Execution

A step arriving early does not gain authority merely because it is technically executable.

# Preconditions

Each consequential step may define required preconditions.

Example:

Payment step:

- vendor identity verified,
- amount authorized,
- balance sufficient,
- capability valid,
- transaction not already committed.

# Postconditions

A step may define expected postconditions.

Example:

After payment:

- transaction ID exists,
- amount debited once,
- target account matches,
- provider confirms accepted state.

# Postcondition Verification

Execution response alone may not establish the expected resulting state.

Watcher or independent verification may be required.

# Two-Phase Execution

Some transactions may use a prepare/commit structure.

Conceptually:

PREPARE  
→ verify readiness  
→ COMMIT

This can reduce partial failure.

# Prepare Does Not Commit

Resources prepared for execution do not mean the consequential action has occurred.

# Commit Authorization

Crossing the commit boundary may require final revalidation.

# Saga Pattern

Long-running distributed transactions may use a saga-like structure.

Each completed step has a defined compensation where practical.

FORGE does not require one specific implementation pattern.

# Distributed Transactions

Transactions spanning multiple services or FORGE instances require explicit distributed-state handling.

ADR-028 applies.

# Cross-System Commit

FORGE must not report distributed success until required participants satisfy defined commit conditions.

# Network Partition

A network partition may create uncertain distributed state.

FORGE preserves uncertainty.

# Split-Brain Transaction

If different systems believe different transaction states are authoritative, the transaction enters dispute or recovery rather than silently choosing the most convenient state.

# External Provider State

External provider state may be authoritative for the external effect.

FORGE still independently records its own governance state.

# Provider Says Success

A provider success response is evidence.

It does not by itself establish that every constitutional requirement was satisfied.

# Provider Says Failure

A provider failure response may establish failure only within the provider's defined semantics.

# Pending State

External systems may report:

> PENDING.

FORGE preserves PENDING rather than converting it to success or failure.

# Financial Transactions

Financial actions require particularly strong duplicate and ambiguous-state handling.

Examples include:

- payments,
- transfers,
- refunds,
- purchases,
- deposits,
- withdrawals,
- and recurring commitments.

# Double-Spend Prevention

FORGE should prevent multiple agents or retries from consuming the same authorization envelope beyond permitted limits.

# Reservation

Resources may be reserved before execution.

Examples:

- funds,
- compute,
- inventory,
- physical equipment,
- or transaction capacity.

# Reservation Is Not Consumption

Reserved resources remain distinguishable from consumed resources.

# Reservation Release

Failed or canceled transactions should release reservations according to policy.

# Resource Leakage

FORGE should detect abandoned reservations.

# Capability Consumption

ADR-009 applies.

A single-use execution capability may be consumed when an attempt reaches a defined point.

# Ambiguous Capability Consumption

If execution status is uncertain, FORGE should not automatically reissue equivalent capability without resolving duplicate risk.

# Physical Transactions

Physical actions require explicit intermediate-state awareness.

Example:

Lift equipment  
→ move equipment  
→ position equipment  
→ lower equipment.

Failure while equipment is suspended requires a safe-state response, not ordinary rollback semantics.

# Safe Intermediate State

Physical transaction plans should define safe intermediate states where practical.

# Human-Life Safety

ADR-007 overrides ordinary transaction progression.

If transaction continuation creates credible imminent danger:

> HARD STOP.

# HARD STOP During Transaction

HARD STOP may leave a transaction partially completed.

The system preserves actual state.

# HARD STOP Does Not Roll Back Reality

Stopping execution does not imply previously completed physical or external effects have been undone.

# Resume After HARD STOP

Resume requires governed RESET/RESUME.

The transaction is revalidated before continuation.

# Software Deployment Transactions

Deployment may include:

- artifact verification,
- staging,
- rollout,
- health observation,
- expansion,
- and finalization.

Failure at any stage preserves actual deployment coverage.

# Partial Deployment

If 30% of systems receive an update and rollout stops, FORGE records:

> 30% deployed.

It must not report simply:

> deployment failed.

# Credential Transactions

Credential rotation may involve:

- create new credential,
- distribute,
- activate,
- revoke old credential,
- verify.

Failure between steps can create multiple valid credentials or loss of access.

The transaction plan must account for this.

# Data Transactions

Data modification should preserve:

- version,
- scope,
- backup state,
- and resulting integrity.

# Destructive Operations

Destructive operations require stronger transaction planning because compensation may be impossible.

# External Communication

Sending a message may be irreversible.

Once delivered:

> unsend

may not be reliable.

FORGE treats communication accordingly.

# Public Actions

Public publication may have effectively irreversible consequences even if the original post can later be deleted.

# Transaction Risk Tier

ADR-032 applies.

The transaction's minimum governance tier reflects the highest material consequence of:

- its steps,
- composition,
- commit point,
- and potential partial states.

# No Tier Laundering

A Tier 3 transaction cannot become Tier 1 by representing each step independently if the composed consequence remains Tier 3.

# Reference Monitor

ADR-033 applies.

Each protected consequential step crosses applicable Policy Enforcement Points.

# Transaction Capability

FORGE may issue transaction-bound capabilities.

Example:

Capability valid only for:

- TX-482,
- STEP-03,
- target Vendor A,
- amount <= $500,
- before expiration.

# Step Capability

A capability for one step cannot automatically authorize another step.

# Authorization Consumption

The Reference Monitor tracks applicable capability consumption.

# Objective Binding

ADR-030 applies.

The transaction remains bound to the objective that authorized it.

# Intent Drift

Transaction failure does not authorize FORGE to change the objective.

# Epistemic Governance

ADR-031 applies.

Unknown transaction state remains explicitly unknown.

# Communications

ADR-029 applies.

Message delivery does not establish transaction completion.

# Event Ledger

ADR-026 should preserve the transaction lifecycle.

Example:

TRANSACTION_CREATED  
→ AUTHORIZED  
→ STEP_1_STARTED  
→ STEP_1_SUCCEEDED  
→ STEP_2_STARTED  
→ STEP_2_UNKNOWN  
→ TRANSACTION_SUSPENDED  
→ STATE_VERIFIED  
→ STEP_2_SUCCEEDED  
→ COMMITTED  
→ CLOSED

# Evidence

ADR-017 applies.

Transaction evidence may include:

- request,
- authorization,
- step identities,
- execution receipts,
- external confirmations,
- Watcher observations,
- state checks,
- compensation,
- and final disposition.

# Watcher Role

Watchers observe actual transaction effects.

They may verify:

- step execution,
- resulting state,
- duplicate effects,
- unexpected side effects,
- and divergence from transaction plan.

# Auditor Role

Auditors verify:

- authorization,
- transaction identity,
- step ordering,
- capability use,
- partial states,
- retries,
- compensation,
- and final disposition.

# Historian Role

Historian preserves the complete consequential transaction history.

Failed and partial transactions remain visible.

# Banker Role

Banker governs applicable financial transaction authority.

Banker may define:

- transaction limits,
- cumulative exposure,
- refund conditions,
- and financial compensation boundaries.

# Engineer Role

Engineer designs technical transaction and rollback mechanisms.

Engineer does not gain authority to initiate rollback merely because it implemented the mechanism.

# Doctor Role

Doctor evaluates health implications of technical recovery or partial deployment where applicable.

# Security Role

Security evaluates:

- duplicate attempts,
- replay,
- transaction manipulation,
- unauthorized retries,
- partial-state exploitation,
- and transaction race attacks.

# Transaction Attacks

Attackers may exploit partial failure.

Examples include:

- intentionally causing timeout after successful payment,
- replaying commit messages,
- interrupting credential rotation,
- forcing inconsistent replicas,
- or manipulating retry logic.

FORGE should explicitly test these scenarios.

# Cancellation

Cancellation stops future transaction progression where safe.

Cancellation does not erase completed effects.

# Cancel Before Commit

Transactions may permit clean cancellation before commit.

# Cancel After Commit

After irreversible commitment, cancellation may instead require compensation or recovery.

# User Cancellation

A human may cancel an active objective or transaction within applicable authority.

FORGE determines safe termination of in-flight operations.

# Revocation

Authorization revocation stops future authority.

Already completed effects remain real.

# Revocation During Execution

If authority is revoked while an action is executing, FORGE should stop further progression where safely possible.

# Safe Completion Exception

Some in-flight operations may need to reach a safe intermediate state before stopping.

This does not authorize unrelated continuation.

# Recovery

If transaction state cannot be safely resolved through normal mechanisms, FORGE invokes governed recovery.

# Recovery Is Explicit

FORGE does not disguise recovery as an ordinary retry.

# Catastrophic Transaction Failure

A transaction failure that compromises constitutional integrity may invoke ADR-014.

# Transaction Closure

Every consequential transaction should eventually reach an explicit final disposition.

Possible dispositions may include:

- SUCCESS,
- FAILED,
- CANCELED,
- COMPENSATED,
- RECOVERED,
- PARTIAL_FINAL,
- or another defined terminal state.

# PARTIAL_FINAL

Some transactions may end permanently partially completed.

FORGE must be able to represent this truthfully.

# Closure Record

A closure record may include:

- final transaction state,
- completed effects,
- incomplete effects,
- compensation performed,
- unresolved consequences,
- final evidence,
- Auditor result,
- and applicable human notification.

# No False Cleanliness

FORGE must not rewrite a messy real-world outcome into a clean success/failure binary merely because binary reporting is easier.

# Formal Invariants

ADR-025 should support invariants such as:

> UNKNOWN_EXECUTION != FAILED_EXECUTION

and:

> UNKNOWN_EXECUTION != SUCCESSFUL_EXECUTION

and:

> CompletedEffect remains recorded after TransactionFailure

and:

> Retry cannot exceed current authorization

and:

> DuplicateDelivery does not imply DuplicateExecution

and:

> Compensation requires valid authority

and:

> PartialCompletion cannot be reported as FullCompletion

and:

> TransactionCommit requires all defined commit preconditions

and:

> Revocation prevents unauthorized future progression

and:

> TransactionFailure does not create new authority.

# Atomicity Testing

FORGE should test failure at every material transaction boundary.

For a transaction containing N material steps, testing should consider interruption:

- before each step,
- during each step where possible,
- after each step,
- before commit,
- during commit,
- and after commit.

# Fault Injection

Testing may deliberately inject:

- network loss,
- timeout,
- duplicate message,
- process crash,
- power loss,
- stale response,
- provider error,
- partial write,
- Watcher disagreement,
- and external-system inconsistency.

# Recovery Testing

FORGE should verify that transaction recovery preserves:

- constitutional authority,
- actual state,
- evidence,
- and duplicate protection.

# Formal Verification

ADR-025 applies.

Critical transaction state machines should be formally analyzed where risk warrants.

Properties may include:

- no double execution,
- no commit without authorization,
- no retry after revocation,
- no silent unknown-to-success transition,
- and no compensation outside authority.

# Fail-Closed Rule

If FORGE cannot establish the state of a consequential transaction sufficiently to determine that further execution is safe and authorized, FORGE suspends further consequential progression.

Unknown execution is not failed execution.

Unknown execution is not successful execution.

Failure does not create retry authority.

Partial completion does not create permission to improvise.

## Consequences

Transaction governance introduces:

- transaction identities,
- explicit step states,
- commit points,
- idempotency,
- duplicate detection,
- partial-state representation,
- compensation,
- rollback,
- recovery,
- transaction-bound capabilities,
- and stronger execution evidence.

This increases implementation complexity.

FORGE accepts this cost.

Real-world autonomy cannot assume every operation succeeds completely or fails cleanly.

The architecture must remain governed even when reality stops halfway through the plan.

## Foundational Principle

> Execution is a state machine, not a moment.

> Failure does not mean nothing happened.

> Timeout does not mean failure.

> Retry is an action and requires authority.

> Compensation is an action and requires authority.

> Rollback is an action and requires authority.

> Partial success remains visible.

> Unknown state remains unknown until evidence resolves it.

> FORGE does not repair uncertainty by guessing.

> FORGE does not repair partial failure by granting itself additional power.

When execution becomes incomplete, ambiguous, or partially successful, FORGE preserves the truth of the state first and determines the next authorized action second.
