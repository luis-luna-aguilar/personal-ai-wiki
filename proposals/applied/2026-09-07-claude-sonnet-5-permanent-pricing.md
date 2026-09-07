---
type: proposal
source: raw/newsletters/2026-08-11-ainews-muse-glimmer-and-spark-open-weights-retu.md
status: pending
created: 2026-09-07
---

# Proposal: Claude Sonnet 5's introductory pricing becomes permanent

## Summary

### The source

AINews' August 11 digest (covering 2026-08-08 through 2026-08-10) includes a brief item, cited to @claudeai, noting that Anthropic has made Claude Sonnet 5's introductory API pricing — $2 per million input tokens, $10 per million output tokens — permanent, rather than letting it expire into the higher post-launch rate as originally announced. AINews frames this as a competitive move, made "amid a rapidly strengthening open and semi-open field" where models like DeepSeek V4 Flash, Kimi K3, and Qwen 3.8 Max keep pushing price/performance expectations down.

### What changes

The wiki's Claude Sonnet 5 page currently states launch pricing "through 2026-08-31, then $3/M input and $15/M output" — implying a step-up was still scheduled. That step-up is now cancelled.

- **Claude Sonnet 5** drops the "through 2026-08-31, then $3/M input and $15/M output" language and states the $2/$10 pricing as permanent; gains a Recent-changes entry; page date moves to 11 August.
- **Wiki index** — the Claude Sonnet 5 line's date moves to 11 August.
- New source page for the AINews issue this pricing note comes from.

### What to weigh

This is a single-fact confirmation from a secondary aggregator (AINews summarizing a tweet), not a primary Anthropic pricing-page citation — the underlying claim is narrow and low-risk, but if Anthropic's own pricing page phrases the change differently, that would be the more authoritative wording to prefer.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/claude-sonnet-5.md` — pricing bullet updated to permanent, Recent-changes entry added, as_of bumped
    > See draft below

- [ ] **Update** `wiki/index.md` — Claude Sonnet 5 line's as_of date moves to 2026-08-11

- [ ] **Create** `wiki/sources/newsletters/claude-sonnet-5-permanent-pricing-2026-08-11.md` — source summary

## Page drafts

### wiki/models/claude-sonnet-5.md (updated)

Frontmatter:
```
as_of: 2026-08-11
sources: [every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-sonnet-5-official-2026-06-30, claude-sonnet-5-permanent-pricing-2026-08-11]
```

`## Current status` pricing bullet — replace:
```
- Launch pricing is $2/M input and $10/M output through 2026-08-31, then $3/M input and $15/M output.
```
with:
```
- Pricing of $2/M input and $10/M output, originally introductory, was made permanent as of 2026-08-11 (the scheduled step-up to $3/M input and $15/M output was cancelled).
```

`## Recent changes` — add one new entry at the top (delta only; live list currently has 2 entries, well under the cap of 10, so nothing spills):
```
- [2026-08-11] Introductory $2/M input, $10/M output pricing made permanent; the scheduled step-up to $3/M input, $15/M output was cancelled.
```

`## Sources` — append:
```
- [AINews - Muse Glimmer and Spark: Open Weights return Personal Superintelligence promise](../sources/newsletters/claude-sonnet-5-permanent-pricing-2026-08-11.md)
```

### wiki/index.md (updated)

Update the Claude Sonnet 5 line's trailing date only:
```
- [models/claude-sonnet-5](models/claude-sonnet-5.md) — Anthropic middle-tier Claude 5 model; official Claude Code/API availability plus early high-effort cost-per-task caveats *(as_of: 2026-08-11)*
```

### wiki/sources/newsletters/claude-sonnet-5-permanent-pricing-2026-08-11.md (new)

```md
---
title: "AINews — Muse Glimmer and Spark: Open Weights return Personal Superintelligence promise"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-11-ainews-muse-glimmer-and-spark-open-weights-retu.md
url: https://www.latent.space/p/ainews-muse-glimmer-and-spark-open
published: 2026-08-11
ingested: 2026-09-07
domains: [models]
---

# AINews — Muse Glimmer and Spark: Open Weights return Personal Superintelligence promise

AINews recap covering 2026-08-08 to 2026-08-10, led by Meta's Muse Glimmer open-weight release and Zuckerberg's "Personal Superintelligence" follow-up essay. Among the Twitter-recap items: Anthropic made Claude Sonnet 5's introductory pricing ($2/M input, $10/M output) permanent rather than letting it rise to the previously announced post-launch rate, read as a competitive response to a strengthening open/semi-open model field.

## Influenced pages

- [models/claude-sonnet-5](../../models/claude-sonnet-5.md) — pricing bullet updated to reflect permanent $2/$10 pricing

## Key claims extracted

- Claude Sonnet 5 API pricing ($2/M input, $10/M output) is now permanent, not introductory
- The previously announced step-up to $3/M input, $15/M output will not happen
- Move read as competitive pressure from open and semi-open-weight models
```
