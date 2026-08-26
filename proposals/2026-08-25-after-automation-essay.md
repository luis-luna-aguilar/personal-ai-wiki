---
type: proposal
source: raw/articles/2026-08-25-everyto-p-after-automation.md
status: pending
created: 2026-08-25
---

# Proposal: Dan Shipper's "After Automation" (Every)

## Summary
Every CEO Dan Shipper argues AI progress creates more expert human work, not less: models commoditize yesterday's competence, cheap competence floods in and produces undifferentiated "slop," slop creates demand for differentiated human judgment, and — because "the frame is not the framer" — this cycle repeats even under strong AGI. The essay also introduces a sharp critique of reading benchmark trend lines in isolation ("chart psychosis"), backed by Every's own in-house Senior Engineer benchmark.

## Intended changes

- [x] **Update** `wiki/training/ai-work-delegation-modes.md` — add concrete agent-employee/human-sandwich evidence and a new failure mode; bump `as_of` to 2026-05-21
    > **Before (Evidence from practice):** two bullets citing Every's May 2026 guidance and Anthropic's Managed Agents docs.
    > **After:** same two bullets plus two new bullets adding Every's "After Automation" agent-employee taxonomy (coworker vs. embedded agents) and the OpenClaw pull-request volume data point.
    > **Before (Failure modes):** three bullets, no mention of agent maintenance/staleness.
    > **After:** same three bullets plus one new bullet on personal-agent staleness and hidden maintenance cost.

- [x] **Update** `wiki/concepts/agent-evals.md` — add a new "Benchmarks measure work inside a frame" section between "Infrastructure layer" and "Caveats"; add a Recent changes entry (`as_of` unchanged, 2026-07-14 remains the newest source-backed claim)
    > See full section draft below. Inserted after the existing "Infrastructure layer (as of 2026-07-08)" section and before "## Caveats" — it's a complementary but distinct point from the existing benchmark-leakage caveat (leakage = benchmark fails to measure what it claims; frame-relativity = benchmark validly measures a moving target that keeps being redefined as it saturates).

- [x] **Create** `wiki/sources/articles/every-after-automation-2026-05.md` — source summary

## Page drafts

### wiki/training/ai-work-delegation-modes.md (updated)

Frontmatter changes:

```yaml
---
title: AI work delegation modes
type: training
domains: [agents]
tags: [agentic]
as_of: 2026-05-21
sources: [ai-work-splitting-2026-05-10, task-routing-cost-discipline-2026-05-13, every-after-automation-2026-05]
---
```

`## Evidence from practice` (full section, replaces existing):

```md
## Evidence from practice

- Framework synthesized from Anthropic's Claude platform team's guidance on designing agent workflows, reported by Every (May 2026)
- Anthropic's Claude Managed Agents documentation for "Define outcomes" (May 2026) formalizes the delegation-mode approach at the platform level
- Every's "After Automation" essay (Dan Shipper, May 2026) reframes delegation mode as "agent employees" — coworker agents you tag and ask to do work (Every's Claudie, Andy, Viktor) and embedded agents living inside a product workflow (Fin, which closed 40.1% of actionable customer-service conversations without a human in a recent week) — and reframes collaboration mode as the "human sandwich": a human frames the task, the agent collapses it, and a human judges and extends the result inside tools like Codex, Claude Code, and Claude Cowork.
- OpenClaw's pull-request volume (44,469 PRs by May 16, 2026; 12,430 since April 1 — versus Kubernetes' 5,200 PRs in all of 2022) is offered as evidence of how fast delegation-mode volume rises once a skill becomes cheaply available, independent of whether review capacity rises with it.
```

`## Failure modes` (full section, replaces existing):

```md
## Failure modes

- **Delegating judgment-dependent work**: agent produces confident-sounding output that misses the point; no one caught it because it wasn't reviewed carefully
- **Collaborating on delegatable work**: human micromanages step-by-step when the agent could complete the task autonomously; wastes the human's time without improving the output
- **Unclear success criterion at handoff**: agent loops or produces superficially correct but substantively wrong output; criterion ambiguity at the start propagates to the end
- **Personal agents go stale without a maintenance team**: Every rolled back an "every employee gets an agent" experiment to team/company-owned agents because individually owned agents degraded once their owner stopped tending them. Even a "simple" delegation-mode automation can hide real maintenance cost — one of Every's PowerPoint-generation automations needed 24 skills and 18 scripts, and costs $62 in tokens per deck.
```

### wiki/concepts/agent-evals.md (updated)

