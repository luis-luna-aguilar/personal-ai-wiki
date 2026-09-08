---
type: proposal
source: raw/newsletters/2026-08-22-ainews-10-worse-100x-cheaper-10000x-faster-w.md
status: pending
created: 2026-09-07
---

# Proposal: DeepSeek-V4-Flash-Vision-Exp adds multimodal input

## Summary

### The source

The same AINews issue that frames Simile's human-simulation work (covered in a companion proposal) also carries a straightforward product update: DeepSeek shipped DeepSeek-V4-Flash-Vision-Exp, adding multimodal (text+image) input to its V4-Flash line while reportedly preserving V4-Flash's existing text capability. AINews-reported benchmarks show a large jump over the prior V4-Flash-0731 release — 83.9 on Terminal-Bench 2.1, 75.9 on Toolathlon-Verified, 64.3 on Chartography — positioned as closing the multimodal-agent gap to Claude Opus-4.8. The release ships with mixed text+image API support (images billed at up to 384 tokens each, at V4-Flash pricing) and a new Files API for reusable image uploads across requests. As of the source's writing, the model's weights weren't yet found on Hugging Face, so it appears to be API-only rather than a full open-weight drop like DeepSeek's prior releases.

### What changes

The wiki already tracks DeepSeek V4 on `models/deepseek-v4.md`, most recently updated for V4 Pro's general availability on 2026-08-13. This is a straightforward version bump.

- **DeepSeek V4** gains a new dated subsection for the Vision-Exp multimodal update and a matching Recent-changes entry. Page date moves to 22 August. The page's Recent-changes list (5 entries) is well under its 10-entry cap, so no spill is needed.

### What to weigh

The benchmark numbers and the "closing the gap to Opus-4.8" framing are AINews's relay of DeepSeek's own release claims, not an independent evaluation — consistent with how this page already treats DeepSeek's self-reported figures elsewhere. Weights not being found on Hugging Face at ingest time is noted as a snapshot, not a settled fact — it may simply not have propagated yet.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/models/deepseek-v4.md` — add Vision-Exp subsection, Recent-changes entry, bump as_of
    > See draft below

## Page drafts

### wiki/models/deepseek-v4.md (updated)

> **Frontmatter:** `as_of: 2026-08-13` → `as_of: 2026-08-22`; append `ainews-10-worse-100x-cheaper-2026-08-22` to `sources:`.

> New subsection, inserted after `## V4 Pro general availability (as of 2026-08-13)` and before `## Strengths`:

```md
## V4-Flash-Vision-Exp adds multimodal (as of 2026-08-22)

DeepSeek shipped DeepSeek-V4-Flash-Vision-Exp, adding multimodal (text+image) input to V4-Flash while reportedly preserving its existing text capability:

- **Benchmarks (per AINews, relaying DeepSeek's release claims):** 83.9 Terminal-Bench 2.1, 75.9 Toolathlon-Verified, 64.3 Chartography — a large jump over the prior V4-Flash-0731 release, positioned as closing the multimodal-agent gap to Claude Opus-4.8
- **API:** mixed text+image support via base64, external URLs, or a new Files API for reusable image uploads across requests; images billed at up to 384 tokens each, at V4-Flash pricing
- **Availability:** live via the DeepSeek API (`model='deepseek-v4-flash-vision-exp'`); weights not yet found on Hugging Face as of this writing, unlike DeepSeek's prior fully open-weighted releases
```

> **Recent changes:** add as the newest entry:
```md
- [2026-08-22] V4-Flash-Vision-Exp adds multimodal (text+image) input while preserving V4-Flash's text capability; reported benchmarks (83.9 Terminal-Bench 2.1, 75.9 Toolathlon-Verified, 64.3 Chartography) position it as closing the multimodal-agent gap to Opus-4.8; API-only at launch, weights not yet found on Hugging Face.
```

> **Sources** (append):
```md
- [AINews — 10% worse, 100x cheaper, 10000x faster: Why Simulation is taking over](../sources/newsletters/ainews-10-worse-100x-cheaper-2026-08-22.md)
```

## Open questions

- None beyond the sourcing note above.
