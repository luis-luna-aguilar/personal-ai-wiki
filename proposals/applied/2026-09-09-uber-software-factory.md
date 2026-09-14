---
type: proposal
source: raw/tweets/2026-09-09-ubereng-2093444169037762840.md
status: pending
created: 2026-09-09
---

# Proposal: Uber Engineering — "Running a Software Factory Efficiently at Uber Scale" (2026-08-28)

## Summary

### The source

On August 28, 2026, Uber's own engineering account posted a detailed, first-party account (written by @udaykiran) of how Uber runs and optimizes its internal AI coding-agent fleet at scale. The headline numbers: more than 70% of Uber's pull requests are now attributed to agents, engineers have built over 3,600 reusable agent skills across the software development lifecycle, and those skills execute more than 30,000 times a day. From February to August 2026, weekly active users across all of Uber's agentic tooling grew 7x and weekly agentic requests grew 9.4x — while, holding model choice fixed, cost per 1,000 requests fell almost 34% from its peak and cost per session fell 52% from its June peak. The post walks through the specific levers behind that cost curve. On model selection: Uber benchmarks every managed agent against its own real work (uReview, its AI code-review tool, is graded on precision/recall/F1 and cost against real PRs with known bugs) and treats the "subagent defaults to a cheaper model while the primary model plans and evaluates" split as its single most impactful, and still-growing, cost lever. On token efficiency: automatic context compaction at a fixed 400K-token threshold, reasoning effort defaulted to Medium, and a prompt-caching TTL choice (1-hour vs. 5-minute cache entries) tuned to how long engineers actually leave sessions idle. On tool-calling overhead: because loading 100+ MCP tool schemas into every session was adding 50-70K tokens before a single prompt was typed, Uber built CLI-based tool resolution and tool search to load only what's needed, plus "Code-mode" — batching multiple tool calls into one script that runs in a subprocess and returns only a summary, cutting token use over 50% even on small responses and over 90% on bulk workflows. On context grounding: an internal "AI Context Graph" (24 million nodes, 80 million edges, spanning 30+ internal systems) that let a grounded agent answer a data-location question in 38 seconds versus 20+ minutes, two subagents, and three errors for an ungrounded one. And on visibility: a live per-session cost counter, staged Slack spend nudges, and a dashboard that flags 16 named cost-anti-patterns (like stale-cache rebuilds or 100K-token prompt-init overhead) with a dollar figure attached to each.

### What changes

The wiki already tracks cost-aware model routing and engineering-specific AI adoption on two dedicated training pages, and general orchestration patterns on a third; none of them yet reflect this level of first-party operational detail from a company running agents at Uber's scale.

- **Cost-aware AI task routing** gains a new evidence entry (Uber's benchmark-driven, Pareto-frontier model-selection process and its cheaper-subagent-by-default lever) and four new FinOps-control bullets (the prompt-caching TTL tradeoff, fixed-threshold auto-compaction, Medium-as-default reasoning effort, and the live-cost-counter/spend-tier/anti-pattern-dashboard visibility stack). This page has no Recent-changes log, so no spill applies; page date moves to 28 August.
- **Agentic orchestration patterns** gains two new pattern entries — the AI Context Graph (grounding agents in a queryable knowledge graph instead of blind code search) and Code-mode (batching tool calls into one script instead of one model turn per call). The page's Recent-changes list is at its 10-entry cap, so its oldest entry (2026-06-29, the Sidekick multi-model harness note) spills to history. Page date moves to 28 August.
- **AI enablement — software development** gains a new Proven-patterns entry covering the Software Factory adoption numbers and Uber's core strategic argument (eliminating wasted tokens, not just cutting unit price, is what let usage scale while unit cost fell). Its Recent-changes list is also at its 10-entry cap, so its oldest entry (2026-05-15, skill atrophy / supervision paradox) spills to history. Page date moves to 28 August.
- One new source page is created for the Uber post.

### What to weigh

This is a strong, detailed first-party source — Uber's own engineering account disclosing its own methodology and figures — so the only standard caveat applies: the numbers are self-reported by the company being measured, the same caveat the wiki already carries on comparable single-company evidence elsewhere on these same two training pages (Shopify, Anthropic's internal RSI figures). Nothing else needs independent verification here.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add 1 Evidence-from-practice entry, add 4 AI-FinOps-controls bullets, bump `as_of` to 2026-08-28, add source id
    > See draft below

