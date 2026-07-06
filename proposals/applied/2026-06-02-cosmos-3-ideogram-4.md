---
type: proposal
sources:
  - raw/newsletters/2026-06-02-ainews-nvidia-cosmos-3-nemotron-3-ultra-and-rt.md
  - raw/newsletters/2026-06-04-ainews-reve-2-and-ideogram-4-layouts-in-imagege.md
status: pending
created: 2026-06-24
---

# Proposal: NVIDIA Cosmos 3 + Ideogram 4.0 — competing #1 open image/video models

## Summary

Two significant open-weight creative model releases in the same period: NVIDIA Cosmos 3 (Mixture-of-Transformers — autoregressive reasoner + diffusion generator; #1 open-weight on Text-to-Image and Image-to-Video leaderboards; full weights/code/data released), and Ideogram 4.0 (#8 overall Arena image, #1 open image model; 9.3B DiT; strong text rendering and branding). The open image/video model landscape shifted materially in this period.

## Intended changes

- [x] **Create** `wiki/models/cosmos-3.md` — new model page for NVIDIA Cosmos 3
    > See draft below

- [x] **Create** `wiki/models/ideogram-4.md` — new model page for Ideogram 4.0
    > See draft below

- [x] **Update** `wiki/state-of/models.md` — add Cosmos 3 to Architecture experiments; add Ideogram 4 to Image generation; add Recent changes entries
    > **Add to Architecture experiments section:**
    > `- [NVIDIA Cosmos 3](../models/cosmos-3.md) — NVIDIA; Mixture-of-Transformers (autoregressive reasoner + diffusion generator); Nano 16B (8B+8B), Super 64B; #1 open-weight Text-to-Image and Image-to-Video leaderboards; Cosmos Coalition with Runway; full weights/code/data released *(as of 2026-06-02)*`
    >
    > **Add to Image generation section (alongside GPT-Image-2 and Nano Banana 2):**
    > `- [Ideogram 4.0](../models/ideogram-4.md) — Ideogram; 9.3B DiT; #8 overall Image Arena, #1 open image model; strong text rendering and branding; fp8/nf4 checkpoints, ComfyUI; no commercial license *(as of 2026-06-04)*`
    >
    > **Add to Recent changes:**
    > `- [2026-06-02] NVIDIA Cosmos 3: Mixture-of-Transformers world model; Nano 16B / Super 64B; #1 open-weight Text2Image and Image2Video; full open release with Runway Cosmos Coalition`
    > `- [2026-06-04] Ideogram 4.0: 9.3B DiT, #1 open image model (Arena #8 overall); fp8/nf4 checkpoints, ComfyUI; strong text rendering`

- [x] **Update** `wiki/state-of/creative.md` — add Ideogram 4.0 to image generation; note Cosmos 3 as video generation entrant; add Recent changes entries
    > **Add a new subcategory or add to AI video generation:**
    >
    > Add to AI video generation section:
    > `- [NVIDIA Cosmos 3 Super](../models/cosmos-3.md) — NVIDIA; #1 open-weight Image-to-Video; Mixture-of-Transformers architecture; full weights released via Cosmos Coalition *(as of 2026-06-02)*`
    >
    > **Add new subcategory `AI image generation` (if not existing) or extend existing note:**
    > `- [Ideogram 4.0](../models/ideogram-4.md) — Ideogram; #1 open image model (Arena #8 overall); 9.3B DiT; strong text rendering and structured layout *(as of 2026-06-04)*`
    >
    > **Add to Recent changes:**
    > `- [2026-06-02] NVIDIA Cosmos 3: #1 open-weight Image-to-Video; Cosmos Coalition with Runway; full open release`
    > `- [2026-06-04] Ideogram 4.0: #1 open image model; strong text/branding capabilities; fp8/nf4, ComfyUI`

## Page drafts

### wiki/models/cosmos-3.md (new)

````md
---
title: NVIDIA Cosmos 3
type: model
domains: [models, creative]
subcategory: image-generation
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
````

### wiki/models/ideogram-4.md (new)

````md
---
title: Ideogram 4.0
type: model
domains: [models, creative]
subcategory: image-generation
tags: [open-weights]
as_of: 2026-06-04
sources: [ainews-cosmos-nemotron-june-2026, ainews-ideogram-june-2026]
---

# Ideogram 4.0

Ideogram's open-weight image generation model, positioning as the leading open image model on Arena benchmarks. Known for strong text rendering inside images and structured visual layout — areas where many generative models struggle.

## Current status (as of 2026-06-04)

- **Size:** 9.3B Diffusion Transformer (DiT)
- **Weights:** Released as fp8 and nf4 checkpoints
- **Tooling:** ComfyUI support; Qwen3-VL-8B-Instruct as the text encoder
- **Prompting:** JSON-structured prompting for layout control
- **Safety:** Watermarked; safety-filtered; **no commercial license** (research/personal use only at launch)
- **Arena:** #8 overall Image Arena; **#1 open image model**; strong scores for text rendering and branding tasks
- Released approximately one day before Cosmos 3 Super in the same period

## Strengths

- #1 open image model by Arena ranking at launch — meaningful for practitioners who want a deployable alternative to GPT-Image-2
- Text rendering within images is notably better than most generative models
- ComfyUI support and quantized checkpoints lower the deployment hardware bar
- JSON-structured prompting enables more deterministic layout control

## Weaknesses / caveats

- No commercial license at launch — limits enterprise deployment
- Safety filters may constrain use cases relative to less restricted open models
- #8 overall Arena places it behind proprietary models (GPT-Image-2, Nano Banana 2) by a significant margin

## Recent changes

- [2026-06-04] Arena results and Arena #1 open model ranking confirmed; fp8/nf4 checkpoints and ComfyUI announced

## Sources

- [AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra, MiniMax M3 (June 2)](../../sources/newsletters/ainews-cosmos-nemotron-june-2026.md)
- [AINews — Ideogram 4 layouts, Harvey routing, enterprise spend (June 4)](../../sources/newsletters/ainews-ideogram-june-2026.md)
````

## Open questions

- `state-of/creative.md` does not have an explicit "AI image generation" subcategory (only "AI video generation"). Should Ideogram 4.0 go under a new `AI image generation` subcategory, or does the existing page need restructuring?
	- Lets create one, yes
- Cosmos 3 is simultaneously a world model architecture experiment and a creative generation model. Should it be in `state-of/models.md` (Architecture experiments) only, or also in `state-of/creative.md`?
	- Its a creative model, the world model is very debatable.
