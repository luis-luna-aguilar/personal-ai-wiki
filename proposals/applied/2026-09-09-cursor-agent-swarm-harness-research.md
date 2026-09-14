---
type: proposal
source: raw/articles/2026-09-09-cursorcom-blog-self-driving-codebases.md
status: pending
created: 2026-09-09
---

# Proposal: Cursor's agent-swarm harness research (self-driving codebases + swarm-economics enrichment + a Codex orchestration example)

## Summary

### The source

Cursor has spent much of 2026 running a long-horizon research project — build a web browser from scratch using swarms of autonomous coding agents — and has now published two engineering posts describing what they learned. "Towards self-driving codebases" is the earlier of the two: it traces the harness's evolution from a flat, self-coordinating swarm (agents sharing a lock file — failed, because locks got held too long and 20 agents throttled to the throughput of 2-3) through a planner/executor/judge split (bottlenecked on the slowest worker) to the final design — a recursive planner/subplanner/worker topology where a root planner never codes, can spawn subplanners that fully own a narrower slice, and disposable workers grind on isolated leaf tasks and report back a single handoff. That system peaked at roughly 1,000 commits/hour across 10 million tool calls over one continuous week with no human intervention. The post has no visible publish date and references Opus 4.5 and GPT-5.1/5.2 as its working models — both several generations behind the wiki's current frontier — and the newer post explicitly calls it "an earlier post," so it clearly predates this September by a meaningful stretch, likely months. A freshly re-read copy of that newer post, "Agent swarms and the new model economics" (already in the wiki, ingested 2026-09-08), turned up a few concrete numbers the original ingest missed: the new generation of the swarm replaced Git with a purpose-built version-control system, lifting peak throughput from that ~1,000-commits/hour predecessor to roughly 1,000 commits *per second*, and Cursor explains the planner/worker split's scaling property in economic terms — a planner never fills its context with implementation detail and a worker never fills its with planning, echoing Ronald Coase's observation that coordination costs grow faster than the work itself. Rounding out the batch is a small, well-documented community project: `donvito/codex-astra-luna-orchestrator`, a GitHub repo that configures OpenAI's Codex CLI so GPT-6 Astra plans and reviews while GPT-5.6 Luna executes across explorer/worker/tester/researcher roles — and keeps the reviewer pinned to Astra even on the cheaper "Plus" plan, so the model reviewing code is never the model that wrote it.

### What changes

The wiki currently documents only the *later* stage of Cursor's swarm research (the SQLite/model-economics post) on the orchestration-patterns workflow page and the cost-routing training page; the earlier harness-design story behind it was untracked, and a few numbers from the later post's own re-read were never captured the first time.

