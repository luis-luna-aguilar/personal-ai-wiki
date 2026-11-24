---
type: proposal
source: raw/articles/2026-10-26-digitaloceancom-blog-managed-agents-public-preview.md
status: pending
created: 2026-10-26
---

# Proposal: DigitalOcean Managed Agents enters public preview

## Summary

### In short
General-purpose clouds are now selling agent runtimes without a harness of their own: DigitalOcean's Managed Agents runs the customer's Claude Code, Codex CLI or OpenCode in pausable microVM sessions billed only on CPU actually used, and routes every tool call through a gateway that keeps credentials out of the sandbox. The proposal creates a DigitalOcean Managed Agents tool page, adds it to State of Agents, and adds one bullet each to Agent runtime platforms and Agent-native compute, plus a source page. Reason to hesitate: the publication date comes from an "Updated" stamp on the post.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
DigitalOcean's product blog announced on 22 September 2026 that Managed Agents, after a private preview, is open to all customers. It is two services. Harness Runtime gives each agent session its own Firecracker microVM (a lightweight virtual machine) with a filesystem, Chromium and a coding sandbox, and lets developers pause, resume and fork sessions, so work can branch or continue on another device or with a teammate. It runs Claude Code, Codex CLI, OpenCode, Hermes, LangGraph agents, or any agent packaged as a standard container image. Action Gateway puts 16,000+ tools from 500+ providers behind one managed MCP endpoint, brokers credentials at call time so they never reach the model or the sandbox, applies central per-agent permissions with human approval for sensitive actions, and picks relevant tools without loading the whole catalog into context.

The economic argument is that agents work in bursts. DigitalOcean bills CPU per second on actual consumption, so an agent waiting for a model reply or a human approval pays nothing for CPU; its example puts a two-vCPU session at 25% utilisation at $0.060 an hour, against $0.126 for the full allocation. Its own benchmark (21 September, Codex CLI on GPT-5.5) has a session ready in 886 ms, first response in 3.3 seconds, and resume in 305 ms, with a resumed session answering as fast as a running one. The post admits running a command is slower than on Fly.io Sprites (189 ms against 79 ms) because each call passes through its authenticated, audited control plane. Insights, a cross-service run trace, is in private preview; Signals, which would turn runs into evaluation and reinforcement-learning feedback, is announced only. Named customers are OpenHands, Qencode and Amplitude.

### What changes
The wiki tracks hosted agent runtimes from model labs (Claude Managed Agents, Gemini) and sandbox specialists (Daytona, Modal, E2B), but no general cloud provider selling a bring-your-own-harness runtime.

