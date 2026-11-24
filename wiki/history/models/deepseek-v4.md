---
title: DeepSeek V4 Flash
type: model
domains: [models, coding, agents]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-08-22
sources: [ainews-not-much-happened-2026-08-01, ainews-10-worse-100x-cheaper-2026-08-22]
---

# DeepSeek V4 Flash (archived)

The V4 Flash tier of [DeepSeek V4](../../models/deepseek-v4.md) (284B total / 13B active, 1M context, MIT). **Superseded by [DeepSeek V4.1 Flash](../../models/deepseek-v4-1-flash.md); moved here from the live DeepSeek V4 page on 2026-10-28.** Its scores used an earlier version of Artificial Analysis' Intelligence Index and are not comparable with V4.1-era scores.

## Archived from current page on 2026-10-28

- **V4 Flash's current builds:** the post-training-only 0731 update (Terminal-Bench 82.7, AA Intelligence Index 50, one point behind GPT-5.6 Luna; open weights with day-0 vLLM) and the API-only V4-Flash-Vision-Exp (2026-08-22), which adds text+image input and reports 83.9 Terminal-Bench 2.1; Vision-Exp weights not yet found on Hugging Face
- V4 Flash pricing (as of 2026-08): $0.14 / $0.28 per 1M input/output tokens.

## V4-Flash 0731 update (as of 2026-07-31)

DeepSeek shipped a post-training-only upgrade to V4-Flash — same 284B total / 13B active architecture, no scaling or architecture change:

- **Benchmarks:** Terminal-Bench 56.9 → 82.7 (+25.8); Artificial Analysis Intelligence Index 40 → 50, one point behind GPT-5.6 Luna's 51 at roughly 60% lower cost per task on DeepSeek's own API; GDPval-AA v2 Elo 1189 → 1559; output-token usage down 12% versus the predecessor.
- **Pricing:** $0.14 / $0.28 per 1M input/output tokens, with a 98% cache-hit discount down to $0.0028/1M cached tokens.
- **Open weights:** released under MIT with immediate day-0 vLLM support — 256 routed experts, 6 active per token, three reasoning-effort levels, and an included DSpark speculative-decoding module enabled via a single flag. Local/quantized builds landed same-day (Unsloth: ~168GB RAM for lossless 4-bit, ~110GB for 3-bit).
- **Scope:** this update applies to V4-Flash only. V4-Pro's API, app, and web product are unchanged; an official V4-Pro release remains pending.
- Widely read as a direct competitive response to OpenAI's GPT-5.6 price cuts the day before.

## V4-Flash-Vision-Exp adds multimodal (as of 2026-08-22)

DeepSeek shipped DeepSeek-V4-Flash-Vision-Exp, adding multimodal (text+image) input to V4-Flash while reportedly preserving its existing text capability:

- **Benchmarks (per AINews, relaying DeepSeek's release claims):** 83.9 Terminal-Bench 2.1, 75.9 Toolathlon-Verified, 64.3 Chartography — a large jump over the prior V4-Flash-0731 release, positioned as closing the multimodal-agent gap to Claude Opus-4.8
- **API:** mixed text+image support via base64, external URLs, or a new Files API for reusable image uploads across requests; images billed at up to 384 tokens each, at V4-Flash pricing
- **Availability:** live via the DeepSeek API (`model='deepseek-v4-flash-vision-exp'`); weights not yet found on Hugging Face as of this writing, unlike DeepSeek's prior fully open-weighted releases

## Recent changes (archived 2026-10-28)

- [2026-08-22] V4-Flash-Vision-Exp adds multimodal (text+image) input while preserving V4-Flash's text capability; reported benchmarks (83.9 Terminal-Bench 2.1, 75.9 Toolathlon-Verified, 64.3 Chartography) position it as closing the multimodal-agent gap to Opus-4.8; API-only at launch, weights not yet found on Hugging Face.
- [2026-07-31] V4-Flash 0731: post-training-only update jumps Terminal-Bench to 82.7 (+25.8) and AA Intelligence Index to 50 (from 40), now 1pt behind GPT-5.6 Luna; open-weighted under MIT with day-0 vLLM support; V4-Pro unaffected, still pending its own release.

## Sources

- [AINews — not much happened today (DeepSeek V4-Flash 0731)](../../sources/newsletters/ainews-not-much-happened-2026-08-01.md)
- [AINews — 10% worse, 100x cheaper, 10000x faster: Why Simulation is taking over](../../sources/newsletters/ainews-10-worse-100x-cheaper-2026-08-22.md)
