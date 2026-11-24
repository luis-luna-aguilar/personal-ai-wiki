---
title: What AI labs report vs what independent tests find · whatmodel.sh
type: source
source_type: article
url: https://whatmodel.sh/claims
fetched: true
fetched_on: 2026-11-24
note: rendered page text (body innerText via Playwright); readability output kept only the 619-row pair table, which lives on the page and in the GitHub data
---

# What AI labs report vs what independent tests find · whatmodel.sh

whatmodel.sh / lab vs independent benchmark

all labs
●
Google
■
Meta
◆
OpenAI
▲
Anthropic
●
other makers
replay
save image
share ▾
How it's worked out
Each dot is one model on one test where its maker published a score and someone independent (a leaderboard, a paper, another lab running it) measured it too. 619 pairs, 187 models, 103 tests. Gaps are in percentage points on each test's own scale, not the whatmodel score.
Lab scores are 6.3% higher on average. For each matched pair, we calculate (lab score − independent score) ÷ independent score × 100, then average those percentages, weighting each pair equally. Lower lab scores and ties are included. For example, 60 vs 50 is 20% higher. The median percentage difference is 1.2%; the mean's 95% interval is 4.0%–10.2%, resampling whole models. 619 pairs have a nonzero independent baseline; zero baselines cannot have a relative percentage difference.
Whenever the scores differ, the lab's is higher 64% of the time: 381 lab higher, 218 independent higher, and 20 exact ties. Every nonzero difference counts, using the scores before display rounding; ties are excluded from that percentage. Its 95% interval is 58%–68%, resampling whole models since one model's pairs aren't independent.
Across all 619 pairs, including ties, the lab's number is higher 62% of the time (95% interval 56%–66%). The median gap is +0.7 points. The tables below use all pairs, including ties.
It depends on the test. Standard tests with a fixed format (MMLU, WinoGrande, ARC Challenge, HumanEval) barely move; tests where the setup is part of the result, like the agent harness on SWE-bench Verified, sampling and reasoning budget on AIME, or few-shot prompting on GSM8K and MBPP, show the biggest gaps.
Against neutral testers (leaderboards, Epoch AI, papers that don't release a model), the maker is higher 56% of 244 pairs; against rival labs' own release documents, 63% of 446. Where a rival and a neutral tester measured the same model on the same test (272 cases), the rival was lower 131 times and higher 130 times (median 0.0).
Gaps aren't all inflation: settings often differ (reasoning effort, agent harness, few-shot prompts, test subset or version), and labs choose which tests to publish, so these pairs aren't a random sample. When a side has several results for the same model and test, the dot uses their median. Accuracy tests only; arena ratings have no maker-reported twin. Hover a dot for both sources.
By test

Tests with 12 or more pairs.

Test	pairs	median gap	maker higher
SWE-bench Verified	13	+9.0	92%
MBPP	13	+9.0	77%
ARC Easy	14	+4.7	79%
AIME 2024	14	+3.8	86%
GSM8K	19	+3.3	84%
AIME 2025	20	+2.6	70%
MMLU-Pro	29	+2.0	69%
IFEval (aggregation unspecified)	13	+1.0	69%
GPQA Diamond	54	+0.9	69%
PIQA	16	+0.5	75%
Terminal-Bench 4.0	12	+0.3	58%
MMLU	20	0.0	50%
HumanEval	34	0.0	47%
WinoGrande	25	-0.1	40%
ARC Challenge	14	-0.6	50%
τ²-bench Telecom	18	-1.3	39%
By maker

Makers with 10 or more pairs. Small groups swing a lot: read these as rough.

Maker	pairs	median gap	maker higher
Alibaba Cloud	148	+1.1	61%
Meta	89	+0.7	62%
Google	49	+2.2	61%
EleutherAI	48	-0.1	40%
DeepSeek	47	+0.8	70%
OpenAI	37	+0.4	57%
Z.ai	27	+0.9	67%
Mistral AI	20	+1.6	75%
BigScience	20	-11.9	10%
BigCode	20	+2.2	95%
Liquid AI	15	-0.7	47%
Ai2	14	+8.8	93%
Microsoft	14	0.0	50%
IBM	13	+1.7	77%
Anthropic	13	+1.6	69%
All makers	619	+0.7	62%
All 619 pairs, biggest maker advantage first

Every result links to its source on the model's page. The data (CC BY-SA 4.0) and code (MIT) are on GitHub.

Scores, speeds, prices and memory figures are estimates derived from the public sources linked on each model's page. They can be incomplete, out of date or wrong, and aren't endorsed by the model makers or the sources. Check before you rely on them, and review any command before you run it. Model names and trademarks belong to their owners.

about · about the author · FAQ · contribute · sponsor · browse · model race · how far behind is your GPU · maker vs independent · how it works · sources · RSS · terms · privacy · contact · jake@whatmodel.sh · © 2026 Merlinsbeard Pty Ltd
