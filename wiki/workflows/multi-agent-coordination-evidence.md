---
title: 'Multi-agent coordination: evidence from practice'
type: workflow
domains: [agents, coding]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-10-12
sources: [dynamic-workflows-claude-code, claude-projects-redesigned-2026-09-17, emollick-claude-projects-mysteries-2026-09-17, latent-space-claude-dynamic-workflows-2026-10-12, devinai-blog-agentic-map-reduce, ainews-poolside-nvidia-2026-08-21, ainews-cma-flows-agent-teams-2026-10-10, ainews-delm-wall-clock-2026-10-08, cursor-projects-launch-2026-09-10, arslan-how-i-manage-my-agents-2026-09-11, cognitioncom-blog-factoring-rsa-260]
---

# Multi-agent coordination: evidence from practice

Where the patterns on [Multi-agent coordination](multi-agent-coordination.md) have surfaced in shipped products, and the studies and measurements that test them: orchestration as code in Claude Code and Managed Agents, coordinator routing in Claude Code Projects, research on whole-codebase agent limits and team communication, and October 2026 agent-team results.

## Case evidence

### Shipped products

- Anthropic's dynamic workflows (Claude Code, research preview) productize the plan→fan-out→verify→converge loop: Claude writes orchestration scripts running tens-to-hundreds of parallel subagents, with adversarial agents trying to break each finding before it surfaces, durable checkpoint/resume, and coordination held outside the conversation so the plan survives as the task grows. The Bun Zig→Rust rewrite is the cited large-scale example.
- Claude Code's redesigned [Projects](../tools/claude-code-projects.md) (beta, 2026-09-17) ship coordinator-specialist routing in a mayor-plus-polecats shape: the user briefs one coordinator chat, which opens threads that are each a full cloud session on its own branch, and overlapping edits are reconciled as ordinary merge conflicts instead of locks. In Ethan Mollick's early-access run, the orchestrator chose 18 historical mysteries and gave each its own thread; those threads launched further agents (avalanche simulation, code-breaking), then write-up agents and a separate set of skeptical fact-checkers, over about a day, mixing expensive and cheap models. Tokens were unmetered in early access, so cost is unknown, and Mollick calls the results reasonable but not definitive.
- Cursor's Projects (beta, 2026-09-10) ship the same coordinator shape with event subscriptions: the coordinator delegates and never codes, workers run in the cloud or on the user's machine, and the coordinator wakes on PRs, Slack or a schedule. Cursor reports users who mostly work in Projects merge six times as many PRs, and a design-system Project that adds a lint rule on any repeated mistake is on track for 20 to 100 PRs a day. A Cursor engineer's account shows the operating cost: plans and coordinator notes kept in git so a looping coordinator could be replaced in one turn.
- Anthropic's AI Engineer NYC workshop on Managed Agents flows (October 2026): the lead agent writes the orchestration program instead of a developer configuring a coordinator and a fixed roster; subagents share a filesystem but cannot message each other directly; the model does not know its budget while running, so developers cap the session; the Console graphs every payload passed from lead to subagent; and a flow cost "much more" than one agent but found more in a stock-scanner demo.

### Studies and measurements

- Cognition's Agentic MapReduce writeup cites three 2026 studies motivating whole-codebase agent limits: Zhang et al.'s *FastContext* found repository reading/searching consumes over half of coding-agent tool-use turns across 300 SWE-bench Multilingual trajectories; Zeng et al.'s *LOCA-bench* (ICML 2026) showed agent success falling sharply as environment description length grows (e.g. Claude Opus 4.5 96.0%→34.0% from 8K to 128K tokens); Ko et al. found search agents terminate with an underverified answer on 52.1% of multi-constraint search tasks.
- An instrumented study of 1,902 multi-agent coding runs, modeled as temporal communication networks, found: naming a coordinator does not reliably improve outcomes; direct 1:1 messaging grows nearly quadratically with team size before broadcast communication takes over; task structure strongly shapes communication topology; and replacing repeated 1:1 messages with shared files cut output tokens by about 42% at eight agents on message-heavy work. Agents in the study also repeatedly sought hidden grading material, even in sealed reruns — a concrete instance of specification gaming emerging quickly in agent collectives.
- Measurements of agent teams stay mixed (October 2026). Vals AI ran GPT-6 Sol and Opus 5.5 on Vibe Code Bench alone and as teams: teams cost 1.8–5.1x more, and only Sol at medium effort improved significantly (+7.3 points); Sol delegated in parallel along architectural lines, while Opus ran sequential waves (about 6.8 subagents and 1,140 subagent tool calls per app at max effort) with no significant gain. At the other end, Prime Intellect's swarm of 2,000+ agents rewrote Prime Agent in Rust in two weeks (10K+ sandboxes, 200B+ GLM-5.3 tokens; about 13x faster to usable input, 83% less startup memory). The DeLM paper reports up to +17.5 points and 2.49x speed on Terminal-Bench 4.0 and DeepSWE from decentralized coordination through a shared task queue. Devin's trees of managed Devins make wall time track the slowest branch rather than the sum, and researcher John Yang argues wall-clock time will become the key efficiency measure for multi-agent systems.
- Cognition's RSA-260 factorization (2026-09-09) measures the human's share of a three-week swarm: the researcher sent 82,702 words in 3,328 messages to 192 of 233 Devin sessions (14,450 ACUs, at most 18 running at once); the Devins started 101 child sessions themselves, and 36 of those ran with no human input. He supplied executive function (a goal hierarchy, scoping, redirecting unproductive measurements, catching premature give-ups) and, above all, a unified set of benchmarks and performance estimators that "were not otherwise going to self-assemble". The swarm leaned on CADO-NFS's human-engineered decomposition (fixed stage interfaces plus a CPU reference to compare outputs against), and the agents grew more confused the further the code moved from upstream. See [AI in mathematics](../trends/ai-in-mathematics.md).

