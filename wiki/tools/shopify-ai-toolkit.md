---
title: Shopify AI Toolkit
type: tool
domains: [coding]
subcategory: agent-toolkits
tags: [agentic]
as_of: 2026-04-10
sources: [shopify-ai-toolkit]
---

# Shopify AI Toolkit

Shopify AI Toolkit is Shopify's integration layer for connecting general-purpose AI coding tools to the Shopify platform. Rather than shipping its own coding agent, Shopify packages platform knowledge and actions into formats existing tools already understand: a plugin where supported, installable agent skills, or a local Dev MCP server.

## Current status (as of 2026-04-10)

- Supports Claude Code, Codex, Cursor, Gemini CLI, and Visual Studio Code
- Recommended install path is a plugin when the host tool supports plugins
- Codex support is explicitly limited to **skills and MCP**, not the plugin path
- Manual install options include Shopify-maintained agent skills and a local `@shopify/dev-mcp` server
- Claimed capabilities include Shopify documentation access, API schemas, and code validation
- Dev MCP server runs locally and does not require authentication, according to the docs page

## Strengths

- Meets developers inside the tools they already use instead of requiring a Shopify-owned IDE
- Supports multiple host environments rather than a single blessed assistant
- Gives agents structured platform context instead of relying on ad hoc prompting
- Makes Shopify app development look more legible to agents than "paste docs into context"

## Weaknesses / caveats

- The page is setup-oriented and light on concrete examples of real tasks completed through the toolkit
- No benchmarks, case studies, or quality measurements are provided
- Capability depth is unclear from the docs page alone
- Codex support appears partial relative to plugin-capable hosts

## Recent changes

- [2026-04-10] Page created from Shopify's AI Toolkit docs page

## Sources

- [[sources/articles/shopify-ai-toolkit]]
