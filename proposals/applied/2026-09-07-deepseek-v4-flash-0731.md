---
type: proposal
source: raw/newsletters/2026-08-01-ainews-not-much-happened-today.md
status: pending
created: 2026-09-07
---

# Proposal: DeepSeek V4-Flash 0731 post-training leap

## Summary

### The source

AINews' August 1 issue (self-deprecatingly titled "not much happened today") leads with what it actually considers the day's biggest story: DeepSeek's public-beta launch of an updated V4-Flash API, released the day after OpenAI's GPT-5.6 price cuts and widely read as a direct competitive response. DeepSeek says the Flash tier's agentic capabilities now surpass the previous V4-Pro-Preview, and that the API now supports OpenAI's Responses format and is "fully adapted for Codex." Crucially, DeepSeek clarified this is a Flash-only update — V4-Pro's API, app, and web product are unchanged for now, and an official V4-Pro release is still pending. The architecture didn't change either: Artificial Analysis confirmed V4-Flash 0731 is still 284B total / 13B active parameters, 1M context, text-only — this is a post-training-only win, not a scaling or architecture story, and multiple commentators (including a DeepSeek co-founder-adjacent account) explicitly called it out as such. The benchmark jump was large: Terminal-Bench rose from 56.9 to 82.7 (+25.8), Artificial Analysis's Intelligence Index rose from 40 to 50 (now just one point behind GPT-5.6 Luna's 51, at roughly 60% lower cost per task on DeepSeek's own API), GDPval-AA v2 Elo went from 1189 to 1559, and output-token usage dropped 12% versus the predecessor. Pricing is $0.14/$0.28 per 1M input/output tokens with a notably aggressive 98% cache-hit discount down to $0.0028/1M cached tokens. Open weights followed almost immediately under MIT license, with day-0 vLLM support: 256 routed experts, 6 active per token, three reasoning-effort levels, and an included DSpark speculative-decoding module enabled via a single flag. Local/quantized builds landed the same day (Unsloth: ~168GB RAM for lossless 4-bit, ~110GB for 3-bit). The release also fed the open-vs-closed security argument already running that week: Hugging Face's Clement Delangue pointed to the earlier autonomous-agent breach as evidence that a vibrant open ecosystem matters even in a world with strong closed models.

### What changes

The wiki's DeepSeek V4 page currently reflects the April 2026 Pro/Flash release and the May 2026 permanent V4-Pro price-discount update; it does not yet cover this post-training-only Flash upgrade or its new benchmark placement relative to GPT-5.6.

- **DeepSeek V4** gains a new "V4-Flash 0731 update" note describing the post-training-only benchmark jump (Terminal-Bench 82.7, AA Intelligence Index 50, GDPval-AA v2 Elo 1559), the unchanged 284B/13B architecture, the new $0.14/$0.28 pricing with 98% cache-hit discount, MIT-licensed open weights, and day-0 vLLM support (256 routed experts, 6 active, DSpark). Explicitly notes V4-Pro is unaffected and still pending its own official release. Page date moves to 31 July.
- **State of Models** updates both DeepSeek V4 leader lines (Coding models and Open-weight models sections) with the new Flash figure and as_of, and gains a Recent-changes entry; the oldest entry spills to history since the list is at its 10-entry cap.
- One new source page for the AINews issue.

### What to weigh

DeepSeek's own benchmark claims are corroborated here by Artificial Analysis's independent index (40→50) and by community reactions (Cline, others) rather than resting on DeepSeek's word alone, so this is better-sourced than a typical vendor-only benchmark claim. The one open thread is V4-Pro's own official release, which the source says is "still pending" — I've left the existing V4-Pro content on the page untouched rather than guessing at numbers that don't exist yet.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/deepseek-v4.md` — add V4-Flash 0731 update section, Recent-changes entry, as_of bump to 2026-07-31
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — bump both DeepSeek V4 leader lines and as_of, add Recent-changes entry
    > See draft below

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — oldest Recent-changes entry at apply time (the draft assumes the list is already at its 10-entry cap; the apply step should spill whatever is actually oldest on the live page)

- [ ] **Create** `wiki/sources/newsletters/ainews-not-much-happened-2026-08-01.md` — source summary

## Page drafts

### wiki/models/deepseek-v4.md (updated)

```md
---
title: DeepSeek V4
type: model
domains: [models, coding, agents]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-07-31
sources: [deepseek-v4-preview, ainews-2026-04-25, ainews-all-model-labs-are-now-agent-labs, ainews-not-much-happened-2026-08-01]
---

...(intro paragraph and "Current status (as of 2026-05-23)" section unchanged)...

## V4-Flash 0731 update (as of 2026-07-31)

DeepSeek shipped a post-training-only upgrade to V4-Flash — same 284B total / 13B active architecture, no scaling or architecture change:

