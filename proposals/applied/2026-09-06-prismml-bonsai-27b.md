---
type: proposal
sources:
  - raw/newsletters/2026-07-14-ainews-not-much-happened-today.md
  - raw/newsletters/2026-07-15-gpt-56-is-raising-concerns.md
status: pending
created: 2026-09-06
---

# Proposal: PrismML's Bonsai 27B — a 27B-class model that runs on a phone

## Summary

### The source

PrismML, a California startup, took Alibaba's Qwen 3.6 27B and compressed it down to two Apache-2.0 variants: "Ternary Bonsai 27B" at 5.9GB (1.71 effective bits per parameter) and a "1-bit Bonsai 27B" at just 3.9GB (1.125 effective bits). The company's headline claim is that the 1-bit version is small enough to run on an iPhone 17 Pro while retaining 90% of the original model's performance — billed as the first 27B-class model that runs on a phone. A developer-preview API is already live via Together AI.

### What changes

The wiki's `concepts/quantization.md` page explains the technique (FP32→FP16→INT8→INT4, the standard ~4x-smaller/~2x-faster/5-10%-accuracy-loss tradeoff) and already tracks one concrete example of aggressive quantization enabling local/offline agents. Bonsai 27B is a sharper data point than anything currently on the page — going below INT4 to sub-2-bit and landing on a phone rather than a workstation:

- **Quantization** gains one new bullet with Bonsai 27B's specific numbers (two variants, sizes, effective bits, retained-performance claim, phone target). Page moves to 15 July.
- One new source page (both raw newsletters cover the same release from different angles, so a single source page draws from both).

### What to weigh

The 90%-performance-retained figure is PrismML's own claim, not independently benchmarked — the draft attributes it as such. Neither raw newsletter names a specific evaluation this 90% figure comes from.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/quantization.md` — add one bullet on Bonsai 27B's sub-2-bit quantization and phone deployment; bump `as_of` to 2026-07-15; add a Recent-changes section (page currently has none); add the new source
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/prismml-bonsai-27b-2026-07.md` — source summary

## Page drafts

### wiki/concepts/quantization.md (updated)

Frontmatter:

```yaml
as_of: 2026-07-15
sources: [ngrok-quantization, local-offline-agents-2026-04-29, prismml-bonsai-27b-2026-07]
```

`## Local agent feasibility (as of 2026-04-29)` — add a new paragraph at the end of this section:

```md
A July 2026 example pushes past standard INT4: PrismML compressed Alibaba's Qwen 3.6 27B into two Apache-2.0 variants — "Ternary Bonsai 27B" (5.9GB, 1.71 effective bits/parameter) and a "1-bit Bonsai 27B" (3.9GB, 1.125 effective bits) — claiming the 1-bit variant fits on an iPhone 17 Pro at 90% of the original model's performance (PrismML's own figure, not independently benchmarked). A developer-preview API is available via Together AI. Billed as the first 27B-class model that runs on a phone.
```

New section, added at the end of the page before `## Sources`:

```md
## Recent changes

- [2026-07-15] PrismML ships Bonsai 27B, a sub-2-bit quantization of Qwen 3.6 27B claimed to run on an iPhone 17 Pro at 90% of original performance.
```

Updated `## Sources` (full section):

```md
## Sources

- [Quantization from the ground up — ngrok blog](../sources/articles/ngrok-quantization.md)
- [Local and offline agents become more credible](../sources/newsletters/local-offline-agents-2026-04-29.md)
- [PrismML ships Bonsai 27B](../sources/newsletters/prismml-bonsai-27b-2026-07.md)
```

### wiki/sources/newsletters/prismml-bonsai-27b-2026-07.md (new)

```md
---
title: "PrismML ships Bonsai 27B"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-15-gpt-56-is-raising-concerns.md
url: https://prismml.com/news/bonsai-27b
published: 2026-07-15
ingested: 2026-09-06
domains: [models]
---

# PrismML ships Bonsai 27B

The Code's coverage of PrismML's Bonsai 27B, a sub-2-bit quantization of Qwen 3.6 27B small enough to target phone deployment; a second, earlier AINews issue (`raw/newsletters/2026-07-14-ainews-not-much-happened-today.md`) covers the same release with the two variants' exact size/bit specs.

## Influenced pages
- [Quantization](../../concepts/quantization.md) — added as a concrete sub-2-bit, phone-deployment example

## Key claims extracted
- Two variants: "Ternary Bonsai 27B" (5.9GB, 1.71 effective bits/parameter) and "1-bit Bonsai 27B" (3.9GB, 1.125 effective bits), both derived from Alibaba's Qwen 3.6 27B under Apache 2.0
- PrismML claims the 1-bit variant fits on an iPhone 17 Pro while retaining 90% of the original model's performance
- Billed as the first 27B-class model that runs on a phone
- A developer-preview API is available now via Together AI
```
