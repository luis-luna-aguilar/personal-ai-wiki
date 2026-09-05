---
title: Grok 4.5
type: model
domains: [models]
subcategory: frontier-model
tags: [xai]
as_of: 2026-07-08
sources: [cursor-blog-grok-4-5-launch-2026-07, ainews-spacexai-grok-45-2026-07-09]
---

# Grok 4.5

xAI's (rebranded SpaceXAI following its Cursor acquisition) first model co-trained with Cursor — a 1.5T-parameter mixture-of-experts model, 3x larger than Grok 4.3. Positioned as "Opus-class" but faster, more token-efficient, and lower cost, and as xAI's first model trained for more than software engineering: a deliberately broad STEM/knowledge-work data mix alongside coding and agent trajectories drawn from Cursor's own usage data.

## Current status (as of 2026-07-08)

- Mixture-of-experts; 1.5T parameters, 3x Grok 4.3 (Musk disclosure, per Artificial Analysis via AINews); trained jointly by xAI/SpaceXAI and Cursor on trillions of tokens of Cursor codebase + developer-agent interaction data, plus broader STEM/knowledge-work data (Cursor blog)
- Pricing: $2/M input, $6/M output (base); $4/M input, $18/M output (fast variant) (Cursor blog); cache hits discounted 75% to $0.50/M; inputs over 200K tokens cost double (per Artificial Analysis, via AINews)
- 500K context window, down from Grok 4.3's 1M (per Artificial Analysis, via AINews); Musk said a return to 1M was expected "by next week"
- Available immediately in Cursor (desktop, web, iOS, CLI, SDK) with double usage for the first week; also available in Grok Build and via API from day 0 (per AINews)
- Per Artificial Analysis, via AINews: #4 Intelligence Index (score 54, +16 vs. Grok 4.3), behind Fable 5/GPT-5.5/Opus 4.8; GDPval-AA v2 Elo 1543 (#4); Coding Agent Index 76 in Grok Build (on par with GPT-5.5 in Codex, below Fable 5 in Claude Code); ~14K avg output tokens per Intelligence Index task, 60%+ lower than Opus 4.8; $0.31 cost per Intelligence Index task
- Composer 2.5 remains Cursor's separate, smaller-weight-class model; Cursor plans to keep releasing models in that size tier alongside the Grok 4.5 weight class

## Why it matters

Grok 4.5 is the first public output of the SpaceX-Cursor tie-up: a frontier-adjacent model trained partly on Cursor's own developer-agent interaction data, deliberately broadened beyond pure coding. It competes on cost/token-efficiency rather than raw benchmark supremacy — Musk's "Opus-class, but faster, more token-efficient and lower cost" framing, with list pricing of $2/$6 against $5/$30 for GPT-5.6 and $5/$25 for Opus 4.8 (user comparisons relayed by AINews) and markedly fewer output tokens per task.

## Weaknesses / caveats

- Context window regressed from Grok 4.3's 1M to 500K at launch (expected to be restored)
- Below Fable 5/GPT-5.5/Opus 4.8 on Intelligence Index and GDPval-AA (per Artificial Analysis, via AINews); positioned on cost/speed, not top-line capability
- All benchmark and size figures are secondary so far (AINews relaying Artificial Analysis and Musk); no primary AA or xAI source captured yet
- CursorBench-style comparisons are flagged by Cursor itself as advantaged by the accidental inclusion of an earlier Cursor codebase snapshot in training data (removed for future models)

## Recent changes

- [2026-07-08] Launched: 1.5T MoE co-trained with Cursor, $2/$6 pricing, available across all Cursor surfaces plus Grok Build and API

## Sources

- [Cursor — Introducing Grok 4.5](../sources/articles/cursor-blog-grok-4-5-launch-2026-07.md)
- [AINews — SpaceXAI launches Grok 4.5](../sources/newsletters/ainews-spacexai-grok-45-2026-07-09.md)