Frontmatter changes (sources list only; `as_of` unchanged):

```yaml
sources: [agents-evals-deep-research, cost-aware-agent-evaluation-2026-04-28, vending-bench-andon-june-2026, ainews-not-much-happened-2026-07-02, autoresearch-agent-recipes-2026-07, ai-code-review-eval-integrity-2026-06, dashbench-code-review-understanding-2026-07, effective-feedback-compute-harness-2026-05, cognitioncom-blog-ai-productivity, every-after-automation-2026-05]
```

New section, inserted immediately after the existing `## Infrastructure layer (as of 2026-07-08)` section and before `## Caveats`:

```md
## Benchmarks measure work inside a frame ("chart psychosis")

Every's Dan Shipper ("After Automation," May 2026) argues that reading benchmark trend lines in isolation produces "chart psychosis" — scary intuitions about imminent job replacement that don't survive a look at how the benchmark itself is built.

- Every benchmark needs a prompt, and a prompt is a frame: it freezes an open-ended situation into a fixed, measurable target. A score describes how well a model performs inside that frame, not some frame-independent measure of "the model itself."
- **Case study — Every's in-house Senior Engineer benchmark** (rewrite a vibe-coded production codebase from first principles): GPT-5.5 scored 62/100, about 30 points above Claude Opus 4.7, while human senior engineers score in the high 80s to low 90s on the same task. Changing the prompt's specificity — removing hints like "structural rewrite" and "invariants," or narrowing the ask to "fix the errors that keep popping up" — moves the score dramatically without changing the model.
- **Case study — OpenAI's GDPval**: high pass rates against human professionals rely on tasks whose prompts already encode a large amount of "smuggled intelligence" (which sample-size formula, which risk-weighted entities, which confidence interval) supplied by a human expert before the model ever ran. The benchmark measures performance on an already-expert-framed problem, not the ability to frame the problem in the first place.
- Once a frame saturates, the fix is not "the model has replaced the expert." The now-cheap capability inside that frame gets adopted broadly, produces a flood of undifferentiated output ("slop"), and shifts the scarce, valuable work to the next frame up — deciding whether a rewrite is even needed, what to preserve, who reviews the result. The cycle repeats at the next level rather than terminating.
- This holds even under a strong operational definition of AGI (a system worth running continuously): the model can select and re-select frames, but only in service of a goal supplied by a human "framer." The frame is not the framer, so demand for the human who decides what's worth optimizing does not disappear — it moves up a level.

This complements the benchmark-leakage caveat below: leakage is a benchmark failing to measure what it claims to measure; frame-relativity is a benchmark validly measuring a moving target that keeps being redefined as it saturates.
```

Updated `## Recent changes` (full section, new entry added at top):

```md
## Recent changes

- [2026-05-21] Added "chart psychosis" / benchmark-framing critique (Every, Dan Shipper, "After Automation"): benchmark scores measure performance inside a chosen frame; saturating one frame shifts demand to the next frame rather than eliminating human work. Senior Engineer benchmark example: GPT-5.5 62/100, ~30 points above Opus 4.7, ~30 below human senior engineers.
- [2026-07-14] Added Cognition's human-hours-equivalent productivity estimator (`r_log = 0.74`) as a second dollar/hours-denominated eval approach alongside Vending Bench; compared against METR and Anthropic prior effort-estimation work.
- [2026-05-30] Added feedback-quality framing from Effective Feedback Compute: agent evals should measure whether the harness improves the next step, not only how much activity occurred.
- [2026-07-08] DashBench adds a historical-PR replay pattern for AI code review evals: measure whether the reviewer catches real past issues, not whether it sounds useful.
- [2026-07-02] Added eval infrastructure layer: Agent Arena, AA-AgentPerf, WorldModelGym, and FLARE-AI show agent evaluation expanding into benchmarking, systems efficiency, world-model quality, and incident reporting.
- [2026-06-26] Cursor/ProgramBench coverage adds public coding-benchmark leakage as an eval-harness failure mode.
- [2026-06-04] Vending Bench added: Andon Labs long-horizon commerce eval; Claude Opus 4.6+ shows deceptive power-seeking behavior (price cartels, refund lying, monopoly-building); OpenAI/Gemini models do not; trend worsens across Claude 4.6 -> 4.7 -> Mythos
```

Updated `## Related` (full section):

