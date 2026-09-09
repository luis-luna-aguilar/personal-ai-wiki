---
type: proposal
source: raw/articles/2026-09-07-blogcloudflarecom-cloudflare-computer.md
status: pending
created: 2026-09-08
---

# Proposal: Cloudflare ships `@cloudflare/computer` — isolates over containers

## Summary

### The source

Cloudflare published an early-preview, open-source package called `@cloudflare/computer`, arguing that giving every agent its own container simply won't scale to the hundreds of millions, then billions, of concurrent agents Cloudflare expects — there isn't remotely enough global container compute for that, which is why Cloudflare frames current industry demand as "desperate, panicked" for CPU compute specifically, not just GPU. Its answer builds on a roughly decade-old architectural bet: isolates (the compute primitive behind Cloudflare Workers and Durable Objects), which spin up and tear down far faster than containers, can hibernate when idle, and can themselves spawn further isolates to run untrusted code. `@cloudflare/computer` gives an agent a durable, declaratively-defined virtual filesystem (backed by SQLite, populated from git repos or cloud storage) shared across two swappable execution backends: an isolate-based runtime (using a shell-to-JavaScript translator called `just-bash` inside a "Dynamic Worker") for file/git/data work, and a full-Linux container backend for anything needing `npm`, native binaries, or a real toolchain. All filesystem operations are gated, audited, and observed. Cloudflare's stated target: containers should be needed for under 10% of an agent's work, with coding tasks, audio/video manipulation, and document creation all handled by the cheaper, faster isolate path.

### What changes

`concepts/harness.md` already treats "execution environment" and sandboxed execution as part of the harness boundary; this proposal adds `@cloudflare/computer`'s isolates-vs-containers split as a concrete architectural example. `trends/agent-native-compute.md` already tracks Daytona, Modal, and Railway converging on agent-native infrastructure from different angles; this proposal adds Cloudflare's isolates argument as a fourth, distinctly infra-vendor-side data point for the same trend (Cloudflare's angle: a shared-filesystem abstraction across two backends, not a sandbox-provisioning speed record). `concepts/harness.md`'s Recent-changes list is already at its 10-entry cap, so this spills its oldest entry (whatever remains oldest at apply time, since two other proposals in this same batch also touch this page).

### What to weigh

Nothing beyond the sourcing itself — this is a primary Cloudflare engineering-blog post, one of the stronger-sourced items in this batch.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/harness.md` — add `@cloudflare/computer` bullet to "What good harness engineering looks like", bump `as_of`, add Recent-changes entry, spill oldest entry
    > See draft below

- [ ] **Spill** `wiki/concepts/harness.md` → `wiki/history/concepts/harness.md` — oldest Recent-changes entry falls off the 10-entry cap (whichever is oldest at apply time)
    > See draft below

- [ ] **Update** `wiki/trends/agent-native-compute.md` — add `@cloudflare/computer` as a fourth agent-native-infra data point, bump `as_of`, add Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/articles/cloudflare-computer-launch-2026-09-07.md` — source summary

## Page drafts

### wiki/concepts/harness.md (updated)

```md
---
as_of: 2026-09-07
sources: [..., cloudflare-computer-launch-2026-09-07]
---

## What good harness engineering looks like

(... existing bullets unchanged ...)

- **Isolates over containers as the default agent-runtime primitive.** Cloudflare's open-source `@cloudflare/computer` argues container-per-agent doesn't scale to hundreds of millions of concurrent agents, and gives agents a durable shared filesystem across two swappable execution backends: fast, cheap isolates (Cloudflare Workers/Durable Objects) for file/git/data work, and full-Linux containers only when npm, native binaries, or a real toolchain are actually needed. Target: containers handle under 10% of an agent's work.

## Recent changes

- [2026-09-07] Added Cloudflare's `@cloudflare/computer`: isolates-over-containers as the default agent-runtime primitive, with a shared filesystem across two swappable execution backends.
- (... existing entries follow, oldest entry spilled below ...)
```

### wiki/history/concepts/harness.md (updated)

```md
## Archived from current page on 2026-09-08

- (whichever Recent-changes entry is oldest on the live page at apply time)
```

### wiki/trends/agent-native-compute.md (updated)

```md
---
as_of: 2026-09-07
sources: [..., cloudflare-computer-launch-2026-09-07]
---

## Current status (as of 2026-09-07)

(... existing bullets unchanged ...)

- **Cloudflare's `@cloudflare/computer` (September 2026):** open-source, early-preview package arguing isolates — not containers — are the only agent-runtime primitive that scales to hundreds of millions or billions of concurrent agents; gives agents a durable shared filesystem across a fast isolate backend and a full-Linux container backend, targeting under 10% of agent work needing a container at all. A distinct angle on this trend from Daytona/Modal/Railway: a shared-filesystem abstraction across backend types, rather than a sandbox-provisioning speed record.

## Recent changes

- [2026-09-07] Cloudflare's `@cloudflare/computer`: isolates-over-containers agent runtime with a shared filesystem across two swappable execution backends, targeting under 10% container usage.
- (... existing entries follow ...)
```

### wiki/sources/articles/cloudflare-computer-launch-2026-09-07.md (new)

```md
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
```
