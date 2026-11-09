# Building the Somatic Stack: Dirgha Code, AIA v1.1, and the LOKAHI Protocol

**Salik Shah**  
Founder & Lead Systems Architect, Dirgha AI · salikshah.com  
New Delhi, India · salik.shah@gmail.com

---

I build software and physical systems for a living. At Dirgha AI, we maintain **Dirgha Code**, our open-source coding and tool-use agent harness used by over 21,000 developers across 17 model providers, alongside the **Arniko** 36-scanner security engine and our open-source robotics platforms (**WallFin**, **DEX ARM 01**, and the **Lite3 Kinematics Lab**). Since 2015, I have also edited *Mithila Review*, an international journal of speculative fiction and futures thinking, and written the 245,468-word near-future duology *The American Emperor*.

Across both fiction and production engineering, the same architectural problem keeps surfacing: **how do we scale autonomous AI agents and embodied robots to deliver universal material abundance without hollowing out human judgment or breaking institutional safety boundaries?**

Over the past year, together with Sabin Ranjit (Senior Security Engineer at Kaluza, London), we built the philosophical, macroeconomic, and software answer to that question. We call the overarching framework **Synthetic Humanism**, anchored in two sentences:

> **"Intelligence, biological or synthetic, shall strive to cause no harm. Synthetic humanism applies intelligence toward the ahimsa of abundance."**

---

## Why Single-Agent Guardrails and Nominal Oversight Fail

When teams wire autonomous agents into production databases, municipal infrastructure, or robotic actuators, two things usually go wrong:

1. **Contextual Blindness and Fail-Open Timeouts:** Prompt classifiers only read text; they have no cryptographic awareness of whether a municipal manifest expired ten minutes ago, whether a query crosses a statutory data-residency border, or whether 24 agents in a consensus quorum are secretly controlled by a single Sybil operator. Worse, when a human-in-the-loop review timer expires without a response, legacy queues often default to auto-approval (`timeout -> approve`).
2. **Exoskeleton Atrophy ("Hollow Oversight"):** In 2025, a multicenter clinical study in *The Lancet Gastroenterology & Hepatology* found that after three months of routine AI assistance, endoscopists' unassisted adenoma detection rate fell from 28.4% to 22.4%. When AI systems interrupt humans on hundreds of trivial steps while smoothing deep uncertainty on high-stakes choices into a single polite recommendation, human capability atrophies.

---

## One Unified Verification Stack: From Compile-Time AIA to Runtime LOKAHI

To solve both problems in running code, we built a zero-dependency, two-stage verification stack inside `04_COMPUTATIONAL_ENGINE/`:

### 1. Stage 1 — The Ahimsa Impact Assessment (`AIA v1.1`, `scorer.py`)
Before a system ships, `scorer.py` evaluates its JSON declaration (`ahimsa-schema.json`) across two non-compensatory axes:
- **The Himsa Risk Penalty ($R \in [0, 187.5]$):** Measures severity, probability, population exposure, and lifecycle compounding with a neutral `v1.1` calibration that evaluates hardware reuse rather than penalizing developers in industrializing regions for municipal grid power.
- **The Sarvodaya Flourishing Index ($F \in [0, 100]$):** Scores contributor dignity, data reciprocity, public-good alignment, and 48-hour human redress.
- **Five Categorical Red Lines & Manifest Compiler:** Immediately vetoes offensive autonomous weapons, warrantless mass biometric surveillance, demographic/hereditary stratification, unsanctioned coercive transfers, and non-consensual community data extraction. Across our 50-system benchmark (`benchmark_50.jsonl`), `AIA v1.1` refuses 14 systems (28.0%), routes 5 intermediate dual-use systems into conditional oversight, and compiles all 36 approved or conditional systems directly into signed RFC 8785 Boundary Manifests (`scorer.py --compile-manifest`).

### 2. Stage 2 — The LOKAHI Protocol (`v0.1.2`, `lokahi.py`)
At runtime, `lokahi.py` intercepts Model Context Protocol (MCP) tool calls and robotics commands across 15 cost-ordered rules in `<0.3 ms`:
- **Autonomic Fast Path & Spinal Circuit Breakers (Rules 1–9):** Reversible, within-manifest calls clear in `<0.3 ms` with zero human prompts, while unsigned, expired, out-of-scope, or rate-exceeded calls fail closed immediately.
- **Collective Restraint & The Ahimsa Timeout Rule (Rules 10–15):** High-consequence calls escalate to a 3-of-3 disjoint steward ring (IETF RFC 9591 FROST). Two non-conflicted dissenting stewards freeze execution (**Rule 13: `suspended_by_ring`**), and if a review window times out without quorum, silence resolves strictly to refusal (**Rule 14: `non_response -> forbidden`**).

### 3. The Somatic Judgment Layer (`ghostproof.py`) & Kinetic Ahimsa (`run_kinetic_evals.py`)
- **Ghostproof (`Paper 5`):** Separates autonomic metabolism (`0 decisions/hr`) from prefrontal deliberation (`1–3 decisions/day` on messy Strong Bundles + `1 daily unassisted Sparring Node`), surfaces token-level Shannon entropy spikes and 300-word Adversarial Crux Briefs, and audits 2–3 peer Crux Pods via Brier calibration (`40/40` routing accuracy and `84%` alert-fatigue reduction on `Ghostproof-40`).
- **Kinetic Ahimsa (`Paper 6`):** Clamps contact forces (`5.0 N ± 1.1 N` on **WallFin**), joint torques and tendon tensions (`1,000 Hz` on **DEX ARM 01**), and support polygons (**Lite3**), blocking `90/90` out-of-envelope planner injections before servo transmission.

---

## Try It in Your Terminal

Every module, test suite, and benchmark runs out of the box on Python 3.10+ with zero external dependencies:

```bash
# Run Stage 1 AIA v1.1 Schema Validator, Unit Tests (12/12), & 50-System Benchmark
py 04_COMPUTATIONAL_ENGINE/validate_schema.py
py 04_COMPUTATIONAL_ENGINE/tests/test_scorer.py
py 04_COMPUTATIONAL_ENGINE/benchmark/run_benchmark.py

# Run Stage 2 LOKAHI v0.1.2, Ghostproof-40, & Kinetic Ahimsa Robotics Suites (38/38 Tests)
py 04_COMPUTATIONAL_ENGINE/lokahi/tests/test_core.py
py 04_COMPUTATIONAL_ENGINE/lokahi/tools/run_evals.py
py 04_COMPUTATIONAL_ENGINE/lokahi/tools/run_ghostproof_evals.py
py 04_COMPUTATIONAL_ENGINE/lokahi/tools/run_kinetic_evals.py
```

- **Repositories:** [github.com/Dirgha-AI/ahimsa-ai](https://github.com/Dirgha-AI/ahimsa-ai) · [github.com/Dirgha-AI/lokahi](https://github.com/Dirgha-AI/lokahi)
- **Website & Essays:** [salikshah.com](https://salikshah.com) · [salik.shah@gmail.com](mailto:salik.shah@gmail.com)
