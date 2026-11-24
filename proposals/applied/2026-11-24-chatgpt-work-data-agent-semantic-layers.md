---
type: proposal
source: raw/articles/2026-09-10-openaicom-index-put-data-to-work.md
sources:
  - raw/articles/2026-09-10-openaicom-index-put-data-to-work.md
  - raw/tweets/2026-09-10-xcom-chatgptstatus20980652969680118.md
  - raw/newsletters/2026-09-12-ainews-deepseek-v41-flash-763b-p8b-d16b-novel.md
status: pending
created: 2026-11-24
---

# Proposal: ChatGPT Work Data agent — warehouse analytics grounded in semantic layers

## Summary

### In short
A mainstream assistant now treats the semantic layer as the place to get business definitions before it queries company data: OpenAI's Data agent in ChatGPT Work reads metric definitions from dbt, Snowflake Horizon, Databricks Genie Ontology and BI dashboards, and enforces each user's table, row and column permissions. OpenAI says nearly all of its product team analyses data this way. The proposal updates **Semantic layer**, **Codex** (home of ChatGPT Work), **AI adoption evidence** and the **Knowledge term map**, and creates one source page. The reason to hesitate is reach: four pages and two history spills for one launch.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 10 September 2026 OpenAI introduced the Data agent in ChatGPT Work, installed from the Plugins directory as "Data" and called with `@Data` in a conversation. The announcement tweet drew 3.7 million views, and AINews read it as enterprise data access becoming a first-class product feature. The agent connects to approved sources, including Amazon Redshift, BigQuery, Snowflake, Databricks, ClickHouse, MongoDB and Datadog, and can bring in files from Google Drive and SharePoint.

The detail that matters most for this wiki is how it interprets the data. OpenAI says the agent uses the organisation's business terms, metric definitions, custom calculations and data relationships, taken from semantic layers and trusted sources: Databricks Genie Ontology, dbt, GitHub, Snowflake Horizon and existing BI dashboards. Administrators choose which connections and roles are allowed, and every query runs under the connected account's existing permissions down to table, row and column. Users can ask follow-up questions, review the evidence behind each finding, and turn the analysis into an interactive dashboard their team can edit, share and refresh. The agent also builds dashboards inside Tableau, Power BI, Sigma, ThoughtSpot, Omni and Oracle BI, and after the user approves it can share findings over Slack or email and act through connected tools.

OpenAI says it uses the same capabilities internally: nearly all of its product team and over two-thirds of its go-to-market organisation analyse company data themselves this way. Its data team made that possible by writing shared business definitions, setting access rules and adding safeguards for sensitive data. NTT DATA, an alpha customer, says non-engineers in sales and corporate functions now build and update their own dashboards.

### What changes
The Semantic layer page describes only PostHog's own implementation, with no outside product that reads from a layer. The Codex page covers ChatGPT Work's architecture and Plugin Directory but no Data plugin.

- **Semantic layer** gains a Current-status bullet naming the Data agent as a mainstream consumer of semantic layers, with permission enforcement, and lists "Genie Ontology" under Also called. Page date moves from 21 August to 10 September.
- **Codex** gains a Data agent bullet in its ChatGPT Work section and a Recent-changes entry; the oldest entry (14 July) moves to history because the list is at its cap.
- **AI adoption evidence** gains OpenAI's internal self-serve analytics case and its prerequisites. Page date stays 2 October.
- **Knowledge term map** gains a row mapping "Genie Ontology" to the semantic layer as a vendor name. Its Recent-changes list is full and the new 10 September entry is older than every live one, so that entry goes straight to the history file. Page date stays 7 November.
- One new source page.

### What to weigh
Mapping Databricks' "Genie Ontology" to the semantic layer, not to the ontology row, is a judgment: Databricks markets it as an ontology, but OpenAI uses it as a semantic-layer source of business definitions, and nothing in the wiki says it carries machine-checked rules. The adoption case goes to the evidence page instead of Company-wide AI enablement, which is already over its length ceiling.

## Intended changes

- [ ] **Update** `wiki/concepts/semantic-layer.md` — add "Genie Ontology" to Also called, one Current-status bullet and one Related line; adds one Recent-changes entry dated 2026-09-10 (list goes to 3); append `openai-chatgpt-data-agent-2026-09-10` to frontmatter `sources:` and one line to `## Sources`; `as_of` and Current-status stamp 2026-08-21 → 2026-09-10
    > See draft below

- [ ] **Update** `wiki/tools/codex.md` — add one bullet to "ChatGPT Work architecture" and move its stamp to 2026-09-10; adds one Recent-changes entry dated 2026-09-10 (list is at 10 of 10, so the oldest entry spills); append source id and Sources line; `as_of` stays 2026-11-23
    > See draft below

- [ ] **Spill** `wiki/tools/codex.md` → `wiki/history/tools/codex.md` — the oldest Recent-changes entry (2026-07-14 at time of writing) moves to history

