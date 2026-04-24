---
title: Deep Agents overview
type: source
source_type: article
url: https://docs.langchain.com/oss/python/deepagents/overview
ingested: 2026-04-23
domains: [agents]
---

# Deep Agents overview

LangChain's overview page for Deep Agents. The key framing is that Deep Agents is explicitly an agent harness: a tool-calling loop with planning, filesystem context management, subagents, permissions, memory, and skills packaged into one reusable layer.

## Influenced pages

- [[workflows/agentic-orchestration-patterns]] — adds a clearer batteries-included harness example to the orchestration-pattern landscape

## Key claims extracted

- Deep Agents is explicitly described as an "agent harness"
- Built-in capabilities include planning, filesystem context management, subagent spawning, long-term memory, permissions, human-in-the-loop, and skills
- It works with any LangChain chat model that supports tool calling
- The same package can target different providers, including OpenAI, Anthropic, Google, OpenRouter, and local backends
