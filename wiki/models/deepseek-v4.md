---
title: DeepSeek V4
type: model
domains: [models, coding, agents]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-04-24
sources: [deepseek-v4-preview]
---

# DeepSeek V4

DeepSeek's April 2026 preview release for long-context open agent workloads. The key claim is not only bigger context, but cheaper usable context: V4 is explicitly optimized for long-running tool-use traces and agent loops, with much lower KV-cache cost and stronger multi-step tool behavior than the prior generation.

## Current status (as of 2026-04-24)

- Preview release with two open-weight checkpoints: **V4-Pro** (1.6T total / 49B active) and **V4-Flash** (284B total / 13B active)
- 1M-token context window; positioning is heavily agent-oriented rather than only chatbot-oriented
- Hugging Face technical analysis highlights major efficiency gains vs DeepSeek-V3.2: lower per-token FLOPs and much smaller KV cache at long context
- Competitive agent results rather than clean category leadership: Terminal Bench 2.0 67.9, SWE Verified 80.6, MCPAtlas Public 73.6, Toolathlon 51.8
- Uses explicit tool-use shaping: interleaved thinking across tool rounds, a dedicated tool-call schema, and RL infrastructure tuned for sandboxed agent training

## Strengths

- Strongest current DeepSeek signal for long-horizon agent traces rather than only static coding prompts
- Open-weight release with unusually serious attention to long-context economics
- Competitive with frontier closed models on several agent benchmarks without needing a proprietary-only deployment story

## Weaknesses / caveats

- Still a preview release
- Benchmark framing is mixed: competitive, but not obvious state-of-the-art across the board
- Current technical detail comes more from the Hugging Face analysis of the release than from a full first-party DeepSeek blog post in this source set

## Recent changes

- [2026-04-24] Preview released: DeepSeek moves its open-model story toward 1M-context agent workloads, hybrid attention for cheaper long traces, and stronger tool-use positioning

## Sources

- [[sources/articles/deepseek-v4-preview]]
