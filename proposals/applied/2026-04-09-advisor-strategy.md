---
type: proposal
source: raw/articles/2026-04-09-claudecom-blog-the-advisor-strategy.md
status: pending
created: 2026-04-09
---

# Proposal: The advisor strategy (Anthropic)

## Summary

Anthropic introduces the "advisor strategy" — a multi-model agentic pattern where a cheap executor (Sonnet or Haiku) runs the loop end-to-end and escalates to Opus *only when it hits a decision it can't solve*. To make the pattern a one-line change, they ship a server-side `advisor_20260301` tool on the Claude API: declare it in `tools` on a Messages request, the executor decides when to invoke it, handoff happens inside a single `/v1/messages` call, and advisor/executor tokens are billed and reported separately. Reported lifts (vendor evals): Sonnet+Opus-advisor vs Sonnet alone → +2.7% on SWE-bench Multilingual *and* −11.9% cost; Haiku+Opus-advisor vs Haiku alone on BrowseComp → 41.2% vs 19.7% (more than double).

This inverts the usual sub-agent pattern (large orchestrator decomposes → small workers execute). It is the first time a major lab has shipped escalation-on-demand as a first-class server-side primitive rather than a library pattern.

## Intended changes

- [x] **Create** `wiki/workflows/advisor-strategy.md` — new workflow page, main subject of this ingest (also establishes the first entry under `wiki/workflows/`)
    > See draft below.

- [x] **Update** `wiki/state-of/agents.md` — add a new `model-orchestration` subcategory with [[workflows/advisor-strategy]] under it, add the source to frontmatter `sources`, add a Recent changes entry. Bumps page `as_of` to 2026-04-09 (already that date).
    > See draft below.

- [x] **Create** `wiki/sources/articles/advisor-strategy.md` — source summary page.
    > See draft below.

- [x] **Update** `wiki/index.md` — add the new workflows entry, refresh page counts.
    > See draft below.

## Page drafts

### wiki/workflows/advisor-strategy.md (new)

```markdown
---
title: Advisor strategy
type: workflow
domains: [agents]
subcategory: model-orchestration
tags: [anthropic, agentic]
as_of: 2026-04-09
sources: [advisor-strategy]
---

# Advisor strategy

A multi-model agentic pattern: a cheap *executor* (Sonnet or Haiku) runs the task end-to-end — calling tools, iterating — and consults a larger *advisor* (Opus) only when it hits a decision it can't reasonably solve. The advisor returns a plan, correction, or stop signal; it does not call tools and does not produce user-facing output.

Inverts the common sub-agent pattern where a large orchestrator decomposes work and delegates to smaller workers. Here the cheap model drives and frontier reasoning fires only at escalation points, keeping steady-state cost at executor level.

## Current status (as of 2026-04-09)

Shipped by Anthropic as `advisor_20260301`, a server-side tool on the Claude API — the first time a major lab has made escalation-on-demand a first-class API primitive rather than a pattern callers must build themselves. Declared in the `tools` array of a Messages request; handoff happens inside a single `/v1/messages` call with no extra round-trips. Executor and advisor tokens are billed at their respective rates and reported separately in `usage`. `max_uses` caps advisor calls per request. Works alongside other server-side tools (web search, code execution) in the same loop.

## Reported results (Anthropic internal evals)

Vendor numbers, no independent replication yet.

- **Sonnet + Opus-advisor** vs Sonnet alone on SWE-bench Multilingual: **+2.7%** score *and* **−11.9%** cost per task.
- **Haiku + Opus-advisor** on BrowseComp: **41.2%** vs Haiku solo **19.7%** (more than double).
- **Haiku + Opus-advisor** vs **Sonnet alone**: trails by 29 points, costs **85% less** per task — positioned as a strong option for high-volume work.
- Gains also reported on BrowseComp and Terminal-Bench 2.0 for Sonnet+Opus-advisor, specific numbers not quoted.

The Haiku-as-executor result is the most interesting data point: it opens a high-volume / bounded-intelligence niche that previously required a custom orchestrator.

## How it works

1. Start a Messages API request with a cheap executor (`claude-sonnet-4-6` or a Haiku build).
2. Declare the advisor tool:

   ```python
   {
       "type": "advisor_20260301",
       "name": "advisor",
       "model": "claude-opus-4-6",
       "max_uses": 3,
   }
   ```

3. The executor runs its loop; when it invokes `advisor`, the platform routes curated context to Opus, which returns a short plan (typically 400–700 tokens), and the executor resumes.

## Caveats

- Numbers are Anthropic's own evals on their own models. Treat as directional.
- Pattern quality depends on the executor recognising *when* it is stuck — metacognition is not separately benchmarked.
- The advisor cannot call tools. Guidance only — not a fallback for work the executor cannot *execute*, only for decisions it cannot *make*.
- Cost advantage shrinks if the executor over-invokes the advisor; `max_uses` is the only advertised ceiling.
- Tied to Anthropic's server-side tooling today. Multi-vendor advisor setups are still DIY.

## Related

- [[state-of/agents]]

## Recent changes

- [2026-04-09] First content for this page, from Anthropic's "The advisor strategy" launch post and the concurrent release of the `advisor_20260301` server-side tool.

## Sources

- [[sources/articles/advisor-strategy]]
```