- [ ] **Update** `wiki/training/ai-adoption-evidence.md` — add one Case-evidence bullet; adds one Recent-changes entry dated 2026-09-10 (list goes to 8, no spill); append source id and Sources line; `as_of` stays 2026-10-02
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-term-map.md` — add one row to "Semantic layer and ontology"; adds one Recent-changes entry dated 2026-09-10 (list is at 10 of 10 and the new entry is the oldest-dated, so it spills at once and the live list is unchanged); append source id and Sources line; `as_of` stays 2026-11-07
    > See draft below

- [ ] **Spill** `wiki/concepts/knowledge-term-map.md` → `wiki/history/concepts/knowledge-term-map.md` — the new 2026-09-10 entry, the oldest-dated once inserted, goes to history (2026-09-09 already spilled today)

- [ ] **Create** `wiki/sources/articles/openai-chatgpt-data-agent-2026-09-10.md` — source summary

## Page drafts

### wiki/concepts/semantic-layer.md (updated)

Frontmatter changes:

```
as_of: 2026-09-10
sources: [posthog-semantic-layer-2026-08-21, helixdb-helix-foundry-2026-10-19, openai-chatgpt-data-agent-2026-09-10]
```

In `## Also called`, append one sentence to the paragraph:

```
Databricks' "Genie Ontology" is a vendor name for a store of business definitions that OpenAI's Data agent reads as a semantic-layer source; despite the name, it belongs here, not under ontologies.
```

Heading change: `## Current status (as of 2026-08-21)` → `## Current status (as of 2026-09-10)`

Append as the last Current-status bullet:

```
- Mainstream assistants now read from the layer instead of guessing: OpenAI's Data agent in ChatGPT Work (2026-09-10) takes business terms, metric definitions, custom calculations and data relationships from semantic layers and trusted sources (dbt, Snowflake Horizon, Databricks Genie Ontology, GitHub, BI dashboards) before it queries the warehouse, and runs every query under the connected account's own table, row and column permissions. See [Codex](../tools/codex.md).
```

In `## Related`, append:

```
- [Codex](../tools/codex.md) — ChatGPT Work's Data agent is the first mainstream consumer of semantic layers recorded here
```

In `## Recent changes`, insert between the 2026-10-19 and 2026-08-21 entries:

```
- [2026-09-10] OpenAI's Data agent in ChatGPT Work grounds warehouse analysis in semantic layers (dbt, Snowflake Horizon, Databricks Genie Ontology, BI dashboards) and enforces per-user table, row and column permissions.
```

In `## Sources`, append:

```
- [OpenAI — Now everyone can put data to work (Data agent in ChatGPT Work)](../sources/articles/openai-chatgpt-data-agent-2026-09-10.md)
```

### wiki/tools/codex.md (updated)

Frontmatter `sources:` appends `openai-chatgpt-data-agent-2026-09-10`; `as_of` unchanged (2026-11-23).

Heading change: `## ChatGPT Work architecture (as of 2026-08-04)` → `## ChatGPT Work architecture (as of 2026-09-10)`

In that section, insert after the Plugin Directory bullet:

```
- **Data agent (2026-09-10):** a "Data" plugin, called as `@Data`, answers business questions over company data (Redshift, BigQuery, Snowflake, Databricks, ClickHouse, MongoDB, Datadog, plus Drive and SharePoint files). It reads definitions from semantic layers ([Semantic layer](../concepts/semantic-layer.md)), enforces each user's table, row and column permissions, builds editable shared dashboards (also inside Tableau, Power BI, Sigma, ThoughtSpot, Omni and Oracle BI) and acts through connected tools after approval.
```

In `## Recent changes`, insert between the 2026-09-29 and 2026-08-12 entries:

```
- [2026-09-10] Data agent in ChatGPT Work: plain-language analysis and editable dashboards over warehouse data, grounded in semantic layers and per-user permissions; OpenAI says nearly all of its product team and over two-thirds of its GTM organization use it.
```

Then remove the oldest entry (the cap is 10):

```
- [2026-07-14] OpenAI folded Codex into a new ChatGPT desktop "superapp" (Chat/Work/Codex modes); power users pushed back hard, but usage estimates put Codex around 6-7M users by mid-July, roughly 10x growth year-to-date.
```

In `## Sources`, append:

```
- [OpenAI — Now everyone can put data to work (Data agent in ChatGPT Work)](../sources/articles/openai-chatgpt-data-agent-2026-09-10.md)
```

### wiki/history/tools/codex.md (updated)

Append at the end of the file:

```

## Archived from current page on 2026-11-24

- [2026-07-14] OpenAI folded Codex into a new ChatGPT desktop "superapp" (Chat/Work/Codex modes); power users pushed back hard, but usage estimates put Codex around 6-7M users by mid-July, roughly 10x growth year-to-date.
```

### wiki/training/ai-adoption-evidence.md (updated)

Frontmatter `sources:` appends `openai-chatgpt-data-agent-2026-09-10`; `as_of` unchanged (2026-10-02).

In `## Case evidence`, append as the last bullet:

