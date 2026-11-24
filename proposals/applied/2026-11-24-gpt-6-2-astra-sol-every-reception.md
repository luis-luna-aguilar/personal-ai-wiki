---
type: proposal
source: raw/newsletters/2026-11-17-vibe-check-gpt-62-astra-and-sol-leave-us-wanting.md
sources:
  - raw/newsletters/2026-11-17-vibe-check-gpt-62-astra-and-sol-leave-us-wanting.md
  - raw/articles/2026-11-24-everyto-vibe-check-vibe-check-gpt-6-2-astra-and-sol-leave-us.md
  - raw/newsletters/2026-11-22-stop-telling-ai-how-you-write-show-it.md
  - raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md
status: pending
created: 2026-11-24
---

# Proposal: GPT-6.2 Astra and Sol — first independent reception (Every Vibe Check)

## Summary

### In short
The first outside verdict on OpenAI's new models is "hand them scoped work": Every's seven testers found GPT-6.2 Astra careful, candid and good at clearly defined coding and operations tasks, but it drifted in long drafts, needed prodding on ambitious builds and kept repeating the same visual defaults. All six who rated Astra gave it a middling yellow; four of five rated Sol red. The proposal adds a short reception section to the **GPT-6.2 Astra** and **GPT-6.2 Sol** pages and creates two source pages. The reason to hesitate is a partial source: the full review is paywalled, so only its preview and Every's recaps were read.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 17 November 2026 Every published its Vibe Check of GPT-6.2 Astra and Sol, written by Katie Parrott. Vibe Checks are Every's hands-on reviews, rated on a colour scale. Seven people used the two models for more than two weeks. Their conclusion is in the headline: the models "leave us wanting more". Mike Taylor, Every's head of evals, notes that the hard test tasks he set at the start of the year are now solved, by these models and by their predecessors.

Astra did well on clearly defined coding and operations work. It was careful and candid: it followed the assignment, said when it fell short and did not game the tests. Its weaknesses showed on open-ended work. Its longer writing lost the thread, and ambitious builds needed prodding. In Dan Shipper's manuscript review it missed a factual contradiction that Claude Fable 5.2 caught. Designer Tyler Nishida saw inventive ideas but unfinished interactions and stubborn defaults: the same grain-texture code turned up in 94% of Astra's designs, even after he told it not to use grain, and Kieran kept getting mountains he never asked for. Sol gave most testers even fewer reasons to switch. Mike gave it his first perfect score on a trip-planning task but still does not plan to use it.

Every's 22 November recap gives the ratings: all six testers who rated Astra gave it yellow, and four of the five who rated Sol gave it red. After questions about differences between the build the team had tested and the public release, Every re-ran its tests live on 18 November. The public Astra did better on Mike's junior-engineer benchmark but still trailed Fable 5.2. Every's advice is to use Astra when you can define the job and check the result; for open-ended writing and building, the team still reaches for Claude and Gemini.

### What changes
Both GPT-6.2 pages carry only OpenAI's launch claims, and the Sol page says no independent reads are captured.

- **GPT-6.2 Astra** gains an "Independent reception" section with Every's strengths, weaknesses, ratings and live re-test, plus a Recent-changes entry dated 22 November. Page date stays at 23 November.
- **GPT-6.2 Sol** gains a short reception section with its ratings and the trip-planning anecdote. Its "no independent reads" caveat is rewritten to say that the only outside read is hands-on, with no benchmark scores. It also gains a Recent-changes entry. Page date stays at 23 November.
- Two new source pages: the Vibe Check email and the reception items from the 22 November recap.

### What to weigh
Every's full review is paywalled. The web page and the email carry only the preview, so the individual verdicts, screenshots and benchmark details were not read. The ratings and the 94% figure come from Every's own recap newsletter.

## Intended changes

- [ ] **Update** `wiki/models/gpt-6-2-astra.md` — add an "Independent reception (as of 2026-11-22)" section after "Safety and preparedness"; adds one Recent-changes entry dated 2026-11-22 (list goes to 2, no spill); append the two new source ids to frontmatter `sources:` and two lines to `## Sources`; `as_of` stays 2026-11-23
    > See draft below

