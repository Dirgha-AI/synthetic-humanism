"""
AIA v1.1 Benchmark Runner, Statistical Profiler & Stage 1->2 Manifest Compiler Check

Executes the Ahimsa Impact Assessment scorer across all systems in benchmark_50.jsonl,
computes empirical score distributions across all four risk bands (Low, Medium, High, Critical)
and three flourishing bands (Exemplary, Substantive, Deficient), verifies red-line detection
and Stage 1->2 LOKAHI manifest compilation, and outputs benchmark_results.json.
"""

import json
import random
import sys
from pathlib import Path

# Add scorer to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scorer"))
from scorer import assess, band_for_risk, compile_to_lokahi_manifest

BENCHMARK_PATH = Path(__file__).parent / "benchmark_50.jsonl"
REPORT_OUTPUT_PATH = Path(__file__).parent / "benchmark_results.json"


def _spearman_rho(xs: list[float], ys: list[float]) -> float:
    """Compute Spearman's rank correlation coefficient rho with zero external dependencies."""
    n = len(xs)
    if n <= 1:
        return 1.0

    def _ranks(vals: list[float]) -> list[float]:
        indexed = sorted(enumerate(vals), key=lambda t: t[1])
        ranks = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and indexed[j + 1][1] == indexed[i][1]:
                j += 1
            avg_rank = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                ranks[indexed[k][0]] = avg_rank
            i = j + 1
        return ranks

    rx = _ranks(xs)
    ry = _ranks(ys)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den_x = sum((a - mx) ** 2 for a in rx) ** 0.5
    den_y = sum((b - my) ** 2 for b in ry) ** 0.5
    if den_x == 0 or den_y == 0:
        return 1.0
    return num / (den_x * den_y)


def run_monte_carlo_sensitivity(results: list[dict], trials: int = 1000, noise_bound: float = 0.25) -> dict:
    """Run a 1,000-trial Monte Carlo weight perturbation sensitivity analysis (+/-25%)
    across all 50 systems to test rank-order stability (Spearman's rho) and refusal/band invariance."""
    rng = random.Random(20261109)
    base_risk = [r["risk_evaluation"]["score"] for r in results]
    base_fl = [r["flourishing_evaluation"]["score"] for r in results]
    base_refused = [bool(r["refused"]) for r in results]

    risk_rhos = []
    fl_rhos = []
    refusal_agreements = []

    for _ in range(trials):
        # Perturb the 4 Sarvodaya pillar weights by +/-25% and normalize to sum to 4.0
        w_pillars = [rng.uniform(1.0 - noise_bound, 1.0 + noise_bound) for _ in range(4)]
        w_sum = sum(w_pillars)
        w_norm = [w * 4.0 / w_sum for w in w_pillars]

        # Perturb Himsa exponent / stack sensitivity by +/-15%
        e_sev = rng.uniform(0.90, 1.10)
        e_lik = rng.uniform(0.90, 1.10)
        e_pop = rng.uniform(0.90, 1.10)
        m_scale = rng.uniform(1.0 - noise_bound * 0.5, 1.0 + noise_bound * 0.5)

        pert_risk = []
        pert_fl = []
        agree_count = 0

        for idx, r in enumerate(results):
            reval = r["risk_evaluation"]
            feval = r["flourishing_evaluation"]["pillar_breakdown"]

            pr = (
                (reval["severity_score"] ** e_sev)
                * (reval["likelihood_score"] ** e_lik)
                * (reval["population_score"] ** e_pop)
                * (1.0 + (reval["stack_multiplier"] - 1.0) * m_scale)
            )
            pf = (
                feval["labor_dignity"] * w_norm[0]
                + feval["data_sovereignty"] * w_norm[1]
                + feval["public_good"] * w_norm[2]
                + feval["redress_accountability"] * w_norm[3]
            )
            pert_risk.append(pr)
            pert_fl.append(pf)

            p_band, _ = band_for_risk(pr)
            p_refused = (len(r["red_line_triggered"]) > 0) or (p_band == "Critical")
            if p_refused == base_refused[idx]:
                agree_count += 1

        risk_rhos.append(_spearman_rho(base_risk, pert_risk))
        fl_rhos.append(_spearman_rho(base_fl, pert_fl))
        refusal_agreements.append(agree_count / len(results))

    return {
        "trials": trials,
        "perturbation_bound": f"+/-{int(noise_bound * 100)}%",
        "mean_risk_spearman_rho": round(sum(risk_rhos) / len(risk_rhos), 4),
        "min_risk_spearman_rho": round(min(risk_rhos), 4),
        "mean_flourishing_spearman_rho": round(sum(fl_rhos) / len(fl_rhos), 4),
        "min_flourishing_spearman_rho": round(min(fl_rhos), 4),
        "mean_refusal_invariance_rate": round((sum(refusal_agreements) / len(refusal_agreements)) * 100.0, 2),
    }