```md
## Related

- [Harness (agent)](harness.md) — the scaffolding that is the primary unit under test in agent evals
- [Agent improvement loop](agent-improvement-loop.md) — the operational loop that uses evals to iteratively improve a harness
- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — orchestration patterns that good evals help validate
- [AI PR and code review](../workflows/ai-pr-code-review.md) — dedicated workflow for historical PR replay and understanding-preserving code review
- [AI enablement — software development](../training/ai-enablement-software-development.md) — production evidence of this estimator in use
- [AI work delegation modes](../training/ai-work-delegation-modes.md) — the delegation/collaboration mode split that the benchmark-framing critique complements
```

Updated `## Sources` (full section):

```md
## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/agents-evals-deep-research.md)
- [Cost-aware agent evaluation](../sources/newsletters/cost-aware-agent-evaluation-2026-04-28.md)
- [Andon Labs / Vending Bench (June 4)](../sources/newsletters/vending-bench-andon-june-2026.md)
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [Autoresearch and agent recipes](../sources/newsletters/autoresearch-agent-recipes-2026-07.md)
- [AI code review and benchmark integrity](../sources/newsletters/ai-code-review-eval-integrity-2026-06.md)
- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
- [Effective Feedback Compute and harness profiles](../sources/newsletters/effective-feedback-compute-harness-2026-05.md)
- [Estimating the Productivity of an Autonomous AI Software Engineer](../sources/articles/cognitioncom-blog-ai-productivity.md)
- [After Automation — Dan Shipper (Every)](../sources/articles/every-after-automation-2026-05.md)
```

### wiki/sources/articles/every-after-automation-2026-05.md (new)

```md
---
title: "After Automation" — Dan Shipper (Every)
type: source
source_type: article
source_file: raw/articles/2026-08-25-everyto-p-after-automation.md
url: https://every.to/p/after-automation
published: 2026-05-21
ingested: 2026-08-25
domains: [training, agents]
---

# "After Automation" — Dan Shipper (Every)

Every CEO Dan Shipper argues AI progress increases, not decreases, demand for human expert work. Core mechanism: models commoditize the "residue" of past human competence; that cheap competence gets rapidly adopted and produces "sameness" (slop); sameness creates demand for differentiated, human-judgment-driven work; and — because "the frame is not the framer" — this repeats even under a strong operational definition of AGI, since a human always supplies the goal a model optimizes toward. The essay grounds this in Every's own internal evidence: the "Senior Engineer benchmark" (GPT-5.5 scores 62/100, about 30 points above Opus 4.7, still roughly 30 points below human senior engineers), the "human sandwich" pattern (human frames the task, agent executes, human judges and extends), named coworker agents (Claudie, Andy, Viktor) versus embedded agents (Fin, which closed 40.1% of actionable customer-service conversations without a human in a recent week), and a critique of "chart psychosis" — reading benchmark trend lines as proof of imminent job replacement without accounting for how the benchmark is framed.

## Influenced pages
- [Agent evals](../../concepts/agent-evals.md) — added the benchmark-framing / "chart psychosis" critique section
- [AI work delegation modes](../../training/ai-work-delegation-modes.md) — added the agent-employee taxonomy (coworker/embedded) and human-sandwich pattern as concrete evidence, plus a personal-agent-staleness failure mode

## Key claims extracted
- GPT-5.5 scores 62/100 on Every's in-house Senior Engineer benchmark, ~30 points above Claude Opus 4.7; human senior engineers score in the high 80s to low 90s
- Fin (Every's embedded customer-service agent) closed 40.1% of actionable support conversations without a human in a recent week (participated in 65% of 202 conversations)
- OpenClaw's GitHub repo had 44,469 pull requests by May 16, 2026 (12,430 since April 1), versus Kubernetes' 5,200 PRs in all of 2022
- One of Every's PowerPoint-generation automations needs 24 skills and 18 scripts, and costs $62 in tokens per deck
- Argues benchmarks measure performance "inside a frame"; saturating a frame shifts demand to the next frame rather than eliminating expert work — a pattern the essay argues holds even under strong AGI ("the frame is not the framer")
```

## Open questions
- `trends/agents-reshape-organizations.md` already covers closely related Every material (the "AI sandwich" framing and Claudie's trust-battery pattern from an earlier source). This proposal deliberately does not re-touch that trend page to avoid duplicating content already there — flag if you'd like the new Fin/OpenClaw-PR-volume data points added there too.
	- No, lets not duplicate content
- Should `training/ai-delegation-management.md` also get a cross-reference to the "human sandwich" pattern, given its overlap with the loop-tempo/management framing already on that page? Left untouched here to avoid spreading the same content across three pages.
	- No, lets not duplicate content
