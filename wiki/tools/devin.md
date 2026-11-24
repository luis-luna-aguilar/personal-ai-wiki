---
title: Devin
type: tool
domains: [coding, agents, cybersecurity]
subcategory: terminal-coding-agent
tags: [cognition]
as_of: 2026-11-23
sources: [devin-auto-triage-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, cognitioncom-blog-ai-productivity, the-code-spacexai-drops-grok-45-2026-07-09, ainews-devin-fusion-router-moat-2026-07-14, cognition-devin-outposts-2026-07-21, devinai-blog-introducing-devin-oncall, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06, devin-cloud-in-your-terminal-2026-09-21, ainews-cma-flows-agent-teams-2026-10-10, devin-dynamic-workflows-docs-2026-10, devinai-bots, cognitioncom-blog-factoring-rsa-260, cognition-swe-2-2026-09-10, cognition-local-fusion-2026-09-11, cognition-aws-sca-2026-09-15, cognition-code-scans-2026-09-16]
---

# Devin

Cognition's autonomous coding agent, initially positioned as one of the first "fully autonomous software engineer" agents. Now expanding into persistent operational roles: [Devin Oncall](devin-oncall.md) (generally available October 2026) investigates and mitigates production alerts and incidents, succeeding Auto-Triage (May 2026), Cognition's first always-on deployment; [Devin Bots](devin-bots.md) (November 2026) run teams of Devins as persistent AI teammates. Cognition valued at $25B (May 2026).

## Current status (as of 2026-11-23)

### Devin Bots

- **Devin Bots (November 2026):** persistent AI teammates that split a goal across parallel Devin sessions until the PRs are mergeable; see [Devin Bots](devin-bots.md).

### Devin Oncall

- **Devin Oncall (GA, October 2026):** investigates alerts and bug reports, diagnoses production incidents and mitigates them through Responders (successor to Auto-Triage) and Incidents, with a separate review agent; 100% end-to-end on SREGym-Lite. Details on its own page, [Devin Oncall](devin-oncall.md).

### Security Swarm, Code Scans and Agentic MapReduce

- **Security Swarm:** parallel agents fan out across a codebase for vulnerability discovery, validation, patching, and PR generation
- Security Swarm aggregates findings, reproduces each issue in a sandbox, validates exploitability, then writes a patch for review
- **Agentic MapReduce (the architecture behind Security Swarm):** a Plan agent studies the repo and authors deterministic "selectors" (Tree-sitter queries, symbol/type queries, import-graph traversals, lexical patterns); the selectors run over every file with no model in the loop (Shard), producing a bounded, inspectable work queue instead of an open-ended search; one fresh Devin session per batch investigates its shard in parallel (Map); a Reducer session dedupes findings and composes cross-shard attack chains, e.g. an unauthenticated ID leak plus an ID-gated RCE becoming one P0 (Reduce); a final Verify stage reproduces each serious finding in a sandboxed session against a running build and marks it Confirmed, False Positive, or Inconclusive
- Benchmarked against a CVE-pinned ground-truth set (GitHub Advisory Database, each pinned to the commit before its fix, dozens of cases across 12+ languages and vulnerability classes): Security Swarm reports **72% recall**, ahead of other scanners tested in the same eval, at a fraction of their cost
- Cognition claims the system finds more verified vulnerabilities at 30% lower cost than rivals; treat both this and the 72% recall figure as vendor-reported until independently verified, though the CVE-pinned methodology is more rigorous than a bare cost claim
- **Code Scans (2026-09-16, `/scan`):** the same Agentic MapReduce engine pointed at any stated goal, not only security: slow paths and N+1 queries, untested flows, dead code and stale feature flags, WCAG accessibility, or a team's own coding standards. Devin helps scope what counts as a finding, reports, and opens the PRs. On the Dioxus repo it cut debug build time from 58.6s to 21.0s (64%) across 22 crates.

### Fusion, productivity measurement, and models

