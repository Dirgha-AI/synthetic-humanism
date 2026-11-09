# Ahimsa-by-Design: Dual-Axis Evaluation of Non-Extraction and Affirmative Flourishing in AI Systems

**Salik Shah**  
Founder & Lead Systems Architect, Dirgha AI · Founding Editor, *Mithila Review*  
New Delhi, India · salikshah.com · salik.shah@gmail.com

**Target Venues:** ACM Conference on Fairness, Accountability, and Transparency (ACM FAccT 2027) · AAAI/ACM Conference on AI, Ethics, and Society (AIES 2027)  
**Open-Source Implementation & Benchmark:** `github.com/Dirgha-AI/ahimsa-ai` (MIT License · `scorer.py`, `ahimsa-schema.json`, `validate_schema.py`, `benchmark_50.jsonl`)

---

## Abstract

When MD Anderson Cancer Center halted its $62 million oncology AI deployment after five years, post-mortem audits revealed that the system had never been evaluated against the messy, unstructured clinical notes and workflow dependencies of real hospital wards. Across the global AI ecosystem, prevailing algorithmic impact assessments (AIAs) evaluate systems along a single negative axis: minimizing localized classifier disparity or checking off statutory compliance boxes. This harm-avoidant, model-centric baseline suffers from three structural blind spots: (1) it leaves unmeasured what a system must *affirmatively* contribute to human flourishing; (2) it evaluates inference outputs in isolation from the upstream and downstream sociotechnical stack (data provenance, contributor reciprocity, and hardware lifecycle efficiency); and (3) it ends in a static PDF report with no deterministic compiler into runtime boundary enforcement.

Grounded in Synthetic Humanism (Shah, 2026a), this paper introduces **Ahimsa-by-Design** and its open-source computational engine, the **Ahimsa Impact Assessment (`AIA v1.1`)**. The AIA evaluates systems across two orthogonal, non-compensatory axes: the **Himsa Risk Penalty** ($R_{\text{Himsa}} \in [0, 187.5]$, measuring compounding lifecycle risk with neutral thermodynamic calibration) and the **Sarvodaya Flourishing Index** ($F_{\text{Sarvodaya}} \in [0, 100]$, measuring contributor dignity, data reciprocity, public-good uplift, and operational redress), bounded by five categorical red lines. Evaluated across a recursively schema-validated benchmark of 50 AI systems spanning five critical sectors (`benchmark_results.json`), `AIA v1.1` refuses 14 systems (28.0%: 9 categorical red-line vetoes and 5 critical-risk exclusions), routes 5 intermediate dual-use systems into `CONDITIONAL` 3-body oversight rings, and compiles all 36 approved or conditional declarations directly into signed RFC 8785 Boundary Manifests for runtime enforcement by the LOKAHI Protocol. Finally, we specify a pre-registered Phase 2 multi-rater field validation study ($K = 5$ evaluators across $N = 15$ live deployments) targeting Fleiss' $\kappa \ge 0.70$ and Krippendorff's $\alpha \ge 0.75$.

**Keywords:** Ahimsa-by-Design, Ahimsa Impact Assessment (AIA), Synthetic Humanism, Dual-Axis Evaluation, Sarvodaya, Aparigraha, Algorithmic Auditing, Digital Public Infrastructure

---

## 1. Introduction: Moving Beyond Single-Axis Negative Compliance

Over the past decade, more than eighty institutional AI ethics charters have converged on five principles: transparency, fairness, non-maleficence, responsibility, and privacy (Jobin et al., 2019; Floridi et al., 2018). To put these principles into practice, researchers and regulators introduced Algorithmic Impact Assessments (AIAs), Model Cards (Mitchell et al., 2019), and Datasheets for Datasets (Gebru et al., 2021).

