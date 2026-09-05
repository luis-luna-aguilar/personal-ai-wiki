---
title: "Giving Agents Computers — Ivan Burazin, Daytona"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-21-giving-agents-computers-ivan-burazin-daytona.md
url: https://www.latent.space/p/daytona
published: 2026-05-21
ingested: 2026-08-25
domains: [agents]
---

# Giving Agents Computers — Ivan Burazin, Daytona

Latent Space podcast transcript with Daytona CEO Ivan Burazin. Daytona pivoted in January 2025 from automating human dev environments to selling "composable computers" for AI agents — bare-metal, stateful, fast-resuming sandboxes rather than preemptible VMs — after a New Year's Eve MVP that customers pulled for.

## Influenced pages
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — new trend page
- [Daytona](../../tools/daytona.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new `Agent sandbox / compute infrastructure` section
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — cross-link and Recent-changes entry

## Key claims extracted
- Bare metal from the start, with Daytona's own scheduler (not Kubernetes/Nomad): ~60ms to spin up one sandbox (with network latency); ~75 seconds to spin up 50,000 concurrently
- Biggest customer runs ~850,000 sandboxes/day; company has fielded a request for ~500,000 concurrent CPUs
- Two distinct usage shapes: "background agents" (Cognition, Lovable, Harvey-style) follow human daily/weekly rhythms; RL/eval workloads are extremely spiky (0 → 100,000 CPUs → 0), pushing mean utilization down to ~15% while peaks reach ~90%
- RL/eval workloads grew from ~0% to ~50% of Daytona's usage within months
- RL customers come to Daytona because GPUs are far more expensive than CPUs: the GPU should stay at ~100% utilization, so the next CPU sandbox must spin up instantly rather than waiting on machine provisioning
- Competing directly against managed Kubernetes (EKS/GKE); customers who switch report "never going back," citing ergonomics, spin-up speed, and dynamic resizing (hard to OOM)
- Investing in Windows/macOS "computer use" sandboxes (not just Linux), currently feature-flagged, to unlock knowledge work locked in legacy desktop apps (Burazin's own US TAM estimate: ~$10T/year)
- Core platform including the scheduler is open source; Windows and GPU features sit behind feature flags — Burazin concedes it is "not full open source"
- CLI seen as mattering more than MCP for exposing agent-usable handles into infrastructure
