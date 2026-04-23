---
title: Introducing the new hosted agents in Foundry Agent Service: secure, scalable compute built for agents
type: source
source_type: article
url: https://devblogs.microsoft.com/foundry/introducing-the-new-hosted-agents-in-foundry-agent-service-secure-scalable-compute-built-for-agents/
fetched: 2026-04-23
---

# Introducing the new hosted agents in Foundry Agent Service: secure, scalable compute built for agents

Agents are already transforming how developers solve problems. Whether it’s a coding agent that refactors your repo overnight, a research agent that synthesizes hundreds of documents into a brief, or an ops agent that monitors and remediates infrastructure — the pattern is clear. Developers are building agents that don’t just answer questions, they go do things.

Agents of today don’t just execute from a list of tools. They access the underlying file system, write and execute code, and persist files and memories for long running and complex tasks.

Today, it is easy to build agents locally. But how do you take that same power and patterns, and deploy it across an enterprise? How do you make it serve thousands of customer conversations securely? How do you give it an identity, govern its access, and observe what it’s doing at scale?

That’s what Microsoft Foundry is releasing today. Today we’re announcing [**hosted agents** **in Foundry Agent Service**](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents?view=foundry), now in public preview. This brings agent-optimized compute and services designed for production-grade enterprise agents. We first previewed hosted agents last year at Microsoft Ignite, but this refresh is a fundamentally different experience: secure per-session sandboxes with filesystem persistence, integrated identity, and scale-to-zero economics.

Convert to GIF project image, image

### **What we’re shipping** Copy link

Hosted agents gives every single agent session its own dedicated, isolated sandbox with a persistent file system. Not process isolation. Not a code execution-only sandbox. Production-proven hypervisor isolation, at cloud scale.

**Core Capabilities:**

* **Predictable cold starts** — spin up agent sessions and harnesses in your custom environment virtually instantly
* **Scale to zero** — pay nothing while your agent is idle, with an agent that will scale down on its own during inactivity
* **Resume with filesystem intact** — files, disk state, and session identity persist across scale-to-zero events. Your agent restarts with its full working directory exactly where it left off
* **Per-session isolation is automatic** — Every single agent session its own VM-isolated sandbox with persistent session state. Use isolation keys to easily manage and namespace your end users’ sessions
* **BYO VNet Support –** drive your agents’ outbound traffic via your VNet
* **Production-ready agent endpoints –** built-in agent versioning with stable endpoints for easy integration, weighted rollouts across versions
* **Multiple protocols out of the box –** OpenResponses protocol support with automatic mapping to/from Activity Protocol for one-click publish to Microsoft 365. Flexible Invocations protocol for custom application integrations, AG-UI support

### **A platform built for agents** Copy link

The problem with traditional compute is that it wasn’t designed for this pattern. Containers, web apps, serverless functions – these were built for web services and APIs where multiple users share the same instance. That’s fine for web apps, but doesn’t work for agents.

When Customer A and Customer B are both calling the same agent — and that agent is writing files, executing code, and accessing credentials on a shared instance — you have a security and isolation nightmare. Agent harnesses need to read and write state. They execute arbitrary code. They hold sensitive context. Sharing a container across sessions isn’t just inefficient, it’s unsafe.

The hard part is no longer writing the agent. The hard part is making it enterprise-ready at scale — with real isolation, real identity, and real governance. That’s our focus with Microsoft Foundry.

|  | **Traditional Compute** | **Hosted Agents** |
| --- | --- | --- |
| **Isolation** | Multiple sessions share a container | Every session gets a dedicated sandbox |
| **Cold starts** | Seconds to minutes (high variance) | Seconds (low variance, predictable) |
| **Idle cost** | Always-on billing or slow scale-from-zero | Scale to zero with filesystem-preserving resume |
| **State persistence** | You build it (databases, external storage) | Built in — files and disk state survive scale-to-zero |
| **Identity** | Shared service account | Per-agent identity + per-user (OBO) |
| **Observability** | You build it | Built in (agent, session, fleet) |

### **Bring any harness, any framework, any environment** Copy link

Rather than locking you into a specific harness or runtime, Foundry lets you bring whatever works best for your agent. Use LangGraph, Microsoft Agent Framework, Claude Agent SDK, OpenAI Agents SDK, the GitHub Copilot SDK — any framework you want. Define the optimal environment for your agent with a Dockerfile, so it has exactly the tools and dependencies it needs to get the job done. Deploy in one command (azd deploy). Microsoft Foundry will take care of running your agent at scale.

This flexibility is the point. Unlike platforms that force one model and one harness, Foundry is multi-model and multi-harness by design. Run models from OpenAI, Anthropic, Meta, Mistral, and more. Bring any orchestration framework. No lock-in.

### **More than compute — a complete agent platform** Copy link

Hosted agents aren’t just infrastructure. They’re integrated with the full Microsoft Foundry platform, including [announcements](https://aka.ms/DeployingAgents-blog) we’re making alongside this refresh:

* **Toolbox (public preview)** — a unified way to configure and manage tools across any framework – using progressive disclosure to preserve context and tokens. Build once, connect any MCP client to the same endpoint. Built-in auth handling, OAuth identity passthrough, and observability for every tool call.
* **Memory (preview)** — managed long-term memory built directly into Foundry Agent Service. Agents remember context across sessions — no external databases to provision. Now natively integrated with Microsoft Agent Framework and LangGraph.
* **Microsoft Agent Framework v1.0** — the stable, production-ready agent framework that unifies the foundations of Semantic Kernel and AutoGen. Build locally, deploy to hosted agents seamlessly.
* **Observability** — end-to-end tracing based on OpenTelemetry, AI Red Teaming Agent for adversarial testing, and continuous evaluation — all in one platform.

And the enterprise capabilities that make this production-ready:

* **Identity**: Every agent gets its own Entra Agent ID and acts on behalf of users via OBO with a continuous audit trail. No more shared service accounts.
* **Governance**: DLP policies, Responsible AI guardrails, and with VNet integration
* **Context**: Agents connect to Work IQ (M365 data), Fabric IQ (business data), and Foundry IQ (curated knowledge and search). Helping you bring your enterprise context graph to any agent with ease.
* **Distribution**: Publish agents directly to Teams and M365 Copilot — where your users already work.

This is the combination that only Microsoft Foundry can offer: agent-optimized compute and services, integrated with thousands of tools, any model, any harness — all with secure sandboxing, persistence, and enterprise identity.

### **What’s next** Copy link

The foundation is in place: agent-optimized compute, secure sandboxes, filesystem persistence, enterprise identity, and deep platform integration. But we’re just getting started.

Your meeting-prep agent shouldn’t start from scratch every Monday. The 10th briefing it writes should build on the previous 9 — already knowing which metrics your VP cares about, which format she prefers, which data sources matter. Context should compound automatically. We’re investing deeply in making agents self-optimizing and long-running — agents that persist state, accumulate context, and improve across every interaction, all in a secure environment that’s enterprise-ready. More to come here soon.

We’re working hard to get this preview into General Availability soon. And we’ll keep building the platform that makes every agent — regardless of model, framework, or harness — production-ready for the enterprise.

### Get Started Copy link