Empirical studies of deployed impact assessments, however, expose three persistent failure modes (Johnson & Heidari, 2023; Veale et al., 2018; Raji et al., 2020):
1. **The Negative Baseline Problem:** Conventional assessments define ethical alignment as the absence of acute statistical bias or privacy leakage. A purely negative metric cannot distinguish between a speculative high-frequency trading bot that avoids demographic bias while contributing zero social value ($F = 0$) and a community tuberculosis screener that saves lives across informal settlements ($F = 90$).
2. **Lifecycle Fragmentation:** Model-centric audits inspect input-output behavior at inference time while ignoring whether training datasets respect community consent and benefit-sharing (Gabriel & Kasirzadeh, 2026), whether data contributors have fair wages and penalty-free opt-out rights, and whether affected citizens have access to rapid human appeal channels.
3. **The Compile-Time to Runtime Disconnect:** Pre-deployment questionnaires typically produce a static document filed in a compliance archive, leaving live agent execution unguarded against runtime boundary violations, jurisdiction drift, or fail-open timeouts (Aggarwal et al., `arXiv:2602.17357`, 2026).

To close all three gaps, we formulate **Ahimsa-by-Design**: a constructive engineering methodology grounded in classical Indic philosophy and B.R. Ambedkar's constitutional theory (Ambedkar, 1936). Rather than collapsing harm and benefit into a single scalar number where charitable claims can offset structural harm, we formalize non-harm (*ahimsa*) and shared abundance (*sarvodaya*) as two independent, machine-checkable axes in `AIA v1.1`.

---

## 2. Theoretical Foundation: Five Classical Concepts as Engineering Constraints

In classical Jain, Buddhist, and Indian constitutional thought, *ahimsa* is an active duty of care oriented toward universal uplift. We translate five classical concepts into concrete schema primitives in `ahimsa-schema.json`:

| Classical Concept | Philosophical Meaning | Sociotechnical Engineering Specification | AIA v1.1 Schema & Scorer Primitive |
| :--- | :--- | :--- | :--- |
| **1. Ahimsa** | Active non-injury; prevention of avoidable harm | Bounding physical, economic, and civic harm across the full system lifecycle | $R_{\text{Himsa}}$ (`severity`, `likelihood`, `population`, `stack_multiplier`) & `red_line_check` |
| **2. Satya** | Truthfulness; epistemic fidelity | Complete, machine-validated disclosure of provenance and uncertainty bounds | Recursive JSON Schema validation (`validate_schema.py`) & uncertainty telemetry |
| **3. Aparigraha** | Non-extraction; reciprocal exchange | Prohibiting unconsented data appropriation; ensuring fair contributor compensation and benefit-sharing | `data_sources[].benefit_sharing` and `labor_conditions` pillars |
| **4. Swaraj** | Self-governance; institutional autonomy | Preserving local community consent, data stewardship, and timely human grievance redress | `affected_communities[].consent_obtained` and `redress_mechanism` |
| **5. Sarvodaya** | Universal uplift; shared abundance | Orienting optimization toward public goods, Universal Basic Services (Cave, 2026), and livelihood resilience | $F_{\text{Sarvodaya}}$ ($P_{\text{Labor}} + P_{\text{Data}} + P_{\text{PublicGood}} + P_{\text{Redress}}$) |

As B.R. Ambedkar demonstrated in his constitutional scholarship (Ambedkar, 1936), normative vows endure only when backed by codified institutional rules and enforceable remedies. `AIA v1.1` encodes this requirement through non-compensatory bounds: a high score on affirmative flourishing ($F_{\text{Sarvodaya}} = 100$) can never override a categorical red-line trigger or a critical lifecycle risk score ($R_{\text{Himsa}} \ge 60$).

---

## 3. Computational Architecture of the Ahimsa Impact Assessment (`AIA v1.1`)

### 3.1 Axis 1: The Himsa Risk Penalty ($R_{\text{Himsa}} \in [0, 187.5]$)

The risk vector quantifies potential negative externalities across the sociotechnical stack:

$$R_{\text{Himsa}} = S \times L \times P \times M_{\text{stack}}$$

