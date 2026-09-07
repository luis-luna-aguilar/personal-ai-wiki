---
title: Qwen 3.8
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [alibaba, open-weights]
as_of: 2026-08-04
sources: [alibaba-qwen38-preview-2026-07-20, ainews-china-policy-openweight-2026-07-21, ainews-qwen38-max-launch-2026-08-04]
---

# Qwen 3.8

Alibaba's flagship after Qwen 3.7. Entered live preview 2026-07-20 and shipped as a full launch on 2026-08-04 as Qwen3.8-Max, with open weights promised "next week" for both Qwen3.8-Max and a smaller companion, Qwen3.8-27B.

## Current status (as of 2026-08-04)

- Qwen3.8-Max: 2.4T total parameters, ~95B active per token (third-party estimate, ~4% activation ratio); 1M context; API priced at $2/M input, $6/M output, $0.25/M cached tokens
- Open weights promised "next week" for both Qwen3.8-Max and a companion Qwen3.8-27B
- Frontend Code Arena: #4 overall at 1,668 Elo, behind only Claude Opus 5 (1,705) and Kimi K3 (1,676)
- Vals AI Index: 66.1, matching Claude Opus 4.7 at roughly 2.3x lower cost per test; SWE-bench 87.3% (ahead of GPT-5.5 and GLM-5.2, behind Claude Opus 4.8's 89.2%); Terminal-Bench 2.1 at 67.4, up from 57.5 for Qwen 3.7 Max about two and a half months earlier
- Vision Arena: #2 at 1,305, 13 points behind Claude Fable 5
- Licensing: terms reportedly restrict use or download in the US, EU, UK, and Korea — a similar complaint was raised about MiniMax H3 the same week, raising the question of how "open" a geographically-restricted release really is for Western teams

## Why it matters

Succeeds [Qwen 3.7](qwen-3-7.md) as Alibaba's flagship, moving from preview to a real open-weight-committed launch just over two weeks after Kimi K3. If the license restrictions hold as reported, this complicates the "open weights as sovereignty infrastructure" argument tracked on [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md) — the weights may not be legally usable by the Western teams that argument targets.

## Caveats

- Active-parameter count (~95B) and some benchmark framing come from third-party summaries (ZhihuFrontier), not Alibaba's own spec sheet
- Weights not yet released at time of writing — "next week" is Alibaba's stated timeline, not a confirmed date
- The license-restriction claim comes from a single X post (@ostrisai) reacting to the terms; no clarifying statement from Alibaba appears in the source coverage

## Recent changes

- [2026-08-04] Full launch as Qwen3.8-Max: 2.4T/~95B active, real benchmarks (Frontend Code Arena #4, SWE-bench 87.3%, Terminal-Bench 2.1 67.4), open weights promised "next week" alongside a Qwen3.8-27B sibling; license reportedly restricts use/download in US/EU/UK/Korea
- [2026-07-21] Third-party roundup reports 2.4T parameters, native video understanding, still inconsistent on long-horizon tasks
- [2026-07-20] Alibaba puts Qwen3.8-Max into live preview, claiming near-Fable-5 capability

## Sources

- [Superhuman — Alibaba teases new frontier model](../sources/newsletters/alibaba-qwen38-preview-2026-07-20.md)
- [AINews — Open-weight competition, Chinese model policy, geopolitics of AI](../sources/newsletters/ainews-china-policy-openweight-2026-07-21.md)
- [AINews — Qwen 3.8 Max (2.4T) and 27B ship](../sources/newsletters/ainews-qwen38-max-launch-2026-08-04.md)
