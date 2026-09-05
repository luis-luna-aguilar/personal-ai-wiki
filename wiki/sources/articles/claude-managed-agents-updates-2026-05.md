---
title: "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels"
type: source
source_type: article
source_file: raw/articles/2026-08-25-claudecom-blog-claude-managed-agents-updates.md
url: https://claude.com/blog/claude-managed-agents-updates
published: 2026-05-20
ingested: 2026-08-25
domains: [agents]
---

# New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Anthropic's official Claude Managed Agents blog post announcing two features unveiled at Code with Claude London: self-hosted sandboxes (public beta) and MCP tunnels (research preview). Self-hosted sandboxes let a Managed Agent execute tools on the customer's own infrastructure or a supported managed provider (Cloudflare, Daytona, Modal, Vercel) while Anthropic's hosted agent loop still handles orchestration, context management, and error recovery. MCP tunnels let agents reach MCP servers inside a private network — via a lightweight customer-deployed gateway — without exposing them to the public internet.

## Influenced pages
- [Claude Managed Agents](../../tools/claude-managed-agents.md) — added self-hosted sandboxes and MCP tunnels to current status
- [Harness (agent)](../../concepts/harness.md) — extended the managed-agent-platform-primitives pattern with this example

## Key claims extracted
- Self-hosted sandboxes: public beta; MCP tunnels: research preview (request access via a Claude form)
- Supported sandbox providers: Cloudflare, Daytona, Modal, Vercel; named customer examples for three of them — Amplitude (Cloudflare), Clay (Daytona), Rogo (Vercel)
- Sandbox provisioning, resource sizing, and runtime image are controlled by the customer
- MCP tunnels supported in both Managed Agents and the Messages API; managed from Claude Console workspace settings by org admins
- No inbound firewall rules or public endpoints required for MCP tunnels; traffic is encrypted end to end