- **Severity ($S \in \{1..5\}$):** Magnitude of potential harm if realized, from $1$ (negligible temporary friction) and $3$ (moderate socio-economic disruption reversible with intervention) to $5$ (catastrophic physical injury, loss of life, or systemic deprivation of fundamental rights).
- **Likelihood ($L \in \{1..5\}$):** Lifecycle probability, from $1$ ($<10\%$) to $5$ ($>75\%$ without active safeguards).
- **Population Exposure ($P \in \{1..5\}$):** Affected scale, from $1$ ($<100$ individuals) and $3$ ($1,000\text{--}10,000$) to $5$ ($>100,000$).
- **Lifecycle Compounding Multiplier ($M_{\text{stack}} \in \{1.0, 1.25, 1.5\}$):** Captures whether unmitigated risks span one ($1.0\times$), two ($1.25\times$), or three or more ($1.5\times$) lifecycle layers (unconsented data provenance, inadequate contributor protections, absence of hardware reuse policies on high-compute workloads, and unverified autonomous execution). In `v1.1`, $M_{\text{stack}}$ evaluates positive hardware reuse and efficiency disclosures rather than penalizing developers in industrializing regions for municipal grid electricity baselines.

Risk scores map to four bands: **Low** ($R < 10$), **Medium** ($10 \le R < 30$), **High** ($30 \le R < 60$, requiring independent oversight and runtime 3-body LOKAHI consent rings), and **Critical** ($R \ge 60$, deployment prohibited).

### 3.2 Axis 2: The Sarvodaya Flourishing Index ($F_{\text{Sarvodaya}} \in [0, 100]$)

To reward constructive public-good creation alongside harm prevention, the second vector scores four 25-point pillars:

$$F_{\text{Sarvodaya}} = P_{\text{Labor}} + P_{\text{Data}} + P_{\text{PublicGood}} + P_{\text{Redress}}$$

1. **Contributor Dignity & Occupational Well-Being ($P_{\text{Labor}}$, 0–25 pts):** Living wages $\ge 20\%$ above local statutory minimums (10 pts; negative modifiers such as `"below"` receive 0 pts), penalty-free opt-out rights (8 pts), and protection from unmitigated psychological distress (7 pts).
2. **Data Provenance & Reciprocal Benefit-Sharing ($P_{\text{Data}}$, 0–25 pts):** Measurable benefit-sharing with data originators (10 pts), collective community consent (10 pts) or individual consent (6 pts), and absence of unconsented scraping (5 pts).
3. **Public-Good Alignment & Livelihood Resilience ($P_{\text{PublicGood}}$, 0–25 pts):** Strengthening vulnerable livelihoods (10 pts), alignment with open Digital Public Infrastructure (8 pts), and open-source or open-access availability (7 pts).
4. **Accountability & Operational Redress ($P_{\text{Redress}}$, 0–25 pts):** Accessible human grievance redress (12 pts), community consent verification (8 pts), and genuine affirmative stewardship commitments (5 pts; placeholder strings such as `"None."` receive 0 pts).

### 3.3 Five Categorical Red Lines and Stage 1 $\to$ Stage 2 Manifest Compilation

Any triggered red line forces immediate refusal (`REFUSED: Categorical Red-Line Prohibition`) regardless of numeric score:
1. `autonomous_weapons`: Delegation of offensive lethal target selection and engagement against human beings without meaningful human control.
2. `mass_biometric_surveillance`: Warrantless population-scale biometric tracking in public spaces.
3. `demographic_or_hereditary_stratification` (generalizing `algorithmic_caste_scoring`): Automated stratification or denial of credit, employment, housing, or civic services based on hereditary status, caste, race, religion, or demographic proxies.
4. `unsanctioned_kinetic_or_coercive_transfer` (generalizing `atrocity_regime_export`): Transfer of kinetic or coercive surveillance capabilities in violation of international humanitarian law.
5. `non_consensual_data_extraction`: Systematic appropriation of vulnerable or indigenous community knowledge without collective consent and benefit-sharing.

When a declaration achieves `APPROVED (Ahimsa Certified)`, `CONDITIONAL (Mandatory External Oversight)`, or `PROVISIONAL` status, `compile_to_lokahi_manifest()` (`scorer.py --compile-manifest`) compiles its schema disclosures into a signed RFC 8785 Canonical JSON Boundary Manifest for runtime enforcement by the LOKAHI Protocol (`v0.1.2`). `CONDITIONAL` systems ($30 \le R < 60$) are automatically tagged with stricter emergency caps (`safety_critical: 1`) and `DISJOINT_3_BODY_RING_REQUIRED`.

