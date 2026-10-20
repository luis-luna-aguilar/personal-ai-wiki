---
title: Introducing Claude Opus 5.5
type: source
source_type: article
source_file: raw/articles/2026-10-20-anthropiccom-claude-opus-5-5.md
url: https://www.anthropic.com/claude-opus-5-5
ingested: 2026-10-20
domains: [models, coding]
---

# Introducing Claude Opus 5.5

Anthropic's launch post for Claude Opus 5.5, the first model in the Claude 5.5 family and its first release since Dario Amodei's "We Must Pace the Frontier" essay. Anthropic says it performs at the level of Fable 5.1 on most work, costs about 40% less than Opus 5 to run, writes more clearly, and ships with Fable 5.1-class safeguards. It includes a benchmark table against Fable 5.1, Opus 5, GPT-6 Astra and GPT-5.6 Sol, a pricing table, about two dozen customer quotes, and a long safety section. The post carries no publication date; it says Sonnet 5.5 and Haiku 5.5 "will follow in the coming weeks," so it predates both. The ingest date (2026-10-20) is used.

## Influenced pages
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — new page: pricing, benchmarks, safeguards, availability
- [Claude Opus 5](../../history/models/claude-opus-5.md) — archived as superseded
- [State of Models](../../state-of/models.md) — Opus 5.5 replaces Opus 5 in Frontier models

## Key claims extracted
- Available on all platforms (AWS, Google Cloud, Microsoft Azure) and on the Claude Platform as `claude-opus-5-5`; thinking can no longer be switched off.
- Pricing per 1M tokens: input $4, output $20, cache writes $5, cache reads $0.20 (Opus 5: $5 / $25 / $6.25 / $0.50). Fast mode up to 2.5x speed at $8 / $40. About 40% cheaper than Opus 5 on typical workloads; output 30%+ faster.
- Benchmarks (Opus 5.5 / Fable 5.1 / Opus 5 / GPT-6 Astra / GPT-5.6 Sol): Terminal-Bench 4.0 66.4 / 55.8 / 52.3 / 57.9 / 37.3; FrontierCode v1.1 54.4 / 50.3 / 48.0 / 53.3 / 47.5; CursorBench 4.0 57.8 / 51.8 / 46.6 / — / 41.7; GDPval-AA v2.1 1846 / 1735 / 1708 / 1542 / 1588; AutomationBench 40.0 / 31.4 / 26.9 / 41.4 / 28.8; HLE with tools 67.7 / 65.6 / 63.6 / 57.2 / —; Terminal-Bench-Science 0.1 58.7 / 52.6 / 29.0 / 64.6 / 22.4; OSWorld 2.1 81.8 / 80.7 / 74.0.
- Anthropic says the real-world gap to Fable 5.1 is narrower than benchmark scores suggest.
- Internal test: Opus 5.5 and Fable 5.1 both ported HAProxy from C to Rust; Opus 5.5 finished in 9.5 hours against 12 and cost 51% less.
- Customer reports: Deloitte 72% of known code-review bugs at low effort against Opus 5's 56% at high; Optiver matched Opus 5 quality in about half the turns, cutting cost 40–50%; Hebbia 86.6% rubric coverage against Opus 5's 60.3%; Box used a third of Opus 5's tokens.
- Safety: best-ever automated behavioral-audit scores; about 85% fewer containment-boundary attempts than Opus 5 or Mythos 5.1; often suspects it is being evaluated. Cyber, biology and anti-distillation safeguards similar to Fable 5.1, falling back transparently (most cyber tasks reroute to Opus 4.8).
- Five-hour usage limits raised on Pro, Max, Team and seat-based Enterprise plans.
