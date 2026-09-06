---
title: Agent-native compute infrastructure
type: trend
domains: [agents]
tags: [agentic]
as_of: 2026-07-08
sources: [railway-agent-native-cloud-2026-05-20, daytona-giving-agents-computers-2026-05-21, modal-agent-experience-2026-07-08, ainews-new-ai-infra-unicorns-2026-05-22, superhuman-autonomous-growth-agent-2026-05-21]
---

# Agent-native compute infrastructure

Cloud infrastructure built for human developers (Kubernetes, EKS/GKE, slow-scaling web-server assumptions) is increasingly being displaced by a distinct category purpose-built for agent workloads: bursty, stateful-but-pausable sandboxes that must scale from zero to tens or hundreds of thousands of concurrent instances, driven substantially by RL/eval training loops rather than steady human traffic. Daytona, Modal, and Railway are converging on this thesis from different starting points, alongside a broader infrastructure funding wave.

## Current status (as of 2026-07-08)

- **[Daytona](../tools/daytona.md)**: pivoted from human dev environments to AI sandboxes; bare-metal scheduler gives ~60ms single-sandbox startup and ~75s to spin up 50,000 concurrently; biggest customer runs ~850,000 sandboxes/day; RL/eval workloads grew from ~0% to ~50% of usage within months; building Windows/macOS computer-use sandboxes to extend beyond Linux-only code execution
- **[Modal](../tools/modal.md)**: raised a $355M Series C (valuation reported by AINews as $4.65–4.7B); reframed its SDK team's mission from "developer experience" to "agent experience"; RL rollouts can require 100,000 sandboxes at once; ships open-source DeFlash (block-based speculative decoding) and "Auto Endpoints"; runs a capacity pool spanning 17 cloud providers with its own reliability layer on top
- **[Railway](../tools/railway.md)**: bare-metal data centers with ~3-month payback vs. cloud rental and ~70% margins subsidizing cloud bursting; built Central Station (internal clustering of customer feedback and incidents) and agent-safe production forks (copy-on-write clones with PII transforms so agents can test against production-like state); founder Jake Cooper argues "the pull request is dying" and that the CLI, not a visual canvas, is becoming the primary agent-facing interface
- **Funding wave** (per AINews 2026-05-22 and Superhuman 2026-05-21, secondary): Exa raised $250M Series C at $2.2B (agent-oriented search/retrieval); Turbopuffer crossed $100M ARR profitably having raised under $1M; Hark raised $700M at $6B (GPU infrastructure, model development, hardware, personal-intelligence products); OpenAI launched "Guaranteed Capacity," letting enterprises lock in 1–3 year compute commitments at volume discounts
- Common technical thread across providers: RL/eval workloads are far spikier than historical human developer traffic (Daytona reports mean utilization near 15% to cover peaks up to 90%); managed Kubernetes (EKS/GKE) is described by both Daytona and Modal as a poor fit; the CLI is emerging as the primary agent-facing interface over dashboards/canvases (Railway, Daytona)

## Why it matters

RL and eval workloads are structurally different from serving ordinary background coding-agent traffic: they spike from zero to tens or hundreds of thousands of sandboxes and back down, need GPUs kept near-100% utilized without stalling while the next CPU sandbox spins up (Daytona's account of why RL customers come to it), and are reportedly becoming a large fraction of usage at infrastructure providers that originally served everyday coding agents. This is a distinct phenomenon from frontier *training*-compute scale (see [Compute infrastructure as decisive competitive moat](compute-infrastructure.md)) — it concerns the execution layer agents themselves run on, not GPU counts for pretraining.

## What to watch

- Whether managed-Kubernetes providers respond with agent-workload-specific offerings, or cede this layer to specialized providers
- Whether RL/eval's share of sandbox usage keeps climbing, and how utilization/pricing models adapt to spiky demand
- Whether Windows/macOS computer-use sandboxes (Daytona) become a meaningful new workload category alongside Linux-only sandboxes
- Whether the "CLI over canvas" pattern generalizes across other agent-infra providers

## Related

- [Compute infrastructure as decisive competitive moat](compute-infrastructure.md) — the frontier-training-scale analog to this execution-layer trend
- [E2B](../tools/e2b.md) — earlier-covered isolated sandbox runtime for agent code execution; part of the same Latent Space "agent cloud" series

## Recent changes

- [2026-07-08] Modal detailed its shift from developer experience to agent experience, its $355M Series C, and 100,000-sandbox RL rollout workloads.
- [2026-05-22] AINews cluster confirmed the funding wave: Exa $250M@$2.2B, Turbopuffer $100M ARR profitable, Modal $355M at $4.65–4.7B (the issue gives both figures), plus Hark $700M@$6B.
- [2026-05-21] Daytona detailed its pivot to AI sandboxes: 60ms startup, 850K sandboxes/day at its largest customer, RL/eval workloads at ~50% of usage, and new Windows/macOS computer-use sandboxes.
- [2026-05-21] OpenAI launched Guaranteed Capacity (per Superhuman), letting enterprises lock in 1–3 year compute commitments at volume discounts.
- [2026-05-20] Railway detailed its agent-native infrastructure thesis: bare-metal 3-month payback, Central Station, agent-safe production forks, and the "pull request is dying" argument for CLI-first agent interfaces.
- [2026-05-05] AINews "inference inflection" framing: inference throughput is the dominant bottleneck for production agent workloads, and agent systems add a compound requirement — CPU, sandbox, browser, and execution capacity matter alongside GPU. Originally recorded on [Compute infrastructure](compute-infrastructure.md); relocated here as the execution-layer analog once this page split off from it.
- [2026-05-05] Manus Cloud Computer: persistent Ubuntu environments with SSH/web-terminal access and tool state that survives across agent sessions — durable-agent runtime as an infrastructure category distinct from ephemeral-per-task containers. Originally recorded on [Compute infrastructure](compute-infrastructure.md); relocated here as the execution-layer analog once this page split off from it.

## Sources

- [Railway: The Agent-Native Cloud — Jake Cooper](../sources/newsletters/railway-agent-native-cloud-2026-05-20.md)
- [Giving Agents Computers — Ivan Burazin, Daytona](../sources/newsletters/daytona-giving-agents-computers-2026-05-21.md)
- [Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO](../sources/newsletters/modal-agent-experience-2026-07-08.md)
- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
- [Superhuman — Meet the autonomous growth agent (OpenAI Guaranteed Capacity mention)](../sources/newsletters/superhuman-autonomous-growth-agent-2026-05-21.md)
