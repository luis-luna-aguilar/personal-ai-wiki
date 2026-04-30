---
title: Building agents that reach production systems with MCP
type: source
source_type: article
source_file: raw/articles/Building agents that reach production systems with MCP _ Claude.pdf
url: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
published: 2026-04-22
ingested: 2026-04-23
domains: [agents]
---

# Building agents that reach production systems with MCP

Anthropic's April 22 MCP guidance post. It is the clearest current explanation of where direct APIs, CLIs, and MCP each fit in production agent systems, and it adds concrete implementation guidance for remote MCP servers, auth, context-efficient clients, and skills pairing.

## Influenced pages

- [Model Context Protocol](../../concepts/mcp.md) — production guidance for APIs vs CLIs vs MCP; server/client design patterns; skills pairing

## Key claims extracted

- Direct APIs work well for narrow one-agent / one-service integrations but do not scale cleanly as a reusable integration layer
- CLIs are strong in local shell-native environments but do not generalize well to web, mobile, or cloud-hosted agents
- MCP is the shared protocol layer for remote, authenticated, reusable integrations across clients and deployment environments
- Recommended server patterns: build remote servers, group tools around intent, and use code orchestration for very large API surfaces
- Recommended client patterns: tool search and programmatic tool calling to reduce context cost
- Skills complement MCP by encoding procedural knowledge on top of raw capabilities
