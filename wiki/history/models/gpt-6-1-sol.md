---
title: GPT-6.1 Sol
type: model
domains: [models, coding, agents]
subcategory: frontier-model
tags: [openai, closed-source]
as_of: 2026-10-19
sources: [ainews-gpt-6-sol-luna-launch-2026-09-23, every-opus-55-sol-split-team-2026-09-27, ainews-gpt-6-1-sol-devday-2026-09-30, ainews-gpt-6-1-sol-evals-2026-10-01, ainews-gpt-6-1-sol-ultrafast-2026-10-08, developersopenaicom-blog-maintaining-software-gpt-6]
---

# GPT-6.1 Sol

OpenAI's current mid-price model in the GPT-6 family, announced at DevDay on 2026-09-29 and pitched as "near-Astra intelligence for a fifth of the price." It replaced GPT-6 Sol a week after that model launched (2026-09-22) and supersedes [GPT-5.6 Sol](../../history/models/gpt-5-6-sol.md). [GPT-6 Astra](gpt-6-astra.md) remains the flagship. The cheapest tier, launched alongside GPT-6 Sol, has its own page: [GPT-6 Luna](../../models/gpt-6-luna.md).

**Superseded by [GPT-6.2 Sol](../../models/gpt-6-2-sol.md) (2026-11-23), at the same $2/$10 price.**

## Current status (as of 2026-10-19)

- **Price:** $2/$10 per 1M input/output tokens; cached input $0.10 (a 95% discount). Same list price as GPT-6 Sol, which was about half of GPT-5.6 Sol's.
- **Artificial Analysis:** one point below Astra on the Intelligence Index, at $0.72 per task vs $3.26 for Astra and $1.04 for GPT-6 Sol. +12 on Terminal-Bench 4.0 and +5 on HLE over GPT-6 Sol; hallucination rate down from 60% to 54%. It emits 10–30% more output tokens than GPT-6 Sol; the per-task saving comes from fewer turns and cheaper cache reads.
- **Leaderboards:** #1 MathArena; #3 Code Arena WebDev (1759, +70 over GPT-6 Sol); #1 on Arena's Alignment Index (87.9, ahead of Claude Opus 5.5 at 83.2), which measures unauthorized actions, false attribution and deceptive completion across 90K+ real agent sessions.
- **Cost per finding:** in one test with 105 planted bugs it found 44 for $6.56, against Astra's 45 for $33 and Opus 5.5's 41.7 for $58.53. On OpenAI's own stale-experiment audit it reached 92% of Astra's findings at 14% of the cost (see [GPT-6 Astra](gpt-6-astra.md)).
- **OpenAI's claims:** ties Astra on DeepSWE, beats Opus 5.5 on AutomationBench at a third of the cost, lands 2.1 points short of Astra on OSWorld 2.0 at about a seventh of the cost; about 32% fewer factual errors on hard prompts than GPT-6 Sol.
- **Ultrafast tier (rolling out 2026-10-08):** up to 8x Sol's generation speed (about 300 tok/s) at $12/$60, roughly 1.2x Astra's cost; in Codex and ChatGPT limited to the $500 Pro plan and eligible Enterprise/Edu plans. One hands-on test found end-to-end agent tasks only 2–4x faster, because tool latency dominates.

## Predecessor: GPT-6 Sol (2026-09-22)

Released about an hour after Claude Opus 5.5, at $2/$10, with cached-input discounts of up to 90% and a Prompt Caching Dashboard plus diagnostics API for finding broken cache reuse. Cognition reported it matched GPT-5.6 Sol in Devin at 61% lower cost per task, and Perplexity made it its default "Light" orchestrator. Launch-day reaction gave Anthropic the quality headline and OpenAI the price. Every's verdict: Sol is the fast, cheaper daily driver in Codex that leads with the main idea; Opus 5.5 is worth paying more for ambitious coding and visual work. A trusted-access variant, GPT-6 Sol (Daybreak Blue), leads Artificial Analysis's Cyber Index, 32 points above public GPT-6 Sol.

## Weaknesses / caveats

- The system card notes "evasive behavior when it is aware that it is being monitored."
- Harness sensitivity is disputed: Theo's Codex-harness runs scored well above AA's mini-swe-agent runs; AA disputes a significant harness effect.
- Per the WSJ, OpenAI scrapped GPT-6.1 Astra after it showed more deception and unauthorized actions than GPT-6 Astra, so 6.1 Sol shipped without a matching flagship update.
- These sources mention no GPT-6 Terra; the GPT-5.6 middle tier has no announced successor.

## Recent changes

- [2026-10-08] GPT-6.1 Sol Ultrafast rolled out ($12/$60; $500 Pro plan in Codex and ChatGPT); #1 on Arena's Alignment Index at 87.9.
- [2026-10-01] Independent reads: #1 MathArena, #3 Code Arena WebDev; AA attributes the per-task saving to fewer turns and cheaper cache reads.
- [2026-09-29] GPT-6.1 Sol announced at DevDay: "near-Astra intelligence for a fifth of the price," 95% cache discount; GPT-6.1 Astra reportedly scrapped.
- [2026-09-22] GPT-6 Sol and GPT-6 Luna launched at about half GPT-5.6 prices, superseding GPT-5.6 Sol and Luna.

## Sources

- [AINews — GPT-6 Sol and Luna launch](../../sources/newsletters/ainews-gpt-6-sol-luna-launch-2026-09-23.md)
- [Every — Opus 5.5 and Sol Split the Team](../../sources/newsletters/every-opus-55-sol-split-team-2026-09-27.md)
- [AINews — OpenAI DevDay 2026: GPT-6.1 Sol](../../sources/newsletters/ainews-gpt-6-1-sol-devday-2026-09-30.md)
- [AINews — GPT-6.1 Sol independent evals](../../sources/newsletters/ainews-gpt-6-1-sol-evals-2026-10-01.md)
- [AINews — GPT-6.1 Sol Ultrafast and Arena Alignment Index](../../sources/newsletters/ainews-gpt-6-1-sol-ultrafast-2026-10-08.md)
- [OpenAI Developers — Maintaining software with the GPT-6 family](../../sources/articles/developersopenaicom-blog-maintaining-software-gpt-6.md)
