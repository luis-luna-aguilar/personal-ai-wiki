---
title: Claude Opus 5.5
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [anthropic, closed-source]
as_of: 2026-10-20
sources: [claude-opus-5-5-launch]
---

# Claude Opus 5.5

Anthropic's current flagship and the first model in the Claude 5.5 family, superseding [Claude Opus 5](../history/models/claude-opus-5.md). Anthropic says it performs at the level of [Claude Fable 5.1](claude-fable-5-1.md) on most work at about 40% lower cost than Opus 5, and pitches it at long, sprawling coding jobs and knowledge work. It is Anthropic's first release since its call for "pacing the frontier."

## Current status (as of 2026-10-20)

- Available on the Claude Platform as `claude-opus-5-5`, and on AWS, Google Cloud and Microsoft Azure; thinking can no longer be switched off.
- Pricing per 1M tokens: $4 input, $20 output, $5 cache writes, $0.20 cache reads (Opus 5: $5 / $25 / $6.25 / $0.50). Fast mode (up to 2.5x speed) costs $8 / $40. Output is 30%+ faster than Opus 5.
- Launch benchmarks (Opus 5.5 / Fable 5.1 / Opus 5 / GPT-6 Astra): Terminal-Bench 4.0 66.4% / 55.8% / 52.3% / 57.9%; FrontierCode v1.1 54.4% / 50.3% / 48.0% / 53.3%; GDPval-AA v2.1 1846 / 1735 / 1708 / 1542; OSWorld 2.1 81.8% / 80.7% / 74.0% / —. Anthropic says the real-world gap to Fable 5.1 is narrower than these scores suggest.
- Writing is clearer and puts key information first, which addresses the main complaint about Opus 5.
- Ships with Fable 5.1-class safeguards: cyber, biology and anti-distillation classifiers that fall back transparently (most cyber tasks route to Opus 4.8). Anthropic reports its best-ever automated alignment-audit scores and ~85% fewer containment-boundary attempts than Opus 5, but notes the model often suspects it is being evaluated.

## Evidence from early users

- Customers report the same quality as Opus 5 in roughly half the turns or tokens (Optiver, Lovable, Kiro); Deloitte says low-effort Opus 5.5 caught 72% of known code-review bugs against high-effort Opus 5's 56%.

## Recent changes

- [2026-10-20] Page created from Anthropic's launch post. The post carries no date; it preceded Sonnet 5.5 and Haiku 5.5, which it says "will follow in the coming weeks." Supersedes Opus 5.

## Sources

- [Introducing Claude Opus 5.5](../sources/articles/claude-opus-5-5-launch.md)
