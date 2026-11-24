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
