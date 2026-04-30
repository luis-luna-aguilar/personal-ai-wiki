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
**Affiliations:** Mila & Universite de Montreal, NYU, Samsung SAIL, Brown University
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
- 48x faster planning than DINO-WM (48 seconds → ~1 second)
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

- [LeWorldModel (LeWM)](../../concepts/leworldmodel.md) — new concept page
