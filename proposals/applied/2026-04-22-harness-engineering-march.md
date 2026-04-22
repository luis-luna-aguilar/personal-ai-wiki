---
type: proposal
sources:
  - raw/newsletters/2026-03-10-ainews-autoresearch-sparks-of-recursive-self-im.md
  - raw/newsletters/2026-03-12-ainews-replit-agent-4-the-knowledge-work-agent.md
  - raw/articles/2026-03-14-openaicom-indexharness-engineering.md
status: pending
created: 2026-04-22
---

# Proposal: Harness engineering as a systems problem

## Summary

The wiki already treats harness engineering as a real concept. This March cluster adds two concrete operational lessons that are still useful: first, long-running agents are constrained by loop controls and session ergonomics as much as by model quality; second, teams increasingly separate durable storage/context from isolated execution so multiple agents can collaborate safely through shared repos and filesystems.

This proposal strengthens the existing concept and workflow pages rather than creating a new one.

## Intended changes

- [x] **Update** `wiki/concepts/harness.md` — add earlier operational lessons on loop primitives and decoupled storage-vs-compute design
  > See diff snippet below.

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add explicit orchestration patterns for isolated execution with shared context and for long-running loop control
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/harness-engineering-march.md` — source summary page for this earlier harness cluster
  > See full draft below.

## Page drafts

### wiki/concepts/harness.md (updated snippet)

```markdown
## What a harness includes

- **Execution environment** — browser, terminal, code sandbox, API layers, memory systems
- **Storage / compute boundary** — many practical agent stacks now separate durable shared context (repos, filesystems, knowledge stores) from isolated execution sandboxes so multiple agents can collaborate without sharing one unsafe runtime

## What good harness engineering looks like

- **Robust loop primitives** give agents a clean way to keep going, pause, rewind, and resume without relying on awkward prompt hacks like reissuing "loop forever" in a brittle session
- **Decoupled shared context with isolated execution** lets teams of agents coordinate through the same source of truth while keeping actual runs sandboxed and failure-contained
```

### wiki/workflows/agentic-orchestration-patterns.md (updated snippet)

```markdown
## Current patterns

- **Scoped context, not global context.** Inject only the files, rules, or project context a sub-agent actually needs; keep the rest out of the loop to avoid context bleed.
- **Shared storage, isolated execution.** Let agents collaborate through the same repo, files, or knowledge store while keeping compute sandboxes separate; this preserves coordination without forcing one giant mutable runtime.
- **Failure-aware replanning.** Don't blindly retry. Feed structured failure metadata back into the orchestrator so it can generate a different plan.
- **Loop controls that are first-class.** Long-running agent work needs explicit pause, resume, rewind, and transparent-session controls rather than fragile prompt conventions.
```

### wiki/sources/newsletters/harness-engineering-march.md (new)

```markdown
---
title: Harness engineering in mid-March
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-10-ainews-autoresearch-sparks-of-recursive-self-im.md
published: 2026-03-10
ingested: 2026-04-22
domains: [coding, agents]
---

# Harness engineering in mid-March

This source summary groups a mid-March cluster on harness engineering before the idea became more mainstream in April. The shared takeaway is that reliable agents depend on systems design around the model: loop controls, eval craft, context structure, and safe separation between shared context and isolated execution.

## Influenced pages

- [[concepts/harness]] — adds concrete operational lessons on loop primitives and storage/compute separation
- [[workflows/agentic-orchestration-patterns]] — adds reusable patterns for isolated execution and long-running loop control

## Key claims extracted

- Long-running agent performance depends heavily on harness affordances such as looping, interruption, rewind, and transparent sessions
- Practical teams increasingly separate durable shared context from execution sandboxes so multiple agents can collaborate through repos or filesystems
- Eval design and harness iteration were already being framed as more important than raw model quality for reliable autonomous work
- OpenAI's first-party harness-engineering post reinforced that software leverage was moving into scaffolding, feedback loops, and control systems
```

## Open questions

- None.
