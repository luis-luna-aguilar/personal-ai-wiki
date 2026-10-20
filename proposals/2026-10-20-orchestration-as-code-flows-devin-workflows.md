---
type: proposal
source: raw/newsletters/2026-10-12-how-anthropics-dynamic-workflows-coordinate-claud.md
sources:
  - raw/newsletters/2026-10-12-how-anthropics-dynamic-workflows-coordinate-claud.md
  - raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
  - raw/newsletters/2026-10-08-ainews-not-much-happened-today.md
  - raw/articles/2026-10-20-docsdevinai-work-with-devin-dynamic-workflows.md
  - raw/tweets/2026-10-13-devindevelopers-2109887510184964285.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Orchestration as code goes cross-vendor (Claude Managed Agents flows, Devin Dynamic Workflows) while agent-team measurements stay mixed

## Summary

### In short
Letting the lead agent write the orchestration program is now a cross-vendor pattern, not a Claude Code feature: in October Anthropic shipped "flows" for Claude Managed Agents (up to 1,000 subagents per run) and Cognition shipped Devin Dynamic Workflows, which record every agent call so an interrupted run resumes without redoing finished work. The payoff is not settled, though: Vals found agent teams cost 1.8–5.1x more and only GPT-6 Sol at medium effort scored significantly better as a team. The proposal updates Multi-agent coordination, Managed Agents, Devin, Cost-aware routing and State of Agents. Reason to hesitate: two of those pages end slightly above their ceilings, inside the warning band.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On Friday 9 October Anthropic put dynamic workflows for Claude Managed Agents, its hosted agent API, into public beta: a lead agent writes a phased plan, fans it out to as many as 1,000 agents in one run and merges the results, and Anthropic warns users to start small because token use can be high. On 12 October, at the AI Engineer conference in New York, Anthropic's CJ Avilla and Harrison Stall explained the design. Claude writes an orchestration program (a "flow") that launches agents, collects their results and manages what each one sees. This replaces the developer-configured coordinator and fixed roster of subagents. In the Q&A they said the model does not know its budget while running, but developers can cap a session; subagents share a filesystem but cannot message each other; the Console graphs every payload the lead passes to a subagent; Anthropic's "dreaming" feature can tidy the memory store so repeated flows get cheaper; and a flow costs "much more" than one agent but found more in their stock-scanner demo.

Cognition shipped the same idea on 13 October, and its docs show what orchestration as code buys. The script is plain Python: each `agent()` call returns output shaped by a JSON schema, which becomes the next stage's prompt; `pipeline()` streams items through stages without waiting for the slowest; `parallel()` waits for all. Every call is recorded under a hash of its prompt and settings, so an interrupted run starts the script again from the top and finished agents replay instantly. That only works if the script never reads the clock, random numbers or the filesystem. The docs also say when not to use it: mechanical codemods, one or two sessions, or tightly coupled work. Separately, Devins can now spawn trees of managed Devins, so wall time tracks the slowest branch.

The evidence on teams is mixed. Vals AI ran GPT-6 Sol and Opus 5.5 on Vibe Code Bench alone and as teams: only Sol at medium effort improved significantly (+7.3 points), while Opus ran sequential waves of about 6.8 subagents with no significant gain. Prime Intellect's swarm of more than 2,000 agents rewrote Prime Agent in Rust in two weeks. The DeLM paper reports gains from a shared task queue, and John Yang argues wall-clock time will become the key efficiency measure.

### What changes
The wiki covers dynamic workflows only as a Claude Code feature, and Managed Agents' page has no orchestration coverage beyond its May Dreams entry.

- **Multi-agent coordination** rewrites the "Scripted subagent orchestration" bullet as a cross-vendor pattern and adds the October measurements (Vals, Prime, DeLM, wall-clock). Page date moves to 13 October.
- **Claude Managed Agents** gains a dynamic-workflows bullet and Recent-changes entry. Page date moves to 12 October.
- **Devin** gains a Dynamic Workflows subsection (10 Recent-changes entries, no spill). Page date stays 19 October.
- **Cost-aware AI task routing** gains the Vals team-cost bullet.
- **State of Agents** refreshes the Managed Agents line; the oldest Recent-changes entry spills to history.
- Four source pages.

