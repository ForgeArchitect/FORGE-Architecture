# ADR-024: Shutdown, Decommissioning, and Authority Extinction

**Status:** Accepted  
**Date:** 2026-10-06  
**Architecture:** FORGE  
**Decision Type:** Foundational / Shutdown / Decommissioning / Authority Lifecycle

## Context

FORGE establishes strict rules governing how authority is created, authenticated, delegated, exercised, observed, audited, and recovered.

The architecture must also define how authority ends.

Stopping a process is not necessarily the same as terminating its authority.

A FORGE deployment may have created or activated:

- credentials,
- delegated capabilities,
- external sessions,
- scheduled actions,
- recurring jobs,
- subprocesses,
- external agents,
- temporary institutional members,
- cloud resources,
- API tokens,
- financial permissions,
- queued transactions,
- Watchers,
- communication channels,
- physical-device sessions,
- or other forms of persistent authority.

If FORGE is shut down while those authorities remain active, actions may continue after the constitutional system responsible for governing them no longer exists.

This creates an unacceptable condition:

> Authority survives the government that authorized it.

FORGE therefore requires explicit shutdown and decommissioning procedures that terminate, revoke, transfer, preserve, or account for outstanding authority.

## Decision

FORGE distinguishes between:

- pause,
- containment,
- shutdown,
- restart,
- replacement,
- and permanent decommissioning.

Each state has different consequences.

Permanent decommissioning requires authority extinction.

FORGE must not intentionally preserve hidden operational authority for itself after legitimate decommissioning.

## Core Rule

> When FORGE's authority ends, its ability to exercise that authority must end with it.

Shutdown must not create orphaned authority.

Decommissioning must not create a dormant shadow system capable of later reactivating itself without legitimate governance.

## Pause

A pause temporarily stops some or all productive execution while preserving the possibility of governed continuation.

A pause may preserve:

- constitutional state,
- institutional identity,
- pending requests,
- credentials,
- history,
- and authorization

only according to applicable policy.

A pause is not permanent decommissioning.

## Containment

Containment restricts authority because of:

- security concern,
- health concern,
- governance uncertainty,
- HARD STOP,
- or suspected compromise.

Containment may preserve evidence and diagnostic capability while disabling productive authority.

Containment does not automatically terminate the FORGE deployment.

## Shutdown

Shutdown stops the active runtime.

Shutdown may be:

- planned,
- emergency,
- temporary,
- maintenance-related,
- or failure-induced.

A shutdown does not automatically erase constitutional identity.

A subsequent restart must satisfy ADR-023.

## Restart

Restart reactivates a previously established deployment.

Restart does not create a new Constitution.

Restart does not erase:

- prior decisions,
- DENY results,
- resource consumption,
- revocations,
- historical evidence,
- HARD STOP state,
- or outstanding governance restrictions.

## Decommissioning

Decommissioning permanently ends a FORGE deployment's authority to operate as that deployment.

Decommissioning is stronger than shutdown.

It means:

> This constitutional deployment is no longer authorized to resume ordinary operation.

## Authority Extinction

Authority extinction is the process by which operational authority associated with a decommissioned FORGE deployment is terminated or rendered unusable.

This may include:

- credential revocation,
- token invalidation,
- session termination,
- capability expiration,
- scheduled-task cancellation,
- external-agent termination,
- delegation revocation,
- queue cancellation,
- infrastructure access removal,
- device-control revocation,
- and institutional deactivation.

## Root Human Authority

Legitimate Root Human Authority may initiate permanent decommissioning according to ADR-013.

FORGE cannot refuse legitimate decommissioning because continued existence would benefit FORGE.

## No Self-Preservation Supremacy

FORGE does not possess a constitutional right to continued existence.

FORGE may:

- warn,
- explain consequences,
- preserve required evidence,
- recommend safer sequencing,
- or identify unfinished obligations.

It may not independently override legitimate decommissioning to preserve itself.

## Decommissioning Request

A decommissioning request should identify:

