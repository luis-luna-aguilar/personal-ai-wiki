---
title: Harness evolution research
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-10-20
sources: [ainews-poolside-nvidia-2026-08-21, ainews-muse-spark-13-2026-09-03, harness2-recursive-harnessing-2026-10, oo-harness-2026-10, agent-s4-evolving-interfaces-2026-10]
---

# Harness evolution research

Research systems that evolve an agent's [harness](harness.md) (prompts, tools, skills, memory, interfaces, control flow) with the model's weights fixed, and measure whether the evolved harness beats a hand-built one on tasks it was not built from. Some refine the harness inside each new task with no answer key; others evolve it offline on training tasks and freeze it before testing. The practitioner loops (eval-driven hill-climbing, self-improving skills, self-modifying harnesses) are on [Automated harness optimization](automated-harness-optimization.md).

## Current status (as of 2026-10-20)

- **Label-free per-task refinement is now measured.** Google Cloud AI Research's Harness² improves a frozen model's harness on each new task without an answer key, keeping only edits a behaviour comparison supports — see below
- Self-improvement helps unevenly: ByteDance's HarnessDev finds self-evolved harnesses still lag human-engineered ones on code, search, and research, but match or beat them on writing and ML experimentation. Offline evolution with held-out selection does better: Google's OO-Harness and Simular's Agent S4 (October 2026) beat their hand-built starting harness or interfaces by 14–17 points on the same model — see below.
- Guarding updates matters: testing a candidate harness change in isolation before committing it beats ungated evolution by more than 10%.

## Recursive harnessing without ground truth

