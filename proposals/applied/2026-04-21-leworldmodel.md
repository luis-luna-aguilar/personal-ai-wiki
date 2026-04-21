---
type: proposal
sources:
  - raw/papers/le-world-model-paper.pdf
  - raw/tweets/2026-04-21-howtoai_-2046254937559237012.md
status: pending
created: 2026-04-21
---

# Proposal: LeWorldModel (LeWM) — Stable End-to-End JEPA from Pixels

## Summary

LeWorldModel (LeWM) is the first JEPA (Joint-Embedding Predictive Architecture) that trains stably end-to-end from raw pixels using only two loss terms. Prior JEPA implementations couldn't avoid "representation collapse" — the model learns to map all inputs to the same point — without frozen encoders, exponential moving averages, or complex multi-term losses. LeWM replaces all of that with SIGReg, a single Gaussian regularizer. Result: 15M parameters, single GPU, trains in a few hours, plans 48× faster than DINO-WM on manipulation tasks. The paper also shows that LeWM's latent space develops physical understanding as an emergent property — it can recover spatial quantities from probing and detects physically impossible events.

*Paper proposal exception applies — this write-up prioritizes plain-language explanation.*

## Intended changes

- [x] **Create** `wiki/concepts/leworldmodel.md` — new concept page
    > See draft below

- [x] **Create** `wiki/sources/papers/leworldmodel.md` — source summary
    > See draft below

- [x] **Update** `wiki/index.md` — add `[[concepts/leworldmodel]]` under Concepts; update page count
    > **Add under `## Concepts`:**
    > ```
    > - [[concepts/leworldmodel]] — LeWM: first JEPA to train end-to-end from pixels; SIGReg solves representation collapse; 15M params, 48× faster planning than DINO-WM *(as_of: 2026-03-13)*
    > ```

## Open questions

- JEPA as a concept (separate from LeWM specifically) may eventually warrant its own `wiki/concepts/jepa.md` page if more papers in this lineage are ingested. Worth considering once there are 2+ JEPA papers in the wiki.
	- Lets separate the JEPA concept, its worth it.
	- Also the world model concept we can extract and just refer in here.

## Page drafts

### wiki/concepts/leworldmodel.md (new)

````md
---
title: LeWorldModel (LeWM)
type: concept
domains: [models]
as_of: 2026-03-13
sources: [leworldmodel-paper]
---

# LeWorldModel (LeWM)

A research paper (arXiv 2603.19312, March 2026) from Mila, NYU, Samsung SAIL, and Brown University — including Yann LeCun as co-author. LeWM is the first implementation of LeCun's JEPA architecture that trains stably end-to-end from raw pixels without requiring frozen encoders, heuristic tricks, or complex multi-term losses.

## The everyday problem this solves

### What is a world model, and why does it matter?

A world model is an AI's internal model of how the environment works — not just what it currently sees, but what will happen next if it takes a given action. This is the mental simulation ability that lets humans plan ahead: you can imagine throwing a ball without actually throwing it. An AI with a good world model can plan sequences of actions "in its head" rather than by trial-and-error in the real world.

Building world models from raw pixels (cameras) is especially attractive because cameras are cheap and universal. The alternative is hand-engineering state representations — measuring exact positions, angles, velocities — which is fragile and domain-specific.

### What is JEPA?

Most world models work generatively: they predict the *next image* pixel by pixel. This wastes enormous compute on irrelevant details — the exact color of a background, lighting variations — that don't matter for understanding what will happen next.

LeCun proposed JEPA (Joint-Embedding Predictive Architecture) as an alternative: instead of predicting the next image, predict the next *abstract representation* of the image. Compress the scene into a small vector (a latent embedding) and predict the next vector. Ignore pixel-level noise; capture only what matters for dynamics. This is more compute-efficient and should force the model to build richer physical understanding.

### Why JEPA hasn't worked well

JEPA has a fatal failure mode called **representation collapse**: the encoder finds an easy shortcut. If it maps every possible input to the same vector (e.g., all zeros), it trivially "predicts" the next state correctly — predicted and actual are both all-zeros. The model learns nothing about the world.

