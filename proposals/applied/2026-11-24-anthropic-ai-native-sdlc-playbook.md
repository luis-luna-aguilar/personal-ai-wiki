---
type: proposal
source: raw/articles/2026-11-23-claudecom-resources-articles-the-ai-native-sdlc-playbook.md
status: pending
created: 2026-11-24
---

# Proposal: Anthropic's AI-native SDLC playbook

## Summary

### In short
Once agents write the code, the bottleneck moves to planning, review and release, which still run at human speed. Anthropic's fix is to chain the lifecycle through committed files: each stage writes one artifact to git, and accepting that artifact triggers the next stage. The chain of commits then serves as the audit trail. The proposal creates `workflows/ai-native-sdlc.md` with that artifact chain, the approval gates and the closed maintenance loop. It adds a pointer on **Software factory**, a See-also line on **AI enablement — software development**, and a source page. The reason to hesitate is overlap: Software factory already describes an agent loop across the lifecycle.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Anthropic's Applied AI team published "The AI-native SDLC playbook" on claude.com on 21 August 2026. It is a long guide, also offered as a PDF. Its starting point is that build time has collapsed to hours while the controls around it were designed for human authors. Line-by-line review cannot keep up with agent-written diffs, security teams are sized for human output, and exceptions still wait for weekly committees. The guide notes that the same idea also goes by "agentic SDLC", "AI SDLC" and "agentic software development".

The guide walks through six stages (Plan, Design, Build, Test, Deploy, Maintain) as "plays". Each play comes with setup steps, a worked template, governance notes and leading and lagging metrics. The thread running through all of them is a committed artifact. An idea becomes an `intent.md` that the product owner corrects. Accepting it starts a design session that produces `spec.md`, the approved spec starts Claude Code plan mode, and so on through the diff, the PR with its ranked review findings, and the incident record. Two governance moves stand out. First, hooks act as approval gates: a script that runs before the agent acts can allow, block, or pause until a named person approves, and the rules nobody may switch off live in managed settings. Second, the loop closes on its own: a deterministic script watches a production metric against a rolling baseline, and a breach writes the next `intent.md`. The guide is equally practical about legacy systems. For every artifact, it says, name one system as the source of truth, and at minimum link the Jira record and the commit to each other. The plays can be adopted one at a time, in the order a dependency graph gives.

### What changes
The wiki describes the software factory as agents covering the whole lifecycle. It explains how to split work and what must exist first, but not how one stage hands off to the next.

- New page `workflows/ai-native-sdlc.md`, dated 21 August. It covers the stage-to-artifact chain, the gate types (human review of artifacts, hooks as allow/ask/block gates, managed settings, branch protection), choosing a source of truth next to legacy tools, control-band triggers that restart the loop, and recurring scans.
- **Software factory** gains one bullet under Structure pointing to the new page, one Related line, the source, and a Recent-changes entry dated 21 August, placed by date (six entries become seven, no spill). Its page date stays 25 October.
- **AI enablement — software development** gains only a See-also line, because its body is already past its word ceiling.
- The index gains the new page, and one new source page is added.

### What to weigh
Two scope choices. First, the new page keeps the pattern general and leaves the product templates on the source page: the CLAUDE.md, skill, verifier, GitHub Actions and managed-settings examples. The wiki already covers most of those mechanisms on its Claude Code practice pages. Second, the open question asks whether the chain should be its own page or a section of Software factory.

## Intended changes

- [ ] **Create** `wiki/workflows/ai-native-sdlc.md` — stage-by-stage artifact chain and gate model
- [ ] **Update** `wiki/workflows/software-factory.md` — one Structure bullet pointing to the new page; one Related line; append source id and Sources link; adds one Recent-changes entry dated 2026-08-21, inserted between the 2026-09-01 and 2026-07-14 entries (6 → 7, no spill); `as_of` stays 2026-10-25
- [ ] **Update** `wiki/training/ai-enablement-software-development.md` — one See-also line only (no body change; page already at 106% of its ceiling)
- [ ] **Update** `wiki/index.md` — add the new workflow page under Workflows, after `workflows/software-factory`
- [ ] **Create** `wiki/sources/articles/claude-ai-native-sdlc-playbook-2026-08-21.md` — source summary

## Page drafts

