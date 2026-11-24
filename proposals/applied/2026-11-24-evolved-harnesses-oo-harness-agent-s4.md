---
type: proposal
source: raw/papers/2026-11-24-arxivorg-html-261028380.md
sources:
  - raw/papers/2026-11-24-arxivorg-html-261028380.md
  - raw/papers/2026-11-24-arxivorg-abs-261028380.md
  - raw/papers/2026-11-24-arxivorg-html-261028601.md
  - raw/papers/2026-11-24-arxivorg-abs-261028601.md
  - raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
status: pending
created: 2026-11-24
---

# Proposal: Evolved harnesses and interfaces beat hand-built ones on a fixed model (OO-Harness, Agent S4)

## Summary

### In short
Two October papers show that a harness or tool set evolved offline from execution records can beat the hand-built one by 14–17 points without touching the model. Google's OO-Harness grows a family of specialized harness subclasses with a router. Simular's Agent S4 has a meta-agent write new computer-use interfaces from unlabeled trajectories. With those interfaces, an open 27B model beats GPT-5.5 and Opus 4.8 on OSWorld V2. The proposal adds a section to Automated harness optimization and softens its "self-evolved harnesses still lag" status line. The reason to hesitate is length: the page goes past its warning line.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Both papers went up on arXiv on 20 October 2026, and AINews covered them on 22 October. Both optimize what surrounds a fixed model and freeze the result before testing on tasks the search never saw.

OO-Harness ("Object-Oriented Harness") comes from Google Cloud AI Research. Its starting point is that one global harness struggles when tasks need different strategies. So an evolution agent reads execution records and builds a class hierarchy. Each specialized harness is a subclass that inherits the base and overrides only what its task cluster needs. Design lessons record which changes helped and which failed. At test time, a router looks at the task and a base run, then picks a subclass or keeps the base result. With the same Gemini 3.5 Flash executor, AutomationBench rose from 61.6% to 77.4% and Workspace-Bench from 25.5% to 39.5%. It beat Meta-Harness and other global optimizers on all three benchmarks. Spending the same extra inference on best-of-K sampling or self-refinement did not reliably help. On deliberately out-of-distribution tasks the router fell back to the base harness, while Meta-Harness's learned harness lowered pass rates.

Agent S4 comes from researchers working at Simular. A meta-agent studies a computer-use agent's trajectories on synthetic tasks, with no success labels. It writes better interfaces, for example a bulk spreadsheet edit instead of typing cell by cell, plus notes on when to use each. Population-based selection keeps the interface sets that score best on validation tasks the meta-agent never sees. With the evolved interfaces, Qwen3.8-27B reached 21.3% on OSWorld V2. That is 3.8 times the same model with fixed interfaces and above GPT-5.5 (13.0%) and Opus 4.8 (20.6%), at about 4.3% and 1.5% of their cost. ScienceBoard success rose from 41.4% to 58.6%. The code is open source.

### What changes
The Automated harness optimization page covers eval-driven hill-climbing, label-free per-task refinement (Harness²) and self-modifying harnesses. Its status section cites ByteDance's HarnessDev finding that self-evolved harnesses still lag human-engineered ones in several domains.

- **Automated harness optimization** gains a section, "Specialized harnesses and evolved interfaces", with both papers. The HarnessDev status bullet now reads as mixed evidence: offline evolution with held-out selection beat the hand-built starting point. The Current-status date moves to 20 October, the page date stays 26 October, and one Recent-changes entry is added.
- The index line names both systems.
- Two new paper source pages, in plain language.

### What to weigh
The claims used were checked against both papers' text on arXiv. The page is already 107% of its 1,200-word concept ceiling, and this adds about 200 words, leaving it near 123%. That is still below the 150% line where a split becomes mandatory. The open question offers a split instead of compressing the new content.

## Intended changes

- [ ] **Update** `wiki/concepts/automated-harness-optimization.md` — new `## Specialized harnesses and evolved interfaces` section after "Recursive harnessing without ground truth"; one sentence appended to the HarnessDev status bullet; Current-status stamp 2026-10-09 → 2026-10-20; adds one Recent-changes entry dated 2026-10-20, inserted between the 2026-10-26 and 2026-10-19 entries (list goes from 6 to 7, no spill); append two source ids and Sources lines; `as_of` stays 2026-10-26
    > See draft below

- [ ] **Update** `wiki/index.md` — refresh the automated-harness-optimization description (date unchanged)
    > See draft below

- [ ] **Create** `wiki/sources/papers/oo-harness-2026-10.md` — source summary

- [ ] **Create** `wiki/sources/papers/agent-s4-evolving-interfaces-2026-10.md` — source summary

## Page drafts

### wiki/concepts/automated-harness-optimization.md (updated)

Frontmatter: append `oo-harness-2026-10, agent-s4-evolving-interfaces-2026-10` to `sources:`. `as_of` unchanged.

Heading: `## Current status (as of 2026-10-09)` → `## Current status (as of 2026-10-20)`.

