---
title: Anthropic — The AI-native SDLC playbook
type: source
source_type: article
source_file: raw/articles/2026-11-23-claudecom-resources-articles-the-ai-native-sdlc-playbook.md
url: https://claude.com/resources/articles/the-ai-native-sdlc-playbook
published: 2026-08-21
ingested: 2026-11-24
domains: [coding, agents]
---

# Anthropic — The AI-native SDLC playbook

A long guide from Anthropic's Applied AI team (also published as a PDF) on rebuilding the whole software lifecycle around agentic coding. It is organized as six stages of "plays", each with prerequisites, setup, a worked template, governance notes and leading/lagging metrics. The publication date comes from the page's `datePublished` metadata.

## Influenced pages
- [Software factory](../../workflows/software-factory.md) — new "Stage hand-offs" section: artifact chain, gates, legacy source of truth, control-band loop closure
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — See-also pointer to the Stage hand-offs section

## Key claims extracted
- With build collapsed to hours, the bottleneck moves to plan, review/test and deploy. Line-by-line human review stops scaling, and governance exceptions still wait for weekly or monthly committees.
- Each stage commits an artifact the next reads: `intent.md` → `spec.md` → plan-mode `plan.md` → diff and tests → PR with review findings → incident record. Each accepted artifact fires the next gate, and the commit chain is the audit trail.
- Plan: the originator brainstorms with Claude into an `intent.md` (problem, proposed outcome, affected users and systems, constraints, open questions). The product owner corrects it before commit. Non-engineers commit through a GitHub connector from claude.ai or Cowork.
- Build: plan mode is the default starting point. Auto-accept becomes the default for routine work once a tuned CLAUDE.md (with a "Things Claude gets wrong" section), policy skills (example: `secure-api-review`), blocking hooks and a runnable test suite exist. Parallel sessions and a verifier subagent come next.
- Legacy systems: name one source of truth per artifact (the repo, or Jira/ServiceNow/the requirements tool via MCP). The minimum bar is two-way linkage of record ID and commit SHA.
- Test: give Claude a feedback loop (a verification block in CLAUDE.md) and run continuous agent evals in CI (example GitHub Actions workflow).
- Deploy: every PR gets the same review passes (bugs, security, compliance), defined in a REVIEW.md that caps nits at five. The writing agent cannot approve its own code, and humans approve through branch protection. Hooks act as approval gates (PreToolUse `production-gate.sh` blocks production deploys without `RELEASE_APPROVAL`, exit 2). Non-negotiable hooks and permission denies go in managed settings deployed via MDM or the admin console.
- Maintain: a deterministic control-band script (rolling baseline, Western Electric rules, `bands.yaml`) logs at 1σ, runs Claude read-only to diagnose at 2σ, and at 3σ may only open a PR or trigger a pre-approved runbook. The diagnosis becomes the next `intent.md`, and each shipped fix adds an eval.
- Recurring codebase scans run on a schedule (Claude Security as the hosted form). Findings that fit one PR go through review, larger ones become `intent.md`. Claude Tag acts as an on-call first responder in Slack and writes post-mortems to a version-controlled lessons file.
- Metrics per play, for example time to first review (should fall to minutes) and defects caught before merge versus escaped to production.
