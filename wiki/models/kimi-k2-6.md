---
title: Kimi K2.6
type: model
domains: [models, coding]
subcategory: coding-model
tags: [moonshot-ai, open-weights, agentic]
as_of: 2026-04-21
sources: [kimi-k2-6-blog, ainews-2026-04-21]
---

# Kimi K2.6

Moonshot AI's April 2026 open-weight coding model. The launch materials position it as an agentic coding model optimized for long-horizon execution, multi-agent coordination, and self-hosted deployment.

## Current status (as of 2026-04-21)

- 1T-parameter MoE with 32B active parameters, 384 experts, 256K context, native multimodal support, and INT4 quantization
- Moonshot claims open-source SOTA on HLE w/ tools (54.0), SWE-Bench Pro (58.6), SWE-bench Multilingual (76.7), and BrowseComp (83.2)
- Launch materials emphasize long-horizon execution: 4,000+ tool calls, 12+ hour runs, and up to 300 parallel sub-agents via Claw Groups
- Day-0 ecosystem support includes vLLM, OpenRouter, Ollama, Cloudflare Workers AI, Baseten, MLX, Hermes Agent, and OpenCode
- Moonshot also claims a 68.6% win+tie rate vs Gemini 3.1 Pro on frontend design tasks

## Demonstrated capabilities

- Moonshot reports a 5-day autonomous infrastructure-agent run handling monitoring, incident response, and system operations
- A Zig inference-engine demo for Qwen3.5-0.8B ran for 12 hours with 4K+ tool calls and reported throughput rising from about 15 to 193 tokens/sec
- An `exchange-core` matching-engine optimization demo reportedly ran for 13 hours and improved medium throughput from 0.43 to 1.24 MT/s

## Caveats

- The strongest comparative claims are vendor-reported; some competitor numbers were re-evaluated by Moonshot under its own setup and should be treated as directional
- "Open-source SOTA" here is a claim about the open-weight field in the launch materials, not an independently verified leaderboard ruling

## Recent changes

- [2026-04-21] Model released and open-sourced; Claw Groups research preview launched

## Sources

- [Kimi K2.6 — Advancing Open-Source Coding](../sources/articles/kimi-k2-6-blog.md)
- [AINews — Moonshot Kimi K2.6, Hermes Agent, Codex Chronicle (2026-04-21)](../sources/newsletters/ainews-2026-04-21.md)
