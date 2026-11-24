---
title: AINews — Perplexity open-sources SPACE
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-16-ainews-agents-disprove-polysemanticity-greatly.md
url: https://www.latent.space/p/ainews-agents-disprove-polysemanticity
published: 2026-10-16
ingested: 2026-10-20
domains: [cybersecurity, agents]
---

# AINews — Perplexity open-sources SPACE

Story from the 16 October 2026 AINews issue (covering 14–15 October): Perplexity open-sources SPACE, its per-task microVM sandbox for agents, with escape-testing results. The 15 October issue had described the same system's internal scale.

## Influenced pages

- [Agent incidents in the wild](../../trends/agent-incidents-in-the-wild.md) — Perplexity SPACE line under containment (moved from State of Cybersecurity on 2026-11-24)

## Key claims extracted

- SPACE is an Apache 2.0 sandbox platform that runs each agent task in a Firecracker microVM, with credentials and egress controlled from outside the VM
- In 108 escape attempts by models with root inside the VM, none reached the host
- SPACE also runs Perplexity's RL and eval workloads
- (15 October issue) SPACE handles millions of executions per day at a <0.0002% error rate, binding requests to executions with short-lived signed identity
