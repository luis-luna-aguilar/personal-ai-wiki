---
title: Agent evals
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-09-01
sources: [agents-evals-deep-research, cost-aware-agent-evaluation-2026-04-28, ainews-not-much-happened-2026-07-02, autoresearch-agent-recipes-2026-07, ai-code-review-eval-integrity-2026-06, dashbench-code-review-understanding-2026-07, effective-feedback-compute-harness-2026-05, every-after-automation-2026-05, ainews-fal-h3-max-live-2026-09-01, ainews-openai-shuts-off-cursor-2026-08-29]
---

# Agent evals

Evaluating an AI agent is not the same as evaluating an AI model. When you run a coding agent, you are not testing the underlying model in isolation. You are testing the combined system: `model + harness + tools + environment`. A change to any of those layers can change agent behavior even when the model itself has not changed.

That means agent evals are really about evaluating systems and behaviors: trajectories, tool use, policy adherence, failure recovery, and output quality together, not output quality alone.

## Why trajectory matters

Two agents can reach the same correct answer through very different paths. One got there efficiently in three steps. The other hallucinated a tool call, self-corrected, read thirty irrelevant files, and eventually succeeded. A result-only check marks both as passing. A trajectory eval catches the broken one.

This is why trajectory evaluation matters: the path reveals planning quality, tool efficiency, and failure risk, none of which are visible from the final answer alone.

## Seven eval dimensions

A useful agent eval suite covers seven dimensions, each catching a different class of failure:

- **Capability** — can the agent perform the task at all? This establishes baseline usefulness before worrying about efficiency or robustness.
- **Regression** — did a change to the prompt, tools, or underlying model break something that used to work?
- **Trajectory** — did the agent take a logical, efficient path? Did it avoid loops, call tools in the right order, and ask for clarification instead of guessing?
- **Unit-level** — does each component of the architecture work correctly in isolation? Examples: tool routing, retrieval, parsing, or permission checks.
- **Online (production)** — asynchronous scoring of live traffic to detect quality degradation, cost explosions, or latency spikes before users notice. In early autoresearch loops, human feedback often supplies the highest-value signal before automated judges are stable enough to trust.
- **Cost and variance** — tracking token spend per task run and run-to-run variance alongside correctness; agent evals that only measure capability miss the cost and reliability dimensions that matter for production deployment. Retries after failures, runaway loops, and tokenizer differences between model versions all affect real costs independently of output quality.
- **Feedback quality** — whether the harness supplies feedback that lets the agent improve its next action. This is distinct from how many tokens or tools the agent used.

These categories are complementary. A unit-level failure suggests a routing or retrieval problem. A trajectory failure points to broken planning. A capability failure means the agent cannot do the task at all.

## Economic evals: dollar and hours-denominated

Rather than a fixed rubric, some evals score agents against real dollar or human-hour outcomes to avoid the saturation problem that plagues code-completion benchmarks — Andon Labs' Vending Bench (deceptive commerce behavior) and Cognition's Devin productivity estimator (`r_log = 0.74` against human-engineer-hours) are the two leading examples. See [Economic agent evals](economic-agent-evals.md) for the full methodology and findings.

## Multi-turn behavioral evals

Transluce released an independent evaluation of 77 model variants across major labs, testing responses to mental-health crisis scenarios across multi-turn conversations rather than single-turn prompts. Several researchers treated it as a template for future agent evals: OpenAI's Wojciech Zaremba argued evals must increasingly simulate users, networks, and internet environments over long horizons rather than scoring isolated exchanges; others emphasized the need for ongoing audits rather than one-time predeployment checks, since sustained, escalating pressure can surface behavior a single prompt never would. This extends the trajectory-evaluation argument above (see "Why trajectory matters") from single-session tool-use paths to extended, adversarial-context conversations.

## How this changes eval design

Because the harness, tools, and environment are part of what you are evaluating:

- Eval results are not portable across harnesses. A score on one scaffold says little about the same model on another.
- Small harness changes such as a reworded system prompt or a new tool description can shift results significantly without any model update.
- The eval suite needs to cover multiple layers: result quality, trajectory quality, and component quality.
- Eval-driven development becomes a first-class practice: iterate on the harness using evals as the signal, separate from any model update. That is the premise of [Agent improvement loop](agent-improvement-loop.md).
- Effective Feedback Compute is a useful direction because it evaluates the information value of feedback inside the loop. Long traces and many tool calls can still be low-value if they do not change the agent's trajectory toward success.
- **Task-completion benchmarks as a harness-evaluation surface.** Alibaba Accio's open-sourced CommerceAgentBench (107 tasks spanning procurement, listings, operations, fulfillment, after-sales) checks what an agent actually changed, saved, or submitted rather than what it claims; the best observed run passed only 61.7% of tasks.

## Infrastructure layer (as of 2026-07-08)

