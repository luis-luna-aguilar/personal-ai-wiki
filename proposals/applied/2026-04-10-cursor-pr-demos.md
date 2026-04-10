---
type: proposal
source: raw/tweets/2026-04-10-cursor_ai-2042287192895267212.md
status: pending
created: 2026-04-10
---

# Proposal: Cursor PR demos and screenshots

## Summary

Cursor shipped a feature that auto-attaches demo videos and screenshots to GitHub PRs created by its cloud agents. Teams can visually review AI-generated code changes directly in GitHub.

## Intended changes

- [x] **Update** `wiki/tools/cursor.md` — add recent change entry and note under current status
    > **Add to Recent changes (becomes entry 2, pushing count to 2):**
    > `- [2026-04-10] Cloud agents now auto-attach demo videos and screenshots to GitHub PRs`
    > **Add bullet to "Current status" section:**
    > `- Cloud agents auto-attach demo videos and screenshots to PRs for visual review *(as of 2026-04-10)*`
    > **Update frontmatter `as_of`** to `2026-04-10` and add `cursor-pr-demos` to `sources:`

- [x] **Create** `wiki/sources/articles/cursor-pr-demos.md` — source summary

## Page drafts

### wiki/sources/articles/cursor-pr-demos.md (new)

```
---
title: Cursor ships PR demo attachments
type: source
source_type: tweet
source_file: raw/tweets/2026-04-10-cursor_ai-2042287192895267212.md
url: https://x.com/cursor_ai/status/2042287192895267212
published: 2026-04-10
ingested: 2026-04-10
domains: [coding]
---

# Cursor ships PR demo attachments

Cursor can now attach demos and screenshots of cloud agent work to the GitHub PRs it opens, letting teams review AI-generated artifacts directly in GitHub.

## Influenced pages

- [[tools/cursor]] — new recent change, status update

## Key claims extracted

- Cloud agents auto-attach demo videos and screenshots to PRs
- Teams can review AI-generated code changes visually in GitHub
```

## Comments

- Also for my personal space, there is stuff that I need to check or delegate to my team to check. This proposal from Cursor, about having remote environments in which we can send something to be completed and attach screenshots and videos to the PR, is very compelling and we need to test it. so let's create some kind of backlog of tasks that refer to my wiki and test in this workflow, which is one of them. Again in my personal space.