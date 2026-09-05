---
title: "Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experi.md
url: https://www.latent.space/p/modal2026
published: 2026-07-08
ingested: 2026-08-25
domains: [agents]
---

# Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO

Latent Space podcast transcript with Modal CTO Akshat Bubna, published alongside Modal's $355M Series C and framed as the close of the show's "Agent Cloud" series (Databricks, Daytona, Railway, E2B). Modal reframed its SDK team's mission from "developer experience" to "agent experience," arguing agents need the same self-provisioning, decorator-based infrastructure that benefited human developers, but with observability mattering more than reading the code itself.

## Influenced pages
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — new trend page
- [Modal](../../tools/modal.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new `Agent sandbox / compute infrastructure` section
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — cross-link and Recent-changes entry

## Key claims extracted
- $355M Series C raised (the transcript gives no valuation; AINews 2026-05-22 reports $4.7B in its header and $4.65B in its body)
- Kubernetes was never designed for bursty, compute-heavy workloads; agents need to write code, run it, inspect output, change the environment, and retry in fast loops
- RL rollouts can require up to 100,000 sandboxes at once; sandboxes now support "sidecars" (Docker-Compose-style multi-container pods) and networked/multi-node configurations
- Ships open-source DeFlash, a block-based speculative decoder, plus "Auto Endpoints" to make frontier-level inference performance available on custom models
- Runs a capacity pool spanning 17 cloud providers; Modal built its own reliability layer on top so that hardware or provider failures ("GPU falls off the bus") do not affect user workloads
- Private IPv6 overlay networking (I6PN) lets containers in the same workspace address each other privately; RDMA and multi-node support originally built for distributed training are reused for networked-sandbox use cases
- Internal "auto inference" repo automates the team's own forward-deployed engineering: sweeping GPU configs, profiling, and tuning without a human in the loop for routine cases
- Production agents still need hard guardrails; observability, not code-reading, is framed as the more important human-facing surface now that agents write most of the code