- [ ] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add 2 new pattern bullets, add 1 Recent-changes entry, bump `as_of` to 2026-08-28, add source id
    > See draft below

- [ ] **Spill** `wiki/workflows/agentic-orchestration-patterns.md` → `wiki/history/workflows/agentic-orchestration-patterns.md` — oldest Recent-changes entry (2026-06-29, Sidekick multi-model harness) falls off the 10-entry cap
    > See draft below

- [ ] **Update** `wiki/training/ai-enablement-software-development.md` — add 1 Proven-patterns entry, add 1 Recent-changes entry, bump `as_of` to 2026-08-28, add source id
    > See draft below

- [ ] **Spill** `wiki/training/ai-enablement-software-development.md` → `wiki/history/training/ai-enablement-software-development.md` — oldest Recent-changes entry (2026-05-15, skill atrophy / supervision paradox) falls off the 10-entry cap
    > See draft below

- [ ] **Create** `wiki/sources/tweets/ubereng-software-factory-2026-08-28.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter: bump `as_of: 2026-09-07` — unchanged, since 2026-08-28 is older than the page's current newest claim (2026-09-07, the Cursor agent-swarm entry); append `ubereng-software-factory-2026-08-28` to `sources:`.

Add to `## Evidence from practice`, as a new bullet (placed after the existing "Cursor's agent-swarm planner-cost comparison" bullet):

```
- **Uber's benchmark-driven model selection.** Uber benchmarks every managed agent against its own real work before picking a model, then keeps moving as the frontier shifts: build a benchmark from the agent's actual task, run it on a harness that serves any model behind one interface, and move to whatever is Pareto-optimal on cost/completed-task, quality, and reliability. Its AI code-review tool, uReview, is graded against real pull requests with known bugs (precision/recall/F1, plus cost/PR, latency, timeouts, noise); switching models improved F1 while cutting cost/PR. A separate internal "Uber SWE Benchmark" (thousands of real PRs across large monorepos) informs model choice across all of Uber's SDLC-managed agents. The single most impactful — and still-growing — lever isn't the primary model, it's the subagent default: subagents are set to a cheaper model since they execute well-defined, delegated work that rarely needs frontier-level reasoning, while the primary model handles decomposition and evaluation, with manual override available per session.
```

Add to `## AI FinOps controls`, as new bullets appended to the existing list:

```
- Choose prompt-cache TTL by session idle-gap length, not a fixed default: Uber found its interactive sessions were frequently idle past the standard 5-minute cache window (forcing full-price prefix rebuilds), so it moved interactive sessions to a 1-hour TTL while keeping subagents — whose work is short-lived and focused — on 5 minutes.
- Cap context growth with a fixed auto-compaction threshold (e.g. 400K tokens) even on much larger context-window models, to control cache-burst and repeated-input costs rather than relying on the full window.
- Default reasoning effort to a middle tier (e.g. Medium) rather than maximum, since reasoning/output tokens bill at a multiple of input-token rates and a large share of tasks don't need top-tier reasoning to hit a good cost/quality balance.
- Pair spend visibility with staged behavioral nudges, not hard caps: a live per-session cost counter, a shared budget pool across interactive tools (separate tiers for managed agents), alerts at 50/80/100% of expected spend, and an on-demand dashboard that flags specific, named cost-anti-patterns (e.g. running simple sessions on an expensive model, stale-cache rebuilds after long idle gaps, 100K-token prompt-init overhead) each paired with its dollar impact — closer-to-real-time feedback than a single aggregate spend number.
```

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Frontmatter: bump `as_of: 2026-09-07` → `as_of: 2026-08-28`... — no change, 2026-08-28 is older than the page's current `as_of` (2026-09-07, from the Cursor swarm-coordination entry), so `as_of` stays `2026-09-07`; append `ubereng-software-factory-2026-08-28` to `sources:`.

