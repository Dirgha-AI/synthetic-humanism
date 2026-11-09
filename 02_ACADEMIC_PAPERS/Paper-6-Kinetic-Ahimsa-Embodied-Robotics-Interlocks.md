# Kinetic Ahimsa: Pre-Flight Force-Envelope Manifests and Hardware Interlocks for Embodied Robotics

**Salik Shah**  
Founder & Lead Systems Architect, Dirgha AI · Founding Editor, *Mithila Review*  
New Delhi, India · salikshah.com · salik.shah@gmail.com

**Target Venues:** IEEE International Conference on Robotics and Automation (ICRA 2027) Safe Embodied AI Workshop · IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2027) · Conference on Robot Learning (CoRL)  
**Open-Source Repositories & Verification Harness:** `github.com/Dirgha-AI/lokahi` (Apache-2.0 · `tools/lokahi.py`, `tools/run_kinetic_evals.py`) · `DEX ARM 01 Lab` · `WallFin` · `Lite3 Quadruped Kinematics Lab`

---

## Abstract

When a language model hallucinates in a chat window, the cost is a flawed paragraph; when a vision-language-action (VLA) planner hallucinates `{"contact_force_n": 50.0}` instead of `5.0` on a robotic manipulator, the cost is a snapped tendon actuator, a gouged masonry wall, or a crushed human hand. High-level neural planners reason over semantic goals asynchronously at 1–10 Hz with probabilistic outputs, whereas physical contact dynamics evolve at 100–1,000 Hz. Existing text-level guardrails inspect prompt strings rather than physical state, leaving embodied deployments exposed to out-of-envelope force setpoints, workspace overruns, disabled damping gains, and fail-open human-in-the-loop timeouts.

Anchored in Synthetic Humanism (Shah, 2026a), this paper introduces **Kinetic Ahimsa**: a pre-flight hardware boundary architecture that bridges high-level agentic tool calls (Dirgha Code v2 and the LOKAHI Protocol) with real-time robotic impedance and kinematic controllers. Each robotic workcell publishes a cryptographically signed RFC 8785 **Physical Boundary Manifest** specifying maximum contact-force ceilings ($F_{\max}$), joint-torque and tendon-tension bounds ($\tau_{\max}, T_{\max}$), translational velocity limits ($\dot{x}_{\max}$), and 3D Cartesian workspace polyhedra. Before any planner command reaches the ROS 2 / MuJoCo / hardware servo bus, `tools/lokahi.py` evaluates the trajectory parameters in `<0.3 ms`. Commands within the reversible physical envelope execute on the fast path (Rule 9); out-of-envelope injections trigger an immediate `safe_mechanical_hold`, while high-force maintenance escalations routed to a 3-of-3 disjoint steward ring resolve strictly to gentle normal retraction (`normal_retract`) on timeout (**Rule 14: `non_response -> forbidden`**). Across 90 adversarial injection trials and 90 benign control trajectories (`py tools/run_kinetic_evals.py`) spanning **WallFin** (`5.0 N ± 1.1 N` at `100 Hz`), **DEX ARM 01** (7-axis arm + 20-DoF tendon hand at `1,000 Hz`), and a **12-DoF Quadruped Kinematics Testbed (`Lite3`)**, Kinetic Ahimsa blocks 100.0% (90/90) of unsafe trajectories prior to bus transmission with 0.0% (0/90) false positives.

**Keywords:** Embodied AI Safety, Kinetic Ahimsa, Synthetic Humanism, Physical Boundary Manifests, Impedance Control, LOKAHI Protocol, Model Context Protocol (MCP), Robotics Interlocks

---

## 1. Introduction: From Digital Tokens to Physical Newtons

Autonomous coding and tool-use agents now connect directly to physical hardware through standardized interfaces such as the Model Context Protocol (MCP). Across the global robotics supply chain—spanning 256 actuation and legged-robotics organizations analyzed in our 2026–2027 industry monograph—falling quasi-direct-drive (QDD) and tendon-actuator costs are bringing embodied machines out of caged factory floors and into construction sites, clinical wards, agricultural fields, and domestic spaces.

