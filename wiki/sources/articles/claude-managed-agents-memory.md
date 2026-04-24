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
