---
type: proposal
sources:
  - raw/articles/2026-04-24-claudecom-blog-claude-managed-agents-memory.md
  - raw/newsletters/2026-04-24-openai-ships-its-most-agentic-model.md
  - raw/newsletters/2026-04-24-gpt-55-is-here.md
status: pending
created: 2026-04-24
---

# Proposal: Claude Managed Agents Memory

## Summary

Anthropic's Managed Agents memory launch is a meaningful platform update, not just a small feature add. It turns the existing page from "hosted runtime direction" into a clearer product story around durable, inspectable, file-backed memory with enterprise controls, shared stores, rollback, and auditability. This belongs on the current `claude-managed-agents` page and should also slightly strengthen the agent-orchestration state page.

## Intended changes

- [x] **Update** `wiki/tools/claude-managed-agents.md` — add built-in memory details; update `as_of`; prepend `Recent changes`
- [x] **Update** `wiki/state-of/agents.md` — sharpen the `claude-managed-agents` line to include durable memory / shared stores; bump `as_of`
- [x] **Update** `wiki/index.md` — refresh the tool blurb
- [x] **Create** `wiki/sources/articles/claude-managed-agents-memory.md` — source summary

## Page drafts

### wiki/tools/claude-managed-agents.md (update — diff only)

> **Update frontmatter:**
> - `as_of: 2026-04-24`
> - append `claude-managed-agents-memory` to `sources`

> **Add to `## Current status`:**
> ```markdown
> - Built-in memory is now in public beta: memories are mounted as files on the agent filesystem instead of hidden inside a proprietary opaque memory layer
> - Memory stores can be shared across agents with scoped permissions (for example org-wide read-only plus per-user read/write)
> - Changes are tracked with audit logs and surfaced as session events in the Claude Console; developers can roll back or redact prior memory state
> - Anthropic is explicitly pitching memory as a way to replace custom retrieval / memory infrastructure for long-running agent deployments
> ```
>
> **Add to `## Why it matters`:**
> ```markdown
> Anthropic is making a strong product bet on inspectable file-backed memory rather than magical hidden persistence. That matters because it keeps memory legible to developers, reviewable for enterprise governance, and compatible with the same bash/code tools agents already use.
> ```
>
> **Add to `## Recent changes` (prepend):**
> `- [2026-04-24] Built-in memory launched in public beta: file-backed stores, scoped sharing, audit logs, rollback/redaction controls, and Claude Console event visibility`

### wiki/state-of/agents.md (update — diff only)

> **Update the `claude-managed-agents` line under `### Agent orchestration`:**
> ```markdown
> - [[tools/claude-managed-agents]] — Anthropic's hosted runtime; separates session, harness, sandbox, and now file-backed built-in memory with shared stores and auditability *(as of 2026-04-24)*
> ```
>
> **Add to `## Recent changes` (prepend):**
> `- [2026-04-24] Claude Managed Agents added built-in file-backed memory with shared stores, audit logs, and rollback controls; Anthropic's hosted-runtime story is becoming a more opinionated durable-agent platform`

### wiki/index.md (update — diff only)

> **Update the `tools/claude-managed-agents` line:**
> ```markdown
> - [[tools/claude-managed-agents]] — Anthropic's hosted long-horizon agent runtime; now adds file-backed built-in memory with shared stores and enterprise audit controls *(as_of: 2026-04-24)*
> ```

### wiki/sources/articles/claude-managed-agents-memory.md (new)

````md
---
title: Built-in memory for Claude Managed Agents
type: source
source_type: article
source_file: raw/articles/2026-04-24-claudecom-blog-claude-managed-agents-memory.md
url: https://claude.com/blog/claude-managed-agents-memory
published: 2026-04-24
ingested: 2026-04-24
domains: [agents]
---

# Built-in memory for Claude Managed Agents

Anthropic's memory launch for Managed Agents. The key signal is architectural and operational: memory is file-backed, shared across agents with explicit scopes, auditable, and controllable through rollback/redaction rather than treated as a hidden platform primitive.

## Influenced pages

- [[tools/claude-managed-agents]] — durable memory becomes a first-class part of the product story
- [[state-of/agents]] — strengthens Anthropic's hosted agent-platform position

## Key claims extracted

- Managed Agents memory is in public beta
- Memories are stored as files mounted on the filesystem
- Stores can be shared across agents with different access scopes
- Developers get audit logs, rollback, redaction, and Claude Console visibility into memory updates
- Anthropic positions this as a replacement for custom memory / retrieval infrastructure in long-running agents
````
