---
type: proposal
source: raw/newsletters/2026-11-16-how-i-finally-got-ai-to-write-like-me.md
sources:
  - raw/newsletters/2026-11-16-how-i-finally-got-ai-to-write-like-me.md
  - raw/newsletters/2026-11-13-your-attention-is-ais-new-bottleneck.md
  - raw/newsletters/2026-11-11-whats-left-for-humans-after-automation.md
  - raw/newsletters/2026-11-22-stop-telling-ai-how-you-write-show-it.md
status: pending
created: 2026-11-24
---

# Proposal: Optimized writing skills beat descriptive style guides (Mike Taylor's tested method)

## Summary

### In short
A "write like me" skill that only describes your style can make AI writing worse; what works is optimizing the skill against your real posts with a blind judge and keeping only changes that score higher. Every's head of evals found a Claude-written style guide lost to all three optimizers on 80–95% of held-out posts, and Opus 5.5 wrote more like him with no skill at all. The proposal adds his six-step method to AI style guides and an overfitting caveat to the personal-benchmarks section of Evals for agentic work. Reason to hesitate: the evals page is already over its length ceiling and reaches about 108% after this.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Mike Taylor, Every's head of evals, has tried to get AI to write like him since 2020. On 16 November 2026 he published the method that finally worked. He took 185 of his posts (335,000 words) and held 54 back as a final exam. A model turned each post into a "brief" with the substance (thesis, outline, facts, quotes) but none of the style, so any draft that sounds like him can be credited to the skill. A "pairwise gold triad" judge then sees his real post and two drafts from the same brief and picks the closer one, run twice with the order swapped because judges favor whatever they read first. Judges differ: Opus 5.5 gave the same answer on swapped order 86% of the time, Sonnet 5.5 70%, the cheap decision model Jev only 50%.

He compared a Claude-written style guide with three optimizers that change the skill and keep a change only if it scores better: Karpathy's autoresearch, DSPy's GEPA and Every's ce-optimize. The written guide lost on 80–95% of held-out posts; it read like a list of his "greatest hits" and produced a caricature. Optimizing cost $27–53 per skill against $5 for the one-shot guide, with most gains in three rounds; GEPA won (77–31 over autoresearch, 85–15 over ce-optimize). Skills belong to a model: Opus 5.5 went from 16% with no skill to 93% with its own optimized skill, and Sonnet 5.5 with an optimized skill beat Opus 5.5 with the written guide on 46 of 60 judgments. He drafts only from a full brief, and his 44 edits on one piece become the next training data. A caveat he names: a skill optimized on past posts sounds like the writer you were.

Two companion Every pieces add evidence. His "Writing Arena" benchmark (13 November) found a one-pass skill lost to simply handing the model a folder of the writer's posts for all five writers tested, until 10+ optimization rounds flipped four of them. And in a talk on personal benchmarks (11 November) he showed checks overfitting: told an ASCII cat was unrecognizable, a model wrote itself the rule "the cat sits facing front," then drew a front-facing cat when asked for one curled up asleep. A 22 November recap repeats the method.

### What changes
The style-guide page tells teams to build guides from real samples and keep them short; it has no evidence that a described style underperforms a tested one.

- **AI style guides** gains a "Test the skill, don't just describe it" section (brief, pairwise judge, optimizer, model-specific skills, Writing Arena), a revised current-guidance bullet and a new failure mode. Page date moves to 16 November.
- **Evals for agentic work** gains an overfitting caveat in its personal-benchmarks section. Page date moves to 11 November.
- New source pages for the essay and for the two companion stories.

### What to weigh
Scope: the triage also suggested an optimizer example on Automated harness optimization; it is left out because that page is about agent harnesses (its research half now lives on Harness evolution research), so the writing case lives on the style-guide page alone. The judge-consistency numbers stay there too rather than on the evals page, which is past its ceiling.

## Intended changes

- [ ] **Update** `wiki/training/ai-style-guides.md` — new `## Test the skill, don't just describe it` section after `## Instruction bloat`; revise one Current-guidance bullet; add one failure mode; add three source ids to `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-11-16 (list has 1, no spill); `as_of` 2026-10-05 → 2026-11-16
- [ ] **Update** `wiki/training/evals-for-agentic-work.md` — one paragraph added to `## Personal benchmarks for picking a model`; add `every-whats-left-for-humans-overfitting-2026-11-11` to `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-11-11 (list has 6, no spill); `as_of` 2026-10-26 → 2026-11-11
- [ ] **Update** `wiki/index.md` — refresh the AI style guides line's description and date, and the evals-for-agentic-work line's date
- [ ] **Create** `wiki/sources/newsletters/every-write-like-me-optimized-skill-2026-11-16.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/every-writing-arena-2026-11-13.md` — story page (Writing Arena item)
- [ ] **Create** `wiki/sources/newsletters/every-whats-left-for-humans-overfitting-2026-11-11.md` — story page (personal-benchmark overfitting caveat)

