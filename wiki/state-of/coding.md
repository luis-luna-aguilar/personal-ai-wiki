---
title: State of Coding
type: state-of
domains: [coding]
tags: []
as_of: 2026-04-24
sources: [sdd-3-tools-fowler, cursor-3-launch, stripe-cli, claude-code-monitor, openai-pro-100, cursor-pr-demos, shopify-ai-toolkit, cursor-bugbot-learning, claude-code-routines, openai-codex-ongoing-tasks, orca-homepage, coding-agent-control-planes, claude-code-leak-architecture, cursor-3-orchestration-bet, skills-and-plugin-packaging-late-march, cursor-cloud-agents-march, claude-code-scheduled-tasks-march, codex-security-march, agentic-devops-deep-research]
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

- [[tools/cursor]] — Cursor 3 is a full rewrite as a cloud-agent orchestration platform; 35% of Cursor's internal PRs now from autonomous cloud agents; 2:1 agent-to-Tab users; Truell defines this as the "third era" where cloud agents run independently and developers review artifacts, not diffs *(as of 2026-04-22)*
- [[tools/orca]] — Open-source worktree IDE for running Claude Code, Codex, and other coding agents side by side with built-in terminals, file review, diff review, and CI/PR status tracking *(as of 2026-04-21)*

### Agentic DevOps

Tools that move AI coding systems closer to full software delivery by covering provisioning, diagnosis, deployment safety, and post-deploy verification rather than code generation alone.

- [[tools/stripe-cli]] — provisioning-first example: agent-compatible CLI for standing up and managing app-stack services across providers *(as of 2026-04-09)*
- [[tools/k8sgpt]] — diagnosis surface for Kubernetes-heavy software teams; useful when coding-agent output needs operational interpretation and triage *(as of 2026-04-24)*
- [[tools/skyflo]] — strongest current example of approval-gated execution for infrastructure mutations triggered from natural-language operational intent *(as of 2026-04-24)*
- [[tools/checkly]] — post-deploy verification layer that turns Playwright/browser checks into continuous synthetic validation *(as of 2026-04-24)*

### Terminal coding agent

CLI-based AI coding agents that still anchor in the terminal, but are increasingly expanding into supervised workspaces with repeatable workflows, background execution, and broader agent control surfaces.

- [[tools/claude-code]] — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: Monitor, Routines, /ultrareview, --worktree, Remote Control, and /autofix-pr all shipped since March; harness architecture increasingly treated as core competitive differentiator *(as of 2026-04-23)*
- [[tools/codex]] — OpenAI; cloud coding agent via CLI and ChatGPT, but current direction increasingly spills into browser work, documents, spreadsheets, and broader computer-use-style workflows *(as of 2026-04-24)*

### Agent toolkits

Toolkits that package a developer platform's docs, schemas, validation, and related capabilities for AI coding tools via plugins, skills, or MCP.

- [[tools/shopify-ai-toolkit]] — Shopify packages platform docs, API schemas, and validation for Claude Code, Codex, Cursor, Gemini CLI, and VS Code via plugin, skills, or local Dev MCP; Codex support is skills/MCP only *(as of 2026-04-10)*

## Recent changes

- [2026-04-24] Broadened `agentic-devops` from provisioning-only CLI workflows toward a fuller infrastructure-operations stack: diagnosis, approval-gated mutation, and post-deploy verification
- [2026-04-24] Codex's April direction now reads less like "coding with extras" and more like a broader computer-work agent that still happens to be anchored in software workflows
- [2026-03-06] Cursor's cloud-agents walkthrough made the workspace thesis explicit: remote agents test their own work, return demo videos, and give humans a supervision surface rather than just an AI-enhanced editor
- [2026-03-07] Claude Code added local scheduled tasks and `/loop`, making recurring background coding work a first-class terminal-agent primitive
- [2026-03-09] Codex Security expanded Codex from code generation into vulnerability review and validation
- [2026-03-23] Late-March signals suggest skills, plugins, hooks, and related packaging are solidifying into the core abstraction layer for coding agents rather than remaining scattered configuration details
- [2026-04-21] Early-April Claude Code leak reinforced that harness quality — memory layering, repo-state awareness, permission boundaries, and subagent design — is becoming a core competitive dimension in coding agents
- [2026-04-14] Cursor 3.1 added tiled multi-agent supervision and stronger control-plane UX, reinforcing the shift from AI-enhanced IDEs toward agent workspaces
- [2026-04-21] Added [[tools/orca]] under `agentic-coding-workspace`; open-source worktree IDE centered on parallel agent supervision
- [2026-04-21] Claude Code routines and Codex ongoing-task/computer-use push reinforce a shift from single-loop CLI agents toward supervised, repeatable agent workflows
- [2026-04-10] Cursor Bugbot learned rules: production PR feedback now turns into active review rules; Cursor reports 78.13% resolution across 50,310 public PRs
- [2026-04-10] Added `agent-toolkits` subcategory with [[tools/shopify-ai-toolkit]]
- [2026-04-22] Cursor 3 confirmed as cloud-agent orchestration bet: 35% internal PRs from cloud agents, 2:1 agent-to-Tab user ratio per Truell essay
- [2026-04-22] Moved Codex Security (vulnerability review/validation) to [[state-of/cybersecurity]]; slopsquatting documented there
