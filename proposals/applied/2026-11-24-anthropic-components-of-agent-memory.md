---
type: proposal
source: raw/articles/2026-11-23-anthropiccom-research-components-of-agent-memory.md
status: pending
created: 2026-11-24
---

# Proposal: Anthropic — "The components of agent memory" (salience, steering, and dreaming)

## Summary

### In short
Newer models decide well for themselves what to remember, so the best memory prompt says what memory is for and leaves the rest to the model. Fixed rules such as "record only failures" cut most of Opus 5's gain. Anthropic's memory research post backs this with evals across model generations. It also shows dreaming, an offline pass that checks notes against transcripts, fixing wrong memories and building wikis that beat search alone. The proposal adds a section to Agent memory and a dreamed-wiki bullet to Knowledge layer. The reason to hesitate is length: Agent memory goes past its warning line.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
"The components of agent memory" is an Anthropic research post, forwarded on 7 November 2026. It defines agent memory as knowledge Claude gains from experience and keeps between sessions as context it can read later. That excludes changes to weights, learning inside one conversation, and compaction. Its framing borrows from sleep: people record experiences as they happen and consolidate only some of them offline. Agents can do the same by writing notes during a session and "dreaming" afterwards.

The first evals test what models choose to remember. On a CL-Bench task, Claude answered database questions, each in a fresh session, with one memory folder that persisted between them. Sonnet 4.6 left scattered, untested guesses. Opus 4.7 consolidated its notes, and Opus 5 was the first to "close the loop" with checked rules and warnings about traps. In Pokémon Red, Sonnet 3.7 wrote 413 memory files in 225 folders and won one badge. Fable 5 wrote nine files plus a `global.md` dashboard and won four, because it saved only what the screen could not tell it. Telling strong models that a memory folder existed was enough. Prescribing rules hurt them, while explicit prompting nearly doubled Sonnet 4.6's score.

The dreaming evals show it doing three jobs. It corrected a wrong landmark note that otherwise kept Claude looping in the game. It built a linked wiki over about 350,000 internal Stainless files: scores rose from 13% to 48% as dreaming scaled from 2 to 128 sessions, and wiki plus search beat search alone. It also improved its own instructions: a self-reflection loop took a legal brief from 72% to 100% of criteria. The post admits limits. On one legal task the wiki added nothing, and on another it grew larger than the documents it summarized.

### What changes
The wiki records Cognition's Devin Dreaming and lists Managed Agents' Dreams feature, but it has no evidence on how well models write memory, how to prompt for it, or what dreaming measurably buys.

- **Agent memory** gains a section, "How agents write memory, and dreaming": salience by model generation, the "say what memory is for, not how" rule, dreaming as correction and promotion, and Claude Code auto memory's 200-line / 25 KB load limit. Current-status date and page date move to 7 November, with one Recent-changes entry.
- **Knowledge layer** gains a bullet on dreamed wikis: the Stainless scaling result, wiki plus search against search alone, where the wiki gave no gain, and the instruction-rewriting loop. Page date moves to 7 November, with one Recent-changes entry.
- Index lines for both pages and one new source page.

### What to weigh
The post carries no date on the page, so 7 November is the date it was forwarded. Agent memory would reach about 115% of its 1,200-word ceiling. The open question offers a split.

## Intended changes

- [ ] **Update** `wiki/concepts/agent-memory.md` — new `## How agents write memory, and dreaming` section after "Context editing and persistent state"; Current-status stamp 2026-10-26 → 2026-11-07; adds one Recent-changes entry dated 2026-11-07 at the top (list goes from 6 to 7, no spill); append source id and Sources line; `as_of` 2026-10-26 → 2026-11-07
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-layer.md` — one Current-status bullet; Current-status stamp 2026-09-29 → 2026-11-07; adds one Recent-changes entry dated 2026-11-07 at the top (list goes from 5 to 6, no spill); append source id and Sources line; `as_of` 2026-09-29 → 2026-11-07
    > See draft below

- [ ] **Update** `wiki/index.md` — refresh the agent-memory and knowledge-layer descriptions and dates
    > See draft below

- [ ] **Create** `wiki/sources/articles/anthropic-components-of-agent-memory-2026-11.md` — source summary

## Page drafts

### wiki/concepts/agent-memory.md (updated)

Frontmatter: `as_of: 2026-10-26` → `as_of: 2026-11-07`; append `anthropic-components-of-agent-memory-2026-11` to `sources:`.

Heading: `## Current status (as of 2026-10-26)` → `## Current status (as of 2026-11-07)`.

