---
type: proposal
source: raw/articles/2026-04-09-cursorcom-blog-cursor-3.md
status: pending
created: 2026-04-09
---

# Proposal: Cursor 3 launch — "Meet the new Cursor"

## How to give me feedback on this proposal

- **Include / skip:** tick `[x]` to include an item, leave `[ ]` to skip. Unchecked items will not be applied.
- **Edit drafts in place:** every page draft below is in a fenced code block. Edit them directly — I re-read the file as you left it and use whatever is there at apply time.
- **Answer open questions:** add an indented bullet directly under the question (any prefix works — `→`, `Comment:`, plain text). I'll pick it up.
- **Free-form notes:** add a `## Comments` section at the bottom for anything that doesn't fit the above.

## Summary
Cursor announces **Cursor 3**, framed as a "unified workspace for building software with agents" rather than an IDE. The interface is rebuilt from scratch (the original Cursor was a VS Code fork; this one is not), centered on managing fleets of local *and* cloud agents in one sidebar, with seamless handoff between environments. Mentions Composer 2 (Cursor's own frontier coding model), an integrated browser, a plugin marketplace (MCPs, skills, subagents), and an option to drop back into the legacy "Cursor IDE" mode.

This is the wiki's second real ingest. We are still in bootstrap (4 content pages), so creating new pages and a new subcategory is appropriate.

## Intended changes

- [x] **Create** `wiki/tools/cursor.md` — new tool page covering Cursor 3 (the new agent-first product) and noting its origin as a VS Code fork
- [x] **Update** `wiki/state-of/coding.md` — add a new `agent-first-ide` subcategory and place Cursor under it; bump page `as_of`
- [x] **Update** `wiki/state-of/agents.md` — first content for this page; add a subcategory for "agent orchestration UIs" with Cursor as a member
- [x] **Create** `wiki/sources/articles/cursor-3-launch.md` — source summary
- [x] **Update** `wiki/index.md` — add the Cursor page; bump tools count to 4, populate state-of/agents

## Schema / vocabulary additions

- [x] Add subcategory `agent-first-ide` to `wiki/_schema/subcategories.md`
  - Parent domain: `coding`
  - Applies to types: `tool`
  - Definition: Coding tools whose primary UI is built around managing one or more AI coding agents (local and/or cloud), rather than file-centric editing with AI assistance bolted on.
- [x] Add subcategory `agent-orchestration-ui` to `wiki/_schema/subcategories.md`
  - Parent domain: `agents`
  - Applies to types: `tool`
  - Definition: Surfaces (desktop, web, mobile, chat-integration) that let a human supervise, hand off, and merge work across multiple AI agents running in parallel.
- [x] Add tags to `wiki/_schema/tags.md`:
  - `closed-source` — license/openness
  - `agentic` — flavor (agent-centric product or workflow)

## Page drafts

### wiki/tools/cursor.md (new)

```
---
title: Cursor
type: tool
domains: [coding, agents]
subcategory: agent-first-ide
tags: [closed-source, agentic]
as_of: 2026-04-09
sources: [cursor-3-launch]
---

# Cursor

Cursor is an AI coding product from Anysphere. It started life as a VS Code fork focused on inline AI editing and pair programming, and with **Cursor 3** has been rebuilt from scratch as an agent-first workspace: a desktop app that surfaces local and cloud AI coding agents in one sidebar, supports multi-repo work, and lets users hand sessions back and forth between environments. The legacy Cursor IDE mode is still available inside the same product.

## Current status (as of 2026-04-09)

- **Cursor 3** is the current shipped version, announced in the "Meet the new Cursor" post on cursor.com/blog
- New top-level interface built from scratch (not the VS Code fork) and centered on agents
- Inherently multi-workspace: humans and agents work across multiple repos simultaneously
- Backed by [[concepts/spec-driven-development|Composer 2]], Cursor's own frontier coding model with high usage limits *(model page TBD)*
- Plugin marketplace ("Cursor Marketplace") supports MCPs, skills, and subagents, with one-click install and private team marketplaces
- Legacy "Cursor IDE" mode still available — switch back at any time

## What's new in Cursor 3

- **All your agents in one place.** Local and cloud agents (kicked off from desktop, mobile, web, Slack, GitHub, Linear) appear in one sidebar.
- **Run many agents in parallel.** Cloud agents produce demos and screenshots for the human to verify; same experience as `cursor.com/agents`, now embedded.
- **Local ↔ cloud handoff.** Move a session from cloud to local for hands-on edits; move local → cloud to keep long-running tasks alive while offline.
- **Diffs & PR flow.** New diffs view for editing/reviewing changes; stage, commit, and manage PRs from inside Cursor.
- **Files for understanding code.** Full LSP support — view files, go to definition — when you want to drop down a level.
- **Integrated browser.** Cursor can open, navigate, and prompt against local sites via a built-in browser tool.

## Strengths

- First-class support for orchestrating multiple agents across repos
- Seamless local/cloud session migration is genuinely novel
- Plugin ecosystem (MCPs, skills, subagents) lowers the bar for extending agent behavior
- Drops back to traditional IDE when the user wants direct control

## Weaknesses / caveats

- Closed source; no published benchmark numbers in the launch post
- Vendor framing emphasizes a "third era" narrative — usefulness for everyday brownfield work is not yet demonstrated by external usage reports
- Requires buying into a new mental model (agent sessions as the unit of work) — users coming from the IDE-centric Cursor will need to relearn the surface

## Recent changes

- [2026-04-09] Cursor 3 announced — rebuilt agent-first interface, multi-repo, local↔cloud handoff, Composer 2, plugin marketplace

## Sources

- [[sources/articles/cursor-3-launch]]
```

### wiki/state-of/coding.md (updated)

```
---
title: State of Coding
type: state-of
domains: [coding]
tags: []
as_of: 2026-04-09
sources: [sdd-3-tools-fowler, cursor-3-launch]
---

# State of Coding

Current state of AI tools for software development. Organized by subcategory — each subcategory can have multiple top players. Ambiguity is expected.

## Subcategories

### Spec-driven development

Tools where a structured natural-language spec is the primary input to AI coding agents. The term is contested and the field is early — no clear leader. See [[concepts/spec-driven-development]] for the concept and taxonomy.

- [[tools/kiro]] — VS Code-based; requirements → design → tasks; lightest-weight, mostly spec-first *(as of 2026-04-09)*
- [[tools/spec-kit]] — GitHub; CLI scaffolder + slash commands; constitution → specify → plan → tasks; most customizable *(as of 2026-04-09)*
- [[tools/tessl]] — CLI + MCP server; only tool pursuing spec-as-source; private beta *(as of 2026-04-09)*

### Agent-first IDE

Coding tools whose primary UI is built around managing one or more AI coding agents (local and cloud), rather than file-centric editing with AI assistance bolted on.

- [[tools/cursor]] — Cursor 3 is a unified agent workspace with multi-repo, local↔cloud handoff, plugin marketplace; built from scratch (not a VS Code fork); legacy IDE mode still available *(as of 2026-04-09)*

## Recent changes

- [2026-04-09] Cursor 3 launched; added new `agent-first-ide` subcategory and placed Cursor under it
- [2026-04-09] First content for this page. Added `spec-driven-development` subcategory with Kiro, spec-kit, Tessl after ingesting Fowler's SDD survey.
```

### wiki/state-of/agents.md (updated)

```
---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-04-09
sources: [cursor-3-launch]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

## Subcategories

### Agent orchestration UIs

Surfaces (desktop, web, mobile, chat) where humans supervise, hand off, and review work across multiple AI agents running in parallel.

- [[tools/cursor]] — Cursor 3's desktop app surfaces local and cloud agents in one sidebar, with handoff between environments and demos/screenshots from cloud agents *(as of 2026-04-09)*

## Recent changes

- [2026-04-09] First content for this page. Added `agent-orchestration-ui` subcategory with Cursor after ingesting the Cursor 3 launch post.
```

### wiki/sources/articles/cursor-3-launch.md (new)

```
---
title: Meet the new Cursor (Cursor 3 launch)
type: source
source_type: article
source_file: raw/articles/2026-04-09-cursorcom-blog-cursor-3.md
url: https://cursor.com/blog/cursor-3
ingested: 2026-04-09
domains: [coding, agents]
---

# Meet the new Cursor (Cursor 3 launch)

Cursor's official launch post for Cursor 3, on cursor.com/blog. Frames Cursor 3 as a rebuild-from-scratch interface centered on agents, in service of a "third era of software development" where fleets of agents work autonomously. No benchmark numbers; this is a positioning + feature post.

## Influenced pages

- [[tools/cursor]] — initial tool page (created from this source)
- [[state-of/coding]] — added new `agent-first-ide` subcategory with Cursor
- [[state-of/agents]] — first content; added `agent-orchestration-ui` subcategory with Cursor

## Key claims extracted

- Cursor 3 is a new top-level interface, built from scratch (the original Cursor was a VS Code fork)
- Sidebar surfaces all local and cloud agents in one place; agents can be kicked off from desktop, mobile, web, Slack, GitHub, Linear
- Cloud agents produce demos and screenshots for the user to verify
- Sessions can be moved between local and cloud in either direction
- "Composer 2" is Cursor's own frontier coding model with high usage limits; positioned as the model behind Cursor 3 work
- New diffs view supports stage / commit / PR management from inside Cursor
- Cursor Marketplace hosts plugins (MCPs, skills, subagents); supports private team marketplaces
- Legacy Cursor IDE mode remains available in the same product
- Vendor invokes a "third era of software development" narrative (linked but not detailed in this post)
- No benchmark numbers in the post (no SWE-bench mention etc.)
```

### wiki/index.md (updated)

```
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

## Models

Foundation models. One page per model family or generation.

_(empty)_

## Tools

Tools and products built on top of models. One page per tool.

- [[tools/cursor]] — Cursor 3 agent-first workspace; multi-repo, local↔cloud agent handoff *(as_of: 2026-04-09)*
- [[tools/kiro]] — VS Code-based SDD tool, 3-doc workflow *(as_of: 2026-04-09)*
- [[tools/spec-kit]] — GitHub's CLI SDD scaffolder with slash commands *(as_of: 2026-04-09)*
- [[tools/tessl]] — CLI + MCP framework exploring spec-as-source; private beta *(as_of: 2026-04-09)*

## Benchmarks

Benchmark pages. Current leaderboards and methodology.

_(empty)_

## Workflows

Reusable patterns and recipes.

_(empty)_

## Concepts

Ideas and techniques (RAG, context engineering, compound engineering, etc.).

- [[concepts/spec-driven-development]] — SDD concept, three-level taxonomy, critiques *(as_of: 2026-04-09)*

## Trends

Things being watched that haven't solidified yet.

_(empty)_

## Sources

See `wiki/sources/` — source summaries are not indexed here (they're many and cheap). Use `grep` or Glob when you need them.

---

## Page count

- state-of: 3 (2 populated, 1 skeleton)
- models: 0
- tools: 4
- benchmarks: 0
- workflows: 0
- concepts: 1
- trends: 0

**Total content pages: 5.** The wiki is in the bootstrap phase (<30 pages) — categorization discipline is relaxed.
```

## Open questions

- **Composer 2 as its own model page?** The post mentions Composer 2 as Cursor's frontier coding model but gives no detail beyond "high usage limits." I draft-mentioned it inside `tools/cursor.md` and left a `*(model page TBD)*` flag instead of stubbing `wiki/models/composer.md`. I think a thin model page is not justified yet. Wait for an actual Composer-focused source?
	- Composer 2 is a model, why did you link it to spec-driven-development? it should have its own page.
- **Two subcategories or one?** I created `agent-first-ide` (under `coding`) AND `agent-orchestration-ui` (under `agents`) and put Cursor in both. This is honest to how the post pitches the product (it's in both spaces) but it does mean Cursor appears on two state-of pages. Alternative: keep only one subcategory and link from the other state-of page in prose. Preference?
	- Lets keep it in 2.
- **Subcategory naming.** `agent-first-ide` is fine but slightly awkward. Alternatives I considered: `agentic-coding-workspace`, `multi-agent-ide`, `agent-orchestration-ide`. Same question for `agent-orchestration-ui`. Let me know if you want me to rename either before applying.
	- i like better agentic coding workspace. lets keep agent orchestration ui
- **Cursor's old identity.** Pre-Cursor-3, Cursor was the leading "IDE pair programming" tool. Should I also create an `ide-pair-programming` subcategory now (for historical accuracy and to make room for future tools like Windsurf), or wait until we ingest a source that justifies one?
	- No, lets not create that
- **"Third era of software development" link.** The post links to `cursor.com/blog/third-era`, which sounds like it would map to a `trends/` page. Do you want me to fetch + ingest that as a follow-up source? (I won't do it as part of this proposal — separate ingest.)
	- No
- **"Composer 2" link.** Same question — `cursor.com/blog/composer-2` is linked from this post. Worth a follow-up ingest?
	- I do want to ingest the composer 2 url so we can have more info on that model page
- **Reconsider the `vscode-fork` decision?** You asked me to drop `vscode-fork` from the tag schema during the SDD ingest. Cursor (the original) is the canonical example of the term. Cursor 3 is *no longer* a VS Code fork, so it doesn't need the tag now — but if we ever ingest pre-Cursor-3 history or Windsurf, the tag may genuinely be useful. Do you want to revisit the decision, leave it dropped, or note this in `DEFERRED.md`?
	- We leave it dropped, its not relevant information

## Comments

- I'm interested in finding a way to show only what changed when you update a page. For example on the coding page, you're writing about spec-driven development, and that was already there. I only want to see what's being added. What kind of formatting can we use to communicate just the real changes and avoid showing the whole page? I don't want to read the whole page. The same happened with the index. They're showing me the whole index.