---
title: Automated harness optimization
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-10-09
sources: [langchain-better-harness, self-improving-skills, ainews-andrew-ng-ai-engineering-2026-08-25, ainews-poolside-nvidia-2026-08-21, ainews-muse-spark-13-2026-09-03, harness2-recursive-harnessing-2026-10, ainews-openai-agi-bar-2026-08-28, primeintellect-prime-agent-2026-08-05]
---

# Automated harness optimization

Systems that change an agent's [harness](harness.md) (prompts, tools, skills, memory, subagents) automatically instead of by hand, while the model's weights stay fixed. They fall into two families. Eval-driven hill-climbing scores each harness change against a task set. Label-free and self-modifying approaches refine the harness during live work, with no answer key. This is the [agent improvement loop](agent-improvement-loop.md) applied to the harness itself.

## Current status (as of 2026-10-09)

- **Label-free per-task refinement is now measured.** Google Cloud AI Research's Harness² improves a frozen model's harness on each new task without an answer key, keeping only edits a behaviour comparison supports — see below
- Self-improvement helps unevenly: ByteDance's HarnessDev finds self-evolved harnesses still lag human-engineered ones on code, search, and research, but match or beat them on writing and ML experimentation.
- Guarding updates matters: testing a candidate harness change in isolation before committing it beats ungated evolution by more than 10%.

## Better-Harness: autonomous harness hill-climbing

LangChain's Better-Harness is a prototype that formalizes the improvement loop as:

1. **Source and tag evals** — hand-curated, mined from production traces, adapted from external datasets
2. **Split** into optimization and holdout sets per behavioral category
3. **Baseline** — run the current harness against both sets
4. **Optimize** — iteratively diagnose errors from traces, propose one scoped harness change at a time (prompt edits, tool descriptions, tool additions)
5. **Validate** — check that changes pass new evals without regressing passing ones; holdout set guards against overfitting
6. **Human review** — manual gate catches overfit instructions and token waste

Tested with Claude Sonnet 4.6 and GLM-5. Results showed near-full generalization to holdout sets on tool_selection and followup_quality categories. The analogy is explicit: `harness + evals + harness engineering → better agent`, mirroring `model + training data + gradient descent → better model`.

## Recursive harnessing without ground truth

Better-Harness needs a scored eval set. Google Cloud AI Research's [Harness²](../tools/harness2.md) (paper and open-source code, October 2026) runs the loop inside each new task with no answer key, keeping model weights fixed:

1. **Reference run** — the agent does the task with its current harness.
2. **Propose** — an editor model writes two edited harnesses: an *invariant* one fixing general agent habits (planning, tool use, delegation, checking its own output) and a *domain* one adding the field's knowledge and procedures. The editable parts are files: system prompt, guardrails, memory, skills, tool guidance, scripts, subagents, and a middleware plugin.
3. **Probe** — both run on the same task under the same model and environment. Comparing their behaviour with the reference run shows whether an edit fixed the targeted weakness, changed nothing, or broke something. It does not show whether the answer is correct.
4. **Compose** — the editor merges, revises, or drops edits, tying each decision to an observed difference, and the combined harness produces the deliverable.
5. **Reflect** — the adopted harness and an `EXPERIENCE.md` of evidence-backed lessons go into a library. Later tasks start from the base harness and reuse library parts selectively, not wholesale.

The budget scales two ways: *parallel* (k candidates per scope, k compositions) or *sequential* (k chained rounds). Reported results: one round raised scores on WorkBuddy-Bench, JobBench, and Harvey's LAB legal benchmark in all four model–harness setups. GLM-5 under OpenCode went from 64.2 to 75.7 on WorkBuddy-Bench, and Gemini 3.5 Flash from 72.4 to 77.5. Gains held when each model edited its own harness, from GLM-5 to Claude Opus 5. Removing the library, the two editor scopes, or the compose step each cost 1.6–3.7 points. Editing without reference runs, probes, or library made things worse (WorkBuddy Code 73.4→63.2). The authors' caveats: each round costs extra runs, and behaviour comparisons inherit run-to-run noise and the model's own blind spots.

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

## Harness continual learning

A paper on "harness continual learning" names a distinct failure mode: harness-level forgetting, where improving one component (a tool, a memory policy, a routing rule) silently breaks another that depended on the old behavior. The proposed fix, guarded harness evolution, separates *proposing* a harness update from *committing* it — testing a candidate change in isolation before it can affect production behavior — reporting >10% gains across textual, multimodal, and open-world tasks versus ungated evolution. See [RL harness quality](rl-harness-quality.md) for the related failure mode when a harness serves as an RL training environment.

## Self-evolved harnesses vs human-engineered ones

ByteDance Seed's HarnessDev has models build and then iteratively improve their own execution harness from a weak, runnable seed, scoring both stages on capability and execution-token cost; across six creator LLMs, four domains, and 2,207 held-out instances, self-evolved harnesses still lag mature human-engineered systems on code, search, and research, but match or exceed them on writing and ML experimentation — a caution that self-improving harnesses help unevenly, not universally.

## Recent changes

- [2026-10-19] Added JIT-Agent (runtime-synthesized harness) and Prime Agent's self-modifiable Continual Harness, moved from [Harness (agent)](harness.md).
- [2026-10-19] Page created, split out of [Agent improvement loop](agent-improvement-loop.md) (Better-Harness, self-improving skills) and [Harness (agent)](harness.md) (self-modifying harnesses, harness continual learning, HarnessDev).
- [2026-10-09] Added Harness² (Google Cloud AI Research): label-free per-task harness refinement via propose-probe-compose, plus a lessons library carried across tasks; up to +11.5 points on WorkBuddy-Bench with frozen weights.
- [2026-04-22] Added self-improving skills pattern: closed feedback loop for skill drift; meta-skill 5-step prompt optimization loop
- [2026-04-10] Added Better-Harness section — LangChain's autonomous harness hill-climbing system

## Related

- [Agent improvement loop](agent-improvement-loop.md) — the broader trace-driven loop this applies to the harness
- [Harness (agent)](harness.md) — what is being optimized
- [Harness vs model](harness-vs-model.md) — why harness changes move scores as much as model swaps
- [Harness²](../tools/harness2.md) — Google's open-source recursive harnessing framework

## Sources

- ["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/tweets/langchain-better-harness.md)
- [Self-improving agent skills — auto-improvement loops](../sources/tweets/self-improving-skills.md)
- [AINews — Andrew Ng gets into AI Engineering](../sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md)
- [AINews — Poolside / NVIDIA (August 21)](../sources/newsletters/ainews-poolside-nvidia-2026-08-21.md)
- [AINews — Muse Spark 1.3 (September 3)](../sources/newsletters/ainews-muse-spark-13-2026-09-03.md)
- [Harness²: Recursive Agent Harnessing for an Open World — Google Cloud AI Research](../sources/papers/harness2-recursive-harnessing-2026-10.md)
- [[AINews] OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [Prime Intellect on X: \"Introducing Prime Agent: A self-improving RLM harness\](../sources/tweets/primeintellect-prime-agent-2026-08-05.md)
