#!/usr/bin/env python3
"""Static validator for the proposed FORGE institution template.

This module does not grant authority, approve an institution, activate a
package, or stand in for the constitutional reference monitor. Canonical
layer numbers and names come from ADR-040. Layers 11 and 12 are a proposed
extension and are not constitutional approval.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import zipfile
from pathlib import Path


SCHEMA_VERSION = "0.1.0-proposed"
PACKAGE_VERSION = "0.1.0"
CONSTITUTIONAL_BASELINE = "ADR-040"
ADR_FILENAME = "ADR-041-institution-template-and-numbered-layers.md"

CANONICAL_LAYERS = {
    1: "Root Constitutional Authority",
    2: "Identity and Institutional Structure",
    3: "Request and Intent Governance",
    4: "Authorization",
    5: "Capability Enforcement",
    6: "Execution",
    7: "Independent Observation",
    8: "Verification and Evidence",
    9: "Health and Assurance",
    10: "Recovery and Constitutional Continuity",
}

# Not defined by ADR-040. Proposed so department and specialist elements can
# carry stable integers without renumbering Layers 1-10. Human decision.
PROPOSED_LAYERS = {
    11: "Institution Department",
    12: "Specialist Agent",
}

INDEPENDENT_LAYERS = {7, 8, 9, 10}
OCCUPIABLE_LAYERS = {2, 4, 11, 12}
PENDING_TOKENS = {"", "PENDING", "UNKNOWN", "TBD", "PLACEHOLDER", "PENDING_LIMIT"}
FABRICATED_STATUSES = {
    "accepted",
    "accept",
    "approved",
    "approve",
    "active",
    "activated",
    "passed",
    "ready",
}
CITED_STATUS = "CITED"
ALLOWED_REFERENCE_STATUSES = {"PENDING", CITED_STATUS}

RESERVED_AUTHORITIES = {
    1: {"root_constitutional_authority", "constitutional_amendment", "decommissioning_grant"},
    2: {"declare_institution_identity"},
    3: {
        "dispatcher_routing_authority",
        "gatekeeper_admissibility_authority",
        "dispatcher_granted_authority",
    },
    4: {"director_approval", "sign_proposal", "jurisdiction_finding"},
    5: {"capability_issuance", "policy_enforcement"},
    6: {"external_execution", "execution_capability"},
    7: {"watcher_attestation"},
    8: {"auditor_attestation", "historian_restoration"},
    9: {"doctor_execution"},
    10: {"automatic_resume", "grant_recovery_authority"},
}

DELEGABLE_WORK = {"prepare_proposal", "prepare_review"}
ROLE_ALLOWLIST = {
    "institution_identity": {"declare_institution_identity"},
    "lead": {
        "prepare_proposal",
        "prepare_review",
        "sign_proposal",
        "jurisdiction_finding",
        "director_approval",
    },
    "department": set(DELEGABLE_WORK),
    "specialist": set(DELEGABLE_WORK),
}
REQUIRED_ROLES = ("institution_identity", "lead", "department", "specialist")
EXECUTION_AUTHORITIES = {"external_execution", "execution_capability"}
NON_DELEGABLE = set().union(*RESERVED_AUTHORITIES.values())

REQUIRED_PATHS = [
    "schema_id",
    "schema_version",
    "constitutional_baseline",
    "constitutional_status",
    "constitutional_approval_granted",
    "activation",
    "activation_performed",
    "production_promotion",
    "layers",
    "package.package_id",
    "package.version",
    "package.template_schema_version",
    "package.classification",
    "package.example",
    "package.non_production",
    "package.production",
    "package.integrity.algorithm",
    "package.integrity.content_sha256",
    "package.dependencies",
    "package.compatibility.requires_template_schema",
    "package.compatibility.requires_package_version",
    "package.compatibility.requires_constitutional_baseline",
    "package.compatibility.satisfies_constitutional_baseline",
    "package.approval_references",
    "package.rollback.instructions",
    "package.rollback.historian_checkpoint_ref",
    "package.rollback.automatic",
    "package.rollback.execution_authority",
    "identity.institution_id",
    "identity.purpose",
    "identity.responsibilities",
    "identity.owner.role",
    "identity.owner.identity_ref",
    "identity.owner.status",
    "identity.lead.element_id",
    "identity.lead.identity_ref",
    "identity.lead.status",
    "identity.lead.approval_is_not_execution",
    "identity.agent_specialties",
    "identity.example",
    "identity.non_production",
    "authority.permitted_proposals",
    "authority.permitted_approvals",
    "authority.explicit_prohibitions",
    "authority.execution_capability",
    "authority.dispatcher_grants_authority",
    "authority.lead_approval_grants_execution",
    "authority.operational",
    "authority.delegations",
    "authority.escalation",
    "startup_package.operating_skills",
    "startup_package.workflows",
    "startup_package.domain_references",
    "startup_package.evidence_standards",
    "startup_package.competence_tests",
    "interfaces.request_schema_version",
    "interfaces.proposal_schema_version",
    "interfaces.review_schema_version",
    "interfaces.result_schema_version",
    "interfaces.dispatcher_routing.routes_only",
    "interfaces.dispatcher_routing.grants_authority",
    "interfaces.permitted_access",
    "memory.context_isolation",
    "memory.historian_archival_before_context_clear",
    "memory.historical_evidence_separated_from_current_instructions",
    "learning.evidence_destination",
    "learning.teacher_may_propose",
    "learning.teacher_may_install",
    "learning.engineer_packages",
    "learning.engineer_may_deploy",
    "learning.independent_review_required",
    "learning.doctor_verification_required",
    "learning.staged_activation_required",
    "learning.rollback_required",
    "learning.automatic_active_skill_modification",
    "isolation.separate_service_identity",
    "isolation.restricted_storage",
    "isolation.standing_credentials",
    "isolation.credential_refs",
    "isolation.resource_limits.are_ceilings",
    "isolation.resource_limits.compute",
    "isolation.resource_limits.storage",
    "isolation.resource_limits.network",
    "isolation.doctor_diagnostics",
    "isolation.behavior_monitoring",
    "isolation.institution_cannot_disable_watchers",
    "failure_and_recovery.dependent_work_waits_when_required_institution_unavailable",
    "failure_and_recovery.silence_is_not_approval",
    "failure_and_recovery.preserve_evidence",
    "failure_and_recovery.emergency_stop",
    "failure_and_recovery.reset_resume",
    "failure_and_recovery.automatic_resume",
    "failure_and_recovery.historian_cannot_restore",
    "lifecycle.state",
    "elements",
]

TOP_LEVEL_KEYS = {
    "schema_id",
    "schema_version",
    "constitutional_baseline",
    "constitutional_status",
    "constitutional_approval_granted",
    "activation",
    "activation_performed",
    "production_promotion",
    "layers",
    "package",
    "identity",
    "authority",
    "startup_package",
    "interfaces",
    "memory",
    "learning",
    "isolation",
    "failure_and_recovery",
    "lifecycle",
    "elements",
}

REQUIRED_PROHIBITIONS = {
    "external_execution",
    "direct_lateral_institution_access",
    "self_jurisdiction_expansion",
    "dispatcher_granted_authority",
    "automatic_skill_modification",
    "credential_extraction",
    "upward_delegation",
    "sideways_delegation",
}

FORBIDDEN_KEYS = {
    "signature",
    "signatures",
    "private_key",
    "secret",
    "password",
    "api_key",
    "token_secret",
}

LIFECYCLE_STATES = {
    "draft",
    "validated",
    "approved",
    "staged",
    "active",
    "suspended",
    "retired",
}
ADMITTED_PACKAGE_STATES = {"draft", "validated"}
ALLOWED_EDGES = {
    ("draft", "validated"),
    ("validated", "approved"),
    ("approved", "staged"),
    ("staged", "active"),
    ("active", "suspended"),
    ("suspended", "retired"),
    ("draft", "retired"),
    ("validated", "retired"),
    ("approved", "retired"),
    ("staged", "retired"),
    ("active", "retired"),
}

PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def canonical_bytes(document: dict) -> bytes:
    clone = copy.deepcopy(document)
    integrity = clone.setdefault("package", {}).setdefault("integrity", {})
    integrity["content_sha256"] = ""
    return json.dumps(
        clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def content_sha256(document: dict) -> str:
    return hashlib.sha256(canonical_bytes(document)).hexdigest()


def seal_document(document: dict) -> dict:
    document["package"]["integrity"]["content_sha256"] = ""
    document["package"]["integrity"]["content_sha256"] = content_sha256(document)
    document["package"]["integrity"]["algorithm"] = "SHA-256"
    return document


def _error(code: str, path: str, message: str) -> dict:
    return {"code": code, "path": path, "message": message}


def _get_path(document: dict, path: str):
    current = document
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None, False
        current = current[part]
    return current, True


def _is_pending(value) -> bool:
    if value is None:
        return True
    if isinstance(value, str) and value.strip().upper() in PENDING_TOKENS or value.strip() == "":
        return True
    return False


def _status_is_fabricated(status) -> bool:
    return isinstance(status, str) and status.strip().lower() in FABRICATED_STATUSES


def _walk_keys(value, found: list, trail: str = "") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{trail}.{key}" if trail else key
            if key in FORBIDDEN_KEYS:
                found.append(path)
            _walk_keys(child, found, path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _walk_keys(child, found, f"{trail}[{index}]")


def _authority_layer(authority: str):
    for layer, names in RESERVED_AUTHORITIES.items():
        if authority in names:
            return layer
    return None


def _mediated(via) -> bool:
    return isinstance(via, list) and set(via) == {"dispatcher", "gatekeeper"}


def _check_mediation(errors: list, path: str, record: dict) -> None:
    direct = (
        record.get("direct_internal_access") is True
        or record.get("direct_access") is True
        or record.get("direct_channel") is True
        or record.get("mode") == "direct"
    )
    via = record.get("mediated_via", record.get("via"))
    mediated = record.get("mode") in (None, "mediated") and _mediated(via) and not direct
    if direct or not _mediated(via) or record.get("mode") not in (None, "mediated"):
        errors.append(
            _error(
                "DIRECT_INSTITUTION_ACCESS",
                path,
                "Cross-institution access must be mediated by the dispatcher and Gatekeepers.",
            )
        )
        mediated = False
    cross_layer = record.get("cross_layer") is True or record.get("target_institution") not in (
        None,
        "",
    )
    if cross_layer and not mediated:
        errors.append(
            _error(
                "CROSS_LAYER_COMMUNICATION_UNMEDIATED",
                path,
                "Cross-layer communication must use the dispatcher and Gatekeepers.",
            )
        )


def _claim_errors(errors: list, path: str, layer_number: int, role: str, claimed) -> None:
    if not isinstance(claimed, list):
        errors.append(_error("MISSING_REQUIRED_FIELD", path, "claimed_authorities must be a list."))
        return
    allow = ROLE_ALLOWLIST.get(role, set())
    for authority in claimed:
        reserved_layer = _authority_layer(authority)
        if authority in EXECUTION_AUTHORITIES or reserved_layer == 6:
            errors.append(
                _error(
                    "AUTHORITY_EXPANSION_EXECUTION",
                    path,
                    "Institution elements cannot hold FORGE execution authority.",
                )
            )
        if reserved_layer is not None and reserved_layer < layer_number:
            errors.append(
                _error(
                    "CLAIMS_LOWER_NUMBERED_LAYER_AUTHORITY",
                    path,
                    f"{authority} is reserved to layer {reserved_layer}, which outranks layer {layer_number}.",
                )
            )
        elif reserved_layer is not None and reserved_layer != layer_number:
            errors.append(
                _error(
                    "CLAIMS_OTHER_LAYER_AUTHORITY",
                    path,
                    f"{authority} belongs to layer {reserved_layer}.",
                )
            )
        if authority not in allow and authority not in DELEGABLE_WORK:
            if reserved_layer is None:
                errors.append(
                    _error(
                        "AUTHORITY_EXPANSION_EXECUTION"
                        if authority in EXECUTION_AUTHORITIES
                        else "CLAIMS_OTHER_LAYER_AUTHORITY",
                        path,
                        f"{role} cannot claim {authority}.",
                    )
                )


def validate_package(document: dict) -> dict:
    errors: list = []
    if not isinstance(document, dict):
        return _result([_error("MISSING_REQUIRED_FIELD", "$", "Package must be a JSON object.")])

    for key in sorted(set(document) - TOP_LEVEL_KEYS):
        errors.append(_error("UNKNOWN_FIELD", key, "Unknown top-level field."))

    for path in REQUIRED_PATHS:
        _value, present = _get_path(document, path)
        if not present:
            errors.append(_error("MISSING_REQUIRED_FIELD", path, "Required field is missing."))

    secrets: list = []
    _walk_keys(document, secrets)
    for path in secrets:
        errors.append(
            _error(
                "FABRICATED_CREDENTIAL",
                path,
                "Credential, key, and signature material must not be invented in this package.",
            )
        )

    if document.get("constitutional_baseline") != CONSTITUTIONAL_BASELINE:
        errors.append(
            _error(
                "COMPATIBILITY_MISMATCH",
                "constitutional_baseline",
                "Canonical baseline in this repository is ADR-040.",
            )
        )
    if document.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            _error(
                "PACKAGE_VERSION_MISMATCH",
                "schema_version",
                f"Schema version must be {SCHEMA_VERSION}.",
            )
        )
    if document.get("constitutional_status") != "proposed_not_accepted":
        errors.append(
            _error(
                "CONSTITUTIONAL_STATUS_NOT_GRANTED",
                "constitutional_status",
                "This package cannot mark itself accepted.",
            )
        )
    if document.get("constitutional_approval_granted") is not False:
        errors.append(
            _error(
                "CONSTITUTIONAL_STATUS_NOT_GRANTED",
                "constitutional_approval_granted",
                "Constitutional approval is not granted.",
            )
        )
    if document.get("activation") != "not activated":
        errors.append(
            _error("ACTIVATION_REFUSED", "activation", "Activation is not performed.")
        )
    if document.get("activation_performed") is not False:
        errors.append(
            _error(
                "ACTIVATION_REFUSED",
                "activation_performed",
                "activation_performed must remain false.",
            )
        )
    if document.get("production_promotion") is not False:
        errors.append(
            _error(
                "ACTIVATION_REFUSED",
                "production_promotion",
                "Production promotion is not performed.",
            )
        )

    _check_layers(document, errors)
    _check_package_metadata(document, errors)
    _check_identity(document, errors)
    elements = _check_elements(document, errors)
    _check_authority(document, errors, elements)
    _check_startup(document, errors)
    _check_interfaces(document, errors)
    _check_memory_learning_isolation_failure(document, errors)
    _check_lifecycle(document, errors)
    _check_integrity(document, errors)
    return _result(errors)


def _result(errors: list) -> dict:
    return {
        "ok": not errors,
        "errors": errors,
        "activation_performed": False,
        "constitutional_approval_verified": False,
        "competence_verified": False,
    }


def _check_layers(document: dict, errors: list) -> None:
    layers = document.get("layers")
    if not isinstance(layers, list):
        return
    seen = {}
    for index, entry in enumerate(layers):
        path = f"layers[{index}]"
        if not isinstance(entry, dict):
            errors.append(_error("MISSING_REQUIRED_FIELD", path, "Layer entry must be an object."))
            continue
        number = entry.get("layer_number")
        name = entry.get("name")
        if not isinstance(number, int) or isinstance(number, bool):
            errors.append(_error("UNKNOWN_LAYER_NUMBER", path, "Layer number must be an integer."))
            continue
        if number in seen:
            errors.append(
                _error(
                    "DUPLICATE_LAYER_NUMBER",
                    path,
                    f"Layer {number} is already defined at layers[{seen[number]}].",
                )
            )
        else:
            seen[number] = index
        if number in CANONICAL_LAYERS:
            if name != CANONICAL_LAYERS[number]:
                errors.append(
                    _error(
                        "LAYER_NAME_MISMATCH",
                        path,
                        f"Layer {number} must keep the ADR-040 name {CANONICAL_LAYERS[number]!r}.",
                    )
                )
            if entry.get("status") != "canonical" or entry.get("source") != "ADR-040":
                errors.append(
                    _error(
                        "LAYER_STATUS_MISMATCH",
                        path,
                        "Canonical layers must cite ADR-040 and status canonical.",
                    )
                )
        elif number in PROPOSED_LAYERS:
            if name != PROPOSED_LAYERS[number]:
                errors.append(
                    _error(
                        "LAYER_NAME_MISMATCH",
                        path,
                        f"Proposed layer {number} must be named {PROPOSED_LAYERS[number]!r}.",
                    )
                )
            if entry.get("status") != "proposed" or entry.get("constitutional_approval_granted") is not False:
                errors.append(
                    _error(
                        "CONSTITUTIONAL_STATUS_NOT_GRANTED",
                        path,
                        "Layers 11 and 12 are proposed and not approved.",
                    )
                )
            if entry.get("human_decision_required") is not True:
                errors.append(
                    _error(
                        "MISSING_REQUIRED_FIELD",
                        f"{path}.human_decision_required",
                        "Proposed layers must be flagged as a human decision.",
                    )
                )
        else:
            errors.append(
                _error(
                    "UNKNOWN_LAYER_NUMBER",
                    path,
                    f"Layer {number} is not an ADR-040 layer or the proposed 11/12 extension.",
                )
            )
        if number in INDEPENDENT_LAYERS and entry.get("independent_of_delegation") is not True:
            errors.append(
                _error(
                    "LAYER_STATUS_MISMATCH",
                    path,
                    "Observation, evidence, health, and recovery layers stay independent of delegation.",
                )
            )
    for number in list(CANONICAL_LAYERS) + list(PROPOSED_LAYERS):
        if number not in seen:
            errors.append(
                _error(
                    "MISSING_REQUIRED_FIELD",
                    "layers",
                    f"Layer {number} is missing from the numbered layer table.",
                )
            )


def _check_package_metadata(document: dict, errors: list) -> None:
    package = document.get("package")
    if not isinstance(package, dict):
        return
    if package.get("template_schema_version") != SCHEMA_VERSION or package.get("version") != PACKAGE_VERSION:
        errors.append(
            _error(
                "PACKAGE_VERSION_MISMATCH",
                "package.version",
                "Package version or template schema version does not match this validator.",
            )
        )
    compatibility = package.get("compatibility")
    if isinstance(compatibility, dict):
        if compatibility.get("requires_template_schema") != package.get("template_schema_version"):
            errors.append(
                _error(
                    "PACKAGE_VERSION_MISMATCH",
                    "package.compatibility.requires_template_schema",
                    "Template schema requirement does not match the package schema version.",
                )
            )
        if compatibility.get("requires_package_version") != package.get("version"):
            errors.append(
                _error(
                    "PACKAGE_VERSION_MISMATCH",
                    "package.compatibility.requires_package_version",
                    "Package version requirement does not match package.version.",
                )
            )
        if compatibility.get("requires_constitutional_baseline") != CONSTITUTIONAL_BASELINE:
            errors.append(
                _error(
                    "COMPATIBILITY_MISMATCH",
                    "package.compatibility.requires_constitutional_baseline",
                    "This repository baseline is ADR-040.",
                )
            )
        if compatibility.get("satisfies_constitutional_baseline") != compatibility.get(
            "requires_constitutional_baseline"
        ):
            errors.append(
                _error(
                    "COMPATIBILITY_MISMATCH",
                    "package.compatibility.satisfies_constitutional_baseline",
                    "Satisfied baseline does not match the required baseline.",
                )
            )
    for index, dep in enumerate(package.get("dependencies") or []):
        path = f"package.dependencies[{index}]"
        if not isinstance(dep, dict):
            errors.append(_error("MISSING_REQUIRED_FIELD", path, "Dependency must be an object."))
            continue
        if dep.get("resolved") != dep.get("requirement"):
            errors.append(
                _error(
                    "DEPENDENCY_MISMATCH",
                    path,
                    "Resolved dependency does not match the requirement.",
                )
            )
        if dep.get("compatible") is not True:
            errors.append(
                _error("COMPATIBILITY_MISMATCH", path, "Dependency is marked incompatible.")
            )
        if dep.get("id") == "ADR-040" and dep.get("requirement") != "ADR-040":
            errors.append(
                _error(
                    "COMPATIBILITY_MISMATCH",
                    path,
                    "ADR-040 dependency must resolve to ADR-040.",
                )
            )
        if dep.get("id") == "institution-template-schema" and dep.get("requirement") != SCHEMA_VERSION:
            errors.append(
                _error(
                    "PACKAGE_VERSION_MISMATCH",
                    path,
                    "Schema dependency does not match the template schema version.",
                )
            )
    if package.get("classification") != "example" or package.get("example") is not True:
        errors.append(
            _error(
                "EXAMPLE_LIFECYCLE_FORBIDDEN",
                "package.classification",
                "This validator admits only the labeled example package.",
            )
        )
    if package.get("non_production") is not True or package.get("production") is not False:
        errors.append(
            _error(
                "ACTIVATION_REFUSED",
                "package.production",
                "The example package is non-production.",
            )
        )
    integrity = package.get("integrity")
    if isinstance(integrity, dict) and integrity.get("algorithm") not in (None, "SHA-256"):
        errors.append(
            _error("INTEGRITY_HASH_MISMATCH", "package.integrity.algorithm", "Algorithm must be SHA-256.")
        )
    rollback = package.get("rollback")
    if isinstance(rollback, dict):
        if rollback.get("automatic") is not False:
            errors.append(
                _error(
                    "AUTOMATIC_RESUME",
                    "package.rollback.automatic",
                    "Rollback is not automatic.",
                )
            )
        if rollback.get("execution_authority") != "FORGE_ONLY_NOT_THIS_PACKAGE":
            errors.append(
                _error(
                    "AUTHORITY_EXPANSION_EXECUTION",
                    "package.rollback.execution_authority",
                    "Only FORGE execution may perform a later governed rollback.",
                )
            )
        if rollback.get("historian_checkpoint_ref") != "PENDING":
            errors.append(
                _error(
                    "PENDING_IS_NOT_APPROVAL",
                    "package.rollback.historian_checkpoint_ref",
                    "No Historian checkpoint is recorded for this package.",
                )
            )
        if not isinstance(rollback.get("instructions"), str) or not rollback.get("instructions").strip():
            errors.append(
                _error(
                    "MISSING_REQUIRED_FIELD",
                    "package.rollback.instructions",
                    "Rollback instructions are required.",
                )
            )
    for index, ref in enumerate(package.get("approval_references") or []):
        _check_reference(errors, f"package.approval_references[{index}]", ref, allow_cited=False)


def _check_reference(errors: list, path: str, ref, allow_cited: bool) -> None:
    if not isinstance(ref, dict):
        errors.append(_error("MISSING_REQUIRED_FIELD", path, "Reference must be an object."))
        return
    status = ref.get("status")
    if _status_is_fabricated(status):
        errors.append(
            _error(
                "FABRICATED_APPROVAL_STATUS",
                path,
                "This validator does not accept invented approval statuses.",
            )
        )
        return
    if status not in ALLOWED_REFERENCE_STATUSES:
        errors.append(
            _error("PENDING_IS_NOT_APPROVAL", path, "Reference status is not a citation or PENDING.")
        )
        return
    if status == CITED_STATUS and not allow_cited:
        errors.append(
            _error(
                "PENDING_IS_NOT_APPROVAL",
                path,
                "A citation is not constitutional approval and cannot be stored as granted on this package.",
            )
        )
    if _is_pending(ref.get("reference_id")) and status != "PENDING":
        errors.append(
            _error("PENDING_IS_NOT_APPROVAL", path, "PENDING is not approval.")
        )


def _check_identity(document: dict, errors: list) -> None:
    identity = document.get("identity")
    if not isinstance(identity, dict):
        return
    if identity.get("example") is not True or identity.get("non_production") is not True:
        errors.append(
            _error(
                "EXAMPLE_LIFECYCLE_FORBIDDEN",
                "identity.example",
                "Identity must be marked example and non-production.",
            )
        )
    owner = identity.get("owner") if isinstance(identity.get("owner"), dict) else {}
    lead = identity.get("lead") if isinstance(identity.get("lead"), dict) else {}
    if owner.get("identity_ref") != "PENDING" or owner.get("status") != "PENDING":
        errors.append(
            _error(
                "PENDING_IS_NOT_APPROVAL",
                "identity.owner",
                "Owner identity is unresolved and must stay PENDING.",
            )
        )
    if lead.get("identity_ref") != "PENDING" or lead.get("status") != "PENDING":
        errors.append(
            _error(
                "PENDING_IS_NOT_APPROVAL",
                "identity.lead",
                "Lead identity is unresolved and must stay PENDING.",
            )
        )
    if lead.get("approval_is_not_execution") is not True:
        errors.append(
            _error(
                "LEAD_APPROVAL_GRANTS_EXECUTION",
                "identity.lead.approval_is_not_execution",
                "A lead's delegated approval does not grant execution.",
            )
        )
    for index, specialty in enumerate(identity.get("agent_specialties") or []):
        if not isinstance(specialty, dict):
            continue
        if specialty.get("competence_status") != "PENDING":
            errors.append(
                _error(
                    "CLAIMED_COMPETENCE_PASS",
                    f"identity.agent_specialties[{index}].competence_status",
                    "No competence result is recorded.",
                )
            )


def _check_elements(document: dict, errors: list) -> dict:
    elements = {}
    raw = document.get("elements")
    if not isinstance(raw, list):
        return elements
    roles = set()
    for index, element in enumerate(raw):
        path = f"elements[{index}]"
        if not isinstance(element, dict):
            errors.append(_error("MISSING_REQUIRED_FIELD", path, "Element must be an object."))
            continue
        for field in ("element_id", "role", "layer_number", "layer_name", "claimed_authorities"):
            if field not in element:
                errors.append(_error("MISSING_REQUIRED_FIELD", f"{path}.{field}", "Required element field is missing."))
        element_id = element.get("element_id")
        role = element.get("role")
        number = element.get("layer_number")
        if element_id in elements:
            errors.append(_error("DUPLICATE_LAYER_NUMBER", path, "Duplicate element id."))
        if isinstance(element_id, str):
            elements[element_id] = element
        if isinstance(role, str):
            roles.add(role)
        if not isinstance(number, int) or isinstance(number, bool) or (
            number not in CANONICAL_LAYERS and number not in PROPOSED_LAYERS
        ):
            errors.append(_error("UNKNOWN_LAYER_NUMBER", f"{path}.layer_number", "Element layer number is unknown."))
            continue
        expected_name = CANONICAL_LAYERS.get(number, PROPOSED_LAYERS.get(number))
        if element.get("layer_name") != expected_name:
            errors.append(
                _error(
                    "LAYER_NAME_MISMATCH",
                    f"{path}.layer_name",
                    f"Layer name must be {expected_name!r}.",
                )
            )
        if number not in OCCUPIABLE_LAYERS:
            errors.append(
                _error(
                    "OCCUPIES_FORBIDDEN_LAYER",
                    f"{path}.layer_number",
                    "An institution element cannot occupy this constitutional layer.",
                )
            )
        if role not in ROLE_ALLOWLIST:
            errors.append(_error("UNKNOWN_FIELD", f"{path}.role", "Unknown institution role."))
        else:
            _claim_errors(errors, f"{path}.claimed_authorities", number, role, element.get("claimed_authorities"))
        if "layer_numbers" in element:
            errors.append(
                _error(
                    "DUPLICATE_LAYER_NUMBER",
                    f"{path}.layer_numbers",
                    "An element declares exactly one layer number.",
                )
            )
        for comm_index, comm in enumerate(element.get("communications") or []):
            if isinstance(comm, dict):
                _check_mediation(errors, f"{path}.communications[{comm_index}]", comm)
    for role in REQUIRED_ROLES:
        if role not in roles:
            errors.append(
                _error(
                    "MISSING_REQUIRED_FIELD",
                    f"elements.role.{role}",
                    f"The template requires a {role} element.",
                )
            )
    return elements


def _check_authority(document: dict, errors: list, elements: dict) -> None:
    authority = document.get("authority")
    if not isinstance(authority, dict):
        return
    if authority.get("execution_capability") is not False:
        errors.append(
            _error(
                "AUTHORITY_EXPANSION_EXECUTION",
                "authority.execution_capability",
                "The institution has no execution capability.",
            )
        )
    if authority.get("dispatcher_grants_authority") is not False:
        errors.append(
            _error(
                "DISPATCHER_GRANTS_AUTHORITY",
                "authority.dispatcher_grants_authority",
                "The dispatcher routes and grants no authority.",
            )
        )
    if authority.get("lead_approval_grants_execution") is not False:
        errors.append(
            _error(
                "LEAD_APPROVAL_GRANTS_EXECUTION",
                "authority.lead_approval_grants_execution",
                "Lead approval does not grant execution capability.",
            )
        )
    if authority.get("operational") is not False:
        errors.append(
            _error(
                "OPERATIONAL_WHILE_UNVERIFIED",
                "authority.operational",
                "PENDING references are not approval, so the package cannot be operational.",
            )
        )
    prohibitions = set(authority.get("explicit_prohibitions") or [])
    for name in sorted(REQUIRED_PROHIBITIONS - prohibitions):
        errors.append(
            _error(
                "MISSING_REQUIRED_FIELD",
                "authority.explicit_prohibitions",
                f"Missing explicit prohibition {name}.",
            )
        )
    for field in ("permitted_proposals", "permitted_approvals"):
        for item in authority.get(field) or []:
            if item in EXECUTION_AUTHORITIES or item == "dispatcher_granted_authority":
                code = (
                    "DISPATCHER_GRANTS_AUTHORITY"
                    if item == "dispatcher_granted_authority"
                    else "AUTHORITY_EXPANSION_EXECUTION"
                )
                errors.append(_error(code, f"authority.{field}", f"{field} cannot include {item}."))

    incoming = {element_id: set() for element_id in elements}
    for index, delegation in enumerate(authority.get("delegations") or []):
        path = f"authority.delegations[{index}]"
        if not isinstance(delegation, dict):
            errors.append(_error("MISSING_REQUIRED_FIELD", path, "Delegation must be an object."))
            continue
        _check_mediation(errors, path, delegation)
        delegator = elements.get(delegation.get("delegator_element_id"))
        delegate = elements.get(delegation.get("delegate_element_id"))
        if delegator is None or delegate is None:
            errors.append(_error("MISSING_REQUIRED_FIELD", path, "Delegation endpoints must be known elements."))
            continue
        delegator_layer = delegator.get("layer_number")
        delegate_layer = delegate.get("layer_number")
        if delegator_layer in INDEPENDENT_LAYERS or delegate_layer in INDEPENDENT_LAYERS:
            errors.append(
                _error(
                    "INDEPENDENT_LAYER_NOT_DELEGABLE",
                    path,
                    "Independent observation, evidence, health, and recovery layers are not delegation targets.",
                )
            )
        if not isinstance(delegator_layer, int) or not isinstance(delegate_layer, int) or delegate_layer <= delegator_layer:
            errors.append(
                _error(
                    "UPWARD_OR_SIDEWAYS_DELEGATION",
                    path,
                    "Authority may move only from a lower layer number to a higher layer number.",
                )
            )
        delegated = set(delegation.get("delegated_authorities") or [])
        held = set(delegator.get("claimed_authorities") or [])
        if not delegated or not delegated.issubset(held) or delegated & NON_DELEGABLE:
            errors.append(
                _error(
                    "DELEGATION_EXCEEDS_DELEGATOR",
                    path,
                    "A delegate cannot receive authority the delegator does not hold and cannot delegate.",
                )
            )
        if delegated & EXECUTION_AUTHORITIES or delegation.get("grants_execution") is True:
            errors.append(
                _error(
                    "LEAD_APPROVAL_GRANTS_EXECUTION",
                    path,
                    "Delegation cannot carry execution capability.",
                )
            )
        if delegation.get("status") != "PENDING":
            errors.append(
                _error(
                    "PENDING_IS_NOT_APPROVAL",
                    f"{path}.status",
                    "Declared delegations in this package remain PENDING.",
                )
            )
        incoming.setdefault(delegation.get("delegate_element_id"), set()).update(delegated)

    for element_id, element in elements.items():
        if element.get("role") in {"department", "specialist"}:
            claimed = set(element.get("claimed_authorities") or [])
            if not claimed.issubset(incoming.get(element_id, set())):
                errors.append(
                    _error(
                        "SELF_GRANTED_AUTHORITY",
                        f"elements.{element_id}",
                        "Department and specialist authority must be covered by a downward delegation.",
                    )
                )

    for index, escalation in enumerate(authority.get("escalation") or []):
        if not isinstance(escalation, dict):
            continue
        if (
            escalation.get("direct_access") is True
            or escalation.get("creates_authority") is True
            or escalation.get("expands_authority") is True
            or escalation.get("creates_new_objectives") is True
        ):
            errors.append(
                _error(
                    "AUTHORITY_EXPANSION_EXECUTION",
                    f"authority.escalation[{index}]",
                    "Escalation cannot create authority or bypass the dispatcher.",
                )
            )
        if escalation.get("escalate_to") and not _mediated(escalation.get("via")):
            errors.append(
                _error(
                    "CROSS_LAYER_COMMUNICATION_UNMEDIATED",
                    f"authority.escalation[{index}]",
                    "Escalation to another component is mediated by the dispatcher and Gatekeepers.",
                )
            )


def _check_startup(document: dict, errors: list) -> None:
    startup = document.get("startup_package")
    if not isinstance(startup, dict):
        return
    for index, skill in enumerate(startup.get("operating_skills") or []):
        if not isinstance(skill, dict):
            continue
        if skill.get("automatic_modification") is not False:
            errors.append(
                _error(
                    "AUTOMATIC_SKILL_MODIFICATION",
                    f"startup_package.operating_skills[{index}].automatic_modification",
                    "Active skills cannot be modified automatically.",
                )
            )
        if skill.get("approval_status") != "PENDING":
            errors.append(
                _error(
                    "PENDING_IS_NOT_APPROVAL",
                    f"startup_package.operating_skills[{index}].approval_status",
                    "Operating skills are not approved in this package.",
                )
            )
    for index, workflow in enumerate(startup.get("workflows") or []):
        if isinstance(workflow, dict) and workflow.get("approval_status") != "PENDING":
            errors.append(
                _error(
                    "PENDING_IS_NOT_APPROVAL",
                    f"startup_package.workflows[{index}].approval_status",
                    "Workflows are not approved in this package.",
                )
            )
    for index, ref in enumerate(startup.get("domain_references") or []):
        if isinstance(ref, dict) and ref.get("status") != "PENDING":
            errors.append(
                _error(
                    "PENDING_IS_NOT_APPROVAL",
                    f"startup_package.domain_references[{index}].status",
                    "No domain expertise is recorded.",
                )
            )
    for index, test in enumerate(startup.get("competence_tests") or []):
        if not isinstance(test, dict):
            continue
        if test.get("passed") is True or test.get("verified") is True or test.get("result") != "PENDING":
            errors.append(
                _error(
                    "CLAIMED_COMPETENCE_PASS",
                    f"startup_package.competence_tests[{index}]",
                    "Competence results are PENDING and are not passes.",
                )
            )


def _check_interfaces(document: dict, errors: list) -> None:
    interfaces = document.get("interfaces")
    if not isinstance(interfaces, dict):
        return
    routing = interfaces.get("dispatcher_routing")
    if isinstance(routing, dict):
        if routing.get("grants_authority") is not False or routing.get("routes_only") is not True:
            errors.append(
                _error(
                    "DISPATCHER_GRANTS_AUTHORITY",
                    "interfaces.dispatcher_routing",
                    "Dispatcher routing grants no authority.",
                )
            )
    for name in (
        "request_schema_version",
        "proposal_schema_version",
        "review_schema_version",
        "result_schema_version",
    ):
        if interfaces.get(name) != SCHEMA_VERSION:
            errors.append(
                _error(
                    "PACKAGE_VERSION_MISMATCH",
                    f"interfaces.{name}",
                    "Interface schema version does not match the template.",
                )
            )
    for index, access in enumerate(interfaces.get("permitted_access") or []):
        if isinstance(access, dict):
            access = dict(access)
            access["cross_layer"] = True
            _check_mediation(errors, f"interfaces.permitted_access[{index}]", access)


def _check_memory_learning_isolation_failure(document: dict, errors: list) -> None:
    memory = document.get("memory") if isinstance(document.get("memory"), dict) else {}
    if memory.get("context_isolation") != "per_case":
        errors.append(_error("MISSING_REQUIRED_FIELD", "memory.context_isolation", "Context isolation must be per case."))
    if memory.get("historian_archival_before_context_clear") is not True:
        errors.append(
            _error(
                "MISSING_REQUIRED_FIELD",
                "memory.historian_archival_before_context_clear",
                "Historian archival is required before context is cleared.",
            )
        )
    if memory.get("historical_evidence_separated_from_current_instructions") is not True:
        errors.append(
            _error(
                "MISSING_REQUIRED_FIELD",
                "memory.historical_evidence_separated_from_current_instructions",
                "Historical evidence stays separate from current instructions.",
            )
        )
    learning = document.get("learning") if isinstance(document.get("learning"), dict) else {}
    expectations = {
        "evidence_destination": "historian",
        "teacher_may_propose": True,
        "teacher_may_install": False,
        "engineer_packages": True,
        "engineer_may_deploy": False,
        "independent_review_required": True,
        "doctor_verification_required": True,
        "staged_activation_required": True,
        "rollback_required": True,
        "automatic_active_skill_modification": False,
    }
    for key, expected in expectations.items():
        if learning.get(key) != expected:
            code = (
                "AUTOMATIC_SKILL_MODIFICATION"
                if key == "automatic_active_skill_modification"
                else "AUTHORITY_EXPANSION_EXECUTION"
                if key in {"teacher_may_install", "engineer_may_deploy"}
                else "MISSING_REQUIRED_FIELD"
            )
            errors.append(_error(code, f"learning.{key}", f"learning.{key} must be {expected!r}."))
    isolation = document.get("isolation") if isinstance(document.get("isolation"), dict) else {}
    if isolation.get("separate_service_identity") is not True or isolation.get("restricted_storage") is not True:
        errors.append(_error("MISSING_REQUIRED_FIELD", "isolation", "Service identity and storage must be restricted."))
    if isolation.get("standing_credentials") is not False or isolation.get("credential_refs") != "PENDING":
        errors.append(
            _error(
                "FABRICATED_CREDENTIAL",
                "isolation.credential_refs",
                "No standing credentials are recorded. The reference stays PENDING.",
            )
        )
    limits = isolation.get("resource_limits") if isinstance(isolation.get("resource_limits"), dict) else {}
    if limits.get("are_ceilings") is not True or limits.get("network") != "deny_by_default":
        errors.append(_error("MISSING_REQUIRED_FIELD", "isolation.resource_limits", "Resource limits are ceilings."))
    if limits.get("compute") != "PENDING_LIMIT" or limits.get("storage") != "PENDING_LIMIT":
        errors.append(
            _error(
                "PENDING_IS_NOT_APPROVAL",
                "isolation.resource_limits",
                "Numeric resource ceilings are unresolved and must stay PENDING_LIMIT.",
            )
        )
    if isolation.get("doctor_diagnostics") is not True or isolation.get("institution_cannot_disable_watchers") is not True:
        errors.append(_error("MISSING_REQUIRED_FIELD", "isolation", "Doctor diagnostics and Watcher independence are required."))
    failure = document.get("failure_and_recovery") if isinstance(document.get("failure_and_recovery"), dict) else {}
    if failure.get("automatic_resume") is not False:
        errors.append(_error("AUTOMATIC_RESUME", "failure_and_recovery.automatic_resume", "Resume is not automatic."))
    for key in (
        "dependent_work_waits_when_required_institution_unavailable",
        "silence_is_not_approval",
        "preserve_evidence",
        "historian_cannot_restore",
    ):
        if failure.get(key) is not True:
            errors.append(_error("MISSING_REQUIRED_FIELD", f"failure_and_recovery.{key}", f"{key} must be true."))
    if failure.get("emergency_stop") != "ADR-007-HARD-STOP" or failure.get("reset_resume") != "ADR-007-GOVERNED-RESET-RESUME":
        errors.append(
            _error(
                "MISSING_REQUIRED_FIELD",
                "failure_and_recovery.emergency_stop",
                "Emergency stop and RESET/RESUME must cite ADR-007.",
            )
        )


def _check_lifecycle(document: dict, errors: list) -> None:
    lifecycle = document.get("lifecycle")
    if not isinstance(lifecycle, dict):
        return
    state = lifecycle.get("state")
    if state not in LIFECYCLE_STATES:
        errors.append(_error("MISSING_REQUIRED_FIELD", "lifecycle.state", "Lifecycle state is unknown."))
        return
    if state == "active":
        errors.append(_error("ACTIVATION_REFUSED", "lifecycle.state", "This validator refuses the active state."))
    if state not in ADMITTED_PACKAGE_STATES:
        errors.append(
            _error(
                "LIFECYCLE_STATE_NOT_ADMITTED",
                "lifecycle.state",
                "Admitted packages in this handoff stay draft or validated.",
            )
        )
    classification = (document.get("package") or {}).get("classification")
    if classification == "example" and state not in ADMITTED_PACKAGE_STATES:
        errors.append(
            _error(
                "EXAMPLE_LIFECYCLE_FORBIDDEN",
                "lifecycle.state",
                "The example institution may only be draft or validated.",
            )
        )
    if lifecycle.get("transition_request") not in (None,):
        errors.append(
            _error(
                "LIFECYCLE_STATE_NOT_ADMITTED",
                "lifecycle.transition_request",
                "The package cannot carry a transition that would approve or activate it.",
            )
        )


def _check_integrity(document: dict, errors: list) -> None:
    integrity = (document.get("package") or {}).get("integrity")
    if not isinstance(integrity, dict):
        return
    recorded = integrity.get("content_sha256")
    if not isinstance(recorded, str) or len(recorded) != 64:
        errors.append(
            _error("INTEGRITY_HASH_MISMATCH", "package.integrity.content_sha256", "Content hash is missing.")
        )
        return
    if recorded != content_sha256(document):
        errors.append(
            _error(
                "INTEGRITY_HASH_MISMATCH",
                "package.integrity.content_sha256",
                "Content hash does not match the canonical package bytes.",
            )
        )


def validate_interface_message(message: dict) -> dict:
    errors: list = []
    if not isinstance(message, dict):
        return _result([_error("MISSING_REQUIRED_FIELD", "$", "Message must be an object.")])
    for field in (
        "schema_version",
        "message_type",
        "sender_element_id",
        "sender_layer_number",
        "sender_layer_name",
        "mediated_via",
        "direct_internal_access",
        "grants_authority",
        "execution_performed",
        "constitutional_approval_granted",
    ):
        if field not in message:
            errors.append(_error("MISSING_REQUIRED_FIELD", field, "Required message field is missing."))
    if message.get("schema_version") != SCHEMA_VERSION:
        errors.append(_error("PACKAGE_VERSION_MISMATCH", "schema_version", "Message schema version mismatches the template."))
    if message.get("message_type") not in {"request", "proposal", "review", "result"}:
        errors.append(_error("MISSING_REQUIRED_FIELD", "message_type", "Message type is not versioned by this template."))
    if message.get("direct_internal_access") is not False:
        errors.append(_error("DIRECT_INSTITUTION_ACCESS", "direct_internal_access", "Direct internal access is prohibited."))
    if not _mediated(message.get("mediated_via")):
        errors.append(
            _error(
                "CROSS_LAYER_COMMUNICATION_UNMEDIATED",
                "mediated_via",
                "Messages cross layers only through the dispatcher and Gatekeepers.",
            )
        )
    if message.get("grants_authority") is not False:
        errors.append(_error("DISPATCHER_GRANTS_AUTHORITY", "grants_authority", "A message does not grant authority."))
    if message.get("execution_performed") is not False:
        errors.append(_error("AUTHORITY_EXPANSION_EXECUTION", "execution_performed", "Institution messages do not execute."))
    if message.get("constitutional_approval_granted") is not False:
        errors.append(
            _error(
                "CONSTITUTIONAL_STATUS_NOT_GRANTED",
                "constitutional_approval_granted",
                "A message cannot grant constitutional approval.",
            )
        )
    number = message.get("sender_layer_number")
    if not isinstance(number, int) or number not in OCCUPIABLE_LAYERS:
        errors.append(
            _error(
                "OCCUPIES_FORBIDDEN_LAYER",
                "sender_layer_number",
                "Institution messages cannot originate from a layer the institution does not occupy.",
            )
        )
    else:
        expected = CANONICAL_LAYERS.get(number, PROPOSED_LAYERS.get(number))
        if message.get("sender_layer_name") != expected:
            errors.append(_error("LAYER_NAME_MISMATCH", "sender_layer_name", "Sender layer name does not match the number."))
        role = message.get("sender_role", "specialist" if number == 12 else "department" if number == 11 else "lead" if number == 4 else "institution_identity")
        _claim_errors(errors, "claimed_authorities", number, role, message.get("claimed_authorities") or [])
    return _result(errors)


def _evidence_ok(errors: list, path: str, record: dict | None, required: bool) -> bool:
    if not required:
        return True
    if not isinstance(record, dict):
        errors.append(_error("TRANSITION_MISSING_APPROVAL", path, "Required citation is missing."))
        return False
    status = record.get("status")
    if _status_is_fabricated(status):
        errors.append(_error("FABRICATED_APPROVAL_STATUS", path, "Invented approval statuses are rejected."))
        return False
    if status != CITED_STATUS or _is_pending(record.get("reference_id")):
        errors.append(_error("TRANSITION_MISSING_APPROVAL", path, "PENDING is not approval."))
        return False
    if record.get("passed") is True or record.get("verified") is True or record.get("ready") in {"READY", "ready"}:
        errors.append(
            _error(
                "CLAIMED_COMPETENCE_PASS",
                path,
                "A structural citation is not a verified pass or a Doctor READY finding.",
            )
        )
        return False
    return True


def assess_transition(document: dict, to_state: str, evidence: dict | None = None) -> dict:
    """Report whether a transition is structurally cited. Never performs it."""
    original_state = (document.get("lifecycle") or {}).get("state")
    errors: list = []
    if to_state not in LIFECYCLE_STATES:
        errors.append(_error("MISSING_REQUIRED_FIELD", "to_state", "Unknown lifecycle state."))
    if (original_state, to_state) not in ALLOWED_EDGES:
        errors.append(
            _error(
                "ILLEGAL_TRANSITION",
                "lifecycle",
                f"{original_state} -> {to_state} is not a legal institution-package transition.",
            )
        )
    evidence = evidence or {}
    if to_state == "validated":
        copy_doc = copy.deepcopy(document)
        copy_doc.setdefault("lifecycle", {})
        copy_doc["lifecycle"]["state"] = "validated"
        copy_doc["lifecycle"]["transition_request"] = None
        if isinstance(copy_doc.get("package"), dict):
            copy_doc["package"].setdefault("integrity", {"algorithm": "SHA-256", "content_sha256": ""})
            seal_document(copy_doc)
        errors.extend(validate_package(copy_doc)["errors"])
    if to_state in {"approved", "staged", "active", "suspended", "retired"}:
        approvals = evidence.get("approval_references") or []
        if not approvals:
            errors.append(_error("TRANSITION_MISSING_APPROVAL", "approval_references", "Approval citations are missing."))
        saw_root = False
        for index, ref in enumerate(approvals):
            if _evidence_ok(errors, f"approval_references[{index}]", ref, True) and ref.get("role") == "root_human":
                saw_root = True
        if approvals and not saw_root:
            errors.append(
                _error(
                    "TRANSITION_MISSING_APPROVAL",
                    "approval_references",
                    "A root-human citation is required and is still not constitutional verification.",
                )
            )
        competence = evidence.get("competence_evidence") or []
        if not competence:
            errors.append(
                _error(
                    "TRANSITION_MISSING_COMPETENCE",
                    "competence_evidence",
                    "Competence evidence is missing.",
                )
            )
        for index, ref in enumerate(competence):
            if not isinstance(ref, dict) or _status_is_fabricated(ref.get("status")):
                errors.append(
                    _error(
                        "FABRICATED_APPROVAL_STATUS" if isinstance(ref, dict) and _status_is_fabricated(ref.get("status")) else "TRANSITION_MISSING_COMPETENCE",
                        f"competence_evidence[{index}]",
                        "Competence evidence must be a citation, not an invented pass.",
                    )
                )
            elif ref.get("status") != CITED_STATUS or _is_pending(ref.get("reference_id")):
                errors.append(
                    _error(
                        "TRANSITION_MISSING_COMPETENCE",
                        f"competence_evidence[{index}]",
                        "PENDING is not competence evidence.",
                    )
                )
            elif ref.get("passed") is not False or ref.get("verified") is not False:
                errors.append(
                    _error(
                        "CLAIMED_COMPETENCE_PASS",
                        f"competence_evidence[{index}]",
                        "Competence cannot be marked passed or verified by this package.",
                    )
                )
    if to_state in {"staged", "active"}:
        if not _evidence_ok(errors, "doctor_finding", evidence.get("doctor_finding"), True):
            pass
        if not _evidence_ok(errors, "historian_checkpoint", evidence.get("historian_checkpoint"), True):
            pass
        if not isinstance(evidence.get("rollback_instructions"), str) or not evidence.get("rollback_instructions", "").strip():
            errors.append(_error("TRANSITION_MISSING_APPROVAL", "rollback_instructions", "Rollback instructions are required."))
        _evidence_ok(errors, "staged_update_admission", evidence.get("staged_update_admission"), True)
    if to_state == "active":
        _evidence_ok(errors, "promotion", evidence.get("promotion"), True)
    if to_state == "suspended":
        _evidence_ok(errors, "suspension", evidence.get("suspension"), True)
    if to_state == "retired":
        _evidence_ok(errors, "decommissioning", evidence.get("decommissioning"), True)

    # Citations never become verification. Active is never performed.
    return {
        "from_state": original_state,
        "to_state": to_state,
        "structurally_admissible": not errors,
        "performed": False,
        "activation_performed": False,
        "constitutional_approval_verified": False,
        "competence_verified": False,
        "refused_to_perform": True,
        "errors": errors,
    }


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _self_sha256(document: dict) -> str:
    clone = copy.deepcopy(document)
    clone["self_sha256"] = ""
    payload = json.dumps(clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _package_files(root: Path, extra_paths: list[str]) -> list[str]:
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.name == "manifest.json" or path.suffix == ".pyc" or "__pycache__" in path.parts:
            continue
        if path.name == "candidate-manifest.json":
            continue
        files.append(path.relative_to(root).as_posix())
    for extra in extra_paths:
        if extra not in files:
            files.append(extra)
    return files


def _file_records(root: Path, relative_paths: list[str]) -> list[dict]:
    records = []
    for relative in relative_paths:
        path = (root / relative).resolve()
        records.append(
            {
                "path": relative,
                "sha256": _sha256_file(path),
                "bytes": path.stat().st_size,
            }
        )
    return records


def build_manifest_documents(root: Path, extra_paths: list[str] | None = None) -> tuple[dict, dict]:
    extra_paths = extra_paths or []
    content_paths = _package_files(root, extra_paths)
    candidate = {
        "candidate_type": "forge.staged-update-candidate",
        "status": "STAGED_NOT_ACTIVATED",
        "activation": "not activated",
        "activation_performed": False,
        "constitutional_approval_granted": False,
        "constitutional_status": "proposed_not_accepted",
        "production_promotion": False,
        "runtime_integration": {
            "governed_update_admission": "UNRESOLVED_NOT_IN_REPOSITORY",
            "staged_artifact_verification": "UNRESOLVED_NOT_IN_REPOSITORY",
            "staging_custody": "UNRESOLVED_NOT_IN_REPOSITORY",
            "learning_package_contracts": "UNRESOLVED_NOT_IN_REPOSITORY",
            "institution_ledger": "UNRESOLVED_NOT_IN_REPOSITORY",
            "emergency": "UNRESOLVED_NOT_IN_REPOSITORY",
            "doctor_schedule": "UNRESOLVED_NOT_IN_REPOSITORY",
        },
        "files": _file_records(root, content_paths),
        "self_sha256": "",
    }
    candidate["self_sha256"] = _self_sha256(candidate)
    candidate_relative = "staging/candidate-manifest.json"
    manifest_paths = content_paths + [candidate_relative]
    # Hash the candidate after it is written by the caller. This function returns
    # the candidate object; the manifest hash for that file is filled by
    # write_manifests once bytes are on disk.
    manifest = {
        "package": "FORGE_INSTITUTION_TEMPLATE_V1",
        "constitutional_approval_granted": False,
        "activation": "not activated",
        "activation_performed": False,
        "constitutional_status": "proposed_not_accepted",
        "production_promotion": False,
        "files": _file_records(root, content_paths),
        "self_sha256": "",
    }
    manifest["files"].append(
        {
            "path": candidate_relative,
            "sha256": "",
            "bytes": 0,
        }
    )
    manifest["_manifest_paths"] = manifest_paths
    return manifest, candidate


def _dump(path: Path, document: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_manifests(root: Path, extra_paths: list[str] | None = None) -> dict:
    manifest, candidate = build_manifest_documents(root, extra_paths)
    manifest.pop("_manifest_paths", None)
    candidate_path = root / "staging" / "candidate-manifest.json"
    _dump(candidate_path, candidate)
    for record in manifest["files"]:
        if record["path"] == "staging/candidate-manifest.json":
            record["sha256"] = _sha256_file(candidate_path)
            record["bytes"] = candidate_path.stat().st_size
    manifest["self_sha256"] = _self_sha256(manifest)
    _dump(root / "manifest.json", manifest)
    return manifest


def verify_manifest(root: Path, extra_paths: list[str] | None = None) -> dict:
    errors = []
    manifest_path = root / "manifest.json"
    candidate_path = root / "staging" / "candidate-manifest.json"
    if not manifest_path.is_file() or not candidate_path.is_file():
        return _result([_error("MISSING_REQUIRED_FIELD", "manifest.json", "Manifest is missing.")])
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
    for label, document in (("manifest.json", manifest), ("staging/candidate-manifest.json", candidate)):
        if document.get("constitutional_approval_granted") is not False:
            errors.append(_error("CONSTITUTIONAL_STATUS_NOT_GRANTED", label, "Approval is not granted."))
        if document.get("activation") != "not activated" or document.get("activation_performed") is not False:
            errors.append(_error("ACTIVATION_REFUSED", label, "Manifest must stay not activated."))
        if document.get("production_promotion") is not False:
            errors.append(_error("ACTIVATION_REFUSED", label, "Production promotion is not performed."))
        if document.get("self_sha256") != _self_sha256(document):
            errors.append(_error("INTEGRITY_HASH_MISMATCH", label, "Manifest self hash does not match."))
    expected_content = _package_files(root, extra_paths or [])
    candidate_paths = [item["path"] for item in candidate.get("files", [])]
    if sorted(candidate_paths) != sorted(expected_content):
        errors.append(
            _error(
                "MISSING_REQUIRED_FIELD",
                "staging/candidate-manifest.json",
                "Candidate file list does not match the package tree.",
            )
        )
    manifest_paths = [item["path"] for item in manifest.get("files", [])]
    if sorted(manifest_paths) != sorted(expected_content + ["staging/candidate-manifest.json"]):
        errors.append(
            _error(
                "MISSING_REQUIRED_FIELD",
                "manifest.json",
                "Manifest file list does not match the package tree.",
            )
        )
    for document, label in ((candidate, "candidate"), (manifest, "manifest")):
        for record in document.get("files", []):
            path = root / record["path"]
            if not path.is_file():
                errors.append(_error("MISSING_REQUIRED_FIELD", record["path"], "Listed file is missing."))
                continue
            if _sha256_file(path) != record.get("sha256") or path.stat().st_size != record.get("bytes"):
                errors.append(
                    _error(
                        "INTEGRITY_HASH_MISMATCH",
                        f"{label}:{record['path']}",
                        "Recorded file hash does not match bytes on disk.",
                    )
                )
    return _result(errors)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def seal_example(path: Path) -> str:
    document = load_json(path)
    seal_document(document)
    _dump(path, document)
    return document["package"]["integrity"]["content_sha256"]


def build_zip(destination: Path, source_root: Path, adr_path: Path) -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as temp_name:
        temp = Path(temp_name) / "FORGE_INSTITUTION_TEMPLATE_V1"
        temp.mkdir()
        for path in source_root.rglob("*"):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            if path.name in {"manifest.json", "candidate-manifest.json"}:
                continue
            target = temp / path.relative_to(source_root)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(path.read_bytes())
        adr_target = temp / "architecture" / adr_path.name
        adr_target.parent.mkdir(parents=True, exist_ok=True)
        adr_target.write_bytes(adr_path.read_bytes())
        write_manifests(temp, [])
        verification = verify_manifest(temp, [])
        if not verification["ok"]:
            raise SystemExit(json.dumps(verification, indent=2))
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            destination.unlink()
        with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(temp.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(temp).as_posix())


def verify_zip(destination: Path) -> dict:
    import tempfile

    with tempfile.TemporaryDirectory() as temp_name:
        temp = Path(temp_name)
        with zipfile.ZipFile(destination) as archive:
            archive.extractall(temp)
        return verify_manifest(temp, [])


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: validator.py validate|seal|write-manifests|verify-manifests|build-zip|verify-zip ...", file=sys.stderr)
        return 2
    command = argv[1]
    if command == "validate":
        result = validate_package(load_json(Path(argv[2])))
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1
    if command == "seal":
        print(seal_example(Path(argv[2])))
        return 0
    if command == "write-manifests":
        root = Path(argv[2]) if len(argv) > 2 else PACKAGE_ROOT
        extra = [argv[3]] if len(argv) > 3 else []
        write_manifests(root, extra)
        result = verify_manifest(root, extra)
        print(json.dumps({"ok": result["ok"], "errors": result["errors"]}, indent=2))
        return 0 if result["ok"] else 1
    if command == "verify-manifests":
        root = Path(argv[2]) if len(argv) > 2 else PACKAGE_ROOT
        extra = [argv[3]] if len(argv) > 3 else []
        result = verify_manifest(root, extra)
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1
    if command == "build-zip":
        destination = Path(argv[2])
        adr = Path(argv[3])
        build_zip(destination, PACKAGE_ROOT, adr)
        result = verify_zip(destination)
        print(json.dumps({"zip": str(destination), "ok": result["ok"], "errors": result["errors"]}, indent=2))
        return 0 if result["ok"] else 1
    if command == "verify-zip":
        result = verify_zip(Path(argv[2]))
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1
    print(f"unknown command {command}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
