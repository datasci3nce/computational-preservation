# Open research questions and proposed prospective tests

These are **future proposals, not executed studies**.

## Primary: do causal dynamics improve out-of-sample preservation forecasts?

**Question.** Can a frozen dynamical diagnosis predict whether a parameter edit or merge will preserve future delayed behavior *more reliably than short-horizon behavioral checks*?

**Design.** Train multiple independent recurrent model organisms to a strict predefined qualification rule on all cue classes and a long horizon. Predefine held-out cue banks, horizons, noise shifts and intervention families. Split by independently trained model (not by pair, trajectory or lambda), so no parent appears in both development and test pools.

**Before test data:** choose the diagnostic features and predictor; the evaluation threshold, metrics, and missing-value/censoring rules; the implementation hash; and the following baselines: native short-horizon task accuracy, parameter-space distance after valid alignment, activation similarity, and equal-compute behavioral or gradient repair screening.

**After freezing:** predict unseen model outcomes and previously unseen interventions (binary and strict three-way separately), report calibrated probability/error/decision utility, and compare to baselines with model-clustered uncertainty. A diagnostic that cannot beat simpler screening **fails the primary claim**.

## Focused NCA verification gates

1. Recover checkpoints and original experiment code; reproduce the augmented fold \(\lambda_*\), critical vectors, and map-derivative \(a,b\) values.
2. Regenerate local passage results at the explicitly chosen \(w=0.10\) directly from original trajectory arrays, with all nine condition labels and censoring rules.
3. Reproduce equal-norm task-gradient and fold-directed modifications, higher-noise and neutral-cue failures, and neighbor-forcing alternatives.
4. Decompose the actual \(W_{in}\) versus \(b_h\) differences along the existing restricted path, including interactions; do not relabel the path parent-to-parent.
5. Only then precommit a test on a new qualified NCA, rather than selecting another fold after seeing all failures.

## Separate ANN skill-composition gate

Recover a correctly versioned executable model and evaluation protocol, or train a *new*, clearly identified competent pair of Homing/Exploration (and possibly Obstacle Avoidance) specialists. Require reliable fresh-bank target reaching, meaningful movement and collision controls before attempting to remove Exploration while preserving Homing. Compare all 16 coalitions for the original four-hidden-unit architecture, ordinary sensitivity and speed/readout alternatives. Treat negative qualification as a stop condition.

## Separate causal-model-discovery gate

A genuine observation-only discovery tool must have **no access** to weights, model Jacobians or hidden ground-truth causes when choosing its interventions. It should maintain multiple candidate explanations, choose interventions using a specified scoring rule and predict effects on a blind held-out family. The archived teacher-output regressions and fold-sensitivity calculations do not meet this definition.

## Stop rules and research reporting

- Do not pursue a general repair-method claim when an equal-budget behavioral baseline outperforms the proposed selector.
- Do not broaden binary recall into three-way memory or 512-step competence into long-horizon competence.
- Do not claim an essential neuron or edge when a fixed forcing/bias alternative can reproduce the outcome.
- Do not use dependent repeated bank draws to substitute for independent model replication.
- When a hypothesis fails, freeze the failure, revise the **next** prospective test, and preserve which conditions were selected post hoc.