Insert a new section after `## Context editing and persistent state` and before `## Practical implications`:

```md
## How agents write memory, and dreaming

Anthropic's "The components of agent memory" (November 2026) separates writing notes during a session from consolidating them afterwards, and measures both.

- **Salience judgment improves with model generation.** On a CL-Bench 1.0 task (a fresh session per question, one persistent memory directory), Sonnet 4.6 left scattered untested theories, Opus 4.7 consolidated its notes and marked what was checked, and Opus 5 was the first to "close the loop" with validated rules and warnings about traps; Opus 5.5 and Sonnet 5.5 matched it. In Pokémon Red, Sonnet 3.7 wrote 413 files in 225 folders and won one badge, while Fable 5 wrote nine files plus a `global.md` dashboard and won four, storing only what the screen could not tell it.
- **Say what memory is for, not how to use it.** Telling strong models a memory folder exists was enough; a fixed rule such as "record only failures" cut most of Opus 5's and Opus 4.7's gain. Steering helps older models: prompting Sonnet 4.6 to read memory and test its theories nearly doubled its score.
- **Dreaming corrects and promotes.** Dreaming reviews memory against the original transcripts. It fixed a wrong landmark note that otherwise kept Claude looping, repaired broken links in agent-built wikis, and can promote a few notes into every session's context. That top layer has to stay small: Claude Code's auto memory loads only the first 200 lines or 25 KB of `MEMORY.md`, used as an index. Dreamed wikis are on [Knowledge layer](knowledge-layer.md).
- **Open trade-offs.** Writing notes in-session costs attention, dreaming costs compute, and memory drifts, so dreaming may need to target the information most likely to change.
```

Recent changes: insert at the top:

```md
- [2026-11-07] Added "How agents write memory, and dreaming" from Anthropic's memory evals: salience by model generation, purpose-not-rules prompting, dreaming as correction and promotion, Claude Code auto memory's 200-line / 25 KB load.
```

Sources: append:

```md
- [Anthropic — The components of agent memory](../sources/articles/anthropic-components-of-agent-memory-2026-11.md)
```

### wiki/concepts/knowledge-layer.md (updated)

Frontmatter: `as_of: 2026-09-29` → `as_of: 2026-11-07`; append `anthropic-components-of-agent-memory-2026-11` to `sources:`.

Heading: `## Current status (as of 2026-09-29)` → `## Current status (as of 2026-11-07)`.

Insert as a new Current-status bullet after the OpenWiki bullet:

```md
- Agents can compile the wiki themselves through dreaming, and it works best alongside search. In Anthropic's tests (November 2026), Opus 5 agents built a linked wiki over ~350k Stainless internal files (~420M tokens); scores on 25 questions rose from 13% to 48% of graded criteria as dreaming scaled from 2 to 128 sessions, and wiki plus search reached 61% against 53% for search alone while saving about 20k tokens per question. On merger questions spanning several documents the wiki scored 87% against search's 73%, but a legal brief answerable from one document showed no gain, and on another task the wiki grew larger than its sources, abstracting nothing. Building instructions matter: a self-reflection loop rewrote them (one page per contract, terms quoted verbatim) and lifted a brief from 72% to 100% of criteria.
```

Recent changes: insert at the top:

```md
- [2026-11-07] Added Anthropic's dreamed-wiki results: a wiki built over 2→128 dreaming sessions (13%→48%), wiki plus search beating search alone, no gain on single-document tasks, and instruction rewriting lifting a brief from 72% to 100%.
```

