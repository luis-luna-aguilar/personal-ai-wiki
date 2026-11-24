---
title: 'Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented Design'
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-html-261028380.md
url: https://arxiv.org/abs/2610.28380
published: 2026-10-20
ingested: 2026-11-24
domains: [agents]
---

# Object-Oriented Harness (Google Cloud AI Research)

**The problem.** A harness is the code around a model: prompts, tools and control flow. Automatic harness optimizers such as Meta-Harness evolve one global harness for every task. Mixed workloads need different strategies, though, and a change that helps one task group can hurt another.

**The idea.** Borrow object-oriented programming. Start from a base harness class. During training, an evolution agent reads execution records, groups tasks, and writes a specialized subclass for each cluster. A subclass inherits everything and overrides only the methods that cluster needs, and can itself be subclassed. Design lessons record which edits helped and which failed, so later evolution does not repeat mistakes. At test time a router reads the task and a base run, then either picks a subclass or keeps the base result. Harness code is frozen before evaluation on held-out tasks.

**Reported results** (same Gemini 3.5 Flash executor throughout):
- AutomationBench (business workflows): 61.6% → 77.4%
- Workspace-Bench: 25.5% → 39.5%
- Best primary score on all three benchmarks against the base harness, Meta-Harness, Agentic Harness Engineering and Adaptive Auto-Harness. On AutomationBench it also used the fewest steps per trajectory.
- Spending the extra inference on best-of-K sampling or self-refinement of the base harness did not reliably match it.
- Inheritance matters: subclasses scored 4.96 points higher on Workspace-Bench than the same evolved code flattened into independent classes.
- On a deliberately out-of-distribution split (Toolathlon test apps disjoint from training), the router reused the base harness on every task, preserving its score. Meta-Harness's learned global harness reduced pass rates there.

**Why this is useful for our projects.** When one agent serves several kinds of tasks, the paper suggests evolving per-cluster variants that inherit a shared base, plus a router, instead of tuning one prompt-and-tool bundle for everything. Keeping a "fall back to base" option protects unfamiliar tasks.

## Influenced pages
- [Harness evolution research](../../concepts/harness-evolution-research.md) — "Specialized harnesses and evolved interfaces" section; HarnessDev status bullet reframed (applied to Automated harness optimization, then split out to this page)

## Key claims extracted
- Harness evolved as a class hierarchy of specialized subclasses with design lessons and a test-time router
- AutomationBench 61.6%→77.4%, Workspace-Bench 25.5%→39.5% with the same Gemini 3.5 Flash; up to ~15 points absolute over base
- Outperforms Meta-Harness and other global/specialized optimizers on all three benchmarks
- Best-of-K and self-refinement do not reliably close the gap
- Inheritance adds 4.96 points on Workspace-Bench over flattened classes