- New page `tools/digitalocean-managed-agents.md` under the agent sandbox subcategory, with runtime, gateway, pricing, benchmark and roadmap detail.
- **State of Agents** gets a DigitalOcean line under Agent sandbox / compute infrastructure. The Recent-changes list is at its cap, so its oldest entry (Claude Cowork's July web/mobile beta) moves to history. Page date stays 19 October.
- **Agent runtime platforms** gains a "bring-your-own-harness managed runtimes" bullet. Page date stays 30 September.
- **Agent-native compute** gains a DigitalOcean bullet on active-CPU billing and fast resume. Page date moves to 22 September.
- One new source page.

### What to weigh
The post shows only "Updated: September 22, 2026", which the proposal treats as the publication date; the benchmark the day before supports it. A tool page is a judgment call for a public-preview product, made here because the wiki has no other general cloud in the sandbox subcategory and the detail would otherwise overload two pages that are near their ceilings: Agent runtime platforms sits at exactly its ceiling and ends near 105%, inside the warning band.

## Intended changes

- [ ] **Create** `wiki/tools/digitalocean-managed-agents.md` — new tool page, subcategory `agent-sandbox-infra`
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — add one leader line at the end of `### Agent sandbox / compute infrastructure`; adds one Recent-changes entry dated 2026-09-22 (live list has 10, at the cap); append one source id; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — the oldest Recent-changes entry (expected: [2026-07-08] Claude Cowork beta expands to web/mobile) moves to history
    > See draft below

- [ ] **Update** `wiki/concepts/agent-runtime-platforms.md` — add one bullet after "Managed-agent platform primitives" in `## Execution runtimes`; adds one Recent-changes entry dated 2026-09-22 (live list has 4, no spill); append one source id and link; `as_of` stays 2026-09-30
    > See draft below

- [ ] **Update** `wiki/trends/agent-native-compute.md` — add one Current-status bullet; Current-status stamp and `as_of` move to 2026-09-22; adds one Recent-changes entry dated 2026-09-22 (live list has 8, no spill); append one source id and link; add one Related line
    > See draft below

- [ ] **Create** `wiki/sources/articles/digitalocean-managed-agents-public-preview-2026-09-22.md` — source summary

## Page drafts

### wiki/tools/digitalocean-managed-agents.md (new)

```
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
```

### wiki/state-of/agents.md (updated)

Frontmatter `sources:` — append one id (`digitalocean-managed-agents-public-preview-2026-09-22`) to the live list; `as_of` unchanged.

`### Agent sandbox / compute infrastructure` — append after the E2B line:

```
- [DigitalOcean Managed Agents](../tools/digitalocean-managed-agents.md) — public preview; runs your own harness (Claude Code, Codex CLI, OpenCode) in pausable Firecracker microVMs billed on active CPU, with an MCP gateway that keeps credentials out of the sandbox *(as of 2026-09-22)*
```

`## Recent changes` — insert one entry between the 2026-10-09 and 2026-09-09 entries, then remove the oldest entry (see Spill):

```
- [2026-09-22] Added [DigitalOcean Managed Agents](../tools/digitalocean-managed-agents.md) to Agent sandbox / compute infrastructure: bring-your-own-harness microVM sessions with active-CPU billing and a credential-brokering MCP tool gateway (public preview).
```

### wiki/history/state-of/agents.md (updated — spill)

Append at the end of the file:

```

## Archived from current page on 2026-10-26

- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

### wiki/concepts/agent-runtime-platforms.md (updated)

Frontmatter `sources:` — append one id (`digitalocean-managed-agents-public-preview-2026-09-22`) to the live list; `as_of` unchanged.

`## Execution runtimes` — insert directly after the "Managed-agent platform primitives" bullet:

```
- **Bring-your-own-harness managed runtimes.** [DigitalOcean Managed Agents](../tools/digitalocean-managed-agents.md) (public preview, September 2026) sells the runtime without a harness of its own: Claude Code, Codex CLI, OpenCode, or a custom container runs in a pausable, forkable microVM session, and tools go through a separate MCP gateway that brokers credentials at call time, so they never enter the sandbox.
```

`## Recent changes` — insert one entry between the 2026-09-30 and 2026-09-07 entries:

```
- [2026-09-22] Added bring-your-own-harness managed runtimes: DigitalOcean Managed Agents runs customer harnesses in microVM sessions behind a credential-brokering MCP gateway.
```

`## Sources` — append:

```
- [DigitalOcean — Introducing Managed Agents](../sources/articles/digitalocean-managed-agents-public-preview-2026-09-22.md)
```

### wiki/trends/agent-native-compute.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-09-22
sources: [railway-agent-native-cloud-2026-05-20, daytona-giving-agents-computers-2026-05-21, modal-agent-experience-2026-07-08, ainews-new-ai-infra-unicorns-2026-05-22, superhuman-autonomous-growth-agent-2026-05-21, cloudflare-computer-launch-2026-09-07, digitalocean-managed-agents-public-preview-2026-09-22]
```

`## Current status` — heading stamp changes and one bullet is appended after the Cloudflare bullet:

```
## Current status (as of 2026-09-22)

- **[DigitalOcean Managed Agents](../tools/digitalocean-managed-agents.md) (September 2026):** a general-purpose cloud entering the category rather than a sandbox specialist. Firecracker microVM sessions are billed per second on CPU actually consumed, so an agent waiting on a model or a human approval costs no CPU, and paused sessions resume to ready in about 305 ms (DigitalOcean's own benchmark), which makes auto-pausing idle agents cheap enough to be the default.
```

`## Recent changes` — insert one entry above the 2026-09-07 entry:

```
- [2026-09-22] DigitalOcean Managed Agents public preview: active-CPU billing and ~305 ms resume for microVM agent sessions; a general cloud provider joining the sandbox specialists.
```

`## Related` — append:

```
- [DigitalOcean Managed Agents](../tools/digitalocean-managed-agents.md) — general-cloud entrant with active-CPU billing and pause/resume sessions
```

`## Sources` — append:

```
- [DigitalOcean — Introducing Managed Agents](../sources/articles/digitalocean-managed-agents-public-preview-2026-09-22.md)
```

### wiki/sources/articles/digitalocean-managed-agents-public-preview-2026-09-22.md (new)

```
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
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — bring-your-own-harness managed runtimes bullet
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
```

## Schema / vocabulary additions

None.

## Open questions

None.
