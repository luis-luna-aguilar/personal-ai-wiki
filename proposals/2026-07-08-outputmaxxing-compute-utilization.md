---
type: proposal
source:
  - raw/newsletters/2026-06-18-the-professor-of-outputmaxxing-anjney-midha-amp.md
  - raw/newsletters/2026-05-27-ainews-new-ai-infra-decacorns-fireworks-basete.md
status: pending
created: 2026-07-08
---

# Proposal: Outputmaxxing and compute utilization

## Summary

The AMP/outputmaxxing interview adds an infrastructure nuance to the compute-moat trend: raw GPU ownership is not enough if utilization, scheduling, power, and systems design are poor. This proposal updates the compute-infrastructure trend and model dashboard.

## Intended changes

- [ ] **Update** `wiki/trends/compute-infrastructure.md` - add outputmaxxing/utilization section.
- [ ] **Update** `wiki/state-of/models.md` - add recent-change note about compute utilization as a model-lab bottleneck.
- [ ] **Create** `wiki/sources/newsletters/outputmaxxing-amp-compute-utilization-2026-06.md` - source summary.

## Page drafts

### wiki/trends/compute-infrastructure.md (updated sections)

```md
---
as_of: 2026-06-18
sources: [..., outputmaxxing-amp-compute-utilization-2026-06]
---

## Current status (as of 2026-06-18)

Add:

- Compute moat is not only cluster size. AMP's "outputmaxxing" thesis argues that utilization, scheduling, power, and systems coordination determine how much useful work a lab extracts from its GPUs.
- The source frames future AI infrastructure as more grid-like: FLOPs flowing across capacity similar to electricity, with scheduling and market coordination becoming core infrastructure problems.

## Outputmaxxing

Outputmaxxing is the discipline of maximizing useful model-training or inference output from fixed compute capacity. In AMP's framing, labs can own enormous clusters and still waste capacity through poor MFU, scheduling friction, power constraints, or insufficient systems coordination.

The useful wiki update is not to treat AMP's exact MFU anecdotes as settled facts. The durable point is that frontier compute advantage is becoming a systems problem: GPU supply, memory, networking, workload scheduling, power, and utilization all affect model progress.

## Recent changes

- [2026-06-18] Added outputmaxxing / compute-utilization framing from AMP: the frontier compute bottleneck includes MFU, scheduling, power, and grid-like coordination, not only GPU count.
```

### wiki/state-of/models.md (updated sections)

```md
---
as_of: 2026-06-18
sources: [..., outputmaxxing-amp-compute-utilization-2026-06]
---

## Recent changes

- [2026-06-18] Outputmaxxing coverage adds compute-utilization nuance: frontier lab advantage depends on scheduling, MFU, power, and systems coordination, not only announced GPU capacity.
```

### wiki/sources/newsletters/outputmaxxing-amp-compute-utilization-2026-06.md (new)

```md
---
title: The Professor of Outputmaxxing - Anjney Midha / AMP
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-18-the-professor-of-outputmaxxing-anjney-midha-amp.md
url: https://www.latent.space/p/amp
published: 2026-06-18
ingested: 2026-07-08
domains: [models]
---

# The Professor of Outputmaxxing - Anjney Midha / AMP

Latent Space's AMP interview argues that frontier AI progress depends on extracting useful output from available compute, not only on buying more GPUs. The interview frames utilization, scheduling, power, and grid-like coordination as central AI infrastructure problems.

## Influenced pages

- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) - outputmaxxing/utilization section
- [State of Models](../../state-of/models.md) - recent-change note

## Key claims extracted

- The source frames compute utilization as a major bottleneck for frontier labs.
- AMP wants AI compute to behave more like grid infrastructure, where capacity is scheduled and routed efficiently.
- The durable claim is systems-level: MFU, scheduling, power, memory, and networking shape model progress.
```

## Open questions

- Should `outputmaxxing` become a standalone concept page if more sources use the term, or stay inside compute infrastructure for now?
