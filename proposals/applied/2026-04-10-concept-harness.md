---
type: proposal
source: internal — synthesized from raw/articles/2026-04-10-justinlin610githubio-blog-from-reasoning-to-agentic-thinking.md, raw/tweets/2026-04-10-vtrivedy10-2041927488918413589.md
status: pending
created: 2026-04-10
---

# Proposal: Concept page — Agent harness

## Summary

"Harness" is used heavily across multiple wiki pages but has no definition of its own. The term is inconsistently interpreted across the field — sometimes it means the scaffolding around a single agent loop, sometimes the full system of prompts + tools + memory + orchestration logic. This proposal anchors the concept with a compact, source-backed definition.

## Intended changes

- [x] **Create** `wiki/concepts/harness.md` — concept page defining what a harness is in the agent context
    > See draft below

- [x] **Update** `wiki/index.md` — add harness to concepts section

## Page drafts

### wiki/concepts/harness.md (new)

```
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

The analogy to model training is explicit in the field: just as training data shapes a model, the harness shapes an agent's behavior. `harness + evals + harness engineering → better agent` mirrors `model + training data + gradient descent → better model`.

## What a harness includes

- **System prompt & instructions** — behavioral constraints, task framing, output format rules
- **Tool suite** — which tools the model can call, their descriptions, when to use them
- **Orchestration logic** — how the agent loops, when it escalates, how sub-agents are coordinated
- **Execution environment** — browser, terminal, code sandbox, API layers, memory systems
- **Evaluation layer** — evals and traces that measure whether the agent behaves as intended

## Why it matters

In the reasoning era, the competitive edge was in model training — better RL, stronger feedback signals. In the agentic era, the edge is in the harness: environment quality, prompt precision, tool design, and the ability to iterate on behavior without retraining the model. Harness engineering is increasingly treated as a first-class discipline.

## Harness vs model

A well-engineered harness can compensate for a weaker model. A poor harness can cripple a strong one. This is why LangChain's Better-Harness and similar systems focus on *harness hill-climbing* — iteratively improving the harness using evals as a signal, separate from any model update.

## Caveats

- The term has no single agreed definition across the field. Some sources use it narrowly (just the prompt + tool config); others include the full execution environment and orchestration layer.
- This page reflects the broader definition, which is consistent with the Junyang Lin essay and LangChain's Better-Harness framing.

## Sources

- [[sources/articles/agentic-thinking-lin]]
- [[sources/articles/langchain-better-harness]]
```

## Comments

-  when you mention Lin's article of the better harness article, just link it please in the page 