- **Benchmarks:** Terminal-Bench 56.9 → 82.7 (+25.8); Artificial Analysis Intelligence Index 40 → 50, one point behind GPT-5.6 Luna's 51 at roughly 60% lower cost per task on DeepSeek's own API; GDPval-AA v2 Elo 1189 → 1559; output-token usage down 12% versus the predecessor.
- **Pricing:** $0.14 / $0.28 per 1M input/output tokens, with a 98% cache-hit discount down to $0.0028/1M cached tokens.
- **Open weights:** released under MIT with immediate day-0 vLLM support — 256 routed experts, 6 active per token, three reasoning-effort levels, and an included DSpark speculative-decoding module enabled via a single flag. Local/quantized builds landed same-day (Unsloth: ~168GB RAM for lossless 4-bit, ~110GB for 3-bit).
- **Scope:** this update applies to V4-Flash only. V4-Pro's API, app, and web product are unchanged; an official V4-Pro release remains pending.
- Widely read as a direct competitive response to OpenAI's GPT-5.6 price cuts the day before.

...(rest of page — Strengths, Weaknesses/caveats — unchanged)...

## Recent changes

- [2026-07-31] V4-Flash 0731: post-training-only update jumps Terminal-Bench to 82.7 (+25.8) and AA Intelligence Index to 50 (from 40), now 1pt behind GPT-5.6 Luna; open-weighted under MIT with day-0 vLLM support; V4-Pro unaffected, still pending its own release.
- [2026-05-23] DeepSeek made the 75% V4-Pro discount permanent; Artificial Analysis pricing/cost-per-Intelligence-Index comparison (via AINews) added, caveated as a May 2026 snapshot since DeepSeek's pricing page (fetched 2026-08-25) has since moved to peak/off-peak, cache-hit/miss tiers.
- [2026-04-25] AINews follow-up reframed DeepSeek V4 from preview to release: Pro/Flash specs, MIT license, API pricing, independent open-model placement, Huawei Ascend compatibility, and token-volume caveats
<!-- cap is 10, well under it — no spill needed on this page -->

## Sources

- [DeepSeek V4 Preview](../sources/articles/deepseek-v4-preview.md)
- [AINews - DeepSeek V4 Pro and Flash](../sources/newsletters/ainews-2026-04-25.md)
- [AINews — All model labs are now agent labs (DeepSeek V4-Pro permanent discount)](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
- [AINews — not much happened today (DeepSeek V4-Flash 0731)](../sources/newsletters/ainews-not-much-happened-2026-08-01.md)
```

### wiki/state-of/models.md (updated snippets)

Coding models section:

```md
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; released open-weight Pro/Flash MoE lineup with 1M context, MIT license; V4-Flash's 0731 post-training update jumped Terminal-Bench to 82.7 and AA Intelligence Index to 50 (1pt behind GPT-5.6 Luna) at $0.14/$0.28 per M tokens; V4-Pro unaffected, still below the strongest closed frontier systems overall *(as of 2026-07-31)*
```

Open-weight models section:

```md
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; MIT open-weight Pro/Flash lineup with 1M context; V4-Flash's 0731 update (post-training only, same 284B/13B architecture) reached AA Intelligence Index 50 and Terminal-Bench 82.7, day-0 vLLM support with DSpark speculative decoding; V4-Pro's official release still pending *(as of 2026-07-31)*
```

Recent changes — insert this entry in date order (newest first):

```md
- [2026-07-31] DeepSeek V4-Flash 0731: post-training-only update (same 284B/13B architecture) jumped Terminal-Bench to 82.7 and AA Intelligence Index to 50, now 1pt behind GPT-5.6 Luna; MIT-licensed, day-0 vLLM support; read as a direct response to OpenAI's price cuts the day before.
```

### wiki/sources/newsletters/ainews-not-much-happened-2026-08-01.md (new)

```md
---
title: "AINews — not much happened today (DeepSeek V4-Flash 0731)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-01-ainews-not-much-happened-today.md
url: https://www.latent.space/p/ainews-not-much-happened-today-038
published: 2026-08-01
ingested: 2026-09-07
domains: [models]
---

# AINews — not much happened today (DeepSeek V4-Flash 0731)

AINews' self-deprecatingly titled issue covers DeepSeek's public-beta launch of a post-training-only V4-Flash update (Terminal-Bench 56.9→82.7, AA Intelligence Index 40→50, GDPval-AA v2 Elo 1189→1559) with unchanged 284B/13B architecture, released a day after OpenAI's GPT-5.6 price cuts and widely read as a direct response. Open-weighted under MIT with day-0 vLLM support. Also covers the week's ongoing agent-security-incident fallout (OpenAI/Anthropic sandbox failures) and continued open-vs-closed security argument.

## Influenced pages

- [DeepSeek V4](../../models/deepseek-v4.md) — V4-Flash 0731 post-training update
- [State of Models](../../state-of/models.md) — updated DeepSeek V4 leader lines, Recent-changes entry

## Key claims extracted

- DeepSeek V4-Flash 0731: post-training-only update, same 284B total/13B active architecture
- Terminal-Bench 56.9 → 82.7 (+25.8); AA Intelligence Index 40 → 50, one point behind GPT-5.6 Luna (51)
- GDPval-AA v2 Elo 1189 → 1559; output-token usage down 12%
- Pricing $0.14/$0.28 per 1M tokens with 98% cache-hit discount to $0.0028/1M cached
- Open-weighted under MIT; day-0 vLLM support (256 routed experts, 6 active, DSpark speculative decoding)
- V4-Pro API/app/web unchanged; official V4-Pro release still pending
```

## Open questions

- None beyond the sourcing note above.
