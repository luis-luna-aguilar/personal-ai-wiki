---
title: Qwen 3.6 35B-A3B
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-04-22
sources: [vectorlab-qwen-3-6-local-threshold, qwen-3-5-medium-february, ainews-2026-04-22]
---

# Qwen 3.6 35B-A3B

Alibaba's open-weight MoE coding model. The current signal is less "benchmark champion" than "practical threshold crossing": recent commentary describes it as the first local coding and agent model people would seriously run in harnesses on accessible hardware.

## Current status (as of 2026-04-22)

- 35B-parameter A3B mixture-of-experts model viable on roughly 24GB-class local hardware
- The "practical local-agent threshold" framing started in the late-February Qwen 3.5 medium release cycle and sharpened further by the 3.6 framing
- Community niche (April 2026 LocalLlama data): strong for coding, tool calling, and agentic tasks; Gemma 4 26B outperforms it for creative writing, translation, and conversation
- Positioned as a practical local-agent baseline rather than a research novelty or general-purpose assistant
- Broad framing: local agent workflows are getting good enough to handle easy and medium-difficulty tasks without relying on proprietary models

## Qwen 3.6 Max Preview (proprietary tier)

Qwen 3.6 Max Preview went live on Qwen Chat (chat.qwen.ai) in April 2026. Community estimates: 600-700B parameters, based on prior 397B Qwen 3.6 Plus lineage. Highest AA-Intelligence Index among Chinese models (score: 52 as of April 2026). Community consensus: unlikely to be open-sourced — Alibaba has historically kept Max-tier models proprietary; their largest open-sourced version is roughly 122B parameters. API access with multi-step workflow support is coming.

## Strengths

- Local execution viability on comparatively modest hardware
- Better cost and control profile for users who want self-hosted coding agents
- Good fit for open agent harnesses and quantized inference stacks

## Caveats

- Current claims are mostly synthesis and practitioner commentary rather than one canonical launch write-up in this batch
- Relative performance versus frontier proprietary models is still presented as directional rather than settled

## Recent changes

- [2026-04-22] Added community reception niche data (coding/tools > creative/translation); added Qwen 3.6 Max Preview section (proprietary, 600-700B est., top Chinese AA-Intelligence Index)

## Sources

- [[sources/newsletters/vectorlab-qwen-3-6-local-threshold]]
- [[sources/newsletters/qwen-3-5-medium-february]]
- [[sources/newsletters/ainews-2026-04-22]]
