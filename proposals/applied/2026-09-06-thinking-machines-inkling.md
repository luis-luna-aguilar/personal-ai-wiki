---
type: proposal
source: raw/newsletters/2026-07-16-ainews-thinkys-inkling-975b-a41b-multimodal-n.md
status: pending
created: 2026-09-06
---

# Proposal: Thinking Machines ships Inkling, a 975B open-weight flagship

## Summary

### The source

On 2026-07-16, AINews carried the full technical breakdown of Inkling, the first publicly-released flagship model from Thinking Machines Lab — Mira Murati's frontier lab, until now known mainly for research previews like its small real-time interaction model. Inkling is a 975B-total / 41B-active mixture-of-experts model, natively multimodal across text, image, and audio, trained on 45 trillion tokens, with a 1M-token context window on the open weights (256K on the hosted Tinker API). Two of its architecture choices drew independent technical attention: it replaces the now-standard RoPE positional scheme with relative positional attention, and it uses large-scale short-convolution layers alongside two experts shared across the MoE routing rather than routed independently. Thinking Machines released the full model under Apache 2.0, plus a smaller Inkling-Small preview (276B total / 12B active). Artificial Analysis scored the flagship at 41 on its Intelligence Index — ahead of NVIDIA's Nemotron 3 Ultra (38) and OpenAI's gpt-oss-120b (24), making it the strongest US-origin open-weight release to date — though it still trails GLM-5.2 and Kimi on agentic and multimodal benchmarks specifically. Two companion newsletters from the same day add framing rather than new facts: one situates the release against China's open-weight lead, the other gives brief local-run instructions.

### What changes

The wiki has tracked Thinking Machines only through a small 276B-parameter real-time interaction research preview (`state-of/models.md`) and general "Model Labs" commentary in the open-weight trend page; it has no page for the lab's actual flagship model.