Add these 2 new bullets to `## Current patterns` (placed near the end of the list, after the existing "Review lenses" bullet):

```
- **AI Context Graph: grounding agents in a queryable knowledge graph.** Rather than leaving agents to discover context via blind code search, ground them in a unified, queryable graph of the organization's actual systems. Uber's version spans 24 million nodes and 80 million edges across 86 node types and 117 edge types, integrating 30+ internal systems (services, teams, incident logs, PRs, architecture docs, deployments, datasets, historical table-usage queries) and answerable in natural language. The measured gap is stark: on an identical prompt to the same model, the graph-grounded agent identified the right table (used by 50+ analysts) and answered in 38 seconds, while the ungrounded agent spent 20+ minutes inspecting service code, spawned 2 subagents, hit 3 errors, and concluded — incorrectly — that the dataset was unqueryable. *Source: Uber Engineering, "Running a Software Factory Efficiently at Uber Scale" (2026-08-28)*
- **Code-mode: batch tool calls into one script instead of one model turn each.** Standard MCP tool use costs a full model turn per action — emit a request, load the raw response into context, process it, repeat — so a single multi-step task (e.g. one SQL query needing 2-5 status polls) burns several turns on protocol overhead alone. Code-mode instead lets the model write a script that runs the whole sequence in a subprocess and returns only a summary to the model's context. Measured on identical tasks run both ways: even minimal responses saw token use drop over 50% (the savings come from cutting schema init, multi-turn polling, and redundant reasoning, not from avoiding large payloads), and bulk/N-turn workflows compounded that to over 90%, since an N-model-turn loop collapses into a single script execution. *Source: Uber Engineering, "Running a Software Factory Efficiently at Uber Scale" (2026-08-28)*
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-08-28] Added the AI Context Graph pattern (grounding agents in a queryable graph of internal systems instead of blind code search — Uber's version: 24M nodes/80M edges, 38-second grounded vs. 20+-minute-and-3-errors ungrounded on an identical prompt) and Code-mode (batching tool calls into one subprocess script instead of one model turn per call — >50% token reduction on minimal responses, >90% on bulk workflows).
```

The list is now 11 entries (was at the 10-entry cap); the oldest, `[2026-06-29] Added Sidekick multi-model harness pattern...`, is removed from this page and spilled below.

### wiki/history/workflows/agentic-orchestration-patterns.md (updated)

Append a new archive block (create the file with this header if it does not already exist):

```
## Archived from current page on 2026-09-09

- [2026-06-29] Added Sidekick multi-model harness pattern: persistent frontier + cheaper sidekick agents, cache-aware mid-session model switching at compaction boundaries; contrasted with per-call advisor/smart-friend escalation.
```

### wiki/training/ai-enablement-software-development.md (updated)

Frontmatter: `as_of: 2026-07-16` → `as_of: 2026-08-28` (newer); append `ubereng-software-factory-2026-08-28` to `sources:`.

Add to `## Proven patterns`, as a new bullet:

