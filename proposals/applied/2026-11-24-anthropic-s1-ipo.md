---
type: proposal
source: raw/newsletters/2026-10-26-is-anthropic-worth-2-trillion.md
sources:
  - raw/newsletters/2026-10-26-is-anthropic-worth-2-trillion.md
  - raw/newsletters/2026-10-28-every-model-has-a-six-month-shelf-life-now.md
  - raw/newsletters/2026-11-19-what-we-let-our-agents-buy.md
  - raw/articles/2026-11-24-anthropiccom-news-s1-sec.md
  - raw/articles/2026-11-24-anthropiccom-news-ipo-close.md
status: pending
created: 2026-11-24
---

# Proposal: Anthropic's S-1 and IPO

## Summary

### In short
Anthropic's S-1 shows a frontier lab whose revenue depends on its newest models while its compute bills are fixed for years: models older than six months earn under 20% of revenue, yet compute contracts rise to about $155B a year by 2028, mostly non-cancelable. The proposal adds one subsection with the filing's key numbers and the IPO outcome to **Compute infrastructure**, plus five source pages. The reason to hesitate is a partial source: the S-1 itself could not be read, so the financial figures come from Every's partly paywalled analysis of it.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Anthropic filed its S-1, the registration statement that precedes an IPO, on 26 October 2026. It listed on Nasdaq as "ANT" on 19 November at $83 a share, opened at $111.50 (about a $2 trillion market cap, per Every), and closed the offering on 20 November with about $91.6B to the company. Seven compute and chip suppliers, NVIDIA among them, bought another $26B of shares at the IPO price.

Evan Armstrong's same-day analysis for Every is the main reading of the filing. Revenue went from $376M in Q1 2025 to $11.6B in Q2 2026. About 1,500 organizations paying $100K or more a year made up 76% of 2025 revenue, and Claude Code is the engine: Enterprise users who use it spend about $1,500 a month, others under $75. Reported gross margin is 85%, or about 45% once all compute counts as cost. Armstrong's frame is the movie studio: models older than six months earn under 20% of revenue, while compute contracts climb to $155B a year by 2028, mostly non-cancelable. Every's 28 October follow-up adds Steve Yegge's "discernment horizon": if users stop being able to tell models apart, the upgrade cycle that pays for those contracts slows.

### What changes
**Compute infrastructure** covers lab economics only through leaked OpenAI figures from June and older Anthropic compute deals. This proposal adds the S-1 numbers there.