- New page **`models/inkling.md`**: the full model profile above — parameter counts, architecture choices, Apache 2.0 licensing, the Inkling-Small variant, and the Artificial Analysis Intelligence Index placement.
- **State of Models** gains a new line for Inkling under the Open-weight models subcategory (975B/41B MoE, Intelligence Index 41, ahead of Nemotron 3 Ultra and gpt-oss-120b, behind GLM-5.2/Kimi on agentic work), plus a new Recent-changes entry dated 16 July; because that section is at its 10-entry cap, the oldest entry spills to `wiki/history/state-of/models.md`.
- **Open-weight momentum broadens** gains a bullet naming Inkling as the first flagship release from a closely-watched frontier lab choosing open weights outright, rather than a closed frontier push — most open-weight competition to date has come from Chinese labs. A matching Recent-changes entry is added; that section is also at its 10-entry cap, so its oldest entry spills to `wiki/history/trends/open-weight-momentum-broadens.md`.
- One new source page, `sources/newsletters/ainews-thinkys-inkling-2026-07-16.md`, covering all three newsletters (the framing and local-run pieces add context but no independent facts, so they're folded into one source page rather than three).

### What to weigh

All benchmark numbers here are Artificial Analysis's independent scoring rather than Thinking Machines' own claims, so sourcing is solid; the one judgment call is scope — Inkling's existing "TML-Interaction-Small" line in `state-of/models.md` covers a different, smaller, real-time-audio model from the same lab, so this proposal adds a second, separate line rather than replacing it. Worth confirming that reads correctly as two distinct products from one lab, not a version bump.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/models/inkling.md` — new model page
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — adds Inkling line under Open-weight models subcategory; adds one Recent-changes entry dated 2026-07-16; spills the oldest Recent-changes entry to history
    > See draft below

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — adds one Current-signal bullet on Inkling; adds one Recent-changes entry dated 2026-07-16; spills the oldest Recent-changes entry to history
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-thinkys-inkling-2026-07-16.md` — source summary covering all three newsletters

- [ ] **Update** `wiki/index.md` — add entry for `models/inkling.md`

## Page drafts

### wiki/models/inkling.md (new)

```md
---
title: Inkling
type: model
domains: [models]
subcategory: open-weight-model
tags: [thinking-machines, open-weights, multimodal]
as_of: 2026-07-16
sources: [ainews-thinkys-inkling-2026-07-16]
---

# Inkling

Thinking Machines Lab's first publicly-released flagship model. A 975B-total / 41B-active mixture-of-experts model, natively multimodal across text, image, and audio, released under Apache 2.0.

## Current status (as of 2026-07-16)

- 975B total / 41B active MoE, trained on 45T tokens
- Natively multimodal: text, image, and audio in one model
- 1M-token context on the open weights; 256K on the hosted Tinker API
- Architecture departs from convention: relative positional attention instead of RoPE, large-scale short-convolution layers, and two MoE experts shared across all tokens rather than routed
- Companion Inkling-Small preview: 276B total / 12B active
- Artificial Analysis Intelligence Index: 41 — ahead of Nemotron 3 Ultra (38) and gpt-oss-120b (24); still behind GLM-5.2 and Kimi on agentic/multimodal benchmarks specifically

## Why it matters

The first flagship release from a lab known until now mainly for research previews (see the smaller TML-Interaction-Small real-time model). A US lab choosing to ship its flagship as open weights is itself notable — most open-weight competition to date has come from Chinese labs.

## Recent changes

- [2026-07-16] Initial release: 975B/41B MoE, Apache 2.0, Intelligence Index 41

## Sources

- [AINews — Thinking Machines' Inkling (975B/41B, multimodal)](../sources/newsletters/ainews-thinkys-inkling-2026-07-16.md)
```

### wiki/state-of/models.md (updated)

```md
### Open-weight models

Broad foundation models whose main current-state question is open or open-ish weight availability, deployment control, and practical ecosystem support.

- [Inkling](../models/inkling.md) — Thinking Machines Lab; 975B/41B MoE; natively multimodal (text/image/audio); Apache 2.0; Intelligence Index 41, ahead of Nemotron 3 Ultra and gpt-oss-120b, behind GLM-5.2/Kimi on agentic work *(as of 2026-07-16)*
- [Nemotron 3 Ultra](../models/nemotron-3-ultra.md) — NVIDIA; 550B/55B MoE; hybrid Mamba/attention + LatentMoE; 1M context; 300-400+ tok/s; OpenMDW 1.1; NVFP4 pretraining on 20T tokens; 47.7 Intelligence Index BF16 *(as of 2026-06-02)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; MIT open-weight Pro/Flash lineup with 1M context and serious long-context agent infrastructure signal; V4-Pro's 75% price discount made permanent in May 2026 — Artificial Analysis (via AINews) put it at ~19x cheaper than Claude Opus 4.7 to run its Intelligence Index, though DeepSeek has since restructured pricing (peak/off-peak tiers), so treat that as a May 2026 snapshot *(as of 2026-05-23)*
- [Cohere Command A+](../models/cohere-command-a-plus.md) — Cohere; its first fully open (Apache 2.0) model; 218B/25B MoE; AA Intelligence Index 37 (~Claude 4.5 Haiku tier per AINews' summary of AA); AA reports strong non-hallucination behavior but weaker coding/science reasoning than top peers *(as of 2026-05-21)*
```

New Recent-changes entry (insert as newest; enforce cap by spilling the oldest live entry to `wiki/history/state-of/models.md`):

```md
- [2026-07-16] Thinking Machines Lab released Inkling, its first flagship model: 975B/41B MoE, natively multimodal, Apache 2.0, Intelligence Index 41 — the strongest US-origin open-weight release to date.
```

### wiki/trends/open-weight-momentum-broadens.md (updated)

New Current-signal bullet:

```md
- **Inkling (Thinking Machines Lab, July 2026):** the lab's first flagship release, and a US lab choosing to ship it as open weights (975B/41B MoE, Apache 2.0, Intelligence Index 41) rather than a closed frontier push — notable because most open-weight competition to date has come from Chinese labs, not US ones.
```

New Recent-changes entry (insert as newest; enforce cap by spilling the oldest live entry to `wiki/history/trends/open-weight-momentum-broadens.md`):

```md
- [2026-07-16] Thinking Machines Lab released Inkling (975B/41B MoE, Apache 2.0, Intelligence Index 41) — its first flagship model, and a rare US-origin open-weight flagship choice.
```

### wiki/sources/newsletters/ainews-thinkys-inkling-2026-07-16.md (new)

```md
---
title: AINews — Thinking Machines' Inkling (975B/41B, multimodal)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-16-ainews-thinkys-inkling-975b-a41b-multimodal-n.md
ingested: 2026-09-06
domains: [models]
---

# AINews — Thinking Machines' Inkling (975B/41B, multimodal)

Thinking Machines Lab released Inkling, its first flagship model: a 975B-total/41B-active natively multimodal MoE trained on 45T tokens, with unconventional architecture choices (relative positional attention, shared MoE experts, short-convolution layers). Apache 2.0 licensed, with an Inkling-Small preview. Artificial Analysis placed it at Intelligence Index 41, the strongest US-origin open-weight release so far.

## Influenced pages

- [Inkling](../../models/inkling.md) — new page
- [State of Models](../../state-of/models.md) — new Open-weight models line
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — new Current-signal bullet

## Key claims extracted

- 975B total / 41B active MoE, 45T training tokens, natively multimodal
- 1M context (open weights), 256K context (Tinker API)
- Relative positional attention (not RoPE); shared MoE experts; short-convolution layers
- Apache 2.0; Inkling-Small variant at 276B/12B
- Artificial Analysis Intelligence Index 41 (ahead of Nemotron 3 Ultra 38, gpt-oss-120b 24; behind GLM-5.2/Kimi on agentic/multimodal work)
```

## Schema / vocabulary additions

None.

## Open questions

None.