## Page drafts

### wiki/training/ai-style-guides.md (updated)

Frontmatter: `as_of: 2026-11-16`; append to `sources:` → `every-write-like-me-optimized-skill-2026-11-16, every-writing-arena-2026-11-13`.

`## Current guidance`, replace the bullet "Build from real examples of your writing rather than inventing rules in the abstract" with:

```
- Build from real examples of your writing rather than inventing rules in the abstract, and test the result blind against held-out examples; a guide that only describes your style can make drafts worse
```

Insert after the `## Instruction bloat` section, before `## Failure modes`:

```
## Test the skill, don't just describe it

Every's head of evals Mike Taylor (November 2026) compared a Claude-written "write like me" guide with three optimizers on 185 of his posts, 54 held out. The written guide lost to all three on 80–95% of held-out posts: it read like a list of his "greatest hits" (one-line paragraphs, signature phrases) and produced a caricature. For Opus 5.5, no skill beat the written skill 61% of the time. His method:

1. **Gather one format.** 12–25 published pieces from one publication; his 30 most recent posts beat the full archive because his style had changed. Meeting transcripts work if you have no samples; tweets and emails do not.
2. **Turn each piece into a brief.** Thesis, outline, facts, sources and quotes, with no phrasing or jokes, so a draft that sounds like you can be credited to the skill.
3. **Build a judge you can trust.** The judge sees the real piece and two drafts from the same brief and picks the closer one, run twice with the order swapped to cancel position bias, and notes how each draft differs. Consistency on swapped order: Opus 5.5 86%, Sonnet 5.5 70%, Jev 50%.
4. **Optimize instead of writing.** An optimizer (DSPy's GEPA won, ahead of Karpathy's autoresearch and Every's ce-optimize) keeps a skill change only if it scores better; the surviving rules are corrections drawn from the judge's notes, not preferences. Cost: $27–53 per skill against $5 for a one-shot guide; most gains come in three rounds.
5. **Optimize for the model you draft with.** Opus 5.5 rose from 16% with no skill to 93% with its optimized skill; Sonnet 5.5 with an optimized skill beat Opus 5.5 with the written guide on 46 of 60 judgments. Re-optimize when you switch models.
6. **Draft from a full brief and feed edits back.** A one-line prompt makes the skill invent plausible content in your voice; your edits on each draft are the next round's data.

His "Writing Arena" benchmark found the same across five Every writers: a one-pass skill lost to just handing the model a folder of the writer's posts for all five, and only after 10+ optimization rounds did the skill win for four. Limit: the judge rewards resemblance to past work, so the skill sounds like the writer you were; hold out your newest pieces. Taylor's skill is on GitHub (everyinc/compound-writing).
```

`## Failure modes`, append:

```
- Trusting a style description no one has tested: a guide of signature habits applied every time yields a caricature, and may score below no guide at all
```

`## Recent changes`: insert at the top:

```
- [2026-11-16] Added "Test the skill, don't just describe it": Mike Taylor's brief + pairwise-judge + optimizer method (written guide lost on 80–95% of held-out posts; GEPA best; skills are model-specific) and the Writing Arena result.
```

`## Sources`: append

```
- [Every — How I Finally Got AI to Write Like Me](../sources/newsletters/every-write-like-me-optimized-skill-2026-11-16.md)
- [Every — Writing Arena (Your Attention Is AI's New Bottleneck)](../sources/newsletters/every-writing-arena-2026-11-13.md)
```

### wiki/training/evals-for-agentic-work.md (updated)

Frontmatter: `as_of: 2026-11-11`; append `every-whats-left-for-humans-overfitting-2026-11-11` to `sources:`.

`## Personal benchmarks for picking a model`, append after the paragraph ending "Every is helping all its staff build one.":

```
Read the checks a model writes the way you would read a draft: they can overfit. Told its ASCII-art cat was unrecognizable, a model wrote a fair check and also the rule "the cat sits facing front," then drew a front-facing cat when asked for one curled up asleep. Taylor calls overfitting "the number one problem in AI right now"; keep testing on everyday work.
```

`## Recent changes`: insert at the top:

```
- [2026-11-11] Added an overfitting caveat to personal benchmarks: model-written checks can encode the wrong rule (Mike Taylor's front-facing-cat example).
```

`## Sources`: append

```
- [Every — What's Left for Humans After Automation (personal-benchmark overfitting)](../sources/newsletters/every-whats-left-for-humans-overfitting-2026-11-11.md)
```

### wiki/index.md (updated)

Before:

