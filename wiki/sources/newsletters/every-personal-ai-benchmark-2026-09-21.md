---
title: 'Every — How to Create Your Own Personal AI Benchmark'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-21-how-to-create-your-own-personal-ai-benchmark.md
url: https://every.to/also-true-for-humans/how-to-create-your-own-personal-ai-benchmark
published: 2026-09-21
ingested: 2026-10-20
domains: [training]
---

# Every — How to Create Your Own Personal AI Benchmark

Mike Taylor, Every's head of evals, explains how an individual can build a private benchmark from their own work to pick a daily-driver model and spot when a cheaper one is good enough. Three levels: collect about ten recent failures from session history and compare models side by side; turn dictated likes and dislikes into yes-or-no checks graded by a second model; then turn each task into a skill that accumulates 20+ cases with a gold example and an eval script. A 27 September Context Window recap (`raw/newsletters/2026-09-27-opus-55-and-sol-split-the-team.md`) repeats the method and adds nothing new.

## Influenced pages

- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — "Personal benchmarks for picking a model" section

## Key claims extracted

- Public benchmarks (MMLU-Pro, Math Olympiad) measure something, but not whether a model helps with your job
- Level 1: have the agent mine the past month's sessions for ~10 tasks that needed heavy back-and-forth or were abandoned; run them in parallel across models in an HTML viewer; compare large vs small, two providers, and three runs of one model
- "Back-pocket evals" (Steve Yegge): tasks AI failed at, rerun on each new model
- Level 2: dictate likes and dislikes, convert to yes/no checks, LLM-as-judge; avoid 100-point scales because ratings cluster around 4/5 or 70/100
- Taylor's 10-task consulting benchmark: Luna came within a few points of Fable; routine tasks sit below the "discernment horizon"
- Level 3: one skill per task that files brief, output and feedback until there are 20+ cases; folder per case with prompt.txt, context/, gold/, evals.py and an index.html viewer
- Benchmarks saturate and must be made harder over time (Mollick's otter test)
