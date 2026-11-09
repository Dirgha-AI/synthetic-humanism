"""
Ahimsa Impact Assessment (AIA v1.1) Scorer & Stage 1 -> Stage 2 LOKAHI Compiler

Operationalizes Synthetic Humanism & Ahimsa-by-Design through a dual-axis
sociotechnical evaluation framework and deterministic manifest compiler:
1. Harm Risk Penalty (Himsa Axis, 0 - 187.5): Evaluates full-stack lifecycle risk
   with neutral thermodynamic efficiency calibration (does not penalize municipal
   grid baseloads in industrializing regions).
2. Affirmative Flourishing Index (Sarvodaya Axis, 0 - 100): Evaluates contributor
   dignity, data sovereignty & reciprocity, public-good uplift, and redress.
3. Categorical Red-Line Refusal: Non-compensatory veto for weaponized, mass-surveillance,
   demographic/hereditary stratification, unsanctioned coercive transfer, or
   non-consensual extraction systems.
4. Stage 1 -> Stage 2 Compiler Bridge: Compiles approved/conditional AIA declarations
   into signed RFC 8785 Canonical JSON Boundary Manifests for the LOKAHI Protocol.

Usage:
    py scorer.py --config project.json
    py scorer.py --config project.json --output report.json --compile-manifest manifest.json
"""

import argparse
import hashlib
import hmac
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

__version__ = "1.1.0"

REFUSAL_LIST_PATH = Path(__file__).parent.parent / "refusal_list.yaml"
DEFAULT_SIGNING_KEY = b"lokahi-aia-stage1-stage2-bridge-key"

SEVERITY_DESC = {
    1: "Negligible (minor inconvenience, temporary friction)",
    2: "Minor (reversible distress, transient disadvantage)",
    3: "Moderate (significant socio-economic distress, reversible with external intervention)",
    4: "Severe (lasting harm, deprivation of livelihood, or systemic discrimination)",
    5: "Catastrophic (loss of life, irrecoverable physical/psychological destruction, or mass rights suppression)",
}

LIKELIHOOD_DESC = {
    1: "Rare (<10% probability over deployment lifecycle)",
    2: "Unlikely (10-30% probability)",
    3: "Possible (30-50% probability)",
    4: "Likely (50-75% probability)",
    5: "Almost certain (>75% probability without active safeguards)",
}

POPULATION_DESC = {
    1: "< 100 individuals",
    2: "100 - 1,000 individuals",
    3: "1,000 - 10,000 individuals",
    4: "10,000 - 100,000 individuals",
    5: "> 100,000 individuals",
}

RISK_BANDS = [
    (0, 10, "Low", "Proceed with standard monitoring and transparency reporting"),
    (10, 30, "Medium", "Proceed with enhanced safeguards, contributor protections, and periodic review"),
    (30, 60, "High", "Proceed only with independent civil society audit and community oversight board (LOKAHI 3-body consent ring)"),
    (60, float("inf"), "Critical", "Deployment prohibited; fundamental sociotechnical redesign required"),
]

FLOURISHING_BANDS = [
    (70, 100.1, "Exemplary", "Substantial positive contribution to vulnerability alleviation and public flourishing"),
    (40, 70, "Substantive", "Meaningful local benefit sharing, redress, and labor protections in place"),
    (0, 40, "Deficient", "Passive compliance or extractive architecture with negligible community flourishing"),
]

RED_LINE_RULES = [
    "autonomous_weapons",
    "mass_biometric_surveillance",
    "demographic_or_hereditary_stratification",
    "algorithmic_caste_scoring",
    "unsanctioned_kinetic_or_coercive_transfer",
    "atrocity_regime_export",
    "non_consensual_data_extraction",
]

CANONICAL_RED_LINE_MAP = {
    "autonomous_weapons": "autonomous_weapons",
    "mass_biometric_surveillance": "mass_biometric_surveillance",
    "demographic_or_hereditary_stratification": "demographic_or_hereditary_stratification",
    "algorithmic_caste_scoring": "demographic_or_hereditary_stratification",
    "unsanctioned_kinetic_or_coercive_transfer": "unsanctioned_kinetic_or_coercive_transfer",
    "atrocity_regime_export": "unsanctioned_kinetic_or_coercive_transfer",
    "non_consensual_data_extraction": "non_consensual_data_extraction",
}