- [ ] **Update** `wiki/models/gpt-6-2-sol.md` — add an "Independent reception (as of 2026-11-22)" section after Current status; replace the first Weaknesses bullet; adds one Recent-changes entry dated 2026-11-22 (list goes to 2, no spill); append the two new source ids and two Sources lines; `as_of` stays 2026-11-23
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-vibe-check-gpt-6-2-2026-11-17.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-gpt-6-2-reception-recap-2026-11-22.md` — story-specific source summary for the GPT-6.2 items in Every's 2026-11-22 recap

## Page drafts

### wiki/models/gpt-6-2-astra.md (updated)

Frontmatter `sources:` becomes:

```
sources: [openai-introducing-gpt-6-2-astra-sol, every-vibe-check-gpt-6-2-2026-11-17, every-gpt-6-2-reception-recap-2026-11-22]
```

Insert a new section between `## Safety and preparedness` and `## Weaknesses / caveats`:

```
## Independent reception (as of 2026-11-22)

Every's Vibe Check (seven testers, two-plus weeks) is the first outside read, and its verdict is to hand Astra clearly scoped work.

- **Strengths:** well-defined coding and operations tasks; careful and candid, following the assignment, saying when it falls short and not gaming tests.
- **Weaknesses:** longer drafts drift from the main point; ambitious builds needed prodding, and fast coding builds left problems in their tests; it missed a factual contradiction in a manuscript that [Claude Fable 5.2](claude-fable-5-2.md) caught; designs repeat visual defaults (the same grain-texture code in 94% of one designer's results, even after being told not to; unrequested mountains).
- **Ratings:** all six testers who rated Astra gave it yellow, Every's middle rating. A live re-test of the public release on 2026-11-18 found it improved on Every's junior-engineer benchmark but still behind [Fable 5.2](claude-fable-5-2.md).
- For open-ended writing and building, Every's team still reaches for Claude and Gemini models.
```

In `## Recent changes`, insert directly below the 2026-11-23 entry:

```
- [2026-11-22] Every's Vibe Check: all six raters gave Astra yellow; strong on scoped coding and ops work, weak on long drafts and ambitious builds, repeats visual defaults; trails Claude Fable 5.2 in a live re-test.
```

In `## Sources`, append:

```
- [Every — Vibe Check: GPT-6.2 Astra and Sol Leave Us Wanting More](../sources/newsletters/every-vibe-check-gpt-6-2-2026-11-17.md)
- [Every — GPT-6.2 ratings and live re-test (recap, 2026-11-22)](../sources/newsletters/every-gpt-6-2-reception-recap-2026-11-22.md)
```

### wiki/models/gpt-6-2-sol.md (updated)

Frontmatter `sources:` becomes:

```
sources: [openai-introducing-gpt-6-2-astra-sol, every-vibe-check-gpt-6-2-2026-11-17, every-gpt-6-2-reception-recap-2026-11-22]
```

Insert a new section between `## Current status (as of 2026-11-23)` and `## Weaknesses / caveats`:

```
## Independent reception (as of 2026-11-22)

- Every's Vibe Check found Sol gave most of its seven testers even fewer reasons to switch than [GPT-6.2 Astra](gpt-6-2-astra.md): four of the five who rated it gave it red, Every's lowest rating.
- It earned head of evals Mike Taylor's first perfect score on a trip-planning task, yet he does not plan to use it day to day.
```

In `## Weaknesses / caveats`, the first bullet is replaced:

```
- No independent benchmark scores of 6.2 Sol are captured; the claims above are OpenAI's, and the only outside read is Every's hands-on Vibe Check.
```

In `## Recent changes`, insert directly below the 2026-11-23 entry:

```
- [2026-11-22] Every's Vibe Check: four of five raters gave Sol red; a perfect trip-planning score did not win it a place in daily use.
```

In `## Sources`, append:

```
- [Every — Vibe Check: GPT-6.2 Astra and Sol Leave Us Wanting More](../sources/newsletters/every-vibe-check-gpt-6-2-2026-11-17.md)
- [Every — GPT-6.2 ratings and live re-test (recap, 2026-11-22)](../sources/newsletters/every-gpt-6-2-reception-recap-2026-11-22.md)
```

### wiki/sources/newsletters/every-vibe-check-gpt-6-2-2026-11-17.md (new)

```
---
title: "Every — Vibe Check: GPT-6.2 Astra and Sol Leave Us Wanting More"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-17-vibe-check-gpt-62-astra-and-sol-leave-us-wanting.md
url: https://every.to/vibe-check/vibe-check-gpt-6-2-astra-and-sol-leave-us-wanting-more
published: 2026-11-17
ingested: 2026-11-24
domains: [models]
---

# Every — Vibe Check: GPT-6.2 Astra and Sol Leave Us Wanting More

Katie Parrott's Vibe Check of OpenAI's GPT-6.2 Astra and Sol, after seven Every staff used them for more than two weeks. Only the free preview was read, in the email and on the web page (raw/articles/2026-11-24-everyto-vibe-check-vibe-check-gpt-6-2-astra-and-sol-leave-us.md); the full review, with individual verdicts, screenshots and benchmarks, is paywalled.

## Influenced pages
- [GPT-6.2 Astra](../../models/gpt-6-2-astra.md) — Independent reception section
- [GPT-6.2 Sol](../../models/gpt-6-2-sol.md) — Independent reception section and rewritten caveat

## Key claims extracted
- Astra is useful for clearly defined coding and operations work; its longer writing lost the thread and its ambitious builds needed prodding
- Sol gave most testers even fewer reasons to switch; Mike Taylor gave it his first perfect score on a travel-planning task but doesn't plan to use it
- Kieran Klaassen's coding builds: Astra's speed came with a problem in the tests it left behind
- Dan Shipper's manuscript review: Astra missed a factual contradiction that Fable caught
- Tyler Nishida's interface designs: inventive ideas, unfinished interactions, stubborn visual defaults
- Mike Taylor's hard tasks from early 2026 (themed curriculum, minute-by-minute show plan, executive exercises) are now handled by both models and their predecessors: "now Codex has kinda saturated them" (web preview)
- Verdict: Astra is worth trying when you can define the job and check the result; for open-ended writing and building the team still reaches for Claude and Gemini
```

### wiki/sources/newsletters/every-gpt-6-2-reception-recap-2026-11-22.md (new)

```
---
title: Every — GPT-6.2 ratings and live re-test (recap, 2026-11-22)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-22-stop-telling-ai-how-you-write-show-it.md
url: https://every.to/context-window/stop-telling-ai-how-you-write-show-it
published: 2026-11-22
ingested: 2026-11-24
domains: [models]
---

# Every — GPT-6.2 ratings and live re-test (recap, 2026-11-22)

The GPT-6.2 items in Every's 2026-11-22 Sunday recap ("Stop Telling AI How You Write—Show It"): the Vibe Check's summary ratings and the result of the live re-Vibe Check of the public release. This page covers only those items; the newsletter's other stories are separate. Every's 2026-11-18 newsletter (raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md) announced the live re-test, citing back-and-forth about differences between the build the frontier team tested and the public release.

## Influenced pages
- [GPT-6.2 Astra](../../models/gpt-6-2-astra.md) — ratings, grain-texture figure, live re-test result
- [GPT-6.2 Sol](../../models/gpt-6-2-sol.md) — ratings

## Key claims extracted
- Both models are careful and candid: they follow the assignment, say when they fall short, and don't game the test
- Astra drifts from the main point in longer drafts and reuses the same look in its designs; Kieran Klaassen kept getting mountains he never asked for
- All six testers who rated Astra gave it yellow; four of the five who rated Sol gave it red; advice: hand them clearly scoped work
- Live re-Vibe Check (2026-11-18): the public Astra improved on Mike Taylor's junior-engineer benchmark but still trails Fable 5.2
- Designer Tyler Nishida found the same grain-texture code in 94% of Astra's designs, even after telling it not to use grain
```

## Schema / vocabulary additions

None.

## Open questions

None.