- **Devin Fusion (Cloud since June; Desktop and CLI since 2026-09-11):** applies the [sidekick multi-model harness pattern](../workflows/multi-agent-coordination.md) — a frontier model and a cheaper model run as two persistent, separately-cached agents, with the frontier model planning and reviewing while the sidekick handles mechanical work. Running on Fable 5, Fusion can beat Opus 4.8 on cost per task not because Fable is cheaper per token, but because stronger delegation and judgment waste fewer actions: per an independent coding-agent index analysis relayed by AINews, in 81% of sampled Fable-led runs the lead model never makes a code edit itself.
- **Fusion numbers (September–October 2026):** with SWE-2 as sidekick, Fusion cut cost 11–46% against the lead model alone across DeepSWE 1.1, Terminal-Bench 4.0, SWE-Atlas QnA, Vals Code Migration and FrontierCode 1.1 Extended, at near-equal scores (measured with Artificial Analysis and Vals AI). On Artificial Analysis's Coding Agent Index (chart updated 2026-10-19), Opus 5.5 led by Fusion with a GPT-6 Luna sidekick scores 68.1 at 31% lower cost than Claude Code on Opus 5.5; Cognition recommends that pairing. Cognition prices "per task, not per token": a sidekick 3.75x pricier per token cut the pair's cost per task 2% and raised the score (see [Cost-aware routing evidence](../training/cost-aware-routing-evidence.md)). Earlier, 88% of Cognition's own merged PRs ran entirely through the automated Fusion router.
- **Session productivity estimator:** an automated system that reviews each completed Devin session, classifies whether it produced useful (typically merged) work, then estimates the equivalent human-engineering hours it saved; calibrated against 258 self-reported sessions from 126 users, reaching `r_log = 0.74` on held-out data, deliberately calibrated to underestimate rather than overestimate; now running in production with customers — Cognition frames this as the first automated system measuring AI engineering productivity in production
- **SWE-2 (2026-09-10):** Cognition's current in-house coding model, post-trained from [Kimi K3](../models/kimi-k3.md) (2.8T) with RL scaled to multiple trillions of parameters; one RL run trains every reasoning-effort level, each with a cost penalty fitted to the base model's cost–performance curve. 50.0% on FrontierCode 1.1 Main (within a point of Fable 5.1 at 64% lower cost), 73.0% DeepSWE 1.1, 92.8% Terminal-Bench 2.1, 27.3% Terminal-Bench 4.0. At medium effort it takes 58% fewer turns and costs 81% less than SWE-1.7 while scoring higher. Available in Devin Desktop, CLI, Web and Fusion; Devin Voice runs on it with GPT-Live.

### Deployment: Outposts, AWS and cross-OS VMs

- **Devin Outposts (July 2026):** Devin's planning/inference loop continues running in Cognition's cloud, but command execution, file edits, and repository access can now run on infrastructure the customer controls — a Mac mini, a lab GPU box, a private-network VM, or a Kubernetes cluster. Launch-partner deployment guides ship with Cloudflare (isolated edge sandbox), Daytona (sub-90ms snapshot-started sandboxes), E2B (fast configurable cloud sandboxes reaching into a private cloud), Modal (same GPU infra used for training/serving, so Devin can reproduce failures on production hardware), and Namespace (M5-powered Mac with Xcode/computer use for Apple-platform apps).
- **AWS single-tenant (2026-09-15):** a multi-year Strategic Collaboration Agreement with AWS. Devin is sold on AWS Marketplace, uses the Agent Toolkit for AWS, and can be deployed single-tenant in a customer-chosen AWS region inside a dedicated VPC; each session runs in its own disposable VM and audit-log APIs feed the customer's monitoring. Cognition cites Mercedes-Benz analysing 200K+ lines of COBOL (an estimated eight-month project done in eight days) and another automaker moving a 25K-line COBOL workflow to Lambda at an estimated 73% lower cost.
- **Cross-OS cloud VMs (September 2026):** Devin runs as a cloud agent on macOS, Windows and Linux, including Mac VMs for end-to-end iOS work from Slack or the web; its VM, networking, VNC and computer-use infrastructure was rebuilt in Rust, with Dioxus Labs joining Cognition to work on it.