### wiki/state-of/agents.md (updated)

```markdown
---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-04-09
sources: [cursor-3-launch, advisor-strategy]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

## Subcategories

### Agent orchestration UIs

Surfaces (desktop, web, mobile, chat) where humans supervise, hand off, and review work across multiple AI agents running in parallel.

- [[tools/cursor]] — Cursor 3's desktop app surfaces local and cloud agents in one sidebar, with handoff between environments and demos/screenshots from cloud agents *(as of 2026-04-09)*

### Model orchestration

Patterns that combine models of different sizes or costs inside a single agentic task. Concerned with *how* agents are structured internally (which model runs the loop, which model steps in when), not with the user-facing surface.

- [[workflows/advisor-strategy]] — Anthropic: a small executor (Sonnet or Haiku) drives the loop and escalates to Opus as an *advisor* only when stuck. Shipped as a server-side `advisor_20260301` tool on the Claude API, making it a one-line change to a Messages request. Reported +2.7% on SWE-bench Multilingual *and* −11.9% cost for Sonnet+Opus-advisor vs Sonnet alone *(as of 2026-04-09)*

## Recent changes

- [2026-04-09] Added `model-orchestration` subcategory with [[workflows/advisor-strategy]] after ingesting Anthropic's advisor-strategy launch post.
- [2026-04-09] First content for this page. Added `agent-orchestration-ui` subcategory with Cursor after ingesting the Cursor 3 launch post.
```

### wiki/sources/articles/advisor-strategy.md (new)

```markdown
---
title: The advisor strategy — Claude blog
type: source
source_type: article
source_file: raw/articles/2026-04-09-claudecom-blog-the-advisor-strategy.md
url: https://claude.com/blog/the-advisor-strategy
ingested: 2026-04-09
domains: [agents]
---

# The advisor strategy — Claude blog

Anthropic announces the "advisor strategy" — pairing Opus (advisor) with Sonnet or Haiku (executor) inside a single agentic task — and ships the `advisor_20260301` server-side tool on the Claude API to make it a one-line API change. Positioning post plus API feature launch, with vendor eval numbers attached.

## Influenced pages

- [[workflows/advisor-strategy]] — new page, main subject of the ingest
- [[state-of/agents]] — new `model-orchestration` subcategory created; advisor strategy placed under it

## Key claims extracted

- Executor (Sonnet or Haiku) runs the agentic loop end-to-end — calls tools, reads results, iterates. The advisor (Opus) is consulted only when the executor hits a decision it can't reasonably solve.
- The advisor returns a plan, a correction, or a stop signal. It does *not* call tools and does *not* produce user-facing output.
- Inverts the common sub-agent pattern where a larger orchestrator decomposes work for smaller workers.
- New server-side tool `advisor_20260301`. Declared in a Messages API request alongside other tools, with `model`, `name`, `max_uses`. Executor decides when to invoke it. Handoff stays inside a single `/v1/messages` call — no extra round-trips, no caller-side context management.
- Advisor typically returns 400–700 text tokens.
- Billing: executor tokens at executor rate, advisor tokens at advisor rate; each reported separately in the `usage` block.
- `max_uses` is the only built-in cap on advisor calls per request.
- **Sonnet + Opus advisor** vs Sonnet alone on SWE-bench Multilingual: +2.7 percentage points in score, −11.9% cost per agentic task.
- **Haiku + Opus advisor** on BrowseComp: 41.2% vs Haiku solo 19.7% — more than double.
- **Haiku + Opus advisor** vs Sonnet solo: trails by 29 points in score, costs 85% less per task. Framed as a strong option for high-volume tasks.
- Also reports gains on BrowseComp and Terminal-Bench 2.0 for Sonnet+Opus-advisor, without specific numbers for those combinations.
- Works alongside other server-side tools (web search, code execution) in the same loop.

## Caveats

- All numbers are from Anthropic's own internal evals on their own models. No independent replication.
- The post references three footnote markers (SWE-bench Multilingual, BrowseComp, Terminal-Bench 2.0). The footnote bodies were not captured in the raw extract.
```

### wiki/index.md (updated)

