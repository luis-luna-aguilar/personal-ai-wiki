---
type: proposal
source: raw/newsletters/2026-07-23-inside-the-model-factory-eiso-kant-poolside-ai.md
status: pending
created: 2026-09-06
---

# Proposal: Poolside ships Laguna S 2.1

## Summary

### The source

Three sources tell one story. An AINews Twitter/Reddit recap and a Latent Space podcast transcript both cover Poolside AI's release of Laguna S 2.1, a 118-billion-parameter mixture-of-experts model with only 8 billion parameters active per token, a 1M-token context window, and open weights under Poolside's own OpenMDW-1.1 license. It's small enough to run locally on a single NVIDIA DGX Spark. On coding and agentic benchmarks it scores 70.2% on Terminal-Bench 2.1, 78.5% on SWE-bench Multilingual, 59.4% on SWE-Bench Pro, 40.4% on DeepSWE, 46.2% on SWE Atlas Codebase Q&A, and 49.7% on Toolathlon Verified — priced cheaper than DeepSeek V4 Flash while beating V4 Pro. An independent agentic eval pitting it against Qwen3.5-122B found it faster and better at tool-calling (109 vs. 103 tokens/sec, cleaner tool-call syntax, deeper tool chains) but more prone to fabricating facts under pressure — 3 confirmed fabrications in the initial run versus zero for Qwen, later cut to 1 across 125 grounding runs after a tokenizer/sampling fix.

The Poolside co-founder, Eiso Kant, unpacks the release and the company's philosophy in a long podcast interview. Poolside calls itself a "neolab" — a Western foundation-model company built from scratch rather than spun out of an existing lab — and Eiso frames Laguna S 2.1 as evidence that persistence and verification behavior, not raw parameter count, is what's driving its results: an internal researcher's read was that the gains come "not from more intelligence, but more from different behavior — more verification, less taking things for granted, being way more persistent." The model was trained in eight weeks end-to-end through Poolside's "Model Factory" pipeline, which streams training data live rather than pre-packaging it and runs 10,000-20,000 experiments a month across a team of under 70 researchers. Poolside raised $500M and states its release strategy is deliberate: Eiso says he'd "rather live in a world with 100 foundation model companies than five," explicitly framing open weights as a hedge against intelligence concentrating in a handful of firms.

### What changes

The wiki currently tracks the open-weight surge through Inkling, Kimi K3, and Qwen 3.8 — all covered by `trends/open-weight-momentum-broadens.md` — but has no page for Poolside or any Poolside model.

- **New page** `models/laguna-s-2-1.md`: covers the release, benchmark scores, the OpenMDW-1.1 license, the DGX-Spark-scale deployment story, the independent Qwen3.5-122B comparison (speed/tool-calling win, fabrication weakness), and Poolside's Model Factory / "100 foundation model companies" framing.
- **Open-weight momentum broadens** gains a new Current-signal bullet for Laguna S 2.1 as a credible non-Chinese open-weight coding entrant arriving in the same window as Inkling and Kimi K3, plus a new Recent-changes entry dated 22 July. The list is at its 10-entry cap, so the oldest entry (30 May, open-weight adoption stats) spills to `wiki/history/trends/open-weight-momentum-broadens.md`.
- **State of Models** adds a Laguna S 2.1 line under Open-weight models and a matching Recent-changes entry. That list is also at its 10-entry cap, so its oldest entry (23 June, GLM-5.2 follow-on coverage) spills to `wiki/history/state-of/models.md`.
- One new source page covering all three raw files (AINews cybersecurity-digest excerpt, AINews Laguna-specific recap, and the full Latent Space podcast transcript).

### What to weigh

