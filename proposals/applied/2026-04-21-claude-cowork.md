---
type: proposal
sources:
  - raw/articles/2026-04-21-anthropiccom-product-claude-cowork.md
  - raw/tweets/2026-04-20-xcom-claudeaistatus2046328619249684-1.md
  - raw/tweets/2026-04-21-aakashgupta-2046331327780356219.md
  - raw/newsletters/2026-04-21-gemini-wants-to-catch-claude.md
status: pending
created: 2026-04-21
---

# Proposal: Claude Cowork — Live Artifacts

## Summary

Anthropic shipped Live Artifacts in Claude Cowork: dashboards and trackers wired to connectors (Slack, Salesforce, Google Drive, Asana, Jira) that auto-refresh on open. Included in Claude Pro ($20/month). Analyst Aakash Gupta frames this as a direct competitive pressure on Tableau, Looker, and Retool — all of which priced on the assumption that live dashboards are hard to build.

## Intended changes

- [x] **Create** `wiki/tools/claude-cowork.md` — new tool page
    > See draft below

- [x] **Create** `wiki/sources/articles/claude-cowork-launch.md` — source summary
    > See draft below

- [x] **Create** `wiki/sources/tweets/aakash-gupta-cowork.md` — source summary
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add `Knowledge-work agents` subcategory with Cowork; bump `as_of`
    > **Frontmatter:** `as_of: 2026-04-21`, add `claude-cowork-launch` to `sources:`
    >
    > **Add new subcategory section before `## Recent changes`:**
    > ```
    > ### Knowledge-work agents
    >
    > Desktop-first agents that connect to workplace apps and complete multi-step knowledge work without step-by-step user direction.
    >
    > - [[tools/claude-cowork]] — Anthropic; desktop agent with Live Artifacts — auto-refreshing dashboards from Slack, Salesforce, Drive, Asana, Jira connectors; included in Claude Pro ($20/mo) *(as of 2026-04-21)*
    > ```
    >
    > **Add to `## Recent changes` (prepend):**
    > ```
    > - [2026-04-21] Added [[tools/claude-cowork]] under new `Knowledge-work agents` subcategory; Live Artifacts ships
    > ```

- [x] **Update** `wiki/index.md` — add `[[tools/claude-cowork]]` under Tools; update page count
    > **Add under `## Tools`:**
    > ```
    > - [[tools/claude-cowork]] — Anthropic's desktop knowledge-work agent; Live Artifacts auto-refresh dashboards from Slack, Salesforce, Drive, Asana, Jira connectors *(as_of: 2026-04-21)*
    > ```

## Schema / vocabulary additions

- [x] **Add subcategory `knowledge-work-agent`** to `wiki/_schema/subcategories.md`
    > ```
    > ### knowledge-work-agent
    > - **Parent domain(s):** agents
    > - **Applies to types:** tool
    > - **Definition:** Desktop-first or ambient agents that connect to workplace apps and complete multi-step knowledge work (research, synthesis, dashboards, reports) without step-by-step user coordination.
    > - **Examples:** [[tools/claude-cowork]]
    > ```

## Page drafts

### wiki/tools/claude-cowork.md (new)

````md
---
title: Claude Cowork
type: tool
domains: [agents]
subcategory: knowledge-work-agent
tags: [anthropic, agentic]
as_of: 2026-04-21
sources: [claude-cowork-launch, aakash-gupta-cowork]
---

# Claude Cowork

Anthropic's desktop agent for knowledge work. Runs locally, moves between files, folders, and applications to complete multi-step tasks without step-by-step user direction. Included in Claude Pro ($20/month).

## Current status (as of 2026-04-21)

- Desktop app; works with local files and connected workplace apps
- **Live Artifacts** (shipped April 2026): dashboards, trackers, and reports wired to app connectors that auto-refresh on open
- Supported connectors: Slack, Salesforce, Google Drive, Asana, Jira
- Included in Claude Pro ($20/month) — no additional charge

## Competitive context

Analyst Aakash Gupta frames Live Artifacts as competitive pressure on:
- **Tableau** ($75–115/seat/month) — Cowork writes and wires a live visualization in one prompt
- **Looker** ($30K+ enterprise floor) — same capability now part of a $20 subscription
- **Retool** ($3.2B valuation, $120M ARR) — internal tools that required a Retool license, a data engineer, and two sprints can now be a chat message

The key inversion: Tableau/Looker/Retool priced on dashboards being scarce and creators being rare. Live Artifacts makes every employee a dashboard creator.

## Recent changes

- [2026-04-21] Live Artifacts shipped — auto-refreshing dashboards from connected apps

## Sources

- [[sources/articles/claude-cowork-launch]]
- [[sources/tweets/aakash-gupta-cowork]]
````

### wiki/sources/articles/claude-cowork-launch.md (new)

````md
---
title: Claude Cowork — Anthropic product page
type: source
source_type: article
source_file: raw/articles/2026-04-21-anthropiccom-product-claude-cowork.md
url: https://www.anthropic.com/product/claude-cowork
published: 2026-04-21
ingested: 2026-04-21
domains: [agents]
---

# Claude Cowork — Anthropic product page

Anthropic's official product page for Claude Cowork. Describes a desktop-first knowledge-work agent that handles high-effort, repeatable tasks by moving between local files, folders, and applications without the user coordinating each step.

## Key claims extracted

- "Takes the outcome and handles the rest" — no per-step prompting required
- Best for high-effort repeatable tasks; no technical background required
- Runs on desktop where most knowledge work happens

## Influenced pages

- [[tools/claude-cowork]] — new tool page
- [[state-of/agents]] — new Knowledge-work agents subcategory
````

### wiki/sources/tweets/aakash-gupta-cowork.md (new)

````md
---
title: Aakash Gupta — Claude Cowork as BI stack threat
type: source
source_type: tweet
source_file: raw/tweets/2026-04-21-aakashgupta-2046331327780356219.md
url: https://x.com/aakashgupta/status/2046331327780356219
published: 2026-04-21
ingested: 2026-04-21
domains: [agents]
---

# Aakash Gupta — Claude Cowork as BI stack threat

Competitive analysis framing Cowork's Live Artifacts as a structural threat to Tableau ($75–115/seat), Looker ($30K+ floor), and Retool ($3.2B valuation, $120M ARR). Core argument: these products priced on dashboards being scarce; Cowork inverts the scarcity assumption.

## Key claims extracted

- Tableau, Looker, Retool all priced on "dashboard creator is rare" — Cowork makes every employee a creator
- "Every internal tools team at every mid-sized company exists because 'live pipeline metrics view' used to require a Retool license, a data engineer, and two sprints"
- Cowork connectors: Slack, Salesforce, Drive, Asana, Jira — matches Tableau/Retool connector coverage
- "Cowork isn't the BI category killer yet. But it's coming for the seat count."

## Influenced pages

- [[tools/claude-cowork]] — competitive context section
````

## Comments

-  we don't need a knowledge work agent vocabulary
-  Claude Cowork is far more than the artifacts so when you add it to the index, don't focus its description on that
-  let's give it less importance to Gupta's opinion and just mention that it did put competitive pressure on dashboards and those kinds of tools 