Sources: append:

```md
- [Anthropic — The components of agent memory](../sources/articles/anthropic-components-of-agent-memory-2026-11.md)
```

### wiki/index.md (updated)

In the agent-memory line, change "Cognition's Agent Memory Repo and Devin Dreaming;" to "Cognition's Agent Memory Repo and Devin Dreaming; Anthropic's memory evals (salience by model generation, purpose-not-rules prompting, dreaming as correction);" and `as_of: 2026-10-26` → `as_of: 2026-11-07`.

Replace the knowledge-layer line:

```md
- [concepts/knowledge-layer](concepts/knowledge-layer.md) — compiled, maintained context layer between raw sources and agents; also called LLM wiki, second brain (personal scope); operating-rules side kept current by ContextOps; dreamed wikis plus search beat search alone (Anthropic) *(as_of: 2026-11-07)*
```

### wiki/sources/articles/anthropic-components-of-agent-memory-2026-11.md (new)

```md
---
title: Anthropic — The components of agent memory
type: source
source_type: article
source_file: raw/articles/2026-11-23-anthropiccom-research-components-of-agent-memory.md
url: https://www.anthropic.com/research/components-of-agent-memory
ingested: 2026-11-24
domains: [agents]
---

# Anthropic — The components of agent memory

Anthropic research post on how Claude writes, corrects and organizes memory, with "dreaming" (an offline pass that reviews memory against session transcripts) as the consolidation step. It reports evals on CL-Bench 1.0, Pokémon Red, a Stainless internal-document corpus, a merger Q&A set and Harvey's LAB legal benchmark, and closes with open design questions. The page carries no date; it was forwarded on 2026-11-07, which the wiki uses as its date.

## Influenced pages
- [Agent memory](../../concepts/agent-memory.md) — new "How agents write memory, and dreaming" section
- [Knowledge layer](../../concepts/knowledge-layer.md) — dreamed-wiki bullet

## Key claims extracted
- Agent memory = knowledge gained from experience and retained between sessions as readable context; excludes weights, in-context learning and compaction
- CL-Bench 1.0: Sonnet 4.6 untested theories; Opus 4.7 consolidated notes; Sonnet 5 marked confirmed answers; Opus 5 first to close the loop with validated rules; Opus 5.5 and Sonnet 5.5 match it
- Pokémon Red at ~10,000 steps: Sonnet 3.7 413 files / 225 folders / 1 badge; Fable 5 nine files in two folders plus `global.md` / 4 badges; Opus 5.5 beat the game with a small memory folder
- Telling the model memory exists beats prescriptive rules; "record only failures" removed much of Opus 5's and Opus 4.7's gain; prompting Sonnet 4.6 to read memory and test theories nearly doubled its score; Sonnet 5 reads memory unprompted 9 of 10 times
- Dreaming corrected a wrong Mt. Moon note; the uncorrected run never reached Cerulean City
- Stainless corpus (~350k files, ~420M tokens): dreamed wiki 13%→48% of criteria over 2→128 sessions; wiki + search 61% vs 53% search alone; ~20k tokens saved per question
- Merger Q&A: wiki 87% vs search 73%; one LAB task no gain; on another the wiki grew larger than the documents
- Self-reflection loop on wiki instructions: brief from 72% (41/57 facts) to 100%
- Claude Code auto memory loads only the first 200 lines or 25 KB of `MEMORY.md`
- Cookbooks published for dreaming with a dynamic workflow and for knowledge wikis
```

## Schema / vocabulary additions

None.

## Open questions

- Agent memory would sit at about 115% of its concept ceiling. Split it now? A natural cut moves "Context editing and persistent state" (in-loop context research and compaction) to a new `concepts/context-editing.md`, leaving Agent memory with lifecycle, memory writing and dreaming. Assumed no split in this proposal; it can be done as a direct refactor.
	- Split it
