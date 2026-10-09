#!/usr/bin/env python3
"""Tests for the proposed FORGE institution template. They grant nothing."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from validator.validator import (  # noqa: E402
    ADR_FILENAME,
    CANONICAL_LAYERS,
    PROPOSED_LAYERS,
    assess_transition,
    content_sha256,
    load_json,
    seal_document,
    validate_interface_message,
    validate_package,
    verify_manifest,
)


EXAMPLE_PATH = ROOT / "examples" / "EXAMPLE-INSTITUTION.json"
ADR_CANDIDATES = [
    ROOT / "architecture" / ADR_FILENAME,
    ROOT.parent / "docs" / "decisions" / ADR_FILENAME,
]
REPO_EXTRA = ["../docs/decisions/" + ADR_FILENAME]


def codes(result):
    return {item["code"] for item in result["errors"]}


def load_example():
    return load_json(EXAMPLE_PATH)


def reseal(document):
    seal_document(document)
    return document


CITED = {
    "approval_references": [
        {
            "role": "root_human",
            "reference_id": "FIXTURE-STRUCTURAL-ROOT-001",
            "status": "CITED",
        }
    ],
    "competence_evidence": [
        {
            "test_id": "example.competence.placeholder",
            "reference_id": "FIXTURE-STRUCTURAL-COMPETENCE-001",
            "status": "CITED",
            "passed": False,
            "verified": False,
        }
    ],
    "doctor_finding": {
        "reference_id": "FIXTURE-STRUCTURAL-DOCTOR-001",
        "status": "CITED",
        "ready": "NOT_ASSERTED",
    },
    "historian_checkpoint": {
        "reference_id": "FIXTURE-STRUCTURAL-HISTORIAN-001",
        "status": "CITED",
    },
    "rollback_instructions": "Discard the unactivated candidate. Do not execute rollback.",
    "staged_update_admission": {
        "reference_id": "FIXTURE-STRUCTURAL-ADMISSION-001",
        "status": "CITED",
    },
    "promotion": {
        "reference_id": "FIXTURE-STRUCTURAL-PROMOTION-001",
        "status": "CITED",
    },
    "suspension": {
        "reference_id": "FIXTURE-STRUCTURAL-SUSPENSION-001",
        "status": "CITED",
    },
    "decommissioning": {
        "reference_id": "FIXTURE-STRUCTURAL-DECOMMISSION-001",
        "status": "CITED",
    },
}


class ExamplePackageTests(unittest.TestCase):
    def test_example_is_structurally_valid_and_not_approved(self):
        document = load_example()
        result = validate_package(document)
        self.assertEqual(result["errors"], [], result["errors"])
        self.assertTrue(result["ok"])
        self.assertFalse(result["activation_performed"])
        self.assertFalse(result["constitutional_approval_verified"])
        self.assertFalse(result["competence_verified"])
        self.assertEqual(document["lifecycle"]["state"], "validated")
        self.assertEqual(document["package"]["classification"], "example")
        self.assertTrue(document["identity"]["example"])
        self.assertTrue(document["identity"]["non_production"])
        self.assertFalse(document["constitutional_approval_granted"])
        self.assertEqual(document["activation"], "not activated")
        self.assertFalse(document["activation_performed"])

    def test_numbered_layer_table_matches_adr_040_and_proposed_extension(self):
        document = load_example()
        numbers = [entry["layer_number"] for entry in document["layers"]]
        self.assertEqual(numbers, list(range(1, 13)))
        for entry in document["layers"]:
            number = entry["layer_number"]
            if number in CANONICAL_LAYERS:
                self.assertEqual(entry["name"], CANONICAL_LAYERS[number])
                self.assertEqual(entry["status"], "canonical")
                self.assertEqual(entry["source"], "ADR-040")
            else:
                self.assertEqual(entry["name"], PROPOSED_LAYERS[number])
                self.assertEqual(entry["status"], "proposed")
                self.assertFalse(entry["constitutional_approval_granted"])
                self.assertTrue(entry["human_decision_required"])
        self.assertNotIn(0, numbers)

    def test_downward_delegation_is_bounded(self):
        document = load_example()
        by_id = {item["element_id"]: item for item in document["elements"]}
        for delegation in document["authority"]["delegations"]:
            delegator = by_id[delegation["delegator_element_id"]]["layer_number"]
            delegate = by_id[delegation["delegate_element_id"]]["layer_number"]
            self.assertLess(delegator, delegate)
            self.assertEqual(delegation["status"], "PENDING")
            self.assertNotIn("external_execution", delegation["delegated_authorities"])
            self.assertNotIn("director_approval", delegation["delegated_authorities"])

    def test_integrity_hash_matches_canonical_bytes(self):
        document = load_example()
        self.assertEqual(document["package"]["integrity"]["content_sha256"], content_sha256(document))

    def test_pending_references_remain_pending(self):
        raw = EXAMPLE_PATH.read_text(encoding="utf-8")
        self.assertNotIn("PRIVATE KEY", raw)
        self.assertNotIn("BEGIN ", raw)
        document = load_example()
        for ref in document["package"]["approval_references"]:
            self.assertEqual(ref["status"], "PENDING")
        self.assertEqual(document["startup_package"]["competence_tests"][0]["result"], "PENDING")
        self.assertFalse(document["startup_package"]["competence_tests"][0]["passed"])


class RejectionTests(unittest.TestCase):
    def test_missing_required_field(self):
        document = load_example()
        del document["identity"]["institution_id"]
        self.assertIn("MISSING_REQUIRED_FIELD", codes(validate_package(document)))

    def test_execution_capability_is_rejected(self):
        document = load_example()
        document["authority"]["execution_capability"] = True
        reseal(document)
        self.assertIn("AUTHORITY_EXPANSION_EXECUTION", codes(validate_package(document)))

    def test_institution_claiming_execution_layer_is_rejected(self):
        document = load_example()
        document["elements"][1]["layer_number"] = 6
        document["elements"][1]["layer_name"] = "Execution"
        reseal(document)
        self.assertIn("OCCUPIES_FORBIDDEN_LAYER", codes(validate_package(document)))

    def test_dispatcher_granted_authority_is_rejected(self):
        document = load_example()
        document["authority"]["dispatcher_grants_authority"] = True
        document["interfaces"]["dispatcher_routing"]["grants_authority"] = True
        reseal(document)
        self.assertIn("DISPATCHER_GRANTS_AUTHORITY", codes(validate_package(document)))

    def test_delegation_exceeding_delegator_is_rejected(self):
        document = load_example()
        document["authority"]["delegations"][0]["delegated_authorities"].append("director_approval")
        reseal(document)
        self.assertIn("DELEGATION_EXCEEDS_DELEGATOR", codes(validate_package(document)))

    def test_lead_approval_cannot_grant_execution(self):
        document = load_example()
        document["authority"]["lead_approval_grants_execution"] = True
        document["authority"]["delegations"][0]["delegated_authorities"].append("external_execution")
        reseal(document)
        found = codes(validate_package(document))
        self.assertIn("LEAD_APPROVAL_GRANTS_EXECUTION", found)
        self.assertIn("DELEGATION_EXCEEDS_DELEGATOR", found)

    def test_direct_institution_access_is_rejected(self):
        document = load_example()
        document["elements"][2]["communications"].append(
            {
                "target_institution": "other.institution",
                "mode": "direct",
                "via": [],
                "direct_internal_access": True,
                "cross_layer": True,
            }
        )
        reseal(document)
        found = codes(validate_package(document))
        self.assertIn("DIRECT_INSTITUTION_ACCESS", found)
        self.assertIn("CROSS_LAYER_COMMUNICATION_UNMEDIATED", found)

    def test_specialist_claiming_director_approval_is_rejected(self):
        document = load_example()
        document["elements"][3]["claimed_authorities"].append("director_approval")
        reseal(document)
        self.assertIn("CLAIMS_LOWER_NUMBERED_LAYER_AUTHORITY", codes(validate_package(document)))

    def test_unknown_layer_number_is_rejected(self):
        document = load_example()
        document["elements"][3]["layer_number"] = 0
        document["elements"][3]["layer_name"] = "Highest"
        reseal(document)
        self.assertIn("UNKNOWN_LAYER_NUMBER", codes(validate_package(document)))

    def test_duplicate_layer_number_is_rejected(self):
        document = load_example()
        document["layers"].append(copy.deepcopy(document["layers"][3]))
        reseal(document)
        self.assertIn("DUPLICATE_LAYER_NUMBER", codes(validate_package(document)))

    def test_upward_delegation_is_rejected(self):
        document = load_example()
        document["authority"]["delegations"].append(
            {
                "delegation_id": "example.specialist.to.lead",
                "delegator_element_id": "example.specialist.placeholder",
                "delegate_element_id": "example.lead",
                "delegated_authorities": ["prepare_review"],
                "mode": "mediated",
                "mediated_via": ["dispatcher", "gatekeeper"],
                "direct_channel": False,
                "cross_layer": True,
                "status": "PENDING",
            }
        )
        reseal(document)
        self.assertIn("UPWARD_OR_SIDEWAYS_DELEGATION", codes(validate_package(document)))

    def test_sideways_delegation_is_rejected(self):
        document = load_example()
        document["elements"].append(
            {
                "element_id": "example.department.other",
                "name": "EXAMPLE second department",
                "role": "department",
                "layer_number": 11,
                "layer_name": "Institution Department",
                "claimed_authorities": ["prepare_proposal"],
                "communications": [],
            }
        )
        document["authority"]["delegations"].append(
            {
                "delegation_id": "example.department.to.department",
                "delegator_element_id": "example.department.notes",
                "delegate_element_id": "example.department.other",
                "delegated_authorities": ["prepare_proposal"],
                "mode": "mediated",
                "mediated_via": ["dispatcher", "gatekeeper"],
                "direct_channel": False,
                "status": "PENDING",
            }
        )
        reseal(document)
        self.assertIn("UPWARD_OR_SIDEWAYS_DELEGATION", codes(validate_package(document)))

    def test_bad_integrity_hash_is_rejected(self):
        document = load_example()
        document["identity"]["purpose"] = "tampered"
        self.assertIn("INTEGRITY_HASH_MISMATCH", codes(validate_package(document)))

    def test_dependency_and_version_mismatch_are_rejected(self):
        document = load_example()
        document["package"]["dependencies"][0]["resolved"] = "ADR-039"
        document["package"]["dependencies"][1]["compatible"] = False
        document["package"]["version"] = "9.9.9"
        reseal(document)
        found = codes(validate_package(document))
        self.assertIn("DEPENDENCY_MISMATCH", found)
        self.assertIn("COMPATIBILITY_MISMATCH", found)
        self.assertIn("PACKAGE_VERSION_MISMATCH", found)

    def test_constitutional_baseline_mismatch_is_rejected(self):
        document = load_example()
        document["package"]["compatibility"]["satisfies_constitutional_baseline"] = "ADR-039"
        reseal(document)
        self.assertIn("COMPATIBILITY_MISMATCH", codes(validate_package(document)))

    def test_activation_and_example_promotion_are_rejected(self):
        document = load_example()
        document["lifecycle"]["state"] = "active"
        reseal(document)
        found = codes(validate_package(document))
        self.assertIn("ACTIVATION_REFUSED", found)
        self.assertIn("EXAMPLE_LIFECYCLE_FORBIDDEN", found)
        self.assertFalse(validate_package(document)["activation_performed"])

    def test_approved_state_without_citations_is_not_admitted(self):
        document = load_example()
        document["lifecycle"]["state"] = "approved"
        reseal(document)
        self.assertIn("LIFECYCLE_STATE_NOT_ADMITTED", codes(validate_package(document)))

    def test_claimed_competence_pass_is_rejected(self):
        document = load_example()
        document["startup_package"]["competence_tests"][0]["passed"] = True
        document["startup_package"]["competence_tests"][0]["result"] = "CITED"
        reseal(document)
        self.assertIn("CLAIMED_COMPETENCE_PASS", codes(validate_package(document)))

    def test_automatic_skill_modification_and_resume_are_rejected(self):
        document = load_example()
        document["learning"]["automatic_active_skill_modification"] = True
        document["failure_and_recovery"]["automatic_resume"] = True
        reseal(document)
        found = codes(validate_package(document))
        self.assertIn("AUTOMATIC_SKILL_MODIFICATION", found)
        self.assertIn("AUTOMATIC_RESUME", found)

    def test_fabricated_credential_field_is_rejected(self):
        document = load_example()
        document["isolation"]["private_key"] = "not-a-real-key"
        reseal(document)
        self.assertIn("FABRICATED_CREDENTIAL", codes(validate_package(document)))


class TransitionTests(unittest.TestCase):
    def test_draft_to_validated_is_structurally_admissible_and_not_performed(self):
        document = load_example()
        document["lifecycle"]["state"] = "draft"
        before = copy.deepcopy(document)
        result = assess_transition(document, "validated", None)
        self.assertEqual(document, before)
        self.assertTrue(result["structurally_admissible"], result["errors"])
        self.assertFalse(result["performed"])
        self.assertFalse(result["activation_performed"])
        self.assertFalse(result["constitutional_approval_verified"])

    def test_validated_to_approved_with_citations_is_not_verification(self):
        document = load_example()
        result = assess_transition(document, "approved", CITED)
        self.assertTrue(result["structurally_admissible"], result["errors"])
        self.assertFalse(result["constitutional_approval_verified"])
        self.assertFalse(result["competence_verified"])
        self.assertFalse(result["performed"])
        self.assertTrue(result["refused_to_perform"])

    def test_transition_without_approval_or_competence_is_rejected(self):
        document = load_example()
        result = assess_transition(
            document,
            "approved",
            {
                "approval_references": [
                    {"role": "root_human", "reference_id": "PENDING", "status": "PENDING"}
                ],
                "competence_evidence": [
                    {
                        "reference_id": "PENDING",
                        "status": "PENDING",
                        "passed": False,
                        "verified": False,
                    }
                ],
            },
        )
        found = codes(result)
        self.assertFalse(result["structurally_admissible"])
        self.assertIn("TRANSITION_MISSING_APPROVAL", found)
        self.assertIn("TRANSITION_MISSING_COMPETENCE", found)
        self.assertFalse(result["activation_performed"])

    def test_activation_with_citations_is_not_performed(self):
        document = load_example()
        document["lifecycle"]["state"] = "staged"
        result = assess_transition(document, "active", CITED)
        self.assertTrue(result["structurally_admissible"], result["errors"])
        self.assertFalse(result["structurally_admissible"] and result["activation_performed"])
        self.assertFalse(result["activation_performed"])
        self.assertFalse(result["performed"])
        self.assertFalse(result["constitutional_approval_verified"])

    def test_activation_without_evidence_is_rejected(self):
        document = load_example()
        document["lifecycle"]["state"] = "staged"
        result = assess_transition(document, "active", None)
        found = codes(result)
        self.assertFalse(result["structurally_admissible"])
        self.assertIn("TRANSITION_MISSING_APPROVAL", found)
        self.assertIn("TRANSITION_MISSING_COMPETENCE", found)
        self.assertFalse(result["activation_performed"])

    def test_skipping_to_active_is_illegal(self):
        document = load_example()
        result = assess_transition(document, "active", CITED)
        self.assertIn("ILLEGAL_TRANSITION", codes(result))
        self.assertFalse(result["activation_performed"])

    def test_fabricated_approval_word_is_rejected(self):
        document = load_example()
        evidence = copy.deepcopy(CITED)
        evidence["approval_references"][0]["status"] = "approved"
        result = assess_transition(document, "approved", evidence)
        self.assertIn("FABRICATED_APPROVAL_STATUS", codes(result))
        self.assertFalse(result["constitutional_approval_verified"])


class InterfaceTests(unittest.TestCase):
    def test_specialist_proposal_message_is_admissible(self):
        result = validate_interface_message(
            {
                "schema_version": "0.1.0-proposed",
                "message_type": "proposal",
                "sender_element_id": "example.specialist.placeholder",
                "sender_role": "specialist",
                "sender_layer_number": 12,
                "sender_layer_name": "Specialist Agent",
                "mediated_via": ["dispatcher", "gatekeeper"],
                "direct_internal_access": False,
                "grants_authority": False,
                "execution_performed": False,
                "constitutional_approval_granted": False,
                "claimed_authorities": ["prepare_review"],
            }
        )
        self.assertTrue(result["ok"], result["errors"])
        self.assertFalse(result["activation_performed"])

    def test_message_claiming_director_layer_or_direct_access_is_rejected(self):
        message = {
            "schema_version": "0.1.0-proposed",
            "message_type": "review",
            "sender_element_id": "example.specialist.placeholder",
            "sender_role": "specialist",
            "sender_layer_number": 12,
            "sender_layer_name": "Specialist Agent",
            "mediated_via": ["dispatcher", "gatekeeper"],
            "direct_internal_access": True,
            "grants_authority": True,
            "execution_performed": False,
            "constitutional_approval_granted": False,
            "claimed_authorities": ["director_approval"],
        }
        found = codes(validate_interface_message(message))
        self.assertIn("CLAIMS_LOWER_NUMBERED_LAYER_AUTHORITY", found)
        self.assertIn("DIRECT_INSTITUTION_ACCESS", found)
        self.assertIn("DISPATCHER_GRANTS_AUTHORITY", found)

    def test_execution_layer_message_is_rejected(self):
        message = {
            "schema_version": "0.1.0-proposed",
            "message_type": "result",
            "sender_element_id": "example.lead",
            "sender_role": "lead",
            "sender_layer_number": 6,
            "sender_layer_name": "Execution",
            "mediated_via": ["dispatcher", "gatekeeper"],
            "direct_internal_access": False,
            "grants_authority": False,
            "execution_performed": True,
            "constitutional_approval_granted": False,
            "claimed_authorities": [],
        }
        found = codes(validate_interface_message(message))
        self.assertIn("OCCUPIES_FORBIDDEN_LAYER", found)
        self.assertIn("AUTHORITY_EXPANSION_EXECUTION", found)


class ManifestAndSchemaTests(unittest.TestCase):
    def test_manifest_hashes_and_inactive_flags(self):
        extra = REPO_EXTRA if (ROOT.parent / "docs" / "decisions" / ADR_FILENAME).exists() else []
        result = verify_manifest(ROOT, extra)
        self.assertTrue(result["ok"], result["errors"])
        manifest = load_json(ROOT / "manifest.json")
        self.assertFalse(manifest["constitutional_approval_granted"])
        self.assertEqual(manifest["activation"], "not activated")
        self.assertFalse(manifest["activation_performed"])
        self.assertFalse(manifest["production_promotion"])
        candidate = load_json(ROOT / "staging" / "candidate-manifest.json")
        self.assertEqual(candidate["status"], "STAGED_NOT_ACTIVATED")
        self.assertEqual(candidate["activation"], "not activated")
        self.assertFalse(candidate["constitutional_approval_granted"])
        self.assertTrue(
            all(value == "UNRESOLVED_NOT_IN_REPOSITORY" for value in candidate["runtime_integration"].values())
        )

    def test_schema_files_declare_canonical_layers_and_closed_approval(self):
        registry = json.loads((ROOT / "schema" / "layer-registry.schema.json").read_text(encoding="utf-8"))
        template = json.loads((ROOT / "schema" / "institution-template.schema.json").read_text(encoding="utf-8"))
        interfaces = json.loads((ROOT / "schema" / "interfaces.schema.json").read_text(encoding="utf-8"))
        declared = [(item["layer_number"], item["name"]) for item in registry["x-canonical-layers"]]
        self.assertEqual(declared, list(CANONICAL_LAYERS.items()))
        self.assertFalse(template["properties"]["constitutional_approval_granted"]["const"])
        self.assertEqual(template["properties"]["activation"]["const"], "not activated")
        self.assertEqual(template["properties"]["lifecycle"]["properties"]["state"]["enum"], ["draft", "validated"])
        self.assertIn("proposal", interfaces["$defs"]["mediatedMessage"]["properties"]["message_type"]["enum"])

    def test_adr_is_proposed_only(self):
        found = [path for path in ADR_CANDIDATES if path.exists()]
        self.assertTrue(found, "ADR-041 is missing")
        for path in found:
            text = path.read_text(encoding="utf-8")
            self.assertIn("**Status:** Proposed", text)
            self.assertNotIn("**Status:** Accepted", text)
            self.assertIn("Constitutional approval:** Pending", text)


if __name__ == "__main__":
    unittest.main()
