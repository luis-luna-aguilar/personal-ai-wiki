---
type: proposal
source: raw/articles/2026-11-24-platformclaudecom-docs-en-api-migration-2026-10-21.md
sources:
  - raw/articles/2026-11-24-platformclaudecom-docs-en-api-migration-2026-10-21.md
  - raw/articles/2026-11-24-platformclaudecom-docs-en-api-versioning.md
  - raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
status: pending
created: 2026-11-24
---

# Proposal: Anthropic API version 2026-10-21

## Summary

### In short
Upgrading an Anthropic SDK to its new major version is now a breaking change: API version 2026-10-21 rejects `temperature`, `top_p` and `top_k` with a 400 error, and new SDKs send that version by default. The proposal adds one Current-status bullet and one Recent-changes entry to the **Claude Platform** page, covering the removed parameters, the other request and field changes, the SDK's switch to bearer-token auth, and the fact that 2023-06-01 still works. It also adds one source page. No red flags. The change is small and lands on a short page.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
AINews flagged it in one line on 22 October. Anthropic's own documentation, fetched for this proposal, has the details. The API versions page lists 2026-10-21 as the first new version since 2023-06-01 and recommends it. The version is available on the Claude API, Claude Platform on AWS, both Google Cloud routes and Microsoft Foundry. On Amazon Bedrock it works only for Claude 4.7 and later. In the Messages API, a request that sends any of the three sampling parameters fails with a 400 error, even at the default value. The same happens when a `document` block sits directly in an assistant message, or when a user message carries citations. The Admin and Enterprise Analytics APIs drop old field names in favour of renamed ones, for example `scope.workspace_id` on API keys.

The migration guide spells out what this means in practice. The latest major SDKs and the CLI send 2026-10-21 and no longer have the three parameters at all. They also send the API key as `Authorization: Bearer` instead of `X-Api-Key`, so a proxy or gateway that reads the old header has to change. For Claude 4.7 and later models nothing changes in sampling, because those models already accept only the defaults. On older models such as Sonnet 4.6, a request that lowered temperature for steadier output loses that effect, and nothing replaces it. The way out is to keep that request on 2023-06-01, which stays supported. Claude Code offers a `/claude-api api-version` command to do the upgrade.

### What changes
The wiki does not mention API versioning anywhere. The Claude Platform page covers billing, usage visibility and tool availability only.

- **Claude Platform** gains a Current-status bullet on the 2026-10-21 version: what breaks, the SDK defaults, the change to bearer-token auth, the Bedrock limit and the fallback to 2023-06-01. It also gains one Recent-changes entry dated 21 October, placed between the 17 November and 7 October entries (five entries live, so nothing spills). The page date stays 17 November.
- One new source page for the migration guide, which also cites the versions page and the AINews item.

### What to weigh
The documentation pages carry no publication date. The proposal dates the change 21 October from the version's own name, and AINews reported it the next day. The Admin API field renames and the SDK type changes are left on the source page rather than the tool page.

## Intended changes

- [ ] **Update** `wiki/tools/claude-platform.md` — add one Current-status bullet, add one Recent-changes entry dated 2026-10-21 (inserted between 2026-11-17 and 2026-10-07; list goes from 5 to 6, no spill), add the source id and Sources link; `as_of` stays 2026-11-17
- [ ] **Create** `wiki/sources/articles/anthropic-api-version-2026-10-21.md` — source summary

## Page drafts

### wiki/tools/claude-platform.md (updated)

Frontmatter (`sources:` appends one id; `as_of` unchanged):

```
sources: [claude-code-fast-mode-default-2026-05, claude-managed-agents-updates-2026-05, ainews-poolside-nvidia-2026-08-21, claude-sonnet-5-5-launch, claude-haiku-5-5-launch-2026-10-19, claude-platform-linked-billing-2026-11-17, anthropic-api-version-2026-10-21]
```

New bullet at the end of `## Current status (as of 2026-11-17)`:

```
- **API version 2026-10-21.** The first new API version since 2023-06-01. The Messages API rejects `temperature`, `top_p` and `top_k` with a 400 error, even at default values. It also rejects `document` blocks placed directly in assistant messages and citations in user messages, and the Admin and Analytics APIs drop old field names. The latest major SDKs and CLI send this version by default and send the key as `Authorization: Bearer` instead of `X-Api-Key`. Claude 4.7+ models sample as before. Requests that need a non-default temperature on older models stay on 2023-06-01, which remains supported. On Bedrock the new version works only for Claude 4.7+.
```

`## Recent changes` (adds one entry dated 2026-10-21 between the 11-17 and 10-07 entries):

```
- [2026-11-17] Linked billing launched in beta: organization links with per-platform spend limits replace shared API keys.
- [2026-10-21] API version 2026-10-21 removes `temperature`, `top_p` and `top_k` from the Messages API; new major SDKs default to it; 2023-06-01 stays supported.
- [2026-10-07] Monthly Platform API credits added for Max and Team subscriptions.
- [2026-08-21] Computer use, browser tool, Skills API and Files API reach GA.
- [2026-05-20] MCP tunnels managed from Console workspace settings.
- [2026-05-19] Console adds prompt-cache diagnostics.
```

`## Sources` (adds one link at the top):

```
- [Migrating to API version 2026-10-21](../sources/articles/anthropic-api-version-2026-10-21.md)
```

### wiki/sources/articles/anthropic-api-version-2026-10-21.md (new)

```
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
```

## Schema / vocabulary additions

None.

## Open questions

None.
