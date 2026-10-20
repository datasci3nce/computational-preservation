# Experimental lineage: from robotic skill merging to causal dynamics

**Scope:** Descriptive genealogy of completed and exploratory studies up to 18 October 2026. The frozen [source record](../records/2026-10-18/FREEZE_20261018.md) and [NCA research note](../paper/nca_fold_case_study/RESEARCH_NOTE.md) determine claim boundaries. This history is not an independently validated dataset or a sequence of preregistered experiments.

## The organising problem

> What survives a change to a learned network, and can we explain or predict the change in future behavior?

Three levels recur: weights, internal state-transition structure, and native behavior. We also distinguish **same-score agreement**, **coordinate equivalence**, and **agreement under specified interventions**. An experiment about one is not automatically evidence about the others.

### A — Thesis ANN: integration of complementary robot skills

**Question.** Can neuron alignment, weight averaging, and neuron-specific pruning combine four independently evolved specialists—Homing, Exploration, Obstacle Avoidance and Wall-Following—without destroying useful composite behavior?

**Approach.** Four-hidden-unit feed-forward controllers; LAP/Hungarian alignment and pruning based on individual-task neuron contributions. Selected thesis results suggested composite performance could be destroyed by neuron removal despite a useful original merge (“synergy destruction”).

**Correction.** A later source and evaluator audit could not reconcile the thesis prose, historical checkpoints and code into the exact reported result. Executable archived weights use eight sensory inputs and 48 weights rather than the thesis prose's seven inputs/36 weights. Archived Homing succeeded on **1/8** pilot starts, with **5/8** crashes, under a headless simulator shim. The original composite pruning contrast has **not** been independently reproduced from these assets.

**Lesson.** A selected favorable merge and failure after pruning are not enough to identify a reusable compositional mechanism. Qualification and provenance come first.

### B — Small NCA: geometry, perturbations and task loss

**Question.** Can nearly equal loss conceal different recurrent sensitivity?

**Approach.** Exact symmetry checks, finite-time Jacobian products \(J_{T-1}\cdots J_0\), coalition interventions, loss Hessians, state sensitivity.

**Reported selected comparison.** Task losses **0.0117 vs 0.0131**, but finite-time perturbation amplification **0.0000794 vs 197.77**. This is a striking within-comparison discrepancy, not broad empirical evidence that Jacobian amplification predicts safety-relevant outcomes.

**Falsification.** A later OOD audit did not find robust superiority over simpler task-loss predictors for predicting different outcome types. Perturbation amplification most directly characterises the perturbations it measures.

### C — Exact symmetries: avoid mistaking coordinates for mechanisms

**Question.** Which transformations leave behavior literally unchanged?

**Approach.** Parameter-consistent hidden permutations for feed-forward ANNs and GRUs; a global hidden-channel \(O(2)\) transformation for the specified seven-cell NCA. Symmetry orbits, interpolation directions and basis-invariant comparisons were examined.

**Result.** Coordinate changes can move weights and activations while preserving function. Inconsistent averaging across coordinate representatives can break behavior.

**Boundary.** The NCA \(O(2)\) is a *global basis symmetry*, **not** physical rotation equivariance or independent local gauge transformations. GRU permutations do not justify arbitrary orthogonal GRU changes. None of these controls proves independently trained models share a mechanism.

### D — Embodied NCA: qualification before explanation

**Question.** Can local recurrent interactions be connected to actual navigation behavior?

**System.** Seven spatial cells, two hidden channels per cell, shared recurrence, pooled steering/speed output.

**Negative findings.** Reward/evaluator mismatch, inconsistent robot-skill qualification, simple speed reduction as a plausible collision improvement, limited evidence of persistent history in some controllers, and insufficient confirmation for specialist routing and macrostate claims.

**Lesson.** Before interpreting a neural change as obstacle reasoning or memory, rule out readout calibration, motion reduction, checkpoint selection and evaluator artifacts.

### E — NCA delayed memory: does a state store useful information?

**Question.** Can cue encoding, state maintenance and native readout be separated?

**Approach.** Delayed signed cue tasks, hidden-state transplants, decodability probes, and attempted causal macrostates.

**Result and boundary.** Cue-dependent signals and selected transplant effects appeared, but independent NCA cohorts were not consistently strictly qualified, especially for neutral cues and long horizons. Decodability did not establish native usability; compact causal macrostates failed sufficiency tests.

### F — Selected NCA fold: local mechanistic explanation

**Question.** Does a fold-associated slow region explain later cue loss in a specific merge-derived recurrent network?

**System.** One previously selected NCA seed-4/5 case. The restricted \(F\to S\) path changes input weights and hidden bias between two *merged* variants—not independently competent parents. Three internal microsteps make one external decision.

**Main result.** Neutral-input fixed-point continuation gave a tracked fold \(\lambda_*=0.20091324\). A derivative-derived normal form predicted passage through a fixed window (\(w=0.10\)) with about **0.22-decision mean absolute discrepancy** across nine correlated path conditions. That is a **local passage** result, not complete lifetime prediction. Parameter/state/timing and coupling changes altered retention consistently with the identified slow regime.

