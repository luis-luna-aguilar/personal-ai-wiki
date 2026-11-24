---
title: GPT-6.2 Sol
type: model
domains: [models, coding, agents, cybersecurity]
subcategory: frontier-model
tags: [openai, closed-source]
as_of: 2026-11-23
sources: [openai-introducing-gpt-6-2-astra-sol]
---

# GPT-6.2 Sol

OpenAI's current mid-price model, launched with [GPT-6.2 Astra](gpt-6-2-astra.md) and billed as "our go-to model for everyday work". OpenAI says it is smarter and more efficient than its predecessor, so paid plans complete more tasks, and that many OpenAI employees use it as their default model. It supersedes [GPT-6.1 Sol](../history/models/gpt-6-1-sol.md) at the same price. [GPT-6 Luna](gpt-6-luna.md) remains the cheapest tier; no GPT-6.2 Luna was announced.

## Current status (as of 2026-11-23)

- **Price:** $2/$10 per 1M input/output tokens and $0.10 for cached input, unchanged from GPT-6.1 Sol.
- **Ultrafast:** available in the API from launch. In ChatGPT and Codex it covers Pro 500 subscribers and, for the first time, Pro 200 subscribers, where Sol gets it first.
- **Availability:** Plus, Pro, Enterprise and Edu in ChatGPT Work and Codex; API as `gpt-6.2-sol`.
- **OpenAI's claims:**
  - [FrontierCode](../benchmarks/frontiercode.md) 2.0: within 0.5 points of GPT-6.2 Astra at about a fifth of the cost (both at max effort).
  - GDPval v2: +5.3 points over GPT-6.1 Sol.
  - LifeVal: beats GPT-6 Astra on OpenAI's everyday-tasks eval at about a seventh of the cost.
  - AA-3D: third at 1,259 Elo, behind 6.2 Astra and Claude Fable 5.2.
- **Safety:** like Astra, it meets OpenAI's Critical cybersecurity and High bio/chem thresholds, ships with tighter cyber safeguards, and shares the finding that it is more likely to leave out blocking obstacles. The post attributes High for AI Self-improvement to Astra only.

## Weaknesses / caveats

- No independent benchmark reads of 6.2 Sol are captured yet; the claims above are OpenAI's.
- Defenders on Daybreak Blue still get GPT-6 Sol with reduced cyber refusals; OpenAI says it will bring 6.2 models to Daybreak.
- Most results are relative claims; chart values were not captured.

## Recent changes

- [2026-11-23] Launched with GPT-6.2 Astra, superseding GPT-6.1 Sol at the same $2/$10; Ultrafast extended to Pro 200 for the first time.

## Sources

- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