The fabrication-rate comparison against Qwen3.5-122B comes from one practitioner's private eval on a single RTX Pro 6000, not a published benchmark — it's included because it's specific and self-correcting (the tokenizer fix reduced the rate), but it's a single source, not an independently replicated result. The benchmark scores themselves (Terminal-Bench, SWE-bench Multilingual, etc.) are Poolside's own reported numbers, not yet corroborated by a third-party leaderboard the way Kimi K3's Intelligence Index score was.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/models/laguna-s-2-1.md` — new page for Poolside's Laguna S 2.1
    > See draft below

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — new Current-signal bullet, new Recent-changes entry, spill oldest entry
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — add Laguna S 2.1 to Open-weight models, new Recent-changes entry, spill oldest entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/poolside-laguna-s-21-2026-07-23.md` — source summary covering all three raw files

- [ ] **Spill** `wiki/trends/open-weight-momentum-broadens.md` → `wiki/history/trends/open-weight-momentum-broadens.md` — oldest recent-change entry (30 May) falls off the 10-entry cap
- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — oldest recent-change entry (23 June) falls off the 10-entry cap

## Page drafts

### wiki/models/laguna-s-2-1.md (new)

````md
---
title: Laguna S 2.1
type: model
domains: [models, coding]
subcategory: open-weight-model
tags: [poolside, open-weights, agentic]
as_of: 2026-07-23
sources: [poolside-laguna-s-21-2026-07-23]
---

# Laguna S 2.1

Poolside AI's flagship open-weight coding model, released 2026-07-22/23. A 118B-total / 8B-active mixture-of-experts model with a 1M-token context window, released under Poolside's own OpenMDW-1.1 license. Small enough to run locally on a single NVIDIA DGX Spark. Poolside is a Western "neolab" — a from-scratch foundation-model company, not a lab spinout — that raised $500M and builds models through an internal "Model Factory" pipeline (streaming training data, 10,000-20,000 experiments/month, five-to-eight-week training cycles).

## Current status (as of 2026-07-23)

- Benchmarks: 70.2% Terminal-Bench 2.1, 78.5% SWE-bench Multilingual, 59.4% SWE-Bench Pro, 40.4% DeepSWE, 46.2% SWE Atlas Codebase Q&A, 49.7% Toolathlon Verified
- Cheaper than DeepSeek V4 Flash while beating V4 Pro on reported benchmarks
- Independent eval vs. Qwen3.5-122B (single RTX Pro 6000, private test): faster and better tool-calling (109 vs. 103 tok/s, cleaner tool-call syntax, deeper tool chains) but more prone to fabricating facts under pressure — 3 confirmed fabrications vs. 0 in the initial run, cut to 1 across 125 grounding runs after a tokenizer/sampling fix
- Poolside frames the release explicitly as resisting intelligence concentration in "three or four companies" — Eiso Kant says he'd rather see 100 foundation-model companies than five
- Trained end-to-end in 8 weeks via Poolside's Model Factory pipeline

## Strengths

- Strong agentic coding and tool-calling performance for its size class (118B total / 8B active)
- Practical local deployment — fits and runs at usable speed on a single DGX Spark or high-RAM consumer/prosumer hardware
- Detailed, well-regarded technical report (data streaming, reproducibility, Model Factory internals)

## Weaknesses / caveats

- More prone to fact fabrication under pressure than Qwen3.5-122B in one practitioner's private eval; not yet independently corroborated at scale
- Benchmark scores are self-reported by Poolside, not yet placed on a third-party leaderboard (e.g. Artificial Analysis)
- No vision support at launch

## Recent changes

- [2026-07-23] Initial page: Laguna S 2.1 release, benchmark scores, independent Qwen3.5-122B comparison, Poolside's Model Factory framing

## Sources

- [Poolside Laguna S 2.1 — release and Model Factory interview](../sources/newsletters/poolside-laguna-s-21-2026-07-23.md)
````

### wiki/trends/open-weight-momentum-broadens.md (updated)

````md
## Current signal

<!-- existing bullets unchanged; new bullet appended after the Inkling bullet: -->

