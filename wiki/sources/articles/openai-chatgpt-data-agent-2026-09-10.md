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
