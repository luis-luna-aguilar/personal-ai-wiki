---
title: Persistent cloud computers for agents
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-01-manus-agents-run-nonstop-now.md
published: 2026-05-01
ingested: 2026-05-05
domains: [agents, computer-use]
---

# Persistent cloud computers for agents

The Code reports Manus Cloud Computer as a persistent Ubuntu environment with SSH access, web terminal access, and pre-installed tools that survive across sessions. Rather than spinning up a fresh container per task, the environment persists indefinitely — agents resume work where they left off.

## Key claims extracted

- Manus Cloud Computer provides a persistent Ubuntu environment (not ephemeral per-task)
- Access via SSH and web terminal; pre-installed tools remain across sessions
- Environment persists between agent runs; state (files, installed packages, running processes) carries over
- Positioned as infrastructure for always-on or nonstop agent workloads rather than one-shot task execution
- Fits the broader durable-agent runtime trend where agents accumulate context and tools over time

## Caveats

- The Code is a secondary newsletter; Manus product specifics should be verified against Manus documentation
- Exact compute specs, pricing, and session persistence guarantees not captured in the newsletter

## Influenced pages

- `wiki/state-of/agents.md` — persistent cloud computers as a durable-agent runtime pattern
- `wiki/trends/compute-infrastructure.md` — persistent personal/business agent environments
