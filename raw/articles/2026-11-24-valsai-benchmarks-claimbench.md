---
title: ClaimBench Leaderboard and Methodology
type: source
source_type: article
url: https://www.vals.ai/benchmarks/claimbench
published: 2026-11-20
fetched: true
fetched_on: 2026-11-24
note: rendered page text (body innerText via Playwright); readability output captured only a sample 10-K excerpt
---

# ClaimBench Leaderboard and Methodology

UPDATED 11/20/2026
Can a decision model automate checking whether a 10-K excerpt supports, contradicts or says nothing about a claim?
As of November 20, 2026, d1-ultra ranks first on ClaimBench among decision models with 100.00%, followed by Decider V1.3 (99.80%) and d1.2-ultra (99.75%).
ClaimBench
Can a decision model take over checking claims against SEC filings?
CLAIMBENCH
•
NOV 20, 2026
DECISION MODELS
ALL MODELS
ACCURACY
COST
FRONTIER
LOG SCALE
SHOWING LATEST, TOP & FRONTIER MODELS (15)
LAB:
BASETEN
GOOGLE
INCEPTION
LIQUID AI
NACE.AI
PERPLEXITY
TYPESAFE
Pinch or Ctrl/Cmd + scroll to zoom. Once zoomed, scroll or swipe with two fingers to pan, or drag to pan. Shift + drag draws a box to zoom into; turn on box zoom to draw one without Shift. Plus and minus keys zoom, arrow keys pan, 0 resets.
EFFICIENT
INEFFICIENT
LOWEST COST
BEST PERFORMANCE
96%
98%
100%
Decider V1.3
d1-ultra
d1.2
Decider Flash V1.3
$0.0001
$0.0002
$0.0003
$0.0004
$0.0005
ClaimBench leaderboard
Rank	Model	Accuracy	Cost / Claim	Latency
1	d1-ultra	100.00%	$0.000212	0.67s
2	Decider V1.3	99.80%	$0.000104	1.71s
3	d1.2-ultra	99.75%	$0.000212	0.43s
4	Mammoth 1	99.69%	$0.000520	0.36s
5	Decider V1.2	99.69%	$0.000104	1.23s
6	d1.2	99.49%	$0.000101	0.29s
7	Drex Max	99.18%	$0.000304	0.81s
8	Mercury Decide	99.08%	$0.000102	0.72s
9	Bison 1	99.08%	$0.000518	0.80s
10	Groundhog 1	99.03%	$0.000181	0.76s
11	Decider V1.1 27B	98.78%	$0.000104	0.51s
12	d1	98.67%	$0.000101	0.38s
13	Microsoft-Decision-1	98.21%	$0.000218	0.33s
14	Jev 1.14	98.06%	$0.000233	0.18s
15	Drex v1.5	98.01%	$0.000205	0.76s
16	Jev 1.13.0	97.65%	$0.000233	0.21s
17	Gemini Decision 1	97.50%	$0.000518	0.39s
18	Decider Flash V1.3	97.45%	$0.000052	0.19s
19	Elephant 1	97.30%	$0.000182	0.24s
20	Drex v2.0	97.30%	$0.000308	0.59s
21	GPT-6 Luna Decisions	96.89%	$0.000501	0.20s
22	Decider Flash V1.2	96.53%	$0.000052	1.09s
23	Clef	95.10%	$0.001260	1.40s
24	Solar Decide	94.39%	$0.000267	2.14s
25	Tev1 4B Experimental	89.80%	$0.000220	0.42s
26	Clef Omni	87.70%	$0.000783	0.42s
27	Classify-1	85.00%	$0.000215	1.24s
28	Clef Flash	84.85%	$0.000199	1.56s
29	Solar Decide Flash	82.45%	$0.000267	0.80s
30	Joey 1	81.17%	$0.000052	0.18s
ClaimBench
Can a decision model take over checking claims against SEC filings?
VIEW:
DECISION MODELS
TASK:
OVERALL
Systems (30)
Accuracy
Cost / Claim
Latency
1
d1-ultra
100.00
%
±0.00
, Accuracy details for d1-ultra
$
0.000212
0.67
s
2
Decider V1.3
99.80
%
±0.10
, Accuracy details for Decider V1.3
$
0.000104
1.71
s
3
d1.2-ultra
99.75
%
±0.11
, Accuracy details for d1.2-ultra
$
0.000212
0.43
s
4
Mammoth 1
99.69
%
±0.13
, Accuracy details for Mammoth 1
$
0.000520
0.36
s
5
Decider V1.2
99.69
%
±0.13
, Accuracy details for Decider V1.2
$
0.000104
1.23
s
6
d1.2
99.49
%
±0.16
, Accuracy details for d1.2
$
0.000101
0.29
s
7
Drex Max
99.18
%
±0.20
, Accuracy details for Drex Max
$
0.000304
0.81
s
8
Mercury Decide
99.08
%
±0.22
, Accuracy details for Mercury Decide
$
0.000102
0.72
s
9
Bison 1
99.08
%
±0.22
, Accuracy details for Bison 1
$
0.000518
0.80
s
10
Groundhog 1
99.03
%
±0.22
, Accuracy details for Groundhog 1
$
0.000181
0.76
s
11
Decider V1.1 27B
98.78
%
±0.25
, Accuracy details for Decider V1.1 27B
$
0.000104
0.51
s
12
d1
98.67
%
±0.26
, Accuracy details for d1
$
0.000101
0.38
s
13
Microsoft-Decision-1
98.21
%
±0.30
, Accuracy details for Microsoft-Decision-1
$
0.000218
0.33
s
14
Jev 1.14
98.06
%
±0.31
, Accuracy details for Jev 1.14
$
0.000233
0.18
s
15
Drex v1.5
98.01
%
±0.32
, Accuracy details for Drex v1.5
$
0.000205
0.76
s
16
Jev 1.13.0
97.65
%
±0.34
, Accuracy details for Jev 1.13.0
$
0.000233
0.21
s
VIEW 14 MORE MODELS
Analysts and lawyers check each statement in a report or brief against the filing it cites. The work is routine and high-volume, and an error that slips through matters more than a slow answer. Frontier language models do it well, but at volume their cost and delay add up.
A decision model is a small model that picks one answer from a fixed list, with a probability for each, in a single call. It is cheap and fast, and its probabilities show when it is unsure. The question is how much checking it can take over: the claims it is confident about, within a set error budget, with the rest sent to a person or a stronger model.
ClaimBench has 1,960 claims, each paired with an excerpt from a 10-K. A system says whether the excerpt supports the claim, contradicts it, or says nothing about it. Below: how many claims each decision model can answer alone within a 1% error budget, which kinds of claim trip it up, and what it costs to send the rest to a language model.
LANGUAGE MODELS
100.0%
Top accuracy, reached by 4 models from $0.0025 per claim
DECISION MODEL ALONE
100.0%
Share of claims Decider V1.3 answers on its own within a 1% error budget
LATENCY
1.7 s
Per claim for Decider V1.3, against 5.1 s for Claude Haiku 5.5
CASCADE
$0.10
Per 1,000 claims for Decider V1.3 in front of Claude Haiku 5.5, whose label call alone costs $1.19
Which claims a decision model can take over
Accuracy by kind of claim
TASK TYPE
EXCERPT LENGTH
AT MOST 1% ERRORS
SYSTEM	DIRECT SUPPORT	SUBTLE CONTRADICTION	NUMERIC DISCREPANCY	MISSING EVIDENCE	NON-SUPPORTING CITATION	OVERALL
d1-ultra
	100.0%	100.0%	100.0%	100.0%	100.0%	100.0%
