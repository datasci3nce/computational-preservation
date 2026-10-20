# Computational Preservation Under Neural-Network Modification

**An exploratory research archive on alignment, merging, recurrent dynamics and causal intervention**  
**Evidence checkpoint:** 18 October 2026 · **Repository packaging:** 20 October 2026

> **Status:** Research archive and work-in-progress technical note. The reported experiments were carried out in earlier investigations and transcribed from their frozen records; this repository has **not** rerun them. The original executable archives, checkpoints and raw result arrays are **not yet bundled**. A compiled manuscript PDF is included but **is not an empirical reproduction**. No general-purpose repair method or frontier-model safety result is claimed.

## Research question

When we align, average, prune, fine-tune or distill learned networks, **what exactly survives?** Can a causal or dynamical account predict whether a desired capability will remain reliable beyond the observed evaluation horizon?

For a recurrent network, three objects matter:

\[
\underbrace{\theta}_{\text{parameters}}
\longrightarrow
\underbrace{h_{t+1}=F_\theta(h_t,u_t)}_{\text{representations and recurrence}}
\longrightarrow
\underbrace{y_t}_{\text{native behavior}}.
\]

Similar scores do not imply similar internal computations. Different parameterizations can implement the same function under a valid change of coordinates. A hidden state can retain decodable information that the model cannot use at a later decision. We study these distinctions using small feed-forward robotic controllers, neural cellular automata (NCAs), and gated recurrent units (GRUs).

### Three kinds of preservation

| Type | Proposed operational test | What it does *not* guarantee |
|---|---|---|
| **Behavioral** | Accuracy or output agreement on a stated input distribution and time horizon | Agreement on unseen inputs, perturbations or later horizons |
| **Coordinate** | Exact function-preserving transformation, with every affected parameter transported consistently | That unrelated trained networks implement the same algorithm |
| **Causal/dynamical** | Agreement of specified interventions and subsequent state/output trajectories | A universal, intervention-independent notion of the “same mechanism” |

These are working distinctions, not a new identifiability theorem.

## Three central findings

**1. A selected NCA has a quantitatively interpretable slow-memory regime.** Along a *restricted path between two merge-derived variants* of a seven-cell, two-channel NCA, the neutral-input recurrent map has a tracked saddle-node fold near **\(\lambda_*=0.20091324\)**. Natural cue trajectories traverse a slow region associated with the fold. A derivative-derived local normal form predicts passage through a specified window with approximately **0.22 decision mean absolute error** over nine correlated interpolation settings. That is **not** the error for entire memory lifetime. Directed state/parameter/coupling interventions change the dynamics and signed recall, but no-cue-inclusive strict memory was not restored. Ordinary task-gradient edits performed comparably to the fold-directed edit.

**2. Qualified GRUs can fail after parameter averaging, but diagnosing the damage is harder than detecting it.** In an original cohort, **21 of 96 GRUs** met the specified 512-decision qualification rule, giving **210 pairs**. Same-task parameter merging sometimes damaged delayed recall despite competent parents. Pair observations are dependent because they share parents. A selected candidate-activation intervention recovered a delayed signed effect on **40/40 held-out histories in each tested direction** under an *artificial clamp*. This is not a unique memory unit or full model repair. A frozen early mechanistic repair selector was outperformed by a simple behavioral screen.

**3. Output matching does not ensure future retention.** In a fresh GRU pair, a student trained on late teacher outputs reached **53/64** strict recall at decision 512, but only **7/64** at decision 1024; an early-output student reached **0/64** at both horizons. In the already selected NCA, fixed learned distillation update directions yielded locally accurate first-order predictions of fold shifts. This demonstrates a *specified training procedure* changing an interpretable recurrent structure—not unique recovery of weights or mechanisms from output observations.

The earlier four-unit ANN robotic work motivates this programme, but a later audit found unresolved checkpoint/evaluator provenance and weak archived Homing success (1/8 pilot starts). It is not presented as independently reproduced multi-skill composition.

## Explore the research

