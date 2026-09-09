---
title: Qwen 3.8
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [alibaba, open-weights]
as_of: 2026-09-01
sources: [alibaba-qwen38-preview-2026-07-20, ainews-china-policy-openweight-2026-07-21, ainews-qwen38-max-launch-2026-08-04, ainews-spacexai-grok-46-and-grok-bot-2026-08-13, ainews-memory-prices-openai-pause-2026-08-19, ainews-death-of-params-glm-53-2026-08-20, ainews-fablemythos-51-2026-09-02]
---

# Qwen 3.8

Alibaba's flagship after Qwen 3.7. Entered live preview 2026-07-20, shipped as a full launch on 2026-08-04 as Qwen3.8-Max, and shipped open weights for Max on 2026-08-13 (text-only initial drop, no vision yet). The promised Qwen3.8-27B sibling gained enough independent momentum in the following week to warrant its own page — see [Qwen 3.8 27B](qwen-3-8-27b.md).

## Current status (as of 2026-08-13)

- Qwen3.8-Max: 2.4T total parameters, ~95B active per token (third-party estimate, ~4% activation ratio); 1M context; API priced at $2/M input, $6/M output, $0.25/M cached tokens
- Open weights shipped 2026-08-13 for Qwen3.8-Max (text-only initial drop, no vision); day-0 vLLM support plus vendor-specific 4-bit checkpoints for NVIDIA B300 and AMD MI355X; Together AI and Baseten also announced immediate support
- Frontend Code Arena: #4 overall at 1,668 Elo, behind only Claude Opus 5 (1,705) and Kimi K3 (1,676)
- Vals AI Index: 66.1, matching Claude Opus 4.7 at roughly 2.3x lower cost per test; SWE-bench 87.3% (ahead of GPT-5.5 and GLM-5.2, behind Claude Opus 4.8's 89.2%); Terminal-Bench 2.1 at 67.4, up from 57.5 for Qwen 3.7 Max about two and a half months earlier
- Vision Arena: #2 at 1,305, 13 points behind Claude Fable 5
- Licensing: terms reportedly restrict use or download in the US, EU, UK, and Korea — a similar complaint was raised about MiniMax H3 the same week, raising the question of how "open" a geographically-restricted release really is for Western teams

## Qwen3.8-Max-0902 refresh (as of 2026-09-01)

Alibaba released Qwen3.8-Max-0902, a refreshed 2.4T-parameter build with 1M context, priced at $2/M input and $6/M output plus cache-hit discounts. Arena reported it debuting #1 on Code Arena: WebDev (1691 Elo), just ahead of Claude Opus 5 Max and Kimi K3 Max, and landing on the current best price/performance frontier.

## Why it matters

Succeeds [Qwen 3.7](qwen-3-7.md) as Alibaba's flagship, moving from preview to a real open-weight-committed launch just over two weeks after Kimi K3. If the license restrictions hold as reported, this complicates the "open weights as sovereignty infrastructure" argument tracked on [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md) — the weights may not be legally usable by the Western teams that argument targets.

## Caveats

- Active-parameter count (~95B) and some benchmark framing come from third-party summaries (ZhihuFrontier), not Alibaba's own spec sheet
- The license-restriction claim comes from a single X post (@ostrisai) reacting to the terms; no clarifying statement from Alibaba appears in the source coverage

## Recent changes

- [2026-09-01] Qwen3.8-Max-0902 refresh debuts #1 on Arena's Code Arena: WebDev (1691), ahead of Claude Opus 5 Max and Kimi K3 Max.
- [2026-08-20] The promised Qwen3.8-27B sibling gained enough independent momentum (local-model rankings, benchmark parity claims, community builds) to get its own page — see [Qwen 3.8 27B](qwen-3-8-27b.md).
- [2026-08-13] Open weights shipped for Qwen3.8-Max (2.4T/~95B active MoE) — text-only initial drop, no vision yet; day-0 vLLM support plus 4-bit checkpoints for NVIDIA B300/AMD MI355X; Together AI and Baseten also added support
- [2026-08-04] Full launch as Qwen3.8-Max: 2.4T/~95B active, real benchmarks (Frontend Code Arena #4, SWE-bench 87.3%, Terminal-Bench 2.1 67.4), open weights promised "next week" alongside a Qwen3.8-27B sibling; license reportedly restricts use/download in US/EU/UK/Korea
- [2026-07-21] Third-party roundup reports 2.4T parameters, native video understanding, still inconsistent on long-horizon tasks
- [2026-07-20] Alibaba puts Qwen3.8-Max into live preview, claiming near-Fable-5 capability

## Sources

- [Superhuman — Alibaba teases new frontier model](../sources/newsletters/alibaba-qwen38-preview-2026-07-20.md)
- [AINews — Open-weight competition, Chinese model policy, geopolitics of AI](../sources/newsletters/ainews-china-policy-openweight-2026-07-21.md)
- [AINews — Qwen 3.8 Max (2.4T) and 27B ship](../sources/newsletters/ainews-qwen38-max-launch-2026-08-04.md)
- [AINews — SpaceXAI Grok 4.6 and Grok Bot (Qwen3.8-Max open weights)](../sources/newsletters/ainews-spacexai-grok-46-and-grok-bot-2026-08-13.md)
