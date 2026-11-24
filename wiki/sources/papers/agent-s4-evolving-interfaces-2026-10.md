---
title: Evolving Agent Interfaces (Agent S4)
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-html-261028601.md
url: https://arxiv.org/abs/2610.28601
published: 2026-10-20
ingested: 2026-11-24
domains: [agents, computer-use]
---

# Evolving Agent Interfaces (Agent S4, Simular)

**The problem.** Computer-use agents act through interfaces people built by hand. So an agent may type a spreadsheet cell by cell when one line of code would do, or print a 2,000-line file to find one function. Hand-building better tools, and the know-how of when to use each, cannot keep up with new apps and models.

**The idea.** Make interface design an agent's job. In Agent S4, a task agent works through synthetic training tasks. A meta-agent then reads its trajectories, with no labels saying which runs succeeded, spots where the interfaces held it back, and edits a repository of tools and usage notes. It mutates one repository or crosses two. Population-based evolution keeps the repositories that score best on validation tasks the meta-agent never sees, so changes that only fit the training tasks get filtered out. Task agent and meta-agent are the same open model (Qwen3.8-27B) in a modified Prime Agent harness.

**Reported results.**
- OSWorld V2 (108 tasks): 21.3% binary success with the evolved repository, 3.8x the same model with fixed interfaces. That is above GPT-5.5 (13.0%) and Claude Opus 4.8 (20.6%), at about 4.3% and 1.5% of their cost per task (their numbers are taken from the OSWorld V2 paper). The authors call it a new state of the art for open-source computer-use agents.
- ScienceBoard (niche scientific apps), separate evolution run: 41.4% → 58.6% with the same model.
- Code is open source.

**Why this is useful for our projects.** If an agent keeps doing something the slow way, the fix may be a better tool rather than a better model. Mining its own traces for missing tools, and checking each new tool on tasks it was not built from, is a cheap path that works with small open models.

## Influenced pages
- [Harness evolution research](../../concepts/harness-evolution-research.md) — Agent S4 bullet in "Specialized harnesses and evolved interfaces" (applied to Automated harness optimization, then split out to this page)

## Key claims extracted
- Meta-agent builds and revises interfaces and usage knowledge from trajectories without success labels
- Population-based selection on unseen validation tasks
- Qwen3.8-27B: 21.3% on OSWorld V2, 3.8x fixed interfaces, above GPT-5.5 (13.0%) and Opus 4.8 (20.6%) at ~4.3% and ~1.5% of their cost
- ScienceBoard 41.4% → 58.6% with the same model
- Open-source code
