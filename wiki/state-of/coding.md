---
title: State of Coding
type: state-of
domains: [coding]
tags: []
as_of: 2026-04-10
sources: [sdd-3-tools-fowler, cursor-3-launch, stripe-cli, claude-code-monitor, openai-pro-100, cursor-pr-demos, shopify-ai-toolkit]
---

# State of Coding

Current state of AI tools for software development. Organized by subcategory — each subcategory can have multiple top players. Ambiguity is expected.

## Subcategories

### Spec-driven development

Tools where a structured natural-language spec is the primary input to AI coding agents. The term is contested and the field is early — no clear leader. See [[concepts/spec-driven-development]] for the concept and taxonomy.

- [[tools/kiro]] — VS Code-based; requirements → design → tasks; lightest-weight, mostly spec-first *(as of 2025-10-15)*
- [[tools/spec-kit]] — GitHub; CLI scaffolder + slash commands; constitution → specify → plan → tasks; most customizable *(as of 2025-10-15)*
- [[tools/tessl]] — CLI + MCP server; only tool pursuing spec-as-source; private beta *(as of 2025-10-15)*

### Agentic coding workspace

Coding tools whose primary UI is built around managing one or more AI coding agents (local and cloud), rather than file-centric editing with AI assistance bolted on.

- [[tools/cursor]] — Cursor 3 is a unified agent workspace with multi-repo, local↔cloud handoff, plugin marketplace; built from scratch (not a VS Code fork); legacy IDE mode still available *(as of 2026-04-02)*

### Agentic DevOps

Tools that turn app-stack setup into a repeatable command-line workflow across multiple providers, with explicit support for agent-executable provisioning.

- [[tools/stripe-cli]] — Stripe CLI's developer-preview `projects` workflow provisions hosting, databases, auth, AI, analytics, and more across providers; credentials sync back to the environment and billing can be managed from the CLI *(as of 2026-04-09)*

### Terminal coding agent

CLI-based AI coding agents that run in the terminal, operating autonomously across file editing, shell commands, and tool use without a graphical IDE.

- [[tools/claude-code]] — Anthropic; terminal-first agent with background Monitor tool for event-driven wakeups *(as of 2026-04-10)*
- [[tools/codex]] — OpenAI; cloud-based coding agent via CLI and ChatGPT *(as of 2026-04-10)*

### Agent toolkits

Toolkits that package a developer platform's docs, schemas, validation, and related capabilities for AI coding tools via plugins, skills, or MCP.

- [[tools/shopify-ai-toolkit]] — Shopify packages platform docs, API schemas, and validation for Claude Code, Codex, Cursor, Gemini CLI, and VS Code via plugin, skills, or local Dev MCP; Codex support is skills/MCP only *(as of 2026-04-10)*

## Recent changes

- [2026-04-10] Added `agent-toolkits` subcategory with [[tools/shopify-ai-toolkit]]
- [2026-04-10] Added `terminal-coding-agent` subcategory with [[tools/claude-code]] and [[tools/codex]]
- [2026-04-10] OpenAI launches $100/mo Pro tier — 5× Codex usage, exclusive Pro model, launch promo through 2026-05-31
- [2026-04-09] Added `agentic-devops` subcategory with [[tools/stripe-cli]] after ingesting the `projects.dev` launch page
- [2026-04-02] Cursor 3 launched; added new `agentic-coding-workspace` subcategory and placed Cursor under it