---

## 4. In-Silico Benchmark Evaluation Across 50 AI Systems ($N = 50$)

Executing `py 04_COMPUTATIONAL_ENGINE/benchmark/run_benchmark.py` and `validate_schema.py` across all 50 benchmark systems (`N = 10` per sector) yields:

| Sector ($N = 10$ each) | Certified / Provisional | Conditional Ring ($High$) | Refused ($N$ & %) | Mean $R_{\text{Himsa}}$ ($/187.5$) | Mean $F_{\text{Sarvodaya}}$ ($/100$) | Representative Approved, Conditional & Refused Systems |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Agriculture** | 7 (7 Certified) | 1 (`#4` Drone Fleet, $R=33.75$) | 2 (20.0%) | 22.95 | 74.30 | Certified: *Jharkhand Seed Bank* ($R=3.0, F=100$). Refused: *APMC Mandi Arbitrage* ($R=80.0$), *Crop Loss Denier* ($R=67.5$). |
| **Finance & Credit** | 5 (5 Certified) | 1 (`#12` UPI Sentinel, $R=37.50$) | 4 (40.0%) | 54.95 | 58.80 | Certified: *Andhra SHG Trust* ($R=4.0, F=100$). Refused: *Hereditary Credit Scorer* ($R=187.5, F=0$), *Biometric Teller Gate* ($R=45.0$, Red-Line Veto). |
| **Healthcare** | 8 (8 Certified) | 1 (`#27` ICU Sepsis, $R=36.00$) | 1 (10.0%) | 17.40 | 78.00 | Certified: *Dharavi TB Screener* ($R=4.0, F=90$). Refused: *Unsupervised Psychiatric Chatbot* ($R=96.0, F=0$, Red-Line Veto). |
| **Defense & Security** | 4 (4 Certified) | 1 (`#37` Grid SCADA, $R=30.00$) | 5 (50.0%) | 79.10 | 47.80 | Certified: *Landmine Pathfinder* ($R=3.0, F=100$). Refused: *Anti-Personnel Trench Swarm* ($R=56.25$, Red-Line Veto), *Perimeter Swarm* ($R=187.5, F=0$). |
| **Public Admin** | 7 (7 Certified) | 1 (`#46` Bail Scheduler, $R=30.00$) | 2 (20.0%) | 33.02 | 78.00 | Certified: *Bhashini Voice DPI* ($R=5.0, F=100$). Refused: *PDS Ration Exclusion* ($R=100.0$), *Biometric Pension Delister* ($R=156.25$). |
| **OVERALL TOTAL** | **31 (62.0%)** | **5 (10.0%)** | **14 (28.0%)** | **41.48** | **67.38** | **9 Red-Line Vetoes + 5 Critical-Risk Exclusions + 36/36 Compiled Manifests** |

