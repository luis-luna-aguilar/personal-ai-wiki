---
type: proposal
source: raw/newsletters/2026-11-12-the-next-two-levels-of-ai-adoption.md
sources:
  - raw/newsletters/2026-11-12-the-next-two-levels-of-ai-adoption.md
  - raw/newsletters/2026-11-15-the-age-of-artisanal-ai-is-coming.md
status: pending
created: 2026-11-24
---

# Proposal: Every's adoption ladder gains Levels 9 (Simulation) and 10 (Multiverse)

## Summary

### In short
Past orchestration, the next step up the adoption ladder is not more delegation but testing strategies before reality does: let several agent teams compete on the same goal, then rerun the competition many times to tell robust strategies from lucky ones. Every's Mike Taylor added these as Levels 9 and 10 to the eight-level framework the wiki carries; his Hacker News simulator shows why a single run can mislead. The proposal extends the ladder on Agent autonomy and governance and adds one data point to AI-simulated human populations. Reason to hesitate: scope, since the levels are a forward-looking proposal, not observed practice.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
In June 2026 Every published "The Eight Levels of AI Adoption", running from Level 1 (ask a chatbot) to Level 8 (a manager agent runs subagents for you). On 12 November Mike Taylor, Every's head of evals, wrote that people reached the top faster than expected, because the Codex and Claude desktop apps make orchestration easy even for non-engineers, and proposed two more levels, first presented at Every's Thesis: 2027 event.

At Level 9, Simulation, you stop designing one plan and design a competition: several orchestrated agent teams pursue the same goal with different strategies, and you define the goal, the scoring rule and the rules of play. Good candidates are problems where trying several approaches is cheaper than guessing wrong, such as growth, pricing or content strategy. Diverse teams need diverse members, which is where Every's colleague clones come in (prompts tuned on a person's past Slack messages or edits). The limits: every team needs reliable orchestration of its own, three competing orchestrators need three times the human attention, and the extra tokens only pay off when a wrong strategy would cost more than a real-world experiment.

At Level 10, Multiverse, you rerun the same competition many times to measure how much of the result was chance. Taylor cites the 2006 Columbia and Santa Fe Institute "music worlds" study, where the same song could hit in one world of listeners and flop in another. His own simulator of nearly 2,000 cloned Hacker News commenters predicted front-page headlines 60% of the time, and the misses came from chance, not bad personas: one extra early upvote sent identical posts down different paths. A strategy that wins 40 of 50 runs is robust; one that wins once may be lucky. His caveat: if the simulation is off, averaging 50 runs gives "a very confident wrong answer," so it works best today on narrow systems such as one social feed or a focus group. A 15 November Every recap restates both levels.

### What changes
The wiki carries the eight-level table and the rule that a higher level is not automatically better; it stops at Level 8.

- **Agent autonomy and governance** gains rows 9 and 10 in the adoption table and a short paragraph on what each level is for and its limits (clones kept to one clause). One Recent-changes entry; page date stays 12 November. Its index line changes "8-level" to "10-level".
- **AI-simulated human populations** gains a practitioner data point: the Hacker News simulator's 60% hit rate and the chance problem behind its misses. Page date moves to 12 November.
- One new source page.

### What to weigh
The colleague-clone results (Dan Lens, KatePass) appear in the essay as Level 9 ingredients; since a clone-focused proposal was declined earlier, the drafts name clones in one clause with no figures.

## Intended changes

- [ ] **Update** `wiki/training/agent-autonomy-and-governance.md` — intro sentence of `## AI adoption and fluency levels` notes the extension; two table rows; one new paragraph after the table's practical rules; add `every-next-two-adoption-levels-2026-11-12` to `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-11-12 (list goes from 8 to 9, no spill); `as_of` stays 2026-11-12
- [ ] **Update** `wiki/trends/synthetic-human-simulation.md` — one new bullet under `## Current signal`; add the source id to `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-11-12 (list has 1, no spill); `as_of` 2026-08-22 → 2026-11-12
- [ ] **Update** `wiki/index.md` — the agent-autonomy-and-governance line says 10-level; the synthetic-human-simulation line's date moves to 2026-11-12
- [ ] **Create** `wiki/sources/newsletters/every-next-two-adoption-levels-2026-11-12.md` — source summary

## Page drafts

### wiki/training/agent-autonomy-and-governance.md (updated)

Frontmatter: append `every-next-two-adoption-levels-2026-11-12` to `sources:`. `as_of` stays `2026-11-12`.

`## AI adoption and fluency levels`, first paragraph, first sentence becomes:

```
Every (Mike Taylor / Laura Entis, June 2026) published an 8-level framework for AI adoption maturity, which its consulting practice also uses as an AI-fluency ladder; Taylor added Levels 9 and 10 in November 2026.
```

Append two rows to the table, after Level 8:

```
| 9 | Simulation | Several orchestrated agent teams pursue the same goal with different strategies and compete under a scoring rule you set. |
| 10 | Multiverse | The same competition is rerun many times to separate strategies that win reliably from ones that won by luck. |
```

