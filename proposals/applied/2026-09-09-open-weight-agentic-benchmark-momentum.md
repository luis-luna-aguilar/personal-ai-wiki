---
type: proposal
sources:
  - raw/newsletters/2026-09-01-ainews-fals-h3-max-live-breaks-the-infinite-vid.md
  - raw/newsletters/2026-09-02-ainews-claude-fablemythos-51-new-sota-model.md
status: pending
created: 2026-09-09
---

# Proposal: Open-weight agentic-benchmark momentum

## Summary

### The source

Two AINews issues from the same week supply fresh agentic-benchmark placements for the open-weight models the wiki already tracks. Z.ai's GLM-5.3-Flash placed #19 overall and #4 among open models on Agent Arena, with a +4.6% net improvement over more than 9,000 real-world sessions, a $0.12 median cost per task, and no reported tool-hallucination issues; separately, Vals reported the broader GLM-5.3 family posting 95.4% on SWE-bench and 78.1% on Vibe Code Bench. Qwen3.8-Flash-Next placed #24 overall and #7 among open models on the same Agent Arena, with a +2.4% net improvement over 8,700+ sessions. Alibaba also pushed a refreshed flagship, Qwen3.8-Max-0902, to #1 on Arena's Code Arena: WebDev leaderboard (1691 Elo) — just ahead of Claude Opus 5 Max and Kimi K3 Max. And a Zhihu roundup adds detail to Tencent Hunyuan's open-source Hy4 Preview (770B total, 49B active, >1M context), reporting it closed much of its capability gap to the prior Hy3 generation in roughly seven weeks through post-training and agent-policy tuning alone, without base-model scaling.

### What changes

The wiki's GLM-5.3, Qwen 3.8, and Open-weight momentum broadens pages currently stop at late-August data (GLM-5.3-Flash's reveal, Qwen3.8-Max's original launch, an architectural description of Hy4-preview without agentic-benchmark numbers).

- **GLM-5.3** gains an Agent Arena and Vals benchmark section, plus a Recent-changes entry.
- **Qwen 3.8** gains a Qwen3.8-Max-0902 refresh section (the new #1 WebDev result), plus a Recent-changes entry.
- **Open-weight momentum broadens** gains a new bullet quantifying GLM-5.3-Flash's and Qwen3.8-Flash-Next's Agent Arena standing for the first time, plus the Qwen3.8-Max-0902 result and the Hy4-preview post-training detail, plus a Recent-changes entry. That list is already at its 10-entry cap, so the oldest entry spills to history.
- No new source pages: both raw newsletters are owned by companion proposals in this same batch (Fable 5.1/Mythos 5.1; Muse Spark 1.3/Muse Code); this proposal references those source slugs directly.

### What to weigh

All four benchmark placements (Agent Arena ×2, Code Arena: WebDev, the Hy4-preview post-training claim) come through AINews' relay of Arena's and a Zhihu account's own posts, not primary leaderboard pages fetched directly — none were independently re-verified. The Hy4-preview post-training detail is presented as extending, not duplicating, the architectural description the trend page already carries from August 29.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/glm-5-3.md` — add Agent Arena/Vals benchmark section; add 1 Recent-changes entry
    > See draft below

- [ ] **Update** `wiki/models/qwen-3-8.md` — add Qwen3.8-Max-0902 refresh section; add 1 Recent-changes entry
    > See draft below

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — add Agent Arena rankings bullet; add 1 Recent-changes entry (list is at the 10-entry cap, so the oldest entry spills to `wiki/history/trends/open-weight-momentum-broadens.md`)
    > See draft below

## Page drafts

### wiki/models/glm-5-3.md (updated)

Insert this new section directly after `## GLM-5.3-Flash: a smaller open-weight sibling (as of 2026-08-27)` and before `## Why it matters`:

```md
## Agent Arena and Vals benchmark placements (as of 2026-09-01)

GLM-5.3-Flash placed #19 overall / #4 among open models on Agent Arena, with a +4.6% net improvement over 9,000+ real-world sessions, a $0.12 median cost/task, and no reported tool-hallucination issues (+15.3% Confirmed Success in the signal breakdown). Separately, Vals reported the broader GLM-5.3 family posting 95.4% on SWE-bench and 78.1% on Vibe Code Bench, alongside its existing 1M context window and a 128k max output token ceiling.
```

Recent changes — add this entry at the top:

```md
- [2026-09-01] Agent Arena placement: GLM-5.3-Flash #19 overall / #4 among open models (+4.6% net improvement, $0.12 median cost/task); Vals reports full GLM-5.3 family at 95.4% SWE-bench, 78.1% Vibe Code Bench.
```

Frontmatter `as_of:` → `2026-09-01`; `sources:` — append `ainews-fal-h3-max-live-2026-09-01`.

### wiki/models/qwen-3-8.md (updated)

Insert this new section directly after `## Current status (as of 2026-08-13)` and before `## Why it matters`:

```md
## Qwen3.8-Max-0902 refresh (as of 2026-09-01)

Alibaba released Qwen3.8-Max-0902, a refreshed 2.4T-parameter build with 1M context, priced at $2/M input and $6/M output plus cache-hit discounts. Arena reported it debuting #1 on Code Arena: WebDev (1691 Elo), just ahead of Claude Opus 5 Max and Kimi K3 Max, and landing on the current best price/performance frontier.
```

Recent changes — add this entry at the top:

```md
- [2026-09-01] Qwen3.8-Max-0902 refresh debuts #1 on Arena's Code Arena: WebDev (1691), ahead of Claude Opus 5 Max and Kimi K3 Max.
```

Frontmatter `as_of:` → `2026-09-01`; `sources:` — append `ainews-fablemythos-51-2026-09-02`.

### wiki/trends/open-weight-momentum-broadens.md (updated)

Insert this new bullet directly after the existing `**Tencent Hy4-preview and Qwen3.8-Flash extend the wave (August 2026):**` bullet under `## Current signal`:

```md
- **Agent Arena rankings quantify GLM-5.3-Flash and Qwen3.8-Flash-Next's open-weight standing (September 2026):** GLM-5.3-Flash placed #19 overall / #4 among open models (+4.6% net improvement over 9K+ real sessions, $0.12 median cost/task), while Qwen3.8-Flash-Next placed #24 overall / #7 among open models (+2.4% net improvement over 8.7K+ sessions) — the first head-to-head agentic-arena data point for both models tracked on this page. Separately, Alibaba's flagship Qwen3.8-Max-0902 refresh debuted #1 on Arena's Code Arena: WebDev (1691), just ahead of Claude Opus 5 Max and Kimi K3 Max, and a Zhihu roundup adds detail to the Tencent Hy4-preview entry above: the open-source 770B/49B-active model reportedly closed much of its capability gap to Hy3 in about seven weeks through post-training and agent-policy tuning alone.
```

Recent changes — add this entry at the top (list is at the 10-entry cap; the oldest entry, `[2026-07-28] NVIDIA launches the "Open Secure AI Alliance"...`, spills to `wiki/history/trends/open-weight-momentum-broadens.md`):

```md
- [2026-09-01] Agent Arena rankings add GLM-5.3-Flash (#19 overall/#4 open) and Qwen3.8-Flash-Next (#24 overall/#7 open) agentic placements; Qwen3.8-Max-0902 debuts #1 Code Arena: WebDev; Hy4-preview reportedly closed its gap to Hy3 in ~7 weeks via post-training.
```

## Open questions

None beyond the sourcing note above.
