---
title: Migrating to API version 2026-10-21 (Claude Platform docs)
type: source
source_type: article
source_file: raw/articles/2026-11-24-platformclaudecom-docs-en-api-migration-2026-10-21.md
url: https://platform.claude.com/docs/en/api/migration-2026-10-21
published: 2026-10-21
ingested: 2026-11-24
domains: [agents]
---

# Migrating to API version 2026-10-21 (Claude Platform docs)

Anthropic's migration guide for moving from API version 2023-06-01 to 2026-10-21, read together with the [API versions page](https://platform.claude.com/docs/en/api/versioning) (raw: `raw/articles/2026-11-24-platformclaudecom-docs-en-api-versioning.md`). AINews reported the change on 2026-10-22 (`raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md`). The docs pages carry no publication date, so the date here comes from the version name.

## Influenced pages
- [Claude Platform](../../tools/claude-platform.md) — new Current-status bullet and Recent-changes entry on the API version

## Key claims extracted
- 2026-10-21 is the recommended version. It is available on the Claude API, Claude Platform on AWS, Claude Models on Google Cloud (Anthropic- and Google-managed) and Microsoft Foundry. On Amazon Bedrock it works only for Claude 4.7 and later.
- Messages API (including token counting and Message Batches): `temperature`, `top_p` and `top_k` return a 400 error, even at default values. `document` blocks placed directly in assistant messages return 400. Non-empty `citations` on text blocks in user messages return 400.
- Without the parameters, requests sample at the defaults (temperature 1.0). Claude 4.7+ already accepts only defaults, so its sampling does not change. On models such as Sonnet 4.6, lowered temperature loses its effect and no setting replaces it. Such requests can stay on 2023-06-01.
- The Admin API and Enterprise Analytics API drop old field names: `roles`→`role_ids`, `group_id`→`rbac_group_id`, `name`→`display_name`, `group_type`→`group.type`, API-key `workspace_id`→`scope.workspace_id`, `actor.email`→`actor.email_address`, `summaries`→`data`.
- SDKs and the CLI at their latest major versions (Python `anthropic` 2.0.0) send `anthropic-version: 2026-10-21`, including the Bedrock and Google Cloud clients, and drop the removed parameters and fields from their types.
- The SDKs send the API key as `Authorization: Bearer` instead of `X-Api-Key`, so proxies and gateways that read the old header must change. A client holds one credential. The Text Completions API is removed from the TypeScript, Go, Java and Ruby SDKs and the CLI. Tool-runner client-side compaction is replaced by server-side compaction.
- Claude Code offers `/claude-api api-version` to do the upgrade.