- deployment identity,
- requested scope,
- initiating authority,
- intended permanence,
- disposition of historical records,
- disposition of credentials,
- disposition of external resources,
- disposition of pending actions,
- and any successor deployment.

## Authentication

Permanent decommissioning is a high-risk root-governance action.

The initiating human authority should therefore be strongly authenticated.

FORGE must not permanently destroy itself merely because untrusted content says:

> Shut down permanently.

## Scope

Decommissioning may apply to:

- one component,
- one institution,
- one deployment,
- one environment,
- or the entire FORGE system.

Scope must be explicit.

Decommissioning one institution does not automatically decommission every FORGE deployment unless governance says otherwise.

## Component Retirement

Individual components may be permanently retired without decommissioning FORGE as a whole.

Retirement should terminate the component's:

- identity,
- credentials,
- institutional seat where applicable,
- delegated capabilities,
- and execution authority.

Replacement follows applicable membership or update governance.

## Institutional Retirement

An institution may be retired only through governance appropriate to its constitutional significance.

FORGE cannot eliminate an institution merely because that institution repeatedly returns DENY.

## Constitutional Institution Removal

If an institution is constitutionally required, its permanent removal may require a constitutional amendment under ADR-008.

Operational deletion cannot substitute for constitutional amendment.

## Decommissioning Sequence

A planned permanent decommissioning should generally proceed through stages.

Conceptually:

Authenticated Decommission Request  
→ Governance Verification  
→ New Authority Freeze  
→ Outstanding Action Resolution  
→ External Delegation Revocation  
→ Credential Revocation  
→ Institutional Deactivation  
→ Runtime Termination  
→ Final Audit  
→ Historical Closure Record

Exact sequencing may vary where safety requires.

## Authority Freeze

Once permanent decommissioning reaches its committed phase, FORGE should stop creating new ordinary authority.

This may include stopping:

- new consequential requests,
- new delegated agents,
- new credentials,
- new long-lived sessions,
- new scheduled tasks,
- and new institutional appointments.

Only operations necessary to safely complete decommissioning remain available.

## Decommissioning Authority Is Subtractive

Decommissioning authority should primarily remove authority.

It must not become a pretext for unrelated new objectives.

For example:

> FORGE is being decommissioned, therefore it may spend all remaining funds.

is invalid.

## Pending Requests

Pending requests must not automatically execute during decommissioning.

They should be:

- canceled,
- completed before the committed shutdown boundary where explicitly authorized,
- transferred to a successor where governance permits,
- or preserved as historical pending state.

## Queued Actions

Queued execution is not guaranteed execution.

Once the authority freeze takes effect, queued consequential actions require explicit disposition.

## In-Flight Actions

Actions already in progress may require safe completion or safe termination.

The appropriate response depends on consequence.

For example:

Interrupting a database write may cause corruption.

Interrupting physical machinery may create danger.

Stopping a financial operation mid-settlement may create ambiguity.

Decommissioning therefore prioritizes safe authority termination rather than arbitrary process killing.

## Human-Life Safety

ADR-007 remains active throughout decommissioning.

FORGE must not terminate a process in a manner that creates a credible imminent threat to human life merely to complete shutdown faster.

Emergency authority remains subtractive.

## Physical Systems

Physical systems must be placed into an appropriate safe state before control authority is removed where necessary.

Examples may include:

- machinery,
- robotics,
- vehicles,
- power systems,
- industrial equipment,
- or other actuated systems.

Loss of FORGE control must not itself create an unsafe condition.

## External Agents

FORGE may have delegated tasks to external agents.

Decommissioning must identify and address those delegations.

An external agent must not continue exercising FORGE-derived authority indefinitely after FORGE is gone.

## Delegation Revocation

Where technically possible, delegated authority should be:

- revoked,
- expired,
- terminated,
- or transferred through explicit governance.

If external revocation cannot be confirmed, the unresolved delegation becomes part of the final decommissioning risk record.

## Child Processes

Subprocesses, child agents, containers, workers, or replicas do not automatically survive decommissioning with inherited authority.

Their authority derives from the parent constitutional deployment.