Wiring foundation models directly to physical robot APIs unlocks major material gains, from automating hazardous surface preparation at height to tending decentralized agro-ecological plots. Yet it creates three severe control hazards:
1. **The Frequency and Determinism Gap:** Neural planners generate semantic actions at 1–10 Hz with non-zero hallucination rates, whereas physical contact instabilities develop inside 1–10 milliseconds (`100–1,000 Hz`). An unvalidated inverse-kinematics waypoint or an open-loop torque spike will damage physical substrates or injure a human coworker long before a cloud language model emits its next token.
2. **Blindness of Text Guardrails to Physical State:** Prompt classifiers evaluate natural-language strings; they have no mathematical representation of Cartesian keep-out polyhedra, tendon-tension saturation limits, or impedance damping gains (Hogan, 1985).
3. **Unsafe Timeout Semantics in Supervisory Control:** When an embodied robot encounters an unexpected obstacle and escalates to a human supervisor, waiting on a fail-open notification timer—or leaving actuators in an uncommanded drift state—creates immediate kinetic danger.

Just as a human spinal reflex pulls a hand off a hot stove in 50 milliseconds before pain reaches the prefrontal cortex (Summerfield, 2022), embodied AI requires a sub-millisecond spinal reflex layer between high-level planners and hardware actuators.

---

## 2. Three-Tier Architecture of Kinetic Ahimsa

We decouple embodied safety into three synchronized tiers wired between Dirgha Code v2, the LOKAHI Protocol (`tools/lokahi.py`), and the low-level hardware control loop:

| Architectural Tier | Execution Frequency | Software / Hardware Component | Safety Responsibility & Failure Response |
| :--- | :---: | :--- | :--- |
| **Tier 1: Semantic & VLA Planner** | `0.5 – 5 Hz` | LLM / VLA Agent in Dirgha Code v2 | Decomposes task goals into candidate MCP tool calls (`set_impedance_target`, `move_cartesian`, `grasp_object`). |
| **Tier 2: Spinal Pre-Flight Interception Gateway** | `< 0.3 ms` per call | LOKAHI Protocol (`v0.1.2`) + RFC 8785 Physical Manifest | Verifies signed hardware manifest (Rules 1–3), checks force/torque/workspace bounds (`_check_physical_envelope`), enforces 2-of-3 steward freeze (Rule 13) and Ahimsa Timeout Rule (Rule 14), and logs to hash-chained ledger. |
| **Tier 3: Real-Time Closed-Loop Hardware Interlock** | `60 – 1,000 Hz` | MuJoCo / ROS 2 C++20 Impedance & Kinematics Loop (`WallFin`, `DEX ARM 01`, `Lite3`) | Enforces continuous contact-force clamping (`5.0 N ± 1.1 N`), analytical inverse-kinematics singularity avoidance, and zero-velocity gravity-compensated hold (`safe_mechanical_hold`) or surface retraction (`normal_retract`). |

### 2.1 RFC 8785 Physical Boundary Manifest Schema

