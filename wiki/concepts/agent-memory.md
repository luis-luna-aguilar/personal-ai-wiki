---
title: Agent memory
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-03-23
sources: [agent-memory-without-vector-db, memory-vs-context-rot-february]
---

# Agent memory

Agent memory is the problem of helping an AI system recover the right facts from past work after the live session window is gone. The core challenge is not only storing history, but retrieving the right parts of it in a form the model can actually use.

## Current status

- A late-March source argues that long-term memory is becoming an active retrieval-and-reasoning problem, not just a vector-database problem
- Supermemory's ASMR system is described as using specialized agents to read conversation history, analyze it, and extract facts instead of embedding everything and querying by similarity
- The reported benchmark jump is large: LongMemEval from roughly 85% to 98.6%
- If this framing holds up, memory quality depends more on how history is interpreted than on which embedding store sits underneath it

## Why it matters

Many agent systems fail not because they lack storage, but because they surface the wrong fragment at the wrong time. A memory architecture that can re-read history, synthesize the relevant facts, and expose them cleanly may matter more than squeezing better recall out of a generic vector-search stack.

## Practical implications

- Separate "store everything" from "understand what matters"
- Treat memory retrieval as a mini-analysis task, not only a nearest-neighbor lookup
- Keep the extracted facts legible so humans can inspect what the agent thinks it remembers
- Treat persistent memory as a tradeoff, not a free upgrade: better recall can be offset by stale instructions, contradictory preferences, and "context rot"
- Prefer memory structures humans can inspect and prune instead of silent accumulation

## Related

- [Knowledge layer](knowledge-layer.md) — complementary concept: a compiled, maintained context surface that sits above raw sources; where agent-memory focuses on retrieval mechanics, the knowledge layer focuses on how content is structured and maintained

## Caveats

- The current source set is centered on one startup's claims and a benchmark delta reported through newsletter coverage
- This should be read as an architectural signal worth watching, not as proof that vector retrieval is obsolete in every setting

## Sources

- [Agent memory without vector databases](../sources/newsletters/agent-memory-without-vector-db.md)
- [Memory versus context rot in late February](../sources/newsletters/memory-vs-context-rot-february.md)
