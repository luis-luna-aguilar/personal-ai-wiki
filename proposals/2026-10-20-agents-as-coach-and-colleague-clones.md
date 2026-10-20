---
type: proposal
source: raw/newsletters/2026-10-09-you-already-signed-this-off-in-the-simulation.md
sources:
  - raw/newsletters/2026-10-02-how-to-get-better-at-ai-by-asking-ai.md
  - raw/newsletters/2026-10-09-you-already-signed-this-off-in-the-simulation.md
  - raw/newsletters/2026-10-04-chatgpt-wants-to-be-your-operating-system.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Agents as coach and stand-in (self-assessment and colleague clones)

## Summary

### In short
An agent that can read your work history is a good coach, but a cloned colleague is a poor stand-in: it learns a person's rules, not when they break them. Arielle Shipper rose from 5.5 to 7.9 on Every's eight-level ladder in four months with weekly Codex-graded reviews. Mike Taylor's clone of Dan Shipper went along with a question's framing 68% of the time; the real Dan did 34% of the time. The proposal updates the autonomy-and-governance, skill-methodology and simulated-humans pages and adds two source pages. One reason to hesitate: Shipper's level descriptions differ from the ladder table the wiki holds.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Two Every essays from early October 2026 use agents to model human judgment. On 2 October Arielle Shipper, Every's head of operations, described how she learned to use AI by asking AI. She gave Codex Every's eight-levels-of-adoption article and asked where she stood based on their past sessions; it placed her at 5.5. She then asked it to redo finished projects at the next level, for example splitting a Stripe sales-tax analysis across an extractor, a verifier and a spreadsheet builder, and to explain those setups without jargon. A weekly Friday task now grades her against the levels, cites the sessions behind the score and proposes next week's experiments; over four months her score went from 5.5 to 7.9. Her "/self improve" skill, already in the wiki from August, now has a published prompt: diagnose the failure, describe what good looks like, propose the smallest durable instruction change, and show it before saving.

On 9 October Mike Taylor, head of evals, wrote about cloning colleagues. He turned a year of his boss's public Slack messages into a persona file with the open-source SynthTeam library and had an agent revise a client email until the clone rated it 10/10. After 73 rounds it stalled at 9/10, dropped half the content and read "like it was drafted by someone's lawyer". A clone of GitHub's COO used the man's favorite framework in 5 of 12 answers; the real one never did. Across 201 Slack threads, a clone of Every's CEO accepted a question's framing twice as often as he did. Taylor still recommends clones for rehearsing a meeting, not for sign-off.

### What changes
The wiki holds Every's eight-level ladder on the autonomy-and-governance page, the self-improve skill as pattern 10 of the skill methodology, and Simile's trained "digital twins" on the simulated-humans trend, which contrasts them with frontier models prompted to role-play.

- **Agent autonomy and governance** gains a paragraph on using the ladder for self-assessment with an agent that reads your sessions. One Recent-changes entry dated 2 October (5 entries). Page date stays at 11 October.
- **Agent skill methodology** adds the published self-improve prompt to pattern 10. One Recent-changes entry (9 entries). Page date moves to 2 October.
- **AI-simulated human populations** gains a signal on prompted colleague clones and one item to watch. One Recent-changes entry (2 entries). Page date moves to 9 October.
- Two new source pages; the 4 October recap gets none.

### What to weigh
Shipper's article names level 5 "building workflows that make an agent's output consistent" and level 6 "an agent that works proactively in the background", while the wiki's table calls level 5 "background agent" and level 6 "goal-directed agent". The draft quotes only her numeric scores and leaves the table alone; whether the table needs checking against Every's original is an open question.

## Intended changes

- [ ] **Update** `wiki/training/agent-autonomy-and-governance.md` — self-assessment paragraph in "AI adoption and fluency levels"; adds one Recent-changes entry dated 2026-10-02 (4 → 5, no spill); append source

- [ ] **Update** `wiki/training/agent-skill-methodology.md` — extend pattern 10 with the published self-improve prompt; adds one Recent-changes entry dated 2026-10-02 (8 → 9, no spill); as_of 2026-09-03 → 2026-10-02; append source

- [ ] **Update** `wiki/trends/synthetic-human-simulation.md` — new Current-signal bullet and one What-to-watch bullet; adds one Recent-changes entry dated 2026-10-09 (1 → 2); as_of 2026-08-22 → 2026-10-09; append source

- [ ] **Create** `wiki/sources/newsletters/every-ask-ai-to-level-up-2026-10-02.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-colleague-clones-2026-10-09.md` — source summary

