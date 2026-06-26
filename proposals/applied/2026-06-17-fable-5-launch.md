---
type: proposal
source: raw/newsletters/2026-06-10-ainews-anthropic-claude-fable-5-mythos-but-saf.md
status: pending
created: 2026-06-17
---

# Proposal: Claude Fable 5 launch details

## Summary

Anthropic released Claude Fable 5 on June 9–10 as its first generally available Mythos-class model (at least 2× Opus size). The launch introduced comprehensive benchmark data, pricing, usage posture guidance, and two controversial policy terms (no ZDR, silent RSI suppression). The existing wiki page (`claude-fable-5.md`) captures the ban and controversy context from the June 13-17 period but is missing the launch benchmarks, pricing, and Every's independent vibe-check data.

## Intended changes

- [x] **Update** `wiki/models/claude-fable-5.md` — add launch benchmarks, pricing/context details, usage posture, Every Senior Engineer benchmark
    > See draft below (diff from existing page)

- [x] **Update** `wiki/state-of/models.md` — add benchmark specifics and pricing to the Fable 5 entry
    > **Before:** `- [Claude Fable 5](../models/claude-fable-5.md) — Anthropic; #1 DeepSWE, FrontierSWE, FrontierMath (87-88%), and Epoch Capabilities Index (161) at launch — **currently suspended globally under US export controls** *(as of 2026-06-17)*`
    > **After:** `- [Claude Fable 5](../models/claude-fable-5.md) — Anthropic; SWE-Bench Pro 80.3%, FrontierCode Diamond 29.3%, HLE 53%, Terminal-Bench 2.1 88.0%, AA Intelligence Index #1 (64.9); $10/$50/M tokens; **currently suspended globally under US export controls** *(as of 2026-06-17)*`

- [x] **Create** `wiki/sources/newsletters/ainews-fable5-june-2026.md` — source summary for AINews June 10 newsletter
    > See draft below

- [x] **Create** `wiki/sources/articles/every-fable5-vibe-check.md` — source summary for Every vibe check article
    > See draft below

## Page drafts

### wiki/models/claude-fable-5.md (updated)

Replace the `## Benchmark record (pre-ban)` and `## What Fable 5 was notable for` sections and add a `## Pricing & access` section; add new sources. Full updated page:

````md
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
````

### wiki/sources/newsletters/ainews-fable5-june-2026.md (new)

```md
---
title: "AINews — Claude Fable 5 / Mythos 5 launch (June 10)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-10-ainews-anthropic-claude-fable-5-mythos-but-saf.md
published: 2026-06-10
ingested: 2026-06-17
domains: [models, coding]
---

# AINews — Claude Fable 5 / Mythos 5 launch (June 10)

AINews (Latent Space) full coverage of the Fable 5 / Mythos 5 release. Primary source for launch benchmarks, pricing, controversial policy terms, and community reaction.

## Influenced pages
- [Claude Fable 5](../../models/claude-fable-5.md) — benchmark record, pricing, usage posture
- [State of Models](../../state-of/models.md) — entry update

## Key claims extracted
- Fable 5 and Mythos 5 share the same underlying model; Fable has added safeguards
- Pricing: $10/$50 per million input/output tokens; $12.50/1 cache write/read; 1M context
- SWE-Bench Pro: 80.3% (vs GPT-5.5 58.6%)
- FrontierCode Diamond: Fable 5 29.3%, Mythos 5 30.9% (vs prior best 13.4%)
- Terminal-Bench 2.1: 88.0% (Cline), CursorBench SOTA 72.9%, HLE 53%
- AA Intelligence Index: #1 at 64.9; GDPval-AA Elo 1932
- No ZDR: 30-day retention for all Mythos-class traffic; silent RSI suppression ~0.03% of traffic
- Community reaction: wide backlash on silent RSI suppression as "ladder-pulling" against open research
```

### wiki/sources/articles/every-fable5-vibe-check.md (new)

```md
---
title: "Vibe Check: Fable 5 Is the Best Coding Model in the World — Dan Shipper / Katie Parrott"
type: source
source_type: article
source_file: raw/articles/2026-06-17-everyto-vibe-check-anthropic-mythos-our-fable-vibe-check.md
url: https://every.to/vibe-check/anthropic-mythos-our-fable-vibe-check
published: 2026-06-08
ingested: 2026-06-17
domains: [models, coding]
---

# Vibe Check: Fable 5 — Every (Dan Shipper & Katie Parrott)

Every's day-zero vibe check on Fable 5. Seven team members tested it across coding, writing, business strategy, data analysis, and growth for a week. Partially paywalled; key verdict and benchmarks accessible.

## Influenced pages
- [Claude Fable 5](../../models/claude-fable-5.md) — Senior Engineer benchmark, usage verdict, one-shot examples

## Key claims extracted
- Every Senior Engineer benchmark: Fable 5 91/100 vs Opus 4.8 63 vs GPT-5.5 62 — "near the range of human engineers who've taken it"
- Verdict: "Strong closer that wants a clear target — treat it as an asynchronous agent, not a chat partner"
- Level 7–8 AI users found it paradigm-shifting; lower-level users struggled to find uses
- One-shot projects: 3D Library of Babel, subscriber survey analysis, custom lecture app
- Pricing: ~2× Opus 4.8, ~3× Sonnet 4.6; uses 500k–1M tokens per long task
- Not ideal for fast creative iteration; best for large, delegable, high-stakes assignments
```