```markdown
---
title: Wiki Index
type: index
as_of: 2026-04-09
---

# Wiki Index

Catalog of every page in the wiki. This file is the LLM's starting point for every query and every ingest — read it first to find relevant pages before drilling in.

When adding a new wiki page (via a proposal), add its index entry under the correct section. One line per page: wikilink + one-line description + `(as_of: YYYY-MM-DD)`.

---

## State of

Read-me-first dashboards per domain.

- [[state-of/coding]] — current state of AI coding tools and workflows *(as_of: 2026-04-09)*
- [[state-of/models]] — current state of foundation models *(as_of: —)*
- [[state-of/agents]] — current state of agentic systems and tool use *(as_of: 2026-04-09)*
- [[state-of/legal]] — current state of AI in legal practice *(as_of: 2026-04-09)*

## Models

Foundation models. One page per model family or generation.

- [[models/composer-2]] — Cursor's in-house frontier coding model; stub *(as_of: 2026-04-09)*

## Tools

Tools and products built on top of models. One page per tool.

- [[tools/cursor]] — Cursor 3 agentic coding workspace; multi-repo, local↔cloud agent handoff *(as_of: 2026-04-09)*
- [[tools/harvey]] — legal AI platform; thin stub from a single editorial source *(as_of: 2026-04-09)*
- [[tools/kiro]] — VS Code-based SDD tool, 3-doc workflow *(as_of: 2026-04-09)*
- [[tools/spec-kit]] — GitHub's CLI SDD scaffolder with slash commands *(as_of: 2026-04-09)*
- [[tools/tessl]] — CLI + MCP framework exploring spec-as-source; private beta *(as_of: 2026-04-09)*

## Benchmarks

Benchmark pages. Current leaderboards and methodology.

_(empty)_

## Workflows

Reusable patterns and recipes.

- [[workflows/advisor-strategy]] — Anthropic's small-executor + Opus-advisor escalation pattern, now a server-side `advisor_20260301` tool on the Claude API *(as_of: 2026-04-09)*

## Concepts

Ideas and techniques (RAG, context engineering, compound engineering, etc.).

- [[concepts/spec-driven-development]] — SDD concept, three-level taxonomy, critiques *(as_of: 2026-04-09)*

## Trends

Things being watched that haven't solidified yet.

- [[trends/agents-reshape-organizations]] — leverage moves from individual to org as autonomous agents take coordination work *(as_of: 2026-04-09)*

## Sources

See `wiki/sources/` — source summaries are not indexed here (they're many and cheap). Use `grep` or Glob when you need them.

---

## Page count

- state-of: 4 (3 populated, 1 skeleton)
- models: 1
- tools: 5
- benchmarks: 0
- workflows: 1
- concepts: 1
- trends: 1

**Total content pages: 9.** The wiki is in the bootstrap phase (<30 pages) — categorization discipline is relaxed.
```

## Schema / vocabulary additions

- [x] Add new subcategory `model-orchestration` to `wiki/_schema/subcategories.md`:

    ```
    ### model-orchestration
    - **Parent domain(s):** agents
    - **Applies to types:** workflow | concept
    - **Definition:** Patterns that combine models of different sizes or costs inside a single agentic task — e.g. a small executor escalating to a larger advisor, or a large orchestrator delegating to small workers. Concerned with how an agent is internally structured, not with the user-facing surface.
    - **Examples:** [[workflows/advisor-strategy]]
    ```

- [x] Add new tag `anthropic` to `wiki/_schema/tags.md`:

    ```
    - **`anthropic`** — vendor/org: Anthropic
    ```

    (The file's own "Categories of tags" section already lists `anthropic` as a canonical example of a vendor tag — formalising it here.)

## Open questions

- **Model pages?** The source names `claude-opus-4-6`, `claude-sonnet-4-6`, and a Haiku build, but it is about a *pattern*, not about the models themselves. I have **not** proposed creating `models/claude-opus.md` / `claude-sonnet.md` / `claude-haiku.md` from this source — that would be creating conceptual pages from incidental mentions. Recommend waiting for an actual model-launch / model-update source. Flag if you'd rather I stub them now anyway.
	- Let's keep them for now. 

- **Benchmark pages?** The source mentions SWE-bench Multilingual, BrowseComp, and Terminal-Bench 2.0, but only as rows for advisor-vs-solo comparisons. Creating `benchmarks/swe-bench-multilingual.md` etc. from a single derivative data point would be premature. Recommend deferring until a source actually describes those benchmarks. Flag if you want stubs.
	-  let's also skip those pages 

- **Subcategory name.** I picked `multi-model-orchestration` because it covers both escalation (small → big, this post) and decomposition (big → small, the pattern this inverts). Alternative: `escalation-patterns` (narrower, advisor-specific). Happy to switch if you prefer.
	- the multi-model orchestration category should be only the model orchestration category

- **Naming on the workflow page.** Anthropic calls it "the advisor strategy". The wiki page title matches. The server-side tool is `advisor_20260301`. If you'd rather make the tool name itself the page title (or create a second tool-focused page), say so.
	-  keep the current name

## Comments

- There is a little bit of redundancy in the workflow file for the advisor strategy. When you mention why it's interesting, it's stuff that you already mentioned. Let's try to make it overall more concise. We need an efficient knowledge base as a general rule
