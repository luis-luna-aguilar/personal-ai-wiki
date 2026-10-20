---
type: proposal
source: raw/tweets/2026-09-09-undefinedki-2095876609689498067.md
triage: proposals/triage/2026-10-19-raw-orphans-sweep.md
status: pending
created: 2026-10-20
---

# Proposal: "How to turn AI into a whole team that runs your business" — Yarchi (Viktor)

## Summary

### In short
Agents can run a small business's recurring work only after the owner does the non-AI groundwork: one lane per job in its own channel, context written once as a pinned job description, a running file of corrections, and a fixed line between reversible work (runs alone) and irreversible work (waits for a person). Yarchi says the setup took an afternoon. The proposal adds a short "Running standing agent lanes" section to AI delegation management, plus a source page. One reason to hesitate: two existing bullets on that page already cover recurring corrections and specialist agent rosters, so part of this restates them.

[[#Open questions|Open questions: 1 to answer.]]

### The source
On 4 September 2026 the X writer Yarchi (@undefinedKi) published a long X Article, marked as a paid partnership with Viktor.com, a product that joins Slack or Teams as an "AI employee". The piece is a setup guide for a one-person services business that wants the work it never gets to (client status, lead research, invoices, reporting) to happen without the owner starting it each time.

It runs in five steps, and the first three involve no AI at all: split the business into lanes (clients, leads, delivery, reporting, finance), each in its own channel; give each lane a pinned message written like a job description, plus a shared "rulings file" of one-line corrections that the author calls the highest-leverage part; and sort every action once into reversible and irreversible, removing the capability where a rule matters (the leads lane has no sending tool). The last two steps are a brief per lane and an ordered schedule. A first-day report on Viktor is mostly refusals: it would not invent missing data or answer a question the data could not support.

### What changes
The delegation page already covers spec-first delegation, layered access control for Every's always-on Claudie agent, and a solo builder running a roster of named Codex specialists, but it has no step-by-step setup for standing, scheduled agents.

- **AI delegation management** gains a section, "Running standing agent lanes", after Proven patterns: one short framing paragraph and five bullets (lanes, pinned context, rulings file, approval line, schedules). The first-day anecdotes stay on the source page. One Recent-changes entry dated 4 September is added (6 entries, no spill). The page date stays at 19 October, since the source is older than the page's newest claim.
- New source page `wiki/sources/tweets/yarchi-ai-team-runs-business-2026-09.md`.

### What to weigh
The rulings file is a concrete form of the existing "turn recurring corrections into reusable instructions" bullet, and one-lane-per-job overlaps the specialist-roster bullet. The draft keeps them as one setup sequence rather than folding each step into an older bullet, because the order of the steps is the point. The scope choice is the delegation page rather than Multiplayer AI: the setup is one owner running agents, not a team sharing sessions, even though Viktor is one of the platforms the multiplayer manifesto names.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-delegation-management.md` — insert a new `## Running standing agent lanes` section between `## Proven patterns` and `## Raising the ambition of a delegation`; adds one Recent-changes entry dated 2026-09-04 (live list has 5, cap 10, no spill); append source id `yarchi-ai-team-runs-business-2026-09` to frontmatter `sources:` and one link to `## Sources`; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Create** `wiki/sources/tweets/yarchi-ai-team-runs-business-2026-09.md` — source summary

## Page drafts

### wiki/training/ai-delegation-management.md (updated)

Frontmatter `sources:` (append one id; `as_of` unchanged):

```
sources: [management-as-ai-superpower-2026-07, andy-matuschak-agent-loop-tempo-2026-07, design-layer-framework-2026-08-04, vibe-coded-security-risk-2026-08-10, securing-ai-employee-guide-2026-08-14, next-era-of-great-work-2026-08-16, engineering-team-cost-of-codex-2026-08-19, rieseberg-how-to-be-more-ambitious, yarchi-ai-team-runs-business-2026-09]
```

New section, inserted after the last bullet of `## Proven patterns` and before `## Raising the ambition of a delegation`:

```
## Running standing agent lanes

Standing agents (ones that wake up on a schedule and work without being started) need groundwork before any prompt is written. Yarchi's setup for a one-person services business (Sep 2026, written as a paid partnership with the AI-employee product Viktor) runs in five steps; the first three involve no AI, and skipping them is what the author says makes such setups fall apart in the second week.

- **One lane, one job, one channel.** Split the business into lanes (for a services firm: clients, leads, delivery, reporting, finance), each in its own Slack or Teams channel, rather than one assistant with one enormous prompt. The channel history is context nobody has to re-explain.
- **Write the context once, as a job description.** Each lane gets one pinned message: what the business sells and to whom, the named outputs the lane delivers, what gets escalated, and five or six rules that never bend. The last paragraph is always a limit ("never finalise, never send, never mark anything as paid").
- **Keep a rulings file.** One running file where every correction lands as a single line ("cost per booked consultation is the metric, not cost per lead"), read by every lane before it works, so a correction becomes permanent instead of repeated. A concrete form of turning recurring corrections into standing instructions (above).
- **Draw the approval line once.** Reading, researching, drafting and building something in a paused state run without asking; sending, publishing, spending and finalising wait for a person. Where a rule matters, remove the capability instead of relying on the rule: the leads lane has no sending tool connected at all.
- **Schedule before you prompt.** A schedule is one sentence in the brief ("every workday at 8:00"). Order schedules so later ones read earlier output (a lane standup at 7:55 feeds a cross-lane rollup at 8:00), and add the next lane only when the last one produces without being started.
```

`## Recent changes` — insert one entry between the 2026-10-19 and 2026-08-19 entries (6 entries after insert, no spill):

```
- [2026-09-04] Added "Running standing agent lanes": Yarchi's five-step setup for scheduled agents in a small business (one lane per channel, pinned job-description context, a rulings file, a fixed approval line, ordered schedules).
```

`## Sources` — append one line:

```
- ["How to turn AI into a whole team that runs your business" — Yarchi](../sources/tweets/yarchi-ai-team-runs-business-2026-09.md)
```

### wiki/sources/tweets/yarchi-ai-team-runs-business-2026-09.md (new)

```
---
title: '"How to turn AI into a whole team that runs your business" — Yarchi'
type: source
source_type: tweet
source_file: raw/tweets/2026-09-09-undefinedki-2095876609689498067.md
url: https://x.com/undefinedKi/status/2095876609689498067
published: 2026-09-04
ingested: 2026-10-20
domains: [agents, training]
---

# "How to turn AI into a whole team that runs your business" — Yarchi

An X Article by Yarchi (@undefinedKi), 4 September 2026, marked as a paid partnership with Viktor.com, an "AI employee" that joins Slack or Teams as a workspace member. It is a five-step setup guide for putting a one-person services business's recurring work on agents: split the work into lanes, write each lane's context once, draw an approval line, brief each lane, and schedule it. The author says the first three steps involve no AI and that skipping them is why such setups fail in the second week. It closes with a first-day report from running the setup on Viktor.

## Influenced pages
- [AI delegation management](../../training/ai-delegation-management.md) — new "Running standing agent lanes" section

## Key claims extracted
- One lane, one job, one channel beats one assistant with one enormous prompt; five lanes (clients, leads, delivery, reporting, finance) cover most of a services business.
- Each lane gets one pinned message shaped like a job description: what the business sells, named outputs, what gets escalated, five or six fixed rules, ending with a limit.
- A "rulings file", one line per correction read by every lane before working, is called the highest-leverage part of the setup.
- Reversible actions (read, research, draft, build paused) run alone; irreversible ones (send, publish, spend, finalise, go live) wait for a person. Where a rule matters, remove the capability: the leads lane has no sending tool.
- Schedules are one sentence in a brief and are ordered so later ones read earlier output (standup 7:55, rollup 8:00); add a lane only when the previous one runs unprompted.
- Setup took one afternoon. First-day observations on Viktor: it posted nothing rather than invent missing data, declined to answer a question the data could not support, applied a buried client rule unprompted, delivered a typeset PDF report, and labelled a dashboard "snapshot, not auto-updating".
- The author says large engineering organisations converged on the same three ideas: one job per agent, context outside the conversation, a gate on anything irreversible.
```

## Schema / vocabulary additions

None.

## Open questions

- Should the five steps fold into the existing "turn recurring corrections into reusable instructions" and "roster of named specialist agents" bullets instead of a new section (assumed no: the step order is the useful part)?