Previous fixes required:
- **Frozen pre-trained encoders** (DINO-WM): don't update the encoder during training, so it can't collapse — but it's then bounded by what the pre-trained encoder knew and can't adapt to the task
- **Exponential moving averages + stop-gradient** (I-JEPA, V-JEPA): heuristic training tricks to slow down collapse, but with no formal guarantee and unstable dynamics
- **Multi-term regularizers** (PLDM): add 6+ loss terms to fight collapse — works but requires polynomial-time hyperparameter search and produces noisy training curves

None of these are principled or simple.

## LeWM's solution: SIGReg

LeWM adds one regularizer called **SIGReg** (Sketched-Isotropic-Gaussian Regularizer). The idea: collapse would make all embeddings identical; a Gaussian distribution can never be identical. So force the embeddings to look like a Gaussian.

How it works:
1. Take the batch of latent embeddings
2. Project them onto M random directions (M=1024 by default)
3. Test whether each 1D projection follows a normal distribution (using the Epps-Pulley statistical test)
4. The regularization loss penalizes deviation from normality across all projections

By the Cramér-Wold theorem, matching all 1D projections onto random directions is mathematically equivalent to matching the full joint distribution. So if SIGReg succeeds, the full embedding distribution is Gaussian — which cannot be collapsed.

This reduces the tunable hyperparameters from 6 (vs. PLDM) to 1: the regularization weight λ. And λ can be found efficiently using a simple bisection search (O(log n)) instead of grid search.

The complete training loss is just two terms:
```
L = prediction_loss + λ × SIGReg(embeddings)
```

where the prediction loss is mean-squared error between the predicted next embedding and the actual next embedding.

## Architecture

- **Encoder**: ViT-tiny (~5M parameters), patch size 14, 12 layers, hidden dimension 192
- **Predictor**: 6-layer transformer (~10M parameters), 16 attention heads, 10% dropout
- Actions are fed to the predictor via Adaptive Layer Normalization (AdaLN)
- **Total: ~15M parameters**
- Trained on a single GPU in a few hours on offline trajectory datasets (no reward signals, no task labels)

## Planning

At inference time, LeWM does not generate images — it plans in latent space:

1. Given current frame → encoder → current latent z₁
2. Given goal frame → encoder → goal latent z_g
3. Sample 300 candidate action sequences
4. Roll each sequence through the predictor to get predicted final latent ẑ_H
5. Score each by distance to goal (‖ẑ_H − z_g‖²)
6. Keep top 30, update sampling distribution, repeat 30 iterations (Cross-Entropy Method)
7. Execute first K actions, replan from new observation

This planning loop completes in **0.98 seconds** (averaged over 50 runs on LeWM vs 47 seconds for DINO-WM — a **48× speedup**). LeWM uses ~200× fewer tokens than DINO-WM because it works in a compact latent space rather than pixel space.

## Results

Evaluated on four environments with continuous action spaces: Push-T (2D manipulation), OGBench-Cube (3D manipulation), Two-Room (2D navigation), Reacher (2D arm).

**Under fixed compute budget:**
- Push-T: **90% success rate** vs DINO-WM 13% (+18% over PLDM)
- OGBench-Cube: **74%** vs DINO-WM 48%
- Two-Room: slightly worse than PLDM/DINO-WM — see Limitations

**Planning speed:**
- 0.98s vs 47s (48× faster) — approaches real-time control

**Physical understanding (emergent):**
- Spatial quantities (agent location, block location, block angle) linearly recoverable from latent vectors — competitive with DINO-WM despite DINO-WM being pre-trained on 100M+ images
- Latent trajectories become *temporally straight* as a purely emergent property — LeWM achieves higher temporal straightness than PLDM, which explicitly regularizes for it
- Violation-of-expectation: model assigns significantly higher surprise (prediction error, p<0.01) to physically impossible events (teleportation) than to normal trajectories; more sensitive to physical perturbations than visual ones (color changes)

## Why this is useful beyond robotics

The core contribution — a single, provably anti-collapse regularizer that enables end-to-end learning of compact predictive representations — is architecture-agnostic and task-agnostic. SIGReg is borrowed from the self-supervised learning literature and is theoretically grounded.

For the wiki's context:

