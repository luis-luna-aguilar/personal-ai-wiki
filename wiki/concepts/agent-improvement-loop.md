---
title: Agent improvement loop
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-04-10
sources: [trace-agent-improvement-loop, langchain-better-harness]
---

# Agent improvement loop

A workflow for improving AI agents by studying **execution traces**: records of what the agent actually did during a run, including model calls, tool calls, intermediate steps, and outputs. The loop is: collect traces, score or review them, identify recurring failure patterns, make targeted changes, validate those changes offline, then redeploy and repeat.

## Current status (as of 2026-04-09)

- LangChain frames tracing as the foundation for systematic agent improvement, not just debugging
- The loop spans both staging and production, with production traces treated as the most valuable source of real failures
- Online evals, offline evals, and human review are complementary layers
- The concept is broader than any one vendor, even though the source article is product-adjacent
- LangChain's Better-Harness (open-sourced 2026-04-10) automates the loop: sources evals, splits optimization/holdout sets, iteratively diagnoses failures from traces, and proposes targeted harness changes with overfitting guards

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

## Caveats

- This is a conceptual guide from LangChain, not an independent market survey.
- The main claim is about process discipline, not a new algorithmic breakthrough.
- Some product-performance claims in the source are vendor-reported.

## Recent changes

- [2026-04-10] Added Better-Harness section — LangChain's autonomous harness hill-climbing system
- [2026-04-09] Page created from LangChain's conceptual guide "The Agent Improvement Loop Starts with a Trace"

## Sources

- [[sources/articles/trace-agent-improvement-loop]]
- [[sources/articles/langchain-better-harness]]