```
- [training/ai-style-guides](training/ai-style-guides.md) — how to externalize editorial taste and anti-patterns so AI writing stops drifting generic, and how to keep guides short so checkable rules don't crowd out judgment *(as_of: 2026-10-05)*
```

After:

```
- [training/ai-style-guides](training/ai-style-guides.md) — how to externalize editorial taste and anti-patterns so AI writing stops drifting generic, keep guides short so checkable rules don't crowd out judgment, and optimize a writing skill against your own work with a blind pairwise judge *(as_of: 2026-11-16)*
```

And on the `training/evals-for-agentic-work` line, change `*(as_of: 2026-10-26)*` to `*(as_of: 2026-11-11)*`.

### wiki/sources/newsletters/every-write-like-me-optimized-skill-2026-11-16.md (new)

```
---
title: "How I Finally Got AI to Write Like Me — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-16-how-i-finally-got-ai-to-write-like-me.md
url: https://every.to/also-true-for-humans/how-i-finally-got-ai-to-write-like-me
published: 2026-11-16
ingested: 2026-11-24
---

# How I Finally Got AI to Write Like Me — Every

Mike Taylor (Every's head of evals) tests four ways to build a "write like me" skill on 185 of his posts and finds that optimizing the skill against held-out posts with a blind pairwise judge beats a descriptive style guide. Gives a six-step method and releases the skill (github.com/everyinc/compound-writing). A 22 November Every recap (`raw/newsletters/2026-11-22-stop-telling-ai-how-you-write-show-it.md`) repeats the method in three steps.

## Influenced pages

- [AI style guides](../../training/ai-style-guides.md) — "Test the skill, don't just describe it" section

## Key claims extracted

- 185 posts (335,000 words, 13 publications); 54 held out; the 30 most recent Every posts optimized better than the full archive
- Each post turned into a style-free brief; drafts judged by a "pairwise gold triad" (real post + two drafts, order swapped)
- Judge consistency on swapped order: Opus 5.5 86%, Sonnet 5.5 70%, Jev 50%
- Claude-written style guide lost to autoresearch, GEPA and ce-optimize on 80–95% of held-out posts; for Opus 5.5 no skill beat it 61% of the time
- Optimizing costs $27–53 per skill vs $5 one-shot; most gains within three rounds; GEPA beat autoresearch 77–31 and ce-optimize 85–15
- Opus 5.5: 16% no skill → 93% with its GEPA skill; GPT-6 Astra 1% → 66%; Sonnet 5.5 + optimized skill beat Opus 5.5 + written skill on 46 of 60 judgments
- 44 edits on one draft versus hundreds in earlier experiments; time from opinion to piece about an hour instead of a day
- Caveat: the judge rewards resemblance to past work
```

### wiki/sources/newsletters/every-writing-arena-2026-11-13.md (new)

```
---
title: "Writing Arena — Every (Your Attention Is AI's New Bottleneck)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-13-your-attention-is-ais-new-bottleneck.md
url: https://every.to/context-window/your-attention-is-ai-s-new-bottleneck
published: 2026-11-13
ingested: 2026-11-24
---

# Writing Arena — Every (Your Attention Is AI's New Bottleneck)

Story page for one item in Every's 13 November Context Window: Mike Taylor's Writing Arena benchmark of "write like me" skills across Every writers.

## Influenced pages

- [AI style guides](../../training/ai-style-guides.md) — Writing Arena result

## Key claims extracted

- A one-pass "write like me" skill lost to handing the model a folder of the writer's posts, for all five writers tested
- After 10+ rounds of agent revision keeping only higher-scoring versions, the skill won for four of the five
- Advice: test a style skill blind against your own posts before trusting it
```

### wiki/sources/newsletters/every-whats-left-for-humans-overfitting-2026-11-11.md (new)

```
---
title: "What's Left for Humans After Automation — Every (personal-benchmark overfitting)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-11-whats-left-for-humans-after-automation.md
url: https://every.to/context-window/what-s-left-for-humans-after-automation
published: 2026-11-11
ingested: 2026-11-24
---

# What's Left for Humans After Automation — Every (personal-benchmark overfitting)

Story page for Every's 11 November Context Window recap of Mike Taylor's Thesis: 2027 talk on turning corrections into a personal benchmark, and its overfitting caveat.

## Influenced pages

- [Evals for agentic work](../../training/evals-for-agentic-work.md) — overfitting caveat in personal benchmarks

## Key claims extracted

- Each correction becomes a yes/no check an AI judge can apply to future outputs of the same task
- Checks can overfit: a model told its ASCII cat was unrecognizable gave itself the rule "the cat sits facing front" and then drew a front-facing cat when asked for a sleeping, curled-up one
- Taylor calls overfitting "the number one problem in AI right now"; "Reality is the ultimate eval"
```

## Schema / vocabulary additions

None.

## Open questions

None.
