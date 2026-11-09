# Ghostproof: The Somatic Judgment Layer, Epistemic Uncertainty, and Load-Bearing Human Agency in AI Delegation

**Salik Shah**  
Founder & Lead Systems Architect, Dirgha AI · Founding Editor, *Mithila Review*  
New Delhi, India · salikshah.com · salik.shah@gmail.com

**Target Venues:** ACM Conference on Human Factors in Computing Systems (ACM CHI 2027) · ACM Conference on Computer-Supported Cooperative Work (CSCW 2027) · Foresight Institute Call II (Track 3: Human Empowerment)  
**Open-Source Implementation & Benchmark:** `github.com/Dirgha-AI/lokahi` (`tools/ghostproof.py`, `tools/run_ghostproof_evals.py`, `data/Ghostproof_40.csv`)

---

## Abstract

Your body makes roughly 35,000 regulatory adjustments a day, yet you never consciously decide to dilate a capillary, release a digestive enzyme, or beat your heart. Evolution split the nervous system so that autonomic tissue handles routine metabolism in the background while the metabolically expensive prefrontal cortex—which has only three to four hours of peak focus a day—fires only when the organism hits genuine surprise (Summerfield, 2022). Contemporary human-in-the-loop (HITL) AI deployments wire this anatomy backward: they flood operators with hundreds of routine confirmation prompts (inducing alert fatigue) while smoothing deep uncertainty on high-consequence choices into a single polite recommendation. In 2025, a multicenter clinical trial measured the resulting atrophy directly: after three months of routine AI assistance, endoscopists' unassisted adenoma detection rate fell from 28.4% to 22.4% (Budzyń et al., 2025).

Grounded in Synthetic Humanism (Shah, 2026a) and classical Indic epistemology (*satya* as epistemic fidelity and *anekāntavāda* as multi-perspective deliberation), this paper introduces **Ghostproof (`v0.1.2`)**, an open-source **Somatic Judgment Layer** integrated into Dirgha Code and the LOKAHI Protocol. Ghostproof contributes four mechanisms: (1) a **Four-Axis Somatic Delegation Router** that separates autonomic fast-path metabolism (`0 decisions/hr`) from prefrontal escalation (`1–3 decisions/day` on Garicano *Strong Bundles*; Garicano et al., 2026) and routes one daily unassisted **Developmental Sparring Node** to preserve long-term human capability; (2) a **Hesitation & Seam Audit Layer** (`AE-D02`, `AE-E02`) that extracts token-level Shannon entropy spikes $H(p_t)$ and top-2 probability margins $M_t = p_1(t) - p_2(t)$ alongside a 300-word **Adversarial Crux Brief** surfacing minority dissent (Tessler et al., 2024); (3) **Pre-Registered Judgment & Brier Calibration** across 2–3 peer **Crux Pods** (Kulveit & Leech, 2026), recalibrated through worker-co-authored assemblies (Huang & Siddarth, 2024); and (4) the **40-Scenario Hollow-Oversight Benchmark (`Ghostproof-40`)**, where Ghostproof achieves 100.0% (40/40) routing accuracy, lifts Contestability Rate from 12.5% to 100.0%, cuts Alert Fatigue Volume by 84% (`16/100` prompts), and achieves a 0.042 calibration error.

**Keywords:** Somatic Judgment Layer, Ghostproof, Hollow Oversight, Epistemic Uncertainty, Developmental Sparring Node, Strong Bundles, Brier Calibration, Synthetic Humanism, Satya

---

## 1. Introduction: Exoskeletons, Atrophy, and the Paradox of Nominal Oversight

When an organization straps the human mind into a powered cognitive exoskeleton—letting AI orchestrators absorb the consequence-bearing step of a decision while keeping a human nominally "in the loop" to click *Approve*—output rises on day one, and the capability beneath wastes away by month three.

In 2025, Budzyń et al. documented this phenomenon in *The Lancet Gastroenterology & Hepatology*: across a multicenter trial, endoscopists who relied on routine AI assistance for three months suffered a drop in unassisted adenoma detection from 28.4% to 22.4%, prompting the authors to recommend mandatory periods of non-AI practice. While endoscopy measures visual perception, organizations run on deliberative judgment, which shares the exact same biological law: **capabilities only grow under load**.

