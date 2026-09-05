---
title: Daytona
type: tool
domains: [agents]
subcategory: agent-sandbox-infra
tags: [agentic]
as_of: 2026-05-22
sources: [daytona-giving-agents-computers-2026-05-21, ainews-new-ai-infra-unicorns-2026-05-22]
---

# Daytona

Daytona sells "composable computers" for AI agents: bare-metal, stateful, fast-resuming sandboxes exposed through an API and run on Daytona's own scheduler rather than Kubernetes. CEO Ivan Burazin describes a hard pivot in January 2025 from automating human cloud dev environments to agent sandboxes, after customers pulled for a New Year's Eve MVP.

## Current status (as of 2026-05-22)

- ~60ms to start one sandbox (including network latency); ~75 seconds to start 50,000 concurrently
- Largest customer runs ~850,000 sandboxes/day; Daytona has fielded requests for ~500,000 concurrent CPUs
- RL/eval workloads grew from ~0% to ~50% of usage within months; because capacity is held for peaks, mean utilization is ~15% against peaks of ~90%
- Building Windows/macOS "computer use" sandboxes (currently feature-flagged) to reach knowledge work locked in legacy desktop apps; Burazin's own US TAM estimate is ~$10T/year
- Core platform, including the scheduler, is open source; Windows and GPU features sit behind feature flags (Burazin concedes it is "not full open source")

## Strengths

- Spin-up speed and dynamic resizing (sandboxes are "very hard to OOM"); customers switching from EKS/GKE are quoted as "never going back"
- Positioned for both steady background-agent traffic (Cognition, Lovable, Harvey-style customers) and spiky RL/eval runs

## Weaknesses / caveats

- All figures are founder-reported in a single podcast transcript; no primary documentation checked
- Spiky RL demand forces low mean utilization — an unresolved economics problem Burazin says every agent-first infra company shares
- Windows/macOS sandboxes are not generally available

## Recent changes

- [2026-05-22] AINews recap repeats the Daytona pitch: 60ms sandboxes, 50K startups in 75 seconds, RL/evals roughly half of usage
- [2026-05-21] Latent Space interview details the pivot, bare-metal scheduler, 850K/day customer, RL/eval share at ~50%, and Windows/macOS computer-use sandboxes

## Sources

- [Giving Agents Computers — Ivan Burazin, Daytona](../sources/newsletters/daytona-giving-agents-computers-2026-05-21.md)
- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
