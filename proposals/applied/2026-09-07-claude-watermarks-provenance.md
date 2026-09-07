---
type: proposal
source: raw/newsletters/2026-08-13-ainews-spacexai-grok-46-and-grok-bot.md
status: pending
created: 2026-09-07
---

# Proposal: Claude text watermarking + file provenance rollout

## Summary

### The source

*(Note: the original triage entry for this signal mis-cited its source as the 2026-08-12 reasoning-trace-theft digest. That digest doesn't contain this content — it actually appears in the 2026-08-13 AINews issue, in an r/LocalLLaMA recap section titled "Claude Text Watermarking Rollout." This proposal draws from the correct file.)*

An AINews digest recaps a Reddit thread breaking down Anthropic's own support-article language on how Claude marks AI-generated content. The careful version of the claim, per commenters reading Anthropic's description, is that Claude applies metadata/provenance signals rather than a classic "watermark baked into visible text" — the mechanism and how long it survives depend on file type and workflow, and can be lost after heavy editing, export, or platform handling. Beyond that cautious framing, commenters also cite a more specific submission detail: Claude models launched on or after August 2, 2026 embed an imperceptible model-level text watermark, intended to survive copy-paste and light editing without changing readability, and supported file outputs (.png, .jpg, .svg) carry digitally signed C2PA provenance metadata. Third-party detection tooling isn't out yet, and older models are expected to be updated during a transition period. A separate sub-thread explains the likely mechanism in plain terms: a keyed generation-time scheme that slightly biases which "next token" the model picks, detectable later via a statistical test (comparable to Google's SynthID-Text) — robust to copy/paste and small edits, but degraded or destroyed by heavy paraphrasing or regeneration through another model.

### What changes

The wiki currently has no note on Claude's watermarking or file-provenance behavior anywhere. This adds one.

- **Claude Sonnet 5** gains a new Current-status bullet describing the watermarking/provenance rollout (applies to Claude models broadly, not Sonnet 5 specifically — see Open Questions) and a new Recent-changes entry dated 2026-08-13; `sources` picks up the new source id. No cap spill — the page has 3 entries today, under any configured cap.
- New source page for the AINews 2026-08-13 issue, since no page yet exists for that raw file.

### What to weigh

This is a cross-model Anthropic product/policy change, not something specific to Sonnet 5 — I picked Sonnet 5 as the anchor page only because it's the most recently active, most current Claude model page in the wiki, and there's no general "Anthropic product policy" or dedicated provenance/watermarking page to hang it on instead. Sourcing is also once-removed: this is a Reddit recap of Anthropic's own support-article wording, not the support article itself, so exact phrasing (e.g. "imperceptible," the precise August 2 cutoff) should be read as community paraphrase rather than a verbatim Anthropic quote.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/claude-sonnet-5.md` — add watermarking/provenance bullet to Current status, new Recent-changes entry, merge new source id
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-spacexai-grok-46-2026-08-13.md` — source summary for the 2026-08-13 AINews issue

## Page drafts

### wiki/models/claude-sonnet-5.md (updated)

```md
## Current status (as of 2026-08-11)

- Every's Vibe Check found Sonnet 5 broadly competent at writing, structured knowledge work, and some coding tasks, but hard to prefer over Opus 4.8, Fable 5, or GPT-5.5 for many specific jobs.
- Anthropic's official launch positions Sonnet 5 as its most agentic Sonnet model yet, available across Claude plans, Claude Code, and the API as `claude-sonnet-5`.
- Pricing of $2/M input and $10/M output, originally introductory, was made permanent as of 2026-08-11 (the scheduled step-up to $3/M input and $15/M output was cancelled).
- The Code reports the model can cost more per finished task than expected because the same work may tokenize larger and run more reasoning loops.
- Artificial Analysis coverage cited by The Code says high-effort Sonnet 5 can cost about 15% more per task than Opus 4.8, while lower effort settings remain cheaper.
- Ramp Labs' benchmark coverage suggests the extra effort can buy tighter self-correction, so the right comparison is cost per completed task, not token list price.
- Claude models launched on or after 2026-08-02 (including Sonnet 5) embed an imperceptible, generation-time text watermark meant to survive copy-paste and light edits, plus signed C2PA provenance metadata on supported file outputs (.png/.jpg/.svg); third-party detection tooling isn't out yet, and heavy paraphrasing or regeneration through another model likely defeats the text signal.

