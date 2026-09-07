---
type: proposal
source: raw/newsletters/2026-07-24-ainews-black-forest-labs-flux-3-multimodal-flo.md
status: pending
created: 2026-09-06
---

# Proposal: Health in ChatGPT rolls out in the U.S.

## Summary

### The source

AINews' July 24 digest (covering AI activity from July 22-23) is mostly about Black Forest Labs' FLUX 3 launch, but buries a smaller rollout that the digest itself calls "more strategically important than it may first appear": OpenAI's U.S. launch of Health in ChatGPT. The feature connects a user's Apple Health data and supported medical records directly into ChatGPT. OpenAI's stated implementation details: connected health data gets additional encryption, is excluded from foundation-model training and ad targeting, and the feature was built with what OpenAI describes as substantial physician review. The digest frames this as a new application layer on top of existing model capability rather than a new model — the news is the product surface, not new intelligence.

### What changes

`state-of/healthcare.md` already tracks a "Patient-side AI" subcategory (frontier models plus a structured investigation process matching or exceeding PCP visits for ambiguous symptoms) but nothing about consumer health-data integration specifically.

- **State of Healthcare** gains a new bullet under Patient-side AI for Health in ChatGPT — the connected-data mechanics, the privacy/training-exclusion claims, and the physician-review claim — plus a new Recent-changes entry dated 22 July. `sources:` gains the new source id.
- New source page for this AINews digest, since it's the first ingest from this raw file (later proposals from this same digest may extend it rather than duplicate — check before applying).

### What to weigh

This is single-sourced from one newsletter's brief mention, not OpenAI's own announcement page or a fuller writeup — the privacy and physician-review claims are OpenAI's own characterization, not independently verified. Treat this as a lightweight product-surface note rather than a deeply verified claim.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/healthcare.md` — add Health in ChatGPT under Patient-side AI, new Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-black-forest-labs-flux-3-2026-07-24.md` — source summary (check for an existing page for this raw file before creating; if a sibling proposal from the same digest already created one, extend it instead)

## Page drafts

### wiki/state-of/healthcare.md (updated)

Add under `### Patient-side AI` (after the existing bullet):

```md
- **Health in ChatGPT** — OpenAI's U.S. rollout connecting Apple Health and supported medical records into ChatGPT; connected health data gets additional encryption, is excluded from foundation-model training and ad targeting, per OpenAI built on substantial physician review *(as of 2026-07-22)*
```

Add to `## Recent changes` (newest first):

```md
- [2026-07-22] Health in ChatGPT rolled out in the U.S. — connects Apple Health and medical records, with encryption and training/ad-targeting exclusions for connected health data.
```

Add `ainews-black-forest-labs-flux-3-2026-07-24` to the page's frontmatter `sources:` list. Bump `as_of` to 2026-07-22 (newer than the page's current 2026-06-18).

### wiki/sources/newsletters/ainews-black-forest-labs-flux-3-2026-07-24.md (new)

```md
---
title: "[AINews] Black Forest Labs FLUX 3 - Multimodal Flow Models"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-24-ainews-black-forest-labs-flux-3-multimodal-flo.md
url: https://www.latent.space/p/ainews-black-forest-labs-flux-3-multimodal
published: 2026-07-24
ingested: 2026-09-06
domains: [healthcare]
---

# [AINews] Black Forest Labs FLUX 3 - Multimodal Flow Models

AINews digest covering AI activity from 2026-07-22 to 2026-07-23. Primarily about Black Forest Labs' FLUX 3 unified image/video/audio/robotics model, with additional coverage of OpenAI's ChatGPT Voice desktop rollout, Health in ChatGPT's U.S. launch, The Stack v3 open-code dataset, and continued Hugging Face incident fallout discussion.

## Influenced pages

- [State of Healthcare](../../state-of/healthcare.md) — added Health in ChatGPT under Patient-side AI

## Key claims extracted

- OpenAI launched Health in ChatGPT for U.S. users, connecting Apple Health and supported medical records
- Connected health data gets additional encryption, excluded from foundation-model training and ad targeting
- OpenAI describes the feature as built on substantial physician review
```

## Schema / vocabulary additions

None.
