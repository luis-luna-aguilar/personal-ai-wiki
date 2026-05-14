---
title: State of Coding
type: state-of
domains: [coding]
tags: []
as_of: 2026-05-13
sources: [sdd-3-tools-fowler, cursor-3-launch, stripe-cli, claude-code-monitor, openai-pro-100, cursor-pr-demos, shopify-ai-toolkit, cursor-bugbot-learning, claude-code-routines, openai-codex-ongoing-tasks, orca-homepage, coding-agent-control-planes, claude-code-leak-architecture, cursor-3-orchestration-bet, skills-and-plugin-packaging-late-march, cursor-cloud-agents-march, claude-code-scheduled-tasks-march, codex-security-march, agentic-devops-deep-research, cursor-sdk-agent-runtime-2026-04-30, symphony-devin-terminal-orchestration-2026-04-28, end-of-finetuning-debate-2026-05-13, claude-code-goal-fastmode-fleetview-2026-05-13, claude-code-agent-view-2026-05-13, model-harness-fit-2026-05-13]
---

# State of Coding

Current state of AI tools for software development. Organized by subcategory — each subcategory can have multiple top players. Ambiguity is expected.

## Subcategories

### Spec-driven development

Tools where a structured natural-language spec is the primary input to AI coding agents. The term is contested and the field is early — no clear leader. See [Spec-Driven Development (SDD)](../concepts/spec-driven-development.md) for the concept and taxonomy.

- [Kiro](../tools/kiro.md) — VS Code-based; requirements → design → tasks; lightest-weight, mostly spec-first *(as of 2025-10-15)*
- [spec-kit](../tools/spec-kit.md) — GitHub; CLI scaffolder + slash commands; constitution → specify → plan → tasks; most customizable *(as of 2025-10-15)*
- [Tessl Framework](../tools/tessl.md) — CLI + MCP server; only tool pursuing spec-as-source; private beta *(as of 2025-10-15)*

### Agentic coding workspace

Coding tools whose primary UI is built around managing one or more AI coding agents (local and cloud), rather than file-centric editing with AI assistance bolted on.

- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK now exposes the runtime headlessly for CI, automations, cloud VMs, and embedded product agents; 35% of Cursor's internal PRs from cloud agents *(as of 2026-04-30)*
- [Orca](../tools/orca.md) — Open-source worktree IDE for running Claude Code, Codex, and other coding agents side by side with built-in terminals, file review, diff review, and CI/PR status tracking *(as of 2026-04-21)*

### Agentic DevOps

Tools that move AI coding systems closer to full software delivery by covering provisioning, diagnosis, deployment safety, and post-deploy verification rather than code generation alone.

- [Stripe CLI](../tools/stripe-cli.md) — provisioning-first example: agent-compatible CLI for standing up and managing app-stack services across providers *(as of 2026-04-09)*
- [K8sGPT](../tools/k8sgpt.md) — diagnosis surface for Kubernetes-heavy software teams; useful when coding-agent output needs operational interpretation and triage *(as of 2026-04-24)*
- [Skyflo](../tools/skyflo.md) — strongest current example of approval-gated execution for infrastructure mutations triggered from natural-language operational intent *(as of 2026-04-24)*
- [Checkly](../tools/checkly.md) — post-deploy verification layer that turns Playwright/browser checks into continuous synthetic validation *(as of 2026-04-24)*

### Terminal coding agent

CLI-based AI coding agents that still anchor in the terminal, but are increasingly expanding into supervised workspaces with repeatable workflows, background execution, and broader agent control surfaces.

- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: `/goal` autonomous loops, Opus 4.7 fast mode, and Agent View (`claude agents`) multi-session supervision with `/bg` and `claude --bg` *(as of 2026-05-13)*
- [Codex](../tools/codex.md) — OpenAI; cloud coding agent via CLI and ChatGPT, but current direction increasingly spills into browser work, documents, spreadsheets, and broader computer-use-style workflows *(as of 2026-04-24)*

### Agent toolkits

Toolkits that package a developer platform's docs, schemas, validation, and related capabilities for AI coding tools via plugins, skills, or MCP.

- [Shopify AI Toolkit](../tools/shopify-ai-toolkit.md) — Shopify packages platform docs, API schemas, and validation for Claude Code, Codex, Cursor, Gemini CLI, and VS Code via plugin, skills, or local Dev MCP; Codex support is skills/MCP only *(as of 2026-04-10)*

## Recent changes

- [2026-05-13] Model-harness fit is becoming a product moat: edit formats, action spaces, and tool-call reliability can matter as much as raw model benchmark scores in coding agents.
- [2026-05-13] Codex and Claude Code are increasingly framed as workflow operating systems: command packs, browser-pane workflows, inbox triage, long-running goals, and multi-agent supervision are now part of the coding-agent competition.
- [2026-05-13] Cognition $25B valuation round publicly confirmed; among top-tier coding shops increasing open-model RLFT investment (not decreasing) alongside OpenAI finetuning API deprecation
- [2026-05-05] OpenAI Symphony: open-source Codex orchestration spec for defining, invoking, and coordinating Codex subagents; issue-queue integration as the input surface (secondary coverage; verify against primary OpenAI documentation)
- [2026-05-05] Devin for Terminal: Cognition AI's shell-native agent with local codebase/tool access and cloud handoff for longer tasks; reinforces terminal as a first-class coding orchestration surface
- [2026-04-30] Cursor SDK released: TypeScript SDK exposes the Cursor agent runtime headlessly for CI pipelines, server automations, cloud VMs, MCP servers, and embedded product agents; Cursor expanding from IDE seat product toward programmable agent infrastructure
- [2026-04-24] Broadened `agentic-devops` from provisioning-only CLI workflows toward a fuller infrastructure-operations stack: diagnosis, approval-gated mutation, and post-deploy verification
- [2026-04-24] Codex's April direction now reads less like "coding with extras" and more like a broader computer-work agent that still happens to be anchored in software workflows
- [2026-03-06] Cursor's cloud-agents walkthrough made the workspace thesis explicit: remote agents test their own work, return demo videos, and give humans a supervision surface rather than just an AI-enhanced editor
- [2026-03-07] Claude Code added local scheduled tasks and `/loop`, making recurring background coding work a first-class terminal-agent primitive