### What to weigh
Managed Agents ends near 1,580 body words (105%) and Cost-aware routing near 2,690 (108%), both in the warning band. The Devin announcement tweet only points to the docs, so it gets no source page; it supplies the 13 October date. Claude Code's own page is not touched, since it is at 99% of its ceiling.

## Intended changes

- [ ] **Update** `wiki/workflows/multi-agent-coordination.md` — replace the "Scripted subagent orchestration" bullet; add two bullets at the end of `## Where these patterns surfaced`; `as_of` moves to 2026-10-13; adds one Recent-changes entry dated 2026-10-13 (live list has 6, no spill); append four source ids and links
    > See draft below

- [ ] **Update** `wiki/tools/claude-managed-agents.md` — add one Current-status bullet; Current-status stamp and `as_of` move to 2026-10-12; adds one Recent-changes entry dated 2026-10-12 (live list has 7, no spill); append two source ids and links
    > See draft below

- [ ] **Update** `wiki/tools/devin.md` — add a `### Dynamic Workflows and Devin trees` subsection at the end of `## Current status`; adds one Recent-changes entry dated 2026-10-13 (live list has 9, becomes 10, no spill); append two source ids and links; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add one bullet at the end of `### Cost variance and budgeting tradeoffs`; adds one Recent-changes entry dated 2026-10-10 (live list has 5, no spill); append one source id and link; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — replace the Claude Managed Agents line under `### Agent orchestration`; adds one Recent-changes entry dated 2026-10-12 (live list has 10, so the oldest spills); append source id; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — the oldest Recent-changes entry at apply time (currently `[2026-07-08] Claude Cowork beta expands to web/mobile…`)
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/latent-space-claude-dynamic-workflows-2026-10-12.md` — source page for the AIE NYC workshop writeup

- [ ] **Create** `wiki/sources/newsletters/ainews-cma-flows-agent-teams-2026-10-10.md` — story-specific source page (CMA dynamic workflows, Vals team study, Prime Agent swarm, Devin trees)

- [ ] **Create** `wiki/sources/newsletters/ainews-delm-wall-clock-2026-10-08.md` — story-specific source page (DeLM, wall-clock metric)

- [ ] **Create** `wiki/sources/articles/devin-dynamic-workflows-docs-2026-10.md` — source page for the Devin docs (dated by the announcement tweet)

## Page drafts

### wiki/workflows/multi-agent-coordination.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-13
sources: [googlecloudtech-adk-2-orchestration-patterns, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, every-claude-dynamic-workflows-reliability-2026-06, dynamic-workflows-claude-code, cursor-agent-swarm-economics-2026-09-07, ainews-poolside-nvidia-2026-08-21, mahax-graph-engineering-2026-07-29, latent-space-claude-dynamic-workflows-2026-10-12, ainews-cma-flows-agent-teams-2026-10-10, ainews-delm-wall-clock-2026-10-08, devin-dynamic-workflows-docs-2026-10]
```

`### Coordination mechanics` — replace the "Scripted subagent orchestration" bullet with:

```
- **Scripted subagent orchestration (orchestration as code).** The model writes the orchestration program for a large task, and the program, not the conversation, decides which subagents run, in what order, and with what prompt. This is more reliable than relying on prompt pressure to make the model remember to spawn separate verifiers. By October 2026 three products ship it: Claude Code's dynamic workflows, [Claude Managed Agents](../tools/claude-managed-agents.md)' "flows" (the API version, up to 1,000 agents per run), and [Devin](../tools/devin.md) Dynamic Workflows. Devin's version shows what the code buys. The script is deterministic Python: `agent()` returns output shaped by a JSON schema, which becomes the next stage's prompt; `pipeline()` streams items through stages with no barrier; `parallel()` waits for every result. Each agent call is recorded under a hash of its prompt and settings, so an interrupted run re-executes the script from the top and finished agents replay instantly. That only works if the script never depends on the clock, randomness, or the filesystem; anything that looks at the outside world goes inside an `agent()` call. Use it for wide fan-out with a combine step (roughly five or more independent units) or a staged pipeline such as audit → fix → verify. Stay with one or two sessions for mechanical codemods, tightly coupled work, or small sequential tasks.
```