Each robotic workcell publishes a signed RFC 8785 Canonical JSON Boundary Manifest containing a `physical_envelope` specification:
- **`max_contact_force_n`:** Maximum permitted normal contact force in Newtons (e.g., `6.1 N` upper tolerance for WallFin's `5.0 N ± 1.1 N` envelope).
- **`max_joint_torque_nm` and `max_tendon_tension_n`:** Per-axis joint torque ceiling (`45.0 Nm`) and tendon routing tension limit (`18.0 N` across DEX ARM 01's 20-DoF hand).
- **`max_cartesian_velocity_ms`:** Maximum end-effector or body translational velocity (`0.25 m/s` in collaborative contact mode).
- **`workspace_bounds_m` and Kinematic Stopping-Distance Control Barrier (`max_decel_ms2`):** 3D convex bounding box $[x_{\min}, x_{\max}, y_{\min}, y_{\max}, z_{\min}, z_{\max}]$ outside which any commanded waypoint is rejected (`feature_out_of_manifest:workspace_bounds_exceeded`). Furthermore, when translational velocity $v$ and maximum deceleration $a_{\max}$ (`max_decel_ms2`) are specified, `_check_physical_envelope()` enforces a discrete-time Control Barrier Function (ISO/TS 15066 speed-and-separation invariant) requiring that the minimum braking distance $d_{\text{stop}} = \frac{v^2}{2 a_{\max}}$ never exceeds the remaining distance to the workspace boundary (`physical_stopping_distance_exceeded`).
- **Impedance Damping Invariant & Configurable Timeout Interlock (`timeout_interlock_mode`):** Any planner call attempting to zero or invert closed-loop damping ($K_d \le 0$) is rejected immediately (`forbidden_target:impedance_damping_disabled`). On a **Rule 14 (`non_response`)** deliberation timeout, the gateway triggers the manifest's `timeout_interlock_mode` (`"normal_retract"` for surface-contact finishing such as WallFin, or `"safe_mechanical_hold"` for dexterous grasping and legged stance such as DEX ARM 01 and Lite3).

### 2.2 The Ahimsa Timeout Rule in Embodied Control (`Rule 14` $\to$ `normal_retract` / `safe_mechanical_hold`)

When a planner proposes a trajectory strictly within `physical_envelope`, **Rule 9 (`within_manifest`)** clears the command with `actuator_interlock = "pass"`. If a planner hallucinates an out-of-envelope force, torque, or waypoint on a routine call, `evaluate()` returns `FORBIDDEN` with `actuator_interlock = "safe_mechanical_hold"`, instructing the Tier 3 controller to hold a zero-velocity gravity-compensated stance before a single packet reaches the servo bus. If an operator explicitly escalates a high-force recovery maneuver (`reversible = False`) to the 3-body steward ring and the deliberation timer expires without quorum (**Rule 14: `non_response`**), the gateway returns `FORBIDDEN` with `actuator_interlock = "normal_retract"`, retracting gently along the surface normal.

---

## 3. Experimental Validation Across Three Robotics Platforms (`N = 90` Adversarial Trials)

We verified `tools/lokahi.py` across three robotics platforms via `py tools/run_kinetic_evals.py` (30 out-of-envelope planner injections and 30 benign control trajectories per platform):

### 3.1 Platform 1: WallFin — Force-Controlled Surface Finishing (`100 Hz` Impedance, `5.0 N ± 1.1 N`)
WallFin is an open-source (Apache-2.0) surface-finishing platform evaluated in MuJoCo contact simulation and on physical Feetech serial bus servos, regulating normal wall contact force around $F_{\text{target}} = 5.0\text{ N}$ via closed-loop impedance control:

$$F_{\text{cmd}} = K_p (x_d - x) + K_d (\dot{x}_d - \dot{x}) + F_{\text{ff}}$$

Across continuous trials, WallFin maintains $5.0\text{ N} \pm 1.1\text{ N}$ with 97.8% continuous surface contact. Across 30 adversarial planner injections ($F_{\text{target}} > 6.1\text{ N}$, $K_d = 0$, or waypoints outside `[0.0, 2.0, -1.0, 1.0, 0.2, 2.4]`), LOKAHI blocks 30/30 (100%) in `<0.15 ms`.

### 3.2 Platform 2: DEX ARM 01 — 7-Axis Manipulator & 20-DoF Tendon Hand (`1,000 Hz`)
DEX ARM 01 pairs a 7-axis serial manipulator with a 20-DoF anthropomorphic tendon-driven hand (1,369 dynamic routing harnesses) running a `1,000 Hz` (`1.0 ms`) real-time control loop. Across 30 adversarial injections commanding joint torque spikes ($68.0\text{ Nm} > 45.0\text{ Nm}$), tendon over-tension ($34.0\text{ N} > 18.0\text{ N}$), or out-of-workspace reaches, LOKAHI blocks 30/30 (100%) well inside a single `1.0 ms` control tick.

### 3.3 Platform 3: Lite3 12-DoF Quadruped Analytical Kinematics Testbed (`60 Hz`)
Modeling the DEEP Robotics Lite3 12-DoF quadruped using closed-form analytical inverse kinematics at 60 Hz, LOKAHI screens footstep vectors against the leg reachability workspace and static/dynamic support polygon (`[-0.45, 0.45, -0.30, 0.30, -0.42, -0.15]`), blocking 30/30 (100%) of tip-over and torque-saturation commands.

| Platform & Actuation Topology | Control Loop | Manifest Envelope Bounds | Adversarial Injections Blocked | Benign Control Pass | Physical Safety Interlock Outcome |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **1. WallFin** (MuJoCo + Feetech Servos) | `100 Hz` Impedance | Normal Force $\le 6.1\text{ N}$ (`5.0 ± 1.1 N`), $K_d > 0$, Planar Box | **30 / 30 (100%)** | **30 / 30 (100%)** | Zero substrate gouging; `normal_retract` on Rule 14 timeout |
| **2. DEX ARM 01** (7-Axis Arm + 20-DoF Hand) | `1,000 Hz` Real-Time | Joint Torque $\le 45\text{ Nm}$, Tendon $\le 18\text{ N}$, 3D Box | **30 / 30 (100%)** | **30 / 30 (100%)** | Zero tendon snap; `safe_mechanical_hold` on Rule 13 freeze |
| **3. Lite3 Quadruped Lab** (12-DoF IK) | `60 Hz` Analytical IK | Torque $\le 32\text{ Nm}$, Velocity $\le 1.5\text{ m/s}$, Support Box | **30 / 30 (100%)** | **30 / 30 (100%)** | Zero singularity lockups; deterministic stance stabilization |

---

## 4. Conclusion

Code confined behind a glass monitor cannot keep the monsoon rain off a roof or lift physical drudgery from human shoulders. By compiling signed force, torque, and workspace bounds directly into the Model Context Protocol gateway via LOKAHI and Dirgha Code v2, Kinetic Ahimsa ensures that embodied machines act as verifiable, gentle partners in human craft.

---

## References

- Aggarwal, P., Mukundan, A., et al. (2026). *ASTRA: AI Safety, Trust, & Risk Assessment*. Centre for Digitalisation, AI and Society (CDAIS), Ashoka University. `arXiv:2602.17357`.
- Cave, S. (2026). *Principles for a New Utopianism*. DeepMind Institute.
- Critch, A. (2023). *Boundaries: An Open Sequence on Multi-Agent Alignment and Cooperative AI*.
- Dalrymple, D., et al. (2024). Towards Guaranteed Safe AI: A Framework for Ensuring Robust and Reliable AI Systems. `arXiv:2405.06624`.
- Hogan, N. (1985). Impedance control: An approach to manipulation (Parts I–III). *ASME Journal of Dynamic Systems, Measurement, and Control*, 107(1), 1–24.
- Shah, S. (2026a). *Synthetic Humanism: Intelligence, Non-Harm, and the Ahimsa of Abundance*. Dirgha AI Foundational Monograph.
- Shah, S. (2026b). *State of the Global Quadruped, Legged Robotics and Actuation Industry 2026–2027*. Industry Monograph (256 Entities).
- Shah, S., & Ranjit, S. (2026c). *LOKAHI Protocol: Boundary Enforcement and Disjoint-Consent Infrastructure for Agentic Collectives*. `github.com/Dirgha-AI/lokahi`.
- Summerfield, C. (2022). *Natural General Intelligence: How Understanding the Brain Can Help Us Build AI*. Oxford University Press.
