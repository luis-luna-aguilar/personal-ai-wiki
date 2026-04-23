---
title: Model Context Protocol
type: concept
domains: [agents]
tags: [anthropic]
as_of: 2026-04-22
sources: [anthropic-mcp, legacy-ai-tools-roadmap-xlsx]
---

# Model Context Protocol

Model Context Protocol, usually shortened to MCP, is an open protocol for exposing tools, resources, and prompts to AI hosts and agents through a standard interface. Anthropic introduced it, but the practical significance is broader: MCP turns many bespoke agent integrations into a reusable connector layer.

## Current status (as of 2026-04-22)

- Originated by Anthropic as an open standard for connecting assistants to external systems
- Increasingly treated as shared infrastructure rather than a vendor-specific feature
- Useful for both local and hosted agent systems because it standardizes tool discovery and invocation

## Why it matters

- Replaces one-off tool glue with a protocol-level integration surface
- Makes it easier for ecosystems to share integrations across hosts
- Helps separate the agent harness problem from the underlying model problem

## Sources

- [[sources/articles/anthropic-mcp]]
- [[sources/notes/legacy-ai-tools-roadmap-xlsx]]

