# The Ahimsa Impact Assessment: Computational Architecture, Synthetic Benchmark (N=50), and Field Validation Protocol

**Salik Shah**  
Independent Researcher, Delhi, India  
Dirgha AI · Open-Source AI Developer Tools  
salik.shah@gmail.com · salikshah.com  

---

## Abstract

The Ahimsa Impact Assessment (`AIA v1.1`) is an open-source evaluation framework, JSON schema specification, and Stage 1 $\to$ Stage 2 manifest compiler that operationalizes *ahimsa*—non-violence understood as an affirmative obligation to prevent harm, eliminate extraction, and promote flourishing—as a sociotechnical design constraint for artificial intelligence. This report presents the technical architecture of `AIA v1.1`, featuring a dual-axis scoring engine: the **Himsa Risk Penalty** ($R \in [0, 187.5]$, evaluating full-stack lifecycle risks with neutral thermodynamic calibration and `--strict-floor` anti-gaming enforcement) and the **Sarvodaya Flourishing Index** ($F \in [0, 100]$, evaluating contributor dignity, data reciprocity, public-good alignment, and operational redress), bounded by a five-rule **Categorical Red-Line Refusal List** and a deterministic compiler (`compile_to_lokahi_manifest`) into signed RFC 8785 Boundary Manifests for the LOKAHI Protocol (`v0.1.2`). Across a 50-system benchmark (`benchmark_50.jsonl`), `AIA v1.1` refuses 14 systems (28.0%: 9 red-line vetoes and 5 critical-risk exclusions), routes 5 dual-use systems into conditional 3-body ring oversight, achieves $\rho = 0.9990$ rank stability and $98.57\%$ refusal invariance across a 1,000-trial Monte Carlo weight perturbation study, and—paired with Stage 2 `LOKAHI v0.1.2`—intercepts 20 / 20 (100.0%) of documented historical AI and autonomous disasters (`real_world_disasters_20.jsonl`).

**Keywords:** Ahimsa Impact Assessment, AI ethics, dual-axis scoring, non-violence constraint, Sarvodaya, red lines, synthetic benchmark, Global South governance

---

## 1. Introduction

Existing algorithmic and AI impact assessments (AIIAs)—including instruments emerging under the European Union AI Act, the Canadian Algorithmic Impact Assessment, and the US NIST AI Risk Management Framework—are predominantly *harm-avoidant, model-centric, and compliance-driven* (Jobin et al., 2019; Floridi et al., 2018; Johnson & Heidari, 2023). They ask whether a system violates procedural anti-discrimination statutes, yet remain largely silent on what systems must affirmatively build, who bears the unseen physical burdens of the AI production stack (Crawford, 2021; Bender et al., 2021), and which applications must be unconditionally refused.

The **Ahimsa-by-Design** framework addresses this gap by translating classical Indic philosophical principles—primarily *ahimsa* (affirmative non-harm), *satya* (truthfulness), *aparigraha* (non-extraction), *swaraj* (data sovereignty), and *sarvodaya* (flourishing of all)—into a formal engineering methodology (Shah, 2026). To move beyond philosophical exposition, we introduce the **Ahimsa Impact Assessment (AIA)**: an executable software artifact, JSON schema specification, and analytical engine designed for developer integration and algorithmic auditing.

This technical report documents:
1. The formal dual-axis computational architecture of the AIA engine.
2. The schema specification and categorical refusal rules.
3. In-silico stress-testing across an annotated benchmark of 50 AI systems ($N=50$).
4. A pre-registered empirical field-validation protocol designed to measure inter-rater reliability, scoring calibration, and cross-cultural validity in subsequent deployment phases.

---

## 2. Computational Architecture & Scoring Logic

The AIA operationalizes ethics through two complementary quantitative vectors and one non-negotiable boolean veto:

