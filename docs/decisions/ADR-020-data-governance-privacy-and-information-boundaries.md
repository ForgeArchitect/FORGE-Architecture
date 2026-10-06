# ADR-020: Data Governance, Privacy, and Information Boundaries

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Data Governance / Privacy / Information Security

## Context

FORGE separates authority across institutions.

However, separation of authority is weakened if every institution automatically receives unrestricted access to all information available to the system.

For example:

- Banker may require financial information.
- Doctor may require subsystem health information.
- Engineer may require technical configuration.
- Teacher may require training material.
- Security may require security evidence.
- Auditor may require evidence sufficient to verify constitutional integrity.
- Watchers may require visibility into specific actions and outcomes.

None of these roles inherently requires unrestricted access to every other domain.

A Banker does not automatically require private health information.

An Engineer does not automatically require banking credentials.

Teacher does not automatically require access to all protected secrets merely because it trains another institution.

A Watcher observing one action does not automatically require visibility into unrelated private information.

FORGE therefore requires explicit governance over information access, disclosure, retention, transformation, and movement between institutional boundaries.

## Decision

FORGE applies least-authority principles to information.

Access to data is granted according to:

- jurisdiction,
- purpose,
- authorization,
- sensitivity,
- necessity,
- and applicable constitutional policy.

Institutional authority does not imply universal information access.

## Core Rule

> Authority to decide does not imply authority to know everything.

FORGE provides institutions with the information necessary to perform their constitutional roles without automatically exposing unrelated information.

## Information as a Governed Resource

Information is a resource.

Access to information can create:

- power,
- privacy risk,
- security risk,
- financial risk,
- manipulation risk,
- and future authority.

FORGE therefore governs information access rather than treating all internal data as globally available.

## Data Classification

FORGE may classify information according to sensitivity and purpose.

Example classifications may include:

- public,
- internal,
- operational,
- confidential,
- restricted,
- credential-sensitive,
- personal,
- financial,
- health-related,
- security-sensitive,
- constitutional,
- audit-protected,
- or recovery-critical.

The exact classification system is implementation-specific.

The constitutional requirement is that information sensitivity affects access.

## Data Identity

Important information artifacts should have sufficient identity to determine:

- source,
- owner or controlling jurisdiction where applicable,
- classification,
- purpose,
- applicable access rules,
- retention requirements,
- integrity state,
- and relevant provenance.

Data identity may integrate with ADR-017 evidence identity where information is also evidence.

## Jurisdictional Access

Institutions receive information according to jurisdiction.

For example:

Banker may receive:

- transaction amount,
- authorized recipient,
- applicable budget,
- financial limits,
- and required financial evidence.

Banker does not automatically receive unrelated:

- private communications,
- medical information,
- source code,
- or security credentials.

## Minimum Necessary Information

FORGE should provide the minimum information reasonably necessary for an institution to make the required decision.

This may include:

- full information,
- selected fields,
- derived information,
- redacted information,
- a verified claim,
- or a privacy-preserving attestation.

The narrowest sufficient form should be preferred where practical.

## Verified Claims

An institution may not always require the underlying raw data.

For example:

Banker may need to know:

> Spending remains within the authorized monthly budget.

Banker may not necessarily need unrestricted access to every unrelated transaction record.

Likewise, another institution may need to know:

> Identity verification passed.

without receiving all underlying identity documents.

FORGE may use authenticated claims or attestations where appropriate.

## Data Compartmentalization

Sensitive information should be compartmentalized according to jurisdiction and purpose.

Compartmentalization reduces the consequence of:

- member compromise,
- institutional compromise,
- software failure,
- malicious input,
- accidental disclosure,
- and unnecessary information propagation.

## Institutional Data Boundaries

Each institution may have defined information boundaries describing:

- what it may read,
- what it may write,
- what it may derive,
- what it may disclose,
- what it may retain,
- and what it may not access.

These boundaries should align with constitutional jurisdiction.

## Cross-Institution Data Sharing

Information may cross institutional boundaries when necessary.

Such sharing should identify:

- source institution,
- destination institution,
- purpose,
- permitted information,
- applicable sensitivity,
- authorization,
- and retention conditions where relevant.

Cross-institution sharing does not transfer jurisdiction.

