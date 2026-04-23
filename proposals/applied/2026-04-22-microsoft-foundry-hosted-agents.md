---
type: proposal
sources:
  - raw/articles/2026-04-23-devblogsmicrosoftcom-foundry-introducing-the-new-hosted-agen.md
  - raw/articles/2026-04-22-devblogsmicrosoftcom-foundryintroducing-the-new-hos.md
status: applied
created: 2026-04-23
---

# Proposal: Microsoft Foundry Hosted Agents

## Summary

Microsoft launched hosted agents in Foundry Agent Service (public preview). The core architectural differentiator: every agent session gets its own **hypervisor-isolated VM sandbox** with a **persistent filesystem that survives scale-to-zero** — not container sharing, not a code-execution-only sandbox. This solves credential/state leakage between enterprise users, a problem that container-shared agents don't address. The platform is multi-framework (LangGraph, MSAF v1.0, Claude Agent SDK, OpenAI Agents SDK, GitHub Copilot SDK) and multi-model, with full governance stack (per-agent Entra Agent ID, Toolbox/MCP, Memory, Agent Registry, Agent Gateway + Model Armor, AP2 payments). Already in production at Comcast, L'Oréal, PayPal, Color Health, and Payhawk. Establishes Microsoft as a third major player in enterprise agent orchestration infrastructure alongside Google Cloud and Anthropic/AWS.

## Intended changes

- [x] **Create** `wiki/tools/microsoft-foundry-agents.md` — new tool page
- [x] **Update** `wiki/state-of/agents.md` — add Microsoft Foundry under agent-orchestration subcategory; prepend Recent changes entry
- [x] **Create** `wiki/sources/articles/microsoft-foundry-agents-2026.md` — source summary

## Page drafts

### wiki/tools/microsoft-foundry-agents.md (new)

````md
---
title: Microsoft Foundry Hosted Agents
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [microsoft, agentic]
as_of: 2026-04-23
sources: [microsoft-foundry-agents-2026]
---

# Microsoft Foundry Hosted Agents

Microsoft's enterprise agent orchestration platform. Launched in public preview April 2026 as part of Foundry Agent Service. Core design: every agent session receives its own hypervisor-isolated VM sandbox with a persistent filesystem that survives scale-to-zero — solving the credential and state leakage problem that plagues container-shared agent deployments.

## Current status (as of 2026-04-23)

**Core compute model:**
- Per-session hypervisor VM isolation (not container sharing, not code-execution-only sandbox)
- Persistent filesystem across scale-to-zero events: files, disk state, and session identity are preserved; agent restarts exactly where it left off
- Predictable cold starts (seconds, low variance)
- Scale-to-zero with resume intact — pay nothing while idle
- Isolation keys for session namespace management per end user
- BYO VNet for outbound traffic routing
- Weighted version rollouts across agent versions
- AG-UI, OpenResponses, and flexible Invocations protocol support

**Identity and governance:**
- Per-agent **Entra Agent ID** — every agent gets a unique identity; no more shared service accounts
- Per-user OBO (on-behalf-of) with continuous audit trail
- DLP policies and Responsible AI guardrails built in
- **Agent Gateway** — policy enforcement layer with Model Armor against prompt injection and data leakage
- OpenTelemetry-based observability (agent, session, fleet)

**Platform components:**
- **Toolbox** (public preview) — unified MCP-compatible tool management; build once, connect any MCP client to the same endpoint; built-in OAuth passthrough and per-call observability
- **Memory** (preview) — managed long-term memory native to Foundry Agent Service; agents remember context across sessions; integrated with Microsoft Agent Framework and LangGraph
- **Microsoft Agent Framework v1.0** — stable production-ready framework that unifies Semantic Kernel and AutoGen; build locally, deploy to hosted agents in one command
- **Agent Registry** (from platform announcements alongside this launch) — central governance catalog
- **Agent Payment Protocol (AP2)** — trusted agent payment flows

