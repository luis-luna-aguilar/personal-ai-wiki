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
