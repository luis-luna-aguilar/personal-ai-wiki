---
type: proposal
source: raw/newsletters/2026-05-14-higgsfield-launches-supercomputer-for-creative.md
status: pending
created: 2026-05-18
---

# Proposal: Claude for Small Business + Legal — 27 one-click agentic workflows (lightweight)

## Summary

Anthropic launched two vertical product bundles on top of Cowork: Claude for Small Business (15 agentic workflows + 15 skills; integrations with QuickBooks, PayPal, DocuSign) and Claude for Legal Professionals (12 one-click workflows). This is Anthropic's first direct move into end-user vertical task automation with prebuilt workflow bundles, rather than a developer API play.

## Intended changes

- [x] **Update** `wiki/tools/claude-cowork.md` — add Small Business and Legal as vertical products built on Cowork; update `as_of`; add Recent changes entry; add source
    > **as_of:** `2026-04-23` → `2026-05-14`
    >
    > **Add new section:**
    > ```markdown
    > ## Vertical workflow bundles (as of 2026-05-14)
    >
    > Anthropic launched two prebuilt Cowork-based workflow bundles targeting end-users rather than developers:
    >
    > - **Claude for Small Business** — 15 ready-to-run agentic workflows + 15 skills; integrations with QuickBooks, PayPal, DocuSign; automates payroll planning, invoice chasing, campaign launch, and similar repeatable tasks
    > - **Claude for Legal Professionals** — 12 one-click workflows for legal document and workflow automation
    >
    > Both bundles are the clearest signal yet of Anthropic shifting from developer API tools toward direct end-user vertical automation products.
    > ```
    >
    > **Add to Recent changes:**
    > `- [2026-05-14] Claude for Small Business and Claude for Legal launched: 27 combined one-click agentic workflows on Cowork, with QuickBooks/PayPal/DocuSign integrations; first direct vertical automation product push`
    >
    > **Add to sources:** `claude-smb-legal-may-2026`

- [x] **Update** `wiki/state-of/agents.md` — update Cowork line in Agent orchestration to reflect vertical products; add to Recent changes
    > **Before:**
    > `- [Claude Cowork](../tools/claude-cowork.md) — Anthropic; desktop knowledge-work agent with Live Artifacts; VM-backed local-first execution; scheduled and persistent tasks *(as of 2026-04-21)*`
    >
    > **After:**
    > `- [Claude Cowork](../tools/claude-cowork.md) — Anthropic; desktop knowledge-work agent with Live Artifacts; VM-backed local-first execution; now also the substrate for Claude for Small Business (15 workflows, QuickBooks/PayPal/DocuSign) and Claude for Legal (12 workflows) *(as of 2026-05-14)*`
    >
    > **Add to Recent changes:**
    > `- [2026-05-14] Anthropic launched Claude for Small Business and Claude for Legal on Cowork: 27 one-click agentic workflows; first direct vertical automation bundles targeting end-users rather than developers`

- [ ] **Create** `wiki/sources/newsletters/claude-smb-legal-may-2026.md` — source summary

## Page drafts

### wiki/sources/newsletters/claude-smb-legal-may-2026.md (new)

```markdown
---
title: "Claude for Small Business + Legal launch (May 2026)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-14-higgsfield-launches-supercomputer-for-creative.md
published: 2026-05-14
ingested: 2026-05-18
domains: [agents]
---

# Claude for Small Business + Legal launch (May 2026)

Superhuman newsletter covered Anthropic's launch of two Cowork-based vertical workflow bundles: Claude for Small Business (15 agentic workflows + 15 skills, QuickBooks/PayPal/DocuSign integrations) and Claude for Legal Professionals (12 one-click workflows). First direct move into prebuilt end-user vertical automation.

## Influenced pages

- [Claude Cowork](../../tools/claude-cowork.md) — vertical workflow bundles added
- [State of Agents](../../state-of/agents.md) — Cowork line updated

## Key claims extracted

- Claude for Small Business: 15 agentic workflows + 15 skills; QuickBooks, PayPal, DocuSign integrations
- Claude for Legal: 12 one-click workflows for legal professionals
- Uses Cowork as the agent substrate
- Signals Anthropic shifting from developer API focus toward end-user vertical automation products
- Product URLs: claude.com/solutions/small-business, claude.com/solutions/legal
```
