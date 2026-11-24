---
title: 'AINews — Claude Opus 5.5 launch roundup: independent evals, cost per task, safeguards'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-23-ainews-claude-opus-55-the-new-default-model-fo.md
url: https://www.latent.space/p/ainews-claude-opus-55-the-new-default
published: 2026-09-23
ingested: 2026-10-20
domains: [models, coding]
---

# AINews — Claude Opus 5.5 launch roundup

The launch-day issue covering Claude Opus 5.5 (released 2026-09-22, about an hour before GPT-6 Sol and Luna). It collects Anthropic's launch claims, third-party and partner evals, an Artificial Analysis cost-per-task breakdown, effort-scaling and ProgramBench caveats, the safeguard over-triggering complaints, and demos of visual work built from code. AINews switched its own pipeline to Opus 5.5 on the strength of its writing. This page covers the Opus 5.5 story only.

## Influenced pages
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — launch date, independent evals, cost and effort caveats, safeguard over-triggering
- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — list price vs cost per task

## Key claims extracted
- Opus 5.5 launched 2026-09-22; default in Claude Code and the Claude app at medium effort
- #1 Vals Index and Vals RSI Index; CursorBench 57.8% (new top); FrontierCode 1.1 Extended 65.3% (#1); FrontierSWE 62.3% (#2 behind GPT-6 Astra 65.5%)
- List price cut 20% to $4/$20; AA: $5.98 per Intelligence Index task at max effort vs Opus 5's $5.86, so the "40% cheaper" claim applies at default medium effort
- On FrontierCode, xhigh effort costs ~2.8x medium for a 3.2-point lower score
- ProgramBench near-100% figure is from a 166/200 subset and uses average test pass rate
- First Opus with Fable 5.1-class safeguards; early over-triggered fallbacks reported
