---
type: proposal
source: raw/articles/2026-09-10-openaicom-indexintroducing-chatgpt-finan.md
status: pending
created: 2026-11-24
---

# Proposal: What ChatGPT for Financial Services contains

## Summary

### In short
OpenAI's finance product competes on data access rather than on the model: it ships premium financial datasets that OpenAI itself indexes and hosts, with citations down to the figure, plus tuned finance connectors, firm templates and information barriers between workspaces. State of Finance currently lists the product only through a conference keynote and a prediction, without saying what it contains. The proposal rewrites that one leader line to describe the product and adds a dated Recent-changes entry and one source page. No red flags; the only trim is that the line is near its length limit, so one in-progress feature stays on the source page.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 10 September 2026 OpenAI launched ChatGPT for Financial Services, a tailored edition of ChatGPT Work for financial institutions, starting with investment banking and equity research. Datasets from Daloopa, PitchBook, LSEG News and Crunchbase come built in, with no separate contracts or connectors to set up. OpenAI indexes and hosts them itself, which it says improves retrieval and lets a banker trace any figure or claim back to the specific table or passage it came from.

For data a firm already pays for, OpenAI says it is working with S&P Capital IQ, LSEG, MSCI, Dow Jones Factiva and Moody's on shared sign-in, so providers can recognise a user's ChatGPT login and grant the access they are already entitled to. The most-used finance MCP connectors (MCP is the standard protocol for plugging tools into an agent) have been tuned to work out of the box, and more than 50 others are available, including FactSet, Preqin and Datasite. Administrators can publish Excel, Word and PowerPoint templates in the firm's format, and can create separate workspaces to enforce information barriers, the walls banks keep between teams holding material non-public information.

### What changes
Today **State of Finance** lists ChatGPT for Financial Services under Finance AI with one line from the October AI Engineer keynote: source traceability in review and a 2027 trading prediction.

- **State of Finance** has that leader line rewritten to name what the product contains: OpenAI-hosted data with figure-level citations, tuned connectors, firm templates and information-barrier workspaces. The prediction stays, and so does the line's 14 October date, because the keynote is newer than the launch post. A Recent-changes entry dated 10 September records the launch, bringing the list to its cap of ten with no spill. Page date stays at 23 November.
- One new source page for the launch post.

### What to weigh
The line stays under the 400-character limit for State of Finance leader lines only by leaving out the shared sign-in with existing data subscriptions. OpenAI describes that sign-in as work in progress, so it is recorded on the source page rather than claimed as shipped. The design partners (Morgan Stanley, Evercore) and the GPT-6 Astra benchmark figures are left out as launch-time detail, since GPT-6.2 Astra has since replaced that model.

## Intended changes

- [ ] **Update** `wiki/state-of/finance.md` — rewrite the ChatGPT for Financial Services leader line (keeps its 2026-10-14 stamp); adds one Recent-changes entry dated 2026-09-10 (list goes to 10 of 10, no spill); append `openai-chatgpt-financial-services-2026-09-10` to frontmatter `sources:` and one line to `## Sources`; `as_of` stays 2026-11-23
    > **Before:** `- **ChatGPT for Financial Services** — OpenAI; builds source traceability (where each number came from) into review; OpenAI's Joseph Kim predicts agents will do investment idea generation and trading in 2027 *(as of 2026-10-14)*`
    > **After:** see draft below

- [ ] **Create** `wiki/sources/articles/openai-chatgpt-financial-services-2026-09-10.md` — source summary

## Page drafts

### wiki/state-of/finance.md (updated)

Frontmatter `sources:` appends `openai-chatgpt-financial-services-2026-09-10`; `as_of` unchanged (2026-11-23).

In `### Finance AI`, the ChatGPT for Financial Services line is replaced (362 characters):

```
- **ChatGPT for Financial Services** — OpenAI; ChatGPT Work edition for banking and equity research: OpenAI-hosted data (Daloopa, PitchBook, LSEG News, Crunchbase) with figure-level citations, tuned finance connectors, firm templates, information-barrier workspaces; OpenAI's Joseph Kim predicts agent-run idea generation and trading in 2027 *(as of 2026-10-14)*
```

In `## Recent changes`, insert directly below the 2026-10-14 entry (date order):

```
- [2026-09-10] ChatGPT for Financial Services launched: OpenAI-hosted premium data (Daloopa, PitchBook, LSEG News, Crunchbase) with figure-level citations, tuned finance MCP connectors plus 50+ others, admin-published Office templates and information-barrier workspaces; shared sign-in to existing data subscriptions in progress.
```

In `## Sources`, append:

```
- [OpenAI — Introducing ChatGPT for Financial Services](../sources/articles/openai-chatgpt-financial-services-2026-09-10.md)
```

### wiki/sources/articles/openai-chatgpt-financial-services-2026-09-10.md (new)

```
---
title: OpenAI — Introducing ChatGPT for Financial Services
type: source
source_type: article
source_file: raw/articles/2026-09-10-openaicom-indexintroducing-chatgpt-finan.md
url: https://openai.com/index/introducing-chatgpt-financial-services/
published: 2026-09-10
ingested: 2026-11-24
domains: [finance]
---

# OpenAI — Introducing ChatGPT for Financial Services

OpenAI's launch post for a ChatGPT Work edition for financial institutions, starting with investment banking and equity research. It leads with data access: premium datasets OpenAI indexes and hosts, sign-in to data a firm already licenses, and tuned finance connectors, plus firm templates and governance controls for material non-public information.

## Influenced pages
- [State of Finance](../../state-of/finance.md) — ChatGPT for Financial Services leader line rewritten to describe the product's contents

## Key claims extracted
- Built-in datasets from Daloopa, PitchBook, LSEG News and Crunchbase (earnings transcripts, financial statements, fundamentals, private companies); no separate contracts or connector setup
- OpenAI indexes and hosts the data, enabling citations that trace figures and claims to specific tables and passages
- OpenAI is working with S&P Capital IQ, LSEG, MSCI, Dow Jones Factiva and Moody's on shared sign-in and entitlement integrations so users get data they already license (in progress at launch)
- The most-used finance MCP connectors are optimized for immediate use; 50+ connectors in total, including Datasite, Box, Preqin, FactSet and Intapp
- Admins publish Excel, Word and PowerPoint templates through an admin page
- Builds on ChatGPT Enterprise SSO, SCIM and role-based access; supported app read/write actions can be enabled per role; multiple workspaces enforce information barriers; logs export through the OpenAI Compliance Platform
- Available to eligible financial institutions through sales; design partners Morgan Stanley and Evercore
- Launched on GPT-6 Astra (69.9% on OfficeQA Pro per OpenAI), since replaced by GPT-6.2 Astra
```

## Schema / vocabulary additions

None.

## Open questions

None.
