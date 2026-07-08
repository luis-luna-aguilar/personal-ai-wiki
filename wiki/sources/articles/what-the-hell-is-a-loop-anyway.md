---
title: "What the hell is a loop, anyway?"
type: source
source_type: article
source_file: raw/articles/2026-07-04-what-the-hell-is-a-loop-anyway.md
url: https://x.com/aparnadhinak/status/2073492320159510869
published: 2026-07-04
ingested: 2026-07-07
domains: [agents, coding]
---

# What the hell is a loop, anyway?

Aparna Dhinakaran, with Seldo, argues that AI engineering discourse is using "loop" to mean several different architectures. The article separates execution loops, task/Ralph loops, product/software-factory loops, and system/autoresearch loops, then adds an oversight layer where humans set goals, budgets, and culling criteria. The practical point is that each loop needs a named object of iteration, a closing signal, and a deliberate autonomy setting.

## Influenced pages

- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — adds a clearer loop taxonomy, Ralph task-loop pattern, oversight-loop framing, and pipeline-vs-loop distinction.

## Key claims extracted

- The same "loop" language currently covers at least four architectures: agent execution, single-spec task restarts, product/software-factory lifecycles, and system/autoresearch improvement loops.
- A Ralph loop restarts a coding agent against the same specification in a fresh context window each iteration, trading token cost for less context rot and clearer single-artifact completion.
- Product/software-factory loops iterate on a codebase and backlog, with external signals such as issues, production logs, user feedback, review outcomes, and monitoring.
- System/autoresearch loops improve the primary system itself: prompts, harnesses, model choices, evals, and even eval design.
- Agentic MapReduce is better understood as a fan-out topology or pipeline unless outputs feed back into another cycle.
- The top oversight loop is where goals, budgets, and culling decisions live; human agency should be explicit there even when lower loops become more autonomous.
