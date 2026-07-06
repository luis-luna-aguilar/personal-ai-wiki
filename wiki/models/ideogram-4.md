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

Ideogram's open-weight image generation model, positioning as the leading open image model on Arena benchmarks. Known for strong text rendering inside images and structured visual layout — areas where many generative models struggle. The model flipped from a closed product to open weights with broad community adoption.

## Current status (as of 2026-06-04)

- **Size:** 9.3B Diffusion Transformer (DiT)
- **Weights:** Released as fp8 and nf4 checkpoints; deployed on fal and Hugging Face
- **Tooling:** ComfyUI support; Qwen3-VL-8B-Instruct text encoder; JSON-structured prompting for layout control
- **Arena:** #8 overall Image Arena; **#1 open image model**
- **Safety:** Watermarked and safety-filtered; no commercial license at launch (research/personal use only)

## Strengths

- #1 open image model by Arena ranking — deployable alternative to GPT-Image-2
- Text rendering within images notably better than most generative models
- ComfyUI support and quantized checkpoints lower hardware requirements for deployment
- Strong gains in branding/commercial design tasks

## Weaknesses / caveats

- No commercial license at launch — limits enterprise deployment
- Safety filters may constrain use cases relative to unrestricted open models
- #8 overall Arena still trails GPT-Image-2 significantly

## Recent changes

- [2026-06-04] Open-weight release announced; fp8/nf4 checkpoints on fal and Hugging Face; Arena results confirmed

## Sources

- [AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra (June)](../../sources/newsletters/ainews-cosmos-nemotron-june-2026.md)
- [AINews — Ideogram 4 layouts, Reve 2 (June)](../../sources/newsletters/ainews-ideogram-june-2026.md)
