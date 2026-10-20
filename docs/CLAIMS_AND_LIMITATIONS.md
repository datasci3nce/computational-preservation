# Claims, evidence status, and limitations

**Source of record:** [frozen checkpoint](../records/2026-10-18/FREEZE_20261018.md), [existing claim register](../records/2026-10-18/CLAIM_REGISTER.csv), [NCA evidence audit](../paper/nca_fold_case_study/EVIDENCE_REGISTER.md). Numerical values are transcriptions of previously reported experiments, **not independently recomputed in this repository**.

## Statement discipline

A **supported observation** reports a defined measured result. An **explanation** links a mathematical or causal hypothesis to observed trajectories or interventions. A **prospective method claim** would require a frozen rule that predicts unseen interventions or models better than explicit simpler baselines. Do not promote one class to another without new evidence.

| Claim | Evidence and independence | Safe interpretation | Disallowed generalization |
|---|---|---|---|
| Exact ANN/GRU permutations and NCA global \(O(2)\) preserve input-output mapping | Mathematically exact transformations with matching tensor transport; examples numerically checked | Coordinate controls are mandatory for fair comparisons | New symmetry theorem; local gauge/physical rotation symmetry; same mechanism across independently trained models |
| NCA normal form predicts local passage | One selected NCA and path; nine correlated settings; \(w=0.10\), ~0.22 decision MAE | Quantitative within-case dynamics | Whole forgetting lifetime predicted with that error; independently replicated law |
| NCA fold-directed bias changes retention | Selected case; within-model trajectory histories | Specific intervention influences slow regime and binary signed recall | Unique repair; three-way accuracy restored; superiority over gradients |
| Neighbor coupling alters fold | Selected NCA; predicted/solved coupling shifts | Cellular messages influence dynamical geometry | Cell 2→1 uniquely transports cue memory; forcing control contradicts exclusivity |
| GRU same-task merging harms delayed recall | 21/96 qualified, 210 dependent pairs | Competent recurrent models can average into impaired models | 210 independent models; multi-skill transfer; general conclusion about LLMs |
| GRU V6 projected candidate restoration recovers donor sign | Selected GRU; clamp; held-out 40 histories per sign | A conditional causal contribution over a specified interval | One natural, unique memory neuron; unmodified recipient fully repaired |
| GRU early mechanistic repair selector failed | Previously frozen selection comparison | Mechanistic diagnostic did not beat behavioral screen under that protocol | All mechanistic diagnosis is useless |
| Late teacher outputs help some distilled GRUs | Fresh pair: 53/64 at t512, 7/64 at t1024 | Short horizon does not establish durable memory | Durable identity of mechanism; universally optimal late supervision |
| NCA output-distillation updates shift tracked fold | One selected NCA; first-order held update directions compared with subsequent solves | Local forward prediction of dynamical effects from known trained update directions | Inverse recovery of mechanism or weights from behavior alone |
| Planted GRU faults can share strict score | Constructed input/readout/recurrent changes to qualified GRUs | Same score can have distinguishable causes | Frozen blind causal discovery or universal repair |
| ANN distillation preserves light-responsive steering | Source-compatible headless pilot; 1/8 goal success for teacher and student | Specific fixed-sensor causal action sensitivity | Competent Homing preserved, Exploration suppressed, original thesis merged checkpoint reproduced |

## Selection and dependence

- **Selected NCA:** The main checkpoint pair/path and diagnostic windows were inspected repeatedly. New cue histories are not independent neural-network replication. Multiple selected windows should not be treated as preregistered independent tests.
- **GRU pairs:** The 210 model pairings reuse the same 21 qualified parents. Pair-level binomial confidence intervals assuming 210 independent trials would be inappropriate.
- **Exploratory versus frozen:** Some fold prediction comparisons were frozen before nonlinear solving or new cue-bank evaluations. That is a narrower kind of precommitment than preregistration before choosing the network or fold. The freeze is dated 18 October 2026, not before all experiments.
- **Three-way versus binary:** Positive/negative signed-cue correctness excludes the neutral class. Strong two-way performance must never be described as restoring strict three-way memory.
- **Time units:** The studied NCA has three internal microsteps per external decision. Local passage errors and horizons quoted in the technical note are measured in **external decisions**.
- **Noise and horizon:** Define training/evaluation noise, cue history, batch, and delay for each claim; 512-step performance does not imply 1024-step performance.
- **Checkpoint identity:** The archived thesis ANN models have architecture and source-version mismatches. This repo makes no exact Figure 7.x reproduction claim.

## A falsifiable standard for stronger claims

A future mechanistic-preservation diagnostic should be selected on development data, then tested on **new qualified models** and **previously unseen interventions**. It should predict future task outcomes and beat fixed comparators (parameter distance, activation distance, short-horizon task score, direct behavioral screening, equal-cost task gradients, and simple bias/readout fixes). A statistically meaningful failure is a legitimate research outcome; retrospectively adjusting the inclusion criteria is not.

## Missing verification before public scientific citation

The old experiment ZIPs, executable code, raw arrays, hashes for each original checkpoint, the final solver environment, original coupling figure and all exact training/reproduction instructions still need to be recovered. The bundled *editorial* source hashes verify only the documents copied into this repository. Consult the [manifests](../reproducibility/README.md) for the explicit gaps.
