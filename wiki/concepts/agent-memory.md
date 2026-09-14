---
title: Agent memory
type: concept
domains: [agents]
tags: [agentic, knowledge-cluster]
as_of: 2026-07-07
sources: [agent-memory-without-vector-db, memory-vs-context-rot-february, agent-memory-systems-layer-2026-06, minteval-paper-2026-05, ainews-erdos-benchmarks-cluster-2026-05-21]
---

# Agent memory

Agent memory is the problem of helping an AI system recover the right facts from past work after the live session window is gone. The core challenge is not only storing history, but retrieving the right parts of it in a form the model can actually use. In the [Knowledge architectures](knowledge-architectures.md) matrix it is the per-agent store of *episodic facts* extracted from sessions, written by the agent itself under governed rules; it is not the shared compiled corpus (that is a [knowledge layer](knowledge-layer.md)) and not the organization-scope system (that is a [company brain](company-brain.md)).

## Also called

Memory layer, memory system, long-term agent memory. "Ghost memory" is not an alias but a named failure mode (see below).

## Current status (as of 2026-07-07)

- Memory is moving from "retrieve old facts" toward a lifecycle system: extract candidate memories, deduplicate them, reconcile conflicts, scope them to the right user/team/task, retrieve evidence, and expire or update stale facts.
- Supermemory's ASMR system is described as using specialized agents to read conversation history, analyze it, and extract facts instead of embedding everything and querying by similarity.
- Engram-style systems frame memory as asynchronous infrastructure that turns traces and activity into cleaned, scoped memories rather than stuffing every event back into the prompt.
- A-TMA-style "ghost memory" work highlights a concrete failure mode: stale and current facts can be retrieved together, causing long-running assistants to act on outdated state.
- ReContext and BlockSearch-style work suggests some memory failures are inference-time evidence-use problems, not only storage problems.
- MINTEval (arXiv, 2026-05) gives independent benchmark evidence for this: across 7 systems (vanilla long-context LLMs, RAG, and memory-augmented agent frameworks) evaluated on long, interference-heavy contexts (state tracking, multi-turn dialogue, Wikipedia revisions, GitHub commits — averaging 138.8k tokens, up to 1.8M), average accuracy is only 27.9% (best system 33.4%, per AINews' recap of the authors' thread), with accuracy degrading further as the number of intervening updates increases.

## Why it matters

Many agent systems fail not because they lack storage, but because they surface the wrong fragment at the wrong time. A memory architecture that can re-read history, synthesize the relevant facts, and expose them cleanly may matter more than squeezing better recall out of a generic vector-search stack.

## Practical implications

- Separate "store everything" from "understand what matters"
- Treat memory retrieval as a mini-analysis task, not only a nearest-neighbor lookup
- Treat memory writes as a governed operation, not automatic accumulation.
- Store evidence and provenance with important memories so humans can debug why the agent believes something.
- Add conflict detection and stale-fact handling before committing durable memories.
- Separate private user memory, team memory, workflow memory, and the shared [knowledge layer](knowledge-layer.md) that serves as source of truth.
- Prefer memory structures humans can inspect and prune instead of silent accumulation

## Recent changes

- [2026-09-09] Terminology reorganization: added the `## Also called` alias line, dated the Current-status stamp, and rewrote the Related lines to agree with the new [Knowledge architectures](knowledge-architectures.md) hub (this page previously described itself as "retrieval mechanics" on one page and as a "lifecycle system" on another).
- [2026-07-07] AINews memory cluster updates agent memory from retrieval problem to systems layer: extraction, dedupe, reconciliation, scoping, lifecycle, and offline trace writeback.
- [2026-05-19] MINTEval published: a dedicated benchmark for long-horizon memory under multi-target interference; 7 evaluated systems average 27.9% accuracy (best 33.4% per AINews' recap), giving independent confirmation that current memory systems are far from solved.

## Related

- [Knowledge architectures](knowledge-architectures.md) — the hub that places this page against knowledge layers, company brains, and ontologies
- [Knowledge layer](knowledge-layer.md) — the shared, human-legible compiled corpus; agent memory is what one agent learned from its own sessions, and the two usually coexist
- [Company brain](company-brain.md) — the organization-scope system; its "remembering" and "dreaming & pruning" functions are agent-memory lifecycle mechanics applied at company scale

## Caveats

- Most of the lifecycle-architecture framing (extraction, dedupe, reconciliation) still traces back to one startup's claims (Supermemory, plus Engram) and a benchmark delta reported through newsletter coverage, not to independent benchmarks
- MINTEval is an independent academic benchmark (an arXiv preprint, not a vendor claim) and gives harder evidence that current memory systems — vanilla long-context LLMs, RAG, and memory-augmented agents alike — struggle badly (27.9% avg accuracy) on realistic interference-heavy tasks
- This should still be read as an architectural signal worth watching, not as proof that vector retrieval is obsolete in every setting — MINTEval shows every evaluated approach struggling, not one architecture winning

## Sources

- [Agent memory without vector databases](../sources/newsletters/agent-memory-without-vector-db.md)
- [Memory versus context rot in late February](../sources/newsletters/memory-vs-context-rot-february.md)
- [Agent memory becomes a systems layer](../sources/newsletters/agent-memory-systems-layer-2026-06.md)
- [MINTEval (arXiv paper)](../sources/papers/minteval-paper-2026-05.md)
- [AINews — agent-benchmark cluster (InferenceBench, Terminal-Bench Science, MINTEval)](../sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md)
