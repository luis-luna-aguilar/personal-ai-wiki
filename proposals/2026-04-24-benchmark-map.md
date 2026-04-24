---
type: proposal
source: raw/deep-research/2026-04-23 Agents Evals.md
status: pending
created: 2026-04-24
---

# Proposal: Agent benchmark map (six new benchmark pages + two updates)

## Summary

The report identifies eight benchmark families relevant to agent evaluation. The wiki already has `swe-bench.md` and `swe-polybench.md`; six more need new pages. All eight are real benchmarks from real papers or benchmark sites. The specific scores reported (OSWorld ~12%, WebArena ~57%, Terminal-Bench <65%) are from the research report and should be verified against current leaderboards — they may be outdated.

The research report also provides a critical warning that belongs on the swe-bench page: SWE-bench Verified was largely deprecated by OpenAI due to data contamination, and the successor is SWE-bench Pro.

## Intended changes

- [x] **Update** `wiki/benchmarks/swe-bench.md` — add data contamination note and SWE-bench Pro framing; update as_of
    > See diff below

- [x] **Update** `wiki/benchmarks/swe-polybench.md` — add methodology detail (2,110 instances, Java/JS/TS/Python, CST metrics); update as_of
    > See diff below

- [x] **Create** `wiki/benchmarks/osworld.md` — computer-use benchmark
    > See draft below

- [x] **Create** `wiki/benchmarks/webarena.md` — web navigation benchmark
    > See draft below

- [x] **Create** `wiki/benchmarks/tau-bench.md` — policy adherence and conversational reliability benchmark
    > See draft below

- [x] **Create** `wiki/benchmarks/gaia.md` — generalized AI agent fundamentals benchmark
    > See draft below

- [x] **Create** `wiki/benchmarks/toolbench.md` — enterprise tool-use and API chaining benchmark
    > See draft below

- [x] **Create** `wiki/benchmarks/terminal-bench.md` — CLI and system administration benchmark
    > See draft below

- [x] **Update** `wiki/index.md` — add six new benchmark entries
    > **Add under Benchmarks:**
    > ```
    > - [[benchmarks/osworld]] — computer-use benchmark across Ubuntu/Windows/macOS; exposes GUI grounding gap *(as_of: 2026-04-23)*
    > - [[benchmarks/webarena]] — stateful web navigation benchmark across real web environments *(as_of: 2026-04-23)*
    > - [[benchmarks/tau-bench]] — policy adherence benchmark; introduces pass^k multi-trial reliability metric *(as_of: 2026-04-23)*
    > - [[benchmarks/gaia]] — generalized AI agent fundamentals: multimodal reasoning, web browsing, tool use *(as_of: 2026-04-23)*
    > - [[benchmarks/toolbench]] — enterprise API-chaining benchmark across 16,000+ real RESTful APIs *(as_of: 2026-04-23)*
    > - [[benchmarks/terminal-bench]] — CLI and system-administration benchmark in isolated container environments *(as_of: 2026-04-23)*
    > ```

## Diffs

### wiki/benchmarks/swe-bench.md — data contamination and SWE-bench Pro

Add the following section after `## Variants` (before `## Current leaderboard`):

````md
## Data contamination and SWE-bench Pro

SWE-bench Verified has faced a significant credibility problem: OpenAI explicitly deprecated their internal use of it due to severe data contamination. Models absorbed the evaluation repository code into their pre-training data, meaning high scores reflected memorization rather than autonomous problem-solving ability.

The successor addressing this is **SWE-bench Pro**, which evaluates against private, proprietary codebases and strictly copyleft-licensed repositories (software whose license requires derivative works to also be open, preventing proprietary LLM labs from quietly absorbing the data into closed pre-training sets). SWE-bench Pro scores should be treated as the more meaningful measure of real engineering capability going forward.

**Practical implication:** When comparing agents on SWE-bench Verified, treat scores with skepticism — especially for models with large and recent pre-training corpora. SWE-bench Pro and SWE-bench Multilingual scores are better proxies for generalizable capability.
````

Update frontmatter: `as_of: 2026-04-23`, add `agents-evals-deep-research` to sources.

### wiki/benchmarks/swe-polybench.md — methodology detail

Replace the sparse `## Current status` section with:

````md
## Current status (as of 2026-04-23)

- 2,110 real-world repository instances across Java, JavaScript, TypeScript, and Python
- Evaluates using two methods: traditional execution-based tests AND novel Concrete Syntax Tree (CST) node-retrieval metrics — the CST metrics expose limitations in how well models navigate non-Python AST structures
- Directly addresses SWE-bench's Python-only limitation; designed to expose multi-language capability gaps in frontier models
- Published by Amazon Science
````