## Page drafts

### wiki/training/agent-autonomy-and-governance.md (updated)

Frontmatter: append `every-ask-ai-to-level-up-2026-10-02` to `sources:`. `as_of` stays 2026-10-11.

New paragraph in `## AI adoption and fluency levels`, inserted after the "Practical rules from the framework" list and before "Where people sit":

```
**Using the ladder for self-assessment (Every, October 2026).** An agent that can read your session history can place you on the ladder from what you actually do. Every's head of operations, Arielle Shipper, gave Codex the framework and asked "what level am I based on how we've been working together?", then asked it to redesign finished projects at the next level, to explain unfamiliar setups (orchestrator threads, context packets, verifier agents) without jargon, and to run a weekly Friday review that grades her, cites the sessions behind the score, and lists experiments for the next week. Her score went from 5.5 to 7.9 in four months; she found the "what changed" and "next week" sections more useful than the number. Wait for about a week of regular sessions before asking, so the agent has evidence to read.
```

`## Recent changes` — adds one entry dated 2026-10-02, inserted between the 2026-10-10 entry and the end of the list (list goes from 4 to 5, no spill):

```
- [2026-10-02] Added "Using the ladder for self-assessment": an agent that reads session history places you on the ladder and runs a weekly graded review (Arielle Shipper, 5.5 → 7.9 in four months).
```

`## Sources` — append:

```
- [Every — How to Get Better at AI by Asking AI](../sources/newsletters/every-ask-ai-to-level-up-2026-10-02.md)
```

### wiki/training/agent-skill-methodology.md (updated)

Frontmatter: `as_of: 2026-10-02`; append `every-ask-ai-to-level-up-2026-10-02` to `sources:`.

Pattern 10, replaced in full:

```
**10. Run a personal self-improve loop, not just a team skill library**
Every's head of operations, Arielle Shipper, keeps a standing "self-improve" skill for her own Codex workflow: whenever the agent produces a wrong or off-tone result, she feeds it feedback on what went wrong and what a better response would have looked like, then runs the skill — which reviews the failure, interrogates the cause, and proposes a targeted edit to Codex's own operating instructions so the mistake is less likely to repeat (e.g. "always re-read prior thread messages before drafting a Slack reply"). This is the same compounding mechanism behind team-facing skills like Every's KateBench/DanLens (which rewrite themselves based on which suggestions get accepted or rejected), scaled down to something one person runs on their own workflow rather than infrastructure a team builds and maintains. Her published prompt: "Look at this conversation, including the original output, and my corrections. Diagnose why it went wrong, describe what a good result looks like, and propose the smallest change to my instructions that would prevent this next time. Show me the change before saving it." The review step matters: corrections from one conversation do not carry to the next unless they are saved, and unreviewed saves are how instruction files bloat.
- (Arielle Shipper, Every, Aug 2026 — skill published on GitHub; prompt published Oct 2026)
```

`## Recent changes` — adds one entry dated 2026-10-02, inserted between the 2026-10-19 and 2026-08-26 entries (list goes from 8 to 9, no spill):

```
- [2026-10-02] Added Arielle Shipper's published self-improve prompt (diagnose, describe good, propose the smallest instruction change, show before saving) to pattern 10.
```

`## Sources` — append:

```
- [Every — How to Get Better at AI by Asking AI](../sources/newsletters/every-ask-ai-to-level-up-2026-10-02.md)
```

### wiki/trends/synthetic-human-simulation.md (updated)

Frontmatter: `as_of: 2026-10-09`; append `every-colleague-clones-2026-10-09` to `sources:`.

New bullet at the end of `## Current signal` (after "The broader pattern"):

```
- **Prompted colleague clones learn rules, not when to break them (Every, October 2026).** Mike Taylor, Every's head of evals, built persona files of three people by prompting frontier models: his boss, from a year of her public Slack messages via the open-source SynthTeam library, and GitHub COO Kyle Daigle and Every CEO Dan Shipper, from public writing. An agent revising a client email for the boss clone's approval ran 73 rounds, stalled at 9/10, and produced a lawyerly email that had dropped half the original content. The Daigle clone used his favorite framework in 5 of 12 answers; the real Daigle never mentioned it (2 strong matches, 4 partial, 6 misses). Across 201 Slack threads the real Dan Shipper went along with a question's framing 34% of the time, against 68% for the prompted model. Taylor still uses clones for rehearsing a meeting, not for sign-off. This is the prompted role-play approach that Simile's post-trained twins are positioned to beat.
```

New bullet at the end of `## What to watch`:

