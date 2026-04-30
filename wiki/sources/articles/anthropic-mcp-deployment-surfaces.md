---
title: Anthropic MCP deployment surfaces
type: source
source_type: article
url: https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop
ingested: 2026-04-23
domains: [agents]
---

# Anthropic MCP deployment surfaces

Anthropic's MCP help material now clearly distinguishes local MCP in Claude Desktop from remote MCP connectors configured through the Claude account. That distinction matters because both paths use MCP, but they have different network and deployment assumptions.

## Influenced pages

- [Model Context Protocol](../../concepts/mcp.md) — practical clarification on local versus remote MCP deployment surfaces across Claude clients

## Key claims extracted

- Claude Desktop supports local MCP servers running on the user's own machine
- Anthropic separately supports remote custom connectors using remote MCP servers
- Remote connectors are brokered through Anthropic's cloud infrastructure, even for clients like Claude Desktop and Cowork
- Local MCP in Claude Desktop remains a separate mechanism from remote connectors
