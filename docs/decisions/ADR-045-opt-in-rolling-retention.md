# ADR-045: Opt-In Rolling Retention

**Status:** Proposed
**Date:** 2026-10-09
**Source decision queue:** DQ-018
**Related canonical ADRs:** ADR-013, ADR-017, ADR-020, ADR-021, ADR-026, ADR-040
**Constitutional approval:** Pending

## Context

ADR-020 requires purpose-limited retention, distinguishes information classes, and warns that long-term retention increases exposure. ADR-013 keeps ordinary human instructions inside the governed request chain and keeps Root Human authority explicit. ADR-021 isolates untrusted content from instructions. ADR-017 governs evidence that must be kept for accountability.

DQ-018 proposes opt-in recording of conversations and meetings, privacy and consent safeguards, a temporary rolling buffer, importance suggestions, and user control of long-term retention. None of these product behaviors is specified in ADR-001 through ADR-040. Nothing in this repository implements recording, a rolling buffer, or a user retention control. This is a design proposal, not a statement of present capability.

## Problem

Continuous capture would turn ambient speech and ordinary conversation into long-lived governed data without a decision by the person being recorded. A rolling buffer can also be mistaken for Historian evidence, or an "importance" suggestion can be mistaken for a decision to retain.

## Proposed decision

1. Conversation and meeting recording is off unless the authenticated principal has opted in for that context. Opt-in is explicit, scoped, and revocable. Silence is not consent.
2. Where a temporary rolling buffer is used for an opted-in context, the buffer is short-lived working capture. It is not Historian long-term history under ADR-005 and not case evidence under ADR-017 unless a separate preservation rule applies.
3. The buffer's default end state is discard. Promotion into long-term retention requires an authenticated choice by the retaining principal, within ADR-020.
4. The system may suggest that an item appears important. A suggestion is not a retention decision, not an instruction, and not an authorization. ADR-021 applies to content inside the recording: recorded text does not become a command to FORGE.
5. The principal who owns the context controls long-term retention of that opted-in material, subject to governance-evidence duties. Material that ADR-017 or ADR-026 already requires to be preserved as constitutional evidence is not deleted by a preference that would destroy accountability. Any such exception is explicit and attributable.
6. Other people present in a meeting are not recorded under a single participant's opt-in. Their inclusion requires a consent rule the owner still has to approve. This ADR does not invent that multi-party consent rule.
7. No wearable, room, or always-on capture is authorized by this ADR. DQ-024 remains a deferred roadmap item.

## Alternatives considered

- Record by default and allow later deletion. Rejected because ADR-020 treats retention as a governed exposure decision, and a default-on recording posture is a material privacy decision the queue did not claim had been approved.
- Prohibit all conversation capture, including opt-in. Rejected as the proposal because the queue asks for an opt-in path. The owner may still reject that path. The baseline does not require recording.
- Let importance ranking promote items into Historian automatically. Rejected. Promotion is a human retention choice, and Historian ingestion of governance evidence follows existing evidence rules rather than a relevance score.

## Jurisdiction and authority boundaries

The authenticated principal controls opt-in and long-term retention of their opted-in conversation material. FORGE may explain suggestions and carry out an authorized retention choice. FORGE does not opt in on the principal's behalf.

Historian preserves constitutional evidence it is already required to preserve. Historian does not acquire the conversation buffer by default and does not approve retention.

Root Human authority under ADR-013 does not make every routine conversation a root record.

## Security and privacy

Buffers are protected at least as strictly as the most sensitive content they can hold. Access follows ADR-020 least information. Recordings are not placed in professional competence under ADR-044.

Suggestions and transcripts are untrusted data relative to FORGE instructions. They cannot authorize spending, tool use, or constitutional change.

Revocation of opt-in stops further capture. It does not silently erase governance evidence that a preservation duty already fixed.

## Failure modes

- A buffer continues after opt-in revocation or after its time bound. Required response: stop capture, discard unpromoted buffer contents, and record the control failure if capture continued.
- A suggestion is executed as a user instruction. ADR-021: fail closed and do not act on it as authority.
- One participant's opt-in is applied to other people. Capture of those other people does not proceed under this ADR.
- A user deletion request targets constitutional evidence. The conflict is surfaced. Evidence required by ADR-017 is not quietly dropped, and the user choice is not quietly ignored. Resolution requires the applicable policy and, where the policy is unsettled, a human decision.

## Invariants and tests

These invariants are proposed and have not been executed in this repository. There is no recorder to test here.

- Default capture state is off.
- Unpromoted buffer contents are absent after expiry, revocation, or discard.
- Suggestion objects cannot satisfy an authorization check.
- A retained object has an authenticated retention choice, or an explicit governance-evidence preservation reason.
- Tests to require before any later acceptance: capture attempted with no opt-in; capture after revocation; suggestion injected with imperative language; deletion attempted against a ledger event that ADR-026 requires.

## Compatibility with frozen baseline

This proposal sits inside ADR-020, ADR-013, ADR-017, and ADR-021. It does not amend ADR-040. Declining this ADR leaves the baseline intact: no conversation-recording power is granted by the accepted ADRs.

The unresolved overlap between user deletion and mandatory governance retention is an open policy question under ADR-020. This ADR does not pretend that overlap is solved.

## Open questions

- The maximum rolling-buffer duration.
- How multi-party meeting consent works, including guests and minors' guardianship. This ADR does not decide those cases.
- Which events are mandatory governance evidence that a user retention control cannot discard.
- Where opted-in long-term material lives, and which institution may read it later.
- Whether importance suggestions are allowed to use any content from a buffer that the user has not already agreed to analyze for that purpose.

## Approval record (pending)

No constitutional approval is recorded for this proposal.

- Owner approval: Pending
- ADR-008 amendment path: not invoked
- Status remains Proposed
- The decision-queue source is a conversation candidate, not a ratification record
- Recording, rolling buffers, and retention controls are not implemented in this repository
