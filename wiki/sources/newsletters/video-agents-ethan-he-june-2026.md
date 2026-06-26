---
title: '"Why Video Agent Models Are Next" — Ethan He on Latent Space (June 1)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-01-why-video-agent-models-are-next-ethan-he-xai-gr.md
published: 2026-06-01
ingested: 2026-06-24
domains: [creative, models]
---

# "Why Video Agent Models Are Next" — Ethan He on Latent Space (June 1)

Latent Space interview with Ethan He, who built NVIDIA Cosmos (world model) and then built Grok Imagine at xAI from scratch in 3 months. Covers the LLM-first intelligence thesis for video models, the video agents paradigm, world model definitions, and the technical architecture of diffusion + LLM prompt rewriting.

## Influenced pages

- [Video agents as next frontier](../../trends/video-agents-next-frontier.md) — new page
- [State of Creative](../../state-of/creative.md) — Grok Imagine Agent entry

## Key claims extracted

- LLM prompt rewriter is the primary intelligence source in video models, not the diffusion model itself
- Cosmos 7B video model + LLM rewriter (Llama/Mixtral) — rewriter is larger than the video model
- Video models take instructions literally and produce flat output without detailed LLM-generated specs
- World model = real-time + interactive + long-horizon (Ethan's definition)
- Grok Imagine 0.9: first large-scale audio-video joint generation model; Grok Imagine Agent beta: first video agent product
- Step distillation: 4-8 steps in production vs 100 during training
- Video agents will call diffusion as a tool, plus FFmpeg, editing software, etc. — same as how coding agents call compilers and tests
- "The next Sora won't be a better video model, it'll be a video agent"
- Ethan leaving xAI to work on LLMs, believing language model improvements are where video leverage actually lies
- Timeline: production-grade video agent quality (ads-ready) by end of 2026 (Ethan's prediction)
- SynthID/watermarking: increasingly reversible as models improve; regulatory pressure varies by country