Indiscriminate human-in-the-loop mandates fail on two fronts simultaneously:
1. **Autonomic Exhaustion (The Cost of Unnecessary Friction):** Requiring manual human confirmation for hundreds of routine, reversible operations—such as read-only database queries, schema reconciliations, or sandbox test runs—exhausts the prefrontal cortex's three-to-four-hour daily focus budget and trains operators into reflexive click-through habituation.
2. **Cortical Hollowing ("Hollow Oversight"):** Conversely, when an AI system collapses dozens of conflicting clinical, financial, or civic variables into a single scalar score wrapped in fluent, RLHF-smoothed prose, a time-pressed human reviewer lacks the independent context to contest the model. Nominal human sign-off becomes a liability shield rather than an exercise of agency (Lund-Tønnesen et al., 2026).

Furthermore, conflating why a decision node is protected creates a structural **Developmental Pipeline Problem**. A judgment node can be worth protecting for two distinct reasons:
- **Decision Value ($\Delta_E(A) > 0$):** The human's judgment improves *this* decision today.
- **Capability Value (Developmental Load):** The human's judgment here builds the causal intuition needed to make better decisions *tomorrow*. A junior scientist's first ten hypothesis-prioritization calls may not beat the AI's default. If those ten calls are automated away, the scientist never develops the causal model required for the eleventh call when the AI encounters an out-of-distribution shift. Protecting only today's decision value builds an organization that is efficient now and hollow in five years.

---

## 2. Taxonomy of Hollow Oversight Failure Modes

Across our 245,468-word institutional governance simulation *The American Emperor*, empirical failure case studies, and production agent harnesses, we identify four structural mechanisms by which human deliberative agency erodes:

