# From Parameter Alignment to Memory Dynamics

### An experimental investigation of merge-derived recurrent networks

**Exploratory research note · 18 October 2026 · Work in progress**  
**Scope:** Selected neural cellular automaton (NCA) dynamical case study, with separate supporting GRU experiments. This document records completed experiments and their limitations; it does **not** claim an independently validated repair algorithm or completed composition of complementary robot skills.

## Abstract

Parameter alignment makes neural-network averaging more meaningful, but a valid alignment does not imply preservation of learned computations. We investigate this distinction in small recurrent models using exact coordinate controls, delayed-cue tasks, dynamical analysis, and causal interventions. Our central case is a previously selected seven-cell NCA. Along a specified parameter path between an input-aligned and an activation-aligned **merged model**, the network changes its ability to retain a binary cue. We identify a saddle-node fold in its neutral-input recurrent map; natural cue-conditioned trajectories traverse the associated slow region. A local normal form derived from map derivatives predicts passage times without fitting those durations. Perturbations along a critical dynamical direction shift the tracked fold and alter long-horizon signed recall. Subsequent tests show that neighbor coupling also shifts the fold and that a successful directed edge cut can be mimicked by cue-independent forcing, arguing against a unique memory-message interpretation. Negative findings delimit the account: neutral-cue behavior is not recovered, increased noise degrades retention, ordinary short-horizon gradients repair as well as the fold-derived direction, and early fold features fail to improve out-of-distribution failure ranking. A separate GRU intervention study illustrates how delayed output effects can depend on a restricted candidate-state contribution, but does not replicate the NCA mechanism. Our contribution is a reproducible **within-system causal and dynamical case study**, not a general theorem or method for model merging.

## 1. The question, and what is actually being compared

**Question:** When model parameters are aligned and combined, how can the resulting recurrent dynamics alter the persistence and usability of task-relevant information?

These experiments emerged from a limitation of an earlier four-hidden-unit, feed-forward robot-controller study: LAP alignment improved selected composite behavior, while task-specific neuron pruning subsequently destroyed it. That observation suggested that *matching units* and *ranking unit importance* need not identify the computation that supports a combined behavior. The present experiments use **different, recurrent synthetic-memory model organisms** to make this question mathematically tractable. They do not themselves merge homing and obstacle-avoidance skills.

Three distinct phenomena must not be collapsed into a single “memory failure”:

1. **Representation:** task information can be present in hidden states and decodable by an auxiliary probe.
2. **Dynamics:** the recurrent update may preserve, transform, or eventually eliminate the distinctions between cue-conditioned trajectories.
3. **Behavior:** the network's own readout may or may not produce the correct output, even while a probe can recover information.

A related distinction concerns coordinates. Exact permutations in the GRU and global hidden-channel \(O(2)\) changes in the NCA preserve a model's input-output function when the parameters are transported consistently. They **do not** guarantee that averaging *different* models preserves the learned computation.

### Experimental provenance

The main NCA has seven spatial cells, two hidden channels per cell, and three internal microsteps per external decision. We denote the input-aligned midpoint by \(F\) and the activation-aligned midpoint by \(S\). The studied path is not parent-to-parent interpolation. It modifies **only** \(W_{\mathrm{in}}\) and \(b_h\) between two merger-derived variants, leaving the other blocks fixed:

\[
\theta(\lambda) = \bigl(W_{\mathrm{in}}^{F}+\lambda (W_{\mathrm{in}}^{S}-W_{\mathrm{in}}^{F}),\; b_h^{F}+\lambda(b_h^{S}-b_h^{F}),\;\text{fixed remaining blocks}\bigr).
\]

The original NCA parents were **not both robustly qualified** for strict 512-step three-way (negative/no-cue/positive) memory. The reported restoration is of **binary signed-cue behavior**, not recovery of a fully qualified three-class capability lost to merging. The selected checkpoint pair, path, and fold have been studied repeatedly; new input-noise histories are *within-model* checks, not independent-model replications.

## 2. Experimental lineage: what each result changed

The sequence below is ordered by the logical experiments, not by the personal history of the project. “Next question” records why the following experiment was necessary.

| Stage | Intervention / observation | What it established | What remained unresolved, motivating the next stage |
|---|---|---|---|
| **A. Representation alignment** | Exact GRU hidden-unit permutations preserve function, while misaligned averages of equivalent copies fail on the tested bank (40 correlated self-merges); undoing the permutation restores all 40. | Coordinate matching is necessary for interpreting weight averaging. This is a known Git Re-Basin phenomenon, not new theory. | Valid alignment says little about preservation of **recurrent computation** after averaging inequivalent models. |
| **B. Readout versus recurrence** | Auxiliary readouts and hidden-state swaps reveal cases where native output fails despite recoverable cue information. Other models lose cue separation at long delays. | Output failure, state information, and dynamical persistence can differ. | What dynamical defect produces delayed loss, rather than merely incorrect output calibration? |
| **C. NCA fold diagnosis** | A fixed-point saddle-node is tracked along the specified \(F\)-to-\(S\) path; natural cue trajectories traverse its slow region. | A specific local dynamical structure is associated with the selected delayed-memory failure. | Does it quantitatively predict transient timing, rather than simply correlate with performance? |
| **D. Quantitative prediction** | A derivative-derived local normal form predicts critical-region passage times; total operational memory lifetime exhibits near-fold scaling. | Strong within-system quantitative account of the observed *local bottleneck*. | Does perturbing this structure causally change actual retention? |
| **E. Parameter, state, and timing interventions** | Critical-bias edits move the tracked fold; critical-mode state shifts advance/delay failure; changing continuation dynamics at different times changes recall. | The proposed slow mode is intervention-relevant for the selected system. | Is it a superior repair strategy? Does it recover neutral behavior or generalize under noise? |
| **F. Falsifying controls** | Short-horizon task gradients match fold-derived repair; no-cue fails; stronger noise lowers success; early fold-based features fail OOD ranking. | Mechanistic explanation does not automatically yield better optimization or early warning. | Does the actual **cellular coupling** contribute, or are we only describing an opaque global recurrence? |
| **G. Neighbor-coupling audit** | Adjoint sensitivities predict coupling-induced fold shifts; directed cuts restore signed responses, but other cuts and fixed cue-independent forcing can do the same. | Cellular coupling affects the tracked dynamics; the data do **not** isolate a uniquely memory-carrying edge. | How do the *actual alignment-induced parameter differences* produce this dynamical change across new qualified merges? |
| **Separate GRU branch** | A selected six-unit GRU's readout-null state swap becomes visible after hundreds of steps; a rank-one candidate-activation contribution conditionally restores the signed effect under a clamp. | Causally effective time- and direction-selective recurrent contribution in another architecture. | It is not an independent replication of the fold and does not yet explain natural merge failure end-to-end. |

## 3. The NCA dynamical result

Let \(T_{\theta}(h;u_0)\) be the **full three-microstep** recurrent decision map under neutral input \(u_0\), and define

\[
G(h,\lambda)=T_{\theta(\lambda)}(h;u_0)-h.
\]

At a tracked saddle-node fold \((h_*,\lambda_*)\), \(G=0\) and \(D_hG\) has a null direction. The refined numerical fold was near \(\lambda_*=0.20091324\). Using the corresponding left and right critical vectors, local derivatives give a reduced equation of the form

\[
 z_{t+1}-z_t\approx a(\lambda-\lambda_*)+bz_t^2,
 \quad a\approx-0.05493465,\quad b\approx0.01169046.
\]

For \(A=a(\lambda-\lambda_*)>0\), the established saddle-node *ghost* approximation predicts the time spent crossing the specified critical-coordinate window \([-w,w]\):

\[
T_{\mathrm{pass}}(w,\lambda) \approx \frac{2}{\sqrt{Ab}}\arctan\left(w\sqrt{\frac{b}{A}}\right).
\]

These coefficients were computed from the map, **not fitted to passage durations**. For \(w=0.10\), predicted-vs-measured local crossing times had a mean absolute discrepancy of approximately **0.22 decisions** over nine interpolation conditions. Broader windows increase error: 0.12 at \(w=0.05\), 0.70 at \(w=0.20\), and 2.20 at \(w=0.30\). This is a local prediction, **not** a 0.22-step prediction of total memory lifetime; comparisons among windows were exploratory.

Separately, the operational lifetime—first time after step 16 when signed hidden-state separation falls below 25% of its step-16 value—scaled descriptively as \((\lambda_*-\lambda)^{-0.49364}\) over eight correlated uncensored points (\(R^2=0.99996\)). Right-censored trajectories are not zeros, and the power law is a known saddle-node phenomenon, not a new law.

The critical-mode measurements and the predicted observable effects were consistent under valid simultaneous global \(O(2)\) hidden-coordinate transformations. This is a correctness check against representation artifacts, **not** physical spatial equivariance or a proof of a new gauge theory.

## 4. Causal tests, including the controls that change the interpretation

### 4.1 Moving the tracked fold

