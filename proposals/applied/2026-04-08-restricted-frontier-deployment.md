---
type: proposal
source: internal — synthesized from raw/newsletters/2026-04-08-ainews-anthropic-30b-arr-project-glasswing-a.md, raw/newsletters/2026-04-10-anthropics-claude-mythos-problem-dark-dna-unveil.md, raw/newsletters/2026-04-12-anthropic-mythos.md, raw/newsletters/2026-04-14-ainews-top-local-models-list-april-2026.md
status: pending
created: 2026-04-08
---

# Proposal: Restricted frontier deployment

## Summary

The strongest enduring signal from the Mythos / Glasswing cluster is not a stable product page for an unreleased model. It is a trend: frontier labs may increasingly split capability into broadly shipped models and strategically restricted ones when cyber or other offensive capability crosses a threshold.

That trend is not represented cleanly in the current wiki. A trend page is a better fit than an unreleased model page.

## Intended changes

- [x] **Create** `wiki/trends/restricted-frontier-deployment.md` — trend page on the emerging split between public frontier products and strategically withheld high-capability systems
  > See full draft below.

- [x] **Update** `wiki/state-of/models.md` — add a recent-changes note pointing to the new trend
  > See diff snippet below.

- [x] **Update** `wiki/index.md` — add the new trend and refresh counts
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/restricted-frontier-deployment.md` — source summary page
  > See full draft below.

## Page drafts

### wiki/trends/restricted-frontier-deployment.md (new)

```markdown
---
title: Restricted frontier deployment
type: trend
domains: [models, agents]
tags: [anthropic]
as_of: 2026-04-08
sources: [restricted-frontier-deployment]
---

# Restricted frontier deployment

The trend: frontier labs may increasingly stop treating "ship the latest model broadly" as the default endpoint. When a new system appears to cross a capability threshold in areas like cyber offense, labs may keep it restricted, deploy it selectively, or frame it more as a safety event than a normal product launch.

## Current signal

- Anthropic's Mythos / Glasswing cluster is the clearest current example in the wiki
- The captured sources repeatedly frame the model as materially stronger on cyber or coding-adjacent offensive tasks than prior public systems
- The notable change is strategic behavior, not just model quality: limited release, heavier safety framing, and public discussion of why broad deployment is being constrained

## Why it matters

This could become a major structural shift in frontier AI. If labs increasingly maintain a split between public-facing models and restricted internal or selective-access systems, state-of pages cannot assume that the most capable system is always the most publicly available one.

## What to watch

- More explicit examples of labs withholding or tightly gating frontier models for capability reasons
- Whether restricted deployment becomes common outside cyber-risk narratives
- How this changes benchmarking, product positioning, and enterprise access patterns

## Open questions

- Is Anthropic the first durable example of this pattern, or just an unusually public one?
- How much of the Mythos story is actual deployment policy vs. launch-stage safety marketing?

## Sources

- [[sources/newsletters/restricted-frontier-deployment]]
```

### wiki/state-of/models.md (updated snippet)

```markdown
## Recent changes

- [2026-04-08] Mythos / Glasswing cluster suggests a new trend: frontier capability may increasingly be deployed selectively rather than broadly — see [[trends/restricted-frontier-deployment]]
- [2026-04-21] Added [[models/qwen-3-6-35b-a3b]] ...
```

### wiki/sources/newsletters/restricted-frontier-deployment.md (new)

```markdown
---
title: Restricted frontier deployment
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-08-ainews-anthropic-30b-arr-project-glasswing-a.md
ingested: 2026-04-08
domains: [models, agents]
---

# Restricted frontier deployment

This source summary captures the Mythos / Glasswing cluster as a strategic deployment signal rather than a normal product launch. The key takeaway is that labs may increasingly separate their most capable systems from their broadly available public products.

## Influenced pages

- [[trends/restricted-frontier-deployment]]
- [[state-of/models]]

## Key claims extracted

- Mythos / Glasswing is repeatedly framed as materially stronger on cyber or coding-adjacent offensive capability
- The public posture around the model is unusually safety-heavy and access-restrictive
- The deeper signal is the emergence of a public/private split in frontier deployment strategy
```

### wiki/index.md (updated snippet)

```markdown
## Trends

- [[trends/agents-reshape-organizations]] — ...
- [[trends/ai-in-science]] — ...
- [[trends/compute-infrastructure]] — ...
- [[trends/proprietary-data-becomes-model-moat]] — ...
- [[trends/restricted-frontier-deployment]] — frontier labs may increasingly withhold or selectively deploy their highest-capability systems rather than ship them broadly *(as_of: 2026-04-08)*

## Page count

- state-of: 7 (6 populated, 1 skeleton)
- models: 5
- tools: 17
- benchmarks: 0
- workflows: 2
- concepts: 8
- trends: 5
- training: 2

**Total content pages: 46.**
```