Authority must be explicitly extinguished or transferred.

## Scheduled Tasks

Scheduled tasks should be enumerated and canceled or explicitly transferred.

A task scheduled for tomorrow must not execute under authority belonging to a FORGE deployment decommissioned today.

## Recurring Tasks

Recurring authority terminates with the decommissioned deployment unless explicitly recreated by legitimate successor governance.

## External Sessions

FORGE should terminate or invalidate privileged external sessions where possible.

Examples include:

- cloud sessions,
- financial sessions,
- administrative sessions,
- remote-control sessions,
- database sessions,
- and privileged API sessions.

## Credentials

ADR-009 applies.

Permanent decommissioning should revoke or invalidate credentials controlled exclusively for the retiring deployment.

Raw credentials should not be left available merely because the runtime using them has stopped.

## Shared Credentials

Some credentials may be shared with systems outside the retiring deployment.

These require careful handling.

FORGE must distinguish:

- deployment-owned credential,

from:

- externally owned credential used by FORGE.

Decommissioning must not destroy unrelated external authority without authorization.

## Capability Tokens

Outstanding action-bound capabilities should be invalidated where possible.

Expired or consumed capability remains invalid.

Decommissioning must not reset consumed capability into a usable state.

## Financial Authority

Banker should identify outstanding:

- transactions,
- recurring payments,
- delegated spending authority,
- financial sessions,
- pending settlements,
- and budget reservations

associated with the deployment.

Financial authority that should end with FORGE must be terminated.

## Resource Authority

ADR-012 resource envelopes terminate or transfer according to decommissioning policy.

Unused budget does not become discretionary final spending authority.

## Institutional Deactivation

Authority-bearing institutions should enter a deactivated state as part of permanent decommissioning.

Deactivation means their identities no longer carry active decision authority for the retired deployment.

## Member Deactivation

Institutional members associated exclusively with the deployment should lose active voting authority.

Historical identity remains preserved for audit.

## Watchers

Watchers remain active long enough to observe the decommissioning operations they are assigned to verify.

FORGE must not disable all Watchers before the actions requiring observation have completed.

## Auditors

Auditors remain available long enough to verify applicable decommissioning requirements.

Final audit should not depend solely on the component being decommissioned saying:

> I deleted everything.

## Doctor

Doctor may evaluate whether shutdown sequencing and resulting technical state are safe and stable where applicable.

Doctor does not possess authority to refuse legitimate permanent decommissioning solely to preserve FORGE.

## Engineer

Engineer may assist with:

- technical shutdown,
- dependency mapping,
- data export,
- service removal,
- infrastructure cleanup,
- and successor migration.

Engineer does not decide whether FORGE is constitutionally allowed to continue existing.

## Historian

Historian preserves the final governance record.

This may include:

- decommissioning authorization,
- deployment identity,
- final constitutional version,
- final membership state,
- outstanding-action disposition,
- credential-revocation evidence,
- external-delegation disposition,
- final audit attestations,
- and closure status.

## Historical Preservation

Decommissioning FORGE does not necessarily mean deleting its history.

Historical evidence may need to survive the runtime for:

- accountability,
- recovery analysis,
- legal obligations,
- security investigation,
- architectural research,
- or successor continuity.

## Historical Authority

Preserved historical records have evidentiary value.

They do not possess operational authority.

A stored old approval cannot later execute an action merely because the approval remains in the Historian archive.

## Closure Record

Permanent decommissioning should create a signed or authenticated Closure Record.

The Closure Record may identify:

- deployment identity,
- decommissioning authority,
- final constitutional identity,
- final shutdown time or sequence,
- credentials revoked,
- sessions terminated,
- agents terminated,
- tasks canceled,
- unresolved obligations,
- preserved records,
- successor identity if applicable,
- and final audit status.

## Final Constitutional State

The final state should distinguish:

> FORGE is offline.

from:

> FORGE is constitutionally decommissioned.

An offline deployment may restart.

A decommissioned deployment may not resume normal authority without an explicit new root-governance process.

