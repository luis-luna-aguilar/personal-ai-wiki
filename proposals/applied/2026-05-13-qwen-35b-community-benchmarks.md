---
type: proposal
sources:
  - raw/newsletters/2026-05-13-ainews-the-end-of-finetuning.md
status: pending
created: 2026-05-13
---

# Proposal: Qwen 3.6 35B A3B community benchmarks — leads the ~20GB local tier

## Summary

Community benchmarks (r/LocalLLaMA, week of May 13) comparing Qwen 3.6 35B A3B, Qwen 3.6 27B, Gemma 4 26B A4B, and Nvidia Nemotron 3 Nano on paper-to-code comprehension and long-context tasks. Qwen 3.6 35B A3B judged strongest overall; all four substantially outperform previous baselines like Devstral Small 2. Practical note: 35B ~20GB at q4; Gemma 26B ~15GB faster for chat; performance sensitive to temperature and quantization settings.

## Intended changes

- [x] **Update** `wiki/models/qwen-3-6-35b-a3b.md` — add community benchmark data; update `as_of` and `sources`
    > See diff snippets below

- [x] **Create** `wiki/sources/newsletters/qwen-35b-community-benchmarks-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/models/qwen-3-6-35b-a3b.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-04-22`
> **After:** `as_of: 2026-05-13`

**Frontmatter `sources` — append:**
> Add `qwen-35b-community-benchmarks-2026-05-13`

**Current status — append after the last bullet (before `## Qwen 3.6 Max Preview`):**
```
- **Community benchmarks (May 2026, r/LocalLLaMA):** strongest overall in the ~20GB local tier on paper-to-code comprehension and long-context tasks; evaluated against Qwen 3.6 27B, Gemma 4 26B A4B, and Nvidia Nemotron 3 Nano — all four substantially outperform prior baselines like Devstral Small 2
- **Practical setup:** ~20GB at q4 quantization; Gemma 4 26B is ~15GB and faster for chat tasks; users running both on a single machine simultaneously; performance is notably sensitive to temperature and quantization settings — small changes can shift results meaningfully
```

**Recent changes — prepend:**
```
- [2026-05-13] Community benchmarks (r/LocalLLaMA): judged strongest in ~20GB local tier on paper-to-code and long-context; all four tested models (35B A3B, 27B, Gemma 26B, Nemotron 3 Nano) beat Devstral Small 2; performance sensitive to temperature/quantization
```

### wiki/sources/newsletters/qwen-35b-community-benchmarks-2026-05-13.md (new)

```markdown
---
title: Qwen 3.6 35B A3B community benchmarks — May 2026 local-tier comparison
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-13-ainews-the-end-of-finetuning.md
published: 2026-05-13
ingested: 2026-05-13
domains: [models, coding]
---

# Qwen 3.6 35B A3B community benchmarks — May 2026 local-tier comparison

AINews newsletter (May 13) includes a summary of r/LocalLLaMA community benchmarks for the ~20GB local model tier. Primary source: https://www.reddit.com/r/LocalLLaMA/ (week of May 13, 2026).

## Influenced pages

- [Qwen 3.6 35B-A3B](../../models/qwen-3-6-35b-a3b.md) — community benchmark data added

## Key claims extracted

- Task: paper-to-code comprehension and long-context evaluation
- Models compared: Qwen 3.6 35B A3B, Qwen 3.6 27B, Gemma 4 26B A4B, Nvidia Nemotron 3 Nano
- Winner: Qwen 3.6 35B A3B judged strongest overall across the tested tasks
- Baseline improvement: all four models substantially outperform Devstral Small 2
- Practical size: Qwen 3.6 35B A3B ~20GB at q4; Gemma 4 26B ~15GB (faster for chat)
- Multi-model setup: users running Qwen 35B and Gemma 26B simultaneously on one machine
- Caveat: Qwen 35B thinking mode can be verbose and slow; performance sensitive to temperature and quantization settings
- Source: community evaluations from r/LocalLLaMA, not a formal benchmark study
```