Insert after the "Practical rules from the framework" bullets, before "**Where people sit**":

```
**Levels 9 and 10 (Every, November 2026).** Levels 1–8 hand off more work and autonomy; 9 and 10 change how agents explore strategies once orchestration is routine. At Level 9 your job becomes defining the goal, the scoring and the rules of competition, for problems where trying several approaches is cheaper than guessing wrong (growth, pricing, content strategy, engineering problems with more than one solution); diverse teams can be seeded with persona prompts built from colleagues' past messages. At Level 10 you rerun that competition with the same starting conditions and trust only what wins across runs: Taylor's simulator of ~2,000 cloned Hacker News commenters predicted front-page headlines 60% of the time, and its misses came from chance (one extra early upvote sent identical posts down different paths), not from bad personas. Limits he states: both levels are experimental and burn far more tokens; each competing team needs reliable orchestration and its own share of human attention; a bad simulation averaged 50 times gives "a very confident wrong answer," so for now this works on narrow systems such as a single feed or focus group. Check a winning plan with real people before acting on it.
```

`## Recent changes`: insert below the existing 2026-11-12 entry (same date, so it sits second):

```
- [2026-11-12] Extended Every's adoption ladder with Level 9 (Simulation: competing agent teams under a scoring rule) and Level 10 (Multiverse: rerun to filter out luck), with Mike Taylor's limits.
```

`## Sources`: append

```
- [Every — The Next Two Levels of AI Adoption](../sources/newsletters/every-next-two-adoption-levels-2026-11-12.md)
```

### wiki/trends/synthetic-human-simulation.md (updated)

Frontmatter: `as_of: 2026-11-12`; append `every-next-two-adoption-levels-2026-11-12` to `sources:`.

`## Current signal`, append:

```
- **A practitioner's limit (Every, November 2026):** Mike Taylor cloned nearly 2,000 Hacker News commenters as personas; the simulator predicted which headlines reached the front page 60% of the time. The misses were not bad personas but chance: one extra early upvote sent identical posts down different paths in parallel runs, echoing the 2006 Columbia/Santa Fe "music worlds" study. His answer is to rerun a simulation many times and trust only results that hold across runs (Level 10 of Every's [adoption ladder](../training/agent-autonomy-and-governance.md)); a wrong simulation rerun 50 times is still wrong.
```

`## Recent changes`: insert at the top:

```
- [2026-11-12] Added Mike Taylor's Hacker News simulator (60% front-page prediction; misses driven by chance) and the rerun-many-times answer.
```

`## Sources`: append

```
- [Every — The Next Two Levels of AI Adoption](../sources/newsletters/every-next-two-adoption-levels-2026-11-12.md)
```

### wiki/index.md (updated)

In the `training/agent-autonomy-and-governance` line, change "and Every's 8-level adoption/fluency model" to "and Every's 10-level adoption/fluency model (Levels 9–10: simulation, multiverse)". Date unchanged.

In the `trends/synthetic-human-simulation` line, change `*(as_of: 2026-08-22)*` to `*(as_of: 2026-11-12)*`.

### wiki/sources/newsletters/every-next-two-adoption-levels-2026-11-12.md (new)

```
---
title: "The Next Two Levels of AI Adoption — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-12-the-next-two-levels-of-ai-adoption.md
url: https://every.to/also-true-for-humans/the-next-two-levels-of-ai-adoption
published: 2026-11-12
ingested: 2026-11-24
domains: [agents]
---

# The Next Two Levels of AI Adoption — Every

Mike Taylor (Every's head of evals) extends Every's eight-level AI adoption framework with Level 9, Simulation (competing agent teams), and Level 10, Multiverse (rerunning the competition to filter out chance), with example prompts and stated limits. A 15 November Every recap (`raw/newsletters/2026-11-15-the-age-of-artisanal-ai-is-coming.md`) restates both levels.

## Influenced pages

- [Agent autonomy and governance](../../training/agent-autonomy-and-governance.md) — Levels 9 and 10 added to the adoption ladder
- [AI-simulated human populations](../../trends/synthetic-human-simulation.md) — Hacker News simulator data point

## Key claims extracted

- People reached Level 8 (orchestration) faster than expected; desktop apps make orchestration easy for knowledge work
- Level 9: several orchestrated teams with different strategies compete; the human defines goal, scoring and rules
- Level 10: rerun the same competition many times; a strategy that wins 40 of 50 runs is robust
- Hacker News simulator: ~2,000 cloned commenters predicted front-page headlines 60% of the time; one extra early upvote changed outcomes for identical posts
- Cites the 2006 Columbia/Santa Fe "music worlds" study (14,341 people, eight worlds, 48 songs)
- Limits: experimental, far more tokens, each team needs reliable orchestration, a bad simulation averaged many times gives "a very confident wrong answer"; best on narrow systems
```

## Schema / vocabulary additions

None.

## Open questions

None.