Replace the second Current-status bullet:

```md
- Self-improvement helps unevenly: ByteDance's HarnessDev finds self-evolved harnesses still lag human-engineered ones on code, search, and research, but match or beat them on writing and ML experimentation. Offline evolution with held-out selection does better: Google's OO-Harness and Simular's Agent S4 (October 2026) beat their hand-built starting harness or interfaces by 14–17 points on the same model — see below.
```

Insert a new section after `## Recursive harnessing without ground truth` and before `## Self-improving skills`:

```md
## Specialized harnesses and evolved interfaces

Two October 2026 papers evolve the harness offline on training tasks, then freeze it and test on held-out tasks with the same model.

- **OO-Harness (Google Cloud AI Research).** An evolution agent builds a class hierarchy instead of one global harness. Subclasses inherit the base and override only what a task cluster needs, design lessons record which changes helped, and a router picks a subclass per task after a base run. On the same Gemini 3.5 Flash, AutomationBench rose from 61.6% to 77.4% and Workspace-Bench from 25.5% to 39.5%, ahead of Meta-Harness on all three benchmarks. Spending that inference on best-of-K or self-refinement did not reliably help. On out-of-distribution tasks the router kept the base harness, while Meta-Harness's global harness lowered pass rates.
- **Agent S4 (Simular).** A meta-agent reads a computer-use agent's trajectories, with no success labels, and writes new interfaces (a bulk spreadsheet edit instead of cell-by-cell typing) plus notes on when to use them. Selection on unseen validation tasks keeps the changes that generalize. Qwen3.8-27B reached 21.3% on OSWorld V2, 3.8x the same model with fixed interfaces and above GPT-5.5 (13.0%) and Opus 4.8 (20.6%) at a few percent of their cost; ScienceBoard rose from 41.4% to 58.6%.
```

Recent changes: insert between the 2026-10-26 and 2026-10-19 entries:

```md
- [2026-10-20] Added OO-Harness (specialized harness subclasses plus a router; AutomationBench 61.6%→77.4% on the same Gemini 3.5 Flash) and Agent S4 (label-free evolved computer-use interfaces; open 27B model 21.3% on OSWorld V2, 3.8x fixed interfaces); HarnessDev status line now reads as mixed evidence.
```

Sources: append:

```md
- [Object-Oriented Harness — Google Cloud AI Research (arXiv)](../sources/papers/oo-harness-2026-10.md)
- [Evolving Agent Interfaces (Agent S4) — Simular (arXiv)](../sources/papers/agent-s4-evolving-interfaces-2026-10.md)
```

### wiki/index.md (updated)

Replace the automated-harness-optimization line:

```md
- [concepts/automated-harness-optimization](concepts/automated-harness-optimization.md) — systems that improve an agent's harness automatically: Better-Harness and Claude Code's /claude-api hillclimb, label-free Harness², OO-Harness specialized subclasses and Agent S4 evolved interfaces, self-improving skills, self-modifying harnesses, guarded evolution *(as_of: 2026-10-26)*
```

### wiki/sources/papers/oo-harness-2026-10.md (new)

```md
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
- [Automated harness optimization](../../concepts/automated-harness-optimization.md) — new "Specialized harnesses and evolved interfaces" section; HarnessDev status bullet reframed

## Key claims extracted
- Harness evolved as a class hierarchy of specialized subclasses with design lessons and a test-time router
- AutomationBench 61.6%→77.4%, Workspace-Bench 25.5%→39.5% with the same Gemini 3.5 Flash; up to ~15 points absolute over base
- Outperforms Meta-Harness and other global/specialized optimizers on all three benchmarks
- Best-of-K and self-refinement do not reliably close the gap
- Inheritance adds 4.96 points on Workspace-Bench over flattened classes
```

### wiki/sources/papers/agent-s4-evolving-interfaces-2026-10.md (new)

```md
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
- [Automated harness optimization](../../concepts/automated-harness-optimization.md) — Agent S4 bullet in "Specialized harnesses and evolved interfaces"

## Key claims extracted
- Meta-agent builds and revises interfaces and usage knowledge from trajectories without success labels
- Population-based selection on unseen validation tasks
- Qwen3.8-27B: 21.3% on OSWorld V2, 3.8x fixed interfaces, above GPT-5.5 (13.0%) and Opus 4.8 (20.6%) at ~4.3% and ~1.5% of their cost
- ScienceBoard 41.4% → 58.6% with the same model
- Open-source code
```

## Schema / vocabulary additions

None.

## Open questions

- Automated harness optimization would sit at about 123% of its concept ceiling. Split it now? One natural cut moves the offline research sections (Recursive harnessing without ground truth, Specialized harnesses and evolved interfaces, Harness continual learning, Self-evolved vs human-engineered) to a new `concepts/harness-evolution-research.md`. The origin page would keep the practitioner loops (Better-Harness, `/claude-api hillclimb`, self-improving skills, self-modifying harnesses). Assumed no split in this proposal; it can be done as a direct refactor.
	- Yes, split
