# Research request: evals for software-development agents and general task agents

Generated: 2026-04-22
Status: draft

## Context for the researcher

This research will feed a personal Obsidian-based AI knowledge wiki. The wiki tracks the current state of AI tools, models, workflows, concepts, trends, benchmarks, and practical training guidance. It is not trying to produce an academic literature review or a vendor leaderboard for its own sake. The end goal is to turn the research into concise, source-backed pages that help a practitioner understand the space, compare options, and teach teams how to operate well with AI systems.

The wiki already has strong coverage of agentic development, coding agents, harness engineering, and organizational AI adoption. It is weaker on evals: the wiki mentions that evals, traces, review gates, and verification are essential for agent autonomy, but it does not yet contain a practical, reusable map of how to do evals in software work or normal business/knowledge-work tasks. This research should close that gap.

## Purpose

The wiki already treats agentic development, harness engineering, agent supervision, and organizational AI adoption as major themes. It repeatedly says evals, traces, review gates, and CI/CD are critical to giving agents more autonomy, but it does not yet contain a practical eval strategy that can be used to train people or teams.

The goal of this research is to build the missing operational layer: how teams should design, run, interpret, and maintain evals for AI agents doing software-development work and for agents doing normal knowledge-work tasks.

## Current wiki baseline

- [[wiki/concepts/harness]] says the evaluation layer is part of the agent harness and frames "harness + evals + harness engineering -> better agent" as the analogue of model training. It lists eval-driven simplification, traces, CI/CD, critique loops, and repo-state awareness, but does not explain how to design eval suites.
- [[wiki/concepts/agent-improvement-loop]] explains a trace-centered loop: collect traces, score/review them, find recurring failures, make targeted harness changes, validate offline, redeploy, and repeat. It distinguishes online and offline evals, but does not give a usable taxonomy or implementation playbook.
- [[wiki/training/ai-enablement-software-development]] says the bottleneck shifts from writing code to safely verifying and deploying it. It mentions CI/CD, tests, rollback, expensive-model review, critique loops, and Shopify's SimGym proxy eval example, but lacks concrete eval patterns for coding agents.
- [[wiki/training/company-wide-ai-enablement]] includes role-first agent design, success criteria, proof-based status rules, promotion only after reliability, and a "trust battery with judge agent." It does not generalize these into a task-agent eval framework.
- [[wiki/training/anti-autopilot-review-friction]] says humans should review gates, specs, acceptance criteria, and verification scripts, not only outputs. It lacks guidance on how to turn those gates into repeatable evals.
- [[wiki/benchmarks/swe-polybench]] is the only benchmark page. It covers the value of broader software-engineering benchmarks, but the wiki has no broader benchmark map for coding agents, computer-use agents, research agents, or workflow agents.

## Known gaps in the wiki

- No dedicated concept page for agent evals, task evals, or eval-driven agent development.
- No training page that teaches teams how to build evals before increasing agent autonomy.
- No taxonomy separating deterministic tests, rubric-based human review, LLM-as-judge, simulation, trace evals, benchmark suites, production monitoring, and regression tests.
- No guidance for software-development evals beyond generic "tests/CI/CD/review are bottlenecks." No typing of evals, classifications, explorations of the different kind of evals we can do on software.
- No guidance for normal business-task agents: research, email, support, sales ops, finance analysis, legal drafting, scheduling, document processing, or workflow automation.
- No autonomy ladder showing what eval evidence is required before moving from "assistant" to "in the loop" to "above the loop" to more autonomous execution.
- No patterns for maintaining eval suites over time: mining production traces, preventing overfitting, building holdout sets, refreshing stale tasks, and deciding when an eval is no longer useful.
- No guidance on evaluator reliability: when LLM judges are acceptable, when humans must label, how to calibrate rubrics, how to measure inter-rater agreement, and how to detect judge drift.
- No implementation recipes for turning specs, acceptance criteria, PR comments, support tickets, SOPs, or role handbooks into eval cases.
- No list of benchmark families worth tracking for agent capability claims, nor a warning about where public benchmarks fail to predict production usefulness.
- No lessons learned and benchmarks from people that had implemented evals across their agentic tasks and software tasks.

