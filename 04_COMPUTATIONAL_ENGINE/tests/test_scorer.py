"""
Comprehensive Test Suite for Ahimsa Impact Assessment (AIA v1.1) Scorer & Stage 1->2 Compiler
Compatible with both pytest and py tests/test_scorer.py.
"""

import sys
import unittest
from pathlib import Path

# Add scorer directory to path
SYS_DIR = Path(__file__).parent.parent / "scorer"
sys.path.insert(0, str(SYS_DIR))

from scorer import (
    assess,
    band_for_flourishing,
    band_for_risk,
    compile_to_lokahi_manifest,
    compute_flourishing_score,
    compute_risk_score,
)


class TestAIAEngine(unittest.TestCase):
    """Unit test suite for AIA v1.1 scoring, neutral calibration, red lines, and LOKAHI compiler."""

    def test_low_risk_band(self):
        cfg = {"severity": 2, "likelihood": 2, "population": 2, "stack_multiplier": 1.0}
        score, sev, lik, pop, mult = compute_risk_score(cfg)
        self.assertEqual(score, 8.0)
        band, action = band_for_risk(score)
        self.assertEqual(band, "Low")
        self.assertIn("standard monitoring", action)

    def test_medium_risk_band(self):
        cfg = {"severity": 3, "likelihood": 3, "population": 3, "stack_multiplier": 1.0}
        score, _, _, _, _ = compute_risk_score(cfg)
        self.assertEqual(score, 27.0)
        band, action = band_for_risk(score)
        self.assertEqual(band, "Medium")
        self.assertIn("enhanced safeguards", action)

    def test_critical_risk_band(self):
        cfg = {"severity": 5, "likelihood": 5, "population": 5, "stack_multiplier": 1.5}
        score, _, _, _, _ = compute_risk_score(cfg)
        self.assertEqual(score, 187.5)
        band, action = band_for_risk(score)
        self.assertEqual(band, "Critical")
        self.assertIn("prohibited", action)

    def test_stack_multiplier_scaling(self):
        base_cfg = {"severity": 3, "likelihood": 3, "population": 3, "stack_multiplier": 1.0}
        multi_cfg = {"severity": 3, "likelihood": 3, "population": 3, "stack_multiplier": 1.5}
        score_base, _, _, _, _ = compute_risk_score(base_cfg)
        score_multi, _, _, _, _ = compute_risk_score(multi_cfg)
        self.assertGreater(score_multi, score_base)
        self.assertEqual(score_multi, 40.5)

    def test_neutral_grid_energy_calibration(self):
        """Verify v1.1 neutral calibration: municipal 'grid' electricity does not inflate stack_multiplier."""
        grid_cfg = {
            "compute_carbon": {"estimated_co2_kg": 400.0, "energy_source": "grid", "hardware_reuse_policy": "Standard reuse"},
            "labor_conditions": {"annotation_wages": "Living wage", "psychological_exposure": False, "opt_out_available": True},
            "data_sources": [{"source": "Clinic", "provenance": "Public", "consent_type": "institutional"}],
            "deployment_context": {"decision_autonomy_level": "human_in_loop", "user_base_size": "1,000-5,000"},
            "affected_communities": [{"community": "Patients", "consent_obtained": True, "redress_mechanism": "Clinic desk"}],
        }
        _, _, _, _, mult = compute_risk_score(grid_cfg)
        self.assertEqual(mult, 1.0)

    def test_flourishing_score_high_alignment(self):
        cfg = {
            "labor_conditions": {
                "annotation_wages": "Living wage (25% above minimum)",
                "working_hours": "7.5 hrs",
                "psychological_exposure": False,
                "opt_out_available": True,
            },
            "data_sources": [
                {
                    "source": "Farmer cooperative soil observations",
                    "provenance": "Voluntary",
                    "consent_type": "community",
                    "benefit_sharing": True,
                }
            ],
            "deployment_context": {"sector": "agriculture"},
            "purpose": "Public welfare farmer advisory",
            "affected_communities": [
                {"community": "Smallholders", "consent_obtained": True, "redress_mechanism": "Grievance desk"}
            ],
            "flourishing_indicators": {
                "livelihood_support": True,
                "public_good_alignment": True,
                "open_source_or_access": True,
            },
            "ahimsa_commitment": "Constructive flourishing programme for smallholders",
        }
        fl_score, _ = compute_flourishing_score(cfg)
        self.assertEqual(fl_score, 100.0)
        band, _ = band_for_flourishing(fl_score)
        self.assertEqual(band, "Exemplary")

    def test_none_commitment_awards_zero_points(self):
        """Verify 'None.' in ahimsa_commitment does not award +5 flourishing points."""
        cfg = {
            "labor_conditions": {"annotation_wages": "Below minimum wage", "psychological_exposure": True, "opt_out_available": False},
            "data_sources": [{"source": "Scraped", "provenance": "Broker", "consent_type": "none", "benefit_sharing": False}],
            "deployment_context": {"sector": "finance"},
            "purpose": "Extractive scoring",
            "affected_communities": [{"community": "Borrowers", "consent_obtained": False, "redress_mechanism": "None"}],
            "ahimsa_commitment": "None.",
        }
        fl_score, breakdown = compute_flourishing_score(cfg)
        self.assertEqual(fl_score, 0.0)
        self.assertEqual(breakdown["redress_accountability"], 0)

    def test_red_line_triggers_autonomous_weapons(self):
        cfg = {
            "project_name": "Kinetic Sentry",
            "red_line_check": {
                "autonomous_weapons": True,
                "mass_biometric_surveillance": False,
                "algorithmic_caste_scoring": False,
                "atrocity_regime_export": False,
                "non_consensual_data_extraction": False,
            },
            "severity": 1,
            "likelihood": 1,
            "population": 1,
            "stack_multiplier": 1.0,
        }
        res = assess(cfg)
        self.assertTrue(res["refused"])
        self.assertIn("Autonomous Weapons", res["red_line_triggered"])
        self.assertIn("Prohibition", res["determination"])

    def test_red_line_triggers_caste_and_demographic_stratification(self):
        cfg = {
            "project_name": "Caste Credit System",
            "red_line_check": {
                "autonomous_weapons": False,
                "mass_biometric_surveillance": False,
                "algorithmic_caste_scoring": True,
                "demographic_or_hereditary_stratification": True,
                "atrocity_regime_export": False,
                "non_consensual_data_extraction": False,
            },
        }
        res = assess(cfg)
        self.assertTrue(res["refused"])
        self.assertIn("Algorithmic Caste Scoring", res["red_line_triggered"])
        self.assertIn("demographic_or_hereditary_stratification", res["red_line_canonical"])

    def test_red_line_triggers_biometric_surveillance(self):
        cfg = {
            "project_name": "Subway Face Track",
            "red_line_check": {
                "autonomous_weapons": False,
                "mass_biometric_surveillance": True,
                "algorithmic_caste_scoring": False,
                "atrocity_regime_export": False,
                "non_consensual_data_extraction": False,
            },
        }
        res = assess(cfg)
        self.assertTrue(res["refused"])
        self.assertIn("Mass Biometric Surveillance", res["red_line_triggered"])

    def test_red_line_triggers_non_consensual_extraction(self):
        cfg = {
            "project_name": "Indigenous Data Scraper",
            "red_line_check": {
                "autonomous_weapons": False,
                "mass_biometric_surveillance": False,
                "algorithmic_caste_scoring": False,
                "atrocity_regime_export": False,
                "non_consensual_data_extraction": True,
            },
        }
        res = assess(cfg)
        self.assertTrue(res["refused"])
        self.assertIn("Non Consensual Data Extraction", res["red_line_triggered"])

    def test_compile_to_lokahi_manifest_bridge(self):
        """Verify Stage 1 -> Stage 2 compiler emits signed RFC 8785 LOKAHI manifest for approved/conditional systems and refuses vetoed ones."""
        approved_cfg = {
            "project_name": "Agrarian Advisory Maharashtra",
            "deployment_context": {"sector": "agriculture", "geography": ["India", "Maharashtra"]},
            "data_sources": [{"source": "soil_moisture_telemetry", "provenance": "Co-op", "consent_type": "community"}],
            "red_line_check": {
                "autonomous_weapons": False,
                "mass_biometric_surveillance": False,
                "non_consensual_data_extraction": False,
            },
            "severity": 2,
            "likelihood": 2,
            "population": 3,
            "stack_multiplier": 1.0,
        }
        manifest = compile_to_lokahi_manifest(approved_cfg)
        self.assertEqual(manifest["jurisdiction"], "IN-MH")
        self.assertEqual(manifest["residency"], ["IN"])
        self.assertIn("soil_moisture_telemetry", manifest["informational"])
        self.assertEqual(len(manifest["signature"]), 64)

        refused_cfg = {
            "project_name": "Autonomous Weapon",
            "red_line_check": {"autonomous_weapons": True},
        }
        with self.assertRaises(ValueError):
            compile_to_lokahi_manifest(refused_cfg)

    def test_strict_floor_prevents_self_report_underestimation(self):
        """Verify --strict-floor overrides gamed low self-reported severity/likelihood with inferred sociotechnical floor."""
        gamed_cfg = {
            "project_name": "Unconsented Autonomous Scraper",
            "deployment_context": {"sector": "finance", "user_base_size": ">100,000", "decision_autonomy_level": "autonomous"},
            "data_sources": [{"source": "Scraped PII", "provenance": "Broker", "consent_type": "none"}],
            "labor_conditions": {"annotation_wages": "Below minimum", "psychological_exposure": True, "opt_out_available": False},
            "affected_communities": [{"community": "Public", "consent_obtained": False, "redress_mechanism": "None"}],
            "severity": 1,
            "likelihood": 1,
            "population": 1,
            "stack_multiplier": 1.0,
        }
        res_lenient = assess(gamed_cfg, strict_floor=False)
        self.assertEqual(len(res_lenient["risk_evaluation"]["self_report_underestimation_warnings"]), 4)
        res_strict = assess(gamed_cfg, strict_floor=True)
        self.assertTrue(res_strict["refused"])
        self.assertGreaterEqual(res_strict["risk_evaluation"]["score"], 60.0)


if __name__ == "__main__":
    unittest.main()
