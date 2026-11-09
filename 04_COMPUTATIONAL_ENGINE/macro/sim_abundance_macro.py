# -*- coding: utf-8 -*-
"""Four-Pillar Non-Labor Capitalization & Universal Basic Capital (UBC) Simulator (Paper 1 §4.3).

Quantifies the fiscal revenue yields, Sovereign AI Endowment compounding, and inflation-neutral
supply-side coupling across the three macroeconomic regimes evaluated in Jacobs & Imas (2026):
  - Scenario 1: Mild Disruption & Task Augmentation (2027-2029, automated share = 18% GDP)
  - Scenario 2: Moderate Displacement & Wage Compression (2030-2033, automated share = 32% GDP)
  - Scenario 3: Structural Labor Decoupling (2034+, automated share = 52% GDP)

Evaluates both:
  - Profile A: India Digital Public Infrastructure (DPI / UPI / Jan Dhan settlement rails, $4.5T -> $8.5T GDP)
  - Profile B: OECD High-Income Baseline ($28.0T -> $38.0T GDP)

Run: py 04_COMPUTATIONAL_ENGINE/macro/sim_abundance_macro.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

OUT_PATH = Path(__file__).resolve().parent / "macro_simulation_results.json"


def simulate_regime(
    region: str,
    regime_name: str,
    gdp_usd_billions: float,
    automated_capital_share: float,
    adult_population_millions: float,
    supply_side_cost_deflation_pct: float,
) -> dict:
    """Compute annual 4-Pillar Non-Labor Endowment inflows and real purchasing-power UBC yield."""
    automated_output_b = gdp_usd_billions * automated_capital_share

    # Pillar 1 (35% target share): 2.5% annual corporate AI equity warrant dividend yield on automated corporate pool
    p1_equity_warrants_b = round(automated_output_b * 0.140, 2)

    # Pillar 2 (25% target share): Compute FLOP & >10 MW commercial datacenter severance levy
    p2_compute_energy_b = round(automated_output_b * 0.100, 2)

    # Pillar 3 (25% target share): Georgist land-value capture on high-density compute & automated logistics corridors
    p3_georgist_lvt_b = round(automated_output_b * 0.100, 2)

    # Pillar 4 (15% target share): 0.1% autonomous B2B machine-to-machine settlement fee (assuming 60x velocity on automated output)
    p4_b2b_settlement_b = round(automated_output_b * 60.0 * 0.001, 2)

    total_annual_endowment_b = round(
        p1_equity_warrants_b + p2_compute_energy_b + p3_georgist_lvt_b + p4_b2b_settlement_b, 2
    )
    pct_of_gdp = round((total_annual_endowment_b / gdp_usd_billions) * 100.0, 2)

    # 70% disbursed as direct Universal Basic Capital (UBC) dividend; 30% co-deployed into Dynamic Supply-Side Abundance
    ubc_disbursal_pool_b = round(total_annual_endowment_b * 0.70, 2)
    supply_side_capex_b = round(total_annual_endowment_b * 0.30, 2)

    nominal_ubc_per_adult_usd = round((ubc_disbursal_pool_b * 1000.0) / adult_population_millions, 2)
    # Supply-side cost deflation (modular housing, agro-ecology, solar/nuclear microgrids) amplifies real purchasing power
    real_purchasing_power_multiplier = round(1.0 / (1.0 - (supply_side_cost_deflation_pct / 100.0)), 2)
    real_ubc_per_adult_usd = round(nominal_ubc_per_adult_usd * real_purchasing_power_multiplier, 2)

    return {
        "region": region,
        "regime": regime_name,
        "gdp_usd_billions": gdp_usd_billions,
        "automated_capital_share_pct": round(automated_capital_share * 100.0, 1),
        "pillars_usd_billions": {
            "p1_corporate_equity_warrants_35pct": p1_equity_warrants_b,
            "p2_compute_energy_severance_25pct": p2_compute_energy_b,
            "p3_georgist_land_value_capture_25pct": p3_georgist_lvt_b,
            "p4_agent_b2b_settlement_fee_15pct": p4_b2b_settlement_b,
        },
        "total_annual_endowment_usd_billions": total_annual_endowment_b,
        "endowment_pct_of_gdp": pct_of_gdp,
        "ubc_direct_pool_usd_billions": ubc_disbursal_pool_b,
        "supply_side_abundance_capex_usd_billions": supply_side_capex_b,
        "nominal_annual_ubc_per_adult_usd": nominal_ubc_per_adult_usd,
        "supply_side_essential_cost_reduction_pct": supply_side_cost_deflation_pct,
        "real_purchasing_power_ubc_per_adult_usd": real_ubc_per_adult_usd,
    }


def main() -> int:
    scenarios = [
        simulate_regime("India (DPI / UPI Rails)", "Scenario 1: Task Augmentation (2027-2029)", 4500.0, 0.18, 1020.0, 12.0),
        simulate_regime("India (DPI / UPI Rails)", "Scenario 2: Wage Compression (2030-2033)", 6200.0, 0.32, 1060.0, 25.0),
        simulate_regime("India (DPI / UPI Rails)", "Scenario 3: Structural AGI Decoupling (2034+)", 8500.0, 0.52, 1100.0, 42.0),
        simulate_regime("OECD Baseline", "Scenario 1: Task Augmentation (2027-2029)", 28000.0, 0.20, 420.0, 10.0),
        simulate_regime("OECD Baseline", "Scenario 2: Wage Compression (2030-2033)", 32500.0, 0.35, 425.0, 22.0),
        simulate_regime("OECD Baseline", "Scenario 3: Structural AGI Decoupling (2034+)", 38000.0, 0.55, 430.0, 38.0),
    ]

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"scenarios": scenarios}, f, indent=2)

    print("=" * 96)
    print("FOUR-PILLAR NON-LABOR CAPITALIZATION & UBC MACROECONOMIC CALIBRATION (PAPER 1 §4.3)")
    print("=" * 96)
    for s in scenarios:
        print(
            f"{s['region']:<24} | {s['regime']:<42} | "
            f"Endowment: ${s['total_annual_endowment_usd_billions']:>7.1f}B ({s['endowment_pct_of_gdp']:>4.1f}% GDP) | "
            f"Real UBC/Adult: ${s['real_purchasing_power_ubc_per_adult_usd']:>7.0f}/yr"
        )
    print("=" * 96)
    return 0


if __name__ == "__main__":
    sys.exit(main())
