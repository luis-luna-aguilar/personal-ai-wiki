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