At the selected operating point \(\lambda=0.10\), a same-norm two-coordinate hidden-bias edit in the critical adjoint direction shifted the numerically solved fold from \(0.20091324\) to approximately \(0.05291139\). Orthogonal and reversed edits yielded approximately \(0.19600716\) and \(0.33432999\), respectively. A first-order sensitivity predicted a shift of about \(-0.139624\) for the norm-0.002 critical edit; the nonlinear augmented solve gave \(-0.148002\). The local approximation weakens for larger edits, as expected.

On a **separate, 24-group noisy bank** at 512 steps, binary signed recall was **20/24** with the critical edit and **0/24** for no edit, orthogonal, or reversed direction. At 1,024 steps it was 19/24. Under harder noise it fell to 9/24 at 512 and 1/24 at 1,024. These are paired histories within one selected model.

Direct critical-mode state perturbations shifted the observed time of native sign failure much more than the tested projection-orthogonal directions. Exploratory dynamics-switch experiments also showed a finite window: at \(\lambda=0.10\), switching from failed to repaired recurrence by step 128 restored binary recall in 71.9% of a 32-group noisy bank, at step 256 in 15.6%, and at step 384 in 0%. Late failure of this particular intervention does **not** prove global information irrecoverability.

### 4.2 A decisive negative optimization baseline

The fold-derived edit did **not** outperform a conventional short-horizon task-loss gradient. Over six correlated \(\lambda\) conditions, 512-step mean signed-binary recall on the standard bank was 76.6% for the fold edit versus **77.1% for a 128-step gradient** under the same bias-parameter and edit-norm budget. The directions were highly aligned. Consequently, the reported contribution is **dynamical explanation**, not a better repair algorithm.

Three-class neutral recall was not restored. No stable neutral-output fixed point was found in the numerical search, but this is not proof that none exists globally. A separate early forecasting study under increased noise also found that early critical-state features did not outperform the simple interpolation-parameter baseline in ranking failures (ROC AUC 0.511 vs **0.648**).

### 4.3 What the neighbor-coupling audit added

The NCA's update includes shared self recurrence and contributions from adjacent cells:

\[
q_i^{k+1}=W_{\mathrm{in}}x_i+b_h+a_{\mathrm{self}}h_i^k+a_Lh_{i-1}^k+a_Rh_{i+1}^k.
\]

The frozen fold's adjoint sensitivity predicted a uniform neighbor-coupling-scale derivative \(d\lambda_*/d\gamma\approx0.674904\). For \(\gamma=0.99\) and 1.01, the predicted fold locations 0.194164 and 0.207662 closely matched the augmented numerical solves 0.194125 and 0.207624. Thus the **actual spatial coupling terms affect the tracked slow-mode structure**.

An edge ranking performed on the fold state selected the directed cell **2 → 1** message at all three internal microsteps. Cutting that connection throughout each decision restored signed recall on 24/24 standard and 21/24 harder-noise groups in the primary bank, whereas the unmodified model had 0/24. But two exploratory controls altered the interpretation:

1. Other physical edges could also rescue signed behavior.
2. A **fixed, cue-independent forcing perturbation** derived from the fold reference state reproduced almost the entire benefit while keeping the live 2 → 1 message intact: 32/32 standard and 31/32 harder-noise histories, compared with 32/32 and 30/32 for the edge cut.

The success of this forcing control undermines a simple claim that we have located an indispensable cue-carrying message. A more defensible interpretation is that **spatially targeted changes to recurrent forcing can shift the dynamical regime supporting binary retention**. This does not exclude information transport by other distributed messages or identify a uniquely necessary causal circuit.

![Local fold location under scaled neighbor coupling](figures/coupling_fold_sensitivity.png)

*Plot from the completed coupling audit. The smaller the perturbation, the more closely the first-order prediction follows the nonlinear fold solve.*

## 5. A separate GRU comparison: conditional rescue, not the same mechanism

The selected six-hidden-unit GRU merge `61004–61067` supplied a different test of recurrent computation. A cue-conditioned hidden-state swap at decision 128 was almost invisible to a **diagnostic readout fitted using 512-step development labels**, but influenced output at decision 512. Candidate-gate activation clamps demonstrated that delayed transfer depends on intervention timing.

In V6 the original-recipient candidate trace \(n_R\) served as a reference. During a disruptive clamp, only the projected part of the candidate computed by the **currently evolving intervened GRU** was restored:

\[
n_{\mathrm{used}}=n_R+vv^\top(n_{\mathrm{current}}-n_R).
\]

On 40 held-out noise histories per signed direction, the selected rank-one restoration over the specified interval recovered the correct **donor sign in 40/40 for each direction**, while an orthogonal residual and shorter restoration window yielded 0/40. The recovered numerical trajectory was substantially less close to the donor than an unrestricted swap. Additional neutral and 32-direction controls were added **after inspecting the main result**. This does not establish an autonomous one-dimensional memory algorithm or a full explanation of natural GRU merging failure.

