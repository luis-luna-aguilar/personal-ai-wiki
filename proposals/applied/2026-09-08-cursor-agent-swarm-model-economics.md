---
type: proposal
source: raw/articles/2026-09-07-cursorcom-blog-agent-swarm-model-economics.md
status: pending
created: 2026-09-08
---

# Proposal: Cursor's "Agent swarms and the new model economics"

## Summary

### The source

Cursor's own engineering blog details a second-generation "agent swarm" — planner agents that decompose a goal into a tree and delegate, worker agents that execute leaves without holding the wider goal in context — tasked with implementing all 835 pages of the SQLite manual in Rust from scratch, with no source code, test suite, or internet access withheld from it, then graded against SQLite's own `sqllogictest` suite (which the swarm was never told existed). The new harness beat the prior generation's swarm in every one of four model-mix configurations tested, reaching 73-85% of the suite within a four-hour budget versus the old swarm's 11-77%, while cutting merge conflicts by more than 98% (fewer than 1,000 vs. over 70,000) and final code size by 3-7x for equivalent or better test scores. The post names five specific multi-agent coordination failure modes it hit and fixed: split-brain design (two planners independently solving the same design question — fixed by having planners make and record decisions themselves, with a rule that no two subtrees may decide the same question); planner contention (two planners aware of each other fighting through repeated edits — fixed by requiring shared, compile-checked design docs that a reconciler agent merges when they conflict); merge conflicts (worker agents are bad at resolving collisions themselves — fixed by a neutral third-party agent that resolves conflicts on behalf of both parties); "megafiles" (popular files become unmanageably large and collision-prone — fixed by flagging and auto-decomposing them); and "ossification" (agents learn from working alongside humans not to touch core code, even when it needs to change — fixed by licensing intentional breakage, with the compiler propagating the resulting failures to every dependent agent). The post also describes "Field Guide," a self-authored, agent-owned shared-context folder automatically injected into every new agent, and a "review lenses" practice — stacking multiple imperfect reviewers (different context slices, different models) rather than relying on one. Cost data: the same task, at similar final quality, cost $1,339 using an Opus 4.8 planner with Composer 2.5 workers, versus $10,565 using GPT-5.5 for both roles — workers carried 69-90%+ of total tokens across every configuration, but planner tokens cost disproportionately more per token.

### What changes

This is a rare, detailed primary-source account of production multi-agent orchestration at scale, and it maps cleanly onto two existing wiki pages. `workflows/agentic-orchestration-patterns.md` gains a new pattern entry naming the five coordination failure modes and their fixes, plus the Field Guide and review-lenses patterns; its 10-entry Recent-changes cap is already full, so this spills its oldest entry. `training/cost-aware-ai-task-routing.md` gains a new "Evidence from practice" bullet with the concrete $1,339-vs-$10,565 same-task cost comparison; that page has no Recent-changes section (consistent with several other training pages), so this proposal only bumps its `as_of`.

### What to weigh

The source article carries no explicit publication date of its own (no dateline visible in the fetched content), so this proposal uses the ingestion date (2026-09-07) as `as_of` per the wiki's date-fallback rule, rather than guessing a launch date from context clues in the post's "earlier this year" phrasing.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add agent-swarm coordination failure-modes pattern, Field Guide, and review-lenses patterns, bump `as_of`, add Recent-changes entry, spill oldest entry
    > See draft below

- [ ] **Spill** `wiki/workflows/agentic-orchestration-patterns.md` → `wiki/history/workflows/agentic-orchestration-patterns.md` — oldest Recent-changes entry falls off the 10-entry cap
    > See draft below

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add Evidence-from-practice bullet with the $1,339 vs. $10,565 cost comparison, bump `as_of`
    > See draft below

- [ ] **Create** `wiki/sources/articles/cursor-agent-swarm-economics-2026-09-07.md` — source summary

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (updated)