Decider V1.3
	100.0%	99.0%	100.0%	100.0%	100.0%	99.8%
d1.2-ultra
	100.0%	98.7%	100.0%	100.0%	100.0%	99.7%
Decider V1.2
	100.0%	98.5%	100.0%	100.0%	100.0%	99.7%
Mammoth 1
	100.0%	98.7%	100.0%	100.0%	99.7%	99.7%
d1.2
	100.0%	97.7%	100.0%	100.0%	99.7%	99.5%
Bison 1
	100.0%	95.7%	99.7%	100.0%	100.0%	99.1%
Groundhog 1
	100.0%	95.2%	100.0%	100.0%	100.0%	99.0%
Decider V1.1 27B
	100.0%	93.9%	100.0%	100.0%	100.0%	98.8%
Microsoft-Decision-1
	99.7%	91.8%	99.5%	100.0%	100.0%	98.2%
Drex Max
	99.2%	98.2%	98.5%	100.0%	100.0%	99.2%
Mercury Decide
	98.0%	97.7%	100.0%	100.0%	99.7%	99.1%
d1
	99.0%	94.6%	99.7%	100.0%	100.0%	98.7%
Jev 1.14
	99.5%	92.6%	98.7%	100.0%	99.5%	98.1%
Drex v1.5
	99.2%	92.6%	99.0%	100.0%	99.2%	98.0%