Update frontmatter: `as_of: 2026-04-23`, add `agents-evals-deep-research` to sources.

## Page drafts

### wiki/benchmarks/osworld.md (new)

````md
---
title: OSWorld
type: benchmark
domains: [agents, computer-use]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# OSWorld

OSWorld is a benchmark for evaluating multimodal agents capable of raw computer use — interacting with real operating system environments using mouse and keyboard actions. It tests agents across Ubuntu, Windows, and macOS in execution-based environments, where the agent must complete real GUI tasks rather than describing how it would.

## Current status (as of 2026-04-23)

- Human baseline task success: ~72.36%
- Top multimodal models: ~12% task success (as reported; verify against current leaderboard)
- The gap — roughly 60 percentage points — reveals the depth of GUI grounding and layout navigation problems in current frontier models
- Evaluates agents as they actually interact with software: clicking buttons, navigating menus, handling dynamic content

## Why it matters

OSWorld is the most important benchmark for teams evaluating autonomous desktop agents, RPA (Robotic Process Automation) systems, and computer-use agents. The large human/model gap makes it a useful discriminator: high OSWorld scores indicate genuine GUI navigation ability rather than pattern matching against API-structured interfaces.

A model or system that performs well on text-based benchmarks but poorly on OSWorld is likely relying on text structure rather than genuine interface understanding.

## Caveats

- Specific scores are from a research synthesis report (April 2026); verify against the OSWorld leaderboard before citing numbers
- Task distribution may favor certain OS environments — verify per-platform breakdown for specific use cases
- GUI environments are updated over time; OSWorld scores may shift as apps change their interfaces

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

### wiki/benchmarks/webarena.md (new)

````md
---
title: WebArena
type: benchmark
domains: [agents]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# WebArena

WebArena is a stateful web navigation benchmark that challenges agents to complete goal-directed tasks across realistic, live-style web environments including e-commerce sites, content management systems, forums, and development platforms. Unlike static QA benchmarks, WebArena maintains state across interactions — an agent's actions in one step affect what it sees in the next.

## Current status (as of 2026-04-23)

- Human baseline: ~78% task success
- Best reported systems: ~57% (as reported; verify against current leaderboard)
- Tests agents against real web noise: popups, dynamic content, navigation menus, and multi-page flows
- Tasks require combining web navigation, information retrieval, and form submission across multiple sites

## Why it matters

WebArena is the primary benchmark for evaluating agents that must operate in open web environments — browser automation, web research agents, and e-commerce assistants. The 20+ percentage point gap between best models and humans reveals how much current agents struggle with real web environments as opposed to clean API-structured tasks.

Unlike OSWorld, WebArena focuses on web-native tasks rather than full desktop control, making it more directly relevant for web-facing product agents.

## Caveats

- Specific scores are from a research synthesis report (April 2026); verify against the WebArena leaderboard
- Web environments change over time; the benchmark requires maintenance to stay aligned with current site layouts
- Performance varies significantly based on how much scaffolding (tool suite, memory) is given to the agent

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

### wiki/benchmarks/tau-bench.md (new)

````md
---
title: tau-bench
type: benchmark
domains: [agents]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# tau-bench

tau-bench (Tool-Agent-User Interaction benchmark) evaluates agents on their ability to navigate multi-turn dialogues with simulated users while adhering to strict corporate policies — handling real-world tasks like airline refunds and retail returns. Its core contribution is the **pass^k metric**, which measures reliability across multiple consecutive trials rather than single-attempt success.

## What tau-bench tests

Agents are evaluated on tasks with simulated users who:
- Have specific goals but may withhold information until asked
- Interact in natural language across multiple turns
- Trigger policy edge cases (unusual refund requests, out-of-scope asks)

Agents must query databases, follow policy rules (which refunds are authorized, under what conditions), and handle the ambiguity of real human communication — not a clean single-turn input.

## The pass^k metric

tau-bench introduced **pass^k**: the probability that an agent succeeds on ALL k consecutive independent trials.

This is distinct from **pass@k** (did at least one of k attempts succeed?), which is appropriate when you can retry. In live customer service, there is no retry — the agent gets one interaction per customer.

**The results expose a severe reliability problem:** an agent with 60% single-attempt success ($pass^1$) can drop below 25% reliability when measured across eight consecutive runs ($pass^8$). Eval suites that only test single-shot success will massively overestimate production readiness for customer-facing workflow agents.

## Why it matters

tau-bench is the premier benchmark for:
- Customer service and support agents
- Any workflow agent operating under policy constraints
- Evaluating whether an agent is consistent across repeated usage, not just capable in demos

It is also relevant for the coding agent domain when measuring reliability of long-running autonomous processes, not just single-task capability.