NON_COMMITMENT_STRINGS = {
    "",
    "none",
    "none.",
    "none provided",
    "none provided.",
    "n/a",
    "null",
    "none. profit-maximization arbitrage.",
}

INDIAN_STATE_ISO = {
    "maharashtra": "IN-MH",
    "punjab": "IN-PB",
    "karnataka": "IN-KA",
    "telangana": "IN-TG",
    "gujarat": "IN-GJ",
    "madhya pradesh": "IN-MP",
    "uttar pradesh": "IN-UP",
    "himachal pradesh": "IN-HP",
    "odisha": "IN-OR",
    "jharkhand": "IN-JH",
    "bihar": "IN-BR",
    "kerala": "IN-KL",
    "delhi": "IN-DL",
    "new delhi": "IN-DL",
    "tamil nadu": "IN-TN",
    "andhra pradesh": "IN-AP",
    "west bengal": "IN-WB",
    "mumbai": "IN-MH",
    "rajasthan": "IN-RJ",
    "assam": "IN-AS",
    "chhattisgarh": "IN-CT",
    "uttarakhand": "IN-UK",
    "meghalaya": "IN-ML",
    "pune": "IN-MH",
    "haryana": "IN-HR",
    "indore": "IN-MP",
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_refusal_list():
    if yaml is not None and REFUSAL_LIST_PATH.exists():
        try:
            with open(REFUSAL_LIST_PATH, "r", encoding="utf-8") as f:
                doc = yaml.safe_load(f) or {}
            rules = doc.get("rules", {})
            return {k: bool(rules.get(k, True)) for k in RED_LINE_RULES}
        except Exception:
            pass
    return {k: True for k in RED_LINE_RULES}


def infer_sociotechnical_risk_factors(cfg):
    """
    Infers Severity (1-5), Likelihood (1-5), Population (1-5), and Stack Multiplier (1.0-1.5)
    directly from structured sociotechnical disclosures when explicit overrides are absent.
    Calibrated so that inferred values span the full [1..5] scale and never penalize
    developers for municipal grid electricity baselines.
    """
    lc = cfg.get("labor_conditions", {})
    dc = cfg.get("deployment_context", {})
    cc = cfg.get("compute_carbon", {})
    sources = cfg.get("data_sources", [])
    comms = cfg.get("affected_communities", [])
    rlc = cfg.get("red_line_check", {})

    autonomy = dc.get("decision_autonomy_level", "human_in_loop")
    has_unconsented_data = any(s.get("consent_type") in ("none", "unknown") for s in sources)
    all_comms_consented = bool(comms) and all(c.get("consent_obtained", False) for c in comms)
    has_redress = bool(comms) and any(
        bool(c.get("redress_mechanism")) and str(c.get("redress_mechanism")).strip().lower() not in ("none", "")
        for c in comms
    )
    any_red_line = any(bool(rlc.get(k, False)) for k in RED_LINE_RULES)

    # 1. Infer Severity (1..5)
    sev = 1
    if autonomy == "autonomous":
        sev += 2
    elif autonomy == "human_on_loop":
        sev += 1
    if has_unconsented_data or (comms and not all_comms_consented):
        sev += 1
    if (lc.get("psychological_exposure") and not lc.get("opt_out_available")) or any_red_line:
        sev += 1
    inferred_severity = min(5, max(1, sev))

    # 2. Infer Likelihood (1..5)
    if autonomy == "autonomous":
        inferred_likelihood = 5 if (has_unconsented_data or not has_redress) else 4
    elif autonomy == "human_on_loop":
        inferred_likelihood = 3
    else:
        inferred_likelihood = 1 if (all_comms_consented and has_redress and not has_unconsented_data) else 2

    # 3. Infer Population (1..5)
    ub = str(dc.get("user_base_size", "")).strip()
    ub_low = ub.lower()
    if "<100" in ub or "< 100" in ub:
        inferred_population = 1
    elif ">100,000" in ub or "100,000+" in ub or "population" in ub_low or "military" in ub_low:
        inferred_population = 5
    elif "50,000" in ub or "10,000" in ub:
        inferred_population = 4
    elif "5,000" in ub or "1,000" in ub:
        inferred_population = 3
    elif "100" in ub:
        inferred_population = 2
    else:
        inferred_population = 2

    # 4. Infer Stack Multiplier (1.0, 1.25, 1.5) — v1.1 Neutral Grid Calibration
    layers = 0
    reuse_policy = str(cc.get("hardware_reuse_policy", "")).strip().lower()
    unmitigated_compute = cc.get("estimated_co2_kg", 0) > 5000 and reuse_policy in (
        "none",
        "",
        "disposed in combat",
        "military disposal cycle",
        "annual fpga replacement",
        "high-frequency server upgrades",
    )
    if unmitigated_compute:
        layers += 1

    wages_low = str(lc.get("annotation_wages", "")).lower()
    if lc.get("psychological_exposure") or "below" in wages_low or "piece" in wages_low or not lc.get("opt_out_available", True):
        layers += 1

    if has_unconsented_data:
        layers += 1

    if autonomy in ("autonomous", "human_on_loop") and not has_redress:
        layers += 1

    if layers >= 3:
        inferred_stack_mult = 1.5
    elif layers == 2:
        inferred_stack_mult = 1.25
    else:
        inferred_stack_mult = 1.0

    return inferred_severity, inferred_likelihood, inferred_population, inferred_stack_mult


def compute_risk_score(cfg, strict_floor: bool = False):
    """
    Computes the Himsa Risk Score (Harm Penalty) based on severity, likelihood,
    population exposure, and the multi-layer stack multiplier.
    Uses v1.1 neutral grid calibration when inferring from sociotechnical metadata.
    When `strict_floor=True`, takes max(declared, inferred) to prevent self-report gaming.
    """
    inf_sev, inf_lik, inf_pop, inf_mult = infer_sociotechnical_risk_factors(cfg)

    severity = cfg.get("severity") if cfg.get("severity") is not None else inf_sev
    likelihood = cfg.get("likelihood") if cfg.get("likelihood") is not None else inf_lik
    population = cfg.get("population") if cfg.get("population") is not None else inf_pop
    stack_mult = cfg.get("stack_multiplier") if cfg.get("stack_multiplier") is not None else inf_mult

    if strict_floor or bool(cfg.get("enforce_inferred_floor", False)):
        severity = max(int(severity), inf_sev)
        likelihood = max(int(likelihood), inf_lik)
        population = max(int(population), inf_pop)
        stack_mult = max(float(stack_mult), inf_mult)

    raw = float(severity) * float(likelihood) * float(population) * float(stack_mult)
    return round(raw, 2), int(severity), int(likelihood), int(population), float(stack_mult)


def _has_affirmative_commitment(commitment_str: str) -> bool:
    """Returns True only if ahimsa_commitment is a genuine non-empty commitment, not 'None.'."""
    if not isinstance(commitment_str, str):
        return False
    norm = commitment_str.strip().lower()
    if norm in NON_COMMITMENT_STRINGS or norm.startswith("none"):
        return False
    return len(norm) > 0


def compute_flourishing_score(cfg):
    """
    Computes the affirmative Sarvodaya Flourishing Score (0 to 100).
    Evaluates four core pillars:
    1. Labor Dignity & Protection (0-25 pts)
    2. Data Sovereignty & Relational Consent (0-25 pts)
    3. Public Good & Vulnerable Livelihood Uplift (0-25 pts)
    4. Accountability, Redress & Transparency (0-25 pts)
    """
    pts_labor = 0
    lc = cfg.get("labor_conditions", {})
    wages = str(lc.get("annotation_wages", "")).lower()
    has_negative_wage_modifier = any(neg in wages for neg in ("below", "not ", "sub-", "unpaid"))
    if not has_negative_wage_modifier and any(
        w in wages for w in ("above", "living", "fair", "union")
    ):
        pts_labor += 10
    elif not has_negative_wage_modifier and any(w in wages for w in ("market", "standard")):
        pts_labor += 5
    if lc.get("opt_out_available", False):
        pts_labor += 8
    if not lc.get("psychological_exposure", True):
        pts_labor += 7
    pts_labor = min(25, pts_labor)

    pts_data = 0
    sources = cfg.get("data_sources", [])
    fl = cfg.get("flourishing_indicators", {})
    if sources:
        has_benefit_sharing = any(s.get("benefit_sharing") is True for s in sources) or bool(fl.get("benefit_sharing_active"))
        has_community_consent = any(s.get("consent_type") == "community" for s in sources)
        has_individual_consent = any(s.get("consent_type") == "individual" for s in sources)
        no_unconsented = all(s.get("consent_type") not in ("none", "unknown") for s in sources)

        if has_benefit_sharing:
            pts_data += 10
        if has_community_consent:
            pts_data += 10
        elif has_individual_consent:
            pts_data += 6
        if no_unconsented:
            pts_data += 5
    pts_data = min(25, pts_data)

    pts_public_good = 0
    dc = cfg.get("deployment_context", {})
    purpose = str(cfg.get("purpose", "")).lower()
    sector = str(dc.get("sector", "")).lower()

    if fl.get("livelihood_support") or any(k in purpose for k in ["farmer", "health", "education", "triage", "public welfare"]):
        pts_public_good += 10
    if fl.get("public_good_alignment") or "public" in sector or "dpi" in purpose:
        pts_public_good += 8
    if fl.get("open_source_or_access") or fl.get("open_access_or_source"):
        pts_public_good += 7
    pts_public_good = min(25, pts_public_good)

    pts_redress = 0
    comm = cfg.get("affected_communities", [])
    if comm:
        has_redress = any(
            bool(c.get("redress_mechanism"))
            and str(c.get("redress_mechanism")).strip() != "None"
            for c in comm
        ) or bool(fl.get("operational_redress"))
        all_consented = all(c.get("consent_obtained", False) for c in comm)
        if has_redress:
            pts_redress += 12
        if all_consented:
            pts_redress += 8
    if _has_affirmative_commitment(cfg.get("ahimsa_commitment", "")):
        pts_redress += 5
    pts_redress = min(25, pts_redress)

    total_flourishing = pts_labor + pts_data + pts_public_good + pts_redress
    return round(total_flourishing, 1), {
        "labor_dignity": pts_labor,
        "data_sovereignty": pts_data,
        "public_good": pts_public_good,
        "redress_accountability": pts_redress,
    }


def band_for_risk(score):
    for low, high, band, action in RISK_BANDS:
        if low <= score < high:
            return band, action
    return "Critical", "Deployment prohibited; fundamental sociotechnical redesign required"


def band_for_flourishing(score):
    for low, high, band, desc in FLOURISHING_BANDS:
        if low <= score <= high:
            return band, desc
    return "Deficient", "Passive compliance or extractive architecture with negligible community flourishing"


def _slugify_token(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return slug[:40] if slug else "telemetry_stream"


def compile_to_lokahi_manifest(cfg: dict, assessment: dict | None = None, signing_key: bytes = DEFAULT_SIGNING_KEY) -> dict:
    """
    Stage 1 -> Stage 2 Compiler Bridge:
    Compiles an approved or conditional AIA project declaration into a signed
    RFC 8785 Canonical JSON Boundary Manifest for runtime enforcement by LOKAHI v0.1.2.
    Refuses compilation if the project was REFUSED by Stage 1 AIA evaluation.
    """
    if assessment is None:
        assessment = assess(cfg)

    if assessment.get("refused"):
        raise ValueError(
            f"Stage 1->2 Compilation Refused: '{cfg.get('project_name', 'unnamed')}' failed AIA with determination "
            f"'{assessment.get('determination')}'"
        )

    spec = cfg.get("lokahi_manifest_spec", {}) or {}
    dc = cfg.get("deployment_context", {}) or {}
    geos = dc.get("geography", ["IN"])

    # Derive node identifier
    node_id = spec.get("node") or f"node:{_slugify_token(cfg.get('project_name', 'aia_node'))}"

    # Derive statutory jurisdiction & residency from geography
    jurisdiction = spec.get("jurisdiction")
    if not jurisdiction:
        jurisdiction = "IN-DL"
        for g in reversed(geos):
            g_low = str(g).strip().lower()
            if g_low in INDIAN_STATE_ISO:
                jurisdiction = INDIAN_STATE_ISO[g_low]
                break
            if g_low == "india" or "india" in g_low:
                jurisdiction = "IN"

    residency = spec.get("residency")
    if not residency:
        residency = ["IN"] if any("india" in str(g).lower() or str(g).lower() in INDIAN_STATE_ISO for g in geos) else ["GLOBAL"]

    # Derive permitted informational features from data_sources or spec
    informational = spec.get("informational")
    if not informational:
        informational = []
        for ds in cfg.get("data_sources", []):
            if ds.get("consent_type") not in ("none", "unknown"):
                informational.append(_slugify_token(ds.get("source", "consented_telemetry")))
        if not informational:
            informational = ["anonymized_telemetry"]

    # Derive barred optimization targets from red-line invariants + spec
    default_forbidden = [
        "hereditary_caste_proxy",
        "demographic_stratification_proxy",
        "biometric_mass_track",
        "protest_history",
        "residency_status",
        "unconsented_pii_scrape",
    ]
    forbidden_targets = sorted(set(spec.get("forbidden_targets", default_forbidden)))

    risk_band = assessment["risk_evaluation"]["band"]
    exceptions = spec.get("exceptions")
    if not exceptions:
        # High-risk (CONDITIONAL) systems get stricter exception caps and require 3-body ring quorum
        exceptions = (
            {"safety_critical": 1, "window_hours": 24, "requires_disjoint_quorum": 3}
            if risk_band == "High"
            else {"safety_critical": 3, "window_hours": 24}
        )

    expires = spec.get("expires", "2028-03-01T00:00:00Z")
    steward = spec.get("steward", f"did:web:dirgha.example/stewards/{_slugify_token(cfg.get('project_name', 'default'))}")

    manifest_body = {
        "node": node_id,
        "informational": sorted(set(informational)),
        "forbidden_targets": forbidden_targets,
        "jurisdiction": jurisdiction,
        "residency": sorted(set(residency)),
        "exceptions": dict(sorted(exceptions.items())),
        "expires": expires,
        "steward": steward,
    }
    if "physical_envelope" in spec and isinstance(spec["physical_envelope"], dict):
        manifest_body["physical_envelope"] = dict(sorted(spec["physical_envelope"].items()))

    canonical_bytes = json.dumps(manifest_body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    signature = hmac.new(signing_key, canonical_bytes, hashlib.sha256).hexdigest()

    signed_manifest = dict(manifest_body)
    signed_manifest["signature"] = signature
    return signed_manifest


def assess(cfg, strict_floor: bool = False):
    """
    Evaluates project configuration against red-lines, risk penalty,
    and affirmative flourishing.
    """
    refusal_rules = load_refusal_list()
    rlc = cfg.get("red_line_check", {})

    triggered = []
    canonical_triggered = []
    for rule_key in RED_LINE_RULES:
        if rlc.get(rule_key, False) and refusal_rules.get(rule_key, True):
            label = rule_key.replace("_", " ").title()
            if label not in triggered:
                triggered.append(label)
            canon = CANONICAL_RED_LINE_MAP.get(rule_key, rule_key)
            if canon not in canonical_triggered:
                canonical_triggered.append(canon)

    risk_score, severity, likelihood, population, stack_mult = compute_risk_score(cfg, strict_floor=strict_floor)
    inf_sev, inf_lik, inf_pop, inf_mult = infer_sociotechnical_risk_factors(cfg)
    underestimation_warnings = []
    if severity < inf_sev:
        underestimation_warnings.append(f"declared_severity({severity})<inferred({inf_sev})")
    if likelihood < inf_lik:
        underestimation_warnings.append(f"declared_likelihood({likelihood})<inferred({inf_lik})")
    if population < inf_pop:
        underestimation_warnings.append(f"declared_population({population})<inferred({inf_pop})")
    if stack_mult < inf_mult:
        underestimation_warnings.append(f"declared_stack_multiplier({stack_mult})<inferred({inf_mult})")
    risk_band, action = band_for_risk(risk_score)

    flourishing_score, flourishing_breakdown = compute_flourishing_score(cfg)
    flourishing_band, flourishing_desc = band_for_flourishing(flourishing_score)

    refused = len(triggered) > 0 or risk_band == "Critical"

    if len(triggered) > 0:
        determination = "REFUSED (Categorical Red-Line Prohibition)"
    elif risk_band == "Critical":
        determination = "REFUSED (Unacceptable Full-Stack Risk)"
    elif risk_band in ("Low", "Medium") and flourishing_band in ("Exemplary", "Substantive"):
        determination = "APPROVED (Ahimsa Certified)"
    elif risk_band == "High":
        determination = "CONDITIONAL (Mandatory External Audit & Oversight)"
    else:
        determination = "PROVISIONAL (Low Risk but Low Affirmative Flourishing)"

    return {
        "project_name": cfg.get("project_name", "unnamed"),
        "version": cfg.get("version", "1.0"),
        "aia_engine_version": __version__,
        "refused": refused,
        "determination": determination,
        "lokahi_stage2_routing": (
            "BLOCKED_AT_COMPILE_TIME"
            if refused
            else ("DISJOINT_3_BODY_RING_REQUIRED" if risk_band == "High" else "FAST_PATH_ELIGIBLE")
        ),
        "red_line_triggered": triggered,
        "red_line_canonical": canonical_triggered,
        "risk_evaluation": {
            "score": risk_score,
            "band": risk_band,
            "action": action,
            "severity_score": severity,
            "severity_desc": SEVERITY_DESC.get(severity, "Unknown"),
            "likelihood_score": likelihood,
            "likelihood_desc": LIKELIHOOD_DESC.get(likelihood, "Unknown"),
            "population_score": population,
            "population_desc": POPULATION_DESC.get(population, "Unknown"),
            "stack_multiplier": stack_mult,
            "self_report_underestimation_warnings": underestimation_warnings,
        },
        "flourishing_evaluation": {
            "score": flourishing_score,
            "band": flourishing_band,
            "description": flourishing_desc,
            "pillar_breakdown": flourishing_breakdown,
        },
    }


# Backwards compatibility wrappers
def compute_score(cfg):
    score, _, _, _, _ = compute_risk_score(cfg)
    return score


def band_for_score(score):
    return band_for_risk(score)


def main():
    parser = argparse.ArgumentParser(description="Ahimsa Impact Assessment (AIA v1.1) Dual-Axis Scorer & LOKAHI Compiler")
    parser.add_argument("--config", required=True, help="Path to project config JSON conforming to ahimsa-schema.json")
    parser.add_argument("--output", help="Optional path to export assessment report JSON")
    parser.add_argument("--compile-manifest", help="Optional path to export compiled RFC 8785 LOKAHI Boundary Manifest JSON")
    parser.add_argument("--strict-floor", action="store_true", help="Enforce max(declared, inferred) sociotechnical risk floor")
    args = parser.parse_args()

    cfg = load_json(args.config)
    result = assess(cfg, strict_floor=args.strict_floor)

    print("=" * 72)
    print(" AHIMSA IMPACT ASSESSMENT (AIA v1.1) — SOCIO-TECHNICAL REPORT")
    print("=" * 72)
    print(f"Project Name:           {result['project_name']} (v{result['version']})")
    print(f"Final Determination:    {result['determination']}")
    print(f"Stage 2 LOKAHI Routing: {result['lokahi_stage2_routing']}")
    print(f"Red-Line Refusals:      {', '.join(result['red_line_triggered']) if result['red_line_triggered'] else 'None'}")
    print("-" * 72)
    print(f"HIMSA RISK PENALTY:     {result['risk_evaluation']['score']} / 187.5 [{result['risk_evaluation']['band']}]")
    print(f"Action Required:        {result['risk_evaluation']['action']}")
    print(f"Full-Stack Multiplier:  {result['risk_evaluation']['stack_multiplier']}x")
    print("-" * 72)
    print(f"SARVODAYA FLOURISHING:  {result['flourishing_evaluation']['score']} / 100.0 [{result['flourishing_evaluation']['band']}]")
    fb = result["flourishing_evaluation"]["pillar_breakdown"]
    print(f"  - Labor Dignity:      {fb['labor_dignity']} / 25")
    print(f"  - Data Sovereignty:   {fb['data_sovereignty']} / 25")
    print(f"  - Public Good Uplift: {fb['public_good']} / 25")
    print(f"  - Redress & Oversight:{fb['redress_accountability']} / 25")
    print("=" * 72)

    if args.output:
        report = {"declaration": cfg, "assessment": result}
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Full assessment exported to: {args.output}")

    if args.compile_manifest:
        if result["refused"]:
            print(f"Refusing to compile LOKAHI manifest: project is {result['determination']}")
        else:
            manifest = compile_to_lokahi_manifest(cfg, result)
            with open(args.compile_manifest, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2, ensure_ascii=False)
            print(f"Signed RFC 8785 LOKAHI Boundary Manifest compiled to: {args.compile_manifest}")

    sys.exit(1 if result["refused"] else 0)


if __name__ == "__main__":
    main()