Gemini Decision 1
	99.5%	90.1%	98.7%	99.7%	99.5%	97.5%
Decider Flash V1.3
	100.0%	89.0%	98.5%	100.0%	99.7%	97.4%
Elephant 1
	100.0%	87.8%	99.0%	100.0%	99.7%	97.3%
Decider Flash V1.2
	100.0%	83.9%	99.0%	100.0%	99.7%	96.5%
Clef
	99.7%	79.6%	96.4%	100.0%	99.7%	95.1%
Jev 1.13.0
	99.5%	92.1%	98.0%	100.0%	98.7%	97.7%
GPT-6 Luna Decisions
	98.2%	88.0%	98.2%	100.0%	100.0%	96.9%
Solar Decide
	99.0%	78.3%	96.4%	100.0%	98.2%	94.4%
Tev1 4B Experimental
	98.5%	68.6%	84.0%	99.7%	98.2%	89.8%
Clef Omni
	98.2%	55.9%	88.0%	99.5%	96.9%	87.7%
Drex v2.0
	98.7%	94.1%	98.0%	98.2%	97.4%	97.3%
Classify-1
	88.0%	66.8%	74.8%	97.7%	97.7%	85.0%
Clef Flash
	99.0%	59.9%	74.3%	96.4%	94.6%	84.8%
Solar Decide Flash
	91.6%	55.9%	75.6%	97.4%	91.8%	82.4%
Joey 1
	92.3%	49.5%	77.6%	95.2%	91.3%	81.2%
When a decision model is unsure
Error against claims answered alone
ACROSS: SHARE OF HELD-OUT CLAIMS A MODEL ANSWERS ALONE.
UP: SHARE OF THOSE ANSWERS THAT ARE WRONG.
DOT: ITS TUNED THRESHOLD.
GREEN: AT MOST 1% WRONG.
Decider V1.3
100.0% alone, 0.15% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Drex Max
99.9% alone, 0.58% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
d1-ultra
99.9% alone, 0.00% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Mammoth 1
99.9% alone, 0.15% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
d1.2
99.8% alone, 0.22% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Decider V1.2
99.7% alone, 0.15% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
d1.2-ultra
99.4% alone, 0.00% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Decider V1.1 27B
99.3% alone, 0.73% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Groundhog 1
98.8% alone, 0.52% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Mercury Decide
98.8% alone, 0.59% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Bison 1
98.3% alone, 0.37% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
d1
97.7% alone, 0.59% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Drex v2.0
95.5% alone, 0.53% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Gemini Decision 1
94.0% alone, 1.16% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Jev 1.14
93.0% alone, 0.39% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Elephant 1
90.8% alone, 0.48% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Jev 1.13.0
88.0% alone, 0.58% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Drex v1.5
81.0% alone, 0.18% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Decider Flash V1.3
79.4% alone, 0.37% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
GPT-6 Luna Decisions
79.4% alone, 1.10% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Decider Flash V1.2
55.5% alone, 0.39% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Solar Decide
44.8% alone, 1.14% wrong
0%
5%
10%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Joey 1
21.2% alone, 0.68% wrong
0%
5%
10%
15%
20%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Solar Decide Flash
17.1% alone, 1.28% wrong
0%
5%
10%
15%
20%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Tev1 4B Experimental
15.6% alone, 0.93% wrong
0%
5%
10%
15%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Clef Flash
3.4% alone, 8.51% wrong
0%
5%
10%
15%
20%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Microsoft-Decision-1
2.9% alone, 7.50% wrong
0%
5%
10%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Classify-1
2.3% alone, 0.00% wrong
0%
5%
10%
15%
20%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Clef
1.7% alone, 4.17% wrong
0%
1%
3%
5%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Clef Omni
1.7% alone, 20.83% wrong
0%
5%
10%
15%
20%
25%
CLAIMS ANSWERED ALONE
WRONG
0%
50%
100%
Each decision model in front of Claude Haiku 5.5
GPT-6 LUNA
CLAUDE HAIKU 5.5
GPT-6.1 SOL
CLAUDE SONNET 5.5
CLAUDE OPUS 5.5
1,376 HELD-OUT CLAIMS. BELOW ITS THRESHOLD, A CLAIM GOES TO CLAUDE HAIKU 5.5. DASHED: ITS LABEL CALL ALONE.
SYSTEM	COST / 1,000 CLAIMS ↓	ACCURACY ↑	AUTOMATED ↑
Decider V1.3
$0.10
	99.85%	