## Caveats

- The benchmark is designed around specific policy domains (airline, retail); generalization to other policy types requires separate evaluation
- LLM-driven user simulators have their own failure modes — they may not fully represent the variance of real human users

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

### wiki/benchmarks/gaia.md (new)

````md
---
title: GAIA
type: benchmark
domains: [agents, models]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# GAIA

GAIA (General AI Assistants benchmark) tests fundamental multimodal reasoning, web browsing, and tool-use capabilities through 466 questions designed to require genuine reasoning chains rather than pattern matching. The questions are conceptually simple for humans but expose deep capability gaps in current frontier models.

## Current status (as of 2026-04-23)

- Human baseline: ~92%
- Frontier LLMs without agentic scaffolding: ~15% (as reported; verify against current leaderboard)
- 466 total questions, designed to be un-gameable through data contamination
- Requires combining multimodal reasoning, web access, and tool use in a single task

## Why it matters

GAIA provides a hard, relatively contamination-resistant upper bound for measuring general agent capability. The ~77-percentage-point gap between humans and frontier models quantifies how far current systems are from the "a smart human with internet access" baseline.

It is useful for:
- Selecting foundation models: filtering by GAIA score screens out models that lack genuine tool-use and reasoning integration
- Long-term capability tracking: as agents improve, GAIA provides a stable hard target
- Identifying genuine capability vs. benchmark gaming

## Caveats

- Low baseline scores mean GAIA is a discriminator at the top end; it does not differentiate between most current models
- Scores can vary significantly depending on how much scaffolding (tools, web access, retry) is provided

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

### wiki/benchmarks/toolbench.md (new)

````md
---
title: ToolBench
type: benchmark
domains: [agents]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# ToolBench

ToolBench is a large-scale benchmark for evaluating agents on real-world tool use and API chaining. It covers over 16,000 real RESTful APIs sourced from the RapidAPI hub and tests agents on single-step, multi-step, and multi-tool planning scenarios.

## Current status (as of 2026-04-23)

- 16,000+ real RESTful APIs from RapidAPI
- Three task types: single-tool single-step, single-tool multi-step, and multi-tool multi-step
- Uses a Depth-First Search-based Decision Tree (DFSDT) algorithm for evaluation — agents must navigate a decision tree of possible API calls to find the correct sequence
- Reference benchmark for enterprise API competence

## Why it matters

ToolBench is directly relevant for evaluating agents that must interact with enterprise software stacks through API calls — the core capability behind most business process automation, integration agents, and internal workflow agents. The 16,000-API scale covers a breadth of real-world API diversity that synthetic benchmarks cannot replicate.

## Caveats

- APIs evolve over time; benchmark coverage may lag behind current API landscapes
- DFSDT evaluation methodology makes direct comparison with non-DFSDT-based agents complex

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

### wiki/benchmarks/terminal-bench.md (new)

````md
---
title: Terminal-Bench
type: benchmark
domains: [agents, coding]
tags: [agentic, cli]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# Terminal-Bench

Terminal-Bench evaluates agents on real-world multi-step tasks in isolated container environments, focusing on CLI-based system administration, compilation workflows, and debugging. It tests capabilities that are invisible in text-only benchmarks: navigating a real terminal, managing system state, and debugging through command-line tools.

## Current status (as of 2026-04-23)

- 89 hard, real-world multi-step tasks in isolated container environments
- Frontier models score below 65% (as reported; verify against current leaderboard)
- Tasks cover system administration, compilation, and CLI-based debugging
- Evaluates agents in real shell environments, not simulated inputs

## Why it matters

Terminal-Bench is relevant for evaluating:
- Terminal-first coding agents (Claude Code, Codex, and similar)
- DevOps and system administration agents
- Any agent that must operate through a CLI rather than a GUI or structured API

The below-65% frontier score on tasks that a competent systems engineer would handle routinely reveals a meaningful gap between chat-style capability and real operational autonomy.

## Caveats

- The benchmark is relatively new and has a small task set (89 tasks); statistical noise may affect individual model comparisons
- Specific scores are from a research synthesis report (April 2026); verify against the Terminal-Bench site or paper
- Container environments may differ from real production environments in ways that affect generalization

## Open questions

- Does Terminal-Bench distinguish between task types (compilation vs. admin vs. debugging)? Per-category breakdown would be useful for evaluating specialized agents.

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
````

## Open questions

- Terminal-Bench is the least well-known benchmark in this set. If verification finds the name is different (e.g., "TerminalBench" vs "Terminal-Bench") or the task count differs, update accordingly.
- The scores for OSWorld, WebArena, and Terminal-Bench are from the research report. Mark for verification against current leaderboards before citing.