### wiki/workflows/ai-native-sdlc.md (new)

````md
---
title: AI-native SDLC
type: workflow
domains: [coding, agents]
subcategory: agentic-orchestration-patterns
tags: [agentic, anthropic]
as_of: 2026-08-21
sources: [claude-ai-native-sdlc-playbook-2026-08-21]
---

# AI-native SDLC

An AI-native software development lifecycle keeps the old control objectives (accountability, separation of duties, audit) but enforces them differently. Each of the six stages (Plan, Design, Build, Test, Deploy, Maintain) ends by committing one artifact to version control, and the next stage starts by reading it. Accepting an artifact fires the next gate, so the lifecycle becomes a loop and humans review at the gates instead of starting each stage. Sources also call it the agentic SDLC, the AI SDLC or agentic software development. [Software factory](software-factory.md) covers the wider question of how to split and supervise agent work across the lifecycle. This page covers how the stages hand off.

## Current status (as of 2026-08-21)

- Anthropic's Applied AI team published the reference playbook. Its premise is that when build shrinks to hours, plan, review/test and deploy become the bottleneck, and controls designed for human authors (line-by-line review, weekly committees) stop matching reality.
- The plays are modular. Teams adopt them in dependency order rather than all at once, and most organizations sit between the traditional and AI-native ends.

## The artifact chain

| Stage | Committed artifact | What accepting it triggers |
| --- | --- | --- |
| Plan | `intent.md`: what is wanted, why, under which constraints, in the originator's words; corrected by the product owner | Requirements and design session |
| Design | `spec.md`, guided by standards encoded as skills | Plan mode |
| Build | `plan.md`, then the diff and its tests | Test and review |
| Test | Eval results from continuous evals in CI | PR |
| Deploy | The PR with ranked review findings and human approval | Pipeline and release gate |
| Maintain | Incident record; a diagnosis written as a new `intent.md` | The loop restarts at Plan |

Early stages use Markdown because a product owner and an agent can both read and act on the same file. From Build on, the artifact is code and its records. The commit chain is the audit trail: who asked for what, what the agent produced, who approved it.

## Gates

- **Human review moves up a level.** Every PR gets the same agent review passes (bugs, security, compliance with spec and plan), with nits capped and findings ranked. Humans judge intent and risk, and approval still comes from a person through branch protection, so the agent that wrote the code cannot approve it.
- **Hooks as approval gates.** A hook that runs before the agent acts can allow, block, or ask, pausing until a named person approves (for example, production deploys need a release authorization). Team hooks live in the repo. Non-negotiable ones go in managed settings that engineers cannot override. A block should state its reason and the route to approval.
- **Autonomy follows the guardrails.** Auto-accept becomes the default for routine work only once instructions, policy skills, blocking hooks and a runnable test suite exist.

## Fitting legacy systems

For each artifact, name one system as the source of truth. That can be the repo, with Jira or the requirements tool referencing commits, or the legacy tool, with the Markdown files as working copies synced through MCP. The minimum bar is linkage: every artifact carries the record ID and every record carries the commit SHA.

## Closing the loop

- **Control bands.** A deterministic, unit-tested script watches one metric with a stable baseline (CI failure rate, post-deploy 5xx, PR cycle time) and responds in tiers. At 1σ it logs. At 2σ it runs the agent read-only to diagnose. At 3σ the agent may act, but only by opening a PR into the review gate or triggering a pre-approved runbook. The diagnosis becomes the next `intent.md`, and each shipped fix adds an eval for the incident.
- **Recurring scans.** Security scans go stale as both the code and the models change, so they run on a schedule. A finding that fits in one PR goes through the review gate. Anything larger becomes an `intent.md`.
- **Chat-channel intake.** An agent in incident channels picks up urgent requests and routes them the same way: a small fix becomes a PR, a larger one becomes an `intent.md`.

## Weaknesses / caveats

- It is a vendor playbook built around Claude Code, Claude Security and Claude Tag. The chain and gate pattern is general, but the templates are product-specific.
- Fully headless maintenance needs every earlier gate in place first: PR review, hooks, a rollback path and the `intent.md` format.

## Recent changes

- [2026-08-21] Page created from Anthropic's AI-native SDLC playbook: stage-to-artifact chain, gate types, source-of-truth options for legacy tools, and control-band loop closure.