```
- Whether clones built from a person's own messages can learn when that person breaks their rules or rejects a question's premise, the gap Every measured, or whether that requires behavioral post-training of the Simile kind
```

`## Recent changes` — adds one entry dated 2026-10-09 above the existing one (list goes from 1 to 2):

```
- [2026-10-09] Added Every's prompted colleague clones: rules learned, exceptions missed (real Dan Shipper accepts a question's framing 34% of the time, his clone 68%).
```

`## Sources` — append:

```
- [Every — You Already Signed This Off (In the Simulation)](../sources/newsletters/every-colleague-clones-2026-10-09.md)
```

### wiki/sources/newsletters/every-ask-ai-to-level-up-2026-10-02.md (new)

```
---
title: 'Every — How to Get Better at AI by Asking AI'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-02-how-to-get-better-at-ai-by-asking-ai.md
published: 2026-10-02
ingested: 2026-10-20
domains: [training, agents]
---

# Every — How to Get Better at AI by Asking AI

Arielle Shipper, Every's head of operations, shares five prompts that use Codex as a coach: assess her level on Every's eight-levels-of-AI-adoption framework from past sessions, suggest next-level redesigns of finished projects, teach the unfamiliar techniques, run a recurring weekly graded review, and turn failures into durable instruction changes. A Context Window recap on 4 October (`raw/newsletters/2026-10-04-chatgpt-wants-to-be-your-operating-system.md`) repeats the prompts and adds nothing new.

## Influenced pages

- [Agent autonomy and governance](../../training/agent-autonomy-and-governance.md) — self-assessment against the ladder
- [Agent skill methodology](../../training/agent-skill-methodology.md) — published self-improve prompt in pattern 10

## Key claims extracted

- Codex placed Shipper at 5.5 (solid level 5, some level 6 habits) from their past sessions
- Codex proposed redoing a Stripe sales-tax data pull with specialist agents (extractor, verifier, Google Sheets builder)
- Orchestrator thread holds goal, constraints, deadline and definition of done; each specialist gets a "context packet" with only what it needs; skeptic and verifier agents for high-stakes work
- Weekly Friday task grades her against the levels, cites sessions, notes what changed, lists next experiments; score went 5.5 → 7.9 in four months
- In her article, level 5 is "building workflows that make an agent's output consistent and reliable" and level 6 "an agent that works proactively in the background"
- /self improve prompt: diagnose why it went wrong, describe a good result, propose the smallest instruction change, show it before saving
- Five prompts published (assess, recommend, teach, recur, self-improve)
```

### wiki/sources/newsletters/every-colleague-clones-2026-10-09.md (new)

```
---
title: 'Every — You Already Signed This Off (In the Simulation)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-09-you-already-signed-this-off-in-the-simulation.md
published: 2026-10-09
ingested: 2026-10-20
domains: [agents, training]
---

# Every — You Already Signed This Off (In the Simulation)

Mike Taylor, Every's head of evals, built AI clones of his boss, GitHub's COO and Every's CEO to stand in for sign-off and to rehearse an interview. The clones learned each person's rules but not when the person would set them aside or reject a question's premise.

## Influenced pages

- [AI-simulated human populations](../../trends/synthetic-human-simulation.md) — prompted colleague-clone signal and a What-to-watch item

## Key claims extracted

- Boss clone: SynthTeam turned a year of Natalia Quintero's public-channel Slack messages into a persona file; GPT-5.5 with /goal revised an email until the clone rated it 10/10, using a fresh subagent per rating
- 73 optimization rounds; 9/10 by round 16, never 10; the result read as lawyer-drafted, dropped the consulting pitch and added promises Taylor had not made
- GitHub COO Kyle Daigle clone (from public writing): must/should/could framework in 5 of 12 answers, never mentioned by the real Daigle; 2 strong matches, 4 partial, 6 misses; Daigle said it overindexed on written work
- Dan Shipper clone on GPT-6 Sol reached 10/10 in 8 rounds but stayed inside the proposal's frame; the real Dan reframed it ("checks", not benchmarks)
- "Dan Lens" vs real replies on 201 Slack threads: real Dan accepts a thread's framing 34% of the time, the model 68%
- Clones are useful for rehearsal and for learning about a person; sign-off still needs the person
```

## Schema / vocabulary additions

None.

## Open questions

- Arielle Shipper's article describes level 5 as building workflows that make agent output consistent and level 6 as proactive background agents, while the wiki's ladder table calls level 5 "background agent" and level 6 "goal-directed agent". Should the table be checked against Every's original framework in a separate fix? The drafts leave it unchanged.