**Multi-framework / multi-model:**
- Supported frameworks: LangGraph, Microsoft Agent Framework v1.0, Claude Agent SDK, OpenAI Agents SDK, GitHub Copilot SDK
- Multi-model: OpenAI, Anthropic, Meta, Mistral, and more
- Dockerfile-defined custom agent environments; `azd deploy` for one-command deployment
- Framework-agnostic: no lock-in to a specific harness or model

**Enterprise context integrations:**
- Work IQ (M365/Microsoft 365 data)
- Fabric IQ (business data)
- Foundry IQ (curated knowledge and search)
- Distribution: publish directly to Teams and M365 Copilot

**Production deployments:**
- Comcast Xfinity: conversational customer support replacing scripted automation
- L'Oréal Beauty Tech: MCP-connected to their data platform; multi-LLM
- PayPal: agent payment flows via AP2
- Color Health: breast cancer screening eligibility and appointment scheduling
- Payhawk: Financial Controller Agent that auto-submits expenses, 50%+ faster submission

## Strengths

- Hypervisor-VM-per-session isolation is a genuine architectural advance over container-shared deployments for enterprise security requirements
- Multi-framework / multi-model stance avoids the lock-in that single-model platforms create
- Entra Agent ID gives each agent a verifiable, auditable identity — critical for enterprise governance
- Scale-to-zero with filesystem persistence reduces cost without sacrificing state continuity

## Weaknesses / caveats

- Public preview — not yet GA; pricing not fully disclosed
- Hosted agents are deeply integrated with Azure/Microsoft infrastructure; "BYO VNet" helps, but non-Azure shops face more friction
- Production customer list overlaps heavily with Google's Gemini Enterprise Agent Platform announcements (Comcast, L'Oréal, PayPal, Payhawk) — the competitive positioning between these platforms is still developing

## Recent changes

- [2026-04-23] Launched in public preview: per-session VM isolation, persistent filesystem, Entra Agent ID, Toolbox (MCP), Memory, multi-framework/multi-model support
````

### wiki/state-of/agents.md (update — diff only)

> **Before** (Agent orchestration section — add after existing entries):
>
> *(add new bullet under agent-orchestration subcategory)*
> ```markdown
> - [[tools/microsoft-foundry-agents]] — Microsoft; per-session hypervisor VM isolation with persistent filesystem; Entra Agent ID per agent; Toolbox (MCP), Memory, Agent Gateway (Model Armor); multi-framework (LangGraph, MSAF v1.0, Claude/OpenAI/Copilot SDKs); multi-model *(as of 2026-04-23)*
> ```

> **Add to `## Recent changes` (prepend):**
> ```markdown
> - [2026-04-23] Microsoft Foundry Hosted Agents (public preview): per-session hypervisor VM sandboxes with persistent filesystem, Entra Agent ID governance, multi-framework/multi-model stance — establishes Microsoft as third major enterprise agent infrastructure player alongside Google and Anthropic/AWS
> ```

### wiki/sources/articles/microsoft-foundry-agents-2026.md (new)

````md
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

Microsoft Foundry announcement blog for hosted agents in Foundry Agent Service (public preview). Full technical post explaining the per-session VM isolation architecture, platform component stack, and production deployments.

## Influenced pages

- [[tools/microsoft-foundry-agents]] — primary source for all tool page content
- [[state-of/agents]] — agent-orchestration subcategory entry

## Key claims extracted

- Every session: dedicated hypervisor-isolated VM sandbox with persistent filesystem (not container sharing)
- Scale-to-zero with filesystem-preserving resume
- Per-agent Entra Agent ID; per-user OBO with audit trail
- Supported frameworks: LangGraph, MSAF v1.0 (Semantic Kernel + AutoGen unified), Claude Agent SDK, OpenAI Agents SDK, GitHub Copilot SDK
- Toolbox: unified MCP endpoint with OAuth passthrough and per-call observability
- Memory: managed long-term memory; integrated with MSAF and LangGraph
- Agent Gateway: Model Armor against prompt injection and data leakage
- Production: Comcast Xfinity, L'Oréal (MCP-connected, multi-LLM), PayPal (AP2), Color Health, Payhawk (50%+ faster expense submission)
````
