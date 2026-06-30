---
title: NVIDIA Cosmos 3
type: model
domains: [models, creative]
subcategory: image-generation-model
tags: [nvidia, open-weights]
as_of: 2026-06-02
sources: [ainews-cosmos-nemotron-june-2026]
---

# NVIDIA Cosmos 3

NVIDIA's open-weight world model using a Mixture-of-Transformers (MoT) architecture — the first significant open model to combine an autoregressive language/reasoning component with a diffusion generation component in a single unified system. Claims #1 open-weight performance on both Text-to-Image and Image-to-Video leaderboards at launch.

## Current status (as of 2026-06-02)

- **Architecture:** Mixture-of-Transformers — autoregressive reasoner (language/planning component) + diffusion generator (image/video component) in a unified model
- **Sizes:** Cosmos 3 Nano (16B = 8B+8B), Cosmos 3 Super (64B)
- **Open release:** Full weights, code, and training data released — among the most open large generative model releases
- **Benchmarks:** Super variant — #1 open-weight on Text-to-Image leaderboard; #1 open-weight on Image-to-Video leaderboard (Artificial Analysis)
- **Cosmos Coalition:** Partnership with Runway for video generation applications; broader coalition for world model deployment
- **Positioning:** Physical AI and world model use cases; designed for robotics sim, autonomous systems, and creative generation

## Strengths

- Most architecturally novel open release in the image/video space: MoT unifies reasoning and generation
- Full open release (weights + code + data) is notably transparent for a model at this scale
- Dual leadership on Text2Image and Image2Video is a strong benchmark position for an open model

## Weaknesses / caveats

- MoT architecture is novel — deployment and ecosystem tooling are less mature than for pure diffusion or pure autoregressive models
- Claims come primarily from NVIDIA's own reporting and Artificial Analysis — independent evaluations pending
- Cosmos Coalition with Runway suggests commercial integration paths, but terms for derivative use are worth verifying

## Recent changes

- [2026-06-02] Launched at Computex 2026; Cosmos Coalition with Runway announced; initial leaderboard positions

## Sources

- [AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra, MiniMax M3 (June 2)](../../sources/newsletters/ainews-cosmos-nemotron-june-2026.md)
