---
title: Podcast direction — how this wiki becomes audio
type: meta
as_of: 2026-04-22
---

# Podcast direction

Goal: ingest this wiki as **three ~40-minute podcasts**, each one narrow enough that a single listen reinforces a coherent slice of the knowledge base. No filler, no outside content — everything sourced from `wiki/` only.

The split below is deliberate: each block has its own job, its own vocabulary, and its own "what should stick after one listen" test. Block intros are prepended to the generated PDF so the podcast tool uses them as framing.

## The three blocks

### Block 1 — State of Play
**File:** `podcast/block-1-state-of-play.md`
**Sources:** `wiki/state-of/*.md`, `wiki/models/*.md`, `wiki/benchmarks/*.md`
**Objective:** Keep a live mental map of who leads each domain right now and which frontier models matter. After listening, the user should be able to answer "what's the current leader for X?" without looking anything up.

### Block 2 — Tools & Workflows
**File:** `podcast/block-2-tools-workflows.md`
**Sources:** `wiki/tools/*.md`, `wiki/workflows/*.md`
**Objective:** Know which specific tools to reach for in practice and how to compose them. After listening, the user should have a short mental shortlist per job-to-be-done and know the reusable patterns that chain them together.

### Block 3 — Concepts, Trends & Enablement
**File:** `podcast/block-3-concepts-trends-training.md`
**Sources:** `wiki/concepts/*.md`, `wiki/trends/*.md`, `wiki/training/*.md`
**Objective:** Stay oriented to where the field is heading and how to bring teams along. After listening, the user should know which ideas are becoming load-bearing, which trends to watch, and the current playbooks for rolling AI out inside a company.

## How to generate

```bash
# from the wiki root
scripts/build_podcast.sh 1      # builds block 1
scripts/build_podcast.sh 2
scripts/build_podcast.sh 3
scripts/build_podcast.sh all    # builds all three
```

Outputs land in `podcast/out/`:
- `podcast/out/block-N-<slug>.md` — concatenated source (intro + all wiki files)
- `podcast/out/block-N-<slug>.html` — formatted HTML (always produced)
- `podcast/out/block-N-<slug>.pdf`  — PDF (if a PDF engine is installed)

## What's excluded on purpose

- `wiki/history/` — archived, stale by design
- `wiki/sources/` — source summaries, already reflected in the pages we include
- `wiki/log.md`, `wiki/index.md` — meta / navigation, not content
- `wiki/_schema/` — controlled vocabulary, not listening material
- `raw/`, `proposals/`, `personal/`, `manual/` — not part of the factual wiki narrative

## Updating the split

If a new top-level folder appears under `wiki/` (e.g. `benchmarks/` fills up, or a new `patterns/` folder is added), update both:

1. The relevant block's `Sources:` line above.
2. The `case` branch in `scripts/build_podcast.sh`.

Keep the three-block shape unless a block's word count grows past ~15k words — at that point split it, don't stretch the listen.
