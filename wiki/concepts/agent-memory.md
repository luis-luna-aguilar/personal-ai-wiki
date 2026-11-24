---
title: Agent memory
type: concept
domains: [agents]
tags: [agentic, knowledge-cluster]
as_of: 2026-10-26
sources: [agent-memory-without-vector-db, memory-vs-context-rot-february, agent-memory-systems-layer-2026-06, minteval-paper-2026-05, ainews-erdos-benchmarks-cluster-2026-05-21, ainews-openai-shuts-off-cursor-2026-08-29, ainews-fal-h3-max-live-2026-09-01, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06, tamaratran-fast-jev-compaction]
---

# Agent memory

Agent memory is the problem of helping an AI system recover the right facts from past work after the live session window is gone. The core challenge is not only storing history, but retrieving the right parts of it in a form the model can actually use. In the [Knowledge architectures](knowledge-architectures.md) matrix it is the per-agent store of *episodic facts* extracted from sessions, written by the agent itself under governed rules; it is not the shared compiled corpus (that is a [knowledge layer](knowledge-layer.md)) and not the organization-scope system (that is a [company brain](company-brain.md)).

## Also called

Memory layer, memory system, long-term agent memory. "Ghost memory" is not an alias but a named failure mode (see below).

## Current status (as of 2026-10-26)

- Memory is moving from "retrieve old facts" toward a lifecycle system: extract candidate memories, deduplicate them, reconcile conflicts, scope them to the right user/team/task, retrieve evidence, and expire or update stale facts.
- Supermemory's ASMR system uses specialized agents to read conversation history and extract facts instead of embedding everything and querying by similarity; Engram-style systems frame memory as asynchronous infrastructure that turns traces into cleaned, scoped memories rather than stuffing every event back into the prompt.
- Cognition ships the lifecycle as a product and opens its format (October 2026). Agent Memory Repo stores one user's agent memory as a git repo of markdown files: a `MEMORY.md` entry point with an index, one fact per line, each ending in a link to the session that produced it, and wiki-style links between files. Devin "Dreaming" runs overnight to prune and link that memory graph. Together they put two of the practical implications below (provenance on every memory, structure a human can inspect and prune) into a shipping agent, and git gives shared writes for free (see the swarm-workspace pattern on [Multi-agent coordination](../workflows/multi-agent-coordination.md)).
- Late-August 2026 research moves memory inside the agent's working loop: explicit mutable state instead of growing transcripts (WikiSkill / SKILL.state), RL credit assigned to individual context edits (ContextPilot), and a Google DeepMind ablation where a persistent knowledge store compiled from traces carried much of the gain (see "Context editing and persistent state" below).
- A-TMA-style "ghost memory" work highlights a concrete failure mode: stale and current facts can be retrieved together, causing long-running assistants to act on outdated state.
- ReContext and BlockSearch-style work suggests some memory failures are inference-time evidence-use problems, not only storage problems.
- MINTEval (arXiv, 2026-05) gives independent benchmark evidence for this: across 7 systems (vanilla long-context LLMs, RAG, and memory-augmented agent frameworks) evaluated on long, interference-heavy contexts (state tracking, multi-turn dialogue, Wikipedia revisions, GitHub commits — averaging 138.8k tokens, up to 1.8M), average accuracy is only 27.9% (best system 33.4%, per AINews' recap of the authors' thread), with accuracy degrading further as the number of intervening updates increases.

## Why it matters

Many agent systems fail not because they lack storage, but because they surface the wrong fragment at the wrong time. A memory architecture that can re-read history, synthesize the relevant facts, and expose them cleanly may matter more than squeezing better recall out of a generic vector-search stack.

## Context editing and persistent state

Late-August 2026 research moves memory inside the agent's working loop rather than leaving it as an external store:

- **Mutable state instead of growing transcripts.** WikiSkill / SKILL.state (Google DeepMind and collaborators) replaces ever-growing conversation histories with explicit mutable state plus persistent skill knowledge, reporting better long-horizon accuracy at lower cumulative token use.
- **Training agents to edit their own context.** Tencent's ContextPilot assigns RL reward at the level of specific context edits rather than final task outcome — a more targeted credit-assignment scheme for long-horizon tasks.
- **A persistent knowledge store carries much of the gain.** Google DeepMind researchers separated three layers: raw execution traces, a persistent accumulated-knowledge store (a "wiki"), and executable skills distilled from it. In ablation the store itself carried much of the measured gain, and the distilled skills transferred across model families, sometimes beating skills a model evolved for itself. That supports portable knowledge and skills over fine-tunes, which often fail to amortize when open base models change this fast. In the [Knowledge architectures](knowledge-architectures.md) vocabulary this store is closer to a [knowledge layer](knowledge-layer.md) than to per-agent episodic memory, though here the agent compiles it from its own traces.
- **Compaction by deletion instead of summary.** The public [fast-jev-compaction](../tools/fast-jev-compaction.md) plugin and npm package (October 2026) replaces Claude Code's compaction summary with pruning. It sends TypeSafe's [Jev](../models/jev.md) decision model the whole conversation, with tool results shortened to size notes, and gets two keep probabilities per tool call: is the call still worth knowing about, and is its output still needed word for word. Below the threshold the output is cut to its first 300 characters or the call is removed with its result. User and assistant text, the first message, and the newest messages are never touched, and everything kept stays verbatim, so the file paths, exact errors, and constraints a summary can lose survive. It falls back to the built-in summary when it cannot remove enough. The author's caveat: a keep probability is not proof a result is safe to delete, though the agent can re-run the tool.

## Practical implications

- Separate "store everything" from "understand what matters"
- Treat memory retrieval as a mini-analysis task, not only a nearest-neighbor lookup
- Treat memory writes as a governed operation, not automatic accumulation.
- Store evidence and provenance with important memories so humans can debug why the agent believes something.
- Add conflict detection and stale-fact handling before committing durable memories.
- Separate private user memory, team memory, workflow memory, and the shared [knowledge layer](knowledge-layer.md) that serves as source of truth.
- Prefer memory structures humans can inspect and prune instead of silent accumulation

## Recent changes

- [2026-10-26] Added deletion-only compaction ([fast-jev-compaction](../tools/fast-jev-compaction.md)): a decision model scores each tool call and result for keeping, and kept messages stay verbatim instead of being summarized.
- [2026-10-19] Added a "Context editing and persistent state" section (WikiSkill/SKILL.state, ContextPilot, Google's trace → knowledge-store → skill ablation), moved from [Harness (agent)](harness.md).
- [2026-10-06] Added Cognition's Agent Memory Repo (git-and-markdown memory format, one sourced fact per line, `MEMORY.md` index) and Devin Dreaming (overnight prune-and-link pass).
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
- [AINews — OpenAI shuts off Cursor](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
- [AINews — Fal's H3 Max Live breaks the infinite videogen barrier](../sources/newsletters/ainews-fal-h3-max-live-2026-09-01.md)
- [Cognition — Agent Memory Repo](../sources/articles/cognition-agent-memory-repo-2026-10.md)
- [AINews — Devin Dreaming and Agent Memory Repo](../sources/newsletters/ainews-devin-dreaming-2026-10-06.md)
- [tamaratran/fast-jev-compaction (GitHub)](../sources/repos/tamaratran-fast-jev-compaction.md)