| Start here | Contents |
|---|---|
| [Experimental lineage](docs/EXPERIMENTAL_LINEAGE.md) | Twelve stages: questions, methods, results, failures and transitions |
| [Claims and limitations](docs/CLAIMS_AND_LIMITATIONS.md) | Supported claims versus overclaims, sample dependence and evidence statuses |
| [Selected NCA technical note](paper/nca_fold_case_study/RESEARCH_NOTE.md) | Original complete case study; includes mathematical derivation and negative controls |
| [NCA technical draft (PDF)](paper/nca_fold_case_study/NCA_Fold_Technical_Draft.pdf) · [LaTeX source](paper/nca_fold_case_study/main.tex) | Compiled three-page selected-case manuscript with author metadata; exploratory, not peer reviewed |
| [Fellowship research direction](docs/ILIAD_RESEARCH_DIRECTION.md) | Three-month falsifiable programme, intended as a proposal rather than evidence of completed work |
| [Prior work](docs/LITERATURE_REVIEW.md) | Relevant methods and novelty boundaries; bibliography requires final verification |
| [Next experiments](docs/OPEN_QUESTIONS.md) | Prospective test plan and stop/falsification criteria |
| [Frozen October 18 records](records/2026-10-18/README.md) | Unaltered research freeze, addendum and claim register |
| [Reproducibility](reproducibility/README.md) | Manifests of present and missing artifacts and exact file hashes |

Architecture-specific folders under [`experiments/`](experiments/README.md) describe the existing study families. They are **indices**, not executable reproductions of missing code.

## How to assess the strongest result

The NCA experiment concerns the *three-microstep external decision map* \(T_\theta\), with neutral-input fixed-point residual

\[
G(h,\lambda)=T_{\theta(\lambda)}(h;u_0)-h.
\]

Close to the tracked fold, derivatives define a local approximation

\[
z_{t+1}-z_t\simeq a(\lambda-\lambda_*)+bz_t^2,
\quad a\simeq-0.05493465,\quad b\simeq0.01169046.
\]

This explains a *local passage-time bottleneck* in one heavily investigated system. The source account separates discovery, within-model checks, post-hoc controls, and held-out histories. Importantly, the path changes \(W_{in}\) and \(b_h\) between two **merged variants**, not between two independently qualified parent networks. It does not establish that averaging competent specialists caused the observed fold.

A minimal, **illustrative-only** implementation of the normal-form formula is included:

```bash
python scripts/normal_form.py
python -m unittest discover -s tests -v
```

This calculation does not rerun the NCA, estimate errors against trajectory data, or produce an empirical figure.

## AI safety motivation—not a demonstrated result

Modification of a safety-relevant learned policy might preserve ordinary short-horizon behavior while changing a computation needed later or under intervention. These small recurrent organisms let us ask whether a causal/dynamical model adds predictive value over simpler tests. **We have not shown preservation or loss of a safety circuit in an LLM**, nor a general diagnostic that outperforms behavioral baselines. The ambition is prospective prediction on independently trained, competent systems, with frozen model-selection and intervention protocols.

## Reproducibility and responsible claims

Read [`reproducibility/checkpoint_manifest.csv`](reproducibility/checkpoint_manifest.csv) before citing numbers as independently reproduced. Present source documents are checked by SHA-256; older reports, trained checkpoints, raw arrays and several figures remain external to this assembly. Reported percentages and quantitative predictions are attributed to prior saved investigations. No missing file has been fabricated, and no publication status has been assigned.

**Next release gate:** obtain the original archives and rerun the main NCA fold solve, the nine-condition local-passage comparison and the gradient/null controls. Then test one frozen mechanistic prediction prospectively on independent qualified networks. See [Open questions](docs/OPEN_QUESTIONS.md).

## Attribution and reuse

This archive is presented as an independent research work in progress. Please cite the exact file/checkpoint revision when discussing results. **No software/content license has been selected** for this starter repository; decide on a license before inviting outside contributions or reuse. Corrections and provenance issues can be documented using the issue template under `.github/ISSUE_TEMPLATE/`.