**Failures and counterchecks.** Strict three-way neutral-cue-inclusive performance remained broken. Higher input noise weakened robustness. Ordinary gradient edits matched or beat fold-based repair in tested conditions. The case and path were heavily inspected; extra histories are not independent model replications.

**Reference.** [Original technical note](../paper/nca_fold_case_study/RESEARCH_NOTE.md); [evidence register](../paper/nca_fold_case_study/EVIDENCE_REGISTER.md).

### G — Independent GRU merging: capability damage on qualified parents

**Question.** Can parameter-averaged recurrent networks fail even when both parents qualify?

**Approach.** A cohort of 96 trained GRUs, 21 qualifying at decision 512, and 210 dependent pairs. Compare raw and permutation-aligned weight averages against output ensembles and delayed-memory qualification.

**Result.** Real same-task competence can be destroyed by parameter averaging; output ensembles often preserve the original task better. But pairing the same trained parents many times does not create 210 independent replications.

**Negative finding.** A frozen early mechanistic repair-choice rule failed to beat a simpler behavioral screen. A predictor of dynamics need not be a useful repair selector.

### H — GRU V1–V6: temporally localized causal contributions

**Question.** Which learned candidate-state interactions contribute to delayed signed output?

**Approach.** Output-null hidden perturbations, state propagation, artificial candidate-activation clamps, rank-one restoration and interval ablations.

**Selected V6 result.** Under a particular clamp and readout, restoring one projected candidate-state contribution yielded correct donor sign in **40/40 held-out histories per signed direction**. Orthogonal/shorter-window controls were negative on the specified comparison. Later controls were partly post-hoc.

**Boundary.** Conditional rescue is not evidence of a uniquely localised natural memory neuron, the sole causal route to retention, or native three-way repair. This is **not** a GRU replication of the NCA fold.

### I — Model-discovery motivation: prospective causal prediction

**Question.** Can experiments identify mechanisms sufficiently to forecast genuinely new interventions?

**Work performed.** Some hidden-geometry/forecasting prototypes and output-regression models; dynamical features often failed to improve repair choice.

**Boundary.** There is no implemented observation-only Bayesian causal world model, no blind mechanism search benchmark and no validated information-gain intervention selector here. This is a **future research target**.

### J — Output-supervised distillation: behavior, updates and recurrence

**Question.** Can a student learn delayed behavior by imitating output-ensemble trajectories, and can its *actual* updates be analyzed mechanistically?

**GRU results.** A selected three-model ensemble and late-supervision controls showed strong dependence on teacher-label timing. In one fresh qualified pair, early 64 labels gave **0/64** at 512 and 1024; late 64 gave **53/64** at 512, **7/64** at 1024; dense 256 gave **34/64** and **1/64**. These are specific training budgets/model pairs, not a claim that later supervision is universally optimal.

**NCA results.** In the *same selected NCA*, learning from a previously bias-repaired binary-only teacher produced controlled update directions. First-order predictions of the tracked fold location at 10% update closely matched new nonlinear solves: input+bias **0.175609 predicted vs 0.175534 solved**, recurrence **0.189535 vs 0.189469**, full-t128 **0.183086 vs 0.183100**. All compared students still had **0/48 strict three-way recall** in the specified bank. Prediction used knowledge of the trained update direction and known critical vectors; it was *not* inference of weights from output sequences alone.

### K — OOD and indistinguishable behavioral failures

**Question.** Can readout, encoding and recurrent decay faults produce the same strict score?

**Result.** Planted readout bias, input-zero and recurrent-weight scaling each yielded strict t512 failure under specified conditions but differed in hidden cue information and effects of targeted probes. A precommitted general replacement-readout target of at least 90% **failed** (85.9% on two held-out models), and it harmed healthy models. Restricted post-hoc scalar bias calibration fixed the known planted fault; it is not a blind repair method.

**Boundary.** Separately hand-engineered equal-early-output, divergent-future systems demonstrate a logical identifiability counterexample, not discovered mechanisms in trained models.

### L — Return to original ANN Homing behavior

**Question.** Can a distilled ANN preserve a meaningful light-to-steering contribution while some other task is removed?

**Result.** An action student imitated fixed-sensor steering; its light sensitivity was about **0.1785**, and selected unit-3 ablation reduced that to **0.0114**. But teacher and student both reached targets on only **1/8** pilot starts and crashed on **5/8**. Exploration was not selectively suppressed.

**Boundary.** This is a chosen-basis light-responsive action contribution, **not** robust Homing, task decomposition, or a symmetry-invariant neuron.

## Synthesis and unresolved challenge

Across the studies we have: (i) known exact coordinate controls, (ii) bounded dynamical and causal case studies, and (iii) negative prospective selection/qualification findings. There is **no established general method** outperforming simple behavioral baselines on independent unseen models.

The next falsifiable question is whether a *frozen* mechanistic predictor adds out-of-sample value to parameter similarity and short-horizon behavioral testing on truly qualified independently trained recurrent networks. See [test plan](OPEN_QUESTIONS.md).