## Recent changes

- [2026-06-30] Official Anthropic launch details added: Claude Code/API availability, `claude-sonnet-5` API name, promotional pricing, effort-level framing, and safety notes.
- [2026-07-02] Every and The Code reported early testing: capable but not clearly best-in-class; cost per task depends heavily on effort and tokenizer behavior.
- [2026-08-11] Introductory $2/M input, $10/M output pricing made permanent; the scheduled step-up to $3/M input, $15/M output was cancelled.
- [2026-08-13] Added note on Claude's rollout of imperceptible text watermarking and C2PA file-provenance metadata for models launched on/after 2026-08-02.

## Sources

- [Every - Sonnet 5 Vibe Check](../sources/newsletters/every-sonnet-5-vibe-check-2026-07-02.md)
- [The Code - Devin Security / Sonnet 5 cost analysis](../sources/newsletters/the-code-devin-security-2026-07-02.md)
- [Every - A Tale of Two Models](../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
- [Claude Sonnet 5 official launch](../sources/articles/claude-sonnet-5-official-2026-06-30.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
- [AINews — SpaceXAI Grok 4.6 and Grok Bot](../sources/newsletters/ainews-spacexai-grok-46-2026-08-13.md)
```

Frontmatter `sources:` list gains `ainews-spacexai-grok-46-2026-08-13`.

### wiki/sources/newsletters/ainews-spacexai-grok-46-2026-08-13.md (new)

```md
---
title: AINews — SpaceXAI Grok 4.6 and Grok Bot
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-13-ainews-spacexai-grok-46-and-grok-bot.md
url: https://www.latent.space/p/ainews-spacexai-grok-46-and-grok
published: 2026-08-13
ingested: 2026-09-07
domains: [models]
---

# AINews — SpaceXAI Grok 4.6 and Grok Bot

A dense AINews digest covering the same-day Grok 4.6/Grok Bot, Qwen3.8-Max, DeepSeek V4 Pro, and MAI-Thinking-1 launches, plus a Reddit recap section explaining Anthropic's rollout of imperceptible Claude text watermarking and C2PA file-provenance metadata for models launched on or after 2026-08-02.

## Influenced pages

- [Claude Sonnet 5](../../models/claude-sonnet-5.md) — added a note on Claude's text-watermarking/file-provenance rollout

## Key claims extracted

- Claude models launched on/after 2026-08-02 embed an imperceptible, generation-time text watermark surviving copy-paste and light edits.
- Supported file outputs (.png/.jpg/.svg) carry digitally signed C2PA provenance metadata.
- Third-party detection tooling not yet available; older models to be updated during a transition period.
- Mechanism (per commenter explanation): keyed token-sampling bias, detected via a statistical z-score-like test; degrades under heavy paraphrasing or cross-model regeneration.
- Per Anthropic's own support-article framing, the robust claim is metadata/provenance marking, not an "undeletable" text watermark.
```

## Open questions

- Should this same watermarking/provenance note also be added to `wiki/models/claude-opus-5.md` and other current Anthropic model pages, since the rollout applies to all Claude models launched after 2026-08-02, not just Sonnet 5? I anchored it on Sonnet 5 alone to keep this a lightweight, single-page ingest per the triage's recommendation, but happy to expand on approval.
- If watermarking/provenance becomes a recurring topic across labs (the source itself notes OpenAI and Google have parallel efforts), it may eventually deserve its own `concepts/` page rather than being a bullet buried in a model page.