```md
---
as_of: 2026-09-07
sources: [..., cursor-agent-swarm-economics-2026-09-07]
---

## Current patterns

(... existing bullets unchanged ...)

- **Agent-swarm coordination failure modes and fixes.** A second-generation planner/worker agent swarm (Cursor, building SQLite from scratch in Rust from only its manual) documents five specific multi-agent coordination failures and their fixes: **split-brain design** (two planners independently duplicate the same design decision — fixed by having planners commit to decisions themselves, with a rule that no two subtrees may decide the same question); **planner contention** (planners aware of each other fight through repeated edits over the same files — fixed via shared, compile-checked design docs that a reconciler agent merges on conflict); **merge conflicts** (worker agents are bad at resolving their own collisions — fixed by a neutral third-party agent that resolves conflicts on behalf of both sides); **"megafiles"** (popular files grow unmanageably large and collision-prone — fixed by flagging and auto-decomposing them); and **"ossification"** (agents learn, from working alongside humans, not to touch core code even when it needs to change — fixed by licensing intentional breakage, with the compiler propagating the resulting failures to every dependent agent). The new harness beat the old one in every tested model mix: 73-85% of a held-out test suite in 4 hours vs. the old swarm's 11-77%, with >98% fewer merge conflicts and 3-7x smaller final code for equal or better quality.
- **Field Guide: self-authored shared context.** A folder owned entirely by the agents themselves, whose index file is automatically injected into every new agent at start; agents alone decide what goes in it, under a line-budget constraint. Modeled on stigmergy (how ants/termites coordinate by modifying their shared environment rather than communicating directly) — since model weights are frozen, capturing genuine surprises for the next agent's trajectory is the mechanism's whole value.
- **Review lenses.** No single review lens catches everything; stacking several imperfect, decorrelated reviewers (full transcript vs. output-only vs. codebase-only; different underlying models) compounds toward much higher reliability than one "best" reviewer, the way self-driving systems exceed human reliability without any single perfect sensor.

## Recent changes

- [2026-09-07] Added Cursor's agent-swarm coordination failure modes (split-brain, planner contention, merge conflicts, megafiles, ossification) and fixes, the Field Guide self-authored-context pattern, and the review-lenses pattern.
- (... existing entries follow, oldest entry spilled below ...)
```

### wiki/history/workflows/agentic-orchestration-patterns.md (updated)

```md
## Archived from current page on 2026-09-08

- [2026-06-18] Every case studies add scripted-subagent orchestration as a practical Dynamic Workflows reliability pattern.
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

```md
---
as_of: 2026-09-07
sources: [..., cursor-agent-swarm-economics-2026-09-07]
---

## Evidence from practice

(... existing bullets unchanged ...)

- **Cursor's agent-swarm planner-cost comparison.** Running an identical multi-agent build task (implementing SQLite from scratch in Rust) across four model mixes at similar final quality, Cursor found dramatic cost variance driven by planner choice: $1,339 with an Opus 4.8 planner + Composer 2.5 workers, versus $10,565 with GPT-5.5 for both roles. Workers carried 69-90%+ of total tokens in every configuration, but planner tokens cost disproportionately more per token — reinforcing that routing the planning/decomposition role to a cost-efficient-but-capable model, while keeping workers cheap, matters more than optimizing worker-model cost alone.
```

### wiki/sources/articles/cursor-agent-swarm-economics-2026-09-07.md (new)

```md
---
title: "Agent swarms and the new model economics"
type: source
source_type: article
source_file: raw/articles/2026-09-07-cursorcom-blog-agent-swarm-model-economics.md
url: https://cursor.com/blog/agent-swarm-model-economics
ingested: 2026-09-08
domains: [agents, coding]
---

# Agent swarms and the new model economics

Cursor's engineering blog details its second-generation agent swarm (planner/worker tree topology) building SQLite from scratch in Rust, documenting five multi-agent coordination failure modes and fixes, a self-authored "Field Guide" context mechanism, stacked "review lenses," and cost data across four model-mix configurations.

## Influenced pages

- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — coordination failure-modes pattern, Field Guide, review lenses
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — $1,339 vs. $10,565 same-task cost comparison

## Key claims extracted

- New swarm harness beat the old one in every model mix: 73-85% of held-out test suite in 4 hours vs. 11-77%
- >98% fewer merge conflicts (under 1,000 vs. over 70,000); 3-7x smaller final code for equal/better quality
- 5 named failure modes with fixes: split-brain design, planner contention, merge conflicts, megafiles, ossification
- Field Guide: self-authored, agent-owned shared context folder, line-budget constrained
- Review lenses: stacking multiple imperfect/decorrelated reviewers beats one "best" reviewer
- Cost: $1,339 (Opus 4.8 planner + Composer 2.5 workers) vs. $10,565 (GPT-5.5 solo) for the same task
```
