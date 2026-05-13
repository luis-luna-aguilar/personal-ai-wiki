---
title: AI coding vocabulary
type: training
domains: [coding, agents]
tags: [agentic]
as_of: 2026-05-01
sources: [mattpocock-dictionary-of-ai-coding]
---

# AI coding vocabulary

Teams using coding agents need shared language for the things that actually determine outcomes: the model, the harness, the session, the context window, the tools, the environment, and the handoff between runs.

## Current guidance

- Use **model** for what the provider actually serves: the neural network weights that process your input and return a response. A model has no memory between calls — it only knows what you send in each request. The word is often misused to describe the entire product experience; that whole system is the agent, built by wrapping a model in a harness.
- Use **agent** for the harnessed system a person interacts with: model plus tools, system prompt, environment, permissions, and loop behavior.
- Use **context** for the information the agent has available right now; distinguish it from durable memory and from the finite context window sent to the model.
- Use **session** for the bounded run that accumulates tool results and conversation history until it is cleared, compacted, or handed off.
- Use **harness** for the scaffolding around the model: tools, prompts, orchestration, context management, permission layers, and environment access.
- Use **environment** for what the agent can actually act on: the filesystem, browser, APIs, shell, and connected services.

## Teaching pattern

Start with the operational distinction: if two products use the same model but behave differently, the harness and environment explain the difference. This prevents teams from over-attributing success or failure to model choice alone.

## Failure modes

- Calling every behavior "the model" and missing harness, tool, or context problems
- Treating a long session as memory instead of a context window slowly filling up
- Letting handoffs depend on chat history instead of durable artifacts

## Sources

- [Matt Pocock — Dictionary of AI Coding](../sources/repos/mattpocock-dictionary-of-ai-coding.md)
