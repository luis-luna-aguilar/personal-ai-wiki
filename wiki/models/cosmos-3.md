---
title: NVIDIA Cosmos 3
type: model
domains: [models, creative]
subcategory: image-generation-model
tags: [open-weights]
as_of: 2026-06-02
sources: [ainews-cosmos-nemotron-june-2026]
---

# NVIDIA Cosmos 3

NVIDIA's open-weight world model using a Mixture-of-Transformers (MoT) architecture — the first significant open model to combine an autoregressive language/reasoning component with a diffusion generation component in a single unified system. Claims #1 open-weight performance on both Text-to-Image and Image-to-Video leaderboards at launch, sitting close behind GPT-Image-2 (Nano Banana 2).

## Current status (as of 2026-06-02)

- **Architecture:** Mixture-of-Transformers — autoregressive reasoner + diffusion generator unified model
- **Sizes:** Cosmos 3 Nano (16B = 8B+8B), Cosmos 3 Super (64B = 32B+32B)
- **Open release:** Full weights, code, and training data released among the most transparent large generative model releases
- **Benchmarks:** Super variant — #1 open-weight on Text-to-Image leaderboard; #1 open-weight on Image-to-Video leaderboard (Artificial Analysis); just below Nano Banana 2 overall
- **Cosmos Coalition:** Partnership with Runway for video generation applications; broader coalition for world model deployment
- **Positioning:** Physical AI and world model use cases; designed for robotics sim, autonomous systems, and creative generation; also integrates with fal platform

## Strengths

- Architecturally novel open release: MoT unifies reasoning and generation in one system
- Full open release (weights + code + data) is notably transparent at this scale
- Dual leadership on Text2Image and Image2Video among open-weight models

## Weaknesses / caveats

- MoT architecture less mature than pure diffusion or autoregressive models for deployment
- Claims from NVIDIA reporting and Artificial Analysis — independent evaluations pending
- Positioned as "world model" but creative generation is more immediately useful; world model claims are debatable

## Recent changes

- [2026-06-02] Launched at Computex 2026; Cosmos Coalition with Runway announced; initial leaderboard positions

## Sources

- [AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra (June)](../../sources/newsletters/ainews-cosmos-nemotron-june-2026.md)
