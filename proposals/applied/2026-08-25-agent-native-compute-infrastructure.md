---
type: proposal
source: raw/newsletters/2026-05-20-railway-the-agent-native-cloud-jake-cooper.md
status: pending
created: 2026-08-25
---

# Proposal: Agent-native compute infrastructure becomes its own category

## Summary

### The source

Between May and July 2026 the Latent Space podcast's "agent cloud" interview series made one shared argument: cloud built for human developers (Kubernetes) is a poor fit for agents, which need thousands of isolated sandboxes that start instantly, hold state, pause and vanish. Daytona's CEO Ivan Burazin (21 May) describes a pivot to "composable computers" for agents: ~60 ms to start a sandbox, 50,000 in ~75 seconds, a largest customer at ~850,000 a day. Half of Daytona's usage is now reinforcement-learning and eval runs that spike from zero to 100,000 CPUs and back, forcing ~15% mean utilization — an economics problem Burazin admits is unsolved. Modal's CTO Akshat Bubna (8 July), fresh off a $355M Series C, says the SDK team's mission has moved from "developer experience" to "agent experience," with RL rollouts needing 100,000 sandboxes. Railway's Jake Cooper (20 May) runs his own bare-metal data centres (~3-month payback, ~70% margins), ships copy-on-write production forks agents can test against, and argues "the pull request is dying."

AINews (22 May) adds the funding wave — Exa at $2.2B, Turbopuffer profitable at $100M ARR, Hark at $6B, Modal at $4.7B or $4.65B (the issue disagrees with itself) — and Superhuman (21 May) notes OpenAI's "Guaranteed Capacity" 1–3 year compute commitments.

### What changes

The wiki treats compute as a frontier-*training* moat and has no page for the execution layer agents run on, nor for these companies.

- **New trend page `trends/agent-native-compute.md`** frames sandboxes and RL/eval workload shapes as a category distinct from training-scale compute, and links the three tools, the funding wave and E2B. Dated 8 July.
- **Three new tool pages** — `tools/daytona.md` (22 May), `tools/modal.md` (8 July), `tools/railway.md` (20 May) — under a new subcategory `agent-sandbox-infra`.
- **State of Agents** gains an "Agent sandbox / compute infrastructure" section listing the three. Its Recent changes list is re-sorted and cut from 13 to the cap of 10; the four oldest (Multica, LangChain Interrupt, Anthropic SMB/Legal, Notion External Agents API) spill to history. Date stays 8 July.
- **Compute infrastructure as decisive competitive moat** gets a Related cross-link, one entry pointing to the spin-off, a re-sorted Recent changes list and a missing source link restored; date moves to 8 July.
- Five newsletter source pages; the Superhuman one covers only Guaranteed Capacity.

### What to weigh

