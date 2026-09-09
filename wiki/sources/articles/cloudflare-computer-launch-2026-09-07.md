---
title: "Your agent needs a computer, not a container — introducing @cloudflare/computer"
type: source
source_type: article
source_file: raw/articles/2026-09-07-blogcloudflarecom-cloudflare-computer.md
url: https://blog.cloudflare.com/cloudflare-computer/
ingested: 2026-09-08
domains: [agents]
---

# Your agent needs a computer, not a container — introducing @cloudflare/computer

Cloudflare open-sources an early-preview package giving agents a durable shared filesystem across two swappable execution backends: isolates (fast, cheap, Cloudflare Workers/Durable Objects) and full-Linux containers, arguing isolates are the only primitive that scales to hundreds of millions of concurrent agents.

## Influenced pages

- [Harness (agent)](../../concepts/harness.md) — isolates-over-containers architecture bullet
- [Agent-native compute infrastructure](../../trends/agent-native-compute.md) — fourth infra-vendor data point for the trend

## Key claims extracted

- Container-per-agent doesn't scale to hundreds of millions/billions of concurrent agents; not enough global container compute
- `@cloudflare/computer`: durable SQLite-backed virtual filesystem, two backends (isolate via `just-bash`, full-Linux container)
- Target: under 10% of agent work needs a container; isolates handle the rest
- All filesystem operations gated, audited, observed