### Devin Cloud in the terminal

- **Devin Cloud in the CLI (2026-09-21):** `devin --cloud` or `/cloud` creates, steers, resumes and watches cloud sessions from the terminal; sessions outlive the terminal that started them, and `devin --cloud --resume <url>` reopens one.
- **Two-way `/handoff`:** sends a local Devin CLI task to Devin on its own cloud VM; run in a cloud session, it fetches the session's PR branch, checks it out locally, and starts a local session on it. `/open web|desktop` switches the view to the web app or Devin Desktop.
- **`devin ssh`:** connects to the agent's VM to edit code, run dev servers with port forwarding, and copy files with scp.

### Memory

- **Devin Dreaming (October 2026):** an overnight pass that prunes and links Devin's memory graph. Cognition is open-sourcing the storage format as Agent Memory Repo: a git repo of markdown files with a `MEMORY.md` index and one source-linked fact per line, which several agents can write at once through ordinary git merges (see [Agent memory](../concepts/agent-memory.md)).

### Dynamic Workflows and Devin trees

- **Devin trees (October 2026):** a Devin can spawn managed Devins that spawn their own, so wall time tracks the slowest branch rather than the sum of all of them.
- **Dynamic Workflows (October 2026):** Devin writes and runs a deterministic Python script that orchestrates a team of Devins, each step a separate session on its own VM (or pinned to the parent's machine, or to the cheaper Devin Lite mode). Stages pass schema-shaped results forward and hand off code through git branches. Every agent call is recorded, so the workflow panel shows live progress and an interrupted run resumes where it stopped, within a seven-day maximum. Runs are auto-approved by default; enterprise admins must switch the feature on. A working workflow can be saved to the repo as a skill (`workflow.py` plus `SKILL.md`) for Devin to rerun. Cognition warns that one run can use far more ACUs than a single session and recommends trying a slice first. See [Multi-agent coordination](../workflows/multi-agent-coordination.md).

### Research swarms

- **RSA-260 factorization (2026-09-09):** up to 18 parallel Devin Cloud sessions (233 in all, 14,450 ACUs) rebuilt the CADO-NFS factoring pipeline for GPUs over three weeks and factored RSA-260; Cognition credits sessions that persist, run sandboxed and can work autonomously for weeks. Results on [AI in mathematics](../trends/ai-in-mathematics.md); the human's share on [Multi-agent coordination: evidence](../workflows/multi-agent-coordination-evidence.md).

## Why it matters

Devin's parent/child structure, which [Devin Oncall](devin-oncall.md) applies to production alerts, extends into enterprise security work through Security Swarm, and Cognition has now named and documented the underlying pattern as [Agentic MapReduce](../workflows/multi-agent-coordination.md): deterministic selection guarantees whole-repo coverage, parallel bounded workers keep cost proportional to relevant code rather than repo size, and a reasoning Reduce step connects findings that isolated workers couldn't see on their own. Devin Fusion applies a different multi-model idea — [sidekick harnesses](../workflows/multi-agent-coordination.md), contrasted with the [Advisor strategy](../workflows/advisor-strategy.md) pattern by keeping both models' contexts persistently cached instead of paying a cache-miss cost per escalation. The productivity estimator is a production instance of [dollar/hours-denominated agent evals](../concepts/economic-agent-evals.md).

## Recent changes

- [2026-11-24] Devin Oncall (Responders, Incidents, review agent, context layers, SREGym-Lite and customer results) split out to its own page, [Devin Oncall](devin-oncall.md).
- [2026-11-23] [Devin Bots](devin-bots.md) launched: persistent AI teammates that split a goal across parallel Devin sessions on separate VMs, reachable by text, Slack or phone; own page.
- [2026-10-13] Devin Dynamic Workflows: deterministic Python orchestration of Devin sessions with record-and-replay resume; Devins can also spawn trees of managed Devins.
- [2026-10-06] Devin Dreaming (overnight memory prune-and-link) launched; storage format open-sourced as Agent Memory Repo.
- [2026-09-21] Devin Cloud in the terminal: `devin --cloud`, two-way `/handoff` between the local CLI and a cloud VM, `/open web|desktop`, `--resume`, and `devin ssh` into the agent's VM.
- [2026-09-16] Code Scans (`/scan`): Agentic MapReduce audits toward any goal (performance, dead code, accessibility, team standards); Dioxus debug build 58.6s → 21.0s. Devin also runs cloud VMs on macOS and Windows as well as Linux.
- [2026-09-15] AWS Strategic Collaboration Agreement: Devin on AWS Marketplace and deployable single-tenant in a customer-chosen region inside a dedicated VPC.
- [2026-09-11] Fusion reaches Devin Desktop and CLI; with SWE-2 as sidekick it cuts cost 11–46% across five benchmarks; Cognition argues for pricing per task, not per token.
- [2026-09-10] SWE-2 replaces SWE-1.7 as Cognition's model: post-trained from Kimi K3, 50.0% FrontierCode 1.1 Main within a point of Fable 5.1 at 64% lower cost.
- [2026-09-09] A Devin Cloud swarm (up to 18 concurrent sessions, 233 total) rebuilt CADO-NFS for GPUs and factored RSA-260 and 2^1277−1.

## Sources

- [Devin Auto-Triage launch](../sources/articles/devin-auto-triage-2026-05.md)
- [The Code - Cognition ships Devin for Security](../sources/newsletters/the-code-devin-security-2026-07-02.md)
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [Agentic MapReduce (Cognition/Devin blog)](../sources/articles/devinai-blog-agentic-map-reduce.md)
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
- [Estimating the Productivity of an Autonomous AI Software Engineer](../sources/articles/cognitioncom-blog-ai-productivity.md)
- [The Code - SpaceXAI drops Grok 4.5](../sources/newsletters/the-code-spacexai-drops-grok-45-2026-07-09.md)
- [AINews — Coding-agent cost/perf tradeoffs: Terra Max, Devin Fusion, and Fable-led delegation](../sources/newsletters/ainews-devin-fusion-router-moat-2026-07-14.md)
- [Cognition — Introducing Devin Outposts](../sources/tweets/cognition-devin-outposts-2026-07-21.md)
- [Cognition — Introducing Devin Oncall](../sources/articles/devinai-blog-introducing-devin-oncall.md)
- [Cognition — Agent Memory Repo](../sources/articles/cognition-agent-memory-repo-2026-10.md)
- [AINews — Devin Dreaming and Agent Memory Repo](../sources/newsletters/ainews-devin-dreaming-2026-10-06.md)
- [Cognition — Bringing Devin Cloud to your terminal](../sources/articles/devin-cloud-in-your-terminal-2026-09-21.md)
- [AINews — Managed Agents flows, agent-team economics, Devin trees](../sources/newsletters/ainews-cma-flows-agent-teams-2026-10-10.md)
- [Devin Docs — Dynamic Workflows](../sources/articles/devin-dynamic-workflows-docs-2026-10.md)
- [Cognition — Devin Bots product page](../sources/articles/devinai-bots.md)
- [Cognition — Factoring RSA-260](../sources/articles/cognitioncom-blog-factoring-rsa-260.md)
- [Cognition — Introducing SWE-2](../sources/articles/cognition-swe-2-2026-09-10.md)
- [Cognition — Introducing Fusion in Devin Desktop & CLI](../sources/articles/cognition-local-fusion-2026-09-11.md)
- [Cognition — Cognition and AWS Strategic Collaboration Agreement](../sources/articles/cognition-aws-sca-2026-09-15.md)
- [Cognition — Introducing Code Scans (X thread)](../sources/tweets/cognition-code-scans-2026-09-16.md)
