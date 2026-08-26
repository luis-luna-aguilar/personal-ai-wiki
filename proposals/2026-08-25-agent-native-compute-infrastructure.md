---
type: proposal
source: raw/newsletters/2026-05-20-railway-the-agent-native-cloud-jake-cooper.md
status: pending
created: 2026-08-25
---

# Proposal: Agent-native compute infrastructure becomes its own category

## Summary
Three long-form interviews (Daytona's Ivan Burazin, Modal's Akshat Bubna, Railway's Jake Cooper) converge on the same thesis: cloud infrastructure built for human developers doesn't fit agent workloads — which are bursty, need stateful-but-pausable sandboxes, and increasingly serve RL/eval training rather than steady human traffic. This sits alongside a funding wave (Exa, Turbopuffer, Modal's $355M round, Hark) and OpenAI's "Guaranteed Capacity" enterprise offering.

## Intended changes

- [x] **Create** `wiki/trends/agent-native-compute.md` — a new trend page scoped to the *agent execution layer* (sandboxes, RL/eval workload shapes), distinct from `trends/compute-infrastructure.md`'s focus on frontier *training*-compute scale as a moat
    > See draft below

- [x] **Update** `wiki/trends/compute-infrastructure.md` — add a cross-link to the new page and a short Recent-changes entry noting the funding wave; no other content changes
    > See draft below

- [x] **Create** `wiki/sources/newsletters/railway-agent-native-cloud-2026-05-20.md`
- [x] **Create** `wiki/sources/newsletters/daytona-giving-agents-computers-2026-05-21.md`
- [x] **Create** `wiki/sources/newsletters/modal-agent-experience-2026-07-08.md`
- [x] **Create** `wiki/sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md`
- [x] **Create** `wiki/sources/newsletters/superhuman-autonomous-growth-agent-2026-05-21.md` — covers only the OpenAI Guaranteed Capacity claim from this issue; the issue's main story (Tempo's autonomous growth agent) is a separate, unrelated signal not actioned here

## Page drafts

### wiki/trends/agent-native-compute.md (new)

```md
---
title: Agent-native compute infrastructure
type: trend
domains: [agents]
tags: [agentic]
as_of: 2026-07-08
sources: [railway-agent-native-cloud-2026-05-20, daytona-giving-agents-computers-2026-05-21, modal-agent-experience-2026-07-08, ainews-new-ai-infra-unicorns-2026-05-22, superhuman-autonomous-growth-agent-2026-05-21]
---

# Agent-native compute infrastructure

Cloud infrastructure built for human developers (Kubernetes, EKS/GKE, slow-scaling web-server assumptions) is increasingly being displaced by a distinct category purpose-built for agent workloads: bursty, stateful-but-pausable sandboxes that must scale from zero to hundreds of thousands of concurrent instances, driven substantially by RL/eval training loops rather than steady human traffic. Daytona, Modal, and Railway are converging on this thesis from different starting points, alongside a broader infrastructure funding wave.

## Current status (as of 2026-07-08)

- **Daytona**: pivoted from human dev environments to AI sandboxes; bare-metal scheduler gives ~60ms single-sandbox startup and ~75s to spin up 50,000 concurrently; biggest customer runs ~850,000 sandboxes/day; RL/eval workloads grew from ~0% to ~50% of usage within months; building Windows/macOS computer-use sandboxes to extend beyond Linux-only code execution
- **Modal**: raised a $355M Series C (~$4.65-4.7B valuation); reframed its SDK team's mission from "developer experience" to "agent experience"; RL rollouts can require 100,000 sandboxes at once; ships open-source DeFlash (block-based speculative decoding) and "Auto Endpoints"; runs a 17-cloud capacity pool rather than owning data centers
- **Railway**: bare-metal data centers with ~3-month payback vs. cloud rental and ~70% margins subsidizing cloud bursting; built Central Station (context/incident aggregation across ~3M users) and agent-safe production forks (copy-on-write clones for AI-SRE); founder Jake Cooper argues "the pull request is dying" and that the CLI, not a visual canvas, is becoming the primary agent-facing interface
- **Funding wave**: Exa raised $250M Series C at $2.2B (agent-oriented search/retrieval); Turbopuffer crossed $100M ARR profitably having raised under $1M; Hark raised $700M at $6B (GPU infra, robotics, hardware); OpenAI launched "Guaranteed Capacity," letting enterprises lock in 1-3 year compute commitments at volume discounts
- Common technical thread across providers: RL/eval workloads are far spikier than historical human developer traffic (Daytona reports mean utilization near 15% to cover peaks up to 90%); managed Kubernetes (EKS/GKE) is widely reported as a poor fit; the CLI is emerging as the primary agent-facing interface over dashboards/canvases

## Why it matters

RL and eval workloads are structurally different from serving ordinary background coding-agent traffic: they spike from zero to tens or hundreds of thousands of sandboxes and back down, need GPUs kept near-100% utilized without stalling on CPU/sandbox provisioning, and are reportedly becoming a large fraction of usage at infrastructure providers that originally served everyday coding agents. This is a distinct phenomenon from frontier *training*-compute scale (see [Compute infrastructure as decisive competitive moat](compute-infrastructure.md)) — it concerns the execution layer agents themselves run on, not GPU counts for pretraining.

## What to watch

- Whether managed-Kubernetes providers respond with agent-workload-specific offerings, or cede this layer to specialized providers
- Whether RL/eval's share of sandbox usage keeps climbing, and how utilization/pricing models adapt to spiky demand
- Whether Windows/macOS computer-use sandboxes (Daytona) become a meaningful new workload category alongside Linux-only sandboxes
- Whether the "CLI over canvas" pattern generalizes across other agent-infra providers

## Related

- [Compute infrastructure as decisive competitive moat](compute-infrastructure.md) — the frontier-training-scale analog to this execution-layer trend

## Recent changes

- [2026-07-08] Modal detailed its shift from developer experience to agent experience, its $355M Series C, and 100,000-sandbox RL rollout workloads.
- [2026-05-22] AINews cluster confirmed the funding wave: Exa $250M@$2.2B, Turbopuffer $100M ARR profitable, Modal $355M@$4.65B, plus Hark $700M@$6B.
- [2026-05-21] Daytona detailed its pivot to AI sandboxes: 60ms startup, 850K sandboxes/day at its largest customer, RL/eval workloads at ~50% of usage, and new Windows/macOS computer-use sandboxes.
- [2026-05-21] OpenAI launched Guaranteed Capacity, letting enterprises lock in 1-3 year compute commitments at volume discounts.
- [2026-05-20] Railway detailed its agent-native infrastructure thesis: bare-metal 3-month payback, Central Station, agent-safe production forks, and the "pull request is dying" argument for CLI-first agent interfaces.

## Sources

- [Railway: The Agent-Native Cloud — Jake Cooper](../sources/newsletters/railway-agent-native-cloud-2026-05-20.md)
- [Giving Agents Computers — Ivan Burazin, Daytona](../sources/newsletters/daytona-giving-agents-computers-2026-05-21.md)
- [Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO](../sources/newsletters/modal-agent-experience-2026-07-08.md)
- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
- [Superhuman — Meet the autonomous growth agent (OpenAI Guaranteed Capacity mention)](../sources/newsletters/superhuman-autonomous-growth-agent-2026-05-21.md)
```

### wiki/trends/compute-infrastructure.md (updated)

`## Related` (full section, one line added):

```md
## Related

- [Proprietary data becomes model moat](proprietary-data-becomes-model-moat.md) — a parallel structural-advantage thesis
- [Agent-native compute infrastructure](agent-native-compute.md) — the agent-execution-layer analog: sandboxes, RL/eval workload shapes, and the Daytona/Modal/Railway funding wave
```

`## Recent changes` — new entry added at the top (full section):

```md
## Recent changes

- [2026-07-08] Agent-execution-layer analog spun off into a dedicated page: [Agent-native compute infrastructure](agent-native-compute.md) covers Daytona/Modal/Railway sandbox economics and the RL/eval funding wave (Exa, Turbopuffer, Hark).
- [2026-06-18] Added outputmaxxing / compute-utilization framing from AMP: the frontier compute bottleneck includes MFU, scheduling, power, and grid-like coordination, not only GPU count.
- [2026-07-02] Added inference-systems counterforce: DSpark/vLLM, TwoTower, WebGPU Gemma, and kernel-level work show competition moving below model weights into runtime speed and serving economics.
- [2026-06-30] Added hybrid local/cloud routing as a compute-control counterforce for private, low-latency, repeated, or cheaper tasks.
- [2026-05-05] Stripe frames stolen compute (API keys, tokens, credits, free trials) as the emerging AI fraud surface — "compute is the new cash"; agents as autonomous purchasers create new commerce and payment-flow design challenges
- [2026-05-05] Manus Cloud Computer: persistent Ubuntu environments with SSH/web-terminal access and tool state that survives across agent sessions; durable-agent runtime as an infrastructure category distinct from ephemeral-per-task containers
- [2026-05-05] Parallel Web Systems raised at a $2B valuation (secondary coverage) for internet/research APIs optimized for AI agents — market signal that agent-oriented web access infrastructure is becoming a standalone investable category
- [2026-05-05] AINews "inference inflection" framing: inference throughput is the dominant current bottleneck, and agent systems add a compound requirement — CPU, sandbox, browser, and execution capacity matter alongside GPU for production agent workloads
- [2026-05-05] Superhuman reports Q1 2026 Big Tech earnings (Alphabet, Amazon, Meta, Microsoft) show AI revenue materializing while capex continues climbing; treat directional signal as confirmed, specific figures as pending primary verification
```

(9 entries total; page remains under the 10-entry cap — no spill needed.)

### wiki/sources/newsletters/railway-agent-native-cloud-2026-05-20.md (new)

```md
---
title: "Railway: The Agent-Native Cloud — Jake Cooper"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-20-railway-the-agent-native-cloud-jake-cooper.md
url: https://www.latent.space/p/railway
published: 2026-05-20
ingested: 2026-08-25
domains: [agents]
---

# Railway: The Agent-Native Cloud — Jake Cooper

Latent Space podcast transcript with Railway founder/CEO Jake Cooper. Railway (35-person team, 3M users, ~100K signups/week) is rebuilding cloud infrastructure — network, compute, storage, orchestration — from scratch for an agent-native world, arguing agents need the same primitives humans did (versioning, observability, feature flags) but at roughly 1,000x scale.

## Influenced pages
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — new trend page

## Key claims extracted
- Bare-metal data centers: ~3-month payback period vs. cloud rental, ~70% margins subsidizing cloud bursting into AWS/GCP/Oracle when needed
- Central Station: internal tool aggregating all customer feedback/incidents into clusters, dynamically routing issues to the right internal team
- Agent-safe production forks: copy-on-write clones of production (with PII transforms) that let an agent test changes as close to prod as possible without risking it
- Progressive/shadow rollouts as a first-class primitive so agents (and their mistakes) can be tested at 0.1% → 1% → full rollout
- Thesis: "the pull request is dying" — the push-pull-rebuild loop is being replaced by versioned, mergeable production changes
- CLI, not canvas, is becoming the primary agent interface; canvas becomes an output/context-anchor rather than an input
- Self-replicating infrastructure: an agent with Railway CLI access can provision its own new infrastructure and deploy itself
```

### wiki/sources/newsletters/daytona-giving-agents-computers-2026-05-21.md (new)

```md
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

Latent Space podcast transcript with Daytona CEO Ivan Burazin. Daytona pivoted (January of the prior year) from automating human dev environments to selling "composable computers" for AI agents — bare-metal, stateful, fast-resuming sandboxes rather than preemptible VMs.

## Influenced pages
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — new trend page

## Key claims extracted
- Bare metal from the start, with Daytona's own scheduler (not Kubernetes/Nomad): ~60ms to spin up one sandbox (with network latency); ~75 seconds to spin up 50,000 concurrently
- Biggest customer runs ~850,000 sandboxes/day; company handles requests for up to ~500,000 concurrent CPUs
- Two distinct usage shapes: "background agents" (Cognition, Lovable, Harvey-style) follow human daily/weekly rhythms; RL/eval workloads are extremely spiky (0 → 100,000 CPUs → 0), pushing mean utilization down to ~15% while peaks reach ~90%
- RL/eval workloads grew from ~0% to ~50% of Daytona's usage within months
- Competing directly against managed Kubernetes (EKS/GKE); customers who switch report "never going back," citing ergonomics, spin-up speed, and dynamic resizing (hard to OOM)
- Investing in Windows/macOS "computer use" sandboxes (not just Linux) to unlock a much larger knowledge-work automation market (Daytona's own TAM estimate: ~$10T/year in the US)
- CLI seen as mattering more than MCP for exposing agent-usable handles into infrastructure
```

### wiki/sources/newsletters/modal-agent-experience-2026-07-08.md (new)

```md
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

Latent Space podcast transcript with Modal CTO Akshat Bubna, published alongside Modal's $355M Series C. Modal reframed its SDK team's mission from "developer experience" to "agent experience," arguing agents need the same self-provisioning, decorator-based infrastructure that benefited human developers, but with observability mattering more than reading the code itself.

## Influenced pages
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — new trend page

## Key claims extracted
- $355M Series C raised (valuation reported elsewhere at ~$4.65-4.7B)
- RL rollouts can require up to 100,000 sandboxes at once; sandboxes now support "sidecars" (Docker-Compose-style multi-container pods) and networked/multi-node configurations
- Ships open-source DeFlash, a block-based speculative decoder, plus "Auto Endpoints" for turnkey frontier-level inference deployment
- Runs a capacity pool spanning 17 cloud/neo-cloud providers rather than owning its own data centers ("supercloud" strategy); reliability layer absorbs individual provider failures
- Private IPv6 overlay networking (I6PN) and RDMA support originally built for distributed training, now reused by customers for other networked-sandbox use cases
- Internal "auto inference"/"auto research" harness automates the team's own forward-deployed engineering: sweeping GPU configs, profiling, and tuning without a human in the loop for routine cases
- Observability, not code-reading, is framed as the more important human-facing surface now that agents write most of the code
```

### wiki/sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md (new)

```md
---
title: "[AINews] New AI Infra unicorns: Exa, Modal, TurboPuffer"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-22-ainews-new-ai-infra-unicorns-exa-modal-turbop.md
url: https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa
published: 2026-05-22
ingested: 2026-08-25
domains: [agents]
---

# AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer

AINews Twitter-recap issue highlighting a cluster of infrastructure funding/scale milestones the same week, framed as evidence that "boring" AI infrastructure — not just frontier model research — is where a lot of value creation is accruing.

## Influenced pages
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — new trend page

## Key claims extracted
- Turbopuffer: crossed $100M ARR in March, 19 months after $1M ARR, profitable, having raised under $1M
- Exa: raised $250M Series C at a $2.2B valuation (agent-oriented search/retrieval infrastructure)
- Modal: raised $355M Series C at a $4.65B valuation
- Hark: raised $700M at a $6B valuation (GPU infrastructure, robotics, hardware, personal-intelligence products); reported a 200-hour uninterrupted autonomous robotics run for "F.03," with limited technical detail
- Daytona's pitch (from the companion Daytona episode) summarized again here: 60ms sandboxes, 50K sandbox startups in 75 seconds, RL/evals now roughly half of usage
- (Not actioned from this issue) OpenAI Erdős math discussion, RAEv2, Gated DeltaNet-2, and other pure-research items — see the companion benchmarks proposal and the triage's "noted but not made into signals" list
```

### wiki/sources/newsletters/superhuman-autonomous-growth-agent-2026-05-21.md (new)

```md
---
title: "Meet the autonomous growth agent (Superhuman)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-21-meet-the-autonomous-growth-agent.md
url: https://www.superhuman.ai/p/tempo-launches-an-ai-head-of-growth
published: 2026-05-21
ingested: 2026-08-25
domains: [agents]
---

# Meet the autonomous growth agent (Superhuman)

Superhuman AI newsletter issue whose lead story is Tempo's autonomous "AI head of growth" agent (a separate, unrelated signal — not actioned by this proposal). This summary extracts only item 3 of the issue: OpenAI's Guaranteed Capacity announcement.

## Influenced pages
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — one supporting data point in the funding-wave/compute-commitment cluster

## Key claims extracted
- OpenAI launched "Guaranteed Capacity": enterprises can lock in long-term access to OpenAI compute for building AI products, agents, and workflows
- Commitments run 1-3 years, with discounts that increase based on annual spend
- (Not actioned from this issue) Tempo's autonomous growth agent; Google's Gemini-3.5-Flash-powered search-box redesign
```

## Schema / vocabulary additions

None needed. `domains: [agents]` and `tags: [agentic]` already exist in the controlled vocabulary.

## Open questions

- Per the advisor's judgment call, I did **not** create standalone tool pages for Daytona, Modal, or Railway. Each would need a `subcategory` and none of the existing ones (`agentic-devops`, `agent-orchestration`, `computer-use`, etc.) cleanly fits "agent sandbox/compute-execution provider" — that's the discriminating constraint. If you want dedicated tool pages, I'd propose a new subcategory (e.g. `agent-sandbox-infra`) for approval first.
	- Yes, create the subcategory and pages
- `as_of` on the new trend page is set to 2026-07-08 (the newest of the five sources, the Modal podcast). The Daytona/Railway podcast recording dates themselves are not stated in the transcripts — I used the newsletter's `received` date as a proxy in each case.
	- Ok