```
- **Uber's "Software Factory": scale usage by eliminating wasted tokens, not just cutting unit price.** Uber reports more than 70% of its pull requests now attributed to agents, 3,600+ engineer-built agent skills across the SDLC, and 30,000+ skill executions a day. From February to August 2026, weekly active agentic users grew 7x and weekly agentic requests grew 9.4x — while, holding model choice fixed, cost per 1,000 requests fell ~34% from its peak and cost per session fell ~52% from its June peak. Uber's framing: this required eliminating zero-value token consumption (context bloat, redundant tool-call overhead, ungrounded search) rather than just choosing cheaper models or downgrading tooling, and the core strategic lever is moving SDLC workloads from interactive developer sessions into fully managed agents, since managed environments grant complete control over model routing, execution harness, and spend. See [Cost-aware AI task routing](cost-aware-ai-task-routing.md) for the specific optimization levers behind these numbers.
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-08-28] Added Uber's Software Factory adoption numbers (70%+ PRs agent-attributed, 3,600+ agent skills, 30K executions/day, 7x WAU growth) and its core strategic argument: eliminating wasted token consumption, not just cheaper unit prices, is what let usage scale 7x while unit costs fell.
```

The list is now 11 entries (was at the 10-entry cap); the oldest, `[2026-05-15] Skill atrophy / supervision paradox failure mode added...`, is removed from this page and spilled below.

### wiki/history/training/ai-enablement-software-development.md (updated)

Append a new archive block (create the file with this header if it does not already exist):

```
## Archived from current page on 2026-09-09

- [2026-05-15] Skill atrophy / supervision paradox failure mode added; Airbnb counter-pattern evidence (Lars Faye essay, May 2026)
```

### wiki/sources/tweets/ubereng-software-factory-2026-08-28.md (new)

```md
---
title: "Running a Software Factory Efficiently at Uber Scale"
type: source
source_type: tweet
source_file: raw/tweets/2026-09-09-ubereng-2093444169037762840.md
url: https://x.com/UberEng/status/2093444169037762840
published: 2026-08-28
ingested: 2026-09-09
domains: [agents, coding]
---

# Running a Software Factory Efficiently at Uber Scale

Uber Engineering's first-party account (posted by @udaykiran) of how it runs and cost-optimizes its internal AI coding-agent fleet: adoption numbers, a six-term cost equation, benchmark-driven Pareto-optimal model selection (uReview, the internal Uber SWE Benchmark), token-efficiency defaults (auto-compaction, reasoning effort, prompt-cache TTL), MCP-schema-bloat fixes (CLI tool resolution, tool search, Code-mode), the AI Context Graph for context grounding, and a spend-visibility/anti-pattern-dashboard stack.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — benchmark-driven model selection, FinOps controls (caching TTL, compaction, reasoning-effort default, spend visibility)
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — AI Context Graph and Code-mode patterns
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — Software Factory adoption numbers and strategic framing

## Key claims extracted

- 70%+ of Uber PRs attributed to agents; 3,600+ agent skills; 30,000+ skill executions/day
- Feb-Aug 2026: weekly active agentic users +7x, weekly agentic requests +9.4x; total spend stabilized since April
- With model held constant, cost/1,000 requests down ~34% from peak, cost/session down ~52% from June peak
- Benchmark-driven model selection (4-step process); uReview graded on precision/recall/F1 + cost against real PRs with known bugs; internal Uber SWE Benchmark
- Subagent-defaults-to-cheaper-model is called the single most impactful, still-growing cost lever
- Auto-compaction at 400K tokens (even on 1M-context models); reasoning effort defaulted to Medium
- Prompt-cache TTL: 1-hour for interactive sessions (was 5-minute, causing rebuilds on idle gaps), 5-minute for subagents
- MCP schema bloat: 100+ tools added 50-70K tokens of schema overhead; fixed via CLI tool resolution and tool search
- Code-mode: batches tool calls into one subprocess script; >50% token reduction on minimal responses, >90% on bulk workflows; 25+ pre-built code-mode skills deployed
- AI Context Graph: 24M nodes / 80M edges / 86 node types / 117 edge types across 30+ internal systems; 38-second grounded answer vs. 20+ minutes/2 subagents/3 errors ungrounded
- Session Analysis Dashboard flags 16 named cost anti-patterns with dollar impact, zero setup required
```
