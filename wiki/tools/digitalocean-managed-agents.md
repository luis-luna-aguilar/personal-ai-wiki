---
title: DigitalOcean Managed Agents
type: tool
domains: [agents]
subcategory: agent-sandbox-infra
tags: [agentic, beta]
as_of: 2026-09-22
sources: [digitalocean-managed-agents-public-preview-2026-09-22]
---

# DigitalOcean Managed Agents

DigitalOcean's hosted agent stack, in public preview since September 2026 after a private preview. It does not ship its own agent harness: it runs the customer's choice of harness in persistent microVM sessions, gives it governed tool access through one MCP endpoint, and integrates natively with DigitalOcean's Inference Engine.

## Current status (as of 2026-09-22)

- **Harness Runtime:** each session is a Firecracker microVM with its own filesystem, built-in Chromium, and a coding sandbox; exec and private port-forwarding APIs; pause/resume through snapshots, forking, and auto-pause when no LLM or tool calls go out; parallel-session and subagent APIs packaged as skills for each supported harness. Runs Claude Code, Codex CLI, OpenCode, Hermes, LangGraph agents, or a custom agent as an OCI container image.
- **Action Gateway:** 16,000+ tools across 500+ providers (GitHub, HubSpot, Stripe, Snowflake, PagerDuty, Box, Supabase, Exa, web search, browser automation, DigitalOcean APIs, custom MCP servers) behind one managed MCP endpoint. Credentials are brokered at execution time and never reach the model or sandbox; per-agent permissions and human approval for sensitive actions are set centrally; retries and rate limits are handled by the gateway. DigitalOcean reports 99.3% accuracy matching an agent's intent to the right tool. Usable from any MCP client, not only Harness Runtime.
- **Pricing:** per-second billing on CPU actually consumed, so time spent waiting on a model or an approval costs no CPU; a paused session stops CPU and memory charges and keeps billable storage. DigitalOcean's example: two vCPUs at 25% average utilisation with a 4 GB memory peak cost $0.060 for an hour, against $0.126 for the full allocation. Storage, inference, and third-party tools are extra.
- **Performance (DigitalOcean benchmark, 21 September 2026, Codex CLI on GPT-5.5):** ready in 886 ms and first agent response in 3.3 s from session creation; resume to ready in 305 ms, with a resumed session answering in 2.43 s against 2.47 s for one already running. A command round trip takes 189 ms against 79 ms on Fly.io Sprites, which DigitalOcean attributes to routing exec through its authenticated, audited control plane.
- **Not yet shipped:** Insights (private preview) traces a run across runtime, gateway, and tools; Signals (announced) is meant to turn runs into evaluation and reinforcement-learning feedback.
- **Customers named:** OpenHands, Qencode, Amplitude. Qencode's support-triage agent on Harness Runtime is estimated to save its team 4–8 hours a week.

## Recent changes

- [2026-09-22] Public preview: Harness Runtime and Action Gateway opened to all customers.

## Related

- [Agent runtime platforms](../concepts/agent-runtime-platforms.md) — the managed-runtime layer this product competes in
- [Agent-native compute infrastructure](../trends/agent-native-compute.md) — the execution-layer trend its billing and resume design targets
- [Claude Managed Agents](claude-managed-agents.md) — a model lab's hosted runtime, which ships its own harness

## Sources

- [DigitalOcean — Introducing Managed Agents](../sources/articles/digitalocean-managed-agents-public-preview-2026-09-22.md)