`## Where these patterns surfaced` — append two bullets:

```
- Anthropic's AI Engineer NYC workshop on Managed Agents flows (October 2026): the lead agent writes the orchestration program instead of a developer configuring a coordinator and a fixed roster; subagents share a filesystem but cannot message each other directly; the model does not know its budget while running, so developers cap the session; the Console graphs every payload passed from lead to subagent; and a flow cost "much more" than one agent but found more in a stock-scanner demo.
- Measurements of agent teams stay mixed (October 2026). Vals AI ran GPT-6 Sol and Opus 5.5 on Vibe Code Bench alone and as teams: teams cost 1.8–5.1x more, and only Sol at medium effort improved significantly (+7.3 points); Sol delegated in parallel along architectural lines, while Opus ran sequential waves (about 6.8 subagents and 1,140 subagent tool calls per app at max effort) with no significant gain. At the other end, Prime Intellect's swarm of 2,000+ agents rewrote Prime Agent in Rust in two weeks (10K+ sandboxes, 200B+ GLM-5.3 tokens; about 13x faster to usable input, 83% less startup memory). The DeLM paper reports up to +17.5 points and 2.49x speed on Terminal-Bench 4.0 and DeepSWE from decentralized coordination through a shared task queue. Devin's trees of managed Devins make wall time track the slowest branch rather than the sum, and researcher John Yang argues wall-clock time will become the key efficiency measure for multi-agent systems.
```

`## Recent changes` — insert one entry directly below the 2026-10-19 entry:

```
- [2026-10-13] Scripted subagent orchestration is now cross-vendor: Claude Managed Agents flows (up to 1,000 agents) and Devin Dynamic Workflows (deterministic Python, record-and-replay resume, explicit when-not-to-use); added October agent-team measurements (Vals team study, Prime Agent Rust swarm, DeLM, wall-clock metric).
```

`## Sources` — append:

```
- [Latent Space — How Anthropic's dynamic workflows coordinate Claude agents](../sources/newsletters/latent-space-claude-dynamic-workflows-2026-10-12.md)
- [AINews — Managed Agents flows, agent-team economics, Devin trees](../sources/newsletters/ainews-cma-flows-agent-teams-2026-10-10.md)
- [AINews — DeLM and the wall-clock metric](../sources/newsletters/ainews-delm-wall-clock-2026-10-08.md)
- [Devin Docs — Dynamic Workflows](../sources/articles/devin-dynamic-workflows-docs-2026-10.md)
```

### wiki/tools/claude-managed-agents.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-12
sources: [managed-agents, every-managed-agents-vibe-check, anthropic-platform-expansion-april-2026, claude-managed-agents-memory, anthropic-spacex-dreams-2026-05-07, claude-managed-agents-feature-parity-2026-05-13, claude-managed-agents-updates-2026-05, anthropic-is-onto-something, ainews-openai-agi-bar-2026-08-28, ainews-cma-flows-agent-teams-2026-10-10, latent-space-claude-dynamic-workflows-2026-10-12]
```

Heading change: `## Current status (as of 2026-08-28)` → `## Current status (as of 2026-10-12)`.

New bullet appended at the end of `## Current status`:

```
- **Dynamic workflows, or "flows" (public beta, October 2026):** the API version of Claude Code's dynamic workflows, enabled with the `multiagent_20261001` beta. A lead agent plans in phases and writes an orchestration program that launches subagents (up to 1,000 per run), collects results, and manages what each sees, replacing the developer-configured coordinator and subagent roster; preconfigured subagents can still be passed in. Subagents share a filesystem but cannot message each other through the API. The model does not know its budget while running, so developers set a session budget, and Anthropic advises starting with scoped tasks because token use can be high. The Console graphs every lead-to-subagent payload. Anthropic suggests the Dreams feature (which rewrites a memory store from past transcripts, merging duplicates and replacing stale entries) to make repeated flows cheaper. See [Multi-agent coordination](../workflows/multi-agent-coordination.md).
```

`## Recent changes` — insert one entry at the top:

```
- [2026-10-12] Dynamic workflows ("flows") in public beta: the lead agent writes its own multi-agent orchestration, up to 1,000 agents per run; session budgets, shared filesystem, Console payload graph.
```

