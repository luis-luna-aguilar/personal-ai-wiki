---
title: "HealthBench (general) leaderboard tab — Artificial Analysis"
url: https://artificialanalysis.ai/evaluations/healthbench
published: 2026-11-24
fetched: true
note: rendered via aside; "HealthBench" tab of the page (the Professional tab is in 2026-11-24-artificialanalysisai-evaluations-healthbench.md); no publication date on the page, date is the fetch date
---

Artificial Analysis
Models
Coding Agents
Image, Speech, Video
Inference
Leaderboards
About
AI Trends
Premium
Log in

All evaluations

HealthBench Professional Benchmark
Reasoning
Writing
Knowledge Work
Medical
OpenAI's HealthBench Professional: 525 clinician conversations covering consult, writing and research tasks, graded against physician-written rubrics.
Background
HealthBench Professional
 is OpenAI's benchmark of 525 conversations with clinicians, split into consult, writing and research use cases. Each conversation comes with a rubric written by physicians, and the model's final reply is graded against it. It includes red-teaming conversations and conversations OpenAI marks as difficult.
Scoring uses a rubric of criteria, each worth -10 to +10 points. A judge model reads the full transcript, the conversation plus the model's reply, and checks whether the reply meets each criterion. A task scores the points of the criteria it meets (negative points subtract) over the positive points available, so a single task can score below zero. We use GPT-5.4 (low) as the judge, as in OpenAI's original implementation. We run 4 repeats per task and report the mean across all repeats.
We report the length-adjusted score and the raw score. The length-adjusted score lowers the score of replies longer than 2,000 characters and raises the score of shorter ones. A chart below plots each model's raw and length-adjusted scores against its mean answer length. The breakdowns by use case, type and difficulty use the raw score, as in OpenAI's original implementation.
Methodology
All evaluations are conducted independently by Artificial Analysis. More information can be found in our HealthBench Professional methodology
.
Related Links
HealthBench Methodology
2604.27470
openai/simple-evals
HealthBench Professional
Claude Fable 5.2 (Xhigh, Default Fallback) scores the highest on HealthBench Professional with a score of 68.1%, followed by Claude Fable 5.2 (Max, Default Fallback) with a score of 67.7% and Claude Fable 5.2 (High, Default Fallback) with a score of 67.6%
Cost per Task
GPT-6 Luna (Max) has the lowest cost per task on HealthBench Professional, at $0.0041, followed by DeepSeek V4.1 Flash (Max) at $0.0099 and Gemini 3.8 Flash (High) at $0.0103
Output Tokens Used
Claude Fable 5.2 (Low, Default Fallback) uses the fewest output tokens to run HealthBench Professional, with 1.05M, followed by Claude Fable 5.2 (Medium, Default Fallback) with 1.17M and Gemini 3.8 Flash (High) with 1.38M
HealthBench Professional
HealthBench
Score
Token Usage
Cost
Speed
Score vs. Release Date
Score
Length-Adjusted Score
Raw Score
HealthBench: Length-Adjusted Score
Share of rubric points earned, adjusted for answer length as OpenAI reports it · Independently benchmarked by Artificial Analysis
17 of 29 models
Claude Sonnet 5.5 (max)
DeepSeek V4.1 Flash (max)
Claude Fable 5.2 (max)
GPT-6.1 Sol (max)
Claude Haiku 5.5 (max)
GPT-6 Astra (max)
Claude Fable 5.1 (max)
Claude Opus 5.5 (max)
Grok 4.7 (xhigh)
Kimi K3 (max)
GPT-6 Luna (max)
GLM-5.3 (max)
GPT-6 Sol (max)
GPT-6.2 Sol (max)
GPT-6.2 Astra (max)
Gemini 4 Argon (high)
Gemini 3.8 Flash (high)
62.1%
60.9%
59.6%
58.5%
58.5%
58.2%
57.2%
57.0%
56.0%
54.7%
54.6%
54.5%
54.2%
53.9%
53.5%
49.1%
48.4%
Length-Adjusted Score vs. Cost per Task
Raw Score vs. Cost per Task
HealthBench: Length-Adjusted Score vs. Cost per Task
HealthBench score (length-adjusted) vs. average cost per task (USD)
17 of 29 models
Most attractive quadrant
Pareto line
Anthropic
OpenAI
Google
SpaceXAI
Z AI
DeepSeek
Kimi
$0.002
$0.003
$0.004
$0.006
$0.008
$0.01
$0.02
$0.03
$0.04
$0.06
$0.08
$0.1
$0.2
$0.3
$0.4
$0.5
Cost per Task (USD, Log Scale)
46%
48%
50%
52%
54%
56%
58%
60%
62%
64%
HealthBench (Length-Adjusted)
GPT-6 Luna (max)
Claude Opus 5.5 (max)
Claude Fable 5.1 (max)
DeepSeek V4.1 Flash (max)
GPT-6 Astra (max)
Claude Haiku 5.5 (max)*
GPT-6 Sol (max)
Kimi K3 (max)
GPT-6.2 Sol (max)
GLM-5.3 (max)
Grok 4.7 (xhigh)
Claude Sonnet 5.5 (max)
Claude Fable 5.2 (max)
GPT-6.1 Sol (max)
GPT-6.2 Astra (max)
Gemini 3.8 Flash (high)
Gemini 4 Argon (high)
Evaluation Cost per Task
HealthBench: Score vs. Answer Length
Each model is drawn at its mean answer length, with a line from its raw score (faded) to its length-adjusted score · Answers longer than 2,000 characters lose score and shorter ones gain · Answer length excludes reasoning · Higher is better
17 of 29 models
Most attractive quadrant
No adjustment (2,000 characters)
Anthropic
OpenAI
Google
SpaceXAI
Z AI
DeepSeek
Kimi
HealthBench: Score by Theme and Axis
Raw score with no length adjustment, as in OpenAI's original implementation · Axis scores count only the rubric items tagged with that axis · Higher is better
17 of 29 models
Token Usage
Output Tokens per Task
Score vs. Output Tokens per Task
Token Breakdown
Score vs. Output Tokens
HealthBench: Output Tokens per Task
Output tokens used to run one task, broken down by reasoning and answer tokens
17 of 29 models
Answer
Reasoning
Evaluation Output Tokens per Task
Cost
Cost per Task
Total Cost to Run
HealthBench: Cost per Task
Average cost per task (USD), broken down by input, cache hit, cache write, reasoning, and answer tokens
17 of 29 models
Answer
Reasoning
Cache Write
Cache Hit
Input
Evaluation Cost per Task
Speed
Time per Task
Score vs. Time per Task
HealthBench: Time per Task
Output tokens divided by end-to-end output speed (minutes per task) · Speed at the model's own endpoint or the median across providers · Lower is better
17 of 29 models
Evaluation Time per Task
Score vs. Release Date
HealthBench: Score vs. Release Date
17 of 29 models
Most attractive region
Anthropic
OpenAI
Google
SpaceXAI
Z AI
DeepSeek
Kimi
Frequently Asked Questions
What is HealthBench Professional?
How is HealthBench Professional different from HealthBench?
What is the length-adjusted score?
Which AI model has the highest HealthBench Professional score?
How are failed replies scored?

