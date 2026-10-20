---
type: proposal
source: raw/newsletters/2026-09-25-copilot-gets-a-seat-in-the-org-chart.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Microsoft relaunches Copilot with Autopilot persistent agents

## Summary

### In short
Microsoft's bet for workplace agents is that existing enterprise permissions make them safe, and the first hands-on report shows those same permissions stop ordinary tasks. At a 23 September launch, Microsoft merged its chat apps into one Copilot with Home, Code and Autopilot tabs; Autopilot agents are named, appear in the org chart under their owner, and run on usage credits. On the demo floor, Copilot found both files for a Word-to-Excel move but lacked permission to edit the workbook. This updates **Microsoft Copilot**, its **State of Agents** line, and the company-specific evals guidance. To weigh: the evals addition goes beyond the pages the triage named.

[[#Open questions|Open questions: none.]]

### The source
Ryan Sloan, a Seattle data scientist who writes about AI measurement, reported for Every from Microsoft's Redmond launch on Wednesday 23 September 2026; the piece went out on 25 September. Microsoft replaced its separate consumer and work chat apps with one Copilot app. Home puts chat, delegated tasks and Word, Excel and PowerPoint in one place with shared context. Code lets non-developers build small apps and share them inside secure environments. Autopilot is a persistent agent you give a goal and leave running. It draws on the last 30 days of your work, your place in the org chart and your calendar, keeps private memories of your preferences, and works under a name you choose, such as "Dot (Ryan's Autopilot)", which colleagues can tag in Teams. It can run Routines such as a daily briefing. Autopilot is off by default, billed in usage credits, and features roll out in previews over the coming months.

Sloan's test off-script went less well: Copilot found both files for a Word-to-Excel table move but said it lacked permission to edit the workbook, and a similar restriction blocked a Chat-to-Code handoff. Satya Nadella called the AI agent "the new massive insider risk". Microsoft spent much of the event on evaluation: it runs about 16,000 internal evals, each built by domain experts from a common workflow seen in usage data, and Lamanna said successful customers have the person who does the job build the eval, "embrace the red" (a failing test shows what to fix), and measure how humans do the job today so the agent has a baseline to beat.

### What changes
The wiki's Copilot page dates from June and describes Autopilot only as the hosted runtime announced at Build; nothing records the one-app relaunch.

- **Microsoft Copilot** gains the relaunch at the top of Current status, the Autopilot bullet is rewritten from "hosted runtime" to the persistent, org-chart-visible agent, the June caveats about thin independent evidence give way to the permission-friction finding, and one Recent-changes entry is added. Page date moves to 25 September.
- **State of Agents** rewrites the Copilot line under Agent orchestration and adds one Recent-changes entry; the list is at its cap of 10, so the oldest entry (8 July) spills to history.
- **Evals for workflow and task agents** gains one Evidence-from-practice bullet on Microsoft's internal eval set and its customer eval practice, plus a Recent-changes entry. Its page date stays at 17 October, which is newer.
- One new source page for Sloan's article.

### What to weigh
The launch date (23 September) comes from "on Wednesday" in a piece emailed 25 September; the wiki uses the publication date. Autopilot was already named on the Copilot page as Build's hosted runtime; this proposal treats the September Autopilot as the same product line now exposed as a user-facing tab, not a separate product, and does not create a page for it. The update to Evals for workflow and task agents is a scope addition beyond the pages the triage named; decline that item if the article's eval practice is too thin to carry there.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/microsoft-copilot.md` — relaunch, Autopilot rewrite, caveats, adds one Recent-changes entry dated 2026-09-25 (list goes 4 → 5, under cap), merges source id, `as_of` → 2026-09-25

- [ ] **Update** `wiki/state-of/agents.md` — rewrite the Microsoft Copilot leader line; adds one Recent-changes entry dated 2026-09-25; merges source id into frontmatter
    > **Before:** `- [Microsoft Copilot](../tools/microsoft-copilot.md) — Microsoft; agentic default mode inside Word, Excel, and PowerPoint; Copilot Cowork reached GA in June 2026 and Microsoft Autopilot launched as a hosted long-running agent runtime *(as of 2026-06-17)*`
    > **After:** `- [Microsoft Copilot](../tools/microsoft-copilot.md) — Microsoft; one Copilot app (Home, Code, Autopilot) since September 2026; Autopilot agents are named, persistent, and sit in the org chart under their owner, with enterprise permissions as both safeguard and blocker *(as of 2026-09-25)*`

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — spills the oldest Recent-changes entry (currently one of the two dated 2026-07-08) to keep the cap of 10

- [ ] **Update** `wiki/training/evals-for-agentic-work.md` — adds one Evidence-from-practice bullet, one Recent-changes entry dated 2026-09-25 (2 → 3 entries), merges source id; `as_of` stays 2026-10-17 (newer)

- [ ] **Create** `wiki/sources/newsletters/every-copilot-seat-in-org-chart-2026-09-25.md` — source summary

## Page drafts

### wiki/tools/microsoft-copilot.md (updated)

Frontmatter fields changed:

```
as_of: 2026-09-25
sources: [microsoft-copilot-agent-mode-office, microsoft-word-legal-agent, copilot-cowork-ga-june-2026, ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026, every-copilot-seat-in-org-chart-2026-09-25]
```

Intro paragraph and Current status (replace both):

```
# Microsoft Copilot

Microsoft's assistant surface across Microsoft 365. Since September 2026 it is one Copilot app with three tabs: Home (chat plus Word, Excel and PowerPoint with shared context), Code (non-developers build and share small apps), and Autopilot (persistent, goal-driven agents that sit in the org chart). Its pitch is that the documents, conversations and permissions an enterprise agent needs already live in Microsoft 365.

## Current status (as of 2026-09-25)

- **One Copilot app (launched 2026-09-23):** replaces the separate consumer and work chat apps; features roll out in previews and the early-access program over the coming months
- **Autopilot** is now the user-facing persistent agent: it draws on the last 30 days of work, the org chart and the calendar, keeps private memories of preferences and corrections, works under a user-given name (e.g. "Dot (Ryan's Autopilot)") that colleagues can tag in Teams, and runs Routines such as daily briefings; shown "reporting" to its owner in the org chart; off by default, billed in usage credits. (Microsoft first announced Autopilot at Build in June as a hosted long-running agent runtime.)
- Office inside Copilot holds context across apps: Copilot knows which document and slide the user is on
- Agentic mode in Word, Excel, and PowerPoint has been GA and the default since April 2026; [Microsoft Word Legal Agent](microsoft-word-legal-agent.md) is a domain-specific example (contract review with playbook redlines, Frontier program)
- **Copilot Cowork GA (June 2026):** available to all Microsoft 365 users with model choice and usage-based billing; Microsoft claims 30-40% cheaper per prompt than Claude Cowork
- **MAI-Code-1-Flash** powers GitHub Copilot and VS Code since Build (June 2026); Microsoft may also explore hosted DeepSeek variants as cheaper backends
- Microsoft runs about 16,000 internal evals built from common workflows and pushes customers toward company-specific evals (see [Evals for workflow and task agents](../training/evals-for-agentic-work.md))
```

Weaknesses / caveats (replace section):

```
## Weaknesses / caveats

- Enterprise permissions cut both ways: in a hands-on test at launch, Copilot found both files for a Word-to-Excel table move but lacked permission to edit the workbook, and a Chat-to-Code handoff was blocked the same way; whether it works on day one depends on the customer's IT setup
- Nadella calls the AI agent "the new massive insider risk"; Autopilot's governance (own permissions, org-chart visibility) is Microsoft's answer, not yet proven at scale
- Always-on agents spend tokens around the clock; Microsoft says Autopilot has to "clear a higher bar" than on-demand tools to justify the cost
```

Recent changes (adds one entry at the top; list 4 → 5):

```
- [2026-09-25] One Copilot app launched 2026-09-23 with Home, Code and Autopilot tabs; Autopilot agents are named, persistent, org-chart-visible and usage-billed; hands-on test hit permission blocks on cross-app tasks
```

Sources (adds one line):

```
- [Every — Copilot Gets a Seat in the Org Chart](../sources/newsletters/every-copilot-seat-in-org-chart-2026-09-25.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter: append `every-copilot-seat-in-org-chart-2026-09-25` to `sources:`. `as_of` stays at the live value (2026-10-19, newer).

Agent orchestration line (replace):

```
- [Microsoft Copilot](../tools/microsoft-copilot.md) — Microsoft; one Copilot app (Home, Code, Autopilot) since September 2026; Autopilot agents are named, persistent, and sit in the org chart under their owner, with enterprise permissions as both safeguard and blocker *(as of 2026-09-25)*
```

Recent changes (insert in date order, between the 2026-10-09 and 2026-09-09 entries):

```
- [2026-09-25] Microsoft relaunched Copilot as one app with an Autopilot tab: persistent, user-named agents that appear in the org chart, joining OpenAI's dots, Meta Muse and Grok Bot in the always-on agent category.
```

### wiki/history/state-of/agents.md (updated)

Append under the existing `## Archived from current page on <apply date>` block (open a new block if the apply date differs from the last header):

```
- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

(The actual spill is whichever entry is oldest at apply time.)

### wiki/training/evals-for-agentic-work.md (updated)

Frontmatter: append `every-copilot-seat-in-org-chart-2026-09-25` to `sources:`.

Evidence from practice (append one bullet):

```
- **Microsoft: thousands of workflow evals, built by the people who do the work.** At the September 2026 Copilot relaunch, Microsoft said it runs about 16,000 internal evals, each a common task found in usage data and built by domain experts, and builds more with customers. Charles Lamanna's pattern for customers who succeed: the person who does the job daily builds the eval; they "embrace the red", treating a failing test as the to-do list and writing a harder one once it passes; and they measure the current human baseline (error rate, contract turnaround time) before the agent tries, so it has a real number to beat.
```

Recent changes (adds one entry, placed below the 2026-10-17 entry):

```
- [2026-09-25] Added Microsoft's eval practice from the Copilot relaunch: ~16,000 internal workflow evals, practitioner-built evals, "embrace the red", and measuring the human baseline first.
```

Sources (adds one line):

```
- [Every — Copilot Gets a Seat in the Org Chart](../sources/newsletters/every-copilot-seat-in-org-chart-2026-09-25.md)
```

### wiki/sources/newsletters/every-copilot-seat-in-org-chart-2026-09-25.md (new)

```
---
title: 'Every — Copilot Gets a Seat in the Org Chart'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-25-copilot-gets-a-seat-in-the-org-chart.md
url: https://every.to/p/copilot-gets-a-seat-in-the-org-chart
published: 2026-09-25
ingested: 2026-10-20
domains: [agents, training]
---

# Every — Copilot Gets a Seat in the Org Chart

Ryan Sloan's report from Microsoft's Redmond launch (2026-09-23), where Microsoft replaced its consumer and work chat apps with one Copilot app (Home, Code, Autopilot). Covers Autopilot persistent agents that appear in the org chart, a hands-on demo where permissions blocked cross-app tasks, and Microsoft's push for company-specific evals.

## Influenced pages

- [Microsoft Copilot](../../tools/microsoft-copilot.md) — one-app relaunch, Autopilot rewrite, permission-friction caveat
- [State of Agents](../../state-of/agents.md) — Copilot leader line, Recent changes
- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — Microsoft eval practice in Evidence from practice

## Key claims extracted

- Launched 2026-09-23: one Copilot app replacing separate consumer and work chat apps; tabs Home, Code, Autopilot; rolling out in previews over the coming months
- Autopilot draws on the last 30 days of work, org chart and calendar; private memories; user-given name visible to colleagues, taggable in Teams; Routines such as daily briefings; shown "reporting" to its owner in the org chart
- Autopilot is off by default and billed in usage credits; Lamanna envisions one Autopilot per person and per group
- Lamanna's Autopilot "Apollo" has the same Outlook access as his executive assistant
- Nadella: "The new massive insider risk is the AI agent"
- Hands-on: Copilot found both files for a Word-to-Excel table move but lacked permission to edit the workbook; a Chat-to-Code handoff was blocked similarly
- Microsoft runs ~16,000 internal evals built by domain experts from common workflows; successful customers have practitioners build evals, "embrace the red", and measure the human baseline first
```

## Schema / vocabulary additions

None.

## Open questions

None.
