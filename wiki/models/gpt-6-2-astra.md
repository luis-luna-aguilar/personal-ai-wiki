---
title: GPT-6.2 Astra
type: model
domains: [models, agents, coding, cybersecurity]
subcategory: frontier-model
tags: [openai, agentic, closed-source]
as_of: 2026-11-23
sources: [openai-introducing-gpt-6-2-astra-sol]
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

## Weaknesses / caveats

- Most results above are relative claims; the launch post's charts were not captured with values, and the system card was not read.
- Defender access lags behind the public tiers: OpenAI's Daybreak program still serves GPT-6-generation models, and 6.2 is only promised.
- OpenAI's comparisons name Claude Fable 5.2 and Gemini 4 Carbon, which have no pages in this wiki yet.

## Recent changes

- [2026-11-23] Launched with GPT-6.2 Sol, superseding GPT-6 Astra: $8/$40; OpenAI reports new highs on Agents' Last Exam and Terminal-Bench-Science and a GDPval v2 lead. First OpenAI model released at High for AI Self-improvement.

## Sources

- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