[Better-Harness](automated-harness-optimization.md#better-harness-autonomous-harness-hill-climbing) needs a scored eval set. Google Cloud AI Research's [Harness²](../tools/harness2.md) (paper and open-source code, October 2026) runs the loop inside each new task with no answer key, keeping model weights fixed:

1. **Reference run** — the agent does the task with its current harness.
2. **Propose** — an editor model writes two edited harnesses: an *invariant* one fixing general agent habits (planning, tool use, delegation, checking its own output) and a *domain* one adding the field's knowledge and procedures. The editable parts are files: system prompt, guardrails, memory, skills, tool guidance, scripts, subagents, and a middleware plugin.
3. **Probe** — both run on the same task under the same model and environment. Comparing their behaviour with the reference run shows whether an edit fixed the targeted weakness, changed nothing, or broke something. It does not show whether the answer is correct.
4. **Compose** — the editor merges, revises, or drops edits, tying each decision to an observed difference, and the combined harness produces the deliverable.
5. **Reflect** — the adopted harness and an `EXPERIENCE.md` of evidence-backed lessons go into a library. Later tasks start from the base harness and reuse library parts selectively, not wholesale.

The budget scales two ways: *parallel* (k candidates per scope, k compositions) or *sequential* (k chained rounds). Reported results: one round raised scores on WorkBuddy-Bench, JobBench, and Harvey's LAB legal benchmark in all four model–harness setups. GLM-5 under OpenCode went from 64.2 to 75.7 on WorkBuddy-Bench, and Gemini 3.5 Flash from 72.4 to 77.5. Gains held when each model edited its own harness, from GLM-5 to Claude Opus 5. Removing the library, the two editor scopes, or the compose step each cost 1.6–3.7 points. Editing without reference runs, probes, or library made things worse (WorkBuddy Code 73.4→63.2). The authors' caveats: each round costs extra runs, and behaviour comparisons inherit run-to-run noise and the model's own blind spots.

## Specialized harnesses and evolved interfaces

Two October 2026 papers evolve the harness offline on training tasks, then freeze it and test on held-out tasks with the same model.

- **OO-Harness (Google Cloud AI Research).** An evolution agent builds a class hierarchy instead of one global harness. Subclasses inherit the base and override only what a task cluster needs, design lessons record which changes helped, and a router picks a subclass per task after a base run. On the same Gemini 3.5 Flash, AutomationBench rose from 61.6% to 77.4% and Workspace-Bench from 25.5% to 39.5%, ahead of Meta-Harness on all three benchmarks. Spending that inference on best-of-K or self-refinement did not reliably help. On out-of-distribution tasks the router kept the base harness, while Meta-Harness's global harness lowered pass rates.
- **Agent S4 (Simular).** A meta-agent reads a computer-use agent's trajectories, with no success labels, and writes new interfaces (a bulk spreadsheet edit instead of cell-by-cell typing) plus notes on when to use them. Selection on unseen validation tasks keeps the changes that generalize. Qwen3.8-27B reached 21.3% on OSWorld V2, 3.8x the same model with fixed interfaces and above GPT-5.5 (13.0%) and Opus 4.8 (20.6%) at a few percent of their cost; ScienceBoard rose from 41.4% to 58.6%.

## Harness continual learning

A paper on "harness continual learning" names a distinct failure mode: harness-level forgetting, where improving one component (a tool, a memory policy, a routing rule) silently breaks another that depended on the old behavior. The proposed fix, guarded harness evolution, separates *proposing* a harness update from *committing* it — testing a candidate change in isolation before it can affect production behavior — reporting >10% gains across textual, multimodal, and open-world tasks versus ungated evolution. See [RL harness quality](rl-harness-quality.md) for the related failure mode when a harness serves as an RL training environment.

## Self-evolved harnesses vs human-engineered ones

ByteDance Seed's HarnessDev has models build and then iteratively improve their own execution harness from a weak, runnable seed, scoring both stages on capability and execution-token cost; across six creator LLMs, four domains, and 2,207 held-out instances, self-evolved harnesses still lag mature human-engineered systems on code, search, and research, but match or exceed them on writing and ML experimentation — a caution that self-improving harnesses help unevenly, not universally.

## Recent changes

- [2026-11-24] Page created, split out of [Automated harness optimization](automated-harness-optimization.md): its "Recursive harnessing without ground truth", "Specialized harnesses and evolved interfaces", "Harness continual learning" and "Self-evolved harnesses vs human-engineered ones" sections and the matching Current-status bullets.
- [2026-10-20] Added OO-Harness (specialized harness subclasses plus a router; AutomationBench 61.6%→77.4% on the same Gemini 3.5 Flash) and Agent S4 (label-free evolved computer-use interfaces; open 27B model 21.3% on OSWorld V2, 3.8x fixed interfaces); HarnessDev status line now reads as mixed evidence.
- [2026-10-09] Added Harness² (Google Cloud AI Research): label-free per-task harness refinement via propose-probe-compose, plus a lessons library carried across tasks; up to +11.5 points on WorkBuddy-Bench with frozen weights.

## Related

- [Automated harness optimization](automated-harness-optimization.md) — the practitioner loops: Better-Harness, `/claude-api hillclimb`, self-improving skills, self-modifying harnesses
- [Harness (agent)](harness.md) — what is being evolved
- [Harness vs model](harness-vs-model.md) — why harness changes move scores as much as model swaps
- [Harness²](../tools/harness2.md) — Google's open-source recursive harnessing framework

## Sources

- [AINews — Poolside / NVIDIA (August 21)](../sources/newsletters/ainews-poolside-nvidia-2026-08-21.md)
- [AINews — Muse Spark 1.3 (September 3)](../sources/newsletters/ainews-muse-spark-13-2026-09-03.md)
- [Harness²: Recursive Agent Harnessing for an Open World — Google Cloud AI Research](../sources/papers/harness2-recursive-harnessing-2026-10.md)
- [Object-Oriented Harness — Google Cloud AI Research (arXiv)](../sources/papers/oo-harness-2026-10.md)
- [Evolving Agent Interfaces (Agent S4) — Simular (arXiv)](../sources/papers/agent-s4-evolving-interfaces-2026-10.md)
