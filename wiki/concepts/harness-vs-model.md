---
title: Harness vs model
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-11-24
sources: [langchain-better-harness, anthropic-riemann-hypothesis-2026-08-11, ainews-openai-agi-bar-2026-08-28, ainews-muse-spark-13-2026-09-03, ainews-navier-stokes-2026-09-09, model-harness-fit-2026-05-13, weinstein-computer-use-180-degrees-2026-09-30, is-bash-all-you-need-2026-09, harness-design-empirical-study-2026-09, periodic-labs-neon-xrd-2026-09-15, whatmodelsh-lab-vs-independent-2026-11-24]
---

# Harness vs model

A well-engineered harness can compensate for a weaker model. A poor harness can cripple a strong one. This is why [Better-Harness](../sources/tweets/langchain-better-harness.md) and similar systems focus on *harness hill-climbing* — iteratively improving the harness using evals as a signal, separate from any model update. The practical model/harness split is now measurable: the same model can underperform in a mismatched product surface, while a cheaper model can approach frontier behavior in a tuned harness. Treat benchmark results as model + harness + environment, not model-only.

## Current status (as of 2026-11-24)

### Measured evidence

Two 2026-08 data points make the split measurable rather than anecdotal. A SWE-bench Pro comparison found harness choice changed pass@1 more than many model upgrades do: scores ranged 23-52% on GLM-5.2 and 15-36% on Gemma 4 26B depending on which harness ran the task, with harness rankings barely transferring between models (rank correlation of -0.05) — the best harness for one model is often not the best for another. Separately, Composio ran DeepSeek V4 Flash through four different harnesses on the same 30 agentic tasks and found Pi Agent both the cheapest and the best-performing of the four, reinforcing the same conclusion with a second model.

Three later data points push the same way. Harvey and Baseten built a recursive-language-model (RLM) harness for M&A due diligence: a root agent searches a data room and delegates document review to sub-agents, aggregating findings over corpora up to 80M tokens. Moving from a standard tool-calling loop to this RLM harness raised mean rubric pass rate on their synthetic diligence benchmark from 23% to 62%, and harness-specific post-training on top (self-distilled SFT on GLM-5.2, GRPO on Qwen3.5) added another 15-33 points depending on the base model — harness and post-training design moving scores as much as, or more than, a base-model swap. openJiuwen (open-source) reached 82.6% SWE-bench Verified / 87.19% Terminal-Bench 2.1 through "rail-based composition" on a fixed model. And research inducing compact finite-state machines from recorded agent traces suggests an agent's behavioral "shape" is often set more by the deployment scaffold than by the underlying model.

Computer use shows the same split from inside a lab. OpenAI's computer-use lead says the past year's gains came "sometimes in the harness and sometimes in the model": the harness side gave agents richer inputs (accessibility trees, the DOM, Playwright) and let them write code that performs many actions in a single step, removing the old screenshot-scroll-screenshot loop. Because OpenAI trains its models on its own computer-use harness, he suggests developers who build on that in-distribution harness through the Agents API may get speed, cost, and accuracy advantages over a custom one. This is model-harness fit from the vendor's side.

Science shows the same split in a domain harness. Periodic Labs held the model fixed (Claude Opus 5, high effort) and compared its own scientific harness, with lab context, in-house materials databases and XRD software, against Claude Code given open databases (COD, Materials Project) and standard XRD software (BGMN). On its FrontierXRD set its harness reached a 3.8× higher success rate at a similar cost per analysis, as graded by an LLM-judge ensemble calibrated to expert ratings. Both setups had appropriate tools, so the gap comes from domain context and data access in the harness, not from the model.

Published scores show the same effect at scale. The open leaderboard whatmodel.sh matched 619 cases where a lab published a score for its own model and an independent party (a leaderboard, Epoch AI, a paper, a rival lab) measured the same model on the same test. When the two differ, the lab's number is higher 64% of the time, 6.3% higher on average, though the median gap is only 0.7 points. Fixed-format tests (MMLU, HumanEval, WinoGrande) barely move; tests where setup is part of the result move most, with median gaps of about 9 points on SWE-bench Verified (agent harness) and MBPP (few-shot prompting). The site attributes much of the gap to different settings and to labs choosing which tests to publish, not only to inflation. Read a lab's launch number as its best-tuned configuration.

### Tool surface: bash vs typed tools

A September 2026 Microsoft paper compared five tool interfaces on two office-work benchmarks (TheAgentCompany, APEX-Agents) with Opus 4.8 and GPT-5.5. Bash alone beat a typed tool catalog by 21.8–24.5 points on TheAgentCompany and 4.8–7.4 points on APEX-Agents, using 19–72% fewer tokens. Adding typed or agent-written tools on top of bash gave no measurable gain. Programmatic tool calling, where the agent writes code that may only call a fixed catalog, saved tokens over direct typed calls but trailed bash on quality and cost. The authors' rule: bash where execution can be sandboxed, programmatic tool calling where compliance requires a fixed tool list. A component-level study of coding harnesses adds a condition: predefined tools help bash-weak models, while bash-capable models do as well with bash only, at much lower cost.

### The harness cycle and its dissent