```
- **OpenAI's self-serve data analysis (September 2026).** OpenAI says nearly all of its product team and over two-thirds of its go-to-market organization analyze company data themselves with data agents in ChatGPT Work. The prerequisites came from its data team: shared business definitions, access rules, and safeguards for sensitive data. Alpha customer NTT DATA reports non-engineers in sales and corporate functions building and updating their own dashboards, which licensing cost and technical skill had kept from spreading. See [Codex](../tools/codex.md) for the Data agent itself.
```

In `## Recent changes`, insert between the 2026-10-02 and 2026-09-09 entries:

```
- [2026-09-10] Added OpenAI's internal self-serve data-analysis case (Data agent in ChatGPT Work) and the definitions, access rules and safeguards its data team put in place first.
```

In `## Sources`, append:

```
- [OpenAI — Now everyone can put data to work (Data agent in ChatGPT Work)](../sources/articles/openai-chatgpt-data-agent-2026-09-10.md)
```

### wiki/concepts/knowledge-term-map.md (updated)

Frontmatter `sources:` appends `openai-chatgpt-data-agent-2026-09-10`; `as_of` unchanged (2026-11-07).

In `### Semantic layer and ontology`, insert after the "metrics layer, governed metric catalog" row:

```
| Genie Ontology (Databricks) | Semantic layer (vendor term) | Databricks' name for the self-maintained business-semantics context layer under Genie One ([Databricks](../tools/databricks.md)). OpenAI's Data agent reads it alongside dbt and Snowflake Horizon as a source of metric and business definitions, which is the semantic layer's job; nothing recorded gives it machine-checked rules, so it is not the ontology row's sense |
```

`## Recent changes` is unchanged: the list is at its cap of 10 and the new 2026-09-10 entry is older than the oldest live entry (2026-09-25), so it goes straight to the history file (below).

In `## Sources`, append:

```
- [OpenAI — Now everyone can put data to work (Data agent in ChatGPT Work)](../sources/articles/openai-chatgpt-data-agent-2026-09-10.md)
```

### wiki/history/concepts/knowledge-term-map.md (updated)

Append to the existing `## Archived from current page on 2026-11-24` block at the end of the file, after the 2026-09-09 entry:

```
- [2026-09-10] Mapped Databricks' "Genie Ontology" to the Semantic layer as a vendor term, following its use as a definitions source by OpenAI's Data agent.
```

### wiki/sources/articles/openai-chatgpt-data-agent-2026-09-10.md (new)

```
---
title: OpenAI — Now everyone can put data to work (Data agent in ChatGPT Work)
type: source
source_type: article
source_file: raw/articles/2026-09-10-openaicom-index-put-data-to-work.md
url: https://openai.com/index/put-data-to-work/
published: 2026-09-10
ingested: 2026-11-24
domains: [agents]
---

# OpenAI — Now everyone can put data to work (Data agent in ChatGPT Work)

OpenAI's launch post for the Data agent in ChatGPT Work, a plugin that turns plain-language business questions into analysis, interactive dashboards and approved follow-up actions over company data. It grounds its answers in the organization's semantic layers and enforces each user's existing data permissions. The announcement tweet (3.7M views; replies asked how permissions work) and AINews' 2026-09-12 issue, which read it as enterprise data access becoming a first-class product primitive, were read alongside it.

## Influenced pages
- [Semantic layer](../../concepts/semantic-layer.md) — first mainstream consumer of semantic layers, with permission enforcement
- [Codex](../../tools/codex.md) — Data agent bullet in the ChatGPT Work section
- [AI adoption: evidence from practice](../../training/ai-adoption-evidence.md) — OpenAI's internal self-serve analytics case
- [Knowledge term map](../../concepts/knowledge-term-map.md) — "Genie Ontology" mapped to the semantic layer as a vendor term

## Key claims extracted
- Listed as "Data" in the ChatGPT Work Plugins directory; invoked with `@Data`; admins enable it and the data-source plugins under Workspace settings > Plugins
- Connects to Amazon Redshift, Datadog, Google BigQuery, ClickHouse, Databricks, MongoDB, Snowflake and more, plus Google Drive and SharePoint files
- Interprets data using business terms, metric definitions, custom calculations and data relationships from semantic layers and trusted sources: Databricks Genie Ontology, dbt, GitHub, Snowflake Horizon, BI dashboards
- Admins choose available connections and roles; queries enforce the connected account's table, row and column permissions
- Builds interactive dashboards that teams can edit, share and refresh; also builds and works with dashboards in Omni, Oracle BI, Power BI, Sigma, Tableau and ThoughtSpot
- Can share findings via Slack or email and carry out approved actions through connected tools
- Nearly all of OpenAI's product team and over two-thirds of its GTM organization use data agents in ChatGPT Work; enabled by shared business definitions, access rules and sensitive-data safeguards from OpenAI's data team
- Alpha-program users include NTT DATA and Thermo Fisher; NTT DATA says non-engineers in sales and corporate functions now build and update their own dashboards
```

## Schema / vocabulary additions

None.

## Open questions

None.
