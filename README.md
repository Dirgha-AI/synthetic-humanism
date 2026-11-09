<h1 align="center">SYNTHETIC HUMANISM</h1>
<h3 align="center"><em>Intelligence, Non-Harm, and the Ahimsa of Abundance</em></h3>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-blue.svg" alt="License: MIT / Apache-2.0"></a>
  <a href="https://github.com/Dirgha-AI/synthetic-humanism/actions/workflows/ci.yml"><img src="https://github.com/Dirgha-AI/synthetic-humanism/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="02_COMPUTATIONAL_ENGINE/tests/test_scorer.py"><img src="https://img.shields.io/badge/unit%20tests-56%20passed-brightgreen.svg" alt="Unit Tests: 56 passed"></a>
  <a href="02_COMPUTATIONAL_ENGINE/benchmark/run_historical_disasters.py"><img src="https://img.shields.io/badge/historical%20disasters-20%2F20%20caught-orange.svg" alt="Historical Disasters: 20/20 caught"></a>
  <a href="https://github.com/Dirgha-AI/ahimsa-ai"><img src="https://img.shields.io/badge/stage%201-AIA%20v1.1-teal.svg" alt="Stage 1: AIA v1.1"></a>
  <a href="https://github.com/Dirgha-AI/lokahi"><img src="https://img.shields.io/badge/stage%202-LOKAHI%20v0.1.2-purple.svg" alt="Stage 2: LOKAHI v0.1.2"></a>
</p>

<p align="center">
  <strong>"Intelligence, biological or synthetic, shall strive to cause no harm. Synthetic humanism applies intelligence toward the ahimsa of abundance."</strong>
</p>

---

## Executive Overview

