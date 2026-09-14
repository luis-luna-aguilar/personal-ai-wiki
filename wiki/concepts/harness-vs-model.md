---
title: Harness vs model
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-09-09
sources: [langchain-better-harness, latent-space-agent-harness-evolution-2026-08-22, anthropic-riemann-hypothesis-2026-08-11]
---

# Harness vs model

A well-engineered harness can compensate for a weaker model. A poor harness can cripple a strong one. This is why [Better-Harness](../sources/tweets/langchain-better-harness.md) and similar systems focus on *harness hill-climbing* — iteratively improving the harness using evals as a signal, separate from any model update. The practical model/harness split is now measurable: the same model can underperform in a mismatched product surface, while a cheaper model can approach frontier behavior in a tuned harness. Treat benchmark results as model + harness + environment, not model-only.

## Current status (as of 2026-08-25)

Two 2026-08 data points make the split measurable rather than anecdotal. A SWE-bench Pro comparison found harness choice changed pass@1 more than many model upgrades do: scores ranged 23-52% on GLM-5.2 and 15-36% on Gemma 4 26B depending on which harness ran the task, with harness rankings barely transferring between models (rank correlation of -0.05) — the best harness for one model is often not the best for another. Separately, Composio ran DeepSeek V4 Flash through four different harnesses on the same 30 agentic tasks and found Pi Agent both the cheapest and the best-performing of the four, reinforcing the same conclusion with a second model.

A widely-shared Latent Space essay argues the "harness matters" era follows a predictable cycle rather than being a permanent architecture choice: train → absorb → shed → repeat. As models get RL-trained inside their own harness (tool calling, compaction, memory management), they absorb capabilities the harness used to have to supply externally, and the harness sheds that scaffolding once the model no longer needs it — Anthropic reportedly deleted 80% of Claude Code's system prompt this way. The essay traces the model/harness "gap" through stages: ReAct as pure prompting with no real harness yet (October 2022); AutoGPT/BabyAGI handing full autonomy to models not remotely ready for it (spring 2023); the IDE-era retreat to human-in-the-loop that followed; and Claude Code's February 2025 "curves cross" moment, where the model finally got reliable enough to be handed the loop back. Its prediction for what comes next: once the model absorbs everything computer-facing, the harness doesn't disappear — it inverts, becoming the interface that governs a person's attention instead of the model's actions, deciding when an agent may interrupt someone, what it can decide alone, and what needs approval, since human attention (not tokens) is the resource that stays scarce. Two 2026-08 data points anchor the "harness still matters enormously today" half of the argument: Harness-Bench found a 23.8-point score swing (52.4→76.2) running one model through different harnesses on the same 106 tasks, and OpenAI tripled GPT-5.6 Sol's ARC-AGI-3 score (13.3%→38.3%) through harness changes (retained reasoning + compaction) alone, with no model change.

Practitioners are increasingly using a consistent vocabulary for these parts: **model** (the neural network weights that process each request — no memory between calls, no built-in ability to act independently), **harness** (the scaffold that adds tools, memory, and loop logic), **agent** (the user-facing system combining both), **context** (what the agent has available right now), **session** (one bounded run until reset or handoff), and **environment** (what the agent can actually act on). Teams that adopt this language spend less time misattributing problems to the wrong layer. See [AI coding vocabulary](../training/ai-coding-vocabulary.md).

## Why it matters

The train→absorb→shed cycle explains why "is harness engineering real?" keeps resurfacing as a live debate rather than settling once: it isn't a permanent architecture choice, it's a moving boundary that shifts every time a model absorbs another capability. Benchmark numbers that don't separate model from harness therefore understate how much of a score swing came from scaffolding rather than the underlying weights.

## Recent changes

- [2026-09-09] Page created, split out of [Harness (agent)](harness.md)'s "Harness vs model" and "The model/harness co-evolution theory" sections, which formed one coherent argument about how much of a benchmark score comes from harness rather than model.
- [2026-08-25] Added the model/harness co-evolution framing (ReAct → AutoGPT → Cursor → Claude Code "curves cross," train→absorb→shed cycle) and its "attention interface" future thesis.
- [2026-08-11] Added SWE-bench Pro harness-swap data (23-52% on GLM-5.2, 15-36% on Gemma 4 26B, -0.05 harness-ranking rank correlation across models) and a Composio DeepSeek V4 Flash four-harness bake-off (Pi Agent cheapest and best-performing) as concrete numbers behind the harness-vs-model claim.

## Related

- [Harness (agent)](harness.md) — what a harness is and what good harness engineering looks like; this page covers the specific model-vs-harness measurement question
- [Harness vs folder-level context](harness.md#harness-vs-folder-level-context) — a different boundary: what the agent knows versus how it operates
- [Agent evals](agent-evals.md) — the evaluation practices that make a harness-vs-model comparison possible in the first place

## Sources

- ["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/tweets/langchain-better-harness.md)
- [The Evolution of the Agent Harness](../sources/newsletters/latent-space-agent-harness-evolution-2026-08-22.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
