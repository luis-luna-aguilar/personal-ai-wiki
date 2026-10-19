---
title: Claude Security product page
type: source
source_type: article
source_file: raw/articles/2026-09-09-claudecom-product-claude-security.md
url: https://claude.com/product/claude-security
ingested: 2026-09-09
domains: [cybersecurity]
---

# Claude Security product page

Anthropic's product page confirms Claude Security is now in public beta for Claude Enterprise: it scans a codebase with Claude Mythos 5.1, traces data flows across files to catch multi-component vulnerabilities pattern-matching tools miss, runs every finding through an adversarial verification pass where Claude challenges its own results before surfacing them, and proposes a reviewable patch for each finding rather than just a report. A separate Claude Security plugin for Claude Code is also in beta, running the same scan/validate/patch pipeline locally while keeping code inside the user's own environment. No publish date appears on the page; content reflects the page as fetched 2026-09-09.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — upgraded the Claude Security bullet from thinly-sourced (AINews secondary coverage, reported use of Opus 4.7) to primary-source-confirmed public beta on Claude Mythos 5.1, with the adversarial-verification and patch-suggestion detail and the separate Claude Code plugin beta
- [Claude Code](../../tools/claude-code.md) — Claude Security section: public beta detail and Claude Code plugin (moved from State of Cybersecurity)

## Key claims extracted
- Claude Security is in public beta for Claude Enterprise (previously only reported via secondary coverage)
- Uses Claude Mythos 5.1 to scan and trace vulnerabilities, not Opus 4.7 as earlier secondary coverage claimed
- Every finding goes through an adversarial self-verification pass before being surfaced
- Findings include a recommended patch for human review and approval
- A separate Claude Security plugin for Claude Code is in beta, running scans locally while keeping code in the user's environment
