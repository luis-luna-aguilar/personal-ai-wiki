---
type: proposal
sources:
  - raw/newsletters/2026-07-01-codex-in-practice.md
  - raw/newsletters/2026-06-28-everyone-gets-an-agent-almost-no-one-gets-the-mod.md
status: pending
created: 2026-07-06
---

# Proposal: Codex and Claude Code as general-purpose work agents

## Summary
Every's Codex coverage treats Codex as a workspace for nontechnical work, not only coding. The same digest frames Claude Code and Codex as general agent harnesses spilling into healthcare coordination, CRM cleanup, writing systems, meeting/voice-note processing, and unattended feature work.

## Intended changes

- [x] **Update** `wiki/tools/codex.md` — add nontechnical work examples and clarify general-purpose workspace positioning.
    > **Add to Current status:** Beyond software tasks, Codex is being used as a file/workspace agent for inbox cleanup, CRM enrichment, family healthcare coordination, writing systems, meeting-note processing, and personal folder maintenance.

- [x] **Update** `wiki/tools/claude-code.md` — add note that its terminal-coding interface is increasingly used as a general agent harness.

- [x] **Update** `wiki/state-of/computer-use.md` — add Codex/Claude Code as developer-facing but generalizing computer-work surfaces.

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add guidance to look for agent-harness uses outside the product's nominal category.

- [x] **Create** `wiki/sources/newsletters/codex-general-work-agents-2026-07.md` — source summary.

## Updated Page Snippets

### `wiki/tools/codex.md`

> **Before:**
> `OpenAI's cloud-based agent surface, accessed via CLI and ChatGPT. It started as a coding agent, but current product direction is expanding into a broader computer-work system that can operate across code, browser flows, documents, spreadsheets, and repeatable knowledge-work tasks.`

> **After:**
> `OpenAI's cloud-based agent surface, accessed via CLI, ChatGPT, and mobile. It started as a coding agent, but current product direction is expanding into a broader computer-work system that can operate across code, browser flows, documents, spreadsheets, inboxes, CRM cleanup, healthcare coordination, meeting notes, and repeatable knowledge-work tasks.`

### `wiki/tools/claude-code.md`

> **Before:**
> `Anthropic's terminal-first AI coding agent. Runs in the shell, operates autonomously on files, shell commands, and tool calls, and is expanding toward supervised multi-session workflows.`

> **After:**
> `Anthropic's terminal-first AI coding agent. Runs in the shell, operates autonomously on files, shell commands, and tool calls, and is expanding toward supervised multi-session workflows; users increasingly treat it as a general-purpose agent harness for product, research, and operational work when those workflows can be represented as files, commands, skills, and review artifacts.`

### `wiki/state-of/computer-use.md`

> **Before:**
> `- [Codex](../tools/codex.md) — OpenAI; increasingly positioned as a horizontal computer-work agent for documents, spreadsheets, slides, browser flows, research, planning, and connected workplace apps; current evidence is newsletter synthesis, not yet the primary Codex for Work page *(as of 2026-05-01)*`

> **After:**
> `- [Codex](../tools/codex.md) — OpenAI; increasingly positioned as a horizontal computer-work agent for documents, spreadsheets, slides, browser flows, research, planning, inbox/CRM cleanup, meeting-note workflows, and connected workplace apps; current evidence remains newsletter synthesis *(as of 2026-07-01)*`

### `wiki/training/company-wide-ai-enablement.md`

> **Before:**
> `- **Terminal agents for non-engineering roles.** Claude Code is being used by product managers for roadmap drafting, PRD writing, ticket management, GitHub Projects tracking, and strategy documentation.`

> **After:**
> `- **Terminal and workspace agents for non-engineering roles.** Claude Code and Codex are being used for roadmap drafting, PRD writing, ticket management, GitHub Projects tracking, strategy documentation, inbox cleanup, CRM enrichment, healthcare coordination, and personal knowledge workflows. The category label matters less than whether the work can be represented as durable files, tools, and reviewable artifacts.`

## Page Drafts

### `wiki/sources/newsletters/codex-general-work-agents-2026-07.md` (new)

```md
---
title: Codex and Claude Code as general-purpose work agents
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-01-codex-in-practice.md
published: 2026-07-01
ingested: 2026-07-06
domains: [computer-use, coding, agents, training]
---

# Codex and Claude Code as general-purpose work agents

Every describes Codex as an adaptive workspace for nontechnical builders, with examples spanning inbox cleanup, CRM enrichment, healthcare coordination, writing setups, and personal folders assembled from meetings and voice notes. The June 28 digest adds a broader signal that Codex and Claude Code are spilling beyond software development into general work automation.

## Influenced pages
- [Codex](../../tools/codex.md) — nontechnical work examples
- [Claude Code](../../tools/claude-code.md) — general harness positioning
- [State of Computer Use](../../state-of/computer-use.md) — developer-facing agents used for broader work
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — category-boundary guidance

## Key claims extracted
- Codex is being used for inbox, CRM, healthcare coordination, writing, meeting, and personal knowledge workflows.
- Claude Code and Codex are increasingly used as general-purpose agent harnesses despite coding-oriented branding.
- Every reports its Compound Engineering plugin can run coding agents unattended through feature build, test, and PR creation.
```
