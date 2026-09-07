---
title: Inkling
type: model
domains: [models]
subcategory: open-weight-model
tags: [open-weights, multimodal]
as_of: 2026-07-16
sources: [ainews-thinkys-inkling-2026-07-16]
---

# Inkling

Thinking Machines Lab's first publicly-released flagship model. A 975B-total / 41B-active mixture-of-experts model, natively multimodal across text, image, and audio, released under Apache 2.0.

## Current status (as of 2026-07-16)

- 975B total / 41B active MoE, trained on 45T tokens
- Natively multimodal: text, image, and audio in one model
- 1M-token context on the open weights; 256K on the hosted Tinker API
- Architecture departs from convention: relative positional attention instead of RoPE, large-scale short-convolution layers, and two MoE experts shared across all tokens rather than routed
- Companion Inkling-Small preview: 276B total / 12B active
- Artificial Analysis Intelligence Index: 41 — ahead of Nemotron 3 Ultra (38) and gpt-oss-120b (24); still behind GLM-5.2 and Kimi on agentic/multimodal benchmarks specifically

## Why it matters

The first flagship release from a lab known until now mainly for research previews (see the smaller TML-Interaction-Small real-time model). A US lab choosing to ship its flagship as open weights is itself notable — most open-weight competition to date has come from Chinese labs.

## Recent changes

- [2026-07-16] Initial release: 975B/41B MoE, Apache 2.0, Intelligence Index 41

## Sources

- [AINews — Thinking Machines' Inkling (975B/41B, multimodal)](../sources/newsletters/ainews-thinkys-inkling-2026-07-16.md)
