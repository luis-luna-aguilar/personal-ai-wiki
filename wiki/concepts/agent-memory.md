---
title: Agent memory
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-07-07
sources: [agent-memory-without-vector-db, memory-vs-context-rot-february, agent-memory-systems-layer-2026-06]
---

# Agent memory

Agent memory is the problem of helping an AI system recover the right facts from past work after the live session window is gone. The core challenge is not only storing history, but retrieving the right parts of it in a form the model can actually use.

## Current status

- Memory is moving from "retrieve old facts" toward a lifecycle system: extract candidate memories, deduplicate them, reconcile conflicts, scope them to the right user/team/task, retrieve evidence, and expire or update stale facts.
- Supermemory's ASMR system is described as using specialized agents to read conversation history, analyze it, and extract facts instead of embedding everything and querying by similarity.
- Engram-style systems frame memory as asynchronous infrastructure that turns traces and activity into cleaned, scoped memories rather than stuffing every event back into the prompt.
- A-TMA-style "ghost memory" work highlights a concrete failure mode: stale and current facts can be retrieved together, causing long-running assistants to act on outdated state.
- ReContext and BlockSearch-style work suggests some memory failures are inference-time evidence-use problems, not only storage problems.

## Why it matters

Many agent systems fail not because they lack storage, but because they surface the wrong fragment at the wrong time. A memory architecture that can re-read history, synthesize the relevant facts, and expose them cleanly may matter more than squeezing better recall out of a generic vector-search stack.

## Practical implications

- Separate "store everything" from "understand what matters"
- Treat memory retrieval as a mini-analysis task, not only a nearest-neighbor lookup
- Treat memory writes as a governed operation, not automatic accumulation.
- Store evidence and provenance with important memories so humans can debug why the agent believes something.
- Add conflict detection and stale-fact handling before committing durable memories.
- Separate private user memory, team memory, workflow memory, and source-of-truth knowledge layers.
- Prefer memory structures humans can inspect and prune instead of silent accumulation

## Recent changes

- [2026-07-07] AINews memory cluster updates agent memory from retrieval problem to systems layer: extraction, dedupe, reconciliation, scoping, lifecycle, and offline trace writeback.

## Related

- [Knowledge layer](knowledge-layer.md) — complementary concept: a compiled, maintained context surface that sits above raw sources; where agent-memory focuses on retrieval mechanics, the knowledge layer focuses on how content is structured and maintained

## Caveats

- The current source set is centered on one startup's claims and a benchmark delta reported through newsletter coverage
- This should be read as an architectural signal worth watching, not as proof that vector retrieval is obsolete in every setting

## Sources

- [Agent memory without vector databases](../sources/newsletters/agent-memory-without-vector-db.md)
- [Memory versus context rot in late February](../sources/newsletters/memory-vs-context-rot-february.md)
- [Agent memory becomes a systems layer](../sources/newsletters/agent-memory-systems-layer-2026-06.md)
