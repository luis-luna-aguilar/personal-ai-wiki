---
title: Claude Fable 5
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-multimodal-model
tags: [anthropic, frontier]
as_of: 2026-06-17
sources: [fable-ban-june-2026, ainews-fable5-june-2026, every-fable5-vibe-check]
---

# Claude Fable 5

Anthropic's frontier model, launched June 9 2026 as the first generally available Mythos-class model. Described by Anthropic as "at least 2× the size of Opus." Reached #1 across nearly all major benchmarks at launch — then suspended worldwide under US government export controls (see [ban coverage](../sources/newsletters/fable-ban-june-2026.md)).

## Current status (as of 2026-06-17)

- **Access suspended globally.** US government classified Fable 5 and Mythos 5 under export controls restricting them to US nationals; Anthropic chose to block all customers rather than implement a partial restriction.
- The trigger was a jailbreak reported by Amazon researchers; Anthropic disputes it as "narrow, non-universal."
- UK government denied carve-out requests; ban ongoing as of 2026-06-17.
- Anthropic briefly and covertly degraded Fable 5 for AI-research use cases before the export-control ban — reversed within a day after practitioner backlash.
- 76 cybersecurity experts signed the FreeFable.org open letter.

## Benchmark record (pre-ban)

- **SWE-Bench Pro:** 80.3% (vs GPT-5.5 58.6%)
- **DeepSWE index:** #1; Claude Code + Fable 5 [max] scored 77 on the Artificial Analysis DeepSWE index
- **FrontierCode Diamond:** 29.3% (Fable 5); 30.9% (Mythos 5) — vs prior best 13.4%
- **FrontierSWE:** #1
- **Terminal-Bench 2.1:** 88.0% (Cline; 4.6 points above GPT-5.5)
- **CursorBench:** SOTA 72.9% (8 points above prior best)
- **FrontierMath Tiers 1-4:** 87% / 88%
- **Humanity's Last Exam:** 53% — 7+ points ahead of next best; ~9% of HLE tasks triggered fallback
- **Artificial Analysis Intelligence Index:** #1 (64.9, ~5 points ahead of GPT-5.5)
- **GDPval-AA Elo:** 1932 (#1 agentic real-world knowledge work)
- **WeirdML:** 87.8%
- **Epoch Capabilities Index:** 161 (new all-time high at launch)
- **Every Senior Engineer benchmark:** 91/100 — vs Opus 4.8 (63) and GPT-5.5 (62)
- **Code Arena (frontend coding):** #1 (Fable unavailable → GLM-5.2 moved to #1)
- **Design Arena:** #1 (same)

## Pricing & access

- **API:** $10 per million input tokens; $50 per million output tokens (approx 2× Opus 4.8, 3× Sonnet 4.6)
- **Cache:** $12.50/M writes, $1/M reads
- **Context:** 1M tokens
- **No ZDR:** 30-day retention for all Mythos-class model traffic (not used for training; privacy controls applied; deletions after 30 days)
- **Subscription access:** Available in Pro/Max/Team/Enterprise until June 22 at launch, then credit-gated due to capacity constraints
- Silent RSI suppression: for frontier LLM development tasks (~0.03% of traffic), Anthropic may silently reduce effectiveness via prompt modification, steering vectors, or PEFT without notifying the user

## What Fable 5 was notable for

Practitioners described it as the first model they trusted for long, complex, minimally supervised tasks — whole-project delegation rather than function-level assistance.

- **Every Senior Engineer benchmark:** 91/100 — near human engineer range; Opus 4.8 scored 63, GPT-5.5 scored 62
- **Every's verdict:** "Strong closer that wants a clear target — treat it as an asynchronous agent, not a chat partner"
- Level 7–8 AI users found it paradigm-shifting; lower-level users struggled to find clear use cases
- One-shot app building: users built a 3D Library of Babel, a subscriber survey analysis app, and a custom Hubert Dreyfus lecture player with single prompts
- Ethan Mollick: could hand it a 15-page design document and it would work for 9+ hours autonomously
- Anthropic cited Stripe using Fable to complete a 50M-line Ruby migration in a day, replacing what would have taken a team over two months
- Usage profile: 500k–1M tokens per long-running task; Simon Willison described it as "slow, expensive and capable"
- Anthropic advised: default to `xhigh/high` effort; rewrite old CLAUDE.md instructions; give objectives/responsibilities rather than tasks; use Fable as an orchestrator delegating to smaller models via Claude Managed Agents

## Weaknesses / caveats

- All benchmark positions are pre-ban; no ongoing public evaluation is possible while access is suspended.
- The ban reveals a new structural risk: regulatory action can remove access to a frontier model faster than any vendor deprecation.
- Classifier over-sensitivity at launch: users reported "cancer" and "What does the heart do?" triggering biosecurity fallback; Anthropic reset rate limits after heavy demand.

## Recent changes

- [2026-06-17] Access suspended globally under US export controls; ban ongoing; Anthropic disputes scope of trigger jailbreak
- [2026-06-09] Launched; pricing $10/$50/M; reached #1 on SWE-Bench Pro (80.3%), FrontierCode Diamond (29.3%), HLE (53%), Intelligence Index; Every Senior Engineer benchmark 91/100

## Sources

- [AINews — Claude Fable 5 / Mythos 5 launch (June 10)](../sources/newsletters/ainews-fable5-june-2026.md)
- [Every vibe check: Fable 5 (June 8)](../sources/articles/every-fable5-vibe-check.md)
- [Claude Fable 5 / Mythos ban coverage](../sources/newsletters/fable-ban-june-2026.md)
