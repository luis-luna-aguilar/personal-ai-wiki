---
title: HealthBench
type: benchmark
domains: [healthcare]
tags: [openai]
as_of: 2026-11-24
sources: [artificial-analysis-healthbench-2026-11, ainews-healthbench-leaderboards-2026-10-21]
---

# HealthBench

OpenAI's benchmark of medical conversations, graded against rubrics written by physicians. It has two sets: **HealthBench**, 5,000 general health conversations from emergency referrals to global health, and **HealthBench Professional**, 525 clinician conversations across consult, writing and research tasks, including red-teaming and hard cases. Artificial Analysis has run independent leaderboards for both since 2026-10-21.

## How it is scored

- Each rubric criterion is worth −10 to +10 points. A judge model (GPT-5.4 low, as in OpenAI's implementation) checks which criteria the reply meets; a task scores the points earned over the positive points available, so it can fall below zero. Artificial Analysis runs four repeats per task.
- Artificial Analysis reports a raw score and a length-adjusted score. The adjustment lowers the score of replies longer than 2,000 characters and raises shorter ones; reasoning tokens do not count toward length. Cite which score you mean: the adjustment reorders the top of the table.

## Current results (as of 2026-11-24)

- **HealthBench, length-adjusted:** [Claude Sonnet 5.5](../models/claude-sonnet-5-5.md) 62.1%, [DeepSeek V4.1 Flash](../models/deepseek-v4-1-flash.md) 60.9%, [Claude Fable 5.2](../models/claude-fable-5-2.md) 59.6%. [GPT-6.2 Astra](../models/gpt-6-2-astra.md) scores 53.5%.
- **Cost (launch figures, 2026-10-21):** DeepSeek V4.1 Flash reached its score at $0.005 per task, against $0.08 for Sonnet 5.5.
- **HealthBench Professional, length-adjusted:** [Claude Fable 5.2](../models/claude-fable-5-2.md) leads at 68.1% at xhigh effort (67.7% at max). Among models current in this wiki it is followed by Sonnet 5.5 (63.0%) and [GPT-6 Luna](../models/gpt-6-luna.md) (61.9%, the cheapest run at $0.0041 per task); results for models the wiki has since replaced are omitted. GPT-6.2 Astra has not been run on this set.
- **Length effect:** at launch, [Claude Opus 5.5](../models/claude-opus-5-5.md) had the highest raw Professional score (71.4%) but fell to 59.9% after adjustment. On the general set, the model with the shortest answers led on communication quality while scoring lowest on completeness.

## Why it matters

It is the wiki's first head-to-head medical leaderboard for general models. The spread between raw and length-adjusted scores shows that "best medical model" depends on whether long, exhaustive answers are rewarded, which is a product choice as much as a capability result.

## Recent changes

- [2026-11-24] Page created. Claude Fable 5.2 now leads HealthBench Professional (length-adjusted); Sonnet 5.5 still leads the general set.
- [2026-10-21] Artificial Analysis launched independent HealthBench and HealthBench Professional leaderboards with raw and length-adjusted scores.

## Sources

- [Artificial Analysis — HealthBench leaderboards](../sources/articles/artificial-analysis-healthbench-2026-11.md)
- [AINews — HealthBench leaderboards launch (Oct 21)](../sources/newsletters/ainews-healthbench-leaderboards-2026-10-21.md)