`## Sources` — append:

```
- [AINews — Managed Agents flows, agent-team economics, Devin trees](../sources/newsletters/ainews-cma-flows-agent-teams-2026-10-10.md)
- [Latent Space — How Anthropic's dynamic workflows coordinate Claude agents](../sources/newsletters/latent-space-claude-dynamic-workflows-2026-10-12.md)
```

### wiki/tools/devin.md (updated)

Frontmatter `sources:` (append two ids; `as_of` unchanged):

```
sources: [devin-auto-triage-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, cognitioncom-blog-ai-productivity, the-code-spacexai-drops-grok-45-2026-07-09, ainews-devin-fusion-router-moat-2026-07-14, cognition-devin-outposts-2026-07-21, devinai-blog-introducing-devin-oncall, ainews-cma-flows-agent-teams-2026-10-10, devin-dynamic-workflows-docs-2026-10]
```

New subsection at the end of `## Current status`, after `### Devin Outposts`:

```
### Dynamic Workflows and Devin trees

- **Devin trees (October 2026):** a Devin can spawn managed Devins that spawn their own, so wall time tracks the slowest branch rather than the sum of all of them.
- **Dynamic Workflows (October 2026):** Devin writes and runs a deterministic Python script that orchestrates a team of Devins, each step a separate session on its own VM (or pinned to the parent's machine, or to the cheaper Devin Lite mode). Stages pass schema-shaped results forward and hand off code through git branches. Every agent call is recorded, so the workflow panel shows live progress and an interrupted run resumes where it stopped, within a seven-day maximum. Runs are auto-approved by default; enterprise admins must switch the feature on. A working workflow can be saved to the repo as a skill (`workflow.py` plus `SKILL.md`) for Devin to rerun. Cognition warns that one run can use far more ACUs than a single session and recommends trying a slice first. See [Multi-agent coordination](../workflows/multi-agent-coordination.md).
```

`## Recent changes` — insert one entry directly below the 2026-10-19 entry (list becomes 10, at the cap, no spill):

```
- [2026-10-13] Devin Dynamic Workflows: deterministic Python orchestration of Devin sessions with record-and-replay resume; Devins can also spawn trees of managed Devins.
```

`## Sources` — append:

```
- [AINews — Managed Agents flows, agent-team economics, Devin trees](../sources/newsletters/ainews-cma-flows-agent-teams-2026-10-10.md)
- [Devin Docs — Dynamic Workflows](../sources/articles/devin-dynamic-workflows-docs-2026-10.md)
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter `sources:` — append `ainews-cma-flows-agent-teams-2026-10-10` to the end of the live list (`as_of` unchanged).

`### Cost variance and budgeting tradeoffs` — append after the Uber bullet:

```
- **Agent teams cost more than they usually return.** Vals AI ran GPT-6 Sol and Opus 5.5 on Vibe Code Bench alone and as multi-agent teams: teams cost 1.8–5.1x more, and only Sol at medium effort improved significantly (+7.3 points). Opus ran sequential waves of subagents for no significant gain. Treat a team configuration as something to measure against a single agent on your own task, not a default upgrade; vendors give the same advice (Anthropic and Cognition both say to try multi-agent workflows on a scoped slice first). See [Multi-agent coordination](../workflows/multi-agent-coordination.md).
```

`## Recent changes` — insert one entry below the 2026-10-19 entries:

```
- [2026-10-10] Added Vals AI's agent-team study: teams cost 1.8–5.1x more on Vibe Code Bench, with a significant gain only for GPT-6 Sol at medium effort.
```

`## Sources` — append:

```
- [AINews — Managed Agents flows, agent-team economics, Devin trees](../sources/newsletters/ainews-cma-flows-agent-teams-2026-10-10.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter `sources:` — append `latent-space-claude-dynamic-workflows-2026-10-12` to the end of the live list (`as_of` unchanged).

`### Agent orchestration` — replace the Claude Managed Agents line:

> **Before:** `- [Claude Managed Agents](../tools/claude-managed-agents.md) — Anthropic's hosted runtime; separates session, harness, sandbox, and file-backed built-in memory with shared stores and auditability; added self-hosted sandboxes (public beta, including Cloudflare/Daytona/Modal/Vercel) and MCP tunnels (research preview) *(as of 2026-05-20)*`