Whether the harness keeps mattering, or models absorb it, is on [Harness-model co-evolution](harness-model-co-evolution.md): the train → absorb → shed cycle, Hugging Face's multi-harness RL proxy, Alex Zhang's view that mainstream coding harnesses are one loop, and Arena's HarnessTax cost measurement.

### Vocabulary and model-harness fit

Practitioners are increasingly using a consistent vocabulary for these parts: **model** (the neural network weights that process each request — no memory between calls, no built-in ability to act independently), **harness** (the scaffold that adds tools, memory, and loop logic), **agent** (the user-facing system combining both), **context** (what the agent has available right now), **session** (one bounded run until reset or handoff), and **environment** (what the agent can actually act on). Teams that adopt this language spend less time misattributing problems to the wrong layer. See [AI coding vocabulary](../training/ai-coding-vocabulary.md).
- **Model-harness fit.** Coding-agent performance depends on how well the surrounding harness matches the model's preferred edit format, action space, tool-call style, and failure recovery patterns. A strong model can underperform in a mismatched harness.
- **Model-specific harness profiles.** LangChain Deep Agents coverage suggests that Qwen, Kimi, DeepSeek, and frontier closed models can require different prompts, tools, and memory layouts. A cheaper model can become viable when the harness matches its operating style.

## Why it matters

Benchmark numbers that don't separate model from harness understate how much of a score swing came from scaffolding rather than the underlying weights.

## Recent changes

- [2026-11-24] Split "The harness cycle and its dissent" (train → absorb → shed essay, Hugging Face's multi-harness proxy, Alex Zhang's dissent, HarnessTax) out to [Harness-model co-evolution](harness-model-co-evolution.md); a pointer paragraph remains.
- [2026-11-24] Added whatmodel.sh's lab-vs-independent comparison: across 619 matched pairs the lab's score is higher 64% of the time when they differ, with the largest gaps on setup-sensitive tests (SWE-bench Verified, MBPP, about +9 points).
- [2026-10-19] Added model-harness fit and model-specific harness profiles, moved from [Harness (agent)](harness.md).
- [2026-10-19] Took the Harvey + Baseten RLM due-diligence harness numbers (23%→62% from the harness swap, +15-33 points from harness-specific post-training), openJiuwen's fixed-model SWE-bench/Terminal-Bench result, and FSM trace induction from [Harness (agent)](harness.md) as further evidence.
- [2026-09-30] Added OpenAI's computer-use account: gains split between model and harness (accessibility trees, DOM, code-writing multi-action steps), and the case for the in-distribution harness in the Agents API.
- [2026-09-17] Added tool-surface evidence (Microsoft: bash alone beats typed tool catalogs on enterprise-work benchmarks with fewer tokens; a component study: predefined tools help only bash-weak models).
- [2026-09-15] Added Periodic Labs' same-model comparison: its scientific harness beat Claude Code with standard XRD tools by 3.8× on X-ray diffraction analysis at similar cost (Claude Opus 5 in both).
- [2026-09-09] Page created, split out of [Harness (agent)](harness.md)'s "Harness vs model" and "The model/harness co-evolution theory" sections, which formed one coherent argument about how much of a benchmark score comes from harness rather than model.
- [2026-08-11] Added SWE-bench Pro harness-swap data (23-52% on GLM-5.2, 15-36% on Gemma 4 26B, -0.05 harness-ranking rank correlation across models) and a Composio DeepSeek V4 Flash four-harness bake-off (Pi Agent cheapest and best-performing) as concrete numbers behind the harness-vs-model claim.

## Related

- [Harness-model co-evolution](harness-model-co-evolution.md) — whether models absorb the harness over time (train → absorb → shed) and the dissent that mainstream harnesses differ mostly in cost
- [Harness (agent)](harness.md) — what a harness is and what good harness engineering looks like; this page covers the specific model-vs-harness measurement question
- [Harness vs folder-level context](harness.md#harness-vs-folder-level-context) — a different boundary: what the agent knows versus how it operates
- [Agent evals](agent-evals.md) — the evaluation practices that make a harness-vs-model comparison possible in the first place

## Sources

- ["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/tweets/langchain-better-harness.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — Muse Spark 1.3 matches GPT-5.6-Sol](../sources/newsletters/ainews-muse-spark-13-2026-09-03.md)
- [AINews — OpenAI reports Navier-Stokes singularity find](../sources/newsletters/ainews-navier-stokes-2026-09-09.md)
- [Model-harness fit as coding-agent moat](../sources/newsletters/model-harness-fit-2026-05-13.md)
- [Ari Weinstein: computer use is "180 degrees different"](../sources/newsletters/weinstein-computer-use-180-degrees-2026-09-30.md)
- [Is Bash All You Need? — Microsoft (arXiv)](../sources/papers/is-bash-all-you-need-2026-09.md)
- [An Empirical Study of Harness Design for Coding Agents (arXiv)](../sources/papers/harness-design-empirical-study-2026-09.md)
- [Periodic Labs — Nature Is Our Learning Environment (Neon)](../sources/articles/periodic-labs-neon-xrd-2026-09-15.md)
- [whatmodel.sh — What AI labs report vs what independent tests find](../sources/articles/whatmodelsh-lab-vs-independent-2026-11-24.md)