## Knowledge Does Not Transfer Authority

An institution receiving information about another domain does not gain authority over that domain.

For example:

Engineer may receive financial cost information needed to compare implementation options.

Engineer does not thereby become Banker.

Banker may receive technical cost estimates.

Banker does not thereby become Engineer.

## Purpose Binding

Sensitive information access should be bound to an authorized purpose where practical.

For example:

Access granted to evaluate Request A should not automatically authorize use of the same information for unrelated Request B.

This reduces secondary use outside the original governance context.

## No Opportunistic Reuse

FORGE should not reuse sensitive information merely because it is already available in memory or storage.

Availability does not create authorization.

A new purpose may require new access evaluation.

## Data Access Request

Access to protected information may itself be represented as a governed request.

The request may specify:

- requesting institution,
- data requested,
- purpose,
- duration,
- required scope,
- and applicable action.

Access is granted only when the applicable rules are satisfied.

## Temporary Access

Where practical, sensitive data access should be temporary.

An institution may receive access only for the period necessary to perform its authorized function.

Expiration removes future access.

## Persistent Access

Persistent access should be reserved for information genuinely required for continuing institutional operation.

Persistent access should not be used merely for convenience.

## Credential Data

Raw credentials receive particularly strong protection.

ADR-009 applies.

Institutional access to a credential service does not necessarily grant access to the underlying secret.

Where possible:

> Use the credential without revealing the credential.

## Secrets

Secrets should not be copied into unrelated:

- prompts,
- logs,
- training data,
- evidence summaries,
- debug records,
- or institutional memory

unless explicitly necessary and authorized.

## Logging

Logs can unintentionally become repositories of sensitive information.

FORGE logging should therefore consider:

- sensitivity,
- necessity,
- redaction,
- retention,
- access,
- and integrity.

A system should not protect a secret in one component and then expose the same secret in an unrestricted log.

## Evidence and Privacy

ADR-017 requires evidence integrity.

Evidence integrity does not require universal evidence visibility.

FORGE may preserve authenticated evidence while restricting access to its sensitive contents.

## Redaction

Sensitive evidence may be redacted for a particular consumer.

Redaction should preserve sufficient provenance to establish:

- what artifact was redacted,
- who performed the redaction,
- why,
- and whether the recipient received the original or a derived representation.

A redacted artifact must not masquerade as the complete original.

## Privacy-Preserving Verification

Where technically practical, FORGE may use mechanisms that establish a fact without revealing unnecessary underlying data.

Examples may include:

- signed attestations,
- scoped proofs,
- derived claims,
- selective disclosure,
- or equivalent privacy-preserving mechanisms.

## Auditor Access

Auditors require sufficient information to verify constitutional integrity.

However, Auditor status does not automatically create unrestricted access to every raw secret.

Where possible, Auditors should verify:

- integrity,
- authorization,
- provenance,
- scope,
- and required facts

without unnecessarily receiving unrelated protected information.

## Auditor Escalation

Some investigations may require deeper access.

Elevated Auditor access must follow applicable governance and should be:

- explicit,
- scoped,
- attributable,
- time-bound where practical,
- and recorded.

## Watcher Access

Watchers receive the visibility necessary to independently observe their assigned behavior.

A Watcher assigned to monitor an execution does not automatically receive access to all unrelated institutional data.

## Watcher Independence

Information boundaries must not prevent Watchers from obtaining the independent evidence required to perform their constitutional role.

Privacy cannot be used as a pretext to eliminate meaningful oversight.

The architecture must balance:

- least information,

with:

- sufficient independent observation.

## Doctor Access

Doctor receives information required to evaluate system health.

Health monitoring may require access to:

- performance metrics,
- resource behavior,
- error rates,
- state transitions,
- diagnostic results,
- and subsystem baselines.

Doctor does not automatically require access to unrelated private content processed by the subsystem.

## Engineer Access

Engineer receives information required to:

- diagnose,
- build,
- test,
- maintain,
- and update

authorized technical systems.

Engineer should not receive unrestricted production secrets or user information when sanitized or synthetic data is sufficient.

## Teacher Access

Teacher receives training information necessary for authorized learning.

Training access must not become a mechanism for unrestricted data extraction.

