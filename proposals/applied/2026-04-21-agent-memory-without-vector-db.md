---
type: proposal
sources:
  - raw/newsletters/2026-03-23-supermemory-cracks-agent-memory.md
status: pending
created: 2026-04-21
---

# Proposal: Agent memory without vector databases

## Summary

The wiki currently talks about knowledge layers and memory as part of harness design, but it does not yet have a dedicated page for long-term agent memory itself. This source is worth promotion because it captures a concrete architectural claim: reliable long-term memory may come less from embedding retrieval and more from active reading, analysis, and fact extraction over conversation history.

## Intended changes

- [x] **Create** `wiki/concepts/agent-memory.md` — new concept page for long-term memory architectures in agents
  > See full draft below.

- [x] **Create** `wiki/sources/newsletters/agent-memory-without-vector-db.md` — source summary page
  > See full draft below.

## Page drafts

### wiki/concepts/agent-memory.md (new)

```markdown
---
title: Agent memory
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-03-23
sources: [agent-memory-without-vector-db]
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

## Caveats

- The current source set is centered on one startup's claims and a benchmark delta reported through newsletter coverage
- This should be read as an architectural signal worth watching, not as proof that vector retrieval is obsolete in every setting

## Sources

- [[sources/newsletters/agent-memory-without-vector-db]]
```

### wiki/sources/newsletters/agent-memory-without-vector-db.md (new)

```markdown
---
title: Agent memory without vector databases
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-23-supermemory-cracks-agent-memory.md
ingested: 2026-04-21
domains: [agents]
---

# Agent memory without vector databases

This source is useful because it turns "memory" from a vague agent feature into a concrete architectural question. The core claim is that better long-term memory can come from agents that actively read and analyze history, rather than relying on embedding similarity as the main retrieval mechanism.

## Influenced pages

- [[concepts/agent-memory]] — opens a dedicated page for long-term memory architectures in agents

## Key claims extracted

- Supermemory's ASMR stands for Agentic Search and Memory Retrieval
- The system is described as replacing vector search with specialized agents that read history, analyze it, and extract facts
- Reported benchmark improvement: LongMemEval from about 85% to 98.6%
- The broader implication is that memory quality may be more about interpretation and fact extraction than about the storage backend alone
```