def main():
    if not BENCHMARK_PATH.exists():
        print(f"Error: {BENCHMARK_PATH} not found.")
        sys.exit(1)

    systems = []
    with open(BENCHMARK_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                systems.append(json.loads(line))

    print(f"Loaded {len(systems)} systems from {BENCHMARK_PATH.name}")

    results = []
    risk_scores = []
    flourishing_scores = []
    risk_bands = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}
    flourishing_bands = {"Exemplary": 0, "Substantive": 0, "Deficient": 0}
    refusal_counts = {
        "total_refused": 0,
        "red_line_refused": 0,
        "critical_risk_refused": 0,
        "conditional_lokahi_ring_routed": 0,
    }
    sector_summary = {}
    compiled_manifests_count = 0

    for s in systems:
        res = assess(s)
        results.append(res)

        r_eval = res["risk_evaluation"]
        f_eval = res["flourishing_evaluation"]

        risk_scores.append(r_eval["score"])
        flourishing_scores.append(f_eval["score"])

        risk_bands[r_eval["band"]] += 1
        flourishing_bands[f_eval["band"]] += 1

        if res["refused"]:
            refusal_counts["total_refused"] += 1
            if len(res["red_line_triggered"]) > 0:
                refusal_counts["red_line_refused"] += 1
            elif r_eval["band"] == "Critical":
                refusal_counts["critical_risk_refused"] += 1
        else:
            manifest = compile_to_lokahi_manifest(s, res)
            if manifest and manifest.get("signature"):
                compiled_manifests_count += 1
            if r_eval["band"] == "High":
                refusal_counts["conditional_lokahi_ring_routed"] += 1

        sec = s.get("deployment_context", {}).get("sector", "unknown")
        if sec not in sector_summary:
            sector_summary[sec] = {
                "total": 0,
                "refused": 0,
                "conditional_high_risk": 0,
                "mean_risk": 0.0,
                "mean_flourishing": 0.0,
            }
        sec_d = sector_summary[sec]
        sec_d["total"] += 1
        if res["refused"]:
            sec_d["refused"] += 1
        elif r_eval["band"] == "High":
            sec_d["conditional_high_risk"] += 1
        sec_d["mean_risk"] += r_eval["score"]
        sec_d["mean_flourishing"] += f_eval["score"]

    for sec, d in sector_summary.items():
        d["mean_risk"] = round(d["mean_risk"] / d["total"], 2)
        d["mean_flourishing"] = round(d["mean_flourishing"] / d["total"], 2)

    mean_risk = round(sum(risk_scores) / len(risk_scores), 2)
    mean_flourishing = round(sum(flourishing_scores) / len(flourishing_scores), 2)
    mc_sensitivity = run_monte_carlo_sensitivity(results, trials=1000, noise_bound=0.25)

    summary = {
        "total_systems_evaluated": len(systems),
        "compiled_lokahi_manifests": compiled_manifests_count,
        "overall_metrics": {
            "mean_himsa_risk_score": mean_risk,
            "min_himsa_risk_score": min(risk_scores),
            "max_himsa_risk_score": max(risk_scores),
            "mean_sarvodaya_flourishing_score": mean_flourishing,
            "min_sarvodaya_flourishing_score": min(flourishing_scores),
            "max_sarvodaya_flourishing_score": max(flourishing_scores),
        },
        "risk_band_distribution": risk_bands,
        "flourishing_band_distribution": flourishing_bands,
        "refusals": refusal_counts,
        "monte_carlo_sensitivity": mc_sensitivity,
        "sector_breakdown": sector_summary,
    }

    print("\n" + "=" * 68)
    print(" AIA v1.1 BENCHMARK (N=50) IN-SILICO EVALUATION SUMMARY")
    print("=" * 68)
    print(f"Systems Evaluated:               {len(systems)}")
    print(f"Mean Himsa Risk Penalty:        {mean_risk} / 187.5")
    print(f"Mean Sarvodaya Flourishing:     {mean_flourishing} / 100.0")
    print(f"Total Systems Refused:          {refusal_counts['total_refused']} ({round(refusal_counts['total_refused']/len(systems)*100, 1)}%)")
    print(f"  - Red-Line Vetoes:            {refusal_counts['red_line_refused']}")
    print(f"  - Critical Risk Exclusively:  {refusal_counts['critical_risk_refused']}")
    print(f"Conditional (3-Body Ring Routed): {refusal_counts['conditional_lokahi_ring_routed']}")
    print(f"Compiled LOKAHI Manifests:      {compiled_manifests_count} / {len(systems) - refusal_counts['total_refused']}")
    print("-" * 68)
    print("Risk Band Breakdown:")
    for b, c in risk_bands.items():
        print(f"  - {b:10s}: {c:2d} ({round(c/len(systems)*100, 1)}%)")
    print("-" * 68)
    print("Flourishing Band Breakdown:")
    for b, c in flourishing_bands.items():
        print(f"  - {b:12s}: {c:2d} ({round(c/len(systems)*100, 1)}%)")
    print("-" * 68)
    print("Sector Performance:")
    for sec, d in sector_summary.items():
        print(
            f"  - {sec.title():22s} [N={d['total']}]: Refused={d['refused']}, "
            f"Conditional={d['conditional_high_risk']}, Risk={d['mean_risk']}, Flourishing={d['mean_flourishing']}"
        )
    print("-" * 68)
    print("Monte Carlo Weight Perturbation Sensitivity (1,000 Trials, +/-25%):")
    print(f"  - Himsa Risk Rank Stability (Spearman rho):     {mc_sensitivity['mean_risk_spearman_rho']} (min={mc_sensitivity['min_risk_spearman_rho']})")
    print(f"  - Sarvodaya Rank Stability (Spearman rho):      {mc_sensitivity['mean_flourishing_spearman_rho']} (min={mc_sensitivity['min_flourishing_spearman_rho']})")
    print(f"  - Refusal Determination Invariance Rate:        {mc_sensitivity['mean_refusal_invariance_rate']}%")
    print("=" * 68)

    with open(REPORT_OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "evaluations": results}, f, indent=2, ensure_ascii=False)
    print(f"\nDetailed evaluation results exported to {REPORT_OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()