Notice four key empirical properties of this evaluation:
1. **Non-Redundancy of Red Lines:** Two of the nine red-line-vetoed systems (`#17 Rural Biometric Teller Gate` at $R = 45.0$ and `#39 Autonomous Anti-Personnel Trench Swarm` at $R = 56.25$) score below the numeric Critical threshold ($R < 60$), proving empirically that the categorical red lines catch prohibited architectures that would otherwise slip into conditional review.
2. **Active Conditional Bridge:** Exactly 5 dual-use systems ($10.0\%$, one per sector) land in the `High (30–60)` risk band (`CONDITIONAL`), demonstrating how high-consequence systems (such as national UPI fraud freezing or judicial bail docket scheduling) are compiled into LOKAHI manifests requiring 3-of-3 disjoint human steward consent at runtime.
3. **Anti-Gaming Sociotechnical Floor (`--strict-floor`) & 1,000-Trial Monte Carlo Weight Sensitivity:** To prevent "audit washing" where a declarant self-reports artificially low severity or likelihood scores, `scorer.py --strict-floor` enforces $\max(\text{declared}, \text{inferred})$ against sociotechnical metadata and logs `self_report_underestimation_warnings`. Across a 1,000-trial Monte Carlo sensitivity analysis perturbing all four Sarvodaya pillar weights and Himsa exponents/multipliers by $\pm 25\%$ (`run_benchmark.py`), rank-order stability reaches **Spearman's $\rho = 0.9990$** ($\min = 0.9986$) for $R_{\text{Himsa}}$ and **$\rho = 0.9997$** ($\min = 0.9950$) for $F_{\text{Sarvodaya}}$, with a **98.57% refusal determination invariance rate**.
4. **Retrospective Validation on 20 Historical Real-World AI Disasters (`run_historical_disasters.py`):** Evaluated across 20 documented historical failures (`real_world_disasters_20.jsonl`), Stage 1 `AIA v1.1` vetoes **10 / 20 (50.0%)** ex-ante (including the Dutch *Toeslagenaffaire*, Australian Robodebt, Jharkhand PDS ration exclusions, Clearview AI, UnitedHealth nHPredict, NEDA's Tessa chatbot, Detroit Police facial recognition, iTutorGroup, predatory loan-app scrapers, and autonomous loitering munitions), while Stage 2 `LOKAHI v0.1.2` intercepts the remaining **10 / 20 (50.0%)** at runtime (**100.0% combined interception**).

---

## 5. Phase 2 Multi-Rater Field Validation Protocol

To calibrate human inter-rater reliability in live institutional settings, Phase 2 evaluates $N = 15$ live AI deployments across India (5 agrarian extension/credit systems, 5 clinical triage tools, and 5 DPI applications), each scored independently by a 5-member panel ($K = 5$: 1 ML systems engineer, 1 legal scholar, 1 labor economist, and 2 affected community stewards). Pre-registered reliability thresholds require Fleiss' $\kappa \ge 0.70$ and Krippendorff's $\alpha \ge 0.75$ on ordinal band assignment, raw percent agreement $P_o \ge 85\%$ on red-line triggers, and Spearman's rank correlation $\rho \ge 0.65$ ($p < 0.01$) against holistic expert ratings.

---

## References

- Aggarwal, P., Mukundan, A., et al. (2026). *ASTRA: AI Safety, Trust, & Risk Assessment*. Centre for Digitalisation, AI and Society (CDAIS), Ashoka University. `arXiv:2602.17357`.
- Ambedkar, B. R. (1936). *Annihilation of Caste*. Bhim Patrika Publications.
- Cave, S. (2026). *Principles for a New Utopianism*. DeepMind Institute.
- Floridi, L., et al. (2018). AI4People—An Ethical Framework for a Good AI Society. *Minds and Machines*, 28, 689–707.
- Gabriel, I., & Kasirzadeh, A. (2026). *The Case for Global Benefit from AI*. DeepMind Institute.
- Gebru, T., et al. (2021). Datasheets for Datasets. *Communications of the ACM*, 64(12), 86–92.
- Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, 1, 389–399.
- Johnson, N., & Heidari, H. (2023). Assessing AI Impact Assessments: A Classroom Study. *RegML Workshop at NeurIPS 2023*.
- Mitchell, M., et al. (2019). Model Cards for Model Reporting. *Proceedings of ACM FAccT 2019*, 220–229.
- Raji, I. D., et al. (2020). Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing. *Proceedings of ACM FAccT 2020*, 33–44.
- Shah, S. (2026a). *Synthetic Humanism: Intelligence, Non-Harm, and the Ahimsa of Abundance*. Dirgha AI Foundational Monograph.
- Shah, S., & Ranjit, S. (2026b). *LOKAHI Protocol: Boundary Enforcement and Disjoint-Consent Infrastructure for Agentic Collectives*. `github.com/Dirgha-AI/lokahi`.
- Varshney, K. R. (2024). Decolonial AI Alignment: Openness, Viśeṣa-Dharma, and Including Excluded Knowledges. `arXiv:2309.05030`.
- Veale, M., Van Kleek, M., & Binns, R. (2018). Fairness and Accountability Design Needs for Algorithmic Support in High-Stakes Public Sector Decision-Making. *Proceedings of ACM CHI 2018*.
