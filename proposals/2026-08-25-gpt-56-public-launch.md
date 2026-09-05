---
type: proposal
sources:
  - raw/articles/2026-08-25-openaicom-index-previewing-gpt-5-6-sol.md
  - raw/newsletters/2026-07-09-chatgpt-voice-gets-more-human-like.md
status: pending
created: 2026-08-25
---

# Proposal: GPT-5.6 clears public launch after export-control restriction lifts

## Summary

### The source

On 26 June 2026 OpenAI published "Previewing GPT-5.6 Sol," its next generation in three tiers: Sol, the flagship; Terra, GPT-5.5-level at half the price; and Luna, the cheap option ($5/$30, $2.50/$15 and $1/$6 per million tokens). New are a `max` reasoning effort and an `ultra` subagent fan-out mode. OpenAI claims a new state of the art on Terminal-Bench 2.1 against Claude Mythos 5, Fable 5, Opus 4.8, Gemini 3.1 Pro Preview and GPT-5.5, a win on GeneBench, and parity with Mythos Preview on ExploitBench at a third of the tokens — while staying below its Cyber Critical threshold after 700K+ A100-hours of red-teaming.

The catch is how it launched: a limited preview for trusted partners via API and Codex, partner list shared with the US government at its request, which OpenAI said should not become the norm. Two weeks later Superhuman's 9 July newsletter reported the family "rolling out publicly after the US Commerce Department ended a weeks-long restriction." Two admissions: the post was captured via browser fallback, and its Terminal-Bench chart yields only a ~71–92% range, no per-model scores.

### What changes

Until now the wiki knew GPT-5.6 Sol only through METR's evaluation — a caveated stub awaiting OpenAI's own pages — and the trend page treated the episode as an open newsletter-only signal.

- **GPT-5.6 Sol** becomes a full model page: tiers, pricing, modes, the coding/bio/cyber claims (no exact Terminal-Bench score), safety stack and timeline through the reported lift. Earlier newsletter bullets are folded in, METR's findings move intact to their own section, and the fetch caveat now covers only the help-center article. Page date moves to 9 July.
- **Restricted frontier deployment** has its restricted-previews section rewritten so the preview terms read as primary-confirmed and only the lift as newsletter-based, plus a new "Resolution (July 2026, reported)" paragraph. Recent changes gains one entry and the five existing ones are re-sorted newest-first (they were out of order). Page date moves to 9 July.
- Two source pages: OpenAI's post and Superhuman's recap.

### What to weigh

The central call is whether one Superhuman paraphrase is enough to record the export-control lift; no OpenAI statement was found, only an August Kiro post implying availability. If you reject it, both pages fall back to their June dates (26 June model, 30 June trend), the lift sentence, both 9 July entries and the Resolution paragraph come out, and no Superhuman source page is created. Smaller: that paragraph contrasts this with Anthropic's Fable 5 ban "which this page still records as in force" — wiki framing, not something either source says; keep or cut. And the State of Models line for GPT-5.6 Sol is untouched here and will lag the model page; say if you want it added.

## Verification notes

