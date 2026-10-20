# Prospective research direction — Iliad Fellowship (January 2027)

**Proposed title:** Causal Dynamics of Computational Preservation Under Neural-Network Modification

**Applicant:** Kishore Kumar Mariappan · independent researcher · M.Sc. Robotics and Autonomous Systems

**Status:** Proposal for future work; not an accepted fellowship, preregistration, or empirical result.

## The scientific question

Suppose two recurrent networks implement a task successfully but their aligned parameter average, a distillation update, or a fine-tuning step loses that capability at a longer horizon. Can a small causal/dynamical model predict *which modification fails, when, and under which intervention* more reliably than inexpensive behavioral tests?

This is a question about the persistence of computation rather than only its currently measured accuracy. A possible safety application is auditing whether post-training modification preserves computations needed for long-horizon behavioral reliability. That safety application is **not** established by the archive.

## Why this question is tractable

For a recurrent model with state transition $h_{t+1}=F_{\theta}(h_t,u_t)$ and readout $y_t=g_{\theta}(h_t)$, local derivatives and causal interventions allow competing explanations of failures to be tested:

- **Representation/readout:** relevant state distinctions survive but the native readout fails.
- **Maintenance:** task-relevant distinctions shrink, rotate, or leave reachable computational regimes.
- **Modification interactions:** several changed parameter blocks jointly disrupt a previously functioning computation.

The diagnostic must make **prospective, falsifiable** predictions. A descriptive phase portrait or a significant probe is not enough.

## Evidence that motivates the proposal

The accompanying *selected-case* NCA technical draft examines a restricted path between two merge-derived variants and reports a saddle-node fold near $\lambda_*=0.20091324$, with derivative-based predictions of slow-region passage. It does **not** show the fold is general, or that the two parent networks were both strictly qualified. Separate qualified-GRU experiments show capability loss following model averaging, while earlier mechanistic selectors failed to beat a simpler behavioral screen. These failures are central motivations, not omissions.

## Three-month research plan

**Month 1 — Qualification and causal model organisms.** Reconstruct exact executable baselines where available and train a prospective cohort of independently seeded, strictly qualified recurrent systems. Freeze qualification on positive, negative, and neutral/no-cue conditions at a specified long horizon. Predefine modification families (alignment plus averaging, limited distillation updates, and restricted recurrent/readout edits). Keep model identities disjoint across development and test. Stop if too few competent systems are obtained.

**Month 2 — Mechanistic predictions before outcomes.** On development models, fit a compact family of competing diagnostics: short-horizon behavior, state decodability, intervention response, task-relevant Jacobian propagation, and fixed-point/slow-region analysis where justified. Predict **future output differences and strict success**, not merely latent geometry. Freeze prediction rules, intervention budgets, and thresholds before accessing test outcomes. Compare with parameter distance after exact symmetry correction, activation similarity, direct behavioral screening, and simple equal-budget gradient/readout adjustments.

**Month 3 — Blind testing, causal challenge, and theory audit.** Evaluate forecasts on unseen trained models, unseen edit magnitudes, new cue schedules, and horizon/noise shifts. Report calibration, mean prediction error, accuracy of selecting better interventions, and whether any theoretical reduction survives targeted counterexamples. Cluster uncertainty by independently trained model, not by correlated paired merges. Disclose state/weight information after prediction only for mechanism auditing if using an observation-only predictor.

## Success and failure criteria

**Success** requires a reproducible, calibrated dynamical method that improves prediction of out-of-sample **behavioral consequences** or correct intervention selection over predeclared simple baselines at comparable cost. Its scope may remain a small model-organism family.

**Informative failure** means the mechanistic diagnostics explain selected cases but fail blind generalization or add no value beyond behavior. In that case the result constrains mechanistic-preservation claims and motivates a narrower causal account rather than a new post-hoc method.

## Relevant background and boundaries

The research combines control theory, state estimation, local bifurcation analysis, causal intervention, recurrent nets, and post-training modification. Established prior art includes Sussillo and Barak on RNN dynamics, Driscoll et al. on dynamical motifs, and Git Re-Basin on parameter symmetries. The proposed novelty is **not** identifying attractors or combining mathematics; it is a held-out prediction and falsification protocol for computation after modification.

**Current reproducibility status:** The research archive includes frozen evidence notes and integrity checks, not the original model checkpoints, training code, or raw arrays. The technical manuscript should not be cited as peer reviewed or fully replicated.