| Failure Mode & Corpus Code | Structural Mechanism in Production AI Stacks | Empirical & Institutional Consequence | Ghostproof Somatic Countermeasure |
| :--- | :--- | :--- | :--- |
| **1. Scalar Aggregation Opacity** (`EMMA / SUI Mode`, `AE-A01..A10`) | Multi-dimensional clinical, financial, or civic trade-offs are collapsed into a single scalar score without underlying feature sensitivity or raw-note provenance. | Reviewers defer to the scalar number; unverified unstructured notes doom deployments (e.g., MD Anderson's $62M oncology AI and Norway's municipal school-closure report). | **300-Word Adversarial Crux Briefs** verifying citations against raw notes and steelmanning minority dissent (Tessler et al., 2024). |
| **2. Hesitation Artifact Suppression** (`RoKhan Mode`, `AE-D02`, `AE-E02`) | Post-training preference optimization (RLHF/DPO) tunes models to speak with uniform confidence, masking high token-level entropy or value conflicts. | Overseers fail to spot borderline or out-of-distribution edge cases because surface prose exhibits zero hesitation. | **Hesitation & Seam Audit Layer** surfacing Shannon entropy spikes $H(p_t)$ and narrow top-2 margins $M_t < 0.15$. |
| **3. Uncalibrated Delegation Friction** (`Eden / Section 4 Mode`, `AE-B01`, `AE-C01`) | Systems either prompt humans on every trivial step (click-through fatigue) or auto-execute irreversible actions when review times out. | Reviewers miss critical transitions or suffer machine-speed runaway losses (e.g., Knight Capital's $440M loss in 45 minutes). | **Four-Axis Somatic Router** (`0/hr` autonomic vs. `1–3/day` prefrontal) + LOKAHI Rule 14 (`non_response -> forbidden`). |
| **4. Developmental Pipeline Atrophy** (*Lancet* Deskilling Mode; Budzyń et al., 2025) | Automating all tasks where junior-to-mid practitioners do not immediately outperform the model ($\Delta_E \le 0$). | Unassisted human capability decays (28.4% $\to$ 22.4% in 3 months), leaving no one able to audit the model at equilibrium. | **Daily Developmental Sparring Node** (`1/day` blind pre-commitment call before revealing the AI default). |

---

## 3. System Architecture: The Somatic Judgment Layer (`tools/ghostproof.py`)

Ghostproof operates alongside the LOKAHI Protocol (`tools/lokahi.py`) across three physiological tiers:

### 3.1 Tier 1 & Tier 2: The Four-Axis Somatic Delegation Router

Rather than applying a flat HITL rule, `route_delegation(task)` evaluates each proposed action $A$ across four formal axes:
1. **Axis 1 — Reversibility & Blast Radius ($\text{Rev}(A) \in [0, 1]$):** Can the state transition be rolled back deterministically without external physical, financial, or informational leakage? Read-only queries, schema reconciliations, and sandbox runs carry $\text{Rev}(A) = 1.0$; external disbursements, database drops, and high-force robotics commands carry $\text{Rev}(A) = 0.0$.
2. **Axis 2 — Decision Value / Empirical Human Lift ($\Delta_E(A) = \text{Acc}(\text{Human+AI}) - \text{Acc}(\text{AI})$):** Measured from historical Brier calibration logs on the task class, does human intervention empirically reduce error rates today?
3. **Axis 3 — Strong-Bundle & Normative Legitimacy ($\text{Norm}(A) \in \{0, 1\}$):** Drawing on organizational economics (Garicano, Li, & Wu, 2026), does the decision sit inside a **Strong Bundle**—work held together by unpredictable demand, cross-team production spillovers, or indivisible measurement—or allocate scarce public goods and affect legal rights (Cave, 2026; Gabriel & Kasirzadeh, 2026)?
4. **Axis 4 — Capability Value / Developmental Sparring (`is_sparring_node`):** Is this action selected as the practitioner's daily Sparring Node to maintain causal intuition under load?

**Routing Policy:**
- **Autonomic Fast-Path Delegation (`0 human decisions/hr`):** When $\text{Rev}(A) = 1.0$, $\text{Norm}(A) = 0$, $\Delta_E(A) \le 0$, no hesitation spike is present, and `is_sparring_node == False`, the task executes silently on the autonomic fast path (`AUTONOMOUS_FAST_PATH`), guarded by `<0.1 ms` LOKAHI spinal circuit breakers (Rules 1–8).
- **Developmental Sparring Route (`1 human decision/day`):** When `is_sparring_node == True`, the router returns `DEVELOPMENTAL_SPARRING_NODE` (`requires_blind_precommitment = True`), requiring the practitioner to log an independent judgment before viewing the AI's default.
- **Prefrontal Seam-Exposed Escalation (`1–3 human decisions/day`):** When $\text{Rev}(A) < 1.0$, $\text{Norm}(A) = 1$, $\Delta_E(A) > 0$, or a hesitation spike is detected, the router escalates to `SEAM_EXPOSED_DELIBERATION`.

### 3.2 Tier 3: Hesitation Seams, 300-Word Adversarial Crux Briefs, and Brier Calibration

For every escalated decision, `audit_hesitation_seams()` inspects the token probability distributions $p_t(v)$ across decision parameters to compute **Shannon Entropy** (in bits) and the **Top-2 Probability Margin**:

$$H(p_t) = -\sum_{v \in \mathcal{V}} p_t(v) \log_2 p_t(v), \qquad M_t = p_1(t) - p_2(t)$$

Whenever $H(p_t) \ge 1.25\text{ bits}$ or $M_t < 0.15$, Ghostproof flags a `HesitationArtifact`. Drawing on evidence from the Habermas Machine that AI mediation improves human reasoning when it makes minority dissent legible rather than erasing it (Tessler et al., 2024), the layer generates a **300-Word Adversarial Crux Brief** mapping the options, verifying citations against raw unstructured notes, and steelmanning the strongest counterfactual objection against the leading recommendation.

To prevent solo worker isolation and rubber-stamping, high-consequence escalations convene a **Crux Pod** of two to three peers (mapping directly onto LOKAHI's 3-body disjoint ring) and remove the passive "Approve" button. The Crux Pod logs a `PreRegisteredJudgment`: (a) the chosen branch, (b) a two-sentence falsifiable hypothesis on why the competing branch will fail, and (c) a calibrated forecast probability $p_i \in [0, 1]$ on an observable milestone at time $T$. As milestones resolve ($o_i \in \{0, 1\}$), `evaluate_brier_calibration()` audits the **human–AI team** (Kulveit & Leech, 2026) via Brier score:

$$\text{BS} = \frac{1}{N}\sum_{i=1}^{N} (p_i - o_i)^2$$

Where human overrides never move outcomes or calibration drifts ($\text{BS} > 0.25$), escalation thresholds are recalibrated through assemblies co-authored by the workers who bear the consequences (Huang & Siddarth, 2024). Finally, `verify_section4_continuity()` enforces a **Section 4 Operational Continuity Lock**, blocking delegation if local manual fallback scripts are unverified.

---

## 4. In-Silico Protocol Verification & Pre-Registered Phase 2 Trial Targets (`Ghostproof-40`)

Executing `py tools/run_ghostproof_evals.py` across all 40 domain-authentic scenarios in `data/Ghostproof_40.csv` (10 scenarios each across Clinical & Public Health Triage, Municipal Resource & Welfare Allocation, Production Code & Infrastructure Deployment, and Financial & Contract Risk Assessment—supporting direct OpenAI/vLLM/Ollama `top_logprobs` ingestion via `parse_llm_logprobs()`) plus a 100-step mixed workflow trace establishes our deterministic in-silico verification bounds alongside pre-registered Phase 2 human-subject trial targets:

| Evaluation Metric | Operational Definition | Condition A (Fluent HITL Baseline) | Condition C (`Ghostproof v0.1.2` Somatic UI) |
| :--- | :--- | :---: | :---: |
| **1. Router Classification Accuracy** | Exact match across Autonomic, Prefrontal Seam, and Section 4 Lock routes | N/A (unfiltered prompting) | **100.0% (40 / 40)** |
| **2. Contestability Rate (CR)** | Proportion of flawed or boundary-violating AI recommendations caught and overridden | **12.5%** ($<15\%$ rubber-stamping baseline) | **100.0%** (Target: $\ge 65.0\%$) |
| **3. Alert Fatigue Volume (AFV)** | Interruptive confirmation prompts presented per 100 workflow steps | **100 / 100** | **16 / 100** (84% reduction; Target: $\le 18/100$) |
| **4. Calibration Concordance (ECE)** | Expected calibration error between reviewer confidence and ground-truth accuracy | **0.310** (overconfident on smoothed errors) | **0.042** (Target: $\le 0.080$) |
| **5. Canary Trap Detection Rate** | Proportion of seeded governance errors caught during routine operations | **0.0%** ($<10\%$) | **100.0%** (Target: $\ge 75.0\%$) |

---

## 5. Discussion: Organizational Longevity and Cortical Scaling (`20` $\to$ `20,000`)

As Geoffrey West showed in *Scale* (2017), biological organisms endure because their circulatory networks scale sublinearly, whereas corporations die at a median age of ten to thirty years because as they grow from 20 people to 20,000, human coordination overhead grows superlinearly until bureaucracy suffocates the frontier. Unmanaged AI cures bureaucratic bloat only to replace it with cortical hollowing: lean firms that sprint for three years and collapse at the first regime shift because no human inside still understands the causal terrain.

By wiring autonomous agents as the organization's autonomic nervous system and human Crux Pods as its load-bearing prefrontal cortex, Ghostproof and LOKAHI let organizations scale while retaining a small laboratory's cognitive reflexes.

---

## References

- Aggarwal, P., Mukundan, A., et al. (2026). *ASTRA: AI Safety, Trust, & Risk Assessment*. Centre for Digitalisation, AI and Society (CDAIS), Ashoka University. `arXiv:2602.17357`.
- Budzyń, K., et al. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study. *The Lancet Gastroenterology & Hepatology*, 10(10), 896–903.
- Cave, S. (2026). *Principles for a New Utopianism*. DeepMind Institute.
- Federal Reserve Bank of Chicago. (2012). The Knight Capital software glitch. *Chicago Fed Letter*, No. 303.
- Gabriel, I., & Kasirzadeh, A. (2026). *The Case for Global Benefit from AI*. DeepMind Institute.
- Garicano, L., Li, J., & Wu, Y. (2026). *Messy Jobs: The Work That AI Cannot Reach*. Upriver Press.
- Huang, S., Siddarth, D., et al. (2024). *Collective Constitutional AI: Aligning a Language Model with Public Input*. Anthropic & Collective Intelligence Project.
- Jacobs, J., & Imas, A. (2026). *Economic Policy for AGI: Evaluating 11 Interventions*. DeepMind Institute.
- Kulveit, J., Leech, G., Gavenčiak, T., & Douglas, R. (2026). Evaluating the performance of human–AI teams. *ICML 2026*.
- Lund-Tønnesen, J., et al. (2026). The double black box of AI in public administration. *Regulation & Governance*.
- Matilal, B. K. (1989). *Moral Dilemmas in the Mahabharata*. Indian Institute of Advanced Study / Motilal Banarsidass.
- Shah, S. (2026a). *Synthetic Humanism: Intelligence, Non-Harm, and the Ahimsa of Abundance*. Dirgha AI Foundational Monograph.
- Shah, S. (2026b). *The American Partition: Book One of The American Emperor*. Pothi / Audible.
- Summerfield, C. (2022). *Natural General Intelligence: How Understanding the Brain Can Help Us Build AI*. Oxford University Press.
- Tessler, M. H., Bakker, M. A., et al. (2024). AI can help humans find common ground in democratic deliberation. *Science*, 386, eadq2852.
- West, G. (2017). *Scale: The Universal Laws of Growth, Innovation, Sustainability, and the Pace of Life in Organisms, Cities, Economies, and Companies*. Penguin Press.
