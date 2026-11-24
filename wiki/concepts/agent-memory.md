---
title: Agent memory
type: concept
domains: [agents]
tags: [agentic, knowledge-cluster]
as_of: 2026-11-24
sources: [agent-memory-without-vector-db, memory-vs-context-rot-february, agent-memory-systems-layer-2026-06, minteval-paper-2026-05, ainews-erdos-benchmarks-cluster-2026-05-21, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06, anthropic-components-of-agent-memory-2026-11, asymptote-labs-agent-beacon]
---

# Agent memory

Agent memory is the problem of helping an AI system recover the right facts from past work after the live session window is gone. The core challenge is not only storing history, but retrieving the right parts of it in a form the model can actually use. In the [Knowledge architectures](knowledge-architectures.md) matrix it is the per-agent store of *episodic facts* extracted from sessions, written by the agent itself under governed rules; it is not the shared compiled corpus (that is a [knowledge layer](knowledge-layer.md)) and not the organization-scope system (that is a [company brain](company-brain.md)).

## Also called

Memory layer, memory system, long-term agent memory. "Ghost memory" is not an alias but a named failure mode (see below).

## Current status (as of 2026-11-24)

- Memory is moving from "retrieve old facts" toward a lifecycle system: extract candidate memories, deduplicate them, reconcile conflicts, scope them to the right user/team/task, retrieve evidence, and expire or update stale facts.
- Supermemory's ASMR system uses specialized agents to read conversation history and extract facts instead of embedding everything and querying by similarity; Engram-style systems frame memory as asynchronous infrastructure that turns traces into cleaned, scoped memories rather than stuffing every event back into the prompt.
- Cognition ships the lifecycle as a product and opens its format (October 2026). Agent Memory Repo stores one user's agent memory as a git repo of markdown files: a `MEMORY.md` entry point with an index, one fact per line, each ending in a link to the session that produced it, and wiki-style links between files. Devin "Dreaming" runs overnight to prune and link that memory graph. Together they put two of the practical implications below (provenance on every memory, structure a human can inspect and prune) into a shipping agent, and git gives shared writes for free (see the swarm-workspace pattern on [Multi-agent coordination](../workflows/multi-agent-coordination.md)).
- Memory is starting to sit across harnesses rather than inside one. Asymptote Labs' open-source [Beacon](../tools/beacon.md) captures sessions from 20+ coding harnesses into one trace format, extracts workflows, corrections and repo conventions, has a human approve them, and serves them back to every harness through MCP or Agent Skills.
- A-TMA-style "ghost memory" work highlights a concrete failure mode: stale and current facts can be retrieved together, causing long-running assistants to act on outdated state.
- ReContext and BlockSearch-style work suggests some memory failures are inference-time evidence-use problems, not only storage problems.
- MINTEval (arXiv, 2026-05) gives independent benchmark evidence for this: across 7 systems (vanilla long-context LLMs, RAG, and memory-augmented agent frameworks) evaluated on long, interference-heavy contexts (state tracking, multi-turn dialogue, Wikipedia revisions, GitHub commits — averaging 138.8k tokens, up to 1.8M), average accuracy is only 27.9% (best system 33.4%, per AINews' recap of the authors' thread), with accuracy degrading further as the number of intervening updates increases.

## Why it matters

Many agent systems fail not because they lack storage, but because they surface the wrong fragment at the wrong time. A memory architecture that can re-read history, synthesize the relevant facts, and expose them cleanly may matter more than squeezing better recall out of a generic vector-search stack.

## Context editing and persistent state

In-loop context management (explicit mutable state instead of growing transcripts, RL credit for individual context edits, compaction by deletion, and the Google DeepMind trace → knowledge-store → skill ablation) now lives on [Context editing](context-editing.md). It is a technique inside one session rather than a store kept between sessions; Anthropic's definition of agent memory explicitly excludes compaction.

## How agents write memory, and dreaming

Anthropic's "The components of agent memory" (November 2026) separates writing notes during a session from consolidating them afterwards, and measures both.

