---
type: proposal
source: raw/newsletters/2026-07-31-ainews-gpt-56-price-cut-by-20-80-cost-of-gpt.md
status: pending
created: 2026-09-07
---

# Proposal: Thinking Machines ships Inkling-Small

## Summary

### The source

AINews' 2026-07-31 digest, mainly about OpenAI's GPT-5.6 price cuts, also covers Thinking Machines shipping Inkling-Small: an open-weight, natively multimodal MoE model at 276B total parameters with 12B active, positioned as delivering performance comparable to the original 975B/41B Inkling flagship at roughly a quarter the size. It processes audio and images jointly with text and supports Python-based image inspection mid-reasoning. Artificial Analysis placed it at 40 on its Intelligence Index — within one point of the flagship's 41 — with particular strength on Humanity's Last Exam, GPQA Diamond, CritPt, and SciCode, though weaker on some agentic tasks and factual knowledge; community summaries noted it can beat or match the larger Inkling on several coding tasks. Day-0 support landed immediately across vLLM, Modal (highlighting single-B300 deployment), SGLang, and Unsloth (local/GGUF guide).

### What changes

The wiki's Inkling page already flags "Companion Inkling-Small preview: 276B total / 12B active" as a bullet under the flagship's Current status — that preview has now shipped with real benchmarks.

- **Inkling** expands that bullet into a full status update: confirmed spec, Intelligence Index 40 (one point behind flagship), benchmark strengths/weaknesses, and day-0 deployment support. Page date moves to 31 July.
- **State of Models** updates its Inkling leader line to note the shipped Inkling-Small sibling alongside the existing flagship entry.
- **Open-weight momentum broadens** gains one new Recent-changes entry, since the trend page already tracks Inkling's story in detail.
- One new source page for the AINews issue, since it hasn't been ingested into the wiki before.

### What to weigh

All figures here are third-party (Artificial Analysis benchmark placement, community summaries) rather than a primary Thinking Machines announcement — treat with the same confidence as the rest of the Inkling page's existing sourcing. Nothing else beyond that.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/inkling.md` — replace the Inkling-Small preview bullet with shipped status, Recent-changes entry, bump as_of to 2026-07-31
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — update Inkling leader line to note the shipped Inkling-Small sibling, Recent-changes entry
    > See draft below

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — add one Recent-changes entry for Inkling-Small's launch
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md` — source summary (note: another proposal in this batch, covering GPT-5.6's price cuts and self-optimization, also draws on this same raw file — if that proposal's source page is applied first, extend it instead of creating a second page for this same `source_file`)

## Page drafts

### wiki/models/inkling.md (updated)

Frontmatter `sources:` gains one new id, `as_of` becomes `2026-07-31`:

```yaml
sources: [ainews-thinkys-inkling-2026-07-16, ainews-gpt-56-price-cut-2026-07-31]
```

The existing bullet `- Companion Inkling-Small preview: 276B total / 12B active` under `## Current status` is replaced with:

```md
- **Inkling-Small (shipped 2026-07-31):** open-weight, natively multimodal MoE, 276B total / 12B active — roughly a quarter of the flagship's active footprint at comparable capability. Processes audio and images jointly with text; supports Python-based image inspection mid-reasoning. Artificial Analysis Intelligence Index: 40, within one point of the flagship's 41 — strong on Humanity's Last Exam, GPQA Diamond, CritPt, and SciCode; weaker on some agentic tasks and factual knowledge. Can beat or match the larger Inkling on several coding tasks per community summaries. Day-0 support across vLLM, Modal (single-B300 deployment), SGLang, and Unsloth (local/GGUF).
```

New line added to `## Recent changes` (list has 1 entry, well under cap):

```md
- [2026-07-31] Inkling-Small shipped: 276B/12B MoE, Intelligence Index 40 (vs flagship's 41), day-0 vLLM/Modal/SGLang/Unsloth support
```

New line added to `## Sources`:

```md
- [AINews — GPT 5.6 price cut by 20%-80%](../sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md)
```

### wiki/state-of/models.md (updated)

The existing line:

```md
- [Inkling](../models/inkling.md) — Thinking Machines Lab; 975B/41B MoE; natively multimodal (text/image/audio); Apache 2.0; Intelligence Index 41, ahead of Nemotron 3 Ultra and gpt-oss-120b, behind GLM-5.2/Kimi on agentic work *(as of 2026-07-16)*
```

becomes:

```md
- [Inkling](../models/inkling.md) — Thinking Machines Lab; 975B/41B MoE flagship (Intelligence Index 41) plus a shipped Inkling-Small sibling (276B/12B, Index 40, ~1/4 the active footprint at near-flagship capability); natively multimodal (text/image/audio); Apache 2.0 *(as of 2026-07-31)*
```

New entry inserted into `## Recent changes` in date order (after the 2026-07-17 Kimi K3 entry, before whatever is next):

```md
- [2026-07-31] Thinking Machines shipped Inkling-Small (276B/12B MoE, Intelligence Index 40), a near-flagship-capability sibling to Inkling at roughly a quarter the active footprint.
```

(Re-check the live list's length at apply time; if it's already at the 10-entry cap from an earlier proposal in this batch, spill the oldest entry to `wiki/history/state-of/models.md` before inserting.)

### wiki/trends/open-weight-momentum-broadens.md (updated)

`sources:` frontmatter gains one new id (append to the existing long list): `ainews-gpt-56-price-cut-2026-07-31`

New entry inserted into `## Recent changes` in date order:

```md
- [2026-07-31] Thinking Machines shipped Inkling-Small (276B/12B MoE, Intelligence Index 40, ~1/4 the flagship's active footprint at near-flagship capability), extending its US-origin open-weight flagship into a smaller sibling.
```

(Re-check the live list's length at apply time — see the note in the companion Kimi K3 deployment-ecosystem proposal in this same batch, which also touches this page's Recent-changes list.)

New line added to `## Sources`:

```md
- [AINews — GPT 5.6 price cut by 20%-80%](../sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md)
```

### wiki/sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md (new)

```markdown
---
title: "AINews — GPT 5.6 price cut by 20%-80%: Cost of GPT 5.4 Intelligence dropped 13x in 4 months"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-31-ainews-gpt-56-price-cut-by-20-80-cost-of-gpt.md
url: https://www.latent.space/p/ainews-gpt-56-price-cut-by-20-80
published: 2026-07-31
ingested: 2026-09-07
domains: [models]
---

# AINews — GPT 5.6 price cut by 20%-80%

Latent Space/AINews daily digest covering 2026-07-29–30. Leads with OpenAI's GPT-5.6 price cuts (Luna -80%, Terra -20%, new Sol Fast tier) and the disclosed self-optimization behind them (Sol autonomously rewrote production kernels and improved its own speculative-decoder training). Also covers Thinking Machines' Inkling-Small release and Google DeepMind's Gemini Robotics 2.

## Influenced pages

- [Inkling](../../models/inkling.md) — Inkling-Small shipped status, benchmarks, deployment support
- [State of Models](../../state-of/models.md) — Inkling leader line update
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Inkling-Small Recent-changes entry

## Key claims extracted

- Inkling-Small: 276B total / 12B active MoE, open-weight, natively multimodal (audio+image+text), Python-based image inspection mid-reasoning
- Artificial Analysis Intelligence Index: Inkling-Small 40 vs flagship Inkling 41
- Inkling-Small strengths: Humanity's Last Exam, GPQA Diamond, CritPt, SciCode; weaker on some agentic tasks and factual knowledge
- Day-0 support: vLLM, Modal (single-B300), SGLang, Unsloth (local/GGUF)
```
