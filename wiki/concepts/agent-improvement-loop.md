---
title: Agent improvement loop
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-04-22
sources: [trace-agent-improvement-loop, langchain-better-harness, cursor-bugbot-learning, self-improving-skills]
---

# Agent improvement loop

A workflow for improving AI agents by studying **execution traces**: records of what the agent actually did during a run, including model calls, tool calls, intermediate steps, and outputs. The loop is: collect traces, score or review them, identify recurring failure patterns, make targeted changes, validate those changes offline, then redeploy and repeat.

## Current status (as of 2026-04-10)

- LangChain frames tracing as the foundation for systematic agent improvement, not just debugging
- The loop spans both staging and production, with production traces treated as the most valuable source of real failures
- Online evals, offline evals, and human review are complementary layers
- The concept is broader than any one vendor, even though the source article is product-adjacent
- LangChain's Better-Harness (open-sourced 2026-04-10) automates the loop: sources evals, splits optimization/holdout sets, iteratively diagnoses failures from traces, and proposes targeted harness changes with overfitting guards
- Cursor's Bugbot provides a product example of the same pattern: reactions, replies, and reviewer comments become candidate rules that are promoted or disabled based on later production signal

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

## Caveats

- This is a conceptual guide from LangChain, not an independent market survey.
- The main claim is about process discipline, not a new algorithmic breakthrough.
- Some product-performance claims in the source are vendor-reported.

## Recent changes

- [2026-04-10] Added Cursor Bugbot as a production example of live feedback turning into agent rules
- [2026-04-10] Added Better-Harness section — LangChain's autonomous harness hill-climbing system
- [2026-04-09] Page created from LangChain's conceptual guide "The Agent Improvement Loop Starts with a Trace"
- [2026-04-22] Added self-improving skills pattern: closed feedback loop for skill drift; meta-skill 5-step prompt optimization loop

## Sources

- [[sources/articles/trace-agent-improvement-loop]]
- [[sources/articles/langchain-better-harness]]
- [[sources/articles/cursor-bugbot-learning]]
- [[sources/tweets/self-improving-skills]]
