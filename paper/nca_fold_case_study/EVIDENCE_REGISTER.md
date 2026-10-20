# Evidence and claim register

**Status:** Audit trail for a selected-case GitHub research note, *not a preregistration of the overall project*.

| Claim | Supporting archived experiment | What the result does NOT show | Sequence status |
|---|---|---|---|
| GRU permutation mismatch can catastrophically damage self-merges, even when endpoints are functionally equivalent | `REPORT(20261015-210943).md` — 40 correlated self-merges from 8 GRUs | New permutation theorem; optimal relative alignment of inequivalent models | Methodological control, reused trained models |
| A selected merge-derived NCA has a fold-associated finite-time slow region | `REPORT(20261015-213922).md`, fixed-point solves, natural cue trajectories | Generic effect of arbitrary merges or fully qualified parent-to-child loss | Selected model/path, exploratory discovery |
| Local normal form quantitatively predicts passage through a fixed critical window | `REPORT(20261015-213922).md` — w=.10, 0.22-step MAE on 9 correlated conditions | Prediction of whole memory lifetime or task success; new scaling law | Explored multiple windows after initial results |
| Critical bias direction moves fold and improves signed retention | `REPORT(20261015-210943).md`; `REPORT(20261015-213922).md` | Unique mediator, superior repair, full three-way recovery | Within-model, additional noisy histories |
| Ordinary task gradient performs at least as well as fold-guided edit in tested conditions | `REPORT(20261015-210943).md` — 77.1% vs 76.6% average | Mechanistic analysis is useless; global comparison to every optimizer | Direct equal-norm, same-bias-block comparator |
| Critical-mode state/dynamics-switch tests alter output failure time and retention | `REPORT(20261015-213922).md` | Proof of irreversible information loss or global basin geometry | Exploratory post-main-result tests |
| Fold-based early features fail to improve OOD failure ranking | `REPORT(20261015-215716).md` — AUC .511 vs .648 lambda-only | All predictive dynamical features are useless | Exploratory, selected-model, different noise regime |
| Actual neighbor coupling moves tracked fold | `NCA_NEIGHBOR_COUPLING_AUDIT_V1/RESULTS_AND_LIMITATIONS.md`; `results/fold_prediction_vs_exact.csv` | Unique neuron/edge representation of memory | Primary prerecord within already selected model |
| Edge cut improves signed recall but is mimicked by constant forcing; other edges work | `NCA_NEIGHBOR_COUPLING_AUDIT_V1/RESULTS_AND_LIMITATIONS.md` | Cue-information transport uniquely localized to 2→1 | Primary cut, subsequent controls explicitly exploratory |
| Rank-one GRU candidate rescue produces signed donor transfer under clamp | `GRU_CANDIDATE_MEDIATION_V6/RESULTS_AND_LIMITATIONS.md` | General GRU mechanism; readout-independent merge repair; three-way task restoration | Main held-out histories; additional random and neutral controls post hoc |

## Invariants and provenance restrictions

- **NCA:** only simultaneous global hidden-channel O(2) transformations with matching parameter/readout transport have been verified. No spatial equivariance or independent local gauge structure is claimed.
- **GRU:** hidden-unit permutations are valid, not arbitrary orthogonal rotations.
- **Source construction:** NCA `F→S` varies `W_in` and `b_h` between two **merger-derived** models, not between two independently task-qualified parent networks.
- **Dependent observations:** different lambda points, trajectory seeds, or edge interventions within the same NCA are **not independent trained-model replications**.
- **Memory outcomes:** signed binary correctness, native readout failure, decodability, and strict no-cue-inclusive three-way task accuracy are distinct.
- **Numerical provenance:** earlier approximate fold locations and later refined augmented solves must not be mixed without rechecking checkpoint/solver definitions.

## Minimum verification before arXiv submission

1. Reproduce fold positions and passage predictions from frozen checkpoint/code hashes.
2. Check that figures use the same definitions of lambda, cue, output sign, memory lifetime, and censoring.
3. Generate the main fold/delayed-memory figures directly from saved arrays rather than recreating them by eye.
4. Clearly mark discovery, prerecord-within-selected-system, post-hoc controls, and held-out trajectory histories.
5. Check related literature, especially neural dynamics of transient memory and model merging; do not claim priority without an exhaustive review.
