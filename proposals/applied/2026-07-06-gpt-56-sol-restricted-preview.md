---
type: proposal
sources:
  - raw/newsletters/2026-06-29-openai-drops-gpt-56-with-limited-access.md
  - raw/newsletters/2026-06-29-openais-new-models-are-government-gated-for-n.md
  - raw/newsletters/2026-06-28-everyone-gets-an-agent-almost-no-one-gets-the-mod.md
  - raw/articles/2026-07-06-openaicom-index-previewing-gpt-5-6-sol.md
status: pending
created: 2026-07-06
---

# Proposal: GPT-5.6 Sol restricted preview

## Summary
The checked newsletter cluster says OpenAI previewed GPT-5.6/Sol as a restricted coding and cybersecurity model lineup available only to vetted partners on API and Codex due to a U.S. government request. The official OpenAI page fetch was blocked and saved only a JavaScript verification page, so this proposal should be treated as newsletter-grounded until the official page is captured.

## Intended changes

- [x] **Update** `wiki/trends/restricted-frontier-deployment.md` — add GPT-5.6/Sol as a restricted frontier-access example.
    > **Add:** In late June 2026, newsletter coverage reported OpenAI's GPT-5.6/Sol preview was limited to a small vetted partner set for API and Codex access after a U.S. government request, making frontier model access itself a governed deployment surface.

- [x] **Update** `wiki/state-of/models.md` — add a caveated restricted-preview note, not a normal public model entry.
    > **Draft line:** GPT-5.6 / Sol — reported restricted private preview for coding and cybersecurity, not broadly available; official page still needs capture *(as of 2026-06-29)*.

- [x] **Create** `wiki/sources/newsletters/gpt-56-sol-restricted-preview-2026-06.md` — source summary with official-fetch caveat.

## Updated Page Snippets

### `wiki/trends/restricted-frontier-deployment.md`

> **Before:**
> `The Fable 5 ban introduced a mechanism distinct from voluntary capability gating: mandatory government compliance.`

> **After:**
> `The Fable 5 ban introduced a mechanism distinct from voluntary capability gating: mandatory government compliance. Newsletter coverage of OpenAI's GPT-5.6/Sol restricted preview suggests the same access-control pattern may now extend beyond Anthropic: frontier model availability can be shaped by government requests, vetted partner lists, and staged API/Codex access rather than normal public launch.`

### `wiki/state-of/models.md`

> **Before:**
> `- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; leads on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and BixBench *(as of 2026-05-13)*`

> **After:**
> `- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; leads on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and BixBench *(as of 2026-05-13)*`
> `- **GPT-5.6 / Sol** — OpenAI; newsletter-reported restricted private preview for coding and cybersecurity via API/Codex, not broadly available; official source fetch still needs clean capture *(as of 2026-06-29)*`

## Page Drafts

### `wiki/sources/newsletters/gpt-56-sol-restricted-preview-2026-06.md` (new)

```md
---
title: GPT-5.6 Sol restricted preview
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-29-openai-drops-gpt-56-with-limited-access.md
published: 2026-06-29
ingested: 2026-07-06
domains: [models, coding, cybersecurity]
---

# GPT-5.6 Sol restricted preview

Newsletter coverage reports that OpenAI previewed a GPT-5.6 lineup led by Sol for coding and cybersecurity, with access limited to vetted partners on API and Codex after a U.S. government request. A direct fetch of the official OpenAI page was blocked by JavaScript verification, so the wiki should keep this as a caveated restricted-preview signal unless the official page is later captured.

## Influenced pages
- [Restricted frontier deployment](../../trends/restricted-frontier-deployment.md) — OpenAI restricted-preview example
- [State of Models](../../state-of/models.md) — caveated restricted-preview note

## Key claims extracted
- GPT-5.6/Sol is described by the newsletters as OpenAI's strongest coding/cybersecurity model family at preview time.
- Access was reportedly limited to a small set of vetted companies through API and Codex.
- The restriction was framed as tied to a government request and broader policy debate over frontier model release.

## Source caveat
- `raw/articles/2026-07-06-openaicom-index-previewing-gpt-5-6-sol.md` contains only a JavaScript verification page, not the official article content.
```

## Open Questions
- Should this create a separate `wiki/models/gpt-5-6.md` page only after the official source is captured or public access broadens?
	- It should, but you also should be using the browser for when javascript is blocked. Find solutions please, you have tools at hand.
