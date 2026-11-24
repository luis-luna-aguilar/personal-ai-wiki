---
title: 'DigitalOcean — Introducing Managed Agents: One AI-native stack to power your intelligence'
type: source
source_type: article
source_file: raw/articles/2026-10-26-digitaloceancom-blog-managed-agents-public-preview.md
url: https://www.digitalocean.com/blog/managed-agents-public-preview
published: 2026-09-22
ingested: 2026-10-26
domains: [agents]
---

# DigitalOcean — Introducing Managed Agents

DigitalOcean's product-blog announcement (dated "Updated: September 22, 2026") that Managed Agents leaves private preview for public preview. Two services: Harness Runtime (Firecracker microVM sessions with pause/resume/fork, exec and port-forwarding APIs, built-in Chromium and coding sandbox, support for Claude Code, Codex CLI, OpenCode, Hermes, LangGraph, or custom OCI images) and Action Gateway (16,000+ tools across 500+ providers behind one managed MCP endpoint, credentials brokered outside the sandbox, central permissions and approvals). Argues agent workloads are bursty and bills CPU per second on actual use; publishes a startup/resume/exec benchmark against Fly.io Sprites; previews Insights (run tracing) and Signals (runs to eval/RL feedback).

## Influenced pages
- [DigitalOcean Managed Agents](../../tools/digitalocean-managed-agents.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new line under Agent sandbox / compute infrastructure
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — bring-your-own-harness managed runtimes bullet (moved from Agent runtime platforms)
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — general-cloud entrant, active-CPU billing, fast resume

## Key claims extracted
- Managed Agents is in public preview after a private preview; customers include OpenHands, Qencode, and Amplitude
- Session creation to agent response in under a couple of seconds; paused work resumes in ~300 ms
- Harness Runtime: dedicated Firecracker microVM per session; pause captures files, processes, and context; auto-pause when idle (no outgoing LLM or tool calls)
- Supported harnesses: Claude Code, Codex CLI, OpenCode, Hermes, LangGraph agents, custom OCI images
- Action Gateway: 16,000+ tools across 500+ providers through one managed MCP endpoint; credentials never reach the model or sandbox; per-user OAuth supported; human approval for sensitive operations
- Internal testing: 99.3% accuracy matching agent intent to tool capabilities
- Pricing example: 2 vCPU at 25% average utilisation with 4 GB memory peak costs $0.060/hour vs $0.126 for full allocated capacity
- Benchmark (21 Sept 2026, Codex CLI on gpt-5.5): ready 886 ms, first response 3.3 s, resume 305 ms, resumed response 2.43 s vs 2.47 s running; exec 189 ms vs 79 ms on Fly.io Sprites
- Insights in private preview; Signals coming soon
- Qencode support-triage agent: an estimated 4–8 hours/week saved
