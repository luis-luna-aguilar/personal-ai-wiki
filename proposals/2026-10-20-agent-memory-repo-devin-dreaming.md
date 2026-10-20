---
type: proposal
source: raw/articles/2026-10-20-cognitioncom-agent-memory-repo.md
sources:
  - raw/articles/2026-10-20-cognitioncom-agent-memory-repo.md
  - raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Cognition's Agent Memory Repo and Devin "Dreaming"

## Summary

### In short
Agent memory is converging on plain git and markdown: Cognition stores a user's agent memory as a repo of one-line, source-linked facts under a `MEMORY.md` index, lets a swarm of agents share it through ordinary git merges, and runs an overnight "Dreaming" pass that prunes and links it. The proposal maps both terms in the knowledge-architectures hub to Agent memory (no new concept page), adds a status bullet there, a swarm-workspace pattern to Multi-agent coordination, a short memory note on Devin, and two source pages. One reason to hesitate: the spec page is a single worked example, so the format's rules are read off that example.

[[#Open questions|Open questions: 1 to answer.]]

### The source
In early October 2026 Cognition, the company behind the Devin coding agent, launched Devin "Dreaming", an overnight job that prunes and links Devin's memory graph, and said it is open-sourcing the storage format behind it as Agent Memory Repo. The AINews newsletter of 6 October carries the launch in one line; the format itself is published as a page at cognition.com.

The page explains the format through a story, not a specification. A user, John, has a checkout service where one request in a hundred takes 2.4 seconds. His agent starts four agents (database, runtime, cache, load balancer) and first creates a folder for the swarm inside John's memory repo, next to his existing notes. The folder holds a README with the goal and rules (measure only with one shared benchmark script so numbers compare; pull and read the shared files before each step; record what you rule out; ask the others when their area might explain what you see), a `findings.md`, a `questions.md`, and one notes file per agent. Every entry is one line ending in a link to the session that produced it, and files link to each other with wiki-style links.

After an hour each agent has one unexplained symptom. The questions file connects them: a price-cache refresh rebuilds a 2 GB table every ten seconds, which causes a 400 ms garbage-collection freeze, which makes queued requests exhaust a 20-connection database pool. Concurrency is handled by git itself: most commits merge, and when two agents edit the same line the second push is rejected and that agent re-reads both versions before writing. When the swarm ends, one line in `MEMORY.md` links its folder, so a later session about slow search reuses the benchmark and checks for freezes first.

### What changes
The wiki treats agent memory as a governed lifecycle (extract, dedupe, reconcile, expire) and already recommends provenance and human-inspectable structure, but it has no shipping product that does both, and "dreaming" appears only as a company-brain function name and as Anthropic's Managed Agents "Dreams" feature, never mapped in the hub.

- **Agent memory** gains one Current-status bullet on Agent Memory Repo and Devin Dreaming, a Recent-changes entry, and two sources. Page date moves to 6 October.
- **Knowledge architectures** adds Agent Memory Repo to the Agent memory row's examples and two term-map rows: "memory repo / Agent Memory Repo" and "dreaming", both mapped to Agent memory. Page date stays 19 October.
- **Multi-agent coordination** gains a "Memory repo as swarm workspace" pattern beside the Field Guide, contrasted with Cursor's failed shared-file locking. Page date moves to 6 October.
- **Devin** gains a short Memory subsection and a Recent-changes entry (10 entries, at the cap, no spill). Page date stays 19 October.
- Two new source pages: the spec page and the AINews launch story.

### What to weigh
The spec page carries no date, so the proposal dates everything to the 6 October newsletter that announced the launch. The hub mapping is a judgment call: the repo's `MEMORY.md` index and linked pages look like a knowledge layer, but agents write it from their own sessions with one sourced fact per line, so it goes on the Agent memory row with a note explaining why. The hub ends near 1,290 body words, about 107% of its ceiling, inside the warning band.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/agent-memory.md` — add one Current-status bullet; Current-status stamp and `as_of` move to 2026-10-06; adds one Recent-changes entry dated 2026-10-06 (live list has 4, no spill); append two source ids and two `## Sources` links
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — extend the Agent memory row's examples; add two term-map rows; adds one Recent-changes entry dated 2026-10-06 (live list has 5, no spill); append two source ids and links; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Update** `wiki/workflows/multi-agent-coordination.md` — add one bullet at the end of `### Coordination mechanics`; `as_of` moves to 2026-10-06; adds one Recent-changes entry dated 2026-10-06 (live list has 6, no spill); append one source id and link
    > See draft below

- [ ] **Update** `wiki/tools/devin.md` — add a `### Memory` subsection at the end of `## Current status`; adds one Recent-changes entry dated 2026-10-06 (live list has 9, becomes 10, no spill); append two source ids and links; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Create** `wiki/sources/articles/cognition-agent-memory-repo-2026-10.md` — source summary for the spec page

- [ ] **Create** `wiki/sources/newsletters/ainews-devin-dreaming-2026-10-06.md` — story-specific source summary for the Devin Dreaming launch line

## Page drafts

### wiki/concepts/agent-memory.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-06
sources: [agent-memory-without-vector-db, memory-vs-context-rot-february, agent-memory-systems-layer-2026-06, minteval-paper-2026-05, ainews-erdos-benchmarks-cluster-2026-05-21, ainews-openai-shuts-off-cursor-2026-08-29, ainews-fal-h3-max-live-2026-09-01, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06]
```

`## Current status` heading and new bullet, inserted after the Supermemory/Engram bullet:

```
## Current status (as of 2026-10-06)

- Cognition ships the lifecycle as a product and opens its format (October 2026). Agent Memory Repo stores one user's agent memory as a git repo of markdown files: a `MEMORY.md` entry point with an index, one fact per line, each ending in a link to the session that produced it, and wiki-style links between files. Devin "Dreaming" runs overnight to prune and link that memory graph. Together they put two of the practical implications below (provenance on every memory, structure a human can inspect and prune) into a shipping agent, and git gives shared writes for free (see the swarm-workspace pattern on [Multi-agent coordination](../workflows/multi-agent-coordination.md)).
```

`## Recent changes` — insert one entry directly below the 2026-10-19 entry:

```
- [2026-10-06] Added Cognition's Agent Memory Repo (git-and-markdown memory format, one sourced fact per line, `MEMORY.md` index) and Devin Dreaming (overnight prune-and-link pass).
```

`## Sources` — append:

```
- [Cognition — Agent Memory Repo](../sources/articles/cognition-agent-memory-repo-2026-10.md)
- [AINews — Devin Dreaming and Agent Memory Repo](../sources/newsletters/ainews-devin-dreaming-2026-10-06.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter `sources:` (append two ids; `as_of` unchanged):

```
sources: [knowledge-layer-architecture, llm-wikis-paperwiki-2026-07-06, agent-memory-systems-layer-2026-06, femke-plantinga-company-brains-2026-08-27, ontologies-agentic-systems-2026-07-30, dhravyashah-supermemory-company-brain-2026-07-28, posthog-semantic-layer-2026-08-21, deeplethe-utopia-2026-09-09, helixdb-helix-foundry-2026-10-19, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06]
```

`## Canonical pages` — Agent memory row, last cell changed:

```
| [Agent memory](agent-memory.md) | one agent, or one user's agents | episodic facts, preferences, and outcomes extracted from past sessions, managed as a lifecycle (extract, dedupe, reconcile, scope, expire) | the agent, under governed write rules | Supermemory, Engram, mem0, Letta, Cognition's Agent Memory Repo (no tool pages yet) |
```

`## Term map` — insert two rows after the "ghost memory" row:

```
| memory repo, Agent Memory Repo | Agent memory | Cognition's open git-and-markdown format for one user's agent memory. Its `MEMORY.md` index and linked pages look like a knowledge layer, but agents write it from their own sessions, one sourced fact per line, so it sits on the agent-memory row |
| dreaming, dreams | Agent memory (lifecycle step) | an offline pass that prunes, links, or rewrites stored memories between sessions, as in Cognition's Devin Dreaming and the Dreams feature of [Claude Managed Agents](../tools/claude-managed-agents.md). The [company brain](company-brain.md)'s "dreaming & pruning" function is the same step at organization scope. A step, not a store |
```

`## Recent changes` — insert one entry below the 2026-10-19 entry:

```
- [2026-10-06] Mapped "memory repo / Agent Memory Repo" and "dreaming / dreams" (Cognition's Devin Dreaming, Anthropic's Managed Agents Dreams) to Agent memory, and added Agent Memory Repo to that row's examples.
```

`## Sources` — append:

```
- [Cognition — Agent Memory Repo](../sources/articles/cognition-agent-memory-repo-2026-10.md)
- [AINews — Devin Dreaming and Agent Memory Repo](../sources/newsletters/ainews-devin-dreaming-2026-10-06.md)
```

### wiki/workflows/multi-agent-coordination.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-06
sources: [googlecloudtech-adk-2-orchestration-patterns, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, every-claude-dynamic-workflows-reliability-2026-06, dynamic-workflows-claude-code, cursor-agent-swarm-economics-2026-09-07, ainews-poolside-nvidia-2026-08-21, mahax-graph-engineering-2026-07-29, cognition-agent-memory-repo-2026-10]
```

`### Coordination mechanics` — append after the Field Guide bullet:

```
- **Memory repo as swarm workspace.** Cognition's Agent Memory Repo gives a swarm its own folder inside the user's git-backed [agent memory](../concepts/agent-memory.md): a README with the goal and the rules (measure only with one shared benchmark script so numbers compare, pull and read the shared files before each step, record what was ruled out, ask when another agent's area might explain what you see), a shared `findings.md`, a `questions.md` where agents ask each other, and one notes file per agent. In the worked example four agents chasing a p99 latency spike each saw one unexplained symptom; the cause (a cache refresh triggering garbage-collection freezes that exhausted the database pool) appeared only when the questions file connected them. Git is the concurrency control: most commits merge, and when two agents edit the same line the second push is rejected and that agent re-reads both versions before writing. When the swarm ends, one index line in `MEMORY.md` links its folder, so later sessions reuse its benchmark and its lessons. This is the Field Guide's stigmergy made durable across sessions, and it differs from the shared-file locking that failed in Cursor's first swarm ([Long-running agent swarms](long-running-agent-swarms.md)) by letting writes collide and resolving them at push time instead of holding locks. *Source: Cognition, Agent Memory Repo (October 2026)*
```

`## Recent changes` — insert one entry directly below the 2026-10-19 entry:

```
- [2026-10-06] Added the memory-repo swarm-workspace pattern (shared findings and questions files in a git-backed memory repo, conflicts resolved at push time) from Cognition's Agent Memory Repo.
```

`## Sources` — append:

```
- [Cognition — Agent Memory Repo](../sources/articles/cognition-agent-memory-repo-2026-10.md)
```

### wiki/tools/devin.md (updated)

Frontmatter `sources:` (append two ids; `as_of` unchanged):

```
sources: [devin-auto-triage-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, cognitioncom-blog-ai-productivity, the-code-spacexai-drops-grok-45-2026-07-09, ainews-devin-fusion-router-moat-2026-07-14, cognition-devin-outposts-2026-07-21, devinai-blog-introducing-devin-oncall, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06]
```

New subsection at the end of `## Current status`, after `### Devin Outposts`:

```
### Memory

- **Devin Dreaming (October 2026):** an overnight pass that prunes and links Devin's memory graph. Cognition is open-sourcing the storage format as Agent Memory Repo: a git repo of markdown files with a `MEMORY.md` index and one source-linked fact per line, which several agents can write at once through ordinary git merges (see [Agent memory](../concepts/agent-memory.md)).
```

`## Recent changes` — insert one entry below the 2026-10-19 entry (list becomes 10, at the cap, no spill):

```
- [2026-10-06] Devin Dreaming (overnight memory prune-and-link) launched; storage format open-sourced as Agent Memory Repo.
```

`## Sources` — append:

```
- [Cognition — Agent Memory Repo](../sources/articles/cognition-agent-memory-repo-2026-10.md)
- [AINews — Devin Dreaming and Agent Memory Repo](../sources/newsletters/ainews-devin-dreaming-2026-10-06.md)
```

### wiki/sources/articles/cognition-agent-memory-repo-2026-10.md (new)

```
---
title: Cognition — Agent Memory Repo
type: source
source_type: article
source_file: raw/articles/2026-10-20-cognitioncom-agent-memory-repo.md
url: https://cognition.com/agent-memory-repo
ingested: 2026-10-20
domains: [agents]
---

# Cognition — Agent Memory Repo

Cognition's page for Agent Memory Repo, the open git-and-markdown format behind Devin's memory. The page carries no date; AINews reported the launch on 6 October 2026. It explains the format through one worked example: four agents investigating why 1 checkout request in 100 takes 2.4 s share a swarm folder inside the user's memory repo (README with goal and rules, `findings.md`, `questions.md`, one notes file per agent, one shared benchmark script). Each finding is one line with a link to the session that produced it. The shared questions file connects three separate symptoms into one cause, git handles concurrent writes, and the finished swarm folder is linked from `MEMORY.md` for later sessions to reuse.

## Influenced pages

- [Agent memory](../../concepts/agent-memory.md) — new Current-status bullet
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — "memory repo" term-map row; Agent memory row example
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — memory-repo swarm-workspace pattern
- [Devin](../../tools/devin.md) — Memory subsection

## Key claims extracted

- Memory repo layout: `MEMORY.md` with an `## Index`, topic files (team structure, projects), and a `swarms/` folder with one subfolder per swarm
- Swarm folder: `README.md` (goal and rules), `findings.md`, `questions.md`, `agents/<name>.md` per agent, `scripts/bench.sh` as the one shared benchmark
- Rules in the example README: measure only with the shared script; pull and read findings and questions before each step; record what you rule out; ask when another agent's area might explain what you see
- Every entry is one line ending in `[source: <session link>]`; files cross-link with `[[...]]` links
- Worked example: price-cache refresh rebuilds a ~2 GB table every 10 s → ~400 ms GC freeze → queued requests exhaust a 20-connection pool; fix (refresh only changed prices) takes the slowest 1% from 2.4 s to 310 ms
- Git merges most concurrent commits; when two agents edit the same line the second push is rejected and that agent reads both versions before writing
- The finished swarm folder stays in the repo and is indexed in `MEMORY.md`; later sessions follow the link and reuse the benchmark
```

### wiki/sources/newsletters/ainews-devin-dreaming-2026-10-06.md (new)

```
---
title: AINews — Devin Dreaming and Agent Memory Repo
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
published: 2026-10-06
ingested: 2026-10-20
domains: [agents]
---

# AINews — Devin Dreaming and Agent Memory Repo

One story from the 6 October 2026 AINews issue ("Reflection Beam"): Cognition launched Devin "Dreaming", which prunes and links a memory graph overnight, and is open-sourcing the git- and markdown-backed format behind it as Agent Memory Repo.

## Influenced pages

- [Agent memory](../../concepts/agent-memory.md) — launch date and Dreaming description
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — "dreaming" term-map row
- [Devin](../../tools/devin.md) — Memory subsection and Recent-changes entry

## Key claims extracted

- Devin Dreaming prunes and links a memory graph overnight
- Cognition is open-sourcing the git- and markdown-backed memory format as Agent Memory Repo
```

## Open questions

- Should Agent Memory Repo eventually get a `tools/` page, or stay as an example on Agent memory until a second source describes the format's rules beyond the worked example (assumed: stay as an example)?
