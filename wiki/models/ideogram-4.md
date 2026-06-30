---
title: Ideogram 4.0
type: model
domains: [models, creative]
subcategory: image-generation-model
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
