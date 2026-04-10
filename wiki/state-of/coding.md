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

### Agentic coding workspace

Coding tools whose primary UI is built around managing one or more AI coding agents (local and cloud), rather than file-centric editing with AI assistance bolted on.

- [[tools/cursor]] — Cursor 3 is a unified agent workspace with multi-repo, local↔cloud handoff, plugin marketplace; built from scratch (not a VS Code fork); legacy IDE mode still available *(as of 2026-04-09)*

## Recent changes

- [2026-04-09] Cursor 3 launched; added new `agentic-coding-workspace` subcategory and placed Cursor under it
- [2026-04-09] First content for this page. Added `spec-driven-development` subcategory with Kiro, spec-kit, Tessl after ingesting Fowler's SDD survey.
