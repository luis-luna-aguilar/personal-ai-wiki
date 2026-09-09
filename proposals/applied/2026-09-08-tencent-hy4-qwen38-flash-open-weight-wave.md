---
type: proposal
sources:
  - raw/newsletters/2026-08-29-ainews-openai-shuts-off-cursor.md
  - raw/tweets/2026-09-07-0xbakeer-2092644019830431817.md
status: pending
created: 2026-09-08
---

# Proposal: Tencent's Hy4-preview and Qwen3.8-Flash extend the Chinese open-weight wave

## Summary

### The source

An AINews digest (2026-08-29) covers two more entrants in the same open-weight wave the wiki already tracks closely. Tencent Hunyuan released **Hy4-preview**, a 770B-total/49B-active MoE with 1M context, explicitly framed as "open source frontier" — external evals place it around #5 on Code Arena: WebDev (a 115-point jump over Hy3) and reportedly leading SWE-bench Pro, with a serving design where 256 routed experts plus one shared expert let only a fraction of layers compute their own sparse index while others reuse it. Alibaba separately pushed **Qwen3.8-Flash** (125B total/6B active, 1M context, multimodal) into OpenCode Go, claimed ~20x cheaper and ~2x faster than Qwen3.8 Max, though early field reports flagged broken multi-turn tracking at FP8 (fixed by switching KV cache to BF16). A recovered tweet thread from independent practitioner @0xBakeer adds real technical depth on what appears to be a related, possibly overlapping model: **Qwen3.8-Flash-Next**, 180B total/6B active, where 51B of the parameters sit in a massive n-gram lookup table — a second embedding table indexed by short token sequences rather than single tokens, so common phrase patterns get memorized instead of recomputed through the transformer's layers each time. Because that table is never multiplied against anything, it doesn't need fast memory: it can be memory-mapped off an SSD and paged in on demand, which is what lets a 180B-parameter model fit on a 128GB unified-memory machine. 0xBakeer's own serving recipe on a single DGX Spark improved from 22 tok/s to 97 tok/s over a few days of iteration (llama.cpp, then a newer vLLM+NVFP4+MTP-draft-head setup).

### What changes

`trends/open-weight-momentum-broadens.md` already tracks this year's broadening Chinese open-weight wave (GLM, Kimi, DeepSeek, Qwen) in detail. This adds one new "Current signal" bullet covering Hy4-preview, Qwen3.8-Flash, and the Qwen3.8-Flash-Next architecture explainer, bumps the page's `as_of` to 2026-08-29, and adds one Recent-changes entry — which, per the page's 10-entry cap already being full, spills its oldest entry (one of the two 2026-07-28 items) to `wiki/history/trends/open-weight-momentum-broadens.md`.

### What to weigh

Both Hy4-preview and Qwen3.8-Flash are relayed entirely through AINews' tweet-recap coverage with no primary technical report fetched — thinner sourcing than most of this page's other entries. The 0xBakeer thread is a genuine, detailed primary technical account, but from an independent practitioner rather than Alibaba, and it's genuinely unclear whether "Qwen3.8-Flash-Next" is the same model as "Qwen3.8-Flash" described two ways, or a distinct sibling — the draft below flags this rather than silently merging the two into one claim.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — add Hy4-preview/Qwen3.8-Flash/Qwen3.8-Flash-Next bullet, bump `as_of`, add Recent-changes entry, spill oldest entry
    > See draft below

- [ ] **Spill** `wiki/trends/open-weight-momentum-broadens.md` → `wiki/history/trends/open-weight-momentum-broadens.md` — oldest Recent-changes entry falls off the 10-entry cap
    > See draft below

- [ ] **Create** `wiki/sources/tweets/0xbakeer-qwen38-flash-next-2026-08-26.md` — source summary

## Page drafts

### wiki/trends/open-weight-momentum-broadens.md (updated)

```md
---
as_of: 2026-08-29
sources: [..., ainews-openai-shuts-off-cursor-2026-08-29, 0xbakeer-qwen38-flash-next-2026-08-26]
---

## Current signal

(... existing bullets unchanged ...)

- **Tencent Hy4-preview and Qwen3.8-Flash extend the wave (August 2026):** Tencent Hunyuan's Hy4-preview (770B total/49B active, 1M context, framed as "open source frontier") posted a 115-point Code Arena: WebDev jump over Hy3 and reportedly leads SWE-bench Pro. Alibaba pushed Qwen3.8-Flash (125B/6B active, 1M context, multimodal) into OpenCode Go at ~20x lower cost than Qwen3.8 Max, with an early FP8 multi-turn bug fixed by switching KV cache to BF16. A recovered independent-practitioner thread (@0xBakeer) gives a detailed architecture account of a related/same-generation variant, Qwen3.8-Flash-Next (180B total/6B active): 51B of its parameters sit in an n-gram embedding lookup table — never multiplied against anything, so it can be memory-mapped off an SSD rather than held in RAM, letting the 180B model fit a 128GB unified-memory box. Note: "Qwen3.8-Flash-Next" and "Qwen3.8-Flash" may be the same model described two ways, or distinct siblings; this page treats them as related but unconfirmed-identical pending an Alibaba primary source.

## Recent changes

- [2026-08-29] Tencent Hy4-preview and Qwen3.8-Flash extend the open-weight wave; independent-practitioner thread details Qwen3.8-Flash-Next's 51B n-gram lookup-table architecture and its SSD-served, 128GB-unified-memory serving recipe.
- (... existing entries follow, oldest entry spilled below ...)
```

### wiki/history/trends/open-weight-momentum-broadens.md (updated)

```md
## Archived from current page on 2026-09-08

- [2026-07-28] <exact text of whichever 2026-07-28 entry is oldest on the live page at apply time>
```

### wiki/sources/tweets/0xbakeer-qwen38-flash-next-2026-08-26.md (new)

```md
---
title: "0xBakeer on X: \"the 51B nobody talks about\" — Qwen3.8-Flash-Next architecture explainer"
type: source
source_type: tweet
source_file: raw/tweets/2026-09-07-0xbakeer-2092644019830431817.md
url: https://x.com/0xbakeer/status/2092644019830431817?s=12
published: 2026-08-26
ingested: 2026-09-08
domains: [models]
---

# 0xBakeer — Qwen3.8-Flash-Next's 51B n-gram embedding table

Independent practitioner thread explaining Qwen3.8-Flash-Next's second embedding table (n-gram lookup, 51B of 180B total params) and a practical DGX Spark serving recipe that went from 22 to 97 tok/s over several days.

## Influenced pages

- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Qwen3.8-Flash-Next architecture bullet

## Key claims extracted

- Qwen3.8-Flash-Next: 180B total params, 6B active, plus a 51B n-gram embedding lookup table
- The lookup table is never multiplied against anything — pure memorization, not computation — so it can be memory-mapped off NVMe/SSD instead of held in RAM
- This is what lets the 180B model fit on a 128GB unified-memory machine at Q4
- Serving recipe on a single DGX Spark improved from 22 tok/s to 97 tok/s (llama.cpp, then vLLM + NVFP4 + the model's own MTP draft head)
```

## Open questions

- Is "Qwen3.8-Flash-Next" the same model as "Qwen3.8-Flash," or a distinct sibling? Worth checking Alibaba's own model card/naming before a future proposal merges these into one claim.