1. **Model efficiency direction**: A 15M-parameter model that understands physics and plans faster than large foundation world models challenges the assumption that world model capability requires massive scale. This is a data point in the generative AI vs. non-generative AI architecture debate.
2. **Agent planning**: Latent-space planning is 48× faster than pixel-space planning. For agents that need to plan in real time, this matters practically.
3. **Representation quality without pre-training**: LeWM recovers physical quantities without having seen any labeled data — this is the "intrinsic physical understanding" result. Foundation models (DINOv2) can do this too, but they needed 124M images; LeWM gets competitive results from a domain-specific offline dataset.

## Limitations (paper-reported)

- Planning quality degrades at long horizons — auto-regressive rollout accumulates errors. Hierarchical world modeling is a listed future direction.
- Requires offline datasets with sufficient interaction coverage — expensive or difficult to collect in new domains
- SIGReg works less well in very low intrinsic dimensionality environments (Two-Room): pushing towards a Gaussian in high-dimensional space when the true dynamics are low-dimensional creates a mismatch
- Requires explicit action labels to predict future states — future direction: inverse dynamics modeling to infer action representations
- All experiments are in simulation (no real-world robotics)
- Preprint, not yet peer-reviewed

## Sources

- [[sources/papers/leworldmodel]]
````

### wiki/sources/papers/leworldmodel.md (new)

````md
---
title: LeWorldModel — Stable End-to-End JEPA from Pixels
type: source
source_type: paper
source_file: raw/papers/le-world-model-paper.pdf
url: https://arxiv.org/abs/2603.19312
published: 2026-03-13
ingested: 2026-04-21
domains: [models]
---

# LeWorldModel — Stable End-to-End JEPA from Pixels

**arXiv:** 2603.19312 | **Status:** Preprint
**Authors:** Lucas Maes*, Quentin Le Lidec* (equal contribution), Damien Scieur, Yann LeCun, Randall Balestriero
**Affiliations:** Mila & Université de Montréal, NYU, Samsung SAIL, Brown University
**Website:** https://le-wm.github.io/ | **Code:** https://github.com/lucas-maes/le-wm

Introduces LeWM, the first JEPA that trains end-to-end from raw pixels without frozen encoders, EMA, or stop-gradient heuristics. A single Gaussian regularizer (SIGReg) replaces all collapse-prevention tricks, reducing tunable hyperparameters from 6 to 1.

## Plain-language thesis

Joint-Embedding Predictive Architectures (JEPAs) predict future states in abstract latent space rather than pixel space — more efficient and physically meaningful. But they collapse: the encoder maps all inputs to the same point to trivially satisfy the prediction objective. LeWM fixes this with SIGReg: force embeddings to look like a Gaussian distribution (which can't be uniform/collapsed). One regularizer, one hyperparameter, provably anti-collapse.

## Key results

| Metric | LeWM | DINO-WM | PLDM |
|---|---|---|---|
| Push-T success (fixed FLOPs) | 90% | 13% | 75% |
| OGBench-Cube success (fixed FLOPs) | 74% | 48% | — |
| Full planning time | 0.98s | 47s | — |
| Tunable hyperparameters | 1 | 1 | 6+ |
| Training from pixels | ✓ end-to-end | ✗ frozen encoder | ✓ end-to-end |

*All results from paper's own evaluations in simulation. No real-world robotics tested.*

## Key claims extracted

- First JEPA with provable anti-collapse guarantees and end-to-end pixel training
- 48× faster planning than DINO-WM (48 seconds → ~1 second)
- Physical quantities (agent/block location, angle) linearly recoverable from latent vectors
- Temporal trajectory straightness emerges without explicit regularization
- Significantly higher surprise on physically impossible events vs. unperturbed trajectories (p<0.01)
- Single GPU, ~15M parameters, trains in hours on offline datasets

## Limitations noted in paper

- Short horizon planning only; long-horizon: error accumulates
- Needs sufficient offline data coverage — limited data diversity hurts SIGReg
- Less effective in very low intrinsic dimensionality environments
- Requires action labels; no action-free training
- Simulation only; not tested on real-world robotics

## Influenced pages

- [[concepts/leworldmodel]] — new concept page
````
