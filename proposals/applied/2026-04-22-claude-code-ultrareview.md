---
type: proposal
sources:
  - raw/articles/2026-04-23-codeclaudecom-docs-en-ultrareview.md
  - raw/articles/2026-04-22-codeclaudecom-docsenultrareview.md
status: pending
created: 2026-04-23
---

# Proposal: Claude Code /ultrareview

## Summary

Anthropic shipped `/ultrareview` in Claude Code v2.1.86+ (research preview). Unlike the existing `/review` (single-pass, seconds, local), ultrareview launches a fleet of reviewer agents in a remote cloud sandbox that **independently reproduces and verifies each finding** before reporting it. Takes 5-10 minutes in the background; results are verified bugs rather than style suggestions. Pricing: 3 free runs through May 5 for Pro/Max, then ~$5-20 per review as extra usage. Requires Claude.ai login; not available on Bedrock, Vertex AI, or Foundry. This is also the clearest current example of Claude Code moving from a local terminal agent toward cloud-native multi-agent workflows.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — add `/ultrareview` section; add source to frontmatter; prepend Recent changes entry
- [x] **Create** `wiki/sources/articles/claude-code-ultrareview.md` — source summary

## Page drafts

### wiki/tools/claude-code.md (update — diff only)

> **Add to `sources` frontmatter:** `claude-code-ultrareview`

> **Add new section after `## Routines`:**
> ```markdown
> ## /ultrareview
>
> Cloud multi-agent code review, introduced in v2.1.86 as a research preview. Unlike `/review` (single-pass, seconds, runs locally), ultrareview launches a fleet of reviewer agents in a remote sandbox that independently reproduces and verifies each finding before reporting it — so results focus on real bugs rather than style suggestions.
>
> - Runs entirely in a remote cloud sandbox; terminal stays free while it runs
> - Many reviewer agents explore the change in parallel, surfacing issues a single-pass review would miss
> - Runs as a background task (~5-10 minutes); findings appear as a notification in your session
> - Can review the diff between your current branch and the default branch (including uncommitted and staged changes), or a GitHub PR by number (`/ultrareview <PR-number>`)
> - Requires authentication with a Claude.ai account — not available with API key only, and not available on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry
> - Not available to organizations with Zero Data Retention enabled
>
> **Pricing:**
> | Plan | Included free runs | After free runs |
> | --- | --- | --- |
> | Pro | 3 free through May 5, 2026 | billed as extra usage |
> | Max | 3 free through May 5, 2026 | billed as extra usage |
> | Team and Enterprise | none | billed as extra usage |
>
> Paid reviews typically cost $5–$20 depending on change size. Extra usage must be enabled on the account before launching a paid review; run `/extra-usage` to check or enable it. Use `/tasks` to monitor or stop a running review.
>
> Use `/review` for fast feedback while iterating. Use `/ultrareview` before merging a substantial change when you want a deeper pass with independent verification.
> ```

> **Add to `## Recent changes` (prepend):**
> ```markdown
> - [2026-04-23] /ultrareview added (v2.1.86+, research preview): cloud multi-agent code review with independent finding verification; 5-10 min background; 3 free runs for Pro/Max through May 5, 2026; then $5-20 extra usage; requires Claude.ai login; not on Bedrock/Vertex AI/Foundry
> ```

> **Update `as_of` in frontmatter:** `as_of: 2026-04-23`

### wiki/sources/articles/claude-code-ultrareview.md (new)

````md
---
title: Find bugs with ultrareview
type: source
source_type: article
source_file: raw/articles/2026-04-23-codeclaudecom-docs-en-ultrareview.md
url: https://code.claude.com/docs/en/ultrareview
published: 2026-04-23
ingested: 2026-04-23
domains: [coding, agents]
---

# Find bugs with ultrareview

Official Claude Code documentation page for the /ultrareview command, introduced in v2.1.86 as a research preview.

## Influenced pages

- [[tools/claude-code]] — new /ultrareview section added

## Key claims extracted

- Fleet of reviewer agents in a remote sandbox; each finding independently reproduced and verified before reporting
- Runs as background task (~5-10 minutes); results appear as notification in session
- Can review branch diff (including uncommitted/staged changes) or GitHub PR by number
- Requires Claude.ai account login — not available with API key only
- Not available on Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry, or Zero Data Retention orgs
- If repo is too large to bundle: use PR mode (`/ultrareview <PR-number>`)
- Pro/Max: 3 free runs through May 5, 2026; then extra usage
- Team/Enterprise: no free runs; always extra usage
- Typical cost per paid review: $5-$20 depending on change size
- Stop a review via `/tasks`; stopping archives the cloud session and returns no partial findings
````