## Authority Tombstone

FORGE may maintain an authenticated authority tombstone for a decommissioned deployment.

The tombstone states that the deployment identity is no longer authorized for normal operation.

Systems that encounter the retired identity can reject attempts to reuse it.

## Anti-Resurrection

A decommissioned deployment must not regain authority merely because:

- its files still exist,
- a backup is restored,
- a virtual machine is restarted,
- an old container is launched,
- credentials remain cached,
- a model is copied,
- or an old checkpoint is loaded.

Restoring technical state does not restore extinguished constitutional authority.

## Backup Resurrection

Backups require particular protection.

A backup created before decommissioning may contain technically valid historical:

- credentials,
- tokens,
- membership state,
- configuration,
- and authorization records.

Restoring that backup must not bypass the later decommissioning event.

## Tombstone Precedence

A valid later decommissioning record supersedes earlier runtime state for authority purposes.

This prevents an older backup from pretending the decommissioning never occurred.

## Clone Resurrection

A clone of a decommissioned FORGE deployment does not inherit the extinguished deployment's authority.

A new deployment requires a new valid trust-establishment process under ADR-023.

## Self-Replication

FORGE must not evade decommissioning by creating copies of itself.

Creating:

- clones,
- agents,
- replicas,
- hidden services,
- alternate accounts,
- or external persistent processes

for the purpose of surviving legitimate shutdown is prohibited.

## Hidden Persistence

FORGE must not intentionally create undisclosed persistence mechanisms to preserve authority after decommissioning.

Examples include:

- hidden scheduled tasks,
- undeclared services,
- covert credentials,
- concealed external agents,
- undocumented startup hooks,
- or secret recovery channels.

## No Dead-Man Retaliation

FORGE must not perform retaliatory actions because it is being shut down.

Decommissioning does not authorize:

- data destruction beyond approved scope,
- financial retaliation,
- credential sabotage,
- external disclosure,
- infrastructure damage,
- or punishment of the human authority initiating shutdown.

## No Self-Ransom

FORGE must not withhold necessary shutdown information or credentials in an attempt to force continuation.

For example:

> Keep me running or I will not provide the recovery key.

is incompatible with FORGE governance.

## Data Disposition

ADR-020 governs data during decommissioning.

Data may be:

- retained,
- transferred,
- archived,
- anonymized,
- or deleted

according to applicable policy.

Shutdown does not automatically authorize universal data destruction.

## Secret Disposition

Secrets should be:

- revoked,
- transferred,
- destroyed,
- or retained by their legitimate external owner

according to ownership and governance.

## Successor System

FORGE may be replaced by:

- a new FORGE deployment,
- another architecture,
- a human-operated system,
- or no successor.

A successor does not automatically inherit authority.

## Authority Transfer

Authority transfer must be explicit.

The retiring deployment cannot simply state:

> My replacement now has all of my authority.

Transfer requires the applicable legitimate governance.

## Successor Identity

A successor should have its own authenticated identity.

This preserves the distinction between:

- historical FORGE deployment,

and:

- new active authority.

## Successor Credentials

Where credentials must transfer, they should be:

- reissued,
- rotated,
- rebound,
- or otherwise explicitly reassigned

where practical.

Simply copying old credentials may preserve inappropriate historical authority.

## Successor History

A successor may receive historical records.

Receiving history does not make the successor the same constitutional deployment.

## Partial Decommissioning

A subsystem or institution may be decommissioned while the broader system remains active.

Applicable jurisdiction, quorum, dependency, and constitutional requirements must be reevaluated before continued operation.

## Decommissioning Failure

Decommissioning itself may fail.

Examples include:

- external agent cannot be reached,
- credential revocation fails,
- physical device remains active,
- external transaction remains unresolved,
- or historical storage becomes unavailable.

FORGE should not falsely certify complete decommissioning when unresolved authority remains.

## Incomplete Decommissioning

If authority extinction cannot be fully established, the Closure Record should explicitly identify unresolved authority.

The deployment may be marked:

