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