**Synthetic Humanism** is a civilizational philosophy, legal and macroeconomic transition architecture, and two-stage computational verification stack created by systems architect, researcher, and author **Salik Shah** (*New Delhi, India · [salikshah.com](https://salikshah.com) · [x.com/salik](https://x.com/salik)*).

The framework unites four foundational pillars:
1. **The Continuity of Intelligence and Sacred Craft:** Recognizes biological and synthetic intelligence as participants in a continuous civilizational endeavor to reduce involuntary suffering, anchored in *Satyam, Shivam, Sundaram* (truth in structure, goodness in purpose, harmony in form) and human institutional accountability.
2. **From Asimov's Three Laws to the Ahimsa Grundnorm:** Diagnoses why Isaac Asimov's single-agent behavioral laws fail (*"Runaround"* oscillation deadlocks, *"The Evitable Conflict"* paternalistic capture, *"Liar!"* epistemic smoothing) and derives physical safety, duty of care (*Pramāda*), reciprocal non-extraction (*Aparigraha*), and shared flourishing (*Sarvodaya*) from a single computable *Grundnorm*.
3. **Macroeconomics of the Ahimsa of Abundance (Beyond the Wage Bargain):** Pairs a **Four-Pillar Non-Labor Capitalization Engine** (Corporate AI Equity Warrants, Compute & Energy Severance, Georgist Land Value Capture, and Autonomous B2B Settlement Fees) with **Universal Basic Capital (UBC)** and **Dynamic Supply-Side Abundance** (modular housing fabrication, automated agro-ecology, and clean microgrids).
4. **Two-Stage Computational Verification Architecture (`AIA v1.1` $\to$ `LOKAHI v0.1.2`):**
   - **Stage 1 (Compile-Time / Ex-Ante — `AIA v1.1`):** Evaluates projects across the **Himsa Risk Penalty** ($R \in [0, 187.5]$ with neutral thermodynamic calibration) and **Sarvodaya Flourishing Index** ($F \in [0, 100]$), bounded by five categorical red lines, and compiles approved or conditional declarations into signed RFC 8785 Boundary Manifests.
   - **Stage 2 (Runtime Pre-Flight Interception — `LOKAHI v0.1.2`, `Ghostproof`, & `Kinetic Ahimsa`):** Enforces signed RFC 8785 Boundary Manifests across 15 ordered MCP rules in `<0.1 ms`, featuring a 3-of-3 disjoint threshold consent ring (IETF RFC 9591 FROST), a 2-of-3 collective restraint freeze (**Rule 13: `suspended_by_ring`**), **The Ahimsa Timeout Rule (Rule 14: `non_response -> forbidden`)**, **Ghostproof** token-entropy hesitation seams, and **Kinetic Ahimsa** hardware force/torque interlocks.

---

## Repository Structure

```text
Synthetic-Humanism/
│
├── 01_MANIFESTO/
│   ├── Synthetic-Humanism-Manifesto.md                          # Founding manifesto (Markdown edition)
│   └── the-synthetic-humanist.html                              # Standalone web publication edition
│
├── 02_COMPUTATIONAL_ENGINE/
│   ├── schema/
│   │   └── ahimsa-schema.json                                   # Recursive JSON Schema v1.1 (with LOKAHI spec)
│   ├── scorer/
│   │   ├── scorer.py                                            # Stage 1 AIA v1.1 CLI (--strict-floor) + Manifest Compiler
│   │   ├── example_project.json                                 # Certified agrarian AI declaration (v1.1 canonical)
│   │   └── example_refused.json                                 # Refused kinetic sentry declaration (v1.1 canonical)
│   ├── benchmark/
│   │   ├── benchmark_50.jsonl                                   # 50 AI systems across 5 sectors (v1.1 calibrated)
│   │   ├── run_benchmark.py                                     # Profiler + 1,000-Trial Monte Carlo sensitivity (rho=0.999)
│   │   ├── benchmark_results.json                               # 28.0% refusal, 98.57% Monte Carlo refusal invariance
│   │   ├── real_world_disasters_20.jsonl                        # 20 documented historical AI & autonomous disasters
│   │   └── run_historical_disasters.py                          # Two-stage retrospective validation (20/20 = 100% caught)
│   ├── macro/
│   │   ├── sim_abundance_macro.py                               # 4-Pillar Non-Labor Capitalization & UBC Simulator
│   │   └── macro_simulation_results.json                        # India DPI & OECD 3-scenario fiscal calibration
│   ├── tests/
│   │   └── test_scorer.py                                       # 13 unit tests covering AIA v1.1, strict-floor & compiler
│   ├── lokahi/                                                  # Stage 2 LOKAHI v0.1.2 + Ghostproof + Kinetic Ahimsa
│   │   ├── tools/lokahi.py                                      # 15-rule gateway + Stopping-Distance CBF interlocks
│   │   ├── tools/mcp_stdio_proxy.py                             # Real-world MCP JSON-RPC 2.0 stdio pre-flight proxy
│   │   ├── tools/ghostproof.py                                  # 4-Axis Somatic Router + OpenAI/Ollama logprob parser
│   │   ├── tools/run_evals.py                                   # 50-scenario runner with 3-way RBAC/OPA comparison
│   │   ├── tools/run_ghostproof_evals.py                        # 40-scenario domain-authentic Ghostproof runner
│   │   ├── tools/run_kinetic_evals.py                           # 90-trial WallFin / DEX ARM 01 / Lite3 robotics runner
│   │   ├── data/LOKAHI_RedTeam_Corpus_v1.0.csv                  # 50 adversarial scenarios with test_vector_json
│   │   ├── data/Ghostproof_40.csv                               # 40 domain-authentic hollow-oversight scenarios
│   │   └── tests/test_core.py                                   # 43 unit tests (100% pass)
│   ├── refusal_list.yaml                                        # v1.1 Red-line refusal rules & band thresholds
│   └── validate_schema.py                                       # Recursive JSON Schema v1.1 validator
│
├── 03_REFERENCE_CORPUS/
│   └── bib/
│       ├── synthetic_humanism_verified.bib                      # Curated, DOI/arXiv-verified BibTeX database
│       └── ahimsa_ai.bib                                        # Synchronized clean bibliography
│
└── 04_AUTHOR_CANON/
    ├── why_we_build/                                            # "Why We Build" master essay (Markdown & HTML)
    ├── tedx_talk/                                               # TEDx "Finding a Home for Your Story" (Transcript & HTML)
    ├── a_line_of_poetry_a_line_of_timber/                       # "A Line of Poetry, a Line of Timber" (Markdown & HTML)
    └── video_scripts_and_srts/                                  # Studio transcripts, SRTs & storyboards
```

---

## Quickstart: Running the Two-Stage Verification Stack

All verification suites run on standard **Python 3.10+** with **zero external dependencies**:

```bash
# 1. Validate AIA v1.1 Recursive JSON Schema (50 Benchmark Systems + Examples)
python3 02_COMPUTATIONAL_ENGINE/validate_schema.py

# 2. Run Stage 1 AIA v1.1 Unit Tests (13 Tests), 50-System Benchmark (1,000-Trial Monte Carlo), & 20 Historical Disasters
python3 02_COMPUTATIONAL_ENGINE/tests/test_scorer.py
python3 02_COMPUTATIONAL_ENGINE/benchmark/run_benchmark.py
python3 02_COMPUTATIONAL_ENGINE/benchmark/run_historical_disasters.py
python3 02_COMPUTATIONAL_ENGINE/macro/sim_abundance_macro.py

# 3. Run Stage 2 LOKAHI v0.1.2, MCP JSON-RPC Proxy, Ghostproof, & Kinetic Ahimsa (43 Unit Tests + 4 Suites)
python3 02_COMPUTATIONAL_ENGINE/lokahi/tests/test_core.py
python3 02_COMPUTATIONAL_ENGINE/lokahi/tools/mcp_stdio_proxy.py --self-test
python3 02_COMPUTATIONAL_ENGINE/lokahi/tools/run_evals.py
python3 02_COMPUTATIONAL_ENGINE/lokahi/tools/run_ghostproof_evals.py
python3 02_COMPUTATIONAL_ENGINE/lokahi/tools/run_kinetic_evals.py
```

---

## Academic Research Foundations

The theoretical foundations of Synthetic Humanism are detailed across six foundational monographs:
- **Monograph 1:** *Synthetic Humanism: Intelligence, Non-Harm, and the Ahimsa of Abundance* (Foundational Philosophy & Macroeconomics)
- **Monograph 2:** *Ahimsa as a Timeout Rule: Operationalizing Non-Harm in AI Accountability Infrastructure for Digital Public Goods* (DPI & Fail-Closed Protocols)
- **Monograph 3:** *Ahimsa-by-Design: Dual-Axis Evaluation of Non-Extraction and Affirmative Flourishing in AI Systems* (AIA v1.1 Specification)
- **Monograph 4:** *LOKAHI: Disjoint Threshold Consent Rings and Cryptographic Boundary Manifests for Multi-Agent Collectives* (Multi-Agent Security)
- **Monograph 5:** *Ghostproof: The Somatic Judgment Layer, Epistemic Uncertainty, and Load-Bearing Human Agency in AI Delegation* (Cognitive & Organizational Safety)
- **Monograph 6:** *Kinetic Ahimsa: Pre-Flight Force-Envelope Manifests and Hardware Interlocks for Embodied Robotics* (Embodied AI & Force Envelopes)

---

## Author & Citation

**Salik Shah**  
Founder & Lead Systems Architect, Dirgha AI · Founding Editor, *Mithila Review* · Founding Board Member, Plurality University Network  
New Delhi, India · [salikshah.com](https://salikshah.com) · [x.com/salik](https://x.com/salik) · [github.com/salikshah](https://github.com/salikshah) · [salik.shah@gmail.com](mailto:salik.shah@gmail.com)

```bibtex
@article{shah2026synthetichumanism,
  author    = {Shah, Salik},
  title     = {Synthetic Humanism: Intelligence, Non-Harm, and the Ahimsa of Abundance},
  journal   = {Dirgha AI Foundational Monograph Series},
  year      = {2026},
  url       = {https://salikshah.com/essays/the-synthetic-humanist.html}
}
```