## Related

- [Software factory](software-factory.md) — the end-to-end agent pipeline this chain operationalizes
- [AI PR and code review](ai-pr-code-review.md) — the Deploy-stage review gate in depth
- [Evals for agentic software development](../training/evals-for-agentic-software-development.md) — the Test-stage eval stack
- [Spec-driven development](../concepts/spec-driven-development.md) — specs as the primary artifact for coding agents
- [AI enablement — software development](../training/ai-enablement-software-development.md) — team rollout guidance

## Sources

- [Anthropic — The AI-native SDLC playbook](../sources/articles/claude-ai-native-sdlc-playbook-2026-08-21.md)
````

### wiki/workflows/software-factory.md (updated)

Frontmatter (`sources:` appends one id; `as_of` unchanged at 2026-10-25):

```
sources: [gas-city-software-factory-2026-05, aiewf-loops-debate-2026-07-03, software-factories-fde-2026-07, aiewf-2026-five-trends-latentspace, latent-space-pr-not-welcome-2026-09-01, ubereng-software-factory-2026-08-28, composio-anti-slop-software-factory-2026-10-12, rauchg-gdp-ts-2026-10, thorstenball-how-i-work-with-agents-2026-10-25, claude-ai-native-sdlc-playbook-2026-08-21]
```

New bullet at the end of `### Structure`:

```
- **Hand off between stages through committed artifacts.** Anthropic's AI-native SDLC playbook has each stage commit one file that starts the next (`intent.md` → `spec.md` → `plan.md` → diff and tests → reviewed PR → incident record), with hooks and branch protection as the gates and the commit chain as the audit trail. See [AI-native SDLC](ai-native-sdlc.md). *Source: Anthropic (2026-08-21)*
```

`## Recent changes` (adds one entry dated 2026-08-21 between the 2026-09-01 and 2026-07-14 entries; 6 → 7, no spill):

```
- [2026-09-01] Added the "PRs closed by default" software-factory pattern ...
- [2026-08-21] Added the artifact-chain hand-off bullet, pointing to the new [AI-native SDLC](ai-native-sdlc.md) page (Anthropic's six-stage playbook).
- [2026-07-14] Added named AI Engineer World's Fair 2026 detail ...
```

`## Related` (adds one line after the Agentic orchestration patterns line):

```
- [AI-native SDLC](ai-native-sdlc.md) — stage-by-stage artifact chain and approval gates for running the lifecycle through agents
```

`## Sources` (appends one link):

```
- [Anthropic — The AI-native SDLC playbook](../sources/articles/claude-ai-native-sdlc-playbook-2026-08-21.md)
```

### wiki/training/ai-enablement-software-development.md (updated)

`## See also` (adds one line after the Software factory line; nothing else changes, `as_of` unchanged):

```
- [AI-native SDLC](../workflows/ai-native-sdlc.md) — Anthropic's six-stage operating model: each stage commits an artifact that triggers the next, hooks as approval gates, control bands that reopen the loop
```

### wiki/index.md (updated)

New line under Workflows, directly after `workflows/software-factory`:

```
- [workflows/ai-native-sdlc](workflows/ai-native-sdlc.md) — Anthropic's AI-native SDLC playbook as a pattern: six stages each commit an artifact (intent.md → spec.md → plan.md → diff → reviewed PR → incident) that triggers the next; hooks as allow/ask/block approval gates, managed settings, source of truth beside legacy tools, control-band loop closure *(as_of: 2026-08-21)*
```

### wiki/sources/articles/claude-ai-native-sdlc-playbook-2026-08-21.md (new)

```
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
- [AI-native SDLC](../../workflows/ai-native-sdlc.md) — new page: artifact chain, gates, legacy source of truth, loop closure
- [Software factory](../../workflows/software-factory.md) — artifact-chain hand-off bullet and pointer
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — See-also pointer

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
```

## Schema / vocabulary additions

None.

## Open questions

- Should the artifact chain live on its own `workflows/ai-native-sdlc.md` page (as drafted), or as a new `### Stage hand-offs` section inside **Software factory**? The section would add about 450 words to a page that is under its ceiling today. The separate page keeps Software factory focused on structure and prerequisites.
	- Inside the software factory
