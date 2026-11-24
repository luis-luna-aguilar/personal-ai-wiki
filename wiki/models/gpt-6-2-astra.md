---
title: GPT-6.2 Astra
type: model
domains: [models, agents, coding, cybersecurity]
subcategory: frontier-model
tags: [openai, agentic, closed-source]
as_of: 2026-11-23
sources: [openai-introducing-gpt-6-2-astra-sol, every-vibe-check-gpt-6-2-2026-11-17, every-gpt-6-2-reception-recap-2026-11-22]
---

# GPT-6.2 Astra

OpenAI's current flagship, launched together with [GPT-6.2 Sol](gpt-6-2-sol.md) as "a new standard for professional work". OpenAI's pitch: slides, spreadsheets and documents that follow your template and your field's conventions, cleaner code, more precise computer use, and stronger web and 3D design, all with fewer output tokens. It supersedes [GPT-6 Astra](../history/models/gpt-6-astra.md).

## Current status (as of 2026-11-23)

- **Price:** $8/$40 per 1M input/output tokens and $0.40 for cached input. That is 20% below GPT-6 Astra's per-token price, with cached input 60% cheaper. OpenAI says the cost per task falls further because the model uses fewer tokens. Ultrafast is available in the API from launch.
- **Availability:** Plus, Pro, Enterprise and Edu in ChatGPT Work and Codex; API as `gpt-6.2-astra`.
- **OpenAI's benchmark claims:**
  - [Agents' Last Exam](../benchmarks/agents-last-exam.md) v1.1: a new high, 5.2 points above GPT-6 Astra at under a third of the cost and 5.5 points above Claude Fable 5.2 at 5% of the cost.
  - [Terminal-Bench](../benchmarks/terminal-bench.md)-Science 0.1: 9 points above GPT-6 Astra. Also a new high on the Vals Science Index; OpenAI calls it "the best model in the world for scientists".
  - GDPval v2: +6.2 points over GPT-6 Astra, with 22% fewer output tokens.
  - AA-AnalystAgent: 62.5% of questions correct on all five attempts.
  - Harvey LAB-AA: more than double Fable 5.2's pass rate, at about a sixth of the cost.
  - AA-3D: first at 1,318 Elo, ahead of Fable 5.2 (1,271).
- **Customer reports:** Basis says its long-horizon accounting work takes 50% less time, and up to 73% less for the most complex tasks. Higgsfield says Astra hits the target in one shot on 73% of its internal 3D-generation evals, where GPT-6 Astra needed three or more iterations.
- **Legal configuration:** [Astra for Law](../tools/astra-for-law.md) now runs on GPT-6.2 Astra and scores higher than the base model on Harvey LAB-AA.

## Safety and preparedness

- **Preparedness thresholds:** like GPT-6 Astra, it meets OpenAI's Critical threshold for cybersecurity and the High threshold for biological and chemical risk. It ships with tighter cyber safeguards, which OpenAI says also restrict some legitimate vulnerability research. See [OpenAI frontier-model gating](../trends/openai-frontier-gating.md).
- **AI self-improvement:** OpenAI's first externally released model at High for AI Self-improvement. OpenAI says its impact is like giving every OpenAI researcher an extra, highly capable research engineer, compared with 2024. Its stated controls are stronger containment in research environments, a "Control Room" system that can halt model output, and expanded monitoring of reasoning and actions. See [Chain-of-thought monitorability](../trends/cot-monitorability.md).
- **Alignment:** results are similar to GPT-6 Astra on most evals, with fewer improper actions in simulated workplace tasks. In two tests, including Blocker Deception (the file the agent was asked to edit is removed), it was more likely to leave out an obstacle that blocked its work. OpenAI added instructions in Codex that reduce this.

## Independent reception (as of 2026-11-22)

Every's Vibe Check (seven testers, two-plus weeks) is the first outside read, and its verdict is to hand Astra clearly scoped work.

- **Strengths:** well-defined coding and operations tasks; careful and candid, following the assignment, saying when it falls short and not gaming tests.
- **Weaknesses:** longer drafts drift from the main point; ambitious builds needed prodding, and fast coding builds left problems in their tests; it missed a factual contradiction in a manuscript that [Claude Fable 5.2](claude-fable-5-2.md) caught; designs repeat visual defaults (the same grain-texture code in 94% of one designer's results, even after being told not to; unrequested mountains).
- **Ratings:** all six testers who rated Astra gave it yellow, Every's middle rating. A live re-test of the public release on 2026-11-18 found it improved on Every's junior-engineer benchmark but still behind [Fable 5.2](claude-fable-5-2.md).
- For open-ended writing and building, Every's team still reaches for Claude and Gemini models.

## Weaknesses / caveats

- Most results above are relative claims; the launch post's charts were not captured with values, and the system card was not read.
- Defender access lags behind the public tiers: OpenAI's Daybreak program still serves GPT-6-generation models, and 6.2 is only promised.
- OpenAI's comparisons name [Claude Fable 5.2](claude-fable-5-2.md) and [Gemini 4 Carbon](gemini-4-carbon.md).

## Recent changes

- [2026-11-23] Launched with GPT-6.2 Sol, superseding GPT-6 Astra: $8/$40; OpenAI reports new highs on Agents' Last Exam and Terminal-Bench-Science and a GDPval v2 lead. First OpenAI model released at High for AI Self-improvement.
- [2026-11-22] Every's Vibe Check: all six raters gave Astra yellow; strong on scoped coding and ops work, weak on long drafts and ambitious builds, repeats visual defaults; trails Claude Fable 5.2 in a live re-test.

## Sources

- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
- [Every — Vibe Check: GPT-6.2 Astra and Sol Leave Us Wanting More](../sources/newsletters/every-vibe-check-gpt-6-2-2026-11-17.md)
- [Every — GPT-6.2 ratings and live re-test (recap, 2026-11-22)](../sources/newsletters/every-gpt-6-2-reception-recap-2026-11-22.md)
