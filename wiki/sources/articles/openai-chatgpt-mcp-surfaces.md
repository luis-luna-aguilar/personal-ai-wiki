---
title: OpenAI and ChatGPT MCP surfaces
type: source
source_type: article
url: https://developers.openai.com/api/docs/guides/tools-connectors-mcp
ingested: 2026-04-23
domains: [agents]
---

# OpenAI and ChatGPT MCP surfaces

OpenAI's current MCP documentation emphasizes remote MCP servers and connectors, while ChatGPT's help docs describe user-built integrations as apps/connectors built with MCP. The current shape is remote-first rather than localhost-desktop-first.

## Influenced pages

- [Model Context Protocol](../../concepts/mcp.md) — practical note that OpenAI/ChatGPT currently point more toward remote MCP deployment than local-only desktop attachment

## Key claims extracted

- OpenAI's API docs describe remote MCP servers as publicly reachable MCP services used through the Responses API
- OpenAI also distinguishes remote MCP servers from OpenAI-maintained connectors
- ChatGPT's help docs describe custom integrations as apps/connectors built with MCP
- The current documented shape is remote-first, not a Claude-Desktop-style local MCP setup