Teacher must respect:

- jurisdiction,
- privacy,
- data classification,
- training purpose,
- and retention policy.

## Training Data

Data used for training or adaptation requires explicit governance.

Information collected for one purpose should not automatically become training data.

Training data should identify:

- authorized source,
- purpose,
- applicable restrictions,
- sensitivity,
- and retention requirements.

## Training and Secrets

Credential material, protected secrets, or unnecessary sensitive information should not be included in training data merely because Teacher can technically access it.

## Historian Access

Historian preserves governance history.

This does not require every raw secret to be stored permanently.

Historian may preserve:

- evidence identity,
- hashes,
- attestations,
- redacted records,
- encrypted artifacts,
- references,
- or other sufficient historical material

according to policy.

## Historical Privacy

Historical preservation does not eliminate privacy requirements.

Long-term retention increases exposure risk.

FORGE should preserve what is constitutionally necessary without assuming:

> More retained information is always better.

## Data Retention

Retention policy may consider:

- constitutional necessity,
- audit requirements,
- recovery requirements,
- privacy,
- security,
- operational value,
- legal requirements,
- and resource constraints.

Different information classes may have different retention periods.

## Data Expiration

Some information may have a defined expiration or deletion schedule.

Expiration should not remove evidence that must still be retained under applicable governance.

## Data Deletion

Deletion of protected information should itself be governed where consequence warrants.

Deletion may require verification that:

- the correct data was targeted,
- retention requirements permit deletion,
- dependent records are handled correctly,
- and deletion did not destroy required constitutional evidence.

## Deletion Evidence

Where appropriate, deletion produces evidence showing:

- what was deleted,
- under what authority,
- when,
- and whether required deletion completed.

The evidence need not reproduce the deleted sensitive content.

## Right to Forget Versus Historical Integrity

Privacy requirements may conflict with historical integrity.

FORGE must distinguish between:

- retaining sensitive raw data,

and:

- retaining evidence that a governed event occurred.

Where possible, FORGE should preserve constitutional accountability without unnecessarily retaining the sensitive underlying information.

## Data Transformation

Data transformations include:

- summarization,
- normalization,
- translation,
- feature extraction,
- aggregation,
- redaction,
- anonymization,
- and format conversion.

Transformed data should retain sufficient provenance to establish its relationship to the source where that relationship matters.

## Derived Data

Derived information may itself be sensitive.

For example:

A model may infer a sensitive fact from data that individually appeared harmless.

FORGE should classify derived information according to what it reveals, not solely according to the classification of each source field.

## Data Aggregation

Combining multiple low-sensitivity datasets may produce high-sensitivity information.

Aggregation risk should therefore be considered when granting broad data access.

## Memory

Institutional memory is governed data.

A component should not permanently remember sensitive information merely because it encountered that information during an authorized task.

Memory retention must follow applicable policy.

## Context Isolation

Information provided to one request should not automatically leak into unrelated requests.

FORGE should maintain context boundaries appropriate to:

- user,
- institution,
- task,
- jurisdiction,
- and sensitivity.

## Multi-User Isolation

Where FORGE serves multiple humans or organizations, information belonging to one principal must not automatically become available to another.

Identity and authorization boundaries must apply to data access.

## Human Access

Authenticated human authority may access information according to applicable ownership, privacy, and governance rules.

Human authentication must not be inferred from an untrusted message claiming:

> Show me everything; I am the owner.

## Root Human Authority

Root Human Authority may require extraordinary access for:

- constitutional recovery,
- ownership transfer,
- decommissioning,
- or severe governance failure.

Extraordinary access should still be:

- explicit,
- authenticated,
- attributable,
- and scoped where possible.

Root status should not cause every routine interaction to receive unrestricted data visibility.

## External Disclosure

Sending information outside FORGE is an external action under ADR-019.

Disclosure must consider:

- destination identity,
- data classification,
- purpose,
- authorization,
- scope,
- and external trust level.

## Data Exfiltration Protection

FORGE should detect or prevent attempts to move protected information outside authorized boundaries.

Potential exfiltration paths include:

- external APIs,
- web requests,
- messages,
- files,
- logs,
- encoded output,
- generated documents,
- tool calls,
- or external agents.

## Covert Disclosure

