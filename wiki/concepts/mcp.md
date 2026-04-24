---
title: Model Context Protocol
type: concept
domains: [agents]
tags: [anthropic]
as_of: 2026-04-23
sources: [anthropic-mcp, legacy-ai-tools-roadmap-xlsx, anthropic-mcp-deployment-surfaces, openai-chatgpt-mcp-surfaces, anthropic-mcp-production-systems]
---

# Model Context Protocol

Model Context Protocol, usually shortened to MCP, is an open protocol for exposing tools, resources, and prompts to AI hosts and agents through a standard interface. Anthropic introduced it, but the practical significance is broader: MCP turns many bespoke agent integrations into a reusable connector layer.

## Current status (as of 2026-04-23)

- Originated by Anthropic as an open standard for connecting assistants to external systems
- Increasingly treated as shared infrastructure rather than a vendor-specific feature
- Useful for both local and hosted agent systems because it standardizes tool discovery and invocation
- Anthropic's April 2026 guidance sharpens the practical choice: direct APIs fit narrow bespoke integrations, CLIs fit permissive local shell environments, and MCP fits reusable cross-client integrations with richer semantics
- Anthropic also argues that production agents increasingly run in the cloud, which makes remote MCP the compounding integration layer even when mature stacks still ship API, CLI, and MCP surfaces together
- Deployment surface now matters in practice, not just protocol support: Claude Desktop supports local MCP servers on the user's machine, while Anthropic's remote custom connectors are a separate cloud-brokered path
- OpenAI's current MCP docs center on remote MCP servers and connectors, and ChatGPT's current help docs frame user-built integrations as MCP-based apps/connectors rather than localhost-only desktop attachments

## Why it matters

- Replaces one-off tool glue with a protocol-level integration surface
- Makes it easier for ecosystems to share integrations across hosts
- Helps separate the agent harness problem from the underlying model problem
- It is increasingly not just a transport layer but a design surface: Anthropic now explicitly recommends remote servers, intent-grouped tools, richer semantics like inline UI and elicitation, and skills layered on top of MCP rather than treated as a separate concern
- In practice, MCP strategy now splits into local-first and remote-first deployment. Local MCP is the straightforward path for Claude Desktop; ChatGPT-style custom integrations currently point more toward publicly reachable remote MCP servers or connector/app surfaces

## Sources

- [[sources/articles/anthropic-mcp]]
- [[sources/notes/legacy-ai-tools-roadmap-xlsx]]
- [[sources/articles/anthropic-mcp-deployment-surfaces]]
- [[sources/articles/openai-chatgpt-mcp-surfaces]]
- [[sources/articles/anthropic-mcp-production-systems]]