```
- [Claude Managed Agents](../tools/claude-managed-agents.md) — Anthropic's hosted runtime; separates session, harness, sandbox, and file-backed memory; self-hosted sandboxes and MCP tunnels; dynamic workflows ("flows", public beta) let a lead agent write its own orchestration across up to 1,000 subagents *(as of 2026-10-12)*
```

`## Recent changes` — insert one entry between the 2026-10-14 and 2026-10-09 entries (list goes to 11, so the oldest spills):

```
- [2026-10-12] Claude Managed Agents dynamic workflows ("flows") enter public beta: the lead agent writes its own orchestration program, up to 1,000 subagents per run; Devin shipped the same pattern as Dynamic Workflows a day later.
```

Remove from `## Recent changes` (spilled, see below):

```
- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

### wiki/history/state-of/agents.md (updated)

Append under the `## Archived from current page on <apply date>` block (open a new block if none exists for the apply date):

```
- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

### wiki/sources/newsletters/latent-space-claude-dynamic-workflows-2026-10-12.md (new)

```
---
title: Latent Space — How Anthropic's dynamic workflows coordinate Claude agents
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-12-how-anthropics-dynamic-workflows-coordinate-claud.md
url: https://www.latent.space/p/claude-dynamic-workflows
published: 2026-10-12
ingested: 2026-10-20
domains: [agents]
---

# Latent Space — How Anthropic's dynamic workflows coordinate Claude agents

Latent Space writeup of an AI Engineer NYC workshop (12 October 2026) where Anthropic's CJ Avilla and Harrison Stall explained dynamic workflows ("flows") for Claude Managed Agents, announced the previous Friday. Flows began in Claude Code as "a harness for every task"; in Managed Agents the lead agent plans and writes an orchestration program, replacing the developer-configured coordinator and roster. A stock-watchlist demo showed a scan phase across isolated-context agents and a review phase. Most of the writeup is the audience Q&A on budgets, self-improvement, visibility, and cost.

## Influenced pages

- [Claude Managed Agents](../../tools/claude-managed-agents.md) — dynamic workflows bullet
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — orchestration-as-code pattern and workshop details
- [State of Agents](../../state-of/agents.md) — Managed Agents leader line

## Key claims extracted

- Flows: "a new type of multiagent orchestration, built for your most ambitious workloads"; Claude chooses the organization of agents and can orchestrate its own topology
- The lead agent creates a plan, then writes an orchestration program that launches agents, collects results, and manages information flow; preconfigured subagents can still be passed in the agent config
- How many agents a task gets is governed by "evals and lower defaults"; ambitious tasks need explicit encouragement to parallelize
- The model does not know its budget while running; developers can set a session budget
- Dreaming (research preview) reads a memory store plus past transcripts and produces a reorganized store; suggested for making repeated flows cheaper
- Self-improving flows are not built in; hill-climbing and dreaming were suggested
- The Console graphs every lead-to-subagent payload
- Subagents share a filesystem; developers cannot make one subagent message another through the API
- Flows cost "much more" than a single agent but were "much more effective at finding all of the details" in the demo
```

### wiki/sources/newsletters/ainews-cma-flows-agent-teams-2026-10-10.md (new)

```
---
title: AINews — Managed Agents flows, agent-team economics, Devin trees
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
published: 2026-10-10
ingested: 2026-10-20
domains: [agents]
---

# AINews — Managed Agents flows, agent-team economics, Devin trees

The "Multi-Agent Orchestration and Coding Tools" section of the 10 October 2026 AINews issue: Claude Managed Agents dynamic workflows enter public beta, Vals AI measures whether agent teams pay off, Prime Intellect's agent swarm rewrites Prime Agent in Rust, and Devins can spawn trees of managed Devins.

## Influenced pages

- [Claude Managed Agents](../../tools/claude-managed-agents.md) — public beta, 1,000-agent limit, beta header, cost warning
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — agent-team measurements
- [Devin](../../tools/devin.md) — Devin trees
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — Vals team-cost bullet

## Key claims extracted

