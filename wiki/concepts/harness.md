---
title: Harness (agent)
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-04-10
sources: [agentic-thinking-lin, langchain-better-harness]
---

# Harness (agent)

The scaffolding that wraps an AI model and turns it into an agent capable of acting in the world. A harness defines *what* the model can do (tools, APIs, memory), *how* it reasons and plans (system prompt, instructions, routing logic), and *what environment* it operates in (browser, terminal, code sandbox, external services).

The analogy to model training is explicit in the field: just as training data shapes a model, the harness shapes an agent's behavior. As [[sources/articles/langchain-better-harness|LangChain's Better-Harness]] frames it: `harness + evals + harness engineering → better agent` mirrors `model + training data + gradient descent → better model`.

## What a harness includes

- **System prompt & instructions** — behavioral constraints, task framing, output format rules
- **Tool suite** — which tools the model can call, their descriptions, when to use them
- **Orchestration logic** — how the agent loops, when it escalates, how sub-agents are coordinated
- **Execution environment** — browser, terminal, code sandbox, API layers, memory systems
- **Evaluation layer** — evals and traces that measure whether the agent behaves as intended

## Why it matters

In the reasoning era, the competitive edge was in model training — better RL, stronger feedback signals. In the agentic era, as [[sources/articles/agentic-thinking-lin|Junyang Lin argues]], the edge is in the harness: environment quality, prompt precision, tool design, and the ability to iterate on behavior without retraining the model. Harness engineering is increasingly treated as a first-class discipline.

## Harness vs model

A well-engineered harness can compensate for a weaker model. A poor harness can cripple a strong one. This is why [[sources/articles/langchain-better-harness|Better-Harness]] and similar systems focus on *harness hill-climbing* — iteratively improving the harness using evals as a signal, separate from any model update.

## Caveats

- The term has no single agreed definition across the field. Some sources use it narrowly (just the prompt + tool config); others include the full execution environment and orchestration layer.
- This page reflects the broader definition, consistent with [[sources/articles/agentic-thinking-lin|Lin's essay]] and [[sources/articles/langchain-better-harness|LangChain's Better-Harness]] framing.

## Sources

- [[sources/articles/agentic-thinking-lin]]
- [[sources/articles/langchain-better-harness]]