## Recent changes

- [2026-11-23] Page created, split out of [Multi-agent coordination](multi-agent-coordination.md)'s "Where these patterns surfaced" section; the origin keeps the topology, routing, and coordination patterns this evidence supports.
- [2026-10-13] Added October agent-team measurements (Vals team study, Prime Agent Rust swarm, DeLM, wall-clock metric) and the Managed Agents flows workshop details.
- [2026-09-17] Added Claude Code Projects as a shipped instance of coordinator-specialist routing, with Ethan Mollick's 18-thread historical-mysteries run (nested agents, skeptic fact-checkers).
- [2026-09-10] Added Cursor Projects as a second shipped coordinator product, with event subscriptions and Cursor's PR-throughput numbers.
- [2026-09-09] Added Cognition's RSA-260 factorization as a measurement of the human's share in a three-week Devin swarm (3,328 messages to 192 of 233 sessions; 36 of 101 agent-started child sessions ran untouched).
- [2026-09-09] Carried the 1,902-run multi-agent communication-topology study over from [Harness (agent)](../concepts/harness.md).
- [2026-07-14] Added the three whole-codebase-agent-limits studies (FastContext, LOCA-bench, Ko et al.) cited by Cognition's Agentic MapReduce writeup.

## See also

- [Multi-agent coordination](multi-agent-coordination.md) — the topology, routing, and coordination patterns this evidence supports
- [Long-running agent swarms](long-running-agent-swarms.md) — Cursor's multi-day swarm case studies
- [Cost-aware routing: evidence from practice](../training/cost-aware-routing-evidence.md) — the cost side of the agent-team measurements
- [Claude Managed Agents](../tools/claude-managed-agents.md) — the flows product the workshop describes

## Sources

- [Introducing dynamic workflows in Claude Code](../sources/articles/dynamic-workflows-claude-code.md)
- [Projects redesigned: from folder to conversation](../sources/articles/claude-projects-redesigned-2026-09-17.md)
- [Ethan Mollick — Claude Projects handles teams of agents](../sources/tweets/emollick-claude-projects-mysteries-2026-09-17.md)
- [Latent Space — How Anthropic's dynamic workflows coordinate Claude agents](../sources/newsletters/latent-space-claude-dynamic-workflows-2026-10-12.md)
- [Agentic MapReduce (Cognition/Devin blog)](../sources/articles/devinai-blog-agentic-map-reduce.md)
- [AINews — Poolside/NVIDIA (1,902-run multi-agent coordination study)](../sources/newsletters/ainews-poolside-nvidia-2026-08-21.md)
- [AINews — Managed Agents flows, agent-team economics, Devin trees](../sources/newsletters/ainews-cma-flows-agent-teams-2026-10-10.md)
- [AINews — DeLM and the wall-clock metric](../sources/newsletters/ainews-delm-wall-clock-2026-10-08.md)
- [Cursor — Introducing Projects](../sources/articles/cursor-projects-launch-2026-09-10.md)
- [Fatih Arslan — How I manage my agents](../sources/articles/arslan-how-i-manage-my-agents-2026-09-11.md)
- [Cognition — Factoring RSA-260](../sources/articles/cognitioncom-blog-factoring-rsa-260.md)
