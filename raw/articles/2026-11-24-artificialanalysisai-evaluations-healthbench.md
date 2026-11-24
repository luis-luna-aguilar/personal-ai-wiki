---
title: HealthBench Professional Benchmark
type: source
source_type: article
url: https://artificialanalysis.ai/evaluations/healthbench
fetched: 2026-11-24
---

# HealthBench Professional Benchmark

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
HealthBench Professional: Length-Adjusted Score
Share of rubric points earned, adjusted for answer length as OpenAI reports it · Independently benchmarked by Artificial Analysis
15 of 19 models
Claude Fable 5.2 (max)
GPT-6 Astra (max)
GPT-6.1 Sol (max)
Claude Sonnet 5.5 (max)
GPT-6 Sol (max)
GPT-6 Luna (max)
Claude Opus 5.5 (max)
Claude Haiku 5.5 (max)
Claude Fable 5.1 (max)
Grok 4.7 (xhigh)
Gemini 4 Argon (high)
Kimi K3 (max)
GLM-5.3 (max)
Gemini 3.8 Flash (high)
DeepSeek V4.1 Flash (max)
67.7%
66.0%
65.1%
63.0%
62.3%
61.9%
59.9%
58.4%
57.8%
55.8%
55.1%
53.2%
52.8%
51.7%
50.7%
Length-Adjusted Score vs. Cost per Task
Raw Score vs. Cost per Task
HealthBench Professional: Length-Adjusted Score vs. Cost per Task
HealthBench Professional score (length-adjusted) vs. average cost per task (USD)
15 of 19 models
Most attractive quadrant
Pareto line
Anthropic
OpenAI
Google
SpaceXAI
Z AI
DeepSeek
Kimi
Evaluation Cost per Task
HealthBench Professional: Score vs. Answer Length
Each model is drawn at its mean answer length, with a line from its raw score (faded) to its length-adjusted score · Answers longer than 2,000 characters lose score and shorter ones gain · Answer length excludes reasoning · Higher is better
15 of 19 models
Most attractive quadrant
No adjustment (2,000 characters)
Anthropic
OpenAI
Google
SpaceXAI
Z AI
DeepSeek
Kimi
HealthBench Professional: Score by Use Case, Type and Difficulty
Raw score with no length adjustment, as in OpenAI's original implementation · Higher is better
15 of 19 models
Token Usage
Output Tokens per Task
Score vs. Output Tokens per Task
Token Breakdown
Score vs. Output Tokens
HealthBench Professional: Output Tokens per Task
Output tokens used to run one task, broken down by reasoning and answer tokens
15 of 19 models
Answer
Reasoning
Evaluation Output Tokens per Task
Cost
Cost per Task
Total Cost to Run
HealthBench Professional: Cost per Task
Average cost per task (USD), broken down by input, cache hit, cache write, reasoning, and answer tokens
15 of 19 models
Answer
Reasoning
Cache Write
Cache Hit
Input
Evaluation Cost per Task
Speed
Time per Task
Score vs. Time per Task
HealthBench Professional: Time per Task
Output tokens divided by end-to-end output speed (minutes per task) · Speed at the model's own endpoint or the median across providers · Lower is better
15 of 19 models
Evaluation Time per Task
Score vs. Release Date
HealthBench Professional: Score vs. Release Date
15 of 19 models
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
Explore Evaluations
Artificial Analysis Intelligence Index v5.0.1

A composite benchmark aggregating nine challenging evaluations to provide a holistic measure of AI capabilities across knowledge work, coding, science, and general knowledge.

AA-Briefcase v1.1: Agentic Knowledge Work Benchmark

A private evaluation developed by Artificial Analysis for frontier agentic capability in long-horizon knowledge work, testing agents on realistic business workflows that require deliverables such as spreadsheets, presentations, and memos.

AA-3D: Interactive 3D Experience Benchmark

A benchmark developed by Artificial Analysis for how well AI models build interactive 3D experiences. Models work as agents in an offline sandbox via Stirrup to turn a written brief into a three.js scene, with Elo ratings derived from blind pairwise votes.

APEX-Agents-AA Benchmark