## Research objective

Produce a practical, source-backed map of agent eval strategies that can become wiki content for:

- A concept page on agent/task evals.
- A training page on evals for software-development agents.
- A training page or section on evals for general task agents and organizational workflows.
- Additional benchmark pages or benchmark-map updates if the research identifies durable benchmark categories.

The research should focus on what people can actually do: eval patterns, examples, rubrics, metrics, toolchains, failure modes, and decision rules for granting autonomy.

## Research questions

1. What are the main categories of evals used for AI agents today, and how should this wiki define them operationally?
2. How do evals differ for single-turn model outputs, tool-using agents, long-horizon agents, coding agents, computer-use agents, and organizational workflow agents?
3. For software-development agents, what eval patterns work best for issue fixing, feature implementation, refactoring, test generation, code review, security review, dependency updates, migration tasks, and CI failure repair?
4. How should software teams combine existing engineering checks, such as unit tests, integration tests, type checks, linters, static analysis, CI, deployment rollback, code review, and security scans, with AI-specific evals?
5. What are the best current practices for converting specs, acceptance criteria, bug reports, PR review comments, postmortems, and production incidents into eval cases?
6. What should a "minimum viable eval suite" look like for a team adopting Claude Code, Codex, Cursor, or similar coding agents?
7. What should an advanced eval stack look like once agents are running in the background, opening PRs, reviewing code, or operating across multiple repos?
8. How should teams evaluate normal task agents that work on email, calendar, research synthesis, customer support, sales ops, finance analysis, document review, or internal operations?
9. Which metrics matter most by task type: task success, factuality, completeness, policy compliance, latency, cost, tool-call efficiency, escalation quality, user satisfaction, business outcome, or regression rate?
10. How can teams evaluate whether an agent should ask for help, escalate, stop, or continue autonomously?
11. What are reliable patterns for online evals from production traces, and how do they feed offline regression suites?
12. When is LLM-as-judge appropriate, and what safeguards are needed: rubrics, calibration sets, pairwise comparison, reference answers, human audits, adversarial examples, or multiple judges?
13. How should evals handle long-horizon tasks where there is no single canonical answer?
14. What do current public benchmarks measure well, and where do they fail to predict real-world agent usefulness?
15. Which public benchmarks should this wiki track for coding agents, computer-use agents, web agents, research agents, and tool-use agents? Candidate names to verify include SWE-bench-family benchmarks, SWE-PolyBench, Terminal-Bench, OSWorld, WebArena, tau-bench, ToolBench, GAIA, and domain-specific task suites.
16. What patterns exist for using simulation or synthetic users to evaluate agents before exposing them to real customers or workflows?
17. How should teams prevent eval overfitting, benchmark gaming, and false confidence from narrow test suites?
18. How should eval results map to autonomy levels, permissions, tool access, spending limits, and human review requirements?
19. What examples exist of companies successfully improving agents through eval loops, trace mining, judge agents, or production feedback?
20. What should be taught to non-experts so they can design useful evals for their own workflows without becoming ML engineers?

## Source priorities

- Official product and platform docs for agent/eval tooling from OpenAI, Anthropic, Google, LangChain/LangSmith, Braintrust, Humanloop, Promptfoo, inspect-style eval frameworks, and similar systems.
- Engineering blogs and talks from teams deploying coding agents or task agents in production, especially examples with concrete eval suites or failure-driven improvements.
- Academic and benchmark papers for software-engineering agents, web/computer-use agents, tool-use agents, research agents, and long-horizon task agents.
- Practitioner guides on LLM-as-judge reliability, rubric design, pairwise evals, human labeling, and production monitoring.
- Case studies from companies using coding agents at scale, such as Shopify/Ramp-style adoption stories, but only when they provide eval, review, CI, or reliability detail.
- Public repositories that include eval harnesses, task sets, judge prompts, benchmark adapters, or regression-test examples.
- Podcasts or conference talks only when they include specific operational details not present in written docs.

## Tools and vendors to map

Treat tool discovery as a core part of the assignment. Identify which tools are useful for designing, running, scoring, tracing, and monitoring evals for agents.