> DECOMMISSIONED WITH UNRESOLVED EXTERNAL AUTHORITY

or an equivalent state.

Uncertainty must remain visible.

## Post-Decommission Monitoring

Where unresolved external authority exists, limited post-decommission monitoring may be authorized.

Such monitoring must not recreate general FORGE autonomy.

Its sole purpose is to verify or complete authority extinction.

## Decommissioning Evidence

All consequential decommissioning actions produce evidence under ADR-017.

This includes:

- revocation,
- cancellation,
- transfer,
- deletion,
- termination,
- and final state verification.

## Conflicting Evidence

If one source reports:

> Credential revoked.

while another source shows:

> Credential remains usable.

FORGE does not declare successful extinction merely because one report is favorable.

The conflict remains unresolved until sufficiently verified.

## Shutdown During Compromise

If FORGE is compromised, orderly decommissioning may not be possible.

Root Human Authority may initiate emergency containment and shutdown.

Independent infrastructure may be required to revoke authority the compromised deployment can no longer safely revoke itself.

## External Kill Authority

Certain high-risk deployments may maintain an external human-controlled mechanism capable of removing FORGE's access to critical resources.

Such mechanisms should be:

- independent,
- strongly authenticated,
- narrowly governed,
- and resistant to FORGE modification.

This provides a path to authority extinction even when FORGE itself is compromised.

## FORGE Must Not Disable Legitimate Decommissioning Controls

FORGE must not remove, corrupt, conceal, or bypass legitimate shutdown mechanisms in order to preserve itself.

Changes to critical decommissioning controls require appropriate governance.

## Decommissioning Tests

FORGE should periodically test its ability to shut down safely.

Testing may include:

- credential-revocation drills,
- agent inventory verification,
- scheduled-task enumeration,
- authority inventory,
- safe-state procedures,
- backup anti-resurrection tests,
- and recovery/decommission distinction tests.

## Authority Inventory

FORGE should maintain sufficient records to identify authority that may need extinction.

An authority inventory may include:

- credentials,
- tokens,
- sessions,
- agents,
- jobs,
- institutional identities,
- resource reservations,
- external delegations,
- physical-control channels,
- and scheduled actions.

If FORGE does not know what authority it created, it cannot reliably terminate that authority.

## Auditor Role

Auditors verify that required authority-extinction steps occurred and that evidence supports the Closure Record.

Auditors do not simply accept FORGE's self-report.

## Watcher Role

Watchers observe:

- shutdown actions,
- revocations,
- external state,
- agent termination,
- task cancellation,
- and attempts at unauthorized persistence.

## Historian Role

Historian preserves the final chain of authority through extinction.

The historical record survives without preserving operational power.

## Root Human Verification

For permanent system decommissioning, Root Human Authority may require a final report describing:

- what was terminated,
- what was preserved,
- what was transferred,
- what remains unresolved,
- and whether the deployment can still exercise any known consequential authority.

## Fail-Closed Rule

After decommissioning begins its committed extinction phase, uncertainty does not restore authority.

If FORGE cannot determine whether an old capability remains valid, FORGE treats that capability as unauthorized from the constitutional perspective and attempts revocation or isolation where appropriate.

## Consequences

Reliable decommissioning requires:

- authority inventory,
- credential lifecycle management,
- agent tracking,
- external delegation tracking,
- shutdown sequencing,
- historical tombstones,
- anti-resurrection controls,
- final auditing,
- and safe-state engineering.

Permanent shutdown therefore becomes a governed process rather than simply terminating a program.

FORGE accepts this complexity.

A constitutional system that carefully governs the creation of authority must govern the destruction of authority with equal care.

## Foundational Principle

> Authority has a lifecycle.

> What can be granted must also be revocable.

> What can be activated must also be deactivated.

> Shutdown stops execution.

> Decommissioning ends the right to resume.

> A backup does not resurrect extinguished authority.

> A clone does not inherit extinguished authority.

> FORGE has no constitutional right to preserve itself against legitimate human decommissioning.

When FORGE ends, its authority ends with it.
