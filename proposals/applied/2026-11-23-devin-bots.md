---
type: proposal
source: raw/articles/2026-11-23-devinai-bots.md
status: pending
created: 2026-11-23
---

# Proposal: Devin Bots

## Summary

### In short
Cognition has entered the AI-teammate race: a Devin Bot takes a goal, runs a team of parallel Devin sessions until their pull requests are ready to merge, and asks a human only for approvals, blockers and decisions. That puts Devin beside Grok Bot, Claude Tag and ChatGPT dots, but built around engineering work rather than general office tasks. The proposal adds a short Devin Bots section to the Devin page, rewrites Devin's leader line on the State of Agents dashboard, and creates one source page. The one hesitation is that the page carries no date, so 23 November is assumed.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The source is Cognition's product page for Devin Bots at devin.ai/bots. It is a launch page, not a technical write-up. A Bot is a long-running manager agent. You give it a goal ("move checkout to the new payments API"), it breaks the goal into pieces, and it starts one Devin session per piece, each on its own cloud machine. It keeps each session going until the pull request passes its tests and review. You can text it, message it in Slack, phone it for a spoken update, or add it to a group chat. A "Needs you" queue shows only what it cannot decide alone: a production deploy to approve, a missing API key, a keep-or-drop call on old endpoints.

Bots also run on schedules and triggers, for example watching a support channel for customer bugs, checking CI health every night, or watching Linear for blocked tickets. Several Bots can work together in Slack: in the page's demo a QA Bot finds a bug, hands it to a Developer Bot, then retests the fix while a PM Bot reports progress. Six templates ship with the launch (Software Factory, Android Engineer, Chief of Staff, Latency Optimizer, Product Engineer, QA Engineer). Bilt's VP of Engineering says its Bots merged about 1,600 pull requests in one week. The page lists enterprise security controls but no pricing.

### What changes
The wiki already covers Devin's parent/child products (Oncall, Security Swarm, Dynamic Workflows) and lists Grok Bot, Claude Tag and ChatGPT dots as the AI-teammate products.

- **Devin** gains a short Devin Bots section at the top of Current status and one line in its opening paragraph. A Recent-changes entry is added, and the oldest entry (Security Swarm, 2 July) moves to history because the list is at its cap of 10. Page date moves to 23 November. The page ends just over its 1,500-word ceiling but within the 10% tolerance, so no split is needed.
- **State of Agents** rewrites Devin's Agent orchestration line to lead with Devin Bots, keeping the Oncall and Security Swarm fan-out as the second half. A Recent-changes entry is added and the oldest (Pi, 6 October) moves to history. Page date moves to 23 November.
- New source page `sources/articles/devinai-bots.md`.

The multi-agent coordination page is left alone, because the product page describes what users see, not a new coordination method.

### What to weigh
The product page has no publication or launch date, so 23 November 2026 (the fetch date) is used for every date in the drafts. The other call is scope: Grok Bot and Claude Tag have their own pages, but Devin Bots goes on the existing Devin page because the source is thin. The open question covers that choice.

## Intended changes

- [ ] **Update** `wiki/tools/devin.md` — add Devin Bots section and a sentence in the opening paragraph; `as_of` and Current status stamp to 2026-11-23; add source id and link; adds one Recent-changes entry dated 2026-11-23
- [ ] **Spill** `wiki/tools/devin.md` → `wiki/history/tools/devin.md` — oldest Recent-changes entry (currently 2026-07-02, Security Swarm) moves to history
- [ ] **Update** `wiki/state-of/agents.md` — rewrite Devin's Agent orchestration line; `as_of` to 2026-11-23; add source id; adds one Recent-changes entry dated 2026-11-23
    > **Before:** `- [Devin](../tools/devin.md) — Cognition; parent/child fan-out across products: Oncall Responders (successor to Auto-Triage) dispatch fresh-context investigations from an alert stream, and Security Swarm (Agentic MapReduce) applies the same pattern to vulnerability discovery and fix PRs *(as of 2026-10-19)*`
    > **After:** `- [Devin](../tools/devin.md) — Cognition; Devin Bots are persistent AI teammates that split a goal across parallel Devin sessions, each on its own VM, until the PRs are mergeable, reachable by text, Slack or phone; Oncall Responders and Security Swarm use the same parent/child fan-out *(as of 2026-11-23)*`
- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — oldest Recent-changes entry (currently 2026-10-06, Pi) moves to history
- [ ] **Create** `wiki/sources/articles/devinai-bots.md` — source summary

## Page drafts

### wiki/tools/devin.md (updated)

Frontmatter changes:

```
as_of: 2026-11-23
sources: [...existing..., devinai-bots]
```

Opening paragraph (replaces the current one):

```
Cognition's autonomous coding agent, initially positioned as one of the first "fully autonomous software engineer" agents. Now expanding into persistent operational roles: Devin Oncall (generally available October 2026) investigates and mitigates production alerts and incidents, succeeding Auto-Triage (May 2026), Cognition's first always-on deployment; Devin Bots (November 2026) run teams of Devins. Cognition valued at $25B (May 2026).
```

Current status heading plus new first subsection (inserted directly above `### Devin Oncall`):

