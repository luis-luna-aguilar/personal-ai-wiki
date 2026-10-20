---
type: proposal
source: raw/articles/2026-10-20-claudecom-blog-building-effective-human-agent-teams.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Anthropic — "Lessons from Anthropic on building effective human-agent teams"

## Summary

### In short
Shared team agents fail on norms more than on technology: Anthropic says its human-agent teams work only when everything is written down where agents can read it, every human and agent has a named role, humans set a written north star, and autonomy widens per task type as reliability is shown. One team got agents to 500 independent bug fixes this way. The proposal updates Multiplayer AI, Claude Tag and Agent autonomy and governance, plus a source page. One reason to hesitate: the publication date is inferred, and the trust-building lesson overlaps the governance page's existing trust-battery and promotion bullets.

[[#Open questions|Open questions: 1 to answer.]]

### The source
Kristen Swanson of Anthropic's Education team wrote this Claude blog post, which reached the wiki through an early-October forward. It describes "multiplayer agents": agents with their own credentials, memory and skills that work with many people at once inside Slack, through Anthropic's Claude Tag product, instead of one person chatting with one agent.

The post gives four lessons from several months of internal use. First, work in public: an agent knows only what a team writes where it can search, so Anthropic sets access with a handful of workspace-wide security boundaries rather than deciding document by document, and defaults new channels to public. Second, keep one roster of humans and agents with named roles, written as skill files so others can stand up agents of the same type; one engineering team added a release-manager agent when a project grew. Without clear roles, the post warns, people run fleets of personal agents on the side and duplicate work. Third, humans write a north star goal and pick which agents may propose new work. Fourth, build trust over time: review everything by hand at first, add a verifier agent, ask for a weekly "lessons & missteps" report, and widen autonomy per task type. One leader's agents ended up handling 500 bug fixes, and were coached to batch questions because human attention is scarce. Private work still goes through a direct message to Claude or through Claude.ai and Cowork.

### What changes
The wiki has a Multiplayer AI concept built from one outside manifesto, a Claude Tag page frozen at its June beta launch, and a governance page whose trust mechanisms come from Every's Claudie agent.

- **Multiplayer AI** gains a Current-status bullet giving Anthropic's four norms as the first operating account from a lab, mapped to the manifesto's principles. One Recent-changes entry; page date moves to 10 October.
- **Claude Tag** gains a Current-status bullet on how Anthropic runs its own teams on it (roles in skill files, private work by direct message, the 500-bug-fix result). One Recent-changes entry; page date moves to 10 October.
- **Agent autonomy and governance** gains one Governance-patterns bullet on widening autonomy per task type, with verifier agents, weekly misstep reports and attention-budget rules. One Recent-changes entry (5 entries, no spill); page date stays at 11 October.
- New source page `wiki/sources/articles/anthropic-human-agent-teams-2026-10.md`.

### What to weigh
The raw file has no publication date. It arrived in the 1–10 October digest, so the drafts use 10 October as an upper bound rather than the 20 October fetch date. The governance bullet sits next to the existing "promotion only after reliability" and "trust battery" bullets; the draft keeps it separate because it adds per-task-type scoping and the attention rules, which neither covers.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/multiplayer-ai.md` — add one bullet at the end of `## Current status`, rename that heading to `(as of 2026-10-10)`; adds one Recent-changes entry dated 2026-10-10 (live list has 1, no spill); add one `## Related` line; append source id and link; `as_of` 2026-09-14 → 2026-10-10
    > See draft below

- [ ] **Update** `wiki/tools/claude-tag.md` — add one bullet at the end of `## Current status`, rename that heading to `(as of 2026-10-10)`; adds one Recent-changes entry dated 2026-10-10 (live list has 1, no spill); append source id and link; `as_of` 2026-06-24 → 2026-10-10
    > See draft below

- [ ] **Update** `wiki/training/agent-autonomy-and-governance.md` — add one bullet to `## Governance patterns`, after "Trust battery with judge agent"; adds one Recent-changes entry dated 2026-10-10 (live list has 4, cap 10, no spill); append source id and link; `as_of` stays 2026-10-11
    > See draft below

- [ ] **Create** `wiki/sources/articles/anthropic-human-agent-teams-2026-10.md` — source summary

## Page drafts

### wiki/concepts/multiplayer-ai.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-10
sources: [multiplayer-ai-manifesto-2026-09-14, anthropic-human-agent-teams-2026-10]
```

`## Current status (as of 2026-09-14)` → `## Current status (as of 2026-10-10)`; append one bullet at the end of the section:

```
- **A lab's own operating account.** Anthropic's Education team (Oct 2026) describes "multiplayer agents", agents with their own credentials, memory and skills that work with many people at once inside Slack via [Claude Tag](../tools/claude-tag.md), and four norms its teams adopted: work in public, with access set by a few workspace-wide security boundaries rather than per-document sharing ("if it's not written down and accessible, it doesn't exist" for an agent); keep one roster of humans and agents with named roles, defined in skill files; have humans write a north star and choose which agents may propose new work; and widen autonomy per task type as reliability is shown (see [Agent autonomy and governance](../training/agent-autonomy-and-governance.md)). This is the manifesto's "work with the door open" and "people are not routers" in practice. The post's warning: without shared roles, people run fleets of personal agents on the side, duplicating work and fracturing team context.
```

`## Recent changes` — insert above the existing entry:

```
- [2026-10-10] Added Anthropic's four norms for human-agent teams (work in public, a shared roster with named roles, a human-set north star, autonomy per task type) as a lab's own operating account.
```

`## Related` — append one line:

```
- [Claude Tag](../tools/claude-tag.md) — Anthropic's Slack-native shared agent, the surface Anthropic's own human-agent teams run on
```

`## Sources` — append one line:

```
- [Lessons from Anthropic on building effective human-agent teams](../sources/articles/anthropic-human-agent-teams-2026-10.md)
```

### wiki/tools/claude-tag.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-10
sources: [claude-tag-slack-agent-2026-06, anthropic-human-agent-teams-2026-10]
```

`## Current status (as of 2026-06-24)` → `## Current status (as of 2026-10-10)`; append one bullet at the end of the section:

```
- Anthropic runs its own human-agent teams on it: agents with their own credentials, memory and roles defined in skill files share Slack threads with people, while private work goes to a direct message with @Claude or to Claude.ai and Cowork with personal MCP connectors. One internal engineering team reports agents handling 500 bug fixes independently after autonomy was widened per task type. Anthropic points to agent teams in Claude Code as the other way to build such agents. See [Multiplayer AI](../concepts/multiplayer-ai.md).
```

`## Recent changes` — insert above the existing entry:

```
- [2026-10-10] Anthropic published how its own teams run human-agent teams on Claude Tag (public-by-default context, role rosters in skill files, per-task-type autonomy; 500 independent bug fixes on one team).
```

`## Sources` — append one line:

```
- [Lessons from Anthropic on building effective human-agent teams](../sources/articles/anthropic-human-agent-teams-2026-10.md)
```

### wiki/training/agent-autonomy-and-governance.md (updated)

Frontmatter `sources:` (append one id; `as_of` stays 2026-10-11):

```
sources: [agents-evals-deep-research, mckinsey-agentic-org, ramp-ai-adoption-playbook, ai-for-boring-businesses, token-tightening-ai-finops-2026-06, every-ai-sandwich-april-2026, every-cheap-competence-after-automation-2026-05, every-33-questions-executives-2026-08-28, every-ai-adoption-levels, karpathy-capability-funnel-2026-10-11, satyanadella-models-as-insider-risks-2026-10-10, anthropic-human-agent-teams-2026-10]
```

`## Governance patterns` — insert one bullet directly after "Trust battery with judge agent":

```
- **Widen autonomy per task type, with verification built in.** Anthropic's teams (Oct 2026) track which kinds of task each agent has earned autonomy on and widen scope one type at a time after repeated successes. They review all agent work by hand at first and turn that feedback into verification checklists, have a separate verifier agent check the doer's work, and ask agents for a weekly "lessons & missteps" report. As agents grow more independent, they are coached to treat human attention as scarce: batch questions into one pass, restate key context, limit how many items a person sees at once; some teams cap agent output per day so review stays sustainable. Retest tasks when models change, since old guardrails can hold a stronger model back. One engineering team reached agents handling 500 bug fixes independently this way.
```

`## Recent changes` — insert between the 2026-10-11 entry and the existing 2026-10-10 entry (5 entries after insert, no spill):

```
- [2026-10-10] Added "Widen autonomy per task type, with verification built in" from Anthropic's lessons on human-agent teams (verifier agents, weekly lessons-and-missteps reports, human-attention budgets).
```

`## Sources` — append one line:

```
- [Lessons from Anthropic on building effective human-agent teams](../sources/articles/anthropic-human-agent-teams-2026-10.md)
```

### wiki/sources/articles/anthropic-human-agent-teams-2026-10.md (new)

```
---
title: Lessons from Anthropic on building effective human-agent teams
type: source
source_type: article
source_file: raw/articles/2026-10-20-claudecom-blog-building-effective-human-agent-teams.md
url: https://claude.com/blog/building-effective-human-agent-teams
ingested: 2026-10-20
domains: [agents, training]
---

# Lessons from Anthropic on building effective human-agent teams

A Claude blog post by Kristen Swanson (Anthropic Education team) on how Anthropic runs teams where "multiplayer agents" (agents with their own credentials, memory and skills, working with many people at once) sit in Slack alongside humans via Claude Tag. It gives four lessons from several months of internal use and five questions to ask before building such a team. No publication date appears in the article; it reached the wiki through a forward in the 1–10 October 2026 digest, so derived pages use 2026-10-10 as an upper bound.

## Influenced pages
- [Multiplayer AI](../../concepts/multiplayer-ai.md) — Anthropic's four norms as a lab's own operating account
- [Claude Tag](../../tools/claude-tag.md) — how Anthropic runs its own teams on the product
- [Agent autonomy and governance](../../training/agent-autonomy-and-governance.md) — per-task-type autonomy with verification and attention budgets

## Key claims extracted
- Work in public: for an agent, "if it's not written down and accessible, it doesn't exist." Anthropic sets access by a handful of workspace-wide security boundaries instead of per-item sharing, defaults channels to public, and writes meeting notes and artifacts for agents to find.
- Private work goes through a direct message to @Claude in Claude Tag, or Claude.ai and Cowork with personal MCP connectors.
- Teams keep one roster of humans and agents with named roles (data analysis, design standard, research synthesis), defined in skill files; one engineering team added a release-manager agent as its project grew. Without clear roles, people run side fleets of personal agents that duplicate work.
- Humans write a north star and choose which agents may proactively propose new work; an agent on an internal tools team proposed onboarding error-message copy changes that measurably raised onboarding success the next week.
- Trust is built per task type: manual review first, verification checklists, a separate verifier agent ("Doer-Verifier" harness), weekly "lessons & missteps" reports, and scope widened after repeated successes. Engineers have dispatched agents to handle 500 bug fixes independently.
- Agents are coached to treat human attention as scarce (batch questions, restate context, limit items per person); some teams cap agent work per day so review stays sustainable. Retest tasks when models change, since older guardrails can constrain a stronger model.
- Anthropic points to agent teams in Claude Code and to Claude Tag as the ways to start building multiplayer agents.
```

## Schema / vocabulary additions

None.

## Open questions

- The article carries no date. Is 10 October (the end of the digest window it arrived in) acceptable for `as_of`, or should the pages use the 20 October fetch date?
