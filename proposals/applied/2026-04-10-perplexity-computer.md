---
type: proposal
source: raw/newsletters/2026-04-10-superhumanai-p-agents-for-your-personal-life-are-here.md
status: pending
created: 2026-04-10
---

# Proposal: Perplexity Computer — financial integrations via Plaid

## Summary
Perplexity's "Computer" feature now connects with 12,000+ financial institutions through Plaid, letting users link accounts into a customizable hub and ask questions about their finances or build custom budgeting/tracking tools. This is an early signal of agentic computer-use applied to personal finance.

## Intended changes

- [x] **Create** `wiki/tools/perplexity.md` — new tool page for Perplexity, focused on the Computer feature
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add entry under a new "Agentic computer use" subcategory section
    > **Add after the "Agentic DevOps" section:**
    > ```
    > ### Agentic computer use
    >
    > Agents that act through real application UIs or integrate with third-party services on behalf of the user, going beyond API tool-calling to interact with systems as a human would.
    >
    > - [[tools/perplexity]] — Perplexity Computer connects to 12,000+ financial institutions via Plaid; users can query finances and build custom tools inside chat *(as of 2026-04-10)*
    > ```

- [x] **Update** `wiki/state-of/agents.md` — add recent-change entry
    > **Append to Recent changes:**
    > `- [2026-04-10] Added `agentic-computer-use` subcategory with [[tools/perplexity]] after triaging Superhuman AI newsletter`

- [x] **Create** `wiki/sources/articles/perplexity-computer-plaid.md` — source summary (sourced from newsletter blurb, not a dedicated article)

- [x] **Update** `wiki/index.md` — add entries for `tools/perplexity` and update page count

## Page drafts

### wiki/tools/perplexity.md (new)

```
---
title: Perplexity
type: tool
domains: [agents]
subcategory: agentic-computer-use
tags: [closed-source]
as_of: 2026-04-10
sources: [perplexity-computer-plaid]
---

# Perplexity

AI-powered answer engine with a growing agentic layer. The "Computer" feature lets users delegate tasks that require interacting with real services beyond simple Q&A.

## Current status (as of 2026-04-10)

- Computer feature connects to 12,000+ financial institutions through Plaid
- Users can link accounts, ask questions about finances, and build custom budgeting/tracking/debt tools
- Positioning as a personal finance hub inside an AI chat interface

## Strengths

- Deep third-party integrations (Plaid covers most US financial institutions)
- Combines natural-language queries with real account data

## Weaknesses / caveats

- Only one feature (finance/Plaid) documented here; broader Computer capabilities not yet covered
- Source is a newsletter blurb — thin detail on architecture, pricing, or limitations

## Recent changes

- [2026-04-10] Computer feature connects to 12,000+ financial institutions via Plaid (sourced from Superhuman AI newsletter)

## Sources

- [[sources/articles/perplexity-computer-plaid]]
```

### wiki/sources/articles/perplexity-computer-plaid.md (new)

```
---
title: Perplexity Computer — Plaid financial integrations
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-10-superhumanai-p-agents-for-your-personal-life-are-here.md
url: https://www.superhuman.ai/p/agents-for-your-personal-life-are-here
published: 2026-04-10
ingested: 2026-04-10
domains: [agents]
---

# Perplexity Computer — Plaid financial integrations

Perplexity's Computer feature now connects with 12,000+ financial institutions through Plaid, letting users link all accounts into a single customizable hub. Users can ask questions about their finances and build custom tools for budgeting, spending, or tracking debt/investments. The announcement reportedly attracted 2M+ views.

## Influenced pages

- [[tools/perplexity]] — new page created
- [[state-of/agents]] — added agentic-computer-use subcategory

## Key claims extracted

- Computer connects to 12,000+ financial institutions through Plaid
- Users can link accounts, query finances, build custom budgeting/tracking tools
- Announcement had 2M+ views
```

## Schema / vocabulary additions

- [x] Add new subcategory `agentic-computer-use` to `wiki/_schema/subcategories.md`:
    ```
    ### agentic-computer-use
    - **Parent domain(s):** agents
    - **Applies to types:** tool
    - **Definition:** Agents that act through real application UIs or integrate with third-party services on behalf of the user, going beyond API tool-calling to interact with systems as a human would.
    - **Examples:** [[tools/perplexity]]
    ```

## Open questions

- Perplexity is a broad product (search, answer engine, etc.). Should this page cover the whole product, or stay narrowly focused on the "Computer" agentic feature? I've kept it narrow since that's all the source covers.
	- Perplexity computer should be a tool in itself, separate from Perplexity, which has more services. Please do a web search on Plexi the computer to improve the content around this tool.
- Should we add a `perplexity` vendor tag? Only one page so far, so probably premature.
	-  please add it 

## Comments

- You are categorizing this as "State of Agents," but I think we should have a separate category for "State of Computer Use" because that is an important subcategory of agents that we need to separate

- I feel like something like the Perplexity plate stuff should open a new state of finances financial page where we can delve into the topics of financial

- We can rename the tag "agentic computer use" as just "computer use" 