- **Compute infrastructure** gains a subsection titled "Anthropic's S-1: the first audited frontier-lab accounts" under Lab and subscription economics, one Current-status bullet, and one Recent-changes entry. The list is at its cap of 10, so the oldest entry (Superhuman's Q1 Big Tech earnings note) moves to history. The page date moves to 20 November.
- Five new source pages: Armstrong's analysis, the six-month shelf-life recap, Every's IPO-day note, and Anthropic's S-1 filing and IPO-close announcements.

### What to weigh
The S-1 itself was not read. EDGAR blocked the automated fetch, and the browser showed only the cover page. Every's article is paywalled after "The case for $2 trillion," so the figures come from the part of Armstrong's article that could be read. Q3's $16.8B comes from press reports, not from audited numbers. Every said the IPO raised $81B, while Anthropic's close announcement gives $91.6B to the company once the underwriters' extra shares are included. The draft uses Anthropic's figure. To keep the page under the 110% split line (about 1,318 of 1,320 allowed body words), the draft leaves out some filing details. Those details stay on the source page.

## Intended changes

- [ ] **Update** `wiki/trends/compute-infrastructure.md` — add one Current-status bullet; add the subsection "Anthropic's S-1: the first audited frontier-lab accounts" under `## Lab and subscription economics` and adjust that section's intro line; add one Recent-changes entry dated 2026-11-20; append five source ids to `sources:` and five links to `## Sources`; `as_of` and the Current-status stamp move to 2026-11-20
    > See draft below

- [ ] **Spill** `wiki/trends/compute-infrastructure.md` → `wiki/history/trends/compute-infrastructure.md` — the Recent-changes list is at its cap of 10; the oldest entry (2026-05-05, Superhuman Q1 Big Tech earnings) moves to history under a new archive header
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-anthropic-s1-2-trillion-2026-10-26.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-six-month-shelf-life-2026-10-28.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-anthropic-ipo-opens-2026-11-19.md` — source summary (story-specific page for this newsletter's IPO item)

- [ ] **Create** `wiki/sources/articles/anthropic-s1-filing-2026-10-26.md` — source summary

- [ ] **Create** `wiki/sources/articles/anthropic-ipo-close-2026-11-20.md` — source summary

## Page drafts

### wiki/trends/compute-infrastructure.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-11-20
sources: [ainews-2026-04-21, runtime-improvements-improve-agent-economics, google-cloud-next-2026, ainews-2026-04-25, ai-earnings-capex-2026-04-30, inference-inflection-agent-runtime-2026-04-30, parallel-web-agent-apis-2026-04-30, persistent-cloud-computers-agents-2026-05-01, stripe-agent-native-commerce-fraud-2026-04-29, ainews-not-much-happened-2026-07-02, local-ai-infrastructure-2026-06, outputmaxxing-amp-compute-utilization-2026-06, railway-agent-native-cloud-2026-05-20, daytona-giving-agents-computers-2026-05-21, modal-agent-experience-2026-07-08, ainews-new-ai-infra-unicorns-2026-05-22, amd-acquires-taalas-2026-08-07, ainews-memory-prices-openai-pause-2026-08-19, openai-economics-june-2026, every-anthropic-s1-2-trillion-2026-10-26, every-six-month-shelf-life-2026-10-28, every-anthropic-ipo-opens-2026-11-19, anthropic-s1-filing-2026-10-26, anthropic-ipo-close-2026-11-20]
```

Current status heading and new bullet (appended as the last bullet of the section):

```
## Current status (as of 2026-11-20)

- Anthropic's S-1 (2026-10-26) gives the first audited frontier-lab accounts: compute contracts reach about $155B a year by 2028 (see Lab and subscription economics).
```

`## Lab and subscription economics` — intro line changed, existing June bullets unchanged, new subsection appended after them:

```
## Lab and subscription economics

The economics behind frontier model access, from June 2026 leaks and estimates to Anthropic's S-1:

<existing four June 2026 bullets unchanged>

### Anthropic's S-1: the first audited frontier-lab accounts

Anthropic filed its S-1 on 2026-10-26, listed on Nasdaq as ANT on 2026-11-19 at $83 a share (about a $2T market cap at the open), and closed the offering on 2026-11-20 with about $91.6B to the company, plus $26B from seven compute and chip suppliers, NVIDIA among them, in a private placement. The filing, as read by Evan Armstrong for Every:

- **Growth:** revenue rose from $376M in Q1 2025 to $11.6B in Q2 2026, with Q3 reported around $16.8B.
- **Six-month shelf life:** models older than six months earn under 20% of revenue, and Anthropic says each release cuts customers' cost per task 25–45%.
- **Who pays:** 76% of 2025 revenue came from about 1,500 organizations paying $100K+ a year, and the top five's share fell from 36% to 21% during 2026. Claude Code users spend about $1,500 a month against under $75 for non-users. 5–7% of revenue came from usage-policy violators, mostly labs distilling Claude, cut off in August and September.
- **Margins:** 85% reported gross margin, about 45% if all compute counts as cost; H1 2026 operating loss $693M.
- **Compute against cash:** compute runs about $22B a year, contracted to about $120B next year and $155B by 2028, mostly non-cancelable; $131.7B in cash and short-term investments at 2026-06-30.

The named risk is Steve Yegge's "discernment horizon" (cited by Every's Mike Taylor): if most users' tasks are too easy to tell models apart, the upgrades that pay for fixed compute slow.
```

`## Recent changes` — adds one entry at the top; the 2026-05-05 Superhuman entry is removed (spilled):

```
- [2026-11-20] Added Anthropic's S-1 and IPO under Lab and subscription economics: revenue and customer concentration, six-month model shelf life, 85% reported vs ~45% all-in gross margin, compute contracts rising to ~$155B/yr by 2028 against $131.7B cash; IPO closed with ~$91.6B to Anthropic plus $26B from seven compute suppliers.
```

`## Sources` — five links appended:

```
- [Every — Is Anthropic Worth $2 Trillion? (Evan Armstrong)](../sources/newsletters/every-anthropic-s1-2-trillion-2026-10-26.md)
- [Every — Every Model Has a Six-month Shelf Life Now](../sources/newsletters/every-six-month-shelf-life-2026-10-28.md)
- [Every — Anthropic's IPO opens at a $2T market cap](../sources/newsletters/every-anthropic-ipo-opens-2026-11-19.md)
- [Anthropic files S-1 with the SEC](../sources/articles/anthropic-s1-filing-2026-10-26.md)
- [Anthropic announces closing of its IPO](../sources/articles/anthropic-ipo-close-2026-11-20.md)
```

### wiki/history/trends/compute-infrastructure.md (updated, spill)

Appended at the end of the file:

```
## Archived from current page on <apply date>

- [2026-05-05] Superhuman reports Q1 2026 Big Tech earnings (Alphabet, Amazon, Meta, Microsoft) show AI revenue materializing while capex continues climbing; treat directional signal as confirmed, specific figures as pending primary verification
```

### wiki/sources/newsletters/every-anthropic-s1-2-trillion-2026-10-26.md (new)

```
---
title: Every — Is Anthropic Worth $2 Trillion? (Evan Armstrong)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-26-is-anthropic-worth-2-trillion.md
url: https://every.to/napkin-math/is-anthropic-worth-2-trillion
published: 2026-10-26
ingested: 2026-11-24
domains: [models]
---

# Every — Is Anthropic Worth $2 Trillion? (Evan Armstrong)

Evan Armstrong's same-day reading of Anthropic's S-1. He argues the filing shows the fastest scaling in the industry's history but a business that only works if each new model keeps outselling the last, because models behave like movies: they earn most of their revenue in the first six months. The article is paywalled after the section "The case for $2 trillion"; only the part before it was read.

## Influenced pages
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — S-1 subsection under Lab and subscription economics

## Key claims extracted
- Revenue: $376M in Q1 2025, $11.6B in Q2 2026, Q3 around $16.8B (press-reported)
- About 900% net revenue retention for "qualified customers" (excludes Pro and Max)
- Models older than six months earn under 20% of revenue; releases in the six months to 2026-09-30 produced over 80% of Q3 revenue
- 76% of 2025 revenue from about 1,500 organizations paying $100K+ a year; 11,900 customers above $100K, up eightfold in nine months; top five customers fell from 36% (Q1) to 21% (Q3) of revenue
- Claude Enterprise users who use Claude Code spend about $1,500/month; non-users under $75
- 5–7% of revenue came from usage-policy violators, mostly labs distilling Claude, cut off in August and September
- 85% reported gross margin; about 45% counting all compute ($8.9B cost of goods in H1)
- H1 2026 operating loss $693M; the $80.7B net loss is driven by $72.4B of mark-to-market losses on Amazon convertible notes
- Compute about $22B/year (Q2 annualized), contracted to about $120B next year and $155B by 2028, mostly non-cancelable; revenue grew 1,368% this year against 300% compute growth
- $141.1B raised since 2021; $131.7B in cash and short-term investments at 2026-06-30; revenue per employee $6.6M trailing
```

### wiki/sources/newsletters/every-six-month-shelf-life-2026-10-28.md (new)

```
---
title: Every — Every Model Has a Six-month Shelf Life Now
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-28-every-model-has-a-six-month-shelf-life-now.md
url: https://every.to/context-window/every-model-has-a-six-month-shelf-life-now
published: 2026-10-28
ingested: 2026-11-24
domains: [models]
---

# Every — Every Model Has a Six-month Shelf Life Now

Every's Context Window recap of Anthropic's S-1. It centres on the filing's dependence on new models and the risk that users stop noticing the difference between them.

## Influenced pages
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — six-month shelf life, discernment-horizon risk

## Key claims extracted
- Models older than six months earn less than 20% of Anthropic's revenue
- Anthropic earned $16.3B in H1 2026, before Opus 5.5 and Fable 5.1 shipped
- Anthropic says its latest releases cut customers' cost per task 25–45%
- Mike Taylor cites Steve Yegge's "discernment horizon": most users' tasks are not hard enough to show the difference between models
- Dan Shipper's "inchworm" model: engineers adopt first, knowledge workers follow, the rest of the economy last
```

### wiki/sources/newsletters/every-anthropic-ipo-opens-2026-11-19.md (new)

```
---
title: Every — Anthropic's IPO opens at a $2T market cap
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-19-what-we-let-our-agents-buy.md
published: 2026-11-19
ingested: 2026-11-24
domains: [models]
---

# Every — Anthropic's IPO opens at a $2T market cap

A news item in Every's 2026-11-19 Context Window ("What We Let Our Agents Buy") on Anthropic's first day of trading.

## Influenced pages
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — opening price and market cap

## Key claims extracted
- Anthropic opened at $111.50 a share, about a $2 trillion market cap
- First frontier AI lab to go public; Every reports $81B raised and calls it the largest IPO on record, ahead of SpaceX
- Now the largest public benefit corporation
```

### wiki/sources/articles/anthropic-s1-filing-2026-10-26.md (new)

```
---
title: Anthropic files S-1 with the SEC for proposed initial public offering
type: source
source_type: article
source_file: raw/articles/2026-11-24-anthropiccom-news-s1-sec.md
url: https://www.anthropic.com/news/s1-sec
published: 2026-10-26
ingested: 2026-11-24
domains: [models]
---

# Anthropic files S-1 with the SEC for proposed initial public offering

Anthropic's announcement that it filed a Form S-1 registration statement for an IPO of its Class A common stock. It gives no financial figures; those are in the S-1 itself (SEC EDGAR, not read for this ingest).

## Influenced pages
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — filing date

## Key claims extracted
- Anthropic, PBC filed its S-1 with the SEC on 2026-10-26
- Planned listing on the Nasdaq Global Select Market under the symbol "ANT"
- Goldman Sachs and Morgan Stanley lead the offering
```

### wiki/sources/articles/anthropic-ipo-close-2026-11-20.md (new)

```
---
title: Anthropic announces closing of initial public offering and concurrent private placement
type: source
source_type: article
source_file: raw/articles/2026-11-24-anthropiccom-news-ipo-close.md
url: https://www.anthropic.com/news/ipo-close
published: 2026-11-20
ingested: 2026-11-24
domains: [models]
---

# Anthropic announces closing of initial public offering and concurrent private placement

Anthropic's announcement that its IPO closed, including the underwriters' full option, alongside a private sale of shares to seven compute and chip suppliers.

## Influenced pages
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — IPO outcome and supplier private placement

## Key claims extracted
- 1,127,000,000 Class A shares sold at $83.00, including the underwriters' full 147,000,000-share option
- Gross proceeds about $93.5B, of which about $91.6B went to Anthropic (the rest to selling stockholders)
- Trading began on Nasdaq on 2026-11-19 under "ANT"; registration declared effective 2026-11-18
- Concurrent private placement of 313,253,007 Class N shares at $83.00 (about $26.0B) to AMD, Broadcom, Google, Micron, Microsoft, NVIDIA and TSMC
- Combined gross proceeds about $119.5B
```

## Schema / vocabulary additions

None.

## Open questions

- Lab and subscription economics now holds two unrelated bodies of evidence (June OpenAI/subscription figures and Anthropic's S-1). Should it become its own trend page (for example `trends/frontier-lab-economics.md`) once a second filing or earnings report arrives, or now? Assumed: keep it on this page for now.
	- Same page, its an evolving topic
