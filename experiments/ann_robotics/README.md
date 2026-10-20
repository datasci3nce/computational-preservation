# ANN robotics

Original motivation: four-hidden-unit feed-forward policies for Homing, Exploration, Obstacle Avoidance and Wall-Following, aligned with LAP before merging/pruning. The old thesis's selected synergy-destruction report is **not** reconstructed by the available saved weights; executable source and model dimensions disagree with thesis prose.

A headless archived Homing pilot reached 1/8 starts (5/8 collisions). Teacher imitation recovered light-sensitive steering on observed sensor states, and a chosen unit ablation diminished it, but this is not robust Homing or selective removal of Exploration.

**Needed:** versioned `evo_test (2).zip`, checkpoints, source-specific evaluator, held-out trajectories and all random seeds. See the [frozen research record](../../records/2026-10-18/FREEZE_20261018.md).