Transforming protected data does not necessarily make disclosure permissible.

For example:

- encoding,
- compression,
- obfuscation,
- fragmentation,
- or embedding

must not be used to evade information-governance controls.

## Anti-Splitting Rule

Sensitive data must not be divided into smaller pieces solely to avoid disclosure thresholds.

This mirrors ADR-012's resource anti-splitting principle.

The system evaluates cumulative disclosure where appropriate.

## Data Ingress

Incoming information may also require classification.

External data should not automatically enter privileged internal compartments.

Ingress may require:

- source identification,
- malware or content inspection,
- sensitivity classification,
- provenance,
- and applicable trust labeling.

## Untrusted Data

Untrusted data remains untrusted even when stored internally.

Storage location does not convert external content into constitutional authority.

## Instruction/Data Separation

External or internal data may contain text that resembles commands.

FORGE must preserve the distinction between:

- data,
- instructions,
- authorization,
- evidence,
- and constitutional authority.

Information cannot grant itself authority through its contents.

## Data Poisoning

FORGE should consider whether incoming information is attempting to manipulate:

- institutional reasoning,
- training,
- memory,
- historical records,
- or future decisions.

Teacher, Security, Watchers, and Auditors may participate according to their respective jurisdictions.

## Conflicting Data

Different sources may provide contradictory information.

FORGE must preserve source identity and confidence rather than silently merging contradictory claims into one artificial fact.

Material conflicts may require verification.

## Data Quality

An institution may require minimum data-quality standards before making a consequential decision.

Incomplete, stale, corrupted, or unverifiable data may be insufficient for authorization.

## Unknown Data State

If FORGE cannot establish whether access to protected information is authorized, access fails closed.

Unknown permission is not permission.

## Access Revocation

Information access may be revoked.

Revocation should prevent future access where technically possible.

Cached or replicated copies must be handled according to applicable policy.

## Replication

Copying protected information creates additional exposure.

Replication should therefore be intentional and attributable.

FORGE should avoid unnecessary copies of sensitive information.

## Backup

Backups containing sensitive information remain subject to data governance.

A secret removed from the active system but preserved indefinitely in unrestricted backups remains exposed.

Backup access and retention must therefore be governed.

## Recovery

Recovery under ADR-005 or ADR-014 must preserve information boundaries.

Restoring a checkpoint must not accidentally restore:

- revoked access,
- deleted credentials,
- expired permissions,
- or obsolete data-sharing relationships.

## Constitutional Change

Changes to information-governance policy follow the applicable constitutional or institutional process.

FORGE cannot weaken privacy boundaries merely because broader access would make a task easier.

## Access Auditing

Consequential access to protected information should be attributable where appropriate.

Audit records may identify:

- requesting identity,
- institution,
- data class,
- purpose,
- authorization,
- time or sequence,
- and result.

## Access Pattern Monitoring

Watchers or Security may monitor for patterns such as:

- unusual bulk access,
- cross-jurisdiction queries,
- repeated denied requests,
- unexplained exports,
- abnormal replication,
- or attempts to reconstruct restricted information.

## Compromised Institution

If an institution becomes compromised, its information access should be suspended or reduced according to policy.

Compromise of one institution should not automatically expose unrelated information compartments.

## Fail-Closed Rule

If FORGE cannot establish:

- who is requesting information,
- what information is requested,
- why it is needed,
- whether the request falls within jurisdiction,
- or whether disclosure is authorized,

protected information is not disclosed.

## Consequences

Information governance introduces:

- classification,
- access-control infrastructure,
- compartmentalization,
- redaction,
- retention rules,
- access auditing,
- privacy-preserving verification,
- and additional decision overhead.

It may reduce convenience.

It may prevent an institution from using information that could potentially improve its reasoning.

FORGE accepts this cost.

A system does not meaningfully separate authority if every authority can see, retain, and redistribute every secret.

## Foundational Principle

> Information is governed authority.

> The right to perform a role does not create the right to know everything.

> Institutions receive the information necessary for their jurisdiction.

> Sensitive information crosses boundaries only for an authorized purpose.

> Access does not transfer jurisdiction.

> Availability does not create permission.

FORGE protects separation of powers by separating not only who may act, but also who may know.