- **Agentic orchestration patterns** gains four new pattern entries describing the harness's design evolution — the recursive planner/subplanner/worker topology, freshness mechanisms for multi-day runs (rewritten scratchpads, self-summarization, self-reflection reminders), two prompting lessons (constraints beat instructions, concrete ranges beat vague scope words), and the "accept a steady error rate" tradeoff behind three named design principles (anti-fragile, empirical-over-assumption, design-for-throughput). The existing swarm-coordination-failures entry is extended with the new-VCS throughput jump and the Coase-style explanation for why the split scales, plus a link to the now-public `minisqlite` codebase. The existing evaluator-separation entry gains the donvito Codex example as a concrete illustration. The page's Recent-changes list is at its 10-entry cap, so the oldest entry (the 2026-06-29 Sidekick multi-model harness note) spills to history.
- **Cursor** (the tool page) gains one Recent-changes line noting the harness research and that part of it is now being made available to some users; its Recent-changes list is also at cap, so its oldest entry (2026-04-22, Truell's "third era" data) spills to history.
- The existing source page for the model-economics post gains three new Key Claims (the VCS throughput jump, the public `minisqlite` link, the Coase framing) — no second source page is created for that URL.
- One new source page is created for "Towards self-driving codebases," explicitly noting its date is unconfirmed and assigned by ingest-date fallback.

### What to weigh

The self-driving-codebases post carries no visible publish date, and internal evidence (the model generations it names) suggests it's actually several months old rather than fresh September news; it's dated 2026-09-09 by the wiki's ingest-date fallback rule, and that's flagged both in the new source page and here so the reviewer can judge whether that's the right call. Separately, the donvito repo is a solid, specific illustration of a pattern the wiki already documents in the abstract, but it has no adoption metrics (stars, users) the way comparable community-tool pages (gstack, paperclip) do — it's folded into the workflow page as a pattern example rather than given its own tool page; see Open Questions if a dedicated page is wanted instead.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add 4 new pattern bullets, extend 2 existing bullets, add 1 Recent-changes entry, bump `as_of` to 2026-09-09, add source id
    > See draft below

- [ ] **Spill** `wiki/workflows/agentic-orchestration-patterns.md` → `wiki/history/workflows/agentic-orchestration-patterns.md` — oldest Recent-changes entry (2026-06-29, Sidekick multi-model harness) falls off the 10-entry cap
    > See draft below

- [ ] **Update** `wiki/tools/cursor.md` — add 1 Recent-changes entry, bump `as_of` to 2026-09-09, add source id
    > See draft below

- [ ] **Spill** `wiki/tools/cursor.md` → `wiki/history/tools/cursor.md` — oldest Recent-changes entry (2026-04-22, Truell's third-era data) falls off the 10-entry cap
    > See draft below

- [ ] **Update** `wiki/sources/articles/cursor-agent-swarm-economics-2026-09-07.md` — append 3 new Key Claims from a closer re-read
    > See draft below

- [ ] **Create** `wiki/sources/articles/cursor-self-driving-codebases-2026-09-09.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Frontmatter: bump `as_of: 2026-09-07` → `as_of: 2026-09-09`; append `cursor-self-driving-codebases-2026-09-09` to the `sources:` list.

Insert these 4 new bullets into `## Current patterns`, directly before the existing "**Agent-swarm coordination failure modes and fixes.**" bullet (so the harness-evolution arc reads as context leading into it):

```
- **Recursive planner/subplanner/worker topology.** Cursor's browser-building harness (predecessor to the SQLite swarm below) converged on three fixed roles after cycling through self-coordination (shared-file locking — failed: agents held locks too long, 20 agents throttled to 1-3x throughput), a planner/executor/judge split (bottlenecked on the slowest worker, too rigid for mid-run replanning), and a continuous executor (overloaded with too many simultaneous responsibilities — plan, explore, spawn, review, merge, judge — causing random idling and premature completion claims). The final design: a root planner owns the whole task and does no coding itself; when its scope is subdividable it spawns subplanners that fully own a narrower slice (recursive); workers pick up leaf tasks, work in isolated repo copies unaware of the larger system, and report back a single handoff (what was done, concerns, deviations, findings) that keeps the requesting planner in continuous motion even after it judges itself "done." An integrator role added for central merge/quality control was later removed once workers proved capable of handling conflicts themselves — a single global gate became the throughput bottleneck at scale. Peaked at ~1,000 commits/hour across 10M tool calls over one week with no human intervention. *Source: Cursor, "Towards self-driving codebases"*
- **Freshness mechanisms for long-running agents.** To stop agents drifting over multi-day runs, Cursor's browser harness: rewrites (not appends to) a shared `scratchpad.md` file each cycle; has individual agents self-summarize on hitting context limits; adds explicit self-reflection/alignment reminders to system prompts; and explicitly encourages agents to pivot and challenge their own prior assumptions rather than defend them. *Source: Cursor, "Towards self-driving codebases"*
- **Constraints over instructions, concrete ranges over vague scope.** Two prompting lessons from running a harness at extreme scale: (1) only instruct on what the model doesn't already know — multi-agent collaboration mechanics, project-specific deploy/test process — and treat the model like "a brilliant new hire who knows engineering but not your codebase"; negative constraints ("no TODOs, no partial implementations") outperform positive reminders ("remember to finish implementations") because they define a boundary rather than competing for attention with the rest of the task. (2) Vague quantity language collapses to a conservative default — "generate many tasks" produces a small, safe number — while concrete ranges ("generate 20-100 tasks") reliably convey that ambitious, wide-scope output is wanted. *Source: Cursor, "Towards self-driving codebases"*
- **Accept a steady error rate over enforcing per-commit correctness.** Requiring 100% correctness before every single commit caused major serialization: a single small error (an API typo) would halt the whole system, and multiple workers would pile onto the same fix and trample each other. Allowing a small, stable, non-worsening error rate — on the trust that other agents will fix issues they encounter — kept throughput high; the tradeoff is a final "green branch" reconciliation pass before release. The same acceptance applies to merge/sync overhead: rather than architecting collisions away, let the system absorb some turbulence and converge naturally, which stays simpler to align, observe, and manage than a conflict-proof design would be. Named design principles: anti-fragile (expect and absorb individual-agent failure as scale increases probability of it), empirical over assumption-driven (adjust from observed data, not analogies to human orgs or classical distributed-systems designs), and design-for-throughput-explicitly (a stated tradeoff, not an accident). *Source: Cursor, "Towards self-driving codebases"*
```

Extend the existing "**Agent-swarm coordination failure modes and fixes.**" bullet by appending this sentence to its end (after "...3-7x smaller final code for equal or better quality."):

```
A purpose-built version-control system replaced Git for this generation of the swarm — since every change routes through it, it's also where the coordination mechanisms above are implemented — and raised throughput from the harness-evolution predecessor's ~1,000 commits/hour peak to ~1,000 commits/second. The underlying reason the planner/worker split scales, per Cursor: a planner never implements so its context never fills with low-level detail, and a worker never plans so it can spend its entire context on one narrow piece — an echo of economist Ronald Coase's observation (in "The Nature of the Firm") that coordination costs grow faster than the work itself, which is why organizations settle into bounded tiers rather than everyone talking to everyone. The solo Opus 4.8 run's output codebase is public: [github.com/cursor/minisqlite](https://github.com/cursor/minisqlite).
```

Extend the existing "**Evaluator separation.**" bullet by appending this sentence to its end:

```
A community-built example for OpenAI's Codex CLI ([donvito/codex-astra-luna-orchestrator](https://github.com/donvito/codex-astra-luna-orchestrator/)) pins this at the config level: GPT-6 Astra plans/orchestrates and reviews, while GPT-5.6 Luna executes across explorer/worker/tester/researcher subagent roles — critically, the reviewer role stays pinned to Astra even on the cheaper "Plus" plan variant (where Luna at max reasoning takes over the orchestrator role too), so the model that reviews code is never the same model that wrote it, on either tier.
```

Add to `## Recent changes` (as the newest entry, at the top of the list):

```
- [2026-09-09] Added Cursor's harness-evolution lessons from its predecessor browser-building research (recursive planner/subplanner/worker topology, freshness mechanisms, constraints-over-instructions and concrete-range prompting, and accept-a-steady-error-rate design principles), extended the swarm-economics entry with the new-VCS throughput jump (1,000 commits/hour → 1,000 commits/second) and the context-efficiency/Coase explanation for why the planner/worker split scales, and extended evaluator separation with a community Codex config (donvito/codex-astra-luna-orchestrator) that pins the reviewer role to a different model than the writer on both subscription tiers.
```

### wiki/history/workflows/agentic-orchestration-patterns.md (updated)

Append a new archive block (the file already has two blocks dated today from earlier applies, so this one is numbered `(3)`):

```
## Archived from current page on 2026-09-09 (3)

- [2026-06-29] Added Sidekick multi-model harness pattern: persistent frontier + cheaper sidekick agents, cache-aware mid-session model switching at compaction boundaries; contrasted with per-call advisor/smart-friend escalation.
```

### wiki/tools/cursor.md (updated)

Frontmatter: bump `as_of: 2026-08-29` → `as_of: 2026-09-09`; append `cursor-self-driving-codebases-2026-09-09` to the `sources:` list.

Add to `## Recent changes` (as the newest entry, at the top of the list):

```
- [2026-09-09] Cursor detailed the agent harness behind its long-running research (browser-building swarm, ~1,000 commits/hour peak over one week, recursive planner/subplanner/worker design) and said part of this research is now being made available to try for some users.
```

### wiki/history/tools/cursor.md (updated)

Append a new archive block:

```
## Archived from current page on 2026-09-09

- [2026-04-22] Added Truell's third-era data: 35% of Cursor internal PRs from cloud agents; 2:1 agent-to-Tab user ratio; 15× agent usage growth YoY
```

### wiki/sources/articles/cursor-agent-swarm-economics-2026-09-07.md (updated)

Append to `## Key claims extracted`:

```
- New custom VCS replaces Git for this generation of the swarm, raising throughput from the predecessor harness's ~1,000 commits/hour to ~1,000 commits/second
- Solo Opus 4.8 run's codebase published: github.com/cursor/minisqlite
- Context-efficiency explanation for why planner/worker splits scale (planner never implements, worker never plans), with an explicit analogy to Coase's "The Nature of the Firm" on coordination costs
```

### wiki/sources/articles/cursor-self-driving-codebases-2026-09-09.md (new)

```md
---
title: "Towards self-driving codebases"
type: source
source_type: article
source_file: raw/articles/2026-09-09-cursorcom-blog-self-driving-codebases.md
url: https://cursor.com/blog/self-driving-codebases
ingested: 2026-09-09
domains: [agents, coding]
---

# Towards self-driving codebases

Cursor's account of the harness behind its long-running browser-building research: how the multi-agent design evolved from a flat, lock-based self-coordinating swarm through a planner/executor/judge split to a recursive planner/subplanner/worker topology, plus the freshness mechanisms, prompting lessons, and throughput tradeoffs learned along the way. No publish date is shown on the live page. The post is Cursor's own follow-up to "Scaling long-running autonomous coding" and is called "an earlier post about the swarm" by the already-ingested 2026-09-07 "Agent swarms and the new model economics" post — meaning it predates that post, likely by several months (it references Opus 4.5 and GPT-5.1/5.2 as current models, both superseded generations by the wiki's other pages' timelines). Dated by ingest-date fallback per the wiki's source-date rule.

## Influenced pages

- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — recursive planner/subplanner/worker topology, freshness mechanisms, prompting lessons, steady-error-rate design principles
- [Cursor](../../tools/cursor.md) — Recent-changes note on the harness research and its partial availability to users

## Key claims extracted

- Recursive planner/subplanner/worker topology: root planner never codes, spawns subplanners for subdividable scope, disposable workers report back a single handoff
- Removed a central integrator role once workers proved capable of resolving their own merge conflicts
- Freshness mechanisms: rewritten (not appended) scratchpad, self-summarization at context limits, self-reflection prompts, encouraged pivoting
- Prompting lessons: negative constraints beat positive reminders; concrete quantity ranges beat vague scope language
- Accepted a small, stable error rate rather than requiring 100% per-commit correctness, with a final "green branch" reconciliation pass
- Named design principles: anti-fragile, empirical-over-assumption-driven, design-for-throughput-explicitly
- Peaked at ~1,000 commits/hour across 10M tool calls over one continuous week with no human intervention
```

## Open questions

- Should `donvito/codex-astra-luna-orchestrator` get its own `wiki/tools/` page? It's a working, well-documented implementation of the planner-uses-smart-model/worker-uses-cheap-model pattern specifically for Codex, similar in spirit to existing pages like [gstack](../wiki/tools/gstack.md) (Garry Tan's Claude Code config) or [Paperclip](../wiki/tools/paperclip.md) — but unlike those, it has no adoption metrics (stars, users) to cite. Currently folded into the workflows page as a pattern example only; say the word if a dedicated page is wanted instead.