- **Laguna S 2.1 (Poolside, July 2026):** a credible non-Chinese open-weight coding entrant arriving in the same window as Inkling and Kimi K3 — 118B/8B-active MoE, OpenMDW-1.1 license, runs on a single DGX Spark, strong agentic-coding benchmarks (70.2% Terminal-Bench 2.1, 78.5% SWE-bench Multilingual). Poolside, a Western "neolab," frames the release the same way as the sovereignty argument above: resisting intelligence concentrating in "three or four companies."

## Recent changes

<!-- insert as the newest entry, before the 2026-07-21 entry: -->
- [2026-07-22] Poolside released Laguna S 2.1 (118B/8B-active MoE, OpenMDW-1.1 license): a new non-Chinese open-weight coding entrant, strong on agentic-coding benchmarks, more prone to fabrication under pressure than Qwen3.5-122B per one independent eval.

<!-- oldest entry (2026-05-30) removed from this page and appended verbatim, with its original date, to wiki/history/trends/open-weight-momentum-broadens.md -->
````

### wiki/state-of/models.md (updated)

````md
### Open-weight models

<!-- new bullet appended to the existing list: -->

- [Laguna S 2.1](../models/laguna-s-2-1.md) — Poolside; 118B/8B-active MoE; OpenMDW-1.1 license; runs on a single DGX Spark; 70.2% Terminal-Bench 2.1, 78.5% SWE-bench Multilingual, 59.4% SWE-Bench Pro; cheaper than DeepSeek V4 Flash while beating V4 Pro *(as of 2026-07-23)*

## Recent changes

<!-- insert as the newest entry, before the 2026-07-17 Kimi K3 entry: -->
- [2026-07-23] Laguna S 2.1 (Poolside) added to Open-weight models: 118B/8B-active MoE, strong agentic-coding benchmarks, cheaper than DeepSeek V4 Flash while beating V4 Pro.

<!-- oldest entry (2026-06-23, GLM-5.2 follow-on coverage) removed from this page and appended verbatim, with its original date, to wiki/history/state-of/models.md -->
````

### wiki/sources/newsletters/poolside-laguna-s-21-2026-07-23.md (new)

````md
---
title: Poolside Laguna S 2.1 — release and Model Factory interview
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-23-inside-the-model-factory-eiso-kant-poolside-ai.md
url: https://www.latent.space/p/poolside
published: 2026-07-23
ingested: 2026-09-06
domains: [models, coding]
---

# Poolside Laguna S 2.1 — release and Model Factory interview

Poolside AI released Laguna S 2.1, a 118B-total/8B-active open-weight coding model under its own OpenMDW-1.1 license, alongside a long Latent Space podcast interview with co-founder Eiso Kant covering the model, Poolside's "Model Factory" training pipeline, and its open-weight philosophy. Also draws on two AINews recaps (Twitter/Reddit) covering the same release with independent benchmark and eval commentary.

## Influenced pages

- [Laguna S 2.1](../../models/laguna-s-2-1.md) — new page
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — new Current-signal bullet, Recent-changes entry
- [State of Models](../../state-of/models.md) — new Open-weight models line, Recent-changes entry

## Key claims extracted

- Laguna S 2.1: 118B total / 8B active MoE, 1M-token context, OpenMDW-1.1 license, runs on a single NVIDIA DGX Spark
- Benchmarks: 70.2% Terminal-Bench 2.1, 78.5% SWE-bench Multilingual, 59.4% SWE-Bench Pro, 40.4% DeepSWE, 46.2% SWE Atlas Codebase Q&A, 49.7% Toolathlon Verified
- Cheaper than DeepSeek V4 Flash while beating V4 Pro
- Independent eval vs. Qwen3.5-122B: faster/better tool-calling (109 vs 103 tok/s) but more prone to fabrication under pressure (3 vs 0 fabrications, later reduced to 1/125 via tokenizer fix)
- Trained end-to-end in 8 weeks via Poolside's "Model Factory" (streaming training data, 10,000-20,000 experiments/month, <70 researchers)
- Poolside raised $500M; frames open weights as resisting intelligence concentration in "three or four companies"
````

## Schema / vocabulary additions

None.

## Open questions

None.
