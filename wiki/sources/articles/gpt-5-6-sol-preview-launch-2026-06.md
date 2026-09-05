---
title: "Previewing GPT-5.6 Sol: a next-generation model"
type: source
source_type: article
source_file: raw/articles/2026-08-25-openaicom-index-previewing-gpt-5-6-sol.md
url: https://openai.com/index/previewing-gpt-5-6-sol/
published: 2026-06-26
ingested: 2026-08-25
domains: [models, coding, cybersecurity]
---

# Previewing GPT-5.6 Sol: a next-generation model

OpenAI's own announcement of the GPT-5.6 family (Sol/Terra/Luna) as a restricted preview, launched June 26, 2026 at the request of the US government pending a cyber Executive Order framework. `scripts/fetch_url.py` was blocked by a Cloudflare JS challenge; content was retrieved via the `aside-browser` skill fallback (real browser render). This resolves a long-standing caveat on `models/gpt-5-6-sol.md`, which previously relied only on METR's secondary evaluation.

## Influenced pages

- [GPT-5.6 Sol](../../models/gpt-5-6-sol.md) — primary-source capability/pricing/safety detail added; caveat resolved
- [Restricted frontier deployment](../../trends/restricted-frontier-deployment.md) — corroborates the restricted-preview episode's existence and terms

## Key claims extracted

- GPT-5.6 family: Sol (flagship), Terra (balanced, competitive with GPT-5.5 at 2x cheaper), Luna (fast/affordable, lowest cost)
- Pricing per 1M tokens: Sol $5/$30, Terra $2.50/$15, Luna $1/$6; new cache-breakpoint pricing (1.25x uncached rate for cache writes, 90% discount retained for cache reads)
- New `max` reasoning effort and `ultra` subagent-fan-out mode
- Terminal-Bench 2.1: new state of the art among a comparison set including Claude Mythos 5, Claude Fable 5, Claude Opus 4.8, Gemini 3.1 Pro Preview, GPT-5.5 (exact per-model scores not reliably extractable from the fetched page's flattened chart text)
- GeneBench v1: stronger than GPT-5.5, fewer tokens
- Cybersecurity: competitive with Claude Mythos Preview on ExploitBench at ~1/3 the output tokens; does not cross the Cyber Critical Preparedness Framework threshold
- 700,000+ A100-equivalent GPU hours of automated red-teaming for universal jailbreaks; ongoing third-party human red-teaming
- Launched as a restricted preview to trusted partners at US government request; broader ChatGPT/Codex/API availability "planned soon" as of this post
- A linked later OpenAI post ("...GPT-5.6 in Kiro," Aug 24, 2026) shows third-party integration, consistent with broader availability by that date
