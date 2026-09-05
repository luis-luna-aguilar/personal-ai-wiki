---
title: Modal
type: tool
domains: [agents]
subcategory: agent-sandbox-infra
tags: [agentic]
as_of: 2026-07-08
sources: [modal-agent-experience-2026-07-08, ainews-new-ai-infra-unicorns-2026-05-22]
---

# Modal

Modal is a serverless cloud for AI workloads — decorator-based Python infrastructure for elastic inference, GPU burst, sandboxes, post-training, and background agents. Fresh off a $355M Series C, CTO Akshat Bubna says the SDK team's mission has moved from "developer experience" to "agent experience": agents need the same self-provisioning primitives human developers did, with observability mattering more than reading the code.

## Current status (as of 2026-07-08)

- $355M Series C; AINews (2026-05-22) reports the valuation as $4.7B in its header and $4.65B in its body
- Sandboxes support "sidecars" (Docker-Compose-style multi-container pods), networked/multi-node setups, a private IPv6 overlay (I6PN), and RDMA; RL rollouts can require up to 100,000 sandboxes at once
- Ships open-source DeFlash, a block-based speculative decoder, and "Auto Endpoints" for frontier-level inference performance on custom models
- Capacity pool spans 17 cloud providers, with Modal's own reliability layer absorbing hardware/provider failures
- Internal "auto inference" harness automates routine forward-deployed engineering (GPU config sweeps, profiling, tuning)

## Strengths

- Elastic, programmatic infrastructure that agents can provision for themselves; multi-cloud capacity without customer-side cloud management

## Weaknesses / caveats

- Valuation is secondary (AINews) and internally inconsistent across that issue
- Bubna stresses that production agents still need hard guardrails
- Single CTO interview as the primary source; product claims not checked against Modal docs

## Recent changes

- [2026-07-08] Latent Space interview: "agent experience" reframing, 100K-sandbox RL rollouts, sidecars, I6PN/RDMA, DeFlash, Auto Endpoints, 17-cloud capacity pool
- [2026-05-22] AINews: $355M Series C at $4.65–4.7B

## Sources

- [Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO](../sources/newsletters/modal-agent-experience-2026-07-08.md)
- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