Artificial Analysis' implementation of the APEX-Agents benchmark, testing AI agents on long-horizon, cross-application tasks in professional-services environments with realistic application tooling.

AA-AnalystAgent Benchmark

Artificial Analysis' data analysis benchmark, testing AI agents on their ability to work with spreadsheets and documents to answer quantitative questions a Business Analyst or Data Analyst would face day-to-day.

AutomationBench-AA: Agentic SaaS Workflow Benchmark

A benchmark measuring agentic task completion across simulated SaaS application environments, scoring the share of each task's objectives completed without guardrail violations.

Harvey LAB-AA v1.1 Benchmark

Artificial Analysis' implementation of Harvey's Legal Agent Benchmark (LAB), testing AI agents on real-world legal work from Harvey's dataset of 120 private tasks spanning 24 legal practice areas. v1.1, built in collaboration with Harvey, checks every deliverable against the task's source documents for hallucinations, so work that passes every rubric criterion but contains a material hallucination receives no credit. A panel of three judges grades each deliverable criterion-by-criterion.

GDP.pdf Benchmark

Artificial Analysis' implementation of Surge AI's GDP.pdf benchmark, testing whether language models can reason over long, real-world professional documents and satisfy detailed task-specific criteria.

EnterpriseOps-Gym-AA Benchmark

Artificial Analysis' independent implementation of ServiceNow's EnterpriseOps-Gym, an agentic benchmark testing whether LLM agents can complete stateful, multi-step enterprise workflows across eight business domains via live tool use, graded on the final state of the underlying databases.

Terminal-Bench 4.0 Benchmark

A harder 66-task benchmark of complex terminal work across software, machine learning, science, operations, security, hardware, and media, with recalibrated compute and time allowances and improved instructions, environments, and verifiers.

Terminal-Bench-Science 0.1 Benchmark

A 70-task benchmark of research workflows authored and reviewed by domain experts across the life, physical, earth, mathematical, and engineering sciences, each completed in a terminal and checked by its own set of tests.

FrontierCode-AA 2.0 Benchmark

Artificial Analysis' implementation of Cognition's FrontierCode 2.0, a private agentic coding benchmark of 132 tasks in real open-source repositories, graded on whether a maintainer would merge the agent's change.

HLE-Diamond Benchmark

A refined and updated 1,000-question set of Humanity's Last Exam, split evenly between reasoning and knowledge questions, with 272 questions that include an image.

AA-PersonalityBench: AI Personality & Communication Style Benchmark

Measures how models communicate rather than whether they are correct: 30 judged personality traits rolled up into 8 indexes, plus 21 measured communication characteristics.

AA-Omniscience v1.1: Knowledge and Hallucination Benchmark

A benchmark measuring factual recall and hallucination across various economically relevant domains.

GPQA Diamond Benchmark

The most challenging 198 questions from GPQA, where PhD experts achieve 65% accuracy but skilled non-experts only reach 34% despite web access.

ITBench-AA Benchmark

Artificial Analysis' implementation of IBM's ITBench benchmark, testing AI agents on Kubernetes incident root-cause analysis from offline incident snapshots. The agent inspects alerts, events, traces, and topology and identifies the contributing-factor entities (deployments, pods, namespaces, network policies, etc.) responsible for the failure.

MMMU-Pro Benchmark

An enhanced MMMU benchmark that eliminates shortcuts and guessing strategies to more rigorously test multimodal models across 30 academic disciplines.

IFBench Benchmark

A benchmark evaluating precise instruction-following generalization on 58 diverse, verifiable out-of-domain constraints that test models' ability to follow specific output requirements.

MLCR-AA: Medical Long Context Reasoning Benchmark

An open benchmark from Wisedocs measuring how well models reason over long, fragmented medical records, performing the multi-document synthesis claims professionals rely on when reviewing insurance and healthcare cases.

Code2Video-AA Benchmark

Artificial Analysis' implementation of HeyGen's Code2Video Bench, evaluating how well models create short product and brand videos from 114 design briefs using HyperFrames HTML.

HealthBench Benchmark

OpenAI's HealthBench: 5,000 health conversations graded against physician-written rubrics, from emergency referrals to global health.

CritPt v2 Benchmark

