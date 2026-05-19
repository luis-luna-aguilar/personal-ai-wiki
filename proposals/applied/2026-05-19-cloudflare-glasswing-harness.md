---
type: proposal
source: raw/articles/2026-05-19-blogcloudflarecom-cyber-frontier-models.md
status: pending
created: 2026-05-19
---

# Proposal: Cloudflare Project Glasswing — Mythos harness architecture

## Summary

Cloudflare published a detailed first-party writeup of using Mythos Preview against 50+ of their own repositories under Project Glasswing. Key findings: Mythos chains low-severity bugs into working exploits autonomously (a new kind of capability vs prior frontier models), and its organic refusals are probabilistically inconsistent — insufficient as a safety boundary alone. Cloudflare built an 8-stage harness (Recon → Hunt → Validate → Gapfill → Dedupe → Trace → Feedback → Report) using ~50 concurrent narrowly scoped agents.

## Intended changes

- [x] **Update** `wiki/models/claude-mythos-preview.md` — add Cloudflare operational findings (exploit chain construction, proof generation loop, inconsistent refusals, harness necessity)
    > See diff below

- [x] **Update** `wiki/state-of/cybersecurity.md` — add Cloudflare findings under `Frontier model capabilities (offensive)`; update Glasswing entry with operational detail; add harness architecture note; add "architectural resilience" takeaway
    > See diff below

- [x] **Update** `wiki/concepts/harness.md` — add Cloudflare's 8-stage security harness as a concrete worked example of narrow-scope parallel agents + adversarial second agent
    > See diff below

- [x] **Create** `wiki/sources/articles/cloudflare-glasswing-2026-05.md` — source summary page

## Page drafts

### wiki/models/claude-mythos-preview.md — additions to `## Current status` and `## Recent changes`

Add after the METR benchmark section:

````md
## Cloudflare Project Glasswing operational findings (May 2026)

Cloudflare red-teamed 50+ of their own repositories with Mythos Preview. Key observations:

- **Exploit chain construction** — Mythos chains multiple low-severity bugs into a single, higher-severity working proof of concept. Previous frontier models would identify interesting bugs but stop short of chaining them. This is the capability gap that distinguishes Mythos from Opus 4.7 / GPT-5.5 for security work.
- **Proof generation loop** — Mythos writes PoC code, compiles it in a scratch environment, runs it, reads failure output, adjusts, and retries autonomously. Finding a bug and proving it exploitable are both within scope.
- **Organic refusals are probabilistically inconsistent** — same task framed differently or presented in a different context can produce opposite outcomes. Refusals are real but not sufficient as a complete safety boundary; additional safeguards are required for any general deployment.
- **Generic coding agents are the wrong tool** — pointing a single coding agent at a large repo produces poor coverage. Mythos requires a harness with many narrow-scope concurrent agents to achieve meaningful security coverage.

Cloudflare's architectural takeaway: "Patching faster is not the answer." Defenses-in-front, component isolation, and simultaneous rollout matter more than compressing the patch cycle.
````

Add to `## Recent changes` (and spill oldest if needed):

```
- [2026-05-19] Cloudflare Project Glasswing detailed writeup: exploit chain construction, proof generation loop, inconsistent organic refusals, and 8-stage narrow-scope harness architecture confirmed
```

### wiki/state-of/cybersecurity.md — update `### Frontier model capabilities (offensive)`

Replace the Mythos line:

> **Before:**
> `- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview; autonomously found thousands of zero-days across major OSes and browsers without human steering; partners: Cisco, AWS, Microsoft; substantially above Opus 4.6 on CyberGym *(as of 2026-04-22)*`

> **After:**
> `- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview; autonomously found thousands of zero-days; chains low-severity bugs into working exploits (exploit chain construction); autonomous proof generation loop; partners: Cisco, AWS, Microsoft; Cloudflare used it across 50+ repos (Project Glasswing, May 2026) *(as of 2026-05-19)*`

Add under `### AI-assisted vulnerability detection` (after existing bullets):

```md
**Cloudflare Project Glasswing harness architecture (May 2026)**

Eight-stage harness Cloudflare built around Mythos Preview for large-scale repo security research:

| Stage | Role |
|---|---|
| Recon | Architecture document; trust boundaries; entry points; initial task queue |
| Hunt | ~50 concurrent narrowly scoped agents; each fans out to exploration subagents with PoC scratch env |
| Validate | Independent adversarial agent re-reads code to *disprove* findings; no ability to emit new findings |
| Gapfill | Re-queues areas touched but not covered thoroughly |
| Dedupe | Collapses findings sharing the same root cause |
| Trace | Per-consumer-repo reachability: "there is a flaw" → "there is a reachable vulnerability" |
| Feedback | Reachable traces become new hunt tasks in consumer repos |
| Report | Structured report against predefined schema; submitted to ingest API |

Key design lessons: narrow scope beats exhaustive single-agent; adversarial second agent reduces noise more than self-review; splitting "is this buggy?" from "can an attacker reach it?" produces better results than asking both together.
```

Add to `## Recent changes`:

```
- [2026-05-19] Cloudflare Project Glasswing: detailed harness architecture (8 stages, ~50 concurrent agents, adversarial validate agent); Mythos exploit chain construction and proof loop confirmed; organic refusals inconsistent as safety boundary; architectural resilience over patch speed as the defender takeaway
```

### wiki/concepts/harness.md — add to `## What good harness engineering looks like`

Add bullet:

```md
- **Narrow-scope parallel agents outperform exhaustive single agents in high-coverage tasks.** Cloudflare's Project Glasswing harness (8 stages, ~50 concurrent Mythos Preview agents) demonstrates this at security-research scale: each agent has one tightly scoped attack class + one target area; an independent adversarial agent validates but cannot emit new findings; root-cause deduplication collapses variant findings. The Trace stage further splits "is this buggy?" from "can an attacker reach this bug?"—a clean instance of decomposing a compound question into two separately answerable ones.
```

### wiki/sources/articles/cloudflare-glasswing-2026-05.md (new)

````md
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
````

## Open questions

- Should the full harness table also move to a standalone `wiki/workflows/` page, or is the concept/harness inline addition sufficient?