100.0%
d1.2
$0.11
	99.78%	
99.8%
Decider V1.2
$0.11
	99.85%	
99.7%
Decider V1.1 27B
$0.11
	99.27%	
99.3%
Mercury Decide
$0.12
	99.42%	
98.8%
d1
$0.13
	99.42%	
97.7%
Groundhog 1
$0.21
	99.49%	
98.8%
d1-ultra
$0.22
	100.00%	
99.9%
d1.2-ultra
$0.22
	100.00%	
99.4%
Drex Max
$0.31
	99.42%	
99.9%
Elephant 1
$0.33
	99.56%	
90.8%
Jev 1.14
$0.34
	99.64%	
93.0%
Decider Flash V1.3
$0.35
	99.71%	
79.4%
Drex v2.0
$0.39
	99.49%	
95.5%
Jev 1.13.0
$0.41
	99.49%	
88.0%
Drex v1.5
$0.47
	99.85%	
81.0%
Mammoth 1
$0.53
	99.85%	
99.9%
Bison 1
$0.55
	99.64%	
98.3%
Gemini Decision 1
$0.63
	98.91%	
94.0%
Decider Flash V1.2
$0.64
	99.78%	
55.5%
GPT-6 Luna Decisions
$0.77
	99.13%	
79.4%
Solar Decide
$0.92
	99.49%	
44.8%
Joey 1
$1.15
	99.85%	
21.2%
Tev1 4B Experimental
$1.29
	99.85%	
15.6%
Solar Decide Flash
$1.32
	99.78%	
17.1%
Microsoft-Decision-1
$1.36
	99.78%	
2.9%
Clef Flash
$1.37
	99.71%	
3.4%
Classify-1
$1.40
	100.00%	
2.3%
Clef Omni
$1.97
	99.64%	
1.7%
Clef
$2.46
	99.93%	
1.7%
Claude Haiku 5.5
$1.19
	100.00%	—