CritPt v2 is the revised version of CritPt, a benchmark designed to test LLMs on research-level physics reasoning tasks, featuring 70 composite research challenges. Models solve problems with a code-execution tool in an offline Linux sandbox.

VIALS-AA Benchmark

VIALS-AA is Artificial Analysis' implementation of Handshake AI's VIALS benchmark. It tests whether language models can interpret scientific images and answer questions about the evidence they contain.

Multimodal Knowledge Agent (MKA) Benchmark

Artificial Analysis' implementation of Google DeepMind's Multimodal Knowledge Agent (MKA) benchmark. It tests whether agents can read visually dense project files, such as architectural drawings, engineering schematics and clinical scans, and produce the deliverables a professional would.

GDPval-AA v2.1 Benchmark

GDPval-AA v2.1 is Artificial Analysis' evaluation framework for OpenAI's GDPval dataset. It tests AI models on real-world tasks across 44 occupations and 9 major industries. Models are given shell access and web browsing capabilities in an agentic loop via Stirrup to solve tasks, with Elo ratings derived from blind pairwise comparisons.

𝜏³-Banking Benchmark

A fintech customer-support benchmark from the 𝜏-Knowledge framework that tests whether agents can navigate a large unstructured knowledge base and execute multi-step tool calls to resolve realistic banking workflows.

Terminal-Bench 2.1 Benchmark

A verified refresh of Terminal-Bench 2.0: 89 curated tasks across software engineering, system administration, data processing, model training, and security, with environment and instruction fixes so scores reflect agent capability rather than environment gaps.

FrontierCode 1.1 Benchmark

Artificial Analysis' implementation of Cognition's FrontierCode 1.1, a private agentic coding benchmark that tests models on completing coding tasks in a way that would actually get merged by maintainers of real-world repositories.

AA-LCR v1.1: Long Context Reasoning Benchmark

A challenging benchmark measuring language models' ability to extract, reason about, and synthesize information from long-form documents ranging from 10k to 100k tokens (measured using the cl100k_base tokenizer).

SciCode Benchmark

A scientist-curated coding benchmark featuring 288 test set subproblems from 80 laboratory problems across 16 scientific disciplines.

Humanity's Last Exam Benchmark

A frontier-level benchmark with 2,500 expert-vetted questions across mathematics, sciences, and humanities, designed to be the final closed-ended academic evaluation.

CritPt Benchmark

A benchmark designed to test LLMs on research-level physics reasoning tasks, featuring 71 composite research challenges.

Terminal-Bench Hard Benchmark

An agentic benchmark evaluating AI capabilities in terminal environments through software engineering, system administration, and data processing tasks.

𝜏²-Bench Telecom Benchmark

A dual-control conversational AI benchmark simulating technical support scenarios where both agent and user must coordinate actions to resolve telecom service issues.

MMLU-Pro Benchmark

An enhanced version of MMLU with 12,000 graduate-level questions across 14 subject areas, featuring ten answer options and deeper reasoning requirements.

LiveCodeBench Benchmark

A contamination-free coding benchmark that continuously harvests fresh competitive programming problems from LeetCode, AtCoder, and CodeForces, evaluating code generation, self-repair, and execution.

MATH-500 Benchmark

A 500-problem subset from the MATH dataset, featuring competition-level mathematics across six domains including algebra, geometry, and number theory.

AIME 2025 Benchmark

All 30 problems from the 2025 American Invitational Mathematics Examination, testing olympiad-level mathematical reasoning with integer answers from 000-999.

Global-MMLU-Lite Benchmark

A lightweight, multilingual version of MMLU, designed to evaluate knowledge and reasoning skills across a diverse range of languages and cultural contexts.

Get notified about new articles

Email address
Subscribe

Artificial Analysis

Explore

LLM Leaderboard
Image Arena
Video Arena
AI Agents
Evaluations

Products

Optima
MicroEvals
Model Recommender
Data Playground
Image Lab

Company

About
Methodology
Contact
Articles
Careers
X
LinkedIn
YouTube
Rednote
Discord

© 2026 Artificial Analysis

Terms of Use
Data Platform Terms
Privacy Policy
English
0.2
