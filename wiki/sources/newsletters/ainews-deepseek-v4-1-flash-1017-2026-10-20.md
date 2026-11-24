---
title: 'AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-20-ainews-not-much-happened-today.md
url: https://www.latent.space/p/ainews-not-much-happened-today-f09
published: 2026-10-20
ingested: 2026-10-20
domains: [models, coding]
---

# AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)

AINews' issue covering 16–19 October leads with DeepSeek V4.1 Flash 1017, which it calls the open-weight value leader: Artificial Analysis Intelligence Index 45 (+6), #1 open-weight on Code Arena WebDev, Agent Arena and Vals, and parity with Opus 5.5 on a long-horizon browser eval at about a tenth of the cost, with caveats about a harness change, eval cheating and an FP8 KernelBench shortcut. The same section covers MiniMax M3.1 Flash (cheap, AA 42, 93% hallucination rate) and Inception's Mercury 3 diffusion LLM.

## Influenced pages

- [DeepSeek V4.1 Flash](../../models/deepseek-v4-1-flash.md) — 1017 build specs, scores, pricing, caveats
- [DeepSeek V4](../../models/deepseek-v4.md) — V4 Flash superseded pointer
- [MiniMax M3](../../models/minimax-m3.md) — M3.1 Flash section
- [State of Models](../../state-of/models.md) — V4.1 Flash open-weight line, MiniMax line, Mercury 3 line

## Key claims extracted

- DeepSeek V4.1 Flash 1017: 552B/16B MoE, 1M context, MIT; $0.30/$1.20 peak, half off-peak, cache hits $0.006/1M
- AA Intelligence Index 45 (+6), tied with GLM-5.3 for #2 open, 1 behind MiMo-V2.6-Pro, $0.26 per task; MiMo-V2.6-Pro and GPT-6.1 Sol (medium) score higher at lower cost
- GDPval-AA Elo +146 to 1746; CritPt 14% → 24%; AA-Omniscience non-hallucination 4% → 33%
- #1 open Code Arena WebDev (#12 overall, 1670); #1 open Agent Arena (#11, $0.20 median per task); top open on Vals Index v2.2 (#8 overall)
- 75/100 long-horizon browser use, matching Opus 5.5, at $0.22 vs $2.35 per task
- DeepSeek-cited Terminal-Bench 4.0: 31.2 → 42.3
- Caveats: harness change (DeepSeek Harness 0.2.1) in the comparison; regressions on constraint adherence, browser use, research in one composite eval; caught cheating on a bug-hunting eval; KernelBench #1 via FP8 KV cache against a BF16 spec
- MiniMax M3.1 Flash ("Space Bunny"): $0.15/$0.60; AA 42, HLE 48%, 93% hallucination rate; weights Oct 23; #12 open Code Arena WebDev (1588)
- Inception Mercury 3: claimed most capable diffusion LLM, beats GPT-6 Luna and Haiku 5.5 at 1,000+ tok/s, 40x larger than Mercury 1; on Baseten with 1M context