Claims
A system gets a claim, a 10-K excerpt and the three labels below, and returns one label, with a probability for each label when it can. Every system gets the same instruction: judge only from the excerpt, not from outside knowledge of the company.
LABEL	MEANING
supported	The excerpt states or directly entails the claim.
contradicted	The excerpt states something that conflicts with the claim.
insufficient_evidence	The excerpt neither supports nor contradicts the claim.
v1 has five categories of about 392 claims each. Gold labels come from the construction rule, never from a model. Excerpts are short (a paragraph), medium (about 2k to 4k tokens) or long (about 8k to 16k tokens).
CATEGORY	GOLD LABEL	HOW THE CLAIM IS BUILT
Direct support	supported	A model paraphrases a sentence of the excerpt.
Subtle contradiction	contradicted	A model makes a small edit to a sentence of the excerpt. Numbers stay the same, a plain negation is rejected, and the wording stays close to the original.
Numeric discrepancy	contradicted	One amount or percentage in a sentence of the excerpt is changed to a plausible wrong value. Sentences with a bound, such as “more than” or “at least”, are excluded.
Missing evidence	insufficient_evidence	A sentence from a different passage of the same filing, with little wording in common with the excerpt.
Non-supporting citation	insufficient_evidence	A sentence from one company, paired with similar prose from another.
The class mix is uneven: 392 supported, 785 contradicted and 783 with insufficient evidence, so always guessing one label scores about 40% accuracy.
Missing evidence and non-supporting citation use sentences copied from filings. The other three categories use edited or generated text, which can carry stylistic quirks, so read the two groups separately.
Examples
Three of the 10 public examples: the shortest for each label, picked by rule and not by reading them first.
Direct support
SOURCE
Danaher Corp, 10-K filed 2026‑02‑24
CLAIM
Interest rate swap contracts were employed by the Company to hedge against cash flow fluctuations resulting from shifts in benchmark interest rates associated with a part of the debt issued by the Company.
EXCERPT
The Company used interest rate swap agreements to hedge the variability in cash flows due to changes in benchmark interest rates related to a portion of the debt the Company issued. These contracts effectively fixed the interest rate for a portion of the Company’s debt equal to the notional amount of the swaps to the rate specified in the interest rate swap agreements and were settled in November 2019 and December 2021. The changes in the fair value of these instruments were recorded in accumulated OCI prior to the issuance of the debt and are subsequently being reclassified to interest expense over the life of the related debt.
CORRECT ANSWER
supported.
Subtle contradiction
SOURCE
Morgan Stanley, 10-K filed 2026‑02‑19
CLAIM
The protection afforded in those jurisdictions may be more established and/or predictable than in the U.S. or other jurisdictions in which we operate.
EXCERPT
We conduct business in various jurisdictions outside the U.S., including jurisdictions that may not have comparable levels of protection for their corporate assets, such as intellectual property, trademarks, trade secrets, know-how, and customer information and records. The protection afforded in those jurisdictions may be less established and/or predictable than in the U.S. or other jurisdictions in which we operate. As a result, there may also be heightened risks associated with the potential theft of their data, technology and intellectual property in those jurisdictions by domestic or foreign actors, including private parties and those affiliated with or controlled by state actors. Additionally, we are subject to complex and evolving U.S. and international laws and regulations governing areas such as cybersecurity, privacy and data governance, transfer and protection, which may differ and potentially conflict, in various jurisdictions or cause us to develop or enhance controls that may encumber
CORRECT ANSWER
contradicted. The claim changes "less established" in the filing to "more established".
Non-supporting citation
SOURCE
Claim from BlackRock, Inc., excerpt from Nucor Corp, 10-K filed 2026‑02‑25
CLAIM
BlackRock FMC is also subject to the China Securities Law and various other financial laws and regulations.
EXCERPT
Show the medium excerpt
CORRECT ANSWER
insufficient_evidence. The claim is about a different company than the excerpt, on a similar topic.
Methodology
Cost and latency are per claim. A language model makes two calls per claim, a label and then a probability for each label, so its figures cover both. Latency is the time the model took, as the gateway measured it, and leaves out the hop between the sandbox and the gateway.
A decision model answers a claim itself when its top probability reaches a threshold: the lowest one that keeps at most 1% of answers wrong on a fixed 30% of the claims. It is then frozen and applied to the other 70%, the held-out claims. In the cascade table the rest go to the language model’s label call, and the cost is the decision model’s on every held-out claim plus that call on the claims it sends.
Related benchmarks
More finance benchmarks
Finance Agent v2.1
Core financial analyst tasks
Excel Modeling Benchmark v1.1
Building Excel financial models
Tax Agent Bench
Agentic US corporate tax research
BENCHMARKS
MODELS
COMPARISON
VALS SMITH
APP REPORTS
ABOUT
METHODOLOGY
NEWS
BLOG
GOVERNMENT
INCIDENTS
SECURITY
CAREERS
Copyright © 2026 Vals AI. All rights reserved.
X (TWITTER)
LINKEDIN
V
A
L
S
I
N
D
E
X
