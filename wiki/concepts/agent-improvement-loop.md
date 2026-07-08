---
title: Agent improvement loop
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-07-07
sources: [trace-agent-improvement-loop, langchain-better-harness, cursor-bugbot-learning, self-improving-skills, agents-evals-deep-research, langchain-interrupt-may-2026, autoresearch-agent-recipes-2026-07, agent-memory-systems-layer-2026-06]
---

# Agent improvement loop

A workflow for improving AI agents by studying **execution traces** and feedback signals: records of what the agent actually did during a run, eval results, human review, cost data, and recurring failure patterns. Autoresearch extends this into an outer loop where agents study and maintain the primary agent system itself. The loop is: collect traces, score or review them, identify recurring failure patterns, make targeted changes, validate those changes offline, then redeploy and repeat.

## Current status (as of 2026-04-24)

- LangChain frames tracing as the foundation for systematic agent improvement, not just debugging
- The loop spans both staging and production, with production traces treated as the most valuable source of real failures
- Online evals, offline evals, and human review are complementary layers
- The concept is broader than any one vendor, even though the source article is product-adjacent
- LangChain's Better-Harness (open-sourced 2026-04-10) automates the loop: sources evals, splits optimization/holdout sets, iteratively diagnoses failures from traces, and proposes targeted harness changes with overfitting guards
- Cursor's Bugbot provides a product example of the same pattern: reactions, replies, and reviewer comments become candidate rules that are promoted or disabled based on later production signal
- Autoresearch treats the agent system itself as the research subject: agents inspect traces, failures, eval results, human feedback, and cost signals to propose improvements under governance controls

## The loop

1. **Collect traces** from staging, eval runs, and production.
2. **Enrich them** with online evals, human ratings, corrections, or comments.
3. **Find patterns** in the failures rather than treating each bad run as isolated.
4. **Make targeted changes** to prompts, routing, tools, or orchestration.
5. **Validate offline** with repeatable test cases built from real failures.
6. **Deploy** and use the new production traces as the starting point for the next cycle.

## Why traces matter

In a normal app, logs usually tell you whether something broke. In an AI system, an execution trace is richer: it shows the path the agent took, which tools it used, what the model saw, and where the reasoning or workflow went off track. That makes traces the raw material for improving behavior, not just monitoring uptime.

## Online vs offline evals

- **Online evals** monitor live behavior and surface drift, edge cases, and traces worth reviewing.
- **Offline evals** test proposed fixes against curated datasets before release.

The practical pattern is: use online signals to discover failure modes, then encode those failures into offline tests so future changes can be measured and regressions caught before shipping.

## Role of human review

Human review still matters when correctness depends on domain judgment or nuance that an automated grader may miss. Reviewers can also create ground-truth outputs, calibrate evaluators, and leave comments that make failure patterns easier to cluster later.

## Better-Harness: autonomous harness hill-climbing

LangChain's Better-Harness is a prototype that formalizes the improvement loop as:

1. **Source and tag evals** — hand-curated, mined from production traces, adapted from external datasets
2. **Split** into optimization and holdout sets per behavioral category
3. **Baseline** — run the current harness against both sets
4. **Optimize** — iteratively diagnose errors from traces, propose one scoped harness change at a time (prompt edits, tool descriptions, tool additions)
5. **Validate** — check that changes pass new evals without regressing passing ones; holdout set guards against overfitting
6. **Human review** — manual gate catches overfit instructions and token waste

Tested with Claude Sonnet 4.6 and GLM-5. Results showed near-full generalization to holdout sets on tool_selection and followup_quality categories. The analogy is explicit: `harness + evals + harness engineering → better agent`, mirroring `model + training data + gradient descent → better model`.

## Product example: Bugbot learned rules

Cursor's Bugbot shows what the improvement loop looks like when shipped inside a user-facing product. Instead of relying only on offline experiments, Bugbot turns feedback from merged PRs into candidate rules, evaluates those rules on later PRs, activates rules that keep earning good signal, and disables rules that perform poorly. That is the same core loop in more operational form: production traces plus human feedback become structured changes to the harness.

## LangSmith Engine: observability as improvement loop

LangChain's LangSmith Engine (launched May 2026 at Interrupt) shows the improvement loop productized at the observability layer. Unlike passive trace logging, Engine actively:

1. Consumes traces from production and staging
2. Clusters failures by pattern
3. Identifies likely code issues behind each cluster
4. Proposes fixes and evals for those specific failure modes

The loop closes without requiring a human to manually review traces and hypothesize causes — the system surfaces the hypotheses automatically for human confirmation.

SmithDB underpins this: a database built specifically for nested, long-running agent traces with large payloads. Built on Apache DataFusion and Vortex, it claims 12–15× faster access on key agent-trace workloads compared to general-purpose databases. The architectural bet is that agent traces are a different workload shape from application logs — nested structure, large payloads, and queries that follow the parent→child trace hierarchy rather than time-range scans.

