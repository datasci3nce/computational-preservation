# Reproducibility and provenance

This is presently an **evidence archive and paper draft**, not a full runnable reproduction of the original studies. The missing model checkpoints, raw arrays, scripts, seeds, and environment definitions are tracked explicitly in `checkpoint_manifest.csv` and `source_file_manifest.csv`.

`source_file_hashes.csv` records SHA-256 digests of the five bundled frozen documents. They allow detecting editorial drift, **not** proving the original experiments executed as described.

Before labeling a result reproduced:

1. Recover the exact archived experiment ZIP, hashes, executed code version and model files.
2. Record the solver configuration and numerical precision (especially the augmented fold solver), training seed, cue bank, readout, time horizon and noise regime.
3. Rerun with raw output matrices or trajectory dumps and retain machine-readable results.
4. Compare reported and recomputed numerical values, including correct definitions for binary versus strict three-way recall.
5. Record whether hypotheses/conditions were explored, selected, pre-registered within a case, frozen before new observations or tested on independent models.

The `scripts/normal_form.py` executable is only a **calculation of a published local approximation**, not a recreation of original NCA trajectories or figures.