The GRU is included here as a **conceptual contrast**, not as independent replication of the NCA's saddle-node mechanism.

## 6. What this note can and cannot claim

**Supported within the selected NCA:** a local fold tracks a slow region traversed by natural cue histories; derivative-derived predictions accurately describe passage within a specified interval; parameter, state, timing, and neighbor-coupling interventions change the tracked dynamics and long-horizon signed behavior in compatible directions. The coordinate controls rule out several trivial reparameterization artifacts.

**Not supported:** proof that parameter averaging of two fully competent three-way memory parents created this particular defect; a general method for merging complementary robot skills; a uniquely necessary memory edge or neuron; restored three-way memory; exhaustive attractor/basin mapping; improved repair over ordinary gradients; reliable out-of-distribution early diagnosis; independent-population generalization to unseen NCA pairs; transfer of the NCA fold explanation to GRUs, LLMs, or AI safety behavior.

The numerical results are a **sequence of exploratory studies on a heavily inspected case**, including specified pre-run hypotheses within that case and later explicitly post-hoc controls. New trajectory seeds do not remove model-selection bias. The figure and claim register should preserve this distinction.

## 7. Why the experiment sequence matters

The main methodological lesson is not that a fold or sparse circuit was found. It is that **successively stronger tests eliminated simpler explanations**:

- An accurate readout is not evidence of correct native future behavior.
- A low-dimensional hidden-state statistic does not guarantee complete memory.
- A local bifurcation model predicts *local passage* but not all future failures.
- A fold-directed patch can be mechanistically informative without beating task gradients.
- An effective neighbor-edge cut need not mean the edge uniquely carries cue content.
- A selective GRU gate rescue demonstrates a conditional causal contribution, not full merge repair.

These failures and distinctions are part of the empirical contribution; they are not optional admissions relegated to a footnote.

## 8. What would actually advance the merging question?

Two follow-ups remain scientifically different from polishing this selected case:

**(i) Reconstruct the actual alignment-induced parameter changes.** Starting from the archived input-aligned and activation-aligned merged models, separate the effects of their input-weight and hidden-bias differences, including interactions, on the fold and natural cue histories. This would strengthen the causal bridge from the *merging procedure* to the *recurrent dynamics*.

**(ii) Prospective replication on qualified independent pairs.** Freeze the diagnostic and controls before testing new merges of independently trained, task-qualified models. Compare mechanistic predictions against parameter/activation similarity, short-horizon behavior, readout calibration, and equal-budget gradients. A negative result would define the boundary of the mechanism, not justify redefining qualification afterward.

The original four-hidden-unit robot-control task—combining genuinely distinct homing and avoidance skills—remains a separate, important test of compositional capability preservation. The present case study does not solve it.

## 9. Records and prior work

**Experiment records and code packages (names in the existing research archive):**

- `REPORT(20261015-210943).md` — exact coordinate controls, fold continuation, gradient baseline.
- `REPORT(20261015-213922).md` — memory-lifetime scaling, derivative-derived passage, critical-state and dynamics-switch interventions.
- `REPORT(20261015-215716).md` — decodability and failures of early forecasting under noise shift.
- `NCA_NEIGHBOR_COUPLING_AUDIT_V1.zip` — exact code, checkpoints, pre-run protocol, exploratory controls, and results from the cellular coupling audit.
- `GRU_CANDIDATE_MEDIATION_V6.zip` — exact GRU clamp and rank-one rescue experiment, selected-case controls.
- `Recurrent_Memory_Publication_Blueprint.md` — working claim register and manuscript plan.

**Closest conceptual prior art:**

- Ainsworth, Hayase & Srinivasa (2023), [*Git Re-Basin*](https://arxiv.org/abs/2209.04836): permutation-aware merging.
- Sussillo & Barak (2013), [*Opening the Black Box*](https://doi.org/10.1162/NECO_a_00409): recurrent fixed points and slow modes.
- Dinc et al. (2026), [*Ghost Mechanism*](https://arxiv.org/abs/2501.02378): saddle-node transients in recurrent memory.
- Makelov et al. (2024), [*Is This the Subspace You Are Looking for?*](https://arxiv.org/abs/2311.17030): risks of overinterpreting subspace-patching interventions.

**Reproducibility note:** numerical values in this document are transcribed from the referenced executed audit reports and saved output tables. This editorial assembly did not independently rerun the archived NCA/GRU experiments or rederive their solvers. Before an external scientific submission, regenerate the key figures and reconcile any historical fold-location discrepancies against checkpoint hashes and the final augmented solver.