- **Salience judgment improves with model generation.** On a CL-Bench 1.0 task (a fresh session per question, one persistent memory directory), Sonnet 4.6 left scattered untested theories, Opus 4.7 consolidated its notes and marked what was checked, and Opus 5 was the first to "close the loop" with validated rules and warnings about traps; Opus 5.5 and Sonnet 5.5 matched it. In Pokémon Red, Sonnet 3.7 wrote 413 files in 225 folders and won one badge, while Fable 5 wrote nine files plus a `global.md` dashboard and won four, storing only what the screen could not tell it.
- **Say what memory is for, not how to use it.** Telling strong models a memory folder exists was enough; a fixed rule such as "record only failures" cut most of Opus 5's and Opus 4.7's gain. Steering helps older models: prompting Sonnet 4.6 to read memory and test its theories nearly doubled its score.
- **Dreaming corrects and promotes.** Dreaming reviews memory against the original transcripts. It fixed a wrong landmark note that otherwise kept Claude looping, repaired broken links in agent-built wikis, and can promote a few notes into every session's context. That top layer has to stay small: Claude Code's auto memory loads only the first 200 lines or 25 KB of `MEMORY.md`, used as an index. Dreamed wikis are on [Knowledge layer](knowledge-layer.md).
- **Open trade-offs.** Writing notes in-session costs attention, dreaming costs compute, and memory drifts, so dreaming may need to target the information most likely to change.

## Practical implications

- Separate "store everything" from "understand what matters"
- Treat memory retrieval as a mini-analysis task, not only a nearest-neighbor lookup
- Treat memory writes as a governed operation, not automatic accumulation.
- Store evidence and provenance with important memories so humans can debug why the agent believes something.
- Add conflict detection and stale-fact handling before committing durable memories.
- Separate private user memory, team memory, workflow memory, and the shared [knowledge layer](knowledge-layer.md) that serves as source of truth.
- Prefer memory structures humans can inspect and prune instead of silent accumulation

## Recent changes

- [2026-11-24] Added cross-harness memory: [Beacon](../tools/beacon.md) turns session traces from 20+ coding harnesses into human-approved, shared knowledge.
- [2026-11-24] Split: "Context editing and persistent state" (mutable state, ContextPilot, the trace → knowledge-store → skill ablation, deletion-only compaction) moved to [Context editing](context-editing.md); a pointer stays here.
- [2026-11-07] Added "How agents write memory, and dreaming" from Anthropic's memory evals: salience by model generation, purpose-not-rules prompting, dreaming as correction and promotion, Claude Code auto memory's 200-line / 25 KB load.
- [2026-10-06] Added Cognition's Agent Memory Repo (git-and-markdown memory format, one sourced fact per line, `MEMORY.md` index) and Devin Dreaming (overnight prune-and-link pass).
- [2026-09-09] Terminology reorganization: added the `## Also called` alias line, dated the Current-status stamp, and rewrote the Related lines to agree with the new [Knowledge architectures](knowledge-architectures.md) hub (this page previously described itself as "retrieval mechanics" on one page and as a "lifecycle system" on another).
- [2026-07-07] AINews memory cluster updates agent memory from retrieval problem to systems layer: extraction, dedupe, reconciliation, scoping, lifecycle, and offline trace writeback.
- [2026-05-19] MINTEval published: a dedicated benchmark for long-horizon memory under multi-target interference; 7 evaluated systems average 27.9% accuracy (best 33.4% per AINews' recap), giving independent confirmation that current memory systems are far from solved.

## Related

- [Knowledge architectures](knowledge-architectures.md) — the hub that places this page against knowledge layers, company brains, and ontologies
- [Knowledge layer](knowledge-layer.md) — the shared, human-legible compiled corpus; agent memory is what one agent learned from its own sessions, and the two usually coexist
- [Company brain](company-brain.md) — the organization-scope system; its "remembering" and "dreaming & pruning" functions are agent-memory lifecycle mechanics applied at company scale
- [Context editing](context-editing.md) — managing what stays in the context window during one session (mutable state, compaction); split out of this page

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
- [Cognition — Agent Memory Repo](../sources/articles/cognition-agent-memory-repo-2026-10.md)
- [AINews — Devin Dreaming and Agent Memory Repo](../sources/newsletters/ainews-devin-dreaming-2026-10-06.md)
- [Anthropic — The components of agent memory](../sources/articles/anthropic-components-of-agent-memory-2026-11.md)
- [Asymptote-Labs/agent-beacon (GitHub)](../sources/repos/asymptote-labs-agent-beacon.md)
