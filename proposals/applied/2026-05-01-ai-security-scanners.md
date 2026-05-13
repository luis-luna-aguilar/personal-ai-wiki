---
type: proposal
source: raw/newsletters/2026-05-01-ainews-agents-for-everything-else-codex-for-kno.md
status: pending
created: 2026-05-05
---

# Proposal: AI security scanners as first-class products

## Summary

AINews reports two parallel product moves: Anthropic launched Claude Security as a repository vulnerability scanner powered by Opus 4.7, and Cursor shipped Cursor Security Review with always-on PR review and scheduled codebase scans. This is a second-hand but useful category signal that coding-agent vendors are packaging security review as a recurring devsecops workflow.

## Intended changes

- [x] **Update** `wiki/state-of/cybersecurity.md` — add Claude Security and Cursor Security Review to `AI-assisted vulnerability detection` as secondary-source entries.
    > **After:** `- **Claude Security** — Anthropic; reported repo vulnerability scanner that validates findings and suggests fixes using Opus 4.7; source is AINews secondary coverage *(as of 2026-05-01)*`
    > **After:** `- **Cursor Security Review** — Cursor; reported always-on PR review plus scheduled codebase scans; source is AINews secondary coverage *(as of 2026-05-01)*`

- [x] **Update** `wiki/tools/cursor.md` — add a recent-change entry for Cursor Security Review, with secondary-source caveat.

- [x] **Update** `wiki/tools/claude-code.md` or create a future Anthropic security tool page only after primary Anthropic material is fetched. Do not overload Claude Code unless the product is confirmed to live there.

- [x] **Create** `wiki/sources/newsletters/ai-security-scanners-2026-05-01.md` — source summary.

## Page drafts

### wiki/sources/newsletters/ai-security-scanners-2026-05-01.md (new)

```markdown
---
title: AI security scanners become first-class vendor products
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-01-ainews-agents-for-everything-else-codex-for-kno.md
published: 2026-05-01
ingested: 2026-05-05
domains: [cybersecurity, coding]
---

# AI security scanners become first-class vendor products

AINews reports that Anthropic and Cursor both introduced packaged security-review products: Claude Security for repo vulnerability scanning and Cursor Security Review for always-on PR review and scheduled scans.

## Influenced pages

- [State of Cybersecurity](../../state-of/cybersecurity.md) — expands AI-assisted vulnerability detection beyond Codex Security
- [Cursor](../../tools/cursor.md) — possible product-surface update

## Key claims extracted

- Anthropic's Claude Security is described as validating findings and suggesting fixes with Opus 4.7.
- Cursor Security Review is described as always-on PR review plus scheduled codebase scanning.
- The broader trend is coding-agent vendors moving into packaged devsecops workflows.
```

## Verification notes

- This should be applied conservatively because the source is a newsletter summary of social/product posts. Fetch primary Anthropic and Cursor pages before creating dedicated tool pages.
