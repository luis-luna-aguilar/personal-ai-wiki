---
type: proposal
source: raw/articles/2026-10-19-developersopenaicom-blog-maintaining-software-with-the-gpt-6.md
status: pending
created: 2026-10-19
---

# Proposal: OpenAI — Maintaining software with the GPT-6 family

## Summary

### In short
GPT-6-class models can now run codebase maintenance from a short, ambiguous prompt, and a cheaper sibling gets most of the way there: OpenAI's Core Experimentation team merged more than 1,400 cleanup pull requests deleting over 800k lines, and GPT-6.1 Sol at Ultra effort found 92% as many stale experiments as GPT-6 Astra for 14% of the API cost. The proposal adds this to GPT-6 Astra, Codex, the engineering adoption evidence page, the software-development enablement guidance and the cost-aware routing page. One hesitation: the post carries no date, and GPT-6.1 Sol has no wiki page yet.

[[#Open questions|Open questions: 1 to answer.]]

### The source
An engineer on OpenAI's Core Experimentation team, which builds the software behind experiments across the company, describes on the OpenAI Developers blog how the team used the GPT-6 models in Codex for maintenance: removing unused code, cleaning up stale experiments, and fixing tests and CI. The premise is that coding agents made the team build faster, which also made the maintenance pile grow faster.

Dead-code removal used to need complex static analysis plus runtime logging, and mistakes still caused incidents. With GPT-5.6 Sol the team could write targeted prompts with clear validation criteria. GPT-6 Astra handled a much vaguer prompt: it read past PRs, Slack threads, project trackers and production profiling tables to confirm deleted lines were never reached, and explained each deletion. Five engineers working part-time over two weeks ran variations of that prompt across repositories.

Stale experiments are harder, because their code may still run in production. Astra drafted its own scanning prompt, folded in the author's review comments, and ranked findings by CPU cost from instrumentation. Its best find, a "Permanent" flag mapped to every other feature, went to human review rather than deletion and saved an estimated 0.42% CPU once removed.

The team then ran the same stale-experiment audit, over 6,000 files and a million lines, on three model and effort settings ("effort" is how long the model is allowed to reason). The author validated the findings by hand. GPT-6.1 Sol missed mainly flags that other flags depend on, a gap the team now patches with prompt corrections it plans to revisit with each new model. A CI-cost prompt led to about 30 PRs that more than halved median CI time. The post admits some proposals added more complexity than they were worth, and closes with a recipe: start with one small task, compare configurations, feed review back into the prompt, then widen.

### What changes
The wiki covers GPT-6 Astra's launch reception and has adoption case studies from Shopify, Uber, Anthropic and Bun, but nothing on agents doing maintenance work and no mention of GPT-6.1 Sol.

- **GPT-6 Astra** gains a Current-status bullet on its maintenance results in Codex and the comparison with GPT-6.1 Sol, plus one Recent-changes entry. Page date moves to 19 October.
- **Codex** gains a maintenance-pass usage pattern (short prompt, evidence before deletion, start small then widen) and a Recent-changes line; the list is full, so the oldest entry (OpenAI Symphony, 28 April) moves to history. Page date moves to 19 October.
- **Engineering AI adoption: evidence from practice** gains the OpenAI case study with its numbers and one Recent-changes entry. Page date moves to 19 October.
- **AI enablement — software development** gains a "start small, review, then expand" maintenance pattern under Engineering discipline; its Recent-changes list reaches the cap of 10 with nothing spilled. Page date moves to 19 October.
- **Cost-aware AI task routing** gains the model and effort comparison as a selection example. Page date moves to 19 October.
- One new source page for the blog post.

### What to weigh
The raw file and article give no publication date, so every page uses the ingest date, 19 October; the real date may be a few days earlier. Cost-aware routing ends at about 99% of its body ceiling, under the warning line but with no room left for the next addition.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/gpt-6-astra.md` — new Current-status bullet; Current status stamp and `as_of` to 2026-10-19; adds one Recent-changes entry dated 2026-10-19 (3 → 4, no spill); appends source id and Sources link
- [ ] **Update** `wiki/tools/codex.md` — new block in "Usage patterns"; `as_of` to 2026-10-19; adds one Recent-changes entry dated 2026-10-19; appends source id and Sources link
- [ ] **Spill** `wiki/tools/codex.md` → `wiki/history/tools/codex.md` — the list is at the 10-entry cap, so the oldest entry (`[2026-04-28] OpenAI Symphony…`) falls off
- [ ] **Update** `wiki/training/engineering-ai-adoption-evidence.md` — new bullet at the end of "Scale data and large-scale case studies"; `as_of` to 2026-10-19; adds one Recent-changes entry dated 2026-10-19 (5 → 6, no spill); appends source id and Sources link
- [ ] **Update** `wiki/training/ai-enablement-software-development.md` — new bullet at the end of "### Engineering discipline"; `as_of` to 2026-10-19; adds one Recent-changes entry dated 2026-10-19 (9 → 10, at cap, no spill); appends source id and Sources link
- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — new bullet at the end of "### Model and harness selection wins"; `as_of` to 2026-10-19; adds one Recent-changes entry dated 2026-10-19 (2 → 3, no spill); appends source id and Sources link
- [ ] **Create** `wiki/sources/articles/developersopenaicom-blog-maintaining-software-gpt-6.md` — source summary

## Page drafts

### wiki/models/gpt-6-astra.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-19
sources: [zawinskis-law-multiagents-2026-08-08, every-vibe-check-gpt-6-astra-2026-09-03, latent-space-gpt-6-astra-ai-engineer-2026-09-03, ainews-gpt-6-astra-launch-2026-09-04, every-split-verdict-fable-astra-2026-09-06, ainews-navier-stokes-2026-09-09, developersopenaicom-blog-maintaining-software-gpt-6]
```

Current status heading becomes `## Current status (as of 2026-10-19)`; append this bullet after the existing four:

```
- **Codebase maintenance in Codex (OpenAI's own team):** handled a short, ambiguous dead-code prompt that GPT-5.6 Sol could not, gathering evidence from past PRs, Slack, project trackers and production profiling before each deletion; five engineers working part-time over two weeks merged 1,400+ PRs removing 800k+ lines. On a stale-experiment audit of 6,000+ files, Astra at Ultra effort produced 142 accepted findings for $109; the newer, cheaper GPT-6.1 Sol at Ultra produced 131 for $15, missing mainly constant flags used as dependencies of other flags. See [Engineering AI adoption: evidence from practice](../training/engineering-ai-adoption-evidence.md).
```

Recent changes — insert at the top:

```
- [2026-10-19] OpenAI's Core Experimentation team reported using Astra in Codex for large-scale maintenance (1,400+ merged PRs, 800k+ lines deleted); GPT-6.1 Sol at Ultra effort reached 92% of Astra Ultra's stale-experiment findings at 14% of the API cost.
```

Sources — append:

```
- [OpenAI Developers — Maintaining software with the GPT-6 family](../sources/articles/developersopenaicom-blog-maintaining-software-gpt-6.md)
```

### wiki/tools/codex.md (updated)

Frontmatter: append `developersopenaicom-blog-maintaining-software-gpt-6` to `sources:`; `as_of: 2026-10-19`.

`## Usage patterns (jxnl)` — append a block after "Side panel as work surface":

```
**Maintenance passes (OpenAI Core Experimentation, October 2026)**
OpenAI's own experimentation team runs codebase maintenance through Codex with short, open prompts ("find code that is never reached, prove it, and remove it") rather than hand-built static analysis. The model gathers evidence first (past PRs, Slack threads, project trackers, production profiling) and explains each deletion; anything risky, such as a widely-used "Permanent" feature flag, goes to human review. The team's recipe: start with one small task, compare model and effort settings, fold review comments back into the prompt, then widen to a subdirectory or project. See [GPT-6 Astra](../models/gpt-6-astra.md) for the results.
```

`## Recent changes` — adds one entry at the top and spills the oldest (`[2026-04-28] OpenAI Symphony…`):

```
- [2026-10-19] Added OpenAI's maintenance-pass pattern: short evidence-first prompts for dead code, stale experiments and CI cost, run on GPT-6 Astra and GPT-6.1 Sol in Codex.
```

`## Sources` — append:

```
- [OpenAI Developers — Maintaining software with the GPT-6 family](../sources/articles/developersopenaicom-blog-maintaining-software-gpt-6.md)
```

### wiki/history/tools/codex.md (updated)

Append:

```

## Archived from current page on <apply date>

- [2026-04-28] OpenAI Symphony: described as an open-source Codex orchestration spec for defining, invoking, and coordinating Codex subagents; issue-tracker integration as the primary input surface; secondary coverage from The Code newsletter — verify spec details against primary OpenAI documentation
```

### wiki/training/engineering-ai-adoption-evidence.md (updated)

Frontmatter: `as_of: 2026-10-19`; append `developersopenaicom-blog-maintaining-software-gpt-6` to `sources:`.

Append at the end of `## Scale data and large-scale case studies`:

```
- OpenAI Core Experimentation team (GPT-6 family in Codex): agent-driven maintenance at scale. Five engineers, part-time over two weeks, ran variations of one short dead-code prompt across repositories with GPT-6 Astra and merged 1,400+ PRs deleting 800k+ lines, with reviews fanned out to the teams that owned each project. One service's container image fell from 3.31GB to 1.72GB (48%) and about 400 visual snapshot variants left the test suite. A stale-experiment pass, ranked by CPU cost from production instrumentation, removed hundreds of experiments and feature flags; Astra raised one flag marked "Permanent", whose single mapping line fanned out to every feature, for human review instead of deleting it, and removing it saved an estimated 0.42% CPU in the main affected service. A CI-cost prompt led to about 30 PRs that cut median CI time from roughly 10 to 4.5 minutes (p90 from 12.5 to 6); one missing mock took a 63-test suite from 592.6s to 29.8s. The team notes some proposals added more complexity than their benefit justified, so prioritization and measurement stayed in the loop. The recipe is on [AI enablement — software development](ai-enablement-software-development.md); the model/effort cost comparison is on [Cost-aware AI task routing](cost-aware-ai-task-routing.md).
```

Recent changes — insert at the top:

```
- [2026-10-19] Added OpenAI Core Experimentation's GPT-6 maintenance case: 1,400+ merged cleanup PRs, 800k+ lines deleted, a 48% smaller container image, hundreds of stale flags removed, median CI time from ~10 to 4.5 minutes.
```

Sources — append:

```
- [OpenAI Developers — Maintaining software with the GPT-6 family](../sources/articles/developersopenaicom-blog-maintaining-software-gpt-6.md)
```

### wiki/training/ai-enablement-software-development.md (updated)

Frontmatter: `as_of: 2026-10-19`; append `developersopenaicom-blog-maintaining-software-gpt-6` to `sources:`.

Append at the end of `### Engineering discipline`:

```
- **Agent-driven maintenance: start small, review, then expand.** Frontier coding agents can now find and justify cleanup work (dead code, stale feature flags, flaky tests, slow CI) from short prompts, and the volume they find can swamp a team. OpenAI's Core Experimentation team's recipe: have the agent find one instance, gather evidence, and open a small draft PR; compare models and effort levels on that task, since a cheaper configuration may be enough; fold your review comments into the next prompt; then widen to a subdirectory and finally the whole codebase. Rank findings with production instrumentation (CPU cost, runtime), send anything marked permanent or operational to human review, and drop proposals whose added complexity outweighs the gain. Case numbers are on [Engineering AI adoption: evidence from practice](engineering-ai-adoption-evidence.md).
```

Recent changes — insert at the top (list reaches 10, no spill):

```
- [2026-10-19] Added the agent-driven maintenance pattern (start small, compare model/effort, feed review back into the prompt, then widen) from OpenAI Core Experimentation's GPT-6 cleanup work.
```

Sources — append:

```
- [OpenAI Developers — Maintaining software with the GPT-6 family](../sources/articles/developersopenaicom-blog-maintaining-software-gpt-6.md)
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter: `as_of: 2026-10-19`; append `developersopenaicom-blog-maintaining-software-gpt-6` to `sources:`.

Append at the end of `### Model and harness selection wins`:

```
- **OpenAI stale-experiment audit: compare model and effort on the real task.** On one Codex audit of 6,000+ files (1M+ lines of Python, TypeScript, Go and Rust), GPT-6 Astra Ultra produced 142 accepted findings for $109.06 ($0.77 each), GPT-6.1 Sol Ultra 131 for $15.12 ($0.12), and GPT-6.1 Sol Medium 86 for $5.27 ($0.06); costs include research subagents and automatic follow-up turns. Reviewing the gap (mostly constant flags used as dependencies of other flags) let the team write prompt corrections so the cheaper model closes it, corrections it plans to revisit when new models ship.
```

Recent changes — insert at the top:

```
- [2026-10-19] Added OpenAI's model/effort comparison on a stale-experiment audit: GPT-6.1 Sol Ultra reached 92% of GPT-6 Astra Ultra's findings at 14% of the API cost.
```

Sources — append:

```
- [OpenAI Developers — Maintaining software with the GPT-6 family](../sources/articles/developersopenaicom-blog-maintaining-software-gpt-6.md)
```

### wiki/sources/articles/developersopenaicom-blog-maintaining-software-gpt-6.md (new)

```
---
title: "OpenAI Developers — Maintaining software with the GPT-6 family"
type: source
source_type: article
source_file: raw/articles/2026-10-19-developersopenaicom-blog-maintaining-software-with-the-gpt-6.md
url: https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family
ingested: 2026-10-19
domains: [coding, models]
---

# OpenAI Developers — Maintaining software with the GPT-6 family

An engineer on OpenAI's Core Experimentation team describes using GPT-6 Astra and GPT-6.1 Sol in Codex for codebase maintenance: removing dead code, cleaning up stale experiments and feature flags, fixing flaky tests and cutting CI time. Astra handled short, ambiguous prompts that GPT-5.6 Sol could not, gathering evidence from PRs, Slack, trackers and production profiling and explaining each deletion. A side-by-side audit found GPT-6.1 Sol Ultra nearly matching Astra Ultra at a fraction of the cost. The post closes with a start-small, review, then expand recipe. No publication date in the post; ingest date used.

## Influenced pages

- [GPT-6 Astra](../../models/gpt-6-astra.md) — maintenance results in Codex, comparison with GPT-6.1 Sol
- [Codex](../../tools/codex.md) — maintenance-pass usage pattern
- [Engineering AI adoption: evidence from practice](../../training/engineering-ai-adoption-evidence.md) — OpenAI maintenance case study
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — agent-driven maintenance pattern
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — model/effort cost-per-finding comparison

## Key claims extracted

- GPT-6 Astra worked from a broad, ambiguous dead-code prompt that GPT-5.6 Sol could not handle completely
- Five engineers, part-time over two weeks, merged 1,400+ PRs deleting 800k+ lines; one container image shrank from 3.31GB to 1.72GB (48%); ~400 visual snapshot variants removed
- Stale-experiment cleanup removed hundreds of experiments and feature flags; one "Permanent" Statsig flag mapped to all features was escalated for review, and removing it saved ~0.42% CPU in the main affected service
- Stale-experiment audit (6,000+ files, 1M+ lines): Astra Ultra 142 findings / $109.06; GPT-6.1 Sol Ultra 131 / $15.12; GPT-6.1 Sol Medium 86 / $5.27; Sol Ultra = 92% of findings at 14% of cost
- Sol's misses were mostly constant flags used as dependencies of other flags; prompt corrections close the gap and should be revisited with new models
- ~30 CI optimization PRs: median CI from ~10 to 4.5 min, p90 from 12.5 to 6 min; one missing mock cut a 63-test suite from 592.6s to 29.8s
- Some proposals added more complexity than their benefit, so prioritization and measurement remained necessary
```

## Schema / vocabulary additions

None.

## Open questions

- GPT-6.1 Sol appears here only as a cheaper Codex option, and the wiki has no page for it. Create `models/gpt-6-1-sol.md` now from this post, or wait for a launch source (assumed: wait)?
	- Wait
