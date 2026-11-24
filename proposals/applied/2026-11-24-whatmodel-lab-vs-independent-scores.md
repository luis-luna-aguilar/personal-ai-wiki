---
type: proposal
source: raw/articles/2026-11-24-whatmodelsh-claims.md
sources:
  - raw/articles/2026-11-24-whatmodelsh-claims.md
  - raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
status: pending
created: 2026-11-24
---

# Proposal: whatmodel.sh — lab-reported vs independent benchmark scores

## Summary

### In short
Labs' own benchmark numbers run modestly but consistently above independent measurements, and the gap is widest exactly where the harness and settings are part of the result. Across 619 matched model-and-test pairs on the open whatmodel.sh leaderboard, the lab's score is higher 64% of the time when they differ and 6.3% higher on average, with SWE-bench Verified and MBPP showing median gaps of about 9 points. The proposal adds one paragraph to **Harness vs model** and a source page. Reason to hesitate: the leaderboard is live and undated, so its numbers drift (6.4% in October, 6.3% now).

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
whatmodel.sh is an open model leaderboard that collects published benchmark results with links to each source; its data and code are public. One of its pages pairs every case where a model's maker published a score and someone independent (a leaderboard, Epoch AI, a paper, or another lab running the model) measured the same model on the same test. On the live page there are 619 such pairs covering 187 models and 103 tests. When the two numbers differ, the maker's is higher 64% of the time; the average relative gap is 6.3%, but the median gap is only 0.7 points, so a minority of large differences drives the mean. Fixed-format tests such as MMLU, HumanEval and WinoGrande barely move. The gaps open on tests where setup decides the score: the agent harness on SWE-bench Verified, sampling and reasoning budget on AIME, few-shot prompting on GSM8K and MBPP. Against neutral testers the maker comes out higher in 56% of 244 pairs. The site itself says the gaps are not all inflation: settings differ, and labs choose which tests to publish. AINews picked the chart up from Reddit on 21 October, when it showed 611 pairs and a 6.4% average.

### What changes
**Harness vs model** already argues that a benchmark score belongs to model plus harness plus environment, with harness-swap experiments as evidence, but it has no measurement across published results.

- **Harness vs model** gains one paragraph under Measured evidence giving the lab-versus-independent figures and the per-test pattern, and a Recent-changes entry. Page date moves to 24 November.
- One new source page for the whatmodel.sh comparison.

### What to weigh
The page has no publication date and updates continuously, so the ingest date (24 November) is used and the live figures replace the October ones AINews quoted. The paragraph takes Harness vs model from 110% to about 121% of its length ceiling, past the warning band, so a split is offered in Open questions.

## Intended changes

- [ ] **Update** `wiki/concepts/harness-vs-model.md` — new paragraph at the end of `### Measured evidence`; Current status stamp and as_of 2026-10-06 → 2026-11-24; adds one Recent-changes entry dated 2026-11-24; adds source id and link
- [ ] **Create** `wiki/sources/articles/whatmodelsh-lab-vs-independent-2026-11-24.md` — source summary

## Page drafts

### wiki/concepts/harness-vs-model.md (updated)

Frontmatter: `as_of: 2026-11-24`; append `whatmodelsh-lab-vs-independent-2026-11-24` to `sources:`.

Heading: `## Current status (as of 2026-11-24)`.

New final paragraph of `### Measured evidence` (after the "Computer use shows the same split" paragraph):

```
Published scores show the same effect at scale. The open leaderboard whatmodel.sh matched 619 cases where a lab published a score for its own model and an independent party (a leaderboard, Epoch AI, a paper, a rival lab) measured the same model on the same test. When the two differ, the lab's number is higher 64% of the time, 6.3% higher on average, though the median gap is only 0.7 points. Fixed-format tests (MMLU, HumanEval, WinoGrande) barely move; tests where setup is part of the result move most, with median gaps of about 9 points on SWE-bench Verified (agent harness) and MBPP (few-shot prompting). The site attributes much of the gap to different settings and to labs choosing which tests to publish, not only to inflation. Read a lab's launch number as its best-tuned configuration.
```

`## Recent changes` — insert at the top (list goes from 8 to 9, no spill):

```
- [2026-11-24] Added whatmodel.sh's lab-vs-independent comparison: across 619 matched pairs the lab's score is higher 64% of the time when they differ, with the largest gaps on setup-sensitive tests (SWE-bench Verified, MBPP, about +9 points).
```

`## Sources` — append:

```
- [whatmodel.sh — What AI labs report vs what independent tests find](../sources/articles/whatmodelsh-lab-vs-independent-2026-11-24.md)
```

### wiki/sources/articles/whatmodelsh-lab-vs-independent-2026-11-24.md (new)

```
---
title: whatmodel.sh — What AI labs report vs what independent tests find
type: source
source_type: article
source_file: raw/articles/2026-11-24-whatmodelsh-claims.md
url: https://whatmodel.sh/claims
ingested: 2026-11-24
domains: [models]
---

# whatmodel.sh — What AI labs report vs what independent tests find

A page of the open whatmodel.sh leaderboard that pairs every maker-published benchmark score with an independent measurement of the same model on the same test, and summarizes the gap by test and by maker. The page is live and undated; figures are as fetched on 2026-11-24. AINews (2026-10-21, via Reddit) reported an earlier state: 611 pairs, 6.4% average.

## Influenced pages
- [Harness vs model](../../concepts/harness-vs-model.md) — new paragraph under Measured evidence

## Key claims extracted
- 619 pairs, 187 models, 103 tests; accuracy tests only
- Lab score higher in 381 pairs, independent higher in 218, 20 ties; lab higher 64% of the time when scores differ (95% interval 58–68%)
- Mean relative gap 6.3% (95% interval 4.0–10.2%); median relative gap 1.2%; median gap +0.7 points
- Largest median gaps: SWE-bench Verified +9.0 (maker higher 92%), MBPP +9.0 (77%), ARC Easy +4.7, AIME 2024 +3.8, GSM8K +3.3
- Near-zero: MMLU 0.0, HumanEval 0.0, WinoGrande −0.1
- Against neutral testers the maker is higher in 56% of 244 pairs; against rival labs' release documents, 63% of 446
- Stated causes beyond inflation: reasoning effort, agent harness, few-shot prompts, test subset or version, and labs choosing which tests to publish
- Data CC BY-SA 4.0, code MIT, on GitHub
```

## Schema / vocabulary additions

None.

## Open questions

- Harness vs model lands at about 121% of its concept ceiling (1,452 of 1,200 body words). Split now? The natural cut is `### The harness cycle and its dissent` (about 510 words: the train → absorb → shed essay, Hugging Face's multi-harness proxy, Alex Zhang's dissent, HarnessTax) into its own concept page, leaving a one-paragraph pointer, which would bring the page back to about 82%. Default: no split in this proposal; it can be done as a refactor.
	- Split
