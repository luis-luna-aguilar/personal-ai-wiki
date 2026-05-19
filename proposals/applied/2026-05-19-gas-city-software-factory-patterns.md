---
type: proposal
source: raw/newsletters/2026-05-19-inside-the-100-agent-software-factory.md
status: pending
created: 2026-05-19
---

# Proposal: Gas City — multi-agent software factory architecture patterns

## Summary

Gas City (GitHub: gastownhall/gascity) is the successor to Gas Town (Steve Yegge's viral post), rebuilt by Chris Sells (ex-Google Flutter) and Julian Knutsen (ex-Block). Currently running ~100 agents merging ~50 PRs/day and burning ~1B tokens/day. Every's Mike Taylor attended a hands-on workshop and extracted three architecture ideas worth capturing beyond the specific toolkit: (1) dark/light factory — background execution vs human-visible work; (2) one pet + many cattle — persistent named "mayor" agent coordinates disposable "polecat" workers; (3) multi-model code review — same code reviewed in parallel by Claude, Codex, and Kimi simultaneously. Verdict: "Learn from the ideas. Skip the toolkit for now."

## Intended changes

- [x] **Update** `wiki/concepts/harness.md` — add Gas City's three architecture patterns as concrete named primitives under `## What good harness engineering looks like`
    > See diff below

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add dark/light factory and mayor/polecats as named orchestration patterns
    > See diff below

- [x] **Create** `wiki/sources/newsletters/gas-city-software-factory-2026-05.md` — source summary

## Page drafts

### wiki/concepts/harness.md — additions to `## What good harness engineering looks like`

```md
- **Dark/light factory split.** Separate the parts of your workflow where humans and agents collaborate (planning, design, review) — the "light" side — from the parts where agents execute clearly defined work on their own in the background — the "dark" side. As trust in agent output increases, more work can migrate from light to dark. Gas City runs ~100 agents in the dark while the human interaction surface stays small and visible.
- **One pet, many cattle (mayor + polecats).** One persistent named supervisor agent ("mayor") you interact with directly coordinates anonymous disposable worker agents ("polecats") that each execute one job and shut down. Instead of managing 100 agents individually, you manage one conversation while the mayor routes work. Workers stay context-clean because they start fresh per task.
- **Multi-model parallel code review.** Submitting the same code to Claude, Codex, and Kimi simultaneously in parallel finds different bugs than running one model three times. Three different models with different training distributions catch issues each would miss alone. Higher signal per review cycle at the cost of higher parallel token spend.
```

### wiki/workflows/agentic-orchestration-patterns.md — additions

Read the current file first before editing. Add to the relevant section:

> The draft content below should be inserted into the existing page's patterns section — specific placement may need adjustment after reading the file.

```md
### Dark factory / light factory

Split agentic workflows into a **light** layer (planning, review, and human-agent interaction stay visible) and a **dark** layer (clearly defined execution runs in the background without human monitoring). As trust builds in the dark layer's output, more work moves out of the visible layer. Distinct from simple background execution: the light/dark split is a deliberate architectural boundary, not just async scheduling.

*Source: Gas City workshop, Every (2026-05-19)*

### Mayor + polecats (one pet + many cattle)

One persistent, named supervisor agent (the "mayor") that a human interacts with directly. The mayor routes work to many anonymous, disposable worker agents ("polecats") that each handle one scoped task and shut down. The human manages one conversation; the mayor manages coordination and worker lifecycle. Workers don't accumulate context or interfere with each other — fresh start per task.

*Source: Gas City workshop, Every (2026-05-19)*
```

### wiki/sources/newsletters/gas-city-software-factory-2026-05.md (new)

```md
---
title: "Inside the 100-agent Software Factory — Gas City"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-19-inside-the-100-agent-software-factory.md
url: https://every.to/context-window/inside-the-100-agent-software-factory
published: 2026-05-19
ingested: 2026-05-19
domains: [agents, coding]
---

# Inside the 100-agent Software Factory — Gas City

Every (Mike Taylor) attended a Gas City workshop and wrote a detailed Vibe Check. Gas City is the open-source successor to Gas Town (Steve Yegge), rebuilt by Chris Sells and Julian Knutsen. Currently ~100 agents, ~50 PRs/day, ~1B tokens/day. Three architecture ideas worth internalizing: dark/light factory, mayor/polecats, and multi-model parallel review. Verdict: sharp ideas, not yet practical for most teams.

## Influenced pages

- [Harness (concept)](../../concepts/harness.md) — dark/light factory, mayor/polecats, multi-model review as named primitives
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — two new named patterns

## Key claims extracted

- Gas City: ~100 agents, ~50 PRs/day, ~1B tokens/day; uses Beads task tracker (agent-first, CLI-only)
- Dark/light factory: visible human-agent collaboration (light) vs background agent execution (dark)
- Mayor + polecats: one persistent named supervisor routes work to anonymous disposable workers
- Multi-model review: Claude + Codex + Kimi in parallel on the same code diff
- Limitations: per-agent sessions don't share memory; six-step jobs cost ~6× one session; requires a day of setup with expert support
- Verdict (Mike Taylor): "Learn from the ideas. Skip the toolkit for now."
- OpenAI Symphony cited as a more accessible enterprise-ready alternative for the same orchestration need
```

## Open questions

- `wiki/workflows/agentic-orchestration-patterns.md` needs to be read before the exact insertion point is determined. The proposal shows the intended content; on apply, read the file first and insert at the appropriate section.
