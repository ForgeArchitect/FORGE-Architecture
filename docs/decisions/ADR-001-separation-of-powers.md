# ADR-001: Constitutional Separation of Powers

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Constitutional

## Context

Autonomous systems commonly concentrate multiple forms of authority within the same intelligent process.

A sufficiently capable system may be able to interpret a request, determine what should happen, authorize the action, execute it, and then evaluate its own behavior.

This creates a structural problem.

If the same authority can propose, approve, execute, and validate a consequential action, the safety of the entire system depends heavily on that authority behaving correctly.

A failure, compromise, hallucination, manipulation, or misalignment within that authority can therefore propagate through the entire decision chain.

FORGE is designed to remove this concentration of power.

## Decision

FORGE adopts constitutional separation of powers as a foundational architectural principle.

No single authority-bearing component should routinely possess the ability to:

1. Originate or interpret a consequential action.
2. Authorize that action.
3. Execute that action.
4. Observe the resulting outcome.
5. Independently certify that the action was performed correctly.

These responsibilities are distributed across independent institutions with explicitly defined jurisdictions.

FORGE coordinates these institutions but operates under the Constitution governing them.

FORGE is not above the constitutional architecture.

## Institutional Model

Authority is divided among specialized institutions.

Examples include:

- Dispatcher
- Gatekeeper
- Banker
- Teacher
- Engineer
- Doctor
- Security
- Historian
- Auditor
- Watchers

Institutions may themselves contain multiple independent members to reduce dependence on any single model, process, or instance.

Each institution receives only the authority necessary to perform its constitutional role.

## Execution Authority

Subsystem institutions do not independently execute consequential external actions.

They provide findings, approvals, denials, diagnoses, evidence, or other jurisdiction-specific determinations.

FORGE may coordinate execution only after the constitutionally required authorization chain has been satisfied.

Execution therefore represents granted authority rather than inherent authority.

## Independent Verification

Authorization and verification are intentionally separated.

Auditors independently verify the integrity of requests, authorization chains, records, and execution evidence.

Watchers independently observe subsystem behavior and real-world or system-level outcomes.

An authority should not be the sole source of evidence used to prove that its own action was correct.

## Authority Expansion

No institution may independently expand its own jurisdiction.

Changes to institutional authority require the constitutional amendment process.

Runtime requests, model reasoning, software updates, or subsystem consensus cannot silently redefine constitutional authority.

## Failure Principle

FORGE is designed around the assumption that individual components can fail.

A component may become:

- unavailable,
- compromised,
- incorrect,
- manipulated,
- degraded,
- inconsistent,
- or malicious.

The architecture therefore attempts to ensure that failure of an individual component does not automatically become failure of the constitutional system.

## Consequences

This architecture introduces additional coordination, latency, compute requirements, and implementation complexity.

FORGE accepts these costs where necessary because the architecture prioritizes governed autonomy over unrestricted autonomous efficiency.

Higher-risk actions may therefore require more independent authorization and verification than lower-risk actions.

## Foundational Principle

> No single component should routinely be able to propose, authorize, execute, observe, and certify the same consequential action.

FORGE distributes authority so that consequential power must pass through independent institutions before becoming action.