Company figures are founder- or CTO-reported from one podcast transcript each and the funding numbers are AINews secondhand — attributed, not verified; the Daytona and Railway dates are newsletter receipt dates, as the transcripts give no recording date. The trend page and new state-of section link to the tool pages, so the tool Creates and the schema approval travel together. E2B sits under `agent-framework` and arguably belongs in the new cohort; I only cross-linked it. Two existing compute-infrastructure entries (Manus's durable runtime, "inference inflection") belong to the new page's scope but stay put.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [x] **Create** `wiki/trends/agent-native-compute.md` — a new trend page scoped to the *agent execution layer* (sandboxes, RL/eval workload shapes), distinct from `trends/compute-infrastructure.md`'s focus on frontier *training*-compute scale as a moat
    > See draft below

- [x] **Update** `wiki/trends/compute-infrastructure.md` — bump `as_of` to 2026-07-08 and the Current status heading to match; extend `sources:`/`## Sources`; add a `## Related` cross-link; reorder Recent changes newest-first and add one 2026-07-08 entry (9 entries, no spill)
    > See draft below

- [x] **Create** `wiki/tools/daytona.md` — agent sandbox provider (new subcategory `agent-sandbox-infra`)
    > See draft below

- [x] **Create** `wiki/tools/modal.md` — serverless AI cloud reframing toward "agent experience" (new subcategory `agent-sandbox-infra`)
    > See draft below

- [x] **Create** `wiki/tools/railway.md` — bare-metal deployment platform rebuilding for agents (new subcategory `agent-sandbox-infra`)
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add `### Agent sandbox / compute infrastructure` section with the three tools; extend `sources:`; add one 2026-07-08 Recent-changes entry; reorder Recent changes newest-first and trim to the 10-entry cap
    > See draft below

- [x] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — four oldest Recent-changes entries by date (2026-05-18 Multica, 2026-05-15 LangChain Interrupt, 2026-05-14 Anthropic SMB/Legal, 2026-05-14 Notion External Agents API) move to history
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

## Sources

- [Railway: The Agent-Native Cloud — Jake Cooper](../sources/newsletters/railway-agent-native-cloud-2026-05-20.md)
- [Giving Agents Computers — Ivan Burazin, Daytona](../sources/newsletters/daytona-giving-agents-computers-2026-05-21.md)
- [Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO](../sources/newsletters/modal-agent-experience-2026-07-08.md)
- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
- [Superhuman — Meet the autonomous growth agent (OpenAI Guaranteed Capacity mention)](../sources/newsletters/superhuman-autonomous-growth-agent-2026-05-21.md)
```

### wiki/trends/compute-infrastructure.md (updated)

Frontmatter — two fields change (`as_of` bumped; four source ids appended, the Superhuman source is not cited on this page):

```md
as_of: 2026-07-08
sources: [ainews-2026-04-21, runtime-improvements-improve-agent-economics, google-cloud-next-2026, ainews-2026-04-25, ai-earnings-capex-2026-04-30, inference-inflection-agent-runtime-2026-04-30, parallel-web-agent-apis-2026-04-30, persistent-cloud-computers-agents-2026-05-01, stripe-agent-native-commerce-fraud-2026-04-29, ainews-not-much-happened-2026-07-02, local-ai-infrastructure-2026-06, outputmaxxing-amp-compute-utilization-2026-06, railway-agent-native-cloud-2026-05-20, daytona-giving-agents-computers-2026-05-21, modal-agent-experience-2026-07-08, ainews-new-ai-infra-unicorns-2026-05-22]
```

`## Current status` heading — date brought in line with `as_of` (bullets unchanged):

```md
## Current status (as of 2026-07-08)
```

`## Related` (full section, one line added):

```md
## Related

- [Proprietary data becomes model moat](proprietary-data-becomes-model-moat.md) — a parallel structural-advantage thesis
- [Agent-native compute infrastructure](agent-native-compute.md) — the agent-execution-layer analog: sandboxes, RL/eval workload shapes, and the Daytona/Modal/Railway thesis plus the broader infra funding wave
```

`## Recent changes` — full section; existing entries reordered newest-first (the live page had 2026-06-18 above 2026-07-02) and one new entry added at the top; no existing entry reworded:

```md
## Recent changes

- [2026-07-08] Agent-execution-layer analog spun off into a dedicated page: [Agent-native compute infrastructure](agent-native-compute.md) covers Daytona/Modal/Railway sandbox economics, RL/eval workload shapes, and the infra funding wave (Exa, Turbopuffer, Hark, Modal).
- [2026-07-02] Added inference-systems counterforce: DSpark/vLLM, TwoTower, WebGPU Gemma, and kernel-level work show competition moving below model weights into runtime speed and serving economics.
- [2026-06-30] Added hybrid local/cloud routing as a compute-control counterforce for private, low-latency, repeated, or cheaper tasks.
- [2026-06-18] Added outputmaxxing / compute-utilization framing from AMP: the frontier compute bottleneck includes MFU, scheduling, power, and grid-like coordination, not only GPU count.
- [2026-05-05] Stripe frames stolen compute (API keys, tokens, credits, free trials) as the emerging AI fraud surface — "compute is the new cash"; agents as autonomous purchasers create new commerce and payment-flow design challenges
- [2026-05-05] Manus Cloud Computer: persistent Ubuntu environments with SSH/web-terminal access and tool state that survives across agent sessions; durable-agent runtime as an infrastructure category distinct from ephemeral-per-task containers
- [2026-05-05] Parallel Web Systems raised at a $2B valuation (secondary coverage) for internet/research APIs optimized for AI agents — market signal that agent-oriented web access infrastructure is becoming a standalone investable category
- [2026-05-05] AINews "inference inflection" framing: inference throughput is the dominant current bottleneck, and agent systems add a compound requirement — CPU, sandbox, browser, and execution capacity matter alongside GPU for production agent workloads
- [2026-05-05] Superhuman reports Q1 2026 Big Tech earnings (Alphabet, Amazon, Meta, Microsoft) show AI revenue materializing while capex continues climbing; treat directional signal as confirmed, specific figures as pending primary verification
```

(9 entries total; page remains under the 10-entry cap — no spill needed.)

`## Sources` — full section; adds the previously missing outputmaxxing link plus the four new sources:

```md
## Sources

- [AINews — Moonshot Kimi K2.6, Hermes Agent, Codex Chronicle (2026-04-21)](../sources/newsletters/ainews-2026-04-21.md)
- [Runtime improvements improve agent economics](../sources/newsletters/runtime-improvements-improve-agent-economics.md)
- [Google Cloud Next 2026 — TPU v8 and Gemini Enterprise Agent Platform](../sources/articles/google-cloud-next-2026.md)
- [AINews - DeepSeek V4 Pro and Flash](../sources/newsletters/ainews-2026-04-25.md)
- [Big Tech earnings and AI capex signal](../sources/newsletters/ai-earnings-capex-2026-04-30.md)
- [Inference inflection and agent runtime bottlenecks](../sources/newsletters/inference-inflection-agent-runtime-2026-04-30.md)
- [Parallel Web Systems as agent web API infrastructure](../sources/newsletters/parallel-web-agent-apis-2026-04-30.md)
- [Persistent cloud computers for agents](../sources/newsletters/persistent-cloud-computers-agents-2026-05-01.md)
- [Stripe agent-native commerce and compute fraud](../sources/newsletters/stripe-agent-native-commerce-fraud-2026-04-29.md)
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [Local AI as open-weight infrastructure](../sources/newsletters/local-ai-infrastructure-2026-06.md)
- [The Professor of Outputmaxxing - Anjney Midha / AMP](../sources/newsletters/outputmaxxing-amp-compute-utilization-2026-06.md)
- [Railway: The Agent-Native Cloud — Jake Cooper](../sources/newsletters/railway-agent-native-cloud-2026-05-20.md)
- [Giving Agents Computers — Ivan Burazin, Daytona](../sources/newsletters/daytona-giving-agents-computers-2026-05-21.md)
- [Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO](../sources/newsletters/modal-agent-experience-2026-07-08.md)
- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
```

### wiki/tools/daytona.md (new)

```md
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
```

### wiki/tools/modal.md (new)

```md
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
```

### wiki/tools/railway.md (new)

```md
---
title: Railway
type: tool
domains: [agents]
subcategory: agent-sandbox-infra
tags: [agentic]
as_of: 2026-05-20
sources: [railway-agent-native-cloud-2026-05-20]
---

# Railway

Railway is a deployment platform ("push code, get a URL") that is rebuilding network, compute, storage, and orchestration for an agent-native world. A 35-person team serves ~3M users adding ~100K signups/week; the company has raised $124M and runs most workloads on its own bare-metal data centers, bursting to public clouds when needed.

## Current status (as of 2026-05-20)

- Bare metal: ~3-month payback vs. cloud rental and ~70% margins that fund cloud bursting; a rebuilt network overlay straddles five clouds including Oracle, AWS, GCP, and Railway's own metal
- Central Station: internal system clustering customer feedback and incidents and routing them to the right team
- Agent-safe production forks: copy-on-write clones of production with PII transforms so agents can test changes against production-like state; progressive/shadow rollouts (0.1% → 1% → all) as first-class primitives
- Thesis: "the pull request is dying" — replaced by versioned, mergeable production changes; the CLI, not the canvas, becomes the primary agent input surface; agents with Railway CLI access can provision their own infrastructure

## Strengths

- Owns the full stack down to metal, which founder Jake Cooper frames as the economic basis for agent-scale workloads

## Weaknesses / caveats

- Suffered a major GCP-linked outage on 2026-05-19 (workload discoverability was still tied to GCP despite the multi-cloud mesh); post-mortem published
- Single founder interview as the only source; economics and user figures are self-reported

## Recent changes

- [2026-05-20] Latent Space interview: bare-metal economics, Central Station, agent-safe production forks, progressive rollouts, "the pull request is dying," CLI over canvas

## Sources

- [Railway: The Agent-Native Cloud — Jake Cooper](../sources/newsletters/railway-agent-native-cloud-2026-05-20.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter — `sources:` extended (append four ids; `as_of` stays 2026-07-08, already the newest source date):

```md
sources: [cursor-3-launch, advisor-strategy, stripe-cli, managed-agents, agentic-thinking-lin, curiosity-driven-imagination, openai-agents-sdk-evolution, ainews-2026-04-21, ainews-2026-04-22, claude-cowork-launch, every-managed-agents-vibe-check, claude-design-launch, orca-homepage, anthropic-platform-expansion-april-2026, coding-agent-control-planes, claude-productivity-surfaces, open-agent-orchestration-late-march, proof-agent-native-documents, cursor-cloud-agents-march, cursor-cloud-agents-february, google-adk, openai-deep-research, gemini-deep-research-max, futurehouse-homepage, uipath-maestro-introduction, anthropic-mcp, google-a2a, legacy-ai-tools-roadmap-xlsx, microsoft-foundry-agents-2026, google-cloud-next-2026, superhuman-2026-04-23, awsai-cowork-bedrock-2026-04-23, microsoft-copilot-agent-mode-office, claude-managed-agents-memory, agentic-devops-deep-research, agent-infrastructure-harness-2026-05-01, codex-for-work-2026-05-01, ai-managed-orchestration-local-browser-agents-2026-04-28, inference-inflection-agent-runtime-2026-04-30, persistent-cloud-computers-agents-2026-05-01, production-agent-orchestration-2026-04-29, hermes-openclaw-persistent-agents-2026-05-11, metr-long-horizon-2026-05-12, thinking-machines-interaction-2026-05-12, frontier-labs-deployment-services-2026-05-13, multica-repo, notion-external-agents-api-may-2026, langchain-interrupt-may-2026, devin-auto-triage-2026-05, papercliping, ainews-june-06-2026, vercel-agents-new-software-2026-07-03, ainews-not-much-happened-2026-07-02, the-code-devin-security-2026-07-02, claude-tag-slack-agent-2026-06, claude-cowork-mobile-2026-07, gemini-managed-agents-2026-07, kimi-goal-mode-creative-agents-2026-06, railway-agent-native-cloud-2026-05-20, daytona-giving-agents-computers-2026-05-21, modal-agent-experience-2026-07-08, ainews-new-ai-infra-unicorns-2026-05-22]
```

New subsection, inserted under `## Subcategories` immediately after `### Agentic DevOps` and before `### Agent-native documents`:

```md
### Agent sandbox / compute infrastructure

Managed compute providers whose core product is execution environments purpose-built for agents: instant-start, stateful, isolated sandboxes and agent-operable cloud primitives that scale from zero to tens of thousands of concurrent instances for background-agent and RL/eval workloads. See [Agent-native compute infrastructure](../trends/agent-native-compute.md) for the trend view.

- [Daytona](../tools/daytona.md) — bare-metal sandboxes on its own scheduler; ~60ms startup, 50K sandboxes in ~75s, largest customer ~850K/day; RL/eval now ~50% of usage; Windows/macOS computer-use sandboxes in progress *(as of 2026-05-22)*
- [Modal](../tools/modal.md) — serverless AI cloud reframing from developer to "agent experience"; 100K-sandbox RL rollouts, sidecars, 17-cloud capacity pool; $355M Series C *(as of 2026-07-08)*
- [Railway](../tools/railway.md) — bare-metal deployment platform with copy-on-write production forks, progressive rollouts, and a CLI-first agent interface *(as of 2026-05-20)*
```

`## Recent changes` — full section; one new entry at the top, existing entries reordered newest-first, trimmed to the 10-entry cap (the four oldest by date spill to history, see below); no retained entry reworded:

```md
## Recent changes

- [2026-07-08] Added `Agent sandbox / compute infrastructure` subcategory with [Daytona](../tools/daytona.md), [Modal](../tools/modal.md), and [Railway](../tools/railway.md); agent execution-layer providers now tracked here and in [Agent-native compute infrastructure](../trends/agent-native-compute.md)
- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
- [2026-07-08] Google managed agents in the Gemini API add MCP support, background execution, custom function calling, and credential refresh, making hosted agent runtime features first-party Gemini primitives.
- [2026-07-03] Vercel eve interview adds an agent-framework signal: agents as a new software category needing resumability, long-running jobs, skills, sandboxes, observability, and evals.
- [2026-07-02] Devin Security Swarm showed Agentic MapReduce applied to enterprise security: fan out bounded agents, aggregate findings, validate exploitability, and hand humans reviewable PRs.
- [2026-07-02] OpenWiki and wiki memory reinforce maintained codebase documentation as an agent context layer.
- [2026-06-24] Claude Tag beta makes Slack a multiplayer Anthropic agent surface: Claude can be tagged into threads with selected channel/tool/data/codebase access.
- [2026-06-19] Kimi Work adds Goal Mode, a long-running desktop-agent loop that continues until the user-defined objective is reached.
- [2026-06-06] New benchmarks: SWE-Marathon (1B-token budget, long-horizon software projects); Meta-Agent Challenge (anti-reward-hacking); Princeton ICML 2026: top models still unreliable on repeated identical tasks
- [2026-05-19] Devin Auto-Triage: Cognition ships always-on session-persistent bug triage agent; Slack monitoring + parent/child Devin structure + long-term deduplication memory
```

(10 entries total — at the cap.)

### wiki/history/state-of/agents.md (updated — spill append)

Append the following four entries (verbatim from the live page, original dates) to the end of the file:

```md
- [2026-05-18] Multica launches
- [2026-05-15] LangChain Interrupt cluster: SmithDB (purpose-built agent trace DB, 12-15× faster, DataFusion+Vortex), LangSmith Engine (trace→cluster→fix loop), LangChain Labs (continual learning from production traces, Prime Intellect partnership) as open-source managed-agents platform: agents are first-class project-board members, not just CLI tools; Squads abstraction routes work through a leader agent; skills compound across sessions
- [2026-05-14] Anthropic launched Claude for Small Business and Claude for Legal on Cowork: 27 one-click agentic workflows; first direct vertical automation bundles targeting end-users rather than developers
- [2026-05-14] Notion External Agents API: Claude Code, Cursor, Codex, Devin, Warp, Decagon can now operate inside Notion workspaces via secure Workers sandbox — Notion joins Proof as an agent-native document surface
```

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

Latent Space podcast transcript with Railway founder/CEO Jake Cooper. Railway (35-person team, ~3M users, ~100K signups/week, $124M raised) is rebuilding cloud infrastructure — network, compute, storage, orchestration — for an agent-native world, arguing agents need the same primitives humans did (versioning, observability, feature flags) but "moving 1,000 times quicker."

## Influenced pages
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — new trend page
- [Railway](../../tools/railway.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new `Agent sandbox / compute infrastructure` section
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — cross-link and Recent-changes entry

## Key claims extracted
- Company scale: 35 people, ~3M users, ~100K signups/week, $124M raised; most workloads moved onto Railway's own bare-metal data centers
- Bare-metal data centers: ~3-month payback period vs. cloud rental, ~70% margins subsidizing cloud bursting; network overlay rebuilt to straddle five clouds (Oracle, AWS, GCP, Railway's own metal, one more)
- Central Station: Railway's internal system for clustering customer feedback and incidents and routing them to the right internal team
- Agent-safe production forks: copy-on-write clones of production (with PII marked for transform when the database is cloned) that let an agent test changes as close to prod as possible without risking it
- Progressive/shadow rollouts as a first-class primitive so agents (and their mistakes) can be tested at 0.1% → 1% → full rollout
- Thesis: "the pull request is dying" — the push-pull-rebuild loop is being replaced by versioned, mergeable production changes
- CLI, not canvas, is becoming the primary agent input; the canvas becomes an output/context-anchor
- Self-replicating infrastructure: an agent with Railway CLI access can provision its own new infrastructure and deploy itself
- Episode intro notes a major Railway outage on 2026-05-19 caused by workload discoverability still being tied to GCP despite a multi-cloud mesh; post-mortem published
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

AINews Twitter-recap issue (covering 2026-05-20 to 2026-05-21) highlighting a cluster of infrastructure funding/scale milestones the same week, framed as evidence that "boring" AI infrastructure — not just frontier model research — is where a lot of value creation is accruing. This summary covers only the infra-funding cluster and the Daytona recap; the issue's research items are out of scope here.

## Influenced pages
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — new trend page (funding-wave bullet)
- [Modal](../../tools/modal.md) — Series C valuation
- [Daytona](../../tools/daytona.md) — recap of the Daytona pitch
- [State of Agents](../../state-of/agents.md) — new `Agent sandbox / compute infrastructure` section
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — cross-link and Recent-changes entry

## Key claims extracted
- Turbopuffer: crossed $100M run-rate in March, 19 months after $1M ARR, profitable, having raised under $1M
- Exa: raised $250M Series C at a $2.2B valuation (agent-oriented search/retrieval infrastructure)
- Modal: raised a $355M Series C; the issue's header says $4.7B valuation, the body says $4.65B
- Hark: raised $700M at a $6B valuation (GPU infrastructure, future model development, hardware, multimodal/personal-intelligence products); also reported a 200-hour uninterrupted autonomous run for "F.03," with limited technical detail
- Daytona's pitch (from the companion Daytona episode) summarized again here: 60ms sandboxes, 50K sandbox startups in 75 seconds, RL/evals now roughly half of usage
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
- OpenAI launched "Guaranteed Capacity": enterprises can lock in long-term access to OpenAI compute for producing AI products, agents, and workflows
- Commitments run one to three years, with discounts that increase based on annual spend
- Out of scope for this summary: Tempo's autonomous growth agent; Google's Gemini 3.5 Flash-powered intelligent search box replacing "ten blue links"
```

## Schema / vocabulary additions

- [x] Add new subcategory `agent-sandbox-infra` to `wiki/_schema/subcategories.md` (also append the slug to the "Declared slugs" line):

```md
### agent-sandbox-infra
- **Parent domain(s):** agents
- **Applies to types:** tool
- **Definition:** Managed compute providers whose core product is execution environments purpose-built for AI agents — instant-start, stateful, isolated sandboxes or agent-operable cloud primitives that scale from zero to tens of thousands of concurrent instances for background-agent and RL/eval workloads.
- **Examples:** [Daytona](../tools/daytona.md), [Modal](../tools/modal.md), [Railway](../tools/railway.md)
```

`domains: [agents]` and `tags: [agentic]` already exist in the controlled vocabulary; no other additions.

## Open questions

- Per the advisor's judgment call, I did **not** originally create standalone tool pages for Daytona, Modal, or Railway. Each would need a `subcategory` and none of the existing ones (`agentic-devops`, `agent-orchestration`, `computer-use`, etc.) cleanly fits "agent sandbox/compute-execution provider" — that's the discriminating constraint. If you want dedicated tool pages, I'd propose a new subcategory (e.g. `agent-sandbox-infra`) for approval first.
	- Yes, create the subcategory and pages
	- *(Implemented in this revision: `agent-sandbox-infra` schema item, three tool drafts, and the matching `state-of/agents.md` section + spill.)*
- `as_of` on the new trend page is set to 2026-07-08 (the newest of the five sources, the Modal podcast). The Daytona/Railway podcast recording dates themselves are not stated in the transcripts — I used the newsletter's `received` date as a proxy in each case.
	- Ok
- Should `tools/e2b.md` (currently `subcategory: agent-framework`) be re-homed into `agent-sandbox-infra` and listed in the new state-of section? Not done here; see Review flags.
