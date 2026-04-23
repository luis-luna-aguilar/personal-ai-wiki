---
title: Introducing the new hosted agents in Foundry Agent Service
type: source
source_type: article
source_file: raw/articles/2026-04-23-devblogsmicrosoftcom-foundry-introducing-the-new-hosted-agen.md
url: https://devblogs.microsoft.com/foundry/introducing-the-new-hosted-agents-in-foundry-agent-service-secure-scalable-compute-built-for-agents/
published: 2026-04-23
ingested: 2026-04-23
domains: [agents]
---

# Introducing the new hosted agents in Foundry Agent Service

Microsoft's Foundry launch post for hosted agents in public preview. The key signal is architectural: hosted agents are framed as isolated per-session VM environments with persistent disk state, wrapped in Microsoft's enterprise identity, governance, and tool-management stack.

## Influenced pages

- [[tools/microsoft-foundry-agents]] — new tool page for Microsoft's hosted enterprise agent runtime
- [[state-of/agents]] — adds Microsoft to `Agent orchestration`

## Key claims extracted

- Every session gets a dedicated hypervisor-isolated VM sandbox with a persistent filesystem
- Sessions can scale to zero and later resume with files and state intact
- Each agent gets its own Entra Agent ID; per-user OBO access is supported with auditability
- Toolbox provides MCP-compatible tool management with OAuth passthrough and per-call observability
- Memory, Agent Gateway / Model Armor, Agent Registry, and AP2 expand the platform beyond raw execution
- Supported frameworks include LangGraph, Microsoft Agent Framework v1.0, Claude Agent SDK, OpenAI Agents SDK, and GitHub Copilot SDK