## Trace-to-memory feedback

Production traces can improve an agent by changing its memory, not only its prompts, tools, or evals. The loop is: collect traces, extract candidate memories, deduplicate and reconcile them, scope them to the right actor/workflow, write them back with provenance, then monitor whether retrieval improves or creates stale-fact failures.

The risk is memory pollution. A trace-derived memory should not become durable just because it appeared in a run; it needs evidence, conflict checks, and a clear owner/scope.

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

## Eval suite hygiene

An eval suite that is not actively maintained will betray you. If you run the same 50 hand-authored test cases indefinitely, the agent optimizes for passing those exact cases and starts failing on the real failure modes that did not exist when the cases were written. The suite needs to evolve as fast as the agent and the environment do.

**Four practices that prevent eval rot:**

**1. Continuous trace mining.** Once an agent is deployed, even in shadow mode, monitor production logs actively. When a user reports a bad response, or when the agent triggers an error, extract that execution trace, anonymize it, and convert it into a new test case. Production failures are more valuable than synthetic cases because they reflect real failure modes, not imagined ones.

When a production incident occurs, for example an agent approving an action that violated policy, that incident should yield a regression test. Generate synthetic variations of the failing interaction so the agent learns the underlying principle, not just the exact case.

**2. Hidden holdout sets.** Maintain a separate set of eval cases that the development team cannot see during normal work. Periodically test against this blind holdout to get an unbiased measure of generalization. If you only test on cases developers have already seen, you are measuring memorization, not capability.

This applies in both directions: do not let holdout cases leak into training data, and do not let eval designers inspect them when writing new cases.

**3. Periodic refresh.** The environment changes. APIs update. Company policies change. Support ticket formats shift. Eval cases built against deprecated documentation will falsely penalize a correct agent. Review and update cases regularly: weekly for fast-moving agent surfaces, monthly at minimum for stable ones.

**4. Retiring stale tests.** A test that achieves a 100% pass rate across many consecutive updates is no longer providing much signal. It is measuring something the agent has already mastered. Archive it and redirect compute toward edge cases and new failure modes instead.

**The meta-rule:** treat the eval suite as a product, not a one-time artifact. It has a maintenance burden, it goes stale, and it needs active curation to stay useful.

## Caveats

- This is a conceptual guide from LangChain, not an independent market survey.
- The main claim is about process discipline, not a new algorithmic breakthrough.
- Some product-performance claims in the source are vendor-reported.

## Recent changes

- [2026-07-07] Added trace-to-memory feedback: offline trace analysis can write back maintained memories, but needs dedupe, scope, and conflict checks.
- [2026-07-01] Added autoresearch as an outer-loop pattern: agents study and improve the primary agent system using traces, evals, human signals, and cost data.
- [2026-05-15] LangSmith Engine added: actively clusters trace failures and proposes fixes/evals — observability as improvement loop, not passive logging. SmithDB: purpose-built agent-trace database, 12-15× faster, Apache DataFusion + Vortex
- [2026-04-24] Added eval suite hygiene section: holdout sets, trace mining, periodic refresh, and retiring stale tests
- [2026-04-22] Added self-improving skills pattern: closed feedback loop for skill drift; meta-skill 5-step prompt optimization loop
- [2026-04-10] Added Cursor Bugbot as a production example of live feedback turning into agent rules
- [2026-04-10] Added Better-Harness section — LangChain's autonomous harness hill-climbing system

## Related

- [Harness (agent)](harness.md) — the harness is what the improvement loop iterates on; better traces → targeted harness changes
- [Skillify — Agent Reliability Pattern](../workflows/skillify-agent-reliability.md) — complementary pattern: encodes failures as permanent skills rather than harness-level prompt changes; works at the skill/script layer instead of the orchestration layer
- [Evals for agentic software development](../training/evals-for-agentic-software-development.md) — coding-agent eval patterns for deterministic gates, shadow mode, and trace-derived regression suites
- [Evals for workflow and task agents](../training/evals-for-agentic-work.md) — workflow-agent eval patterns for reliability, simulation, and production-safe evaluation

## Sources

- [The Agent Improvement Loop Starts with a Trace — LangChain](../sources/articles/trace-agent-improvement-loop.md)
- ["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/articles/langchain-better-harness.md)
- [Bugbot now self-improves with learned rules](../sources/articles/cursor-bugbot-learning.md)
- [Self-improving agent skills — auto-improvement loops](../sources/tweets/self-improving-skills.md)
- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/agents-evals-deep-research.md)
- [LangChain Interrupt conference — May 2026](../sources/newsletters/langchain-interrupt-may-2026.md)
- [Autoresearch and agent recipes](../sources/newsletters/autoresearch-agent-recipes-2026-07.md)
- [Agent memory becomes a systems layer](../sources/newsletters/agent-memory-systems-layer-2026-06.md)
