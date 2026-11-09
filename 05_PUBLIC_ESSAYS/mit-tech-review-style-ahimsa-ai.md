# From Prose Statutes to Sub-Millisecond Interlocks: Compiling Ahimsa Into the AI Stack

**Salik Shah**  
Founder & Lead Systems Architect, Dirgha AI · salikshah.com  
New Delhi, India · salik.shah@gmail.com

---

On August 1, 2012, an automated trading script at Knight Capital executed four million unverified orders in forty-five minutes, losing $440 million before human engineers could isolate the faulty deployment flag. In 2026, a Norwegian municipality relied on hallucinated generative AI citations to justify closing rural schools, illustrating what public-administration researchers call the "double black box" of algorithmic and institutional opacity.

As autonomous AI agents move from chat windows into Model Context Protocol (MCP) tool chains, Digital Public Infrastructure (DPI), and physical robotics actuators, AI governance faces a structural timing mismatch. High-level neural planners operate at 1 to 10 Hz with probabilistic outputs; physical robotic contact loops run at 100 to 1,000 Hz; and statutory compliance frameworks operate on multi-year judicial timelines.

Natural-language regulations establish essential normative boundaries, yet an autonomous agent or a 1,000 Hz tendon-driven robotic hand cannot pause mid-trajectory to interpret a 400-page prose statute. Conversely, prompt-level content classifiers (such as Llama Guard or NeMo Guardrails) inspect text strings in isolation. As researchers at Ashoka University's Centre for Digitalisation, AI and Society (CDAIS) demonstrated in *ASTRA: AI Safety, Trust, & Risk Assessment* (`arXiv:2602.17357`, 2026), single-prompt guardrails suffer from **contextual blindness**: they cannot see whether an agent is crossing a municipal jurisdiction, joining two legally separated welfare databases, or treating an unanswered human review timer as permission to execute an irreversible cutoff.

To close the gap between prose law and millisecond runtime execution, we need an axiomatic specification that compiles directly into software schemas and wire protocols.

---

## The Computable Invariant of Synthetic Humanism

In classical Indic jurisprudence—spanning Jain, Buddhist, and constitutional thought—*ahimsa* is an operational engineering discipline: the active prevention of injury paired with the affirmative obligation to cultivate shared flourishing (*sarvodaya*). Within **Synthetic Humanism**, this principle is stated in two sentences:

> **"Intelligence, biological or synthetic, shall strive to cause no harm. Synthetic humanism applies intelligence toward the ahimsa of abundance."**

To prove that this principle can govern both pre-deployment procurement and sub-millisecond runtime execution, we built a two-stage open-source verification stack (`Dirgha-AI/ahimsa-ai` and `Dirgha-AI/lokahi`, zero external dependencies):

### Stage 1: The Ahimsa Impact Assessment (`AIA v1.1`) & Manifest Compiler

Implemented in `04_COMPUTATIONAL_ENGINE/scorer/scorer.py`, the AIA replaces subjective compliance checklists with a **Dual-Axis Evaluation Engine**:
1. **The Himsa Risk Penalty ($R \in [0, 187.5]$):**
   $$R = \text{Severity} \times \text{Likelihood} \times \text{Population} \times M_{\text{stack}}$$
   Quantifies compounding risk across data provenance, contributor working conditions, hardware lifecycle reuse, and deployment autonomy. Crucially, our `v1.1` neutral calibration evaluates positive hardware reuse and inference efficiency disclosures rather than penalizing developers in industrializing regions for municipal electricity grid baselines.
2. **The Sarvodaya Flourishing Index ($F \in [0, 100]$):**
   Scores affirmative public-good creation across four 25-point pillars: contributor dignity (living wages, penalty-free opt-out rights), data sovereignty (community consent and reciprocal benefit-sharing), public-good alignment (open-access DPI and livelihood resilience), and operational redress (48-hour human review for automated account or welfare holds).
3. **Five Categorical Red Lines & RFC 8785 Compilation:**
   Enforces unconditional vetoes (`ExitCode = 1`) against offensive autonomous weapons, warrantless mass biometric surveillance, demographic or hereditary stratification, unsanctioned coercive transfers, and non-consensual community data extraction. Across our 50-system benchmark (`benchmark_50.jsonl`), `AIA v1.1` refuses 14 systems (28.0%: 9 red-line vetoes and 5 critical-risk exclusions), routes 5 intermediate dual-use systems (`30 <= R < 60`) into conditional oversight, and compiles all 36 approved or conditional declarations directly into signed RFC 8785 Canonical JSON Boundary Manifests (`scorer.py --compile-manifest`).

### Stage 2: The LOKAHI Protocol (`v0.1.2`), Ghostproof, and Kinetic Ahimsa

At runtime, `tools/lokahi.py` enforces the compiled RFC 8785 Boundary Manifest at the MCP gateway and robotics actuator bus across 15 cost-ordered decision rules in `<0.3 ms`:
- **Fail-Closed Membrane Checks (Rules 1–8):** Unsigned, tampered, or expired manifests, barred optimization targets, unlisted features, jurisdictional mismatches, data-residency violations, and exceeded sliding-window emergency caps (`Ledger.count_exceptions_in_window()`) fail closed immediately (`FORBIDDEN`).
- **Autonomic Fast Path vs. 3-Body Disjoint Ring (Rules 9–15):** Routine reversible calls clear locally in `<0.3 ms` (`Rule 9: within_manifest`). Irreversible or population-affecting calls escalate to a 3-of-3 disjoint steward ring (IETF RFC 9591 FROST) that deduplicates Sybil agent swarms by operator identity (`AE-E05`). Any two non-conflicted dissenting stewards trigger an immediate safety freeze (**Rule 13: `suspended_by_ring`**), and if a review window times out without quorum, silence resolves strictly to refusal (**Rule 14: `non_response -> forbidden` — The Ahimsa Timeout Rule**).
- **The Somatic Judgment Layer (`ghostproof.py`) & Kinetic Ahimsa (`run_kinetic_evals.py`):** To prevent human reviewers from rubber-stamping smoothed AI outputs—a failure mode that caused endoscopists' unassisted detection rates to drop from 28.4% to 22.4% in a 2025 *Lancet* trial—`ghostproof.py` surfaces token-level Shannon entropy spikes and 300-word Adversarial Crux Briefs, routes one daily unassisted Sparring Node, and scores 2–3 peer Crux Pods via Brier calibration (`100%` contestability rate and `84%` alert-fatigue reduction across `Ghostproof-40`). In physical robotics, `lokahi.py` clamps contact forces (`5.0 N ± 1.1 N` on **WallFin**), joint torques and tendon tensions (`1,000 Hz` on **DEX ARM 01**), and kinematic support polygons (**Lite3**), blocking `90/90` out-of-envelope injections before a single servo packet reaches the hardware bus.

By compiling ethical principles into deterministic pre-flight protocols and open Digital Public Infrastructure, builders can ship high-velocity autonomous systems that expand material abundance while remaining provably safe by design.
