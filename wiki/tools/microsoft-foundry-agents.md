---
title: Microsoft Foundry Hosted Agents
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [closed-source, agentic]
as_of: 2026-04-23
sources: [microsoft-foundry-agents-2026]
---

# Microsoft Foundry Hosted Agents

Microsoft Foundry Hosted Agents is Microsoft's hosted enterprise agent runtime inside Foundry Agent Service. The main architectural claim is stronger isolation than the typical shared-container pattern: each agent session gets its own hypervisor-isolated VM sandbox with a persistent filesystem that survives scale-to-zero and resume.

## Current status (as of 2026-04-23)

- Public preview inside Foundry Agent Service
- Per-session hypervisor-isolated VM sandbox rather than container sharing
- Persistent filesystem across scale-to-zero and resume, so agent state and files survive idle periods
- Per-agent Entra Agent ID plus per-user on-behalf-of access and audit trail
- Toolbox adds MCP-compatible tool management with OAuth passthrough and observability
- Memory, Agent Gateway / Model Armor, Agent Registry, and AP2 position it as a full enterprise agent platform rather than only a sandbox runtime
- Supports LangGraph, Microsoft Agent Framework v1.0, Claude Agent SDK, OpenAI Agents SDK, and GitHub Copilot SDK across multiple model providers

## Strengths

- VM-per-session isolation is a meaningful enterprise differentiation versus shared-runtime agent platforms
- Persistent resume plus scale-to-zero is a better state/cost tradeoff than disposable sandboxes
- Multi-framework and multi-model support reduces platform lock-in
- Governance story is unusually complete at launch: identity, policy, observability, and network controls are all first-class

## Weaknesses / caveats

- Still in public preview
- Current evidence is mostly Microsoft's own launch framing rather than independent operator reporting
- Strongest fit is for Azure/Microsoft-centered enterprises; cross-cloud teams may face more friction

## Recent changes

- [2026-04-23] Public preview launch: per-session VM isolation, persistent filesystem, Entra Agent ID, Toolbox, Memory, and multi-framework / multi-model support

## Sources

- [[sources/articles/microsoft-foundry-agents-2026]]
