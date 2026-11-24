---
title: Automated harness optimization
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-10-26
sources: [langchain-better-harness, self-improving-skills, ainews-andrew-ng-ai-engineering-2026-08-25, ainews-openai-agi-bar-2026-08-28, primeintellect-prime-agent-2026-08-05, claude-api-build-eval-hillclimb]
---

# Automated harness optimization

Systems that change an agent's [harness](harness.md) (prompts, tools, skills, memory, subagents) automatically instead of by hand, while the model's weights stay fixed. Eval-driven hill-climbing scores each harness change against a task set; self-improving skills and self-modifying harnesses refine prompts, tools and memory during live work. Research systems that evolve harnesses without labels or offline against held-out tasks are on [Harness evolution research](harness-evolution-research.md). This is the [agent improvement loop](agent-improvement-loop.md) applied to the harness itself.

## Current status (as of 2026-10-26)

- **Eval-driven hill-climbing is now a product feature.** Anthropic's `/claude-api hillclimb` productizes the loop LangChain's Better-Harness prototyped: a held-out split, a noise check, and one patch per round kept only if train and test both rise.
- Cheap, attributable surfaces (prompt text, skill descriptions) climb best; open-ended harness rewrites and near-saturated evals stall.
- Self-modifying harnesses (Headlong, exo, JIT-Agent, Prime Agent) push the loop into persistent agents that rewrite their own prompts, tools and memory.
- Research on label-free and offline-evolved harnesses, and on how self-evolved harnesses compare with human-engineered ones, is on [Harness evolution research](harness-evolution-research.md).

## Better-Harness: autonomous harness hill-climbing

LangChain's Better-Harness is a prototype that formalizes the improvement loop as:

1. **Source and tag evals** — hand-curated, mined from production traces, adapted from external datasets
2. **Split** into optimization and holdout sets per behavioral category
3. **Baseline** — run the current harness against both sets
4. **Optimize** — iteratively diagnose errors from traces, propose one scoped harness change at a time (prompt edits, tool descriptions, tool additions)
5. **Validate** — check that changes pass new evals without regressing passing ones; holdout set guards against overfitting
6. **Human review** — manual gate catches overfit instructions and token waste

Tested with Claude Sonnet 4.6 and GLM-5. Results showed near-full generalization to holdout sets on tool_selection and followup_quality categories. The analogy is explicit: `harness + evals + harness engineering → better agent`, mirroring `model + training data + gradient descent → better model`.

## Guided hill-climbing in Claude Code

Anthropic's `/claude-api hillclimb` productizes the same loop. The user picks what may change (prompt, skills, tool descriptions, model and effort, harness code) and the goal (quality, or cost at equal quality). A random test split is never read, and the eval's noise must be smaller than the smallest gain worth acting on. Each round makes one root-cause patch, kept only if train and test both rise. Failing transcripts never go into the prompt. After two or three flat rounds Claude sorts the remaining failures by cause, which catches broken tasks and graders. It advises against merging gains within noise. Cheap, attributable surfaces (prompt text, skill descriptions) climb best; open-ended harness rewrites and near-saturated evals stall. Eval design is on [Evals for workflow and task agents](../training/evals-for-agentic-work.md).

## Research on evolved harnesses

Research systems that evolve the harness with no answer key or offline against held-out tasks (Google's label-free Harness², OO-Harness's specialized subclasses, Simular's Agent S4 evolved interfaces, guarded harness evolution, and ByteDance's HarnessDev comparison with human-engineered harnesses) are on [Harness evolution research](harness-evolution-research.md).

## Self-improving skills

A variation of the improvement loop applied at the *skill/prompt* level rather than the full agent harness. The problem: skills in a Claude Code skills folder are static, but the environment around them isn't. A skill that worked last month may quietly start failing when the codebase changes, the model updates, or user request patterns shift. The failures are often invisible until someone notices degraded output.

**The closed loop approach (tricalt, April 2026):** Treat skills as living components, not fixed prompt files. Diagnose which component is failing (routing? individual instructions? tool call?). Close the feedback loop by automatically scoring outputs and proposing targeted changes.