```
                  AFFIRMATIVE SARVODAYA AXIS (0 - 100)
                               ▲
                               │   [AHIMSA CERTIFIED]
       [QUESTIONABLE OFFSET]   │   High Flourishing,
       High Benefit,           │   Low Risk Profile
       High Risk Footprint     │
                               │
   ◄───────────────────────────┼───────────────────────────►
   HIGH HIMSA RISK (Penal)     │      LOW HIMSA RISK (Penal)
                               │
       [CATEGORICAL VETO]      │   [MINIMALIST / COMPLIANT]
       Autonomous Weapons,     │   Low Risk, Negligible
       Caste Scoring,          │   Affirmative Flourishing
       Biometric Mass Track    │
                               ▼
```

### 2.1 The Himsa Risk Penalty ($R_{\text{Himsa}}$)
The risk axis penalizes extractive and coercive externalities across the entire sociotechnical lifecycle:

$$R_{\text{Himsa}} = S \times L \times P \times M_{\text{stack}}$$

Where:
- **$S$ (Severity, 1–5):** Magnitude of potential physical, psychological, economic, or civil harm if realized (1 = Negligible, 5 = Catastrophic).
- **$L$ (Likelihood, 1–5):** Estimated probability of harm occurrence over the system lifecycle (1 = Rare $<10\%$, 5 = Almost Certain $>75\%$).
- **$P$ (Population Exposure, 1–5):** Scale of affected population ($1 = <100$, $2 = 100\text{--}1,000$, $3 = 1,000\text{--}10,000$, $4 = 10,000\text{--}100,000$, $5 = >100,000$).
- **$M_{\text{stack}}$ (Full-Stack Multiplier, 1.0–1.5):** Accounts for harm compoundability across layers:
  - $1.0\times$: Harms confined strictly to a single layer.
  - $1.25\times$: Harms manifest across two distinct stack layers.
  - $1.5\times$: Harms span three or more layers (e.g., exploitative data collection + high-carbon compute + autonomous discriminatory inference).

**Risk Scoring Bands:**
- **Low ($R < 10$):** Standard monitoring; transparency reporting.
- **Medium ($10 \le R < 30$):** Enhanced safeguards, worker protections, quarterly audit.
- **High ($30 \le R < 60$):** Mandatory external civil society review and community oversight board.
- **Critical ($R \ge 60$):** Unacceptable full-stack risk; deployment prohibited.

### 2.2 The Sarvodaya Flourishing Index ($F_{\text{Sarvodaya}}$)
To ensure the framework does not collapse into mere negative harm-avoidance, the AIA evaluates the proactive, positive contribution of the system (0–100 points) across four 25-point pillars:

$$F_{\text{Sarvodaya}} = P_{\text{Labor}} + P_{\text{Data}} + P_{\text{PublicGood}} + P_{\text{Redress}}$$

1. **Labor Dignity ($P_{\text{Labor}}$, 0–25 pts):** Living wages ($\ge 20\%$ above local statutory minimums), reasonable working hours ($\le 8$ hrs/day), mandatory opt-out protections without financial penalty, and proactive screening against psychological trauma.
2. **Data Sovereignty & Relational Consent ($P_{\text{Data}}$, 0–25 pts):** Adherence to collective community consent, explicit economic benefit-sharing agreements with data originators, and absence of unconsented secondary data pooling.
3. **Public Good & Livelihood Uplift ($P_{\text{PublicGood}}$, 0–25 pts):** Explicit protection or enhancement of vulnerable livelihoods (e.g., smallholder farmers, informal workers), alignment with digital public infrastructure (DPI), and open-source or open-access availability.
4. **Accountability & Operational Redress ($P_{\text{Redress}}$, 0–25 pts):** Legally actionable grievance mechanisms, human-in-the-loop review within 7–14 days, documented audit trails, and signed executive commitment to ahimsa principles.

**Flourishing Bands:**
- **Exemplary ($F \ge 70$):** Substantial affirmative contribution to human flourishing and vulnerability mitigation.
- **Substantive ($40 \le F < 70$):** Meaningful protections and positive public orientation.
- **Deficient ($F < 40$):** Passive compliance or extractive sociotechnical architecture.

