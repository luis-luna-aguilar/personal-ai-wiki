---
title: State of Coding
type: state-of
domains: [coding]
tags: []
as_of: 2026-04-21
sources: [sdd-3-tools-fowler, cursor-3-launch, stripe-cli, claude-code-monitor, openai-pro-100, cursor-pr-demos, shopify-ai-toolkit, cursor-bugbot-learning, claude-code-routines, openai-codex-ongoing-tasks, orca-homepage, coding-agent-control-planes, claude-code-leak-architecture, cursor-3-orchestration-bet]
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

- [[tools/cursor]] — Cursor remains the clearest reference point for the category: Cursor 3 and 3.1 treat coding as agent supervision work first, with tiled multi-agent control, local↔cloud handoff, branch-aware remote execution, plugin-marketplace extensibility, and Bugbot learning loops from production PR feedback *(as of 2026-04-14)*
- [[tools/orca]] — Open-source worktree IDE for running Claude Code, Codex, and other coding agents side by side with built-in terminals, file review, diff review, and CI/PR status tracking *(as of 2026-04-21)*

### Agentic DevOps

Tools that turn app-stack setup into a repeatable command-line workflow across multiple providers, with explicit support for agent-executable provisioning.

- [[tools/stripe-cli]] — Stripe CLI's developer-preview `projects` workflow provisions hosting, databases, auth, AI, analytics, and more across providers; credentials sync back to the environment and billing can be managed from the CLI *(as of 2026-04-09)*

### Terminal coding agent

CLI-based AI coding agents that still anchor in the terminal, but are increasingly expanding into supervised workspaces with repeatable workflows, background execution, and broader agent control surfaces.

- [[tools/claude-code]] — Anthropic; terminal-first agent with Monitor wakeups, hosted routines, and a product direction toward multi-session supervision *(as of 2026-04-21)*
- [[tools/codex]] — OpenAI; cloud coding agent via CLI and ChatGPT, increasingly framed around app use, memory, and repeatable ongoing tasks *(as of 2026-04-21)*

### Agent toolkits

Toolkits that package a developer platform's docs, schemas, validation, and related capabilities for AI coding tools via plugins, skills, or MCP.

- [[tools/shopify-ai-toolkit]] — Shopify packages platform docs, API schemas, and validation for Claude Code, Codex, Cursor, Gemini CLI, and VS Code via plugin, skills, or local Dev MCP; Codex support is skills/MCP only *(as of 2026-04-10)*

## Recent changes

- [2026-04-21] Early-April Claude Code leak reinforced that harness quality — memory layering, repo-state awareness, permission boundaries, and subagent design — is becoming a core competitive dimension in coding agents
- [2026-04-14] Cursor 3.1 added tiled multi-agent supervision and stronger control-plane UX, reinforcing the shift from AI-enhanced IDEs toward agent workspaces
- [2026-04-21] Added [[tools/orca]] under `agentic-coding-workspace`; open-source worktree IDE centered on parallel agent supervision
- [2026-04-21] Claude Code routines and Codex ongoing-task/computer-use push reinforce a shift from single-loop CLI agents toward supervised, repeatable agent workflows
- [2026-04-10] Cursor Bugbot learned rules: production PR feedback now turns into active review rules; Cursor reports 78.13% resolution across 50,310 public PRs
- [2026-04-10] Added `agent-toolkits` subcategory with [[tools/shopify-ai-toolkit]]
