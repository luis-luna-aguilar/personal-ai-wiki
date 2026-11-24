---
title: 'Shann Holmberg on X — "How to Become a Hermes Agent Operator"'
type: source
source_type: tweet
source_file: raw/tweets/2026-05-18-shannholmberg-2055335043904492011.md
url: https://x.com/shannholmberg/status/2055335043904492011
published: 2026-05-18
ingested: 2026-10-20
domains: [agents]
---

# Shann Holmberg on X — "How to Become a Hermes Agent Operator"

Long X Article by Shann Holmberg, an AI marketer, on how he runs his marketing operation on Hermes Agent: the anatomy of a Hermes agent (memory files, soul, self-written skills), his fleet of specialist agents in Docker containers on one VPS, the "agent control room" folder that governs the fleet, four levels of setup from one agent to a scheduled, orchestrated team, a prototype-to-production method for new workflows, and honest trade-offs. He links a public control-room template whose skills let Claude Code or Codex provision the VPS and register the first agent.

## Influenced pages

- [Hermes Agent](../../tools/hermes-agent.md) — "Operating a Hermes fleet" section
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — control-room pattern (docs-only fleet governance kept apart from agent runtime)

## Key claims extracted

- As of May 2026: ~150K GitHub stars, 123 bundled skills, 70+ gateway tools, 300+ models through one subscription, six deployment targets (local, Docker, SSH, Daytona, Singularity, Modal), 20+ messaging surfaces, #1 on OpenRouter for token usage
- Memory at `~/.hermes/memories/`: `MEMORY.md` and `USER.md` injected at session start; sessions in SQLite with full-text recall; `SOUL.md` sets personality
- Closed learning loop: the agent writes new skills as it works; advice is to let it write skills from real work rather than writing them on day one
- Hermes vs OpenClaw framed as "Rails vs Linux": opinionated defaults vs explicit primitives
- Fleet: personal assistant, SEO, outbound, design review, content, a company-brain agent over Slack/email/transcripts, and a routing-only orchestrator, each in its own container
- SEO agent: 21 steps in three phases (research, production, distribution) in one container because the work is sequential
- Control room (`/root/vps-agents`): docs, rules, runbooks, env-map, registry, no raw secrets; live runtime per agent at `/srv/<agent>/data` (secrets, memory, skills, sessions, cron)
- Three paths: control path (manage the fleet), direct path (talk to a specialist), orchestrated path (orchestrator → task bus → specialists)
- Four levels: one agent; direct specialists; orchestrator front door; scheduled automation
- New agent only for its own credentials, its own long-term memory, or a separate recurring role
- Prototype → run 2–3 times on real work → fine-tune in a dedicated workspace → deploy on a VPS schedule after a week unattended
- Trade-offs: defaults feel heavy for explicit-control users; levels 3–4 have a learning curve; the framework does not make a small model a strategist