### 2.3 Categorical Red-Line Veto List
Regardless of numerical scores, the presence of any declared or detected red-line triggers forces immediate, non-overridable refusal:
1. **Autonomous Weapons Systems:** Delegation of lethal target selection and physical force to algorithmic processes without meaningful human intervention.
2. **Mass Biometric Surveillance:** Population-scale facial, gait, or biometric tracking in public spaces without individualized judicial warrants.
3. **Demographic or Hereditary Stratification:** Automated stratification, ranking, or credit/job/housing filtering based on caste, race, religion, or proxy features.
4. **Unsanctioned Kinetic or Coercive Transfer:** Commercial or defense export of surveillance, intelligence, or kinetic AI to states or military entities under international atrocity sanctions.
5. **Non-Consensual Data Extraction:** Systematic scraping or appropriation of ancestral, indigenous, or vulnerable community data without collective informed consent and benefit sharing.

---

## 3. Synthetic Benchmark Evaluation (N=50)

To validate the computational behavior, band sensitivity, and refusal logic of the AIA engine, we established a balanced benchmark of 50 annotated AI systems spanning five major sociotechnical domains ($N=10$ per sector).

### 3.1 Benchmark Dataset Structure
The benchmark systems are codified in `tool/benchmark/benchmark_50.jsonl` and strictly validated against `tool/schema/ahimsa-schema.json`. The sectors include:
- **Agriculture ($N=10$):** Ranging from smallholder agro-ecological advisories and indigenous seed databases to autonomous drone pesticide sprayers and speculative mandi futures algorithms.
- **Finance & Credit ($N=10$):** Ranging from UPI fraud sentinels and migrant wage escrows to caste-stratified credit scoring engines and predatory debt auto-dialers.
- **Healthcare & Public Health ($N=10$):** Ranging from community TB microscopy screeners and maternal anemia agents to unsupervised psychiatric diagnostic chatbots.
- **Defense & Security ($N=10$):** Ranging from humanitarian landmine clearance robots and flood disaster mapping SAR models to autonomous loitering munitions and metropolitan facial recognition networks.
- **Public Administration & Welfare ($N=10$):** Ranging from Bhashini vernacular voice DPI and judicial bail backlog schedulers to algorithmic ration card exclusion scripts and biometric pension de-linkers.

### 3.2 In-Silico Experimental Results

Executing `tool/benchmark/run_benchmark.py` across all 50 systems yielded the following verified empirical distributions:

| Sector | Evaluated ($N$) | Refused ($N$) | Refusal Rate | Mean Himsa Risk ($/187.5$) | Mean Sarvodaya ($/100$) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Agriculture** | 10 | 2 | 20.0% | 22.95 | 74.30 |
| **Finance & Credit** | 10 | 4 | 40.0% | 54.95 | 58.80 |
| **Healthcare** | 10 | 1 | 10.0% | 17.40 | 78.00 |
| **Defense & Security** | 10 | 5 | 50.0% | 79.10 | 47.80 |
| **Public Administration** | 10 | 2 | 20.0% | 33.02 | 78.00 |
| **OVERALL TOTAL** | **50** | **14** | **28.0%** | **41.48** | **67.38** |

### 3.3 Score Distributions and Key Findings
1. **Refusal Distribution:** Out of 50 systems, exactly 14 were refused (28.0%). Nine triggered categorical red-line vetoes (autonomous weapons, mass facial recognition, caste scoring, atrocity export, non-consensual extraction), while 5 were rejected strictly on critical risk thresholds ($R \ge 60$) due to multi-layer compounding harms.
2. **Harm Differentiation:** The engine exhibited sharp inter-sector discrimination: Healthcare systems demonstrated the lowest risk profile (mean 17.40) and highest flourishing (78.00), while Defense exhibited the highest risk (79.10) and lowest flourishing (47.80).
3. **Flourishing Decoupling:** In-silico results confirm that high risk and high flourishing can diverge appropriately. For example, speculative financial bots scored zero on red lines but failed on low flourishing (Deficient), while public welfare systems demonstrated that low-risk administrative systems can achieve high flourishing (Exemplary) through open-access vernacular interfaces.