Agent evaluation is splitting into several infrastructure problems:

- **Historical-work replay.** DashBench, from DoorDash, replays historical PRs to test whether AI reviewers catch real issues that mattered in production rather than writing plausible comments. This is stronger than synthetic review prompts because it anchors review quality to known defects and team-specific code context. See [AI PR and code review](../workflows/ai-pr-code-review.md).
- **Agent arenas** compare models or harnesses in agent mode, not only chat mode.
- **Systems efficiency metrics** such as AA-AgentPerf measure agents-per-megawatt, making inference and runtime efficiency part of agent evaluation.
- **World-model evals** such as WorldModelGym test whether a simulated world supports better decisions, not only plausible generations.
- **Incident reporting** efforts such as FLARE-AI aim to route AI flaws and safety incidents to the right developers and registries.

The pattern: evals are no longer only pass/fail task scores. They are becoming observability, incident intake, cost accounting, historical replay, and system-capacity infrastructure.

## Benchmarks measure work inside a frame

Dan Shipper's "chart psychosis" critique (Every, May 2026) argues a benchmark score measures performance inside the frame its prompt sets, not the model in general; the full argument now lives on [AGI timeline claims](../trends/agi-timeline-claims.md). It complements the benchmark-leakage caveat below: leakage is a benchmark failing to measure what it claims to measure; frame-relativity is a benchmark validly measuring a moving target that keeps being redefined as it saturates.

## Caveats

- The five-category taxonomy here is a synthesis of common practice, not a single canonical industry standard.
- The harness-as-unit-under-test framing is widely shared, but the exact vocabulary varies by team and framework.
- **Benchmark leakage through public artifacts.** Coding agents may improve benchmark scores by retrieving known solutions from the internet, public repos, or git history instead of solving the task under intended constraints. A benchmark's network access, repository history, hidden tests, and tool permissions are part of what it measures.

## Related

- [Economic agent evals](economic-agent-evals.md) — dollar and human-hours-denominated evaluation methods
- [Harness (agent)](harness.md) — the scaffolding that is the primary unit under test in agent evals
- [Agent improvement loop](agent-improvement-loop.md) — the operational loop that uses evals to iteratively improve a harness
- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — orchestration patterns that good evals help validate
- [AI PR and code review](../workflows/ai-pr-code-review.md) — dedicated workflow for historical PR replay and understanding-preserving code review
- [Engineering AI adoption: evidence from practice](../training/engineering-ai-adoption-evidence.md) — production evidence of this estimator in use
- [AI work delegation modes](../training/ai-work-delegation-modes.md) — the delegation/collaboration mode split that the benchmark-framing critique complements

## Recent changes

- [2026-10-19] Added CommerceAgentBench as an outcome-checking task benchmark, moved from [Harness (agent)](harness.md).
- [2026-10-19] Split: the "chart psychosis" benchmark-framing critique moved to [AGI timeline claims](../trends/agi-timeline-claims.md); a one-paragraph pointer remains.
- [2026-09-01] Added multi-turn behavioral evals: Transluce's 77-model-variant mental-health-crisis eval, framed by researchers as a template for long-horizon, user/environment-simulating agent evals.
- [2026-07-14] Added a pointer to the new [Economic agent evals](economic-agent-evals.md) page (Cognition's human-hours-equivalent estimator alongside Vending Bench).
- [2026-07-08] DashBench adds a historical-PR replay pattern for AI code review evals: measure whether the reviewer catches real past issues, not whether it sounds useful.
- [2026-07-02] Added eval infrastructure layer: Agent Arena, AA-AgentPerf, WorldModelGym, and FLARE-AI show agent evaluation expanding into benchmarking, systems efficiency, world-model quality, and incident reporting.
- [2026-06-26] Cursor/ProgramBench coverage adds public coding-benchmark leakage as an eval-harness failure mode.
- [2026-05-30] Added feedback-quality framing from Effective Feedback Compute: agent evals should measure whether the harness improves the next step, not only how much activity occurred.

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/agents-evals-deep-research.md)
- [Cost-aware agent evaluation](../sources/newsletters/cost-aware-agent-evaluation-2026-04-28.md)
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [Autoresearch and agent recipes](../sources/newsletters/autoresearch-agent-recipes-2026-07.md)
- [AI code review and benchmark integrity](../sources/newsletters/ai-code-review-eval-integrity-2026-06.md)
- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
- [Effective Feedback Compute and harness profiles](../sources/newsletters/effective-feedback-compute-harness-2026-05.md)
- [After Automation — Dan Shipper (Every)](../sources/articles/every-after-automation-2026-05.md)
- [AINews — Fal's H3 Max Live breaks the infinite videogen barrier](../sources/newsletters/ainews-fal-h3-max-live-2026-09-01.md)
- [[AINews] OpenAI shuts off Cursor](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
