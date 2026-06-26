---
type: proposal
sources:
  - raw/newsletters/2026-06-16-76-security-experts-say-free-fable.md
status: pending
created: 2026-06-17
---

# Proposal: Stanford AI labor market data — junior worker displacement

## Summary

Stanford's Digital Economy Lab (25,000-firm dataset) found that early-career workers aged 22-25 in AI-exposed occupations are declining 3.8%/yr since 2022, while least-exposed roles grow at 2.0%. Junior software developers and customer service workers are hardest hit. Concern: if entry-level roles disappear, the senior talent pipeline weakens ("hollow pipeline").

## Intended changes

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add Stanford data to the Junior talent problem section
- [x] **Update** `wiki/trends/agents-reshape-organizations.md` — add Stanford data as a concrete signal in the Concrete signals section

## Page drafts

### wiki/training/ai-enablement-software-development.md (updated section)

> **Frontmatter: update `as_of` to 2026-06-16; add `stanford-labor-june-2026` to sources.**

> **## The junior talent problem — update with Stanford data:**

> **Before (last paragraph of that section):**
```
Mid-career engineers may be the most vulnerable group — more so than juniors or seniors. ...
```
> **After (add after that paragraph):**
```
**Stanford AI Economic Indicators (June 2026):** The most rigorous data to date on junior displacement comes from Stanford's Digital Economy Lab, which analyzed 25,000 firms. Findings:
- Overall hiring has not surged or collapsed since ChatGPT's launch — the macro picture is stable
- But early-career workers aged 22-25 in AI-exposed occupations are declining at **3.8% per year**
- Least-exposed roles are growing at 2.0%
- Most affected: junior software developers, customer service workers
- Least affected: home health aides and other roles with low AI exposure
- Stanford explicitly labels these "early signals from a fixed sample" rather than a definitive global picture

The hollow pipeline concern is now data-backed: if the entry-level disappears, the senior pipeline weakens roughly 5-10 years later.
```

> **Add to ## Evidence from practice:**
```
- Stanford Digital Economy Lab (June 2026): 25,000-firm study; AI-exposed early-career (22-25) jobs declining 3.8%/yr since 2022; least-exposed jobs growing 2.0%; junior software devs and customer service hardest hit
```

> **Add to ## Sources:**
```
- [Stanford AI labor market data — June 2026](../sources/newsletters/stanford-labor-june-2026.md)
```

### wiki/trends/agents-reshape-organizations.md (updated section)

> **Frontmatter: update `as_of` to 2026-06-16; add `stanford-labor-june-2026` to sources.**

> **Concrete signals — add new bullet:**

> **After the McKinsey bullet:**
```
- **First rigorous labor-market data on junior displacement.** Stanford's Digital Economy Lab (25,000 firms): early-career workers aged 22-25 in AI-exposed occupations declining 3.8%/yr since 2022; least-exposed roles growing 2.0%. Junior software developers and customer service hardest hit. The concern is not mass unemployment but a "hollow pipeline" — if entry-level roles disappear, the supply of senior talent weakens 5-10 years later (Stanford AI Economic Indicators, June 2026).
```

> **Add to ## Recent changes (prepend):**
```
- [2026-06-16] Stanford 25,000-firm study: AI-exposed early-career workers declining 3.8%/yr since 2022; junior software devs hardest hit; hollow pipeline concern is now data-backed
```

> **Add to ## Sources:**
```
- [Stanford AI labor market data — June 2026](../sources/newsletters/stanford-labor-june-2026.md)
```

### wiki/sources/newsletters/stanford-labor-june-2026.md (new)

````md
---
title: Stanford AI Economic Indicators — junior worker displacement (June 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-16-76-security-experts-say-free-fable.md
published: 2026-06-16
ingested: 2026-06-17
domains: []
---

# Stanford AI Economic Indicators — junior worker displacement (June 2026)

Stanford's Digital Economy Lab labor market analysis covering AI's impact on early-career workers.

## Influenced pages

- [AI enablement — software development](../../training/ai-enablement-software-development.md) — junior talent problem section
- [Agents reshape organizations](../../trends/agents-reshape-organizations.md) — concrete signals section

## Key claims extracted

- Dataset: 25,000 firms; Stanford Digital Economy Lab
- Overall hiring unchanged since ChatGPT launch (2022)
- Early-career (22-25) in AI-exposed roles: declining 3.8%/yr
- Least AI-exposed roles: growing 2.0%
- Hardest hit: junior software developers, customer service workers
- Least affected: low-exposure roles (home health aides etc.)
- Stanford labels these "early signals from a fixed sample" — not definitive global figures
- Hollow pipeline concern: entry-level disappearing → senior pipeline weakens 5-10 years later
````