- Claude Managed Agents dynamic workflows (public beta): lead agent writes a phased plan, fans out to up to 1,000 agents per run, merges results; enabled with `multiagent_20261001`
- Anthropic advises starting with scoped tasks because token use can be high
- Vals AI, Vibe Code Bench, GPT-6 Sol and Opus 5.5 alone vs. as teams: teams cost 1.8–5.1x more; only Sol at medium effort improved significantly (+7.3 points)
- Sol delegated in parallel along architectural lines; Opus ran sequential waves, about 6.8 subagents and ~1,140 subagent tool calls per app at max effort, no significant gain
- Prime Intellect: 2,000+ agents, 10K+ sandboxes, 200B+ GLM-5.3 tokens over two weeks rewrote Prime Agent in Rust; ~13x faster to usable input, 83% less startup memory
- Devins can spawn trees of managed Devins, so wall time tracks the slowest branch rather than the sum
```

### wiki/sources/newsletters/ainews-delm-wall-clock-2026-10-08.md (new)

```
---
title: AINews — DeLM and the wall-clock metric
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-08-ainews-not-much-happened-today.md
published: 2026-10-08
ingested: 2026-10-20
domains: [agents]
---

# AINews — DeLM and the wall-clock metric

Two research items from the 8 October 2026 AINews issue on multi-agent efficiency: the DeLM paper on decentralized coordination through a shared queue, and an argument that wall-clock time will become the key efficiency measure for multi-agent systems.

## Influenced pages

- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — agent-team measurements

## Key claims extracted

- DeLM: decentralized multi-agent coordination via a shared queue gives up to +17.5pp accuracy and 2.49x speed on Terminal-Bench 4.0 and DeepSWE
- John Yang (@jyangballin) argues wall-clock time will become the key efficiency axis for multi-agent systems
```

### wiki/sources/articles/devin-dynamic-workflows-docs-2026-10.md (new)

```
---
title: Devin Docs — Dynamic Workflows
type: source
source_type: article
source_file: raw/articles/2026-10-20-docsdevinai-work-with-devin-dynamic-workflows.md
url: https://docs.devin.ai/work-with-devin/dynamic-workflows
published: 2026-10-13
ingested: 2026-10-20
domains: [agents, coding]
---

# Devin Docs — Dynamic Workflows

Cognition's documentation page for Devin Dynamic Workflows, announced by @devindevelopers on 13 October 2026 (`raw/tweets/2026-10-13-devindevelopers-2109887510184964285.md`, which only links here). A dynamic workflow is a deterministic Python script, written and run by Devin, that orchestrates a team of Devin sessions; every agent call is recorded, so runs are observable and resumable. The page covers when to use a workflow, the authoring primitives, where agents run, the determinism rules that make resume work, cost, and saving a workflow as a skill.

## Influenced pages

- [Devin](../../tools/devin.md) — Dynamic Workflows subsection
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — orchestration-as-code pattern

## Key claims extracted

- Use a workflow for wide fan-out with a combine step (roughly 5+ independent units) or a staged pipeline (e.g. audit → fix → verify); not for mechanical codemods, one or two sessions, or tightly coupled or small sequential work
- Primitives: `register_workflow`, `agent(prompt, phase, schema)` returning a schema-shaped dict, `pipeline(items, stages…)` with no barrier between stages, `parallel([...])`, `log()`
- Each agent is by default a separate Devin session on its own VM, handing code off through git branches; can be pinned to the parent's VM (shared working tree, lower concurrency) or to a cheaper mode such as Devin Lite
- On resume the script re-executes from the top; each agent call is keyed by a hash of prompt, schema, and settings, so completed calls replay and only unfinished work runs; scripts must not depend on time, randomness, generated IDs, environment variables, filesystem state, or network responses
- Editing a prompt re-runs that agent and everything downstream; maximum run budget is seven days; failed agents are handled by the script (skip, default, retry, fail)
- Runs are auto-approved by default; enterprise admins must enable the feature
- One run can use far more ACUs than a single session; test on a slice first
- A working workflow can be committed as a skill (`workflow.py` plus `SKILL.md`)
```

## Open questions

- Claude Code's page (at 99% of its ceiling) still describes dynamic workflows as a Claude Code research preview. Should a later trim make room for one line noting the API version, or is the Multi-agent coordination link enough (assumed: enough)?