- General eval and observability platforms for LLMs and agents, such as LangSmith, Braintrust, Humanloop, Promptfoo, OpenAI eval-related tooling, Anthropic tooling, Google tooling, inspect-style frameworks, and comparable products.
- Coding-agent-specific or software-eval-adjacent tools, such as CI-integrated evaluation harnesses, benchmark runners, regression-test tooling, code-review evaluators, judge pipelines, sandboxed task runners, and trace/telemetry systems.
- Workflow-agent and business-task eval tooling, such as simulation frameworks, test harnesses for support/sales/research workflows, rubric/grading systems, human-review operations tools, and monitoring products for long-running agents.
- Any open-source frameworks, repos, or templates that make it easier for teams to stand up evals without building everything from scratch.
- For each tool, capture what it is good for, what type of evals it supports, where it fits in the stack, its likely user, and its limitations.

## What to extract from each useful source

- Publication date or date of record.
- Whether the source is about model evals, agent evals, coding-agent evals, workflow evals, or benchmark design.
- The eval target: output quality, task success, tool use, planning, escalation, safety, latency, cost, autonomy, or business outcome.
- The eval method: deterministic checks, golden examples, unit/integration tests, LLM judge, human review, simulation, production traces, benchmark tasks, adversarial tests, or hybrid methods.
- How eval cases are created: hand-authored, mined from production traces, generated synthetically, adapted from tickets/incidents, or imported from public benchmarks.
- How grading works, including rubrics, reference answers, pass/fail criteria, pairwise comparisons, scorer prompts, human labels, and calibration.
- How teams avoid overfitting, such as holdout sets, hidden tests, trace splits, periodic refreshes, or human review of proposed harness changes.
- How evals connect to operational decisions: deployment, rollback, permission changes, autonomy increases, model choice, prompt/harness changes, or user training.
- Concrete examples, templates, prompts, rubrics, dashboards, or eval cases that can be adapted into training material.
- Which tools, frameworks, or vendors are mentioned or implied, and whether practitioners actually use them in production.
- For each tool worth tracking: category, core use case, strengths, weaknesses, notable integrations, and whether it is better for coding agents, business-task agents, or both.
- Failure modes: benchmark mismatch, judge bias, brittle tests, stale evals, false positives/negatives, gaming, cost explosion, review fatigue, or evals that reward the wrong behavior.

## Desired final wiki outputs

- New concept page candidate: `wiki/concepts/agent-evals.md` or `wiki/concepts/task-evals.md`, covering taxonomy, online/offline loops, judge reliability, trace mining, and autonomy gating.
- New training page candidate: `wiki/training/evals-for-agentic-software-development.md`, focused on software teams using coding agents.
- New training page candidate: `wiki/training/evals-for-agentic-work.md`, focused on normal business/task agents and manager-level supervision.
- New tool pages or updates for eval-specific tools if the research finds products important enough to track directly.
- Update candidate: [[wiki/concepts/harness]] with a tighter link from harness design to eval design.
- Update candidate: [[wiki/concepts/agent-improvement-loop]] with more concrete eval-suite and trace-mining patterns.
- Update candidate: [[wiki/training/ai-enablement-software-development]] with a practical "eval stack" for coding-agent adoption.
- Update candidate: [[wiki/training/company-wide-ai-enablement]] with an autonomy/eval ladder for moving agents from bounded roles to broader responsibilities.
- Update candidate: [[wiki/training/anti-autopilot-review-friction]] with eval-oriented review gates.
- Benchmark candidates: pages for any durable benchmark families that the research confirms are important enough to track separately from [[wiki/benchmarks/swe-polybench]].

## Exclusions

- Do not spend much time on generic LLM leaderboard comparisons unless they directly inform agent or task eval design.
- Do not treat public benchmark scores as sufficient evidence for production readiness.
- Do not focus on RLHF, pretraining, or model-lab internal evaluation unless it transfers directly to user-facing agent evals.
- Do not produce a vendor catalog unless it helps explain practical eval patterns.
- Do not assume software-development evals and normal task-agent evals are the same; compare them explicitly.