```
## Current status (as of 2026-11-23)

### Devin Bots

- **Devin Bots (November 2026):** an engineering-focused AI teammate, like [Grok Bot](grok-bot.md) or [Claude Tag](claude-tag.md). A Bot splits a goal across parallel Devin sessions, each on its own VM, until every PR is mergeable. Users reach it by text, Slack or phone; it brings back only approvals, blockers and decisions.
- Bots run on schedules and triggers (Slack channels, nightly CI, Linear blockers) and hand work to one another, e.g. a QA Bot passing a bug to a Developer Bot. Templates include Software Factory, QA Engineer and Latency Optimizer.
- Bilt reports about 1,600 PRs merged in one week. No pricing published.
```

Recent changes — adds one entry at the top; the oldest entry (2026-07-02) spills to history:

```
- [2026-11-23] Devin Bots launched: persistent AI teammates that split a goal across parallel Devin sessions on separate VMs, reachable by text, Slack or phone, with schedules, triggers and bot-to-bot handoff.
```

Sources — appends one link:

```
- [Cognition — Devin Bots product page](../sources/articles/devinai-bots.md)
```

### wiki/history/tools/devin.md (updated)

Appended under the existing `## Archived from current page on 2026-11-23` block (open a new block with that header if the apply date differs):

```
- [2026-07-02] Cognition shipped Devin Security Swarm for parallel vulnerability discovery, sandbox reproduction, exploitability validation, and fix PRs.
```

### wiki/state-of/agents.md (updated)

Frontmatter changes:

```
as_of: 2026-11-23
sources: [...existing..., devinai-bots]
```

Agent orchestration, Devin line (replaces the current line in place):

```
- [Devin](../tools/devin.md) — Cognition; Devin Bots are persistent AI teammates that split a goal across parallel Devin sessions, each on its own VM, until the PRs are mergeable, reachable by text, Slack or phone; Oncall Responders and Security Swarm use the same parent/child fan-out *(as of 2026-11-23)*
```

Recent changes — adds one entry at the top; the oldest entry (2026-10-06) spills to history:

```
- [2026-11-23] Cognition launched Devin Bots, joining Grok Bot, Claude Tag and ChatGPT dots in the AI-teammate category: a persistent Bot splits a goal across parallel Devin sessions and brings only approvals, blockers and decisions back to the user. Devin's Agent orchestration line now leads with it.
```

### wiki/history/state-of/agents.md (updated)

Appended under the existing `## Archived from current page on 2026-11-23` block (open a new block with that header if the apply date differs):

```
- [2026-10-06] Added [Pi](../../tools/pi.md) to Agent frameworks: Pi 1.0 and Pi Durable (checkpointed, crash-resuming harness on Bun or Cloudflare Durable Objects).
```

### wiki/sources/articles/devinai-bots.md (new)

```
---
title: Cognition — Devin Bots product page
type: source
source_type: article
source_file: raw/articles/2026-11-23-devinai-bots.md
url: https://devin.ai/bots
ingested: 2026-11-23
domains: [agents, coding]
---

# Cognition — Devin Bots product page

Cognition's launch page for Devin Bots, its AI-teammate product. A Bot is a persistent manager agent: given a goal, it breaks the work down, runs parallel Devin sessions (each on its own cloud machine) until their pull requests are ready to merge, and asks the user only for approvals, blockers and decisions. Users reach it by text, Slack, phone call or group chat. Bots also act on schedules and triggers and can coordinate with one another in Slack. The page carries no publication date; the fetch date (2026-11-23) is used.

## Influenced pages
- [Devin](../../tools/devin.md) — new Devin Bots section and opening-paragraph mention
- [State of Agents](../../state-of/agents.md) — Devin's Agent orchestration line now leads with Devin Bots

## Key claims extracted
- A Devin Bot breaks a goal into tasks and runs parallel Devin sessions, each on its own cloud VM, until each PR is ready to merge
- Reachable by text, Slack, phone call, or group chat; a "Needs you" queue surfaces approvals, blockers and decisions for one-click handling
- Schedules and triggers: e.g. watch a Slack channel for customer issues, verify CI health nightly, monitor Linear for blockers
- Bots coordinate with each other (demo: QA Bot finds a bug, Developer Bot fixes it, QA Bot retests, PM Bot reports in Slack)
- Built on Devin's existing stack: codebase understanding, a cloud computer per agent, Devin Review, automated browser testing
- Launch templates: Software Factory, Android Engineer, Chief of Staff, Latency Optimizer, Product Engineer, QA Engineer
- Customer quotes: Bilt says its Bots merged about 1,600 PRs in a week; Fireworks AI says productivity tripled; Decagon and Reducto describe it as engineering-focused rather than a calendar/email summarizer; it ran as a beta before launch
- Security: per-session VM, zero data retention with model providers, audit logs, RBAC/SSO/SCIM/OIDC, private networking; no pricing published
```

## Schema / vocabulary additions

None.

## Open questions
- Devin Bots is drafted as a section of the Devin page. Grok Bot and Claude Tag each have their own `tools/` page. Should Devin Bots get its own `tools/devin-bots.md` instead (with a one-line pointer from Devin and its own leader line on State of Agents)? Assumed no for now, since a single product page is thin evidence for a new entity page.
	- Yes, own page