**The meta-skill approach (Ole Lehmann, April 2026):** A single meta-skill that improves any other skill automatically:
1. Run the target skill and score the output
2. Find what's failing in the score
3. Make one small change to the skill prompt
4. Run it again to see if the score went up
5. Keep the change if it improved; discard if not

This mirrors the Better-Harness pattern at the prompt level. The loop is based on Karpathy's "autoresearch" method applied to prompt optimization. Can run on autopilot; the meta-skill improves the target skill without human intervention.

## Self-modifying persistent harnesses

- **Self-modifying, persistent harnesses.** Two open-source projects push recursive self-improvement into the harness itself: Headlong stores agent trajectories as a DAG of jsonl files and runs a self-guided inner loop continuously rather than only on request (reported a 48-minute unattended self-debugging repair, at $1-2/hr background-thinking cost); exo adds an append-only event log, a swappable executor, and a snapshot/rollback-capable sandbox so an agent can rewrite its own prompts/tools/memory without corrupting durable state.
- **JIT-Agent.** The model synthesizes its own harness over modules for memory, planning, action protocol, and tool orchestration at runtime, reporting gains over off-the-shelf agent scaffolds — a step further than a fixed harness the developer designs upfront.
- **Prime Agent: context as a variable, self-modifiable harness.** Prime Intellect's open-source Prime Agent (built on "pi") gives the model a persistent IPython kernel as its only tool, so it programs over its own history and launches sub-agents (long sessions become a programming problem, not a context-window problem), plus persistent multi-agent orchestration and a self-modifiable "Continual Harness." Vendor-reported: 95.5% on ARC-AGI-3, above the cited human-expert baseline, and working SEGA Genesis and Game Boy Color emulators built from scratch in Rust on EmulatorBench.

## Recent changes

- [2026-11-24] Split "Recursive harnessing without ground truth", "Harness continual learning", "Self-evolved harnesses vs human-engineered ones" and the new OO-Harness/Agent S4 material out to [Harness evolution research](harness-evolution-research.md); the Harness² and OO-Harness/Agent S4 entries moved with them.
- [2026-10-26] Added Anthropic's `/claude-api hillclimb`: train/test split, noise check, one patch per round kept only if both sets rise, failure sorting by cause when the score stalls.
- [2026-10-19] Added JIT-Agent (runtime-synthesized harness) and Prime Agent's self-modifiable Continual Harness, moved from [Harness (agent)](harness.md).
- [2026-10-19] Page created, split out of [Agent improvement loop](agent-improvement-loop.md) (Better-Harness, self-improving skills) and [Harness (agent)](harness.md) (self-modifying harnesses, harness continual learning, HarnessDev).
- [2026-04-22] Added self-improving skills pattern: closed feedback loop for skill drift; meta-skill 5-step prompt optimization loop
- [2026-04-10] Added Better-Harness section — LangChain's autonomous harness hill-climbing system

## Related

- [Agent improvement loop](agent-improvement-loop.md) — the broader trace-driven loop this applies to the harness
- [Harness (agent)](harness.md) — what is being optimized
- [Harness vs model](harness-vs-model.md) — why harness changes move scores as much as model swaps
- [Harness evolution research](harness-evolution-research.md) — label-free and offline harness evolution research: Harness², OO-Harness, Agent S4, guarded evolution, HarnessDev

## Sources

- ["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/tweets/langchain-better-harness.md)
- [Self-improving agent skills — auto-improvement loops](../sources/tweets/self-improving-skills.md)
- [AINews — Andrew Ng gets into AI Engineering](../sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md)
- [[AINews] OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [Prime Intellect on X: \"Introducing Prime Agent: A self-improving RLM harness\](../sources/tweets/primeintellect-prime-agent-2026-08-05.md)
- [Anthropic — Automating eval design and hillclimbing with Claude](../sources/articles/claude-api-build-eval-hillclimb.md)
