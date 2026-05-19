---
title: "Project Glasswing: what Mythos showed us"
type: source
source_type: article
source_file: raw/articles/2026-05-19-blogcloudflarecom-cyber-frontier-models.md
url: https://blog.cloudflare.com/cyber-frontier-models/
published: 2026-05-19
ingested: 2026-05-19
domains: [cybersecurity, agents]
---

# Project Glasswing: what Mythos showed us

Cloudflare's first-party writeup of using Mythos Preview (via Anthropic's Project Glasswing program) to scan 50+ of their own repositories. Covers two headline capabilities (exploit chain construction and autonomous proof generation loop), the signal-to-noise problem, why generic coding agents fail at security coverage, and the 8-stage harness Cloudflare built to achieve high-coverage research at scale. Also covers organic refusal inconsistency and the architectural resilience takeaway.

## Influenced pages

- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — operational findings; exploit chain construction; proof loop; refusal inconsistency
- [State of Cybersecurity](../../state-of/cybersecurity.md) — Glasswing updated with harness detail; architectural resilience takeaway
- [Harness (concept)](../../concepts/harness.md) — 8-stage narrow-scope parallel harness as worked example

## Key claims extracted

- Mythos chains low-severity primitives into working exploits (exploit chain construction) — prior frontier models stopped short
- Proof generation loop: write PoC → compile → run → read failure → adjust → retry, autonomously
- Organic refusals are probabilistically inconsistent; same task framed differently can produce opposite outcomes
- A generic coding agent against a large repo covers ~0.1% of surface before context fills — wrong shape for security research
- Harness stages: Recon → Hunt (~50 concurrent) → Validate (adversarial, no new findings) → Gapfill → Dedupe → Trace (reachability per consumer repo) → Feedback → Report
- Main defender takeaway: architectural resilience (defenses-in-front, isolation, simultaneous rollout) > patch speed