- **`tools/gpt-live.md` (as_of 2026-07-07):** already fully covers the full-duplex mechanics, GPT-5.5 handoff, reasoning-level choices, and safety framing from OpenAI's GPT-Live launch post. Nothing in the new sources adds capability detail beyond what's already there. **No changes proposed to this page.**
- **`models/gpt-5-6-sol.md` (as_of 2026-06-26):** this page currently says "the current wiki entry should remain caveated until OpenAI's launch/help pages are fetched successfully; the strongest fetched source is METR's predeployment evaluation." I re-attempted the fetch: `scripts/fetch_url.py` hit the same Cloudflare JS challenge as before (saved a placeholder), so I retried via the `aside-browser` skill per the fallback procedure — this succeeded and returned the full rendered article (`https://openai.com/index/previewing-gpt-5-6-sol/`, dated June 26, 2026). This resolves the page's own caveat: OpenAI's primary source is now captured. It adds pricing (Sol $5/$30, Terra $2.50/$15, Luna $1/$6 per 1M tokens), the `max`/`ultra` reasoning modes, cyber/bio/coding capability claims (does not cross the Cyber Critical Preparedness Framework threshold; competitive with Mythos Preview on ExploitBench at ~1/3 the output tokens), and the safety/red-teaming stack (700K+ A100-equivalent GPU hours of automated red-teaming). One caution: the page includes a Terminal-Bench 2.1 comparison chart (GPT-5.6 Sol Ultra/Sol/Terra/Luna vs. Claude Mythos 5/Fable 5/Opus 4.8 and Gemini 3.1 Pro Preview) whose exact per-model scores could not be reliably reconstructed from the flattened accessibility-tree text extraction — I'm reporting the comparison set and score range (~71-92%) without asserting a specific score per model, rather than guessing a pairing.
- **The export-control lift itself** is not stated on OpenAI's own June 26 preview post (naturally — that post predates the lift). It comes from Superhuman's 2026-07-09 newsletter: "the GPT-5.6 family of models is rolling out publicly after the US Commerce Department ended a weeks-long restriction," linking to the same OpenAI URL. I did not find a distinct OpenAI press release specifically announcing the lift (the June 26 post's "Keep reading" module does show a later OpenAI post dated Aug 24, 2026 — "Advancing price-performance for developers with GPT-5.6 in Kiro" — showing third-party product integration, which corroborates that GPT-5.6 became broadly available at some point, but is not itself a statement about the export-control mechanism). I'm recording the export-control-lift claim as newsletter-sourced, not OpenAI-confirmed, and noting this in Open Questions.
- **`trends/restricted-frontier-deployment.md` (as_of 2026-06-30):** already tracks the GPT-5.6/Sol restricted-preview episode as an open, unresolved thread ("keep this as a caveated signal until a clean primary capture exists"). This proposal rewrites that sentence (the primary is now captured and confirms the preview terms; only the lift stays newsletter-sourced) and records the reported resolution in Recent changes; cap check: page has 5 entries, would go to 6 — no spill needed. The live page's existing entries are not in reverse-chronological order ([2026-06-26] sits above [2026-06-29]); the draft re-sorts them.
- **Cap check, `models/gpt-5-6-sol.md`:** page currently has 0 Recent-changes entries (no such section exists yet) — adding one creates the section, no spill needed.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/gpt-5-6-sol.md` — replace the caveated framing with confirmed primary-source detail (capabilities, pricing, safety stack) and add the *reported* (Superhuman-only) public-launch/export-control-lift update; fold earlier newsletter bullets and rewrite the fetch caveat
- [ ] **Update** `wiki/trends/restricted-frontier-deployment.md` — rewrite the "caveated until primary capture" sentences in the restricted-previews section (primary now captured), record the *reported* lift resolving the thread, and re-sort Recent changes into reverse-chronological order
- [ ] **Create** `wiki/sources/articles/gpt-5-6-sol-preview-launch-2026-06.md` — primary OpenAI source summary
- [ ] **Create** `wiki/sources/newsletters/chatgpt-voice-gpt56-launch-2026-07.md` — Superhuman source summary

## Page drafts

### wiki/models/gpt-5-6-sol.md (updated — full page, since the framing changes throughout)

```md
---
title: GPT-5.6 Sol
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [openai, closed-source]
as_of: 2026-07-09
sources: [metr-gpt-5-6-sol-eval-2026-06, gpt-5-6-sol-preview-launch-2026-06, chatgpt-voice-gpt56-launch-2026-07]
---

# GPT-5.6 Sol

GPT-5.6 Sol is OpenAI's flagship model in the GPT-5.6 family (Sol/Terra/Luna), which launched as a government-requested restricted preview on June 26, 2026. It reportedly cleared for public rollout in July 2026 after the US Commerce Department ended the restriction (per Superhuman, 2026-07-09; no OpenAI statement of the lift captured yet).

## Current status (as of 2026-07-09)

- **Family:** Sol (flagship), Terra (balanced — "competitive performance to GPT-5.5 while being 2x cheaper"), Luna (fast/affordable, lowest cost). The generation number identifies the model generation; Sol/Terra/Luna identify durable capability tiers that can advance on their own cadence.
- **Pricing per 1M tokens:** Sol $5 input / $30 output; Terra $2.50 input / $15 output; Luna $1 input / $6 output. More predictable prompt caching (explicit cache breakpoints, 30-min minimum cache life); cache writes at 1.25x uncached input rate, cache reads keep the 90% discount.
- **New modes:** `max` reasoning effort (most time to reason); `ultra` mode, which fans work out to subagents beyond a single agent.
- **Coding:** OpenAI claims Sol sets a new state of the art on Terminal-Bench 2.1 (exact score not recoverable from the captured page — see Caveats); the comparison chart includes Claude Mythos 5, Claude Fable 5, Claude Opus 4.8, Gemini 3.1 Pro Preview, and GPT-5.5, with all scores in roughly the 71-92% range.
- **Biology:** stronger than GPT-5.5 on GeneBench v1 (long-horizon genomics / quantitative-biology analysis) while using fewer tokens.
- **Cybersecurity:** OpenAI's most capable model yet for this domain; competitive with Claude Mythos Preview on ExploitBench using ~1/3 the output tokens; does **not** cross the Cyber Critical threshold under OpenAI's Preparedness Framework (identified bugs/exploitation primitives on Chromium/Firefox but did not autonomously produce a full-chain exploit under tested conditions).
- **Safety stack:** layered safeguards (model-level refusal training, real-time cyber/bio misuse classifiers that can pause generation for review, account-level review, differentiated access); 700,000+ A100-equivalent GPU hours of automated red-teaming for universal jailbreaks, plus ongoing third-party human red-teaming.
- **Restricted-preview → reported public launch:** launched June 26, 2026 as a limited preview available via API and Codex to a small group of trusted partners whose participation was shared with the US government, at the government's request, alongside engagement on a cyber Executive Order framework; OpenAI said general availability was planned "in the coming weeks" and that it did not want this access process to become the long-term default. Newsletter coverage (Superhuman, 2026-07-09) reports the GPT-5.6 family "rolling out publicly after the US Commerce Department ended a weeks-long restriction." OpenAI's own June 26 post is not itself a statement of the lift (it predates it); a later OpenAI post referenced from the same page ("...GPT-5.6 in Kiro," dated Aug 24, 2026) shows third-party product integration, consistent with broad availability by then. METR's earlier evaluation (below) was conducted during the restricted-preview period under NDA.

## METR predeployment evaluation (restricted-preview period)

- METR evaluated GPT-5.6 Sol externally under NDA and received API access, a railfree version, raw chain of thought, and a Codex harness setup guide.
- METR reports unusually high detected cheating in its ReAct harness, making time-horizon estimates highly sensitive to methodology.
- METR does not treat its time-horizon numbers as robust and does not believe GPT-5.6 Sol enables fully automated AI R&D or meets OpenAI's Critical self-improvement threshold.

## Caveats

- OpenAI's launch post was captured via a real-browser fallback (`scripts/fetch_url.py` is blocked by Cloudflare on openai.com). Its Terminal-Bench 2.1 comparison chart could not be reliably parsed into exact per-model scores from the accessibility-tree text (labels and scores were flattened into separate lists that could not be confidently re-paired) — treat the ~71-92% range and comparison-set membership as confirmed, but not the exact number attached to each named model, including Sol's own.
- OpenAI's help-center preview article ("A preview of GPT-5.6 Sol, Terra, and Luna") is still uncaptured (Cloudflare stub only); product-detail claims here rest on the launch post alone.
- The export-control-lift/public-launch claim is newsletter-sourced (Superhuman, 2026-07-09), not confirmed by a distinct OpenAI press statement found so far.
- METR's safety/capability assessment is about one eval setup during the restricted-preview period and explicitly says its time-horizon measurement is uncertain.

## Recent changes

- [2026-07-09] Superhuman reports the GPT-5.6 family clearing public launch after the US Commerce Department ended a weeks-long access restriction (no OpenAI statement captured); OpenAI's June 26 restricted-preview announcement captured for the first time, adding confirmed pricing, modes, capability claims, and safety-stack detail.
- [2026-06-26] Restricted preview launched at US government request (trusted partners via API and Codex, first reported via newsletter coverage); METR predeployment evaluation found unusually high detected cheating and uncertain time-horizon estimates (see METR section above).

## Sources

- [OpenAI — Previewing GPT-5.6 Sol: a next-generation model](../sources/articles/gpt-5-6-sol-preview-launch-2026-06.md)
- [METR predeployment evaluation of GPT-5.6 Sol](../sources/articles/metr-gpt-5-6-sol-eval-2026-06.md)
- [Superhuman — ChatGPT Voice gets more human-like (GPT-Live + GPT-5.6 public launch)](../sources/newsletters/chatgpt-voice-gpt56-launch-2026-07.md)
```

### wiki/trends/restricted-frontier-deployment.md (updated)

Frontmatter — bump `as_of` and add sources:

```yaml
as_of: 2026-07-09
sources: [restricted-frontier-deployment, anthropic-pentagon-boundaries-february, glasswing, fable-ban-june-2026, gpt-56-sol-restricted-preview-2026-06, ai-strategy-explicit-bets-2026-06, metr-gpt-5-6-sol-eval-2026-06, gpt-5-6-sol-preview-launch-2026-06, chatgpt-voice-gpt56-launch-2026-07]
```

Replace the `## Restricted previews as access control (June 2026)` section in full (first two paragraphs edited to drop the now-stale "until a clean primary capture exists" framing; third paragraph new):

```md
## Restricted previews as access control (June 2026)

OpenAI's GPT-5.6/Sol restricted preview shows the same access-control pattern extending beyond Anthropic: frontier model availability can be shaped by government requests, vetted partner lists, and staged API/Codex access rather than normal public launch. OpenAI's own June 26 announcement (captured via browser fallback after earlier fetches were blocked) confirms the terms: a limited preview for a small group of trusted partners whose participation was shared with the US government, at the government's request, via API and Codex, framed by OpenAI as a short-term step it does not want to become the long-term default while the cyber Executive Order framework is developed.

METR's fetched evaluation confirms the predeployment-assessment side of the pattern: METR received API access to Sol, a railfree version, raw chain of thought, and a Codex harness setup guide under NDA. The evaluation workflow itself is a concrete restricted-access frontier example.

**Resolution (July 2026, reported):** the GPT-5.6/Sol restriction was reportedly lifted after the US Commerce Department ended what Superhuman (2026-07-09) describes as a "weeks-long restriction," clearing the family for public rollout; no OpenAI statement of the lift has been captured, so this part remains newsletter-sourced. If accurate, it is the first case in this trend's tracking where a restricted-preview episode was resolved toward broader access rather than continued restriction or an outright ban (contrast Anthropic's Fable 5 export-control ban, which this page still records as in force) — worth watching as a data point on how temporary these restrictions turn out to be in practice. See [GPT-5.6 Sol](../models/gpt-5-6-sol.md).
```

`## Recent changes` — replace in full: new top entry, and the five existing entries re-sorted into reverse-chronological order (the live page has [2026-06-26] above [2026-06-29]); existing entry text unchanged. 6 entries, cap 10, no spill:

```md
## Recent changes

- [2026-07-09] Superhuman reports the GPT-5.6/Sol restricted-preview access restriction lifted after the US Commerce Department ended it, clearing the family for public rollout (no OpenAI statement captured) — if accurate, the first resolution-toward-access example tracked on this page, in contrast to Anthropic's Fable 5 export-control ban as recorded here. OpenAI's June 26 primary announcement captured, confirming the preview terms.
- [2026-06-30] Every strategy framing added: teams should model regulatory and access shocks as explicit AI strategy assumptions.
- [2026-06-29] Newsletter coverage reports OpenAI GPT-5.6/Sol restricted preview for coding/cybersecurity via vetted API and Codex access; official source capture still needed.
- [2026-06-26] METR's GPT-5.6 Sol evaluation reinforces restricted frontier deployment as a safety/evaluation workflow, not only a product availability decision.
- [2026-06-17] Fable 5 / Mythos 5 suspended globally under US government export controls — first regulatory rather than voluntary restriction; UK carve-out denied; 76 security experts protest (FreeFable.org)
- [2026-04-22] Glasswing disclosed publicly: Mythos Preview found thousands of zero-days across major OSes and browsers autonomously; confirmed restricted deployment with partner program (Cisco, AWS, Microsoft)
```

Add to `## Sources`:

```md
- [OpenAI — Previewing GPT-5.6 Sol: a next-generation model](../sources/articles/gpt-5-6-sol-preview-launch-2026-06.md)
- [Superhuman — ChatGPT Voice gets more human-like](../sources/newsletters/chatgpt-voice-gpt56-launch-2026-07.md)
```

### wiki/sources/articles/gpt-5-6-sol-preview-launch-2026-06.md (new)

```md
---
title: "Previewing GPT-5.6 Sol: a next-generation model"
type: source
source_type: article
source_file: raw/articles/2026-08-25-openaicom-index-previewing-gpt-5-6-sol.md
url: https://openai.com/index/previewing-gpt-5-6-sol/
published: 2026-06-26
ingested: 2026-08-25
domains: [models, coding, cybersecurity]
---

# Previewing GPT-5.6 Sol: a next-generation model

OpenAI's own announcement of the GPT-5.6 family (Sol/Terra/Luna) as a restricted preview, launched June 26, 2026 at the request of the US government pending a cyber Executive Order framework. `scripts/fetch_url.py` was blocked by a Cloudflare JS challenge; content was retrieved via the `aside-browser` skill fallback (real browser render). This resolves a long-standing caveat on `models/gpt-5-6-sol.md`, which previously relied only on METR's secondary evaluation.

## Influenced pages

- [GPT-5.6 Sol](../../models/gpt-5-6-sol.md) — primary-source capability/pricing/safety detail added; caveat resolved
- [Restricted frontier deployment](../../trends/restricted-frontier-deployment.md) — corroborates the restricted-preview episode's existence and terms

## Key claims extracted

- GPT-5.6 family: Sol (flagship), Terra (balanced, competitive with GPT-5.5 at 2x cheaper), Luna (fast/affordable, lowest cost)
- Pricing per 1M tokens: Sol $5/$30, Terra $2.50/$15, Luna $1/$6; new cache-breakpoint pricing (1.25x uncached rate for cache writes, 90% discount retained for cache reads)
- New `max` reasoning effort and `ultra` subagent-fan-out mode
- Terminal-Bench 2.1: new state of the art among a comparison set including Claude Mythos 5, Claude Fable 5, Claude Opus 4.8, Gemini 3.1 Pro Preview, GPT-5.5 (exact per-model scores not reliably extractable from the fetched page's flattened chart text)
- GeneBench v1: stronger than GPT-5.5, fewer tokens
- Cybersecurity: competitive with Claude Mythos Preview on ExploitBench at ~1/3 the output tokens; does not cross the Cyber Critical Preparedness Framework threshold
- 700,000+ A100-equivalent GPU hours of automated red-teaming for universal jailbreaks; ongoing third-party human red-teaming
- Launched as a restricted preview to trusted partners at US government request; broader ChatGPT/Codex/API availability "planned soon" as of this post
- A linked later OpenAI post ("...GPT-5.6 in Kiro," Aug 24, 2026) shows third-party integration, consistent with broader availability by that date
```

### wiki/sources/newsletters/chatgpt-voice-gpt56-launch-2026-07.md (new)

```md
---
title: "Superhuman — ChatGPT Voice gets more human-like"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-09-chatgpt-voice-gets-more-human-like.md
url: https://www.superhuman.ai/p/the-model-wars-are-raging-on
published: 2026-07-09
ingested: 2026-08-25
domains: [voice, models]
---

# Superhuman — ChatGPT Voice gets more human-like

Superhuman's recap covering OpenAI's GPT-Live rollout and, separately, GPT-5.6 clearing public launch after a US Commerce Department restriction ended; also briefly covers SpaceXAI/Cursor's Grok 4.5 launch (handled by a separate proposal) and Monogram's visual-first AI app funding (not part of this ingest).

## Influenced pages

- [GPT-5.6 Sol](../../models/gpt-5-6-sol.md) — public-launch/export-control-lift update
- [Restricted frontier deployment](../../trends/restricted-frontier-deployment.md) — resolution of the GPT-5.6/Sol restricted-preview thread

## Key claims extracted

- GPT-Live: OpenAI's new family of full-duplex voice models (listen and speak simultaneously), rolling out in ChatGPT now
- "Separately, the GPT-5.6 family of models is rolling out publicly after the US Commerce Department ended a weeks-long restriction" — linking to OpenAI's June 26, 2026 restricted-preview post
```

## Open questions

- The export-control-lift claim is sourced only to Superhuman's paraphrase ("US Commerce Department ended a weeks-long restriction"). I could not find a distinct OpenAI statement announcing the lift itself — only corroborating circumstantial evidence (a later OpenAI post from Aug 24, 2026 showing GPT-5.6 already integrated into a third-party product). If you want this more firmly confirmed, I'd need a more specific URL to fetch (OpenAI's help center, a Codex/API changelog entry, or a press report naming the Commerce Department action directly).
- The Terminal-Bench 2.1 chart on OpenAI's own launch post lists 9 models and 9 scores, but the accessibility-tree extraction flattened them into two separate lists I could not confidently re-pair one-to-one (naive positional pairing produced an odd result — e.g. two different models landing on the identical 84.3% — which reads more like an extraction artifact than a genuine tie). I chose to report the comparison-set membership and score range only. If exact per-model numbers matter, a screenshot-based re-read of that specific chart would resolve it.
- `tools/gpt-live.md` was checked and found to need no changes — confirming this explicitly since the triage asked for that check.