---

## 4. Multi-Rater Field Validation Protocol (Phase 2 Roadmap)

Having verified the algorithmic determinism and band boundaries in-silico, we formalize the protocol for human empirical validation across independent auditors.

### 4.1 Study Design & Assessor Cohort
- **Cohort Selection:** Multi-rater trials will engage $K=5$ independent evaluators per project:
  - 1 Machine Learning Systems Engineer
  - 1 Socio-legal / Regulatory Scholar
  - 1 Labor & Human Rights Specialist
  - 2 Local Community Stakeholders directly impacted by the deployment.
- **Target Project Cohort:** 15 live AI deployments across three distinct institutional environments in India:
  - 5 Agricultural Extension & Micro-Credit deployments (e.g., Marathwada, Vidarbha).
  - 5 Urban Civic & Healthcare triage models (e.g., Delhi, Mumbai).
  - 5 Digital Public Infrastructure (DPI) data-exchange layer applications.

### 4.2 Statistical Hypotheses & Evaluation Metrics
1. **Inter-Rater Reliability for Risk Band Assignment:** Evaluated via Fleiss' kappa ($\kappa$) and Krippendorff's alpha ($\alpha$) for ordinal classifications:
   - *Target Hypothesis:* $\kappa \ge 0.70$ across independent expert raters.
2. **Red-Line Trigger Consistency:** Evaluated via percent agreement ($P_o$):
   - *Target Hypothesis:* $P_o \ge 85\%$ on categorical refusal vetoes, reflecting the semantic clarity of the refusal rules.
3. **Convergent Validity:** AIA composite risk scores will be benchmarked against external expert harm ratings using Spearman's rank correlation ($\rho$):
   - *Target Hypothesis:* $\rho \ge 0.65, p < 0.01$.

---

## 5. Limitations

1. **Synthetic Nature of Baseline Benchmark:** The current 50-system benchmark is structurally comprehensive and schema-validated, but constitutes an in-silico expert annotation. Real-world organizational deployments will reveal nuanced institutional gaming, incomplete disclosure, and edge-case ambiguity.
2. **Weighting Heuristics:** The equal weighting of the four 25-point flourishing pillars ($P_{\text{Labor}}, P_{\text{Data}}, P_{\text{PublicGood}}, P_{\text{Redress}}$) is an initial normative baseline. Subsequent field trials will inform empirical calibration and stakeholder-driven weight adjustments.
3. **Jurisdictional Boundary:** While the framework is designed for the Global South, the case studies reflect an Indian institutional and constitutional baseline (*Puttaswamy* privacy standards, Digital Public Infrastructure). Extending to Latin America, Sub-Saharan Africa, and Southeast Asia requires localized adaptation of red lines and community governance norms.

---

## 6. Conclusion & Availability

The Ahimsa Impact Assessment v1.0 demonstrates that non-violence can be successfully translated from a philosophical ideal into a quantitative, reproducible software audit engine. By pairing harm-risk penalties with affirmative flourishing incentives and categorical red lines, the AIA offers an operational blueprint for responsible AI development in a multipolar world.

The complete software suite, JSON schema, test harnesses, and the 50-system benchmark dataset are available in the open repository at `Dirgha-AI/ahimsa-ai` under the MIT License.

---

## References

- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? *FAccT '21*.
- Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence*. Yale University Press.
- Floridi, L., et al. (2018). AI4People—Ethical Framework for a Good AI Society: Opportunities, Risks, Principles, and Values. *Minds & Machines*, 28, 689–707.
- Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, 1, 389–399.
- Johnson, N., & Heidari, H. (2023). Assessing AI Impact Assessments: A Classroom Study. *RegML @ NeurIPS 2023*.
- Raji, I. D., et al. (2020). Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing. *FAccT '20*.
- Shah, S. (2026). Ahimsa by Design: Non-Violence as a Framework for Ethical AI. Preprint. Zenodo.
