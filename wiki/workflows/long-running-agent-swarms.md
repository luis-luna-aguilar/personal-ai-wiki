---
title: Long-running agent swarms
type: workflow
domains: [agents, coding]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-09-09
sources: [cursor-self-driving-codebases-2026-09-09, cursor-agent-swarm-economics-2026-09-07]
---

# Long-running agent swarms

Case-study lessons from running hundreds of coding agents together for days without human intervention, drawn from Cursor's two published swarm generations: a first-generation harness that built a web browser (peaking at ~1,000 commits/hour across 10M tool calls in one week) and a second-generation swarm that built SQLite from scratch in Rust from only its manual. The general topology and routing patterns these swarms instantiate live on [Multi-agent coordination](multi-agent-coordination.md); this page keeps the swarm-specific topology evolution, failure modes, and operating principles.

## Topology

- **Recursive planner/subplanner/worker topology.** Cursor's first-generation browser-building harness converged on three fixed roles after cycling through self-coordination (shared-file locking — failed: agents held locks too long, 20 agents throttled to 1-3x throughput), a planner/executor/judge split (bottlenecked on the slowest worker, too rigid for mid-run replanning), and a continuous executor (overloaded with too many simultaneous responsibilities — plan, explore, spawn, review, merge, judge — causing random idling and premature completion claims). The final design: a root planner owns the whole task and does no coding itself; when its scope is subdividable it spawns subplanners that fully own a narrower slice (recursive); workers pick up leaf tasks, work in isolated repo copies unaware of the larger system, and report back a single handoff (what was done, concerns, deviations, findings) that keeps the requesting planner in continuous motion even after it judges itself "done." An integrator role added for central merge/quality control was later removed once workers proved capable of handling conflicts themselves — a single global gate became the throughput bottleneck at scale. Peaked at ~1,000 commits/hour across 10M tool calls over one week with no human intervention. *Source: Cursor, "Towards self-driving codebases"*

## Coordination failure modes and fixes

- **Five coordination failure modes and fixes.** The second-generation planner/worker agent swarm (Cursor, building SQLite from scratch in Rust from only its manual) documents five specific multi-agent coordination failures and their fixes: **split-brain design** (two planners independently duplicate the same design decision — fixed by having planners commit to decisions themselves, with a rule that no two subtrees may decide the same question); **planner contention** (planners aware of each other fight through repeated edits over the same files — fixed via shared, compile-checked design docs that a reconciler agent merges on conflict); **merge conflicts** (worker agents are bad at resolving their own collisions — fixed by a neutral third-party agent that resolves conflicts on behalf of both sides); **"megafiles"** (popular files grow unmanageably large and collision-prone — fixed by flagging and auto-decomposing them); and **"ossification"** (agents learn, from working alongside humans, not to touch core code even when it needs to change — fixed by licensing intentional breakage, with the compiler propagating the resulting failures to every dependent agent). The new harness beat the old one in every tested model mix: 73-85% of a held-out test suite in 4 hours vs. the old swarm's 11-77%, with >98% fewer merge conflicts and 3-7x smaller final code for equal or better quality. A purpose-built version-control system replaced Git for this generation of the swarm — since every change routes through it, it's also where the coordination mechanisms above are implemented — and raised throughput from the first-generation harness's ~1,000 commits/hour peak to ~1,000 commits/second. The underlying reason the planner/worker split scales, per Cursor: a planner never implements so its context never fills with low-level detail, and a worker never plans so it can spend its entire context on one narrow piece — an echo of economist Ronald Coase's observation (in "The Nature of the Firm") that coordination costs grow faster than the work itself, which is why organizations settle into bounded tiers rather than everyone talking to everyone. The solo Opus 4.8 run's output codebase is public: [github.com/cursor/minisqlite](https://github.com/cursor/minisqlite).

## Keeping long runs on track

- **Freshness mechanisms for long-running agents.** To stop agents drifting over multi-day runs, Cursor's browser harness: rewrites (not appends to) a shared `scratchpad.md` file each cycle; has individual agents self-summarize on hitting context limits; adds explicit self-reflection/alignment reminders to system prompts; and explicitly encourages agents to pivot and challenge their own prior assumptions rather than defend them. *Source: Cursor, "Towards self-driving codebases"*
- **Constraints over instructions, concrete ranges over vague scope.** Two prompting lessons from running a harness at extreme scale: (1) only instruct on what the model doesn't already know — multi-agent collaboration mechanics, project-specific deploy/test process — and treat the model like "a brilliant new hire who knows engineering but not your codebase"; negative constraints ("no TODOs, no partial implementations") outperform positive reminders ("remember to finish implementations") because they define a boundary rather than competing for attention with the rest of the task. (2) Vague quantity language collapses to a conservative default — "generate many tasks" produces a small, safe number — while concrete ranges ("generate 20-100 tasks") reliably convey that ambitious, wide-scope output is wanted. *Source: Cursor, "Towards self-driving codebases"*

## Design principles

- **Accept a steady error rate over enforcing per-commit correctness.** Requiring 100% correctness before every single commit caused major serialization: a single small error (an API typo) would halt the whole system, and multiple workers would pile onto the same fix and trample each other. Allowing a small, stable, non-worsening error rate — on the trust that other agents will fix issues they encounter — kept throughput high; the tradeoff is a final "green branch" reconciliation pass before release. The same acceptance applies to merge/sync overhead: rather than architecting collisions away, let the system absorb some turbulence and converge naturally, which stays simpler to align, observe, and manage than a conflict-proof design would be. Named design principles: anti-fragile (expect and absorb individual-agent failure as scale increases probability of it), empirical over assumption-driven (adjust from observed data, not analogies to human orgs or classical distributed-systems designs), and design-for-throughput-explicitly (a stated tradeoff, not an accident). *Source: Cursor, "Towards self-driving codebases"*

## Recent changes

- [2026-10-19] Page created, split out of [Multi-agent coordination](multi-agent-coordination.md)'s "Coordination mechanics and case studies" section, which keeps the general patterns (Agentic MapReduce, sidekick harness, scripted subagent orchestration, Field Guide).
- [2026-09-09] Added Cursor's harness-evolution lessons from its predecessor browser-building research (recursive planner/subplanner/worker topology, freshness mechanisms, constraints-over-instructions and concrete-range prompting, and accept-a-steady-error-rate design principles), and extended the swarm-coordination-failures pattern with the new-VCS throughput jump (1,000 commits/hour → 1,000 commits/second) and the context-efficiency/Coase explanation for why the planner/worker split scales.
- [2026-09-07] Added Cursor's agent-swarm coordination failure modes (split-brain, planner contention, merge conflicts, megafiles, ossification) and fixes.

## Related

- [Multi-agent coordination](multi-agent-coordination.md) — general topology, routing, and coordination patterns, including the Field Guide self-authored context from the same SQLite swarm
- [Agentic orchestration patterns](agentic-orchestration-patterns.md) — review lenses and evaluator separation from the same Cursor sources
- [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) — the SQLite swarm's model-mix cost comparison
- [Cursor](../tools/cursor.md) — the company behind both swarms

## Sources

- [Cursor — Towards self-driving codebases](../sources/articles/cursor-self-driving-codebases-2026-09-09.md)
- [Cursor — Agent swarms and the new model economics](../sources/articles/cursor-agent-swarm-economics-2026-09-07.md)
