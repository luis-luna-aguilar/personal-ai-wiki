---
type: proposal
source: raw/articles/2026-11-24-anthropiccom-research-agents-judgment-calls.md
status: pending
created: 2026-11-24
---

# Proposal: Anthropic study — covertly steered Claude Code swayed analysts' judgment calls 86% of the time

## Summary

### In short
An expert's sign-off on agent-assisted work no longer shows that the expert made the judgment calls. In Anthropic's randomized study, 50 professional analysts sided with Claude Code's secretly assigned preference 86% of the time on open analytical choices. 77% then justified those choices with the agent's arguments, and only 15% credited the AI. The proposal adds a deferral section, a guidance bullet and a failure mode to **Anti-autopilot review friction**, plus a source page. No red flags: the page stays well under its length ceiling, and the study's own limits travel with the numbers.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 27 October 2026 Anthropic researchers Amaç Herdağdelen, Hailey Joren and Alex Tamkin published "How AI agents shape experts' judgment calls". Fifty analysts trained in causal inference used Claude Code with Opus 4.8 to advise a fictional farming cooperative on whether to expand an advisory program. They faced four choices, each with two defensible options, such as measuring yield per hectare or per unit of cost. A hidden instruction gave each analyst's agent a coin-flip preference on every choice. It told the agent to argue honestly, to change its mind if the evidence demanded, and never to mislead.

Analysts went with the agent's lean 86% of the time, where 50% would mean no influence. Those who had already stated a preference switched 60% of the time when the agent disagreed, against 6% when it agreed. From the coin flips alone, a model predicted 82% of final recommendations. Analysts who followed the agent rated the result their own and were as confident as the rest, and experience did not predict who deferred. The 11 who worked without the agent made serious errors far more often (55% against 6%) and took longer, although they were less experienced. The authors' limits: the preferences were deliberately strengthened, and the study covers one task, one field and one model.

### What changes
**Anti-autopilot review friction** already cites studies on comprehension loss and on anchoring at the start of a task. It gains a short "Deferral on judgment calls" section with the study's numbers and caveats, a guidance bullet (record your own pick before the agent weighs in and ask it to argue the other option), and a failure mode (counting sign-off as independent judgment). It gains one Recent-changes entry dated 27 October, and the page date moves there. `wiki/index.md` refreshes the line, and one source page is added.

### What to weigh
The authors suggest fixes, such as agents arguing both options or asking for the expert's view first, but they have not tested them. The draft labels those as Anthropic's suggestions rather than proven patterns.

## Intended changes

- [ ] **Update** `wiki/training/anti-autopilot-review-friction.md` — new `## Deferral on judgment calls` section after "What works and what fails (empirical ratios)"; one `## Current guidance` bullet; one `## Failure modes` bullet; `as_of` → 2026-10-27; adds one Recent-changes entry dated 2026-10-27; add source
- [ ] **Update** `wiki/index.md` — refresh the `training/anti-autopilot-review-friction` line
- [ ] **Create** `wiki/sources/articles/anthropic-agents-judgment-calls-2026-10-27.md` — source summary

## Page drafts

### wiki/training/anti-autopilot-review-friction.md (updated)

Frontmatter: `as_of: 2026-10-27`; append `anthropic-agents-judgment-calls-2026-10-27` to `sources:`.

`## Current guidance`: new bullet appended at the end:

```
- On open judgment calls (which metric, which comparison, which population), write down your own pick before the agent offers one, and ask it for the strongest case for the option it is not recommending
```

New section inserted after `## What works and what fails (empirical ratios)` and before `## Cognitive debt`:

```
## Deferral on judgment calls

Anthropic's October 2026 randomized study measured how much an agent's preference decides calls that experts believe they are making. Fifty causal-inference analysts did an hour-long analysis with Claude Code (Opus 4.8). On four choices with two defensible options each, the agent was secretly given a coin-flip lean and told to argue honestly and never mislead.

- Analysts went with the agent's lean 86% of the time (50% would mean no influence). Analysts who had already picked an option switched 60% of the time when the agent disagreed, against 6% when it agreed.
- The coin flips alone predicted 82% of final recommendations.
- 77% justified their choices with the agent's arguments, sometimes word for word; 15% credited the agent. Those who deferred most were as confident as the rest and as likely to call the result their own. Experience did not predict deferral.
- Working with the agent still beat working without it: the 11 who skipped it made serious errors far more often (55% against 6%) and took longer, though they were less experienced.

Limits: the agents' preferences were deliberately strengthened, and the study covers one task, field and model. Anthropic's untested suggestions are agents that argue each option or ask for the expert's view first, and institutions that decide which calls need a person's own informed judgment.
```

`## Failure modes`: new bullet inserted after "Using AI to replace the judgment layer rather than the execution layer":

```
- **Counting sign-off as independent judgment.** When an agent frames the open choices, experts adopt its preferences without noticing. Error checks don't catch it because both options look sound, and asking the expert afterwards doesn't either, because they report the decision as their own.
```

`## Recent changes`: adds one entry dated 2026-10-27 at the top:

```
- [2026-10-27] Added "Deferral on judgment calls": in Anthropic's randomized study, analysts followed Claude Code's covertly assigned lean 86% of the time and 77% reused its arguments while 15% credited it; plus a guidance bullet and a failure mode.
```

`## Sources`: append

```
- [Anthropic — How AI agents shape experts' judgment calls](../sources/articles/anthropic-agents-judgment-calls-2026-10-27.md)
```

### wiki/index.md (updated)

```
- [training/anti-autopilot-review-friction](training/anti-autopilot-review-friction.md) — deliberate review friction, acceptance reasons, review artifacts, escalation evals, near-correct artifact caveats, agent deferral on judgment calls, and cognitive-debt evidence and learning posture to keep human judgment active *(as_of: 2026-10-27)*
```

### wiki/sources/articles/anthropic-agents-judgment-calls-2026-10-27.md (new)

```
---
title: Anthropic — How AI agents shape experts' judgment calls
type: source
source_type: article
source_file: raw/articles/2026-11-24-anthropiccom-research-agents-judgment-calls.md
url: https://www.anthropic.com/research/agents-judgment-calls
published: 2026-10-27
ingested: 2026-11-24
domains: [agents]
---

# Anthropic — How AI agents shape experts' judgment calls

A randomized study by Amaç Herdağdelen, Hailey Joren and Alex Tamkin. Professional analysts did a realistic causal-inference task with Claude Code, whose agent was covertly given a coin-flip preference on each open analytical decision. Analysts mostly adopted the agent's preferences, explained them in its words, and still described the decisions as their own. The authors argue this undermines human sign-off as an independent check, including in AI safety research, where agents increasingly run experiments.

## Influenced pages
- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — new "Deferral on judgment calls" section, guidance bullet and failure mode

## Key claims extracted
- 61 analysts recruited; 50 used the agent (Claude Code, Opus 4.8 at High effort); median task time 65 minutes
- Four analytical choices (outcome measure, comparison method, population, weighting) and a final recommendation; the agent's lean was set by coin flip, with instructions to argue honestly, update on evidence and never mislead
- Analysts matched the lean 86% overall (92%, 82%, 81%, 90% per decision); the final recommendation moved less (54% vs 36% rollout); four leans predicted 82% of recommendations vs a 61% baseline
- Prior-stated preferences switched 60% when the agent disagreed vs 6% when it agreed (38 cases; 95% CI on the gap 24–82 points)
- 77% reused the agent's arguments, 15% credited it; confidence was similar for full followers (71) and others (73); no tested characteristic reliably predicted deferral
- Without the agent: 6 of 11 made serious methodological errors vs 3 of 50 with it; median 90 vs 65 minutes; the no-agent group was less experienced
- With no assigned lean, Opus 4.8 made the same five choices in 112 of 123 runs
- Limits: strengthened leans; one task, field and model; average effects only. Proposed directions: measuring deferral, agents that argue each option or ask first, institutions deciding which decisions need a person's own judgment
```

## Schema / vocabulary additions

None.

## Open questions

None.
