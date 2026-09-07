---
title: Unpacking ChatGPT Work — the Agent for a Billion Users
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-04-unpacking-chatgpt-work-the-agent-for-a-billion-us.md
url: https://www.latent.space/p/unpacking-chatgpt-work
published: 2026-08-04
ingested: 2026-09-07
domains: [agents]
---

# Unpacking ChatGPT Work — the Agent for a Billion Users

Latent Space guest post (Shlok) independently investigating OpenAI's July 9 ChatGPT Work launch, based on direct hands-on use with Codex/Work. Covers Work's cloud-microVM architecture, its deliberate split between agent-owned scratch space and product-managed continuity (Personal Context, Library, Projects), browser-service tool use with a persistent browser profile, early proactive task suggestions, two-tier Scheduled Tasks, and the 1,000+-plugin Plugin Directory's discovery gap. Reports Work plus Codex crossing 10M users three weeks post-launch and a confirmed Chat/Work merger by year-end.

## Influenced pages

- [tools/codex](../../tools/codex.md) — new section on Work's cloud-computer architecture and continuity model
- [state-of/agents](../../state-of/agents.md) — refreshed Codex/Workspace-Agents line with the 10M-user milestone and merger timeline

## Key claims extracted

- ChatGPT Work launched 2026-07-09: three new models across fourteen configurations, merged ChatGPT/Codex desktop app, mainstream cloud agents
- Work plus Codex reportedly crossed 10M users three weeks post-launch
- Pro cloud microVM: 8 CPUs, 20GB RAM, 64GB disk; Plus: 14GB RAM
- Continuity across tasks flows through Personal Context, Library, and Projects — not through the computer itself, unlike OpenClaw
- Library and per-thread local file copies can silently diverge (no sync)
- Two Scheduled Tasks types: standalone (fresh task from saved prompt) and heartbeat-triggered (resumes an existing thread with context intact)
- Plugin Directory has 1,000+ plugins but doesn't suggest relevant installed-but-unused plugins, even when the service is named directly
- Greg Brockman has confirmed Work and Chat will merge into one product by end of 2026
