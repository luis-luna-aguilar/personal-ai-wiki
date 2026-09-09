---
type: proposal
source: raw/newsletters/2026-09-04-the-folder-is-the-agent.md
status: pending
created: 2026-09-09
---

# Proposal: "Folder as agent" dispatch layers and RLM-style sub-agent harnesses

## Summary

### The source

Two related harness stories landed this week. Every's Kieran Klaassen (GM of Cora, Every's email product) republished and extended his "folder is the agent" framing: after three months failing to make free-form agent swarms work, he settled on running 44 specialized agents as durable folders — each one a project directory with a CLAUDE.md/AGENT.md, skill definitions, and months of accumulated institutional knowledge, where pointing the same base model (mostly Opus) at a different folder produces a genuinely different specialist. What's new in this piece beyond the pattern itself is the dispatch layer he built to manage it: a Ruby daemon watches a directory for spawn requests, creates a lead agent that breaks a task into subtasks and writes each as a file, then spawns worker agents in the right folders; workers report back by writing files, and the daemon polls status every 60 seconds. He interacts with it through two slash commands — `/hey` for a cross-project status briefing, `/orchestrate` to kick off a task — and watches everything live through tmux panes and an "agent tree" dashboard. He cites Anthropic's own multi-agent research to justify the approach: an Opus lead with Sonnet sub-agents beat a single Opus agent by 90% on research tasks, but multi-agent setups burn 15x more tokens, and most coding tasks parallelize worse than research does. His hard-won rule: "you can't vibe orchestrate" — build a flow, use it yourself, and trust it before handing it to autonomous dispatch. Separately, Harvey and Baseten published a recursive-language-model (RLM) harness built for M&A due diligence: a root agent searches a data room and delegates document review to sub-agents, aggregating findings over corpora up to 80 million tokens. Moving from a standard tool-calling loop to the RLM harness raised mean rubric pass rate on their synthetic diligence benchmark from 23% to 62%; harness-specific post-training on top of that (self-distilled SFT on GLM-5.2, GRPO on Qwen3.5) added another 15 to 33 points depending on the base model. LangChain shipped matching primitives in `deepagents` the same week: subagent forking that passes a supervisor's context down to its subagents, plus managed connections that abstract OAuth/token/consent flows for either agent-owned or user-owned identities.

### What changes

The wiki's **Agentic orchestration patterns** page already has a "Folder-scoped specialization" pattern bullet and a "Where these patterns surfaced" note crediting Every's original April "folder is the agent" framing — this proposal extends that existing bullet with concrete operational detail rather than adding a duplicate entry. **Harness (agent)** already discusses Prime Intellect's separate RLM-native Prime Agent and LangChain DeepAgents' `deepagents.toml` manifest concept.

- **Agentic orchestration patterns**: the existing "Folder-scoped specialization" bullet gains the dispatch-layer mechanics (Ruby daemon, `/hey`/`/orchestrate`, file-based worker reporting), the Anthropic multi-agent research citation (90% better / 15x tokens / coding parallelizes worse than research), and the "can't vibe orchestrate" build-first rule. Page date moves to 4 September.
- **Harness (agent)** gains a new entry for Harvey + Baseten's RLM due-diligence harness (23% → 62% pass-rate jump, plus post-training gains on top), clearly distinguished from the existing Prime Agent RLM reference, and an extension to the existing DeepAgents mention naming the specific new `deepagents` primitives (subagent context-forking, managed OAuth/consent connections). Page date moves to 4 September.
- One new source page for Every's folder-is-the-agent piece. The RLM-harness and LangChain facts come from the newsletter already owned by the Navier-Stokes proposal in this batch (`ainews-navier-stokes-2026-09-09`) — referenced here, not recreated.

### What to weigh

The source explicitly frames itself as a *rerun* of an April 2026 Every piece, republished with new material ahead of a follow-up article — the core "folder is the agent" claim is not new to this wiki, only the dispatch-layer mechanics and the Anthropic citation are. Harvey and Baseten's 23%→62% figure is measured on their own synthetic diligence benchmark, not an independently reproduced or third-party-audited eval.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — extends the existing folder-scoped-specialization pattern with dispatch-layer mechanics and the Anthropic multi-agent research citation
    > See draft below

- [ ] **Update** `wiki/concepts/harness.md` — new RLM due-diligence harness entry (Harvey + Baseten), extended DeepAgents mention (LangChain subagent forking, managed connections)
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-folder-is-the-agent-2026-09-04.md` — source summary

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Frontmatter `as_of` moves from `2026-09-07` to `2026-09-07` (unchanged — this proposal's newest fact is dated 2026-09-04, older than the page's current date); append `every-folder-is-the-agent-2026-09-04` to `sources:`.

The existing bullet — `**Folder-scoped specialization.** A durable folder plus instructions, skills, and accumulated context often works better than a "swarm" of generic agents sharing one giant context.` — is replaced with:

```md
- **Folder-scoped specialization.** A durable folder plus instructions, skills, and accumulated context often works better than a "swarm" of generic agents sharing one giant context. A concrete production instance: Every's Cora GM runs 44 specialized agents as folders (each a project directory with a CLAUDE.md/AGENT.md, skills, and months of accumulated institutional knowledge), routed by a small dispatch layer — a daemon watches a directory for spawn requests, a lead agent breaks a task into subtasks and writes each as a file, worker agents in the right folders pick them up and report back by writing files, and the daemon polls status every 60 seconds. Two slash commands cover most interaction: a cross-project status briefing, and a task-kickoff command that spawns the lead and workers. He cites Anthropic's own multi-agent research to justify the approach — an Opus lead with Sonnet sub-agents beat a single Opus agent by 90% on research tasks, but multi-agent setups burn 15x more tokens, and most coding tasks parallelize worse than research does — and states the hard-won rule plainly: "you can't vibe orchestrate." Build a flow, use it yourself, and trust it before handing it to autonomous dispatch. *Source: Every, "The Folder Is the Agent" (2026-09-04)*
```

New entry at the top of `## Recent changes`:

```md
- [2026-09-04] Extended folder-scoped specialization with a concrete 44-agent dispatch-layer implementation (daemon, status/orchestrate commands, file-based worker reporting) and Anthropic's multi-agent-research numbers (90% better / 15x tokens for Opus-lead + Sonnet-subagent research tasks).
```

### wiki/concepts/harness.md (updated)

Frontmatter `as_of` moves from `2026-09-07` to `2026-09-07` (unchanged — newest fact here is also 2026-09-04); append `every-folder-is-the-agent-2026-09-04, ainews-navier-stokes-2026-09-09` to `sources:`.

New bullet added to the `## What good harness engineering looks like` list, after the existing Prime Agent bullet:

```md
- **RLM-style sub-agent harness for enterprise due diligence.** Harvey and Baseten built a recursive-language-model harness for M&A due diligence, distinct from Prime Intellect's general-purpose Prime Agent above: a root agent searches a data room and delegates document review to sub-agents, aggregating findings over corpora up to 80M tokens. Moving from a standard tool-calling loop to this RLM harness raised mean rubric pass rate on their synthetic diligence benchmark from 23% to 62%; harness-specific post-training on top (self-distilled SFT on GLM-5.2, GRPO on Qwen3.5) added another 15-33 points depending on the base model — a second concrete data point (after the SWE-bench Pro and Composio results already on this page) that harness and post-training design move benchmark scores as much as, or more than, the base model swap. LangChain shipped matching primitives in `deepagents` the same week: subagent forking that passes a supervisor's context down to its subagents, and managed connections that abstract OAuth/token/consent flows for either agent-owned or user-owned identities — concrete implementations of the deployment-manifest/access-control layer this page already tracks via `deepagents.toml`.
```

New entry at the top of `## Recent changes`:

```md
- [2026-09-04] Added Harvey + Baseten's RLM due-diligence harness (23%→62% rubric pass rate via harness swap, +15-33 points from harness-specific post-training) and LangChain deepagents' subagent-forking and managed-connection primitives.
```

### wiki/sources/newsletters/every-folder-is-the-agent-2026-09-04.md (new)

```md
---
title: The Folder Is the Agent
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-04-the-folder-is-the-agent.md
url: https://every.to/source-code/the-folder-is-the-agent-rerun
published: 2026-09-04
ingested: 2026-09-09
domains: [agents, coding]
---

# The Folder Is the Agent

Every's Kieran Klaassen (Cora GM) describes running 44 specialized agents as durable folders, each with its own CLAUDE.md/AGENT.md, skills, and accumulated institutional knowledge, routed by a small file-based dispatch layer. Cites Anthropic's own multi-agent research (90% better / 15x tokens for Opus-lead + Sonnet-subagent research tasks) and closes on "you can't vibe orchestrate" — build and trust a flow before handing it to autonomous dispatch.

## Influenced pages

- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — extended folder-scoped-specialization pattern with dispatch-layer mechanics and the Anthropic citation

## Key claims extracted

- 44 agents run as folders, routed by a Ruby daemon dispatch layer
- Two slash commands: cross-project status briefing, and task-kickoff/orchestrate
- Anthropic: Opus lead + Sonnet sub-agents beat single Opus by 90% on research tasks, at 15x the token cost
- Most coding tasks parallelize worse than research tasks
- Rule of thumb: build a flow yourself, use it, trust it — only then hand it to autonomous dispatch
```

## Schema / vocabulary additions

None.

## Open questions

- The source mentions "Anthropic just launched Claude Managed Agents" in passing. `wiki/tools/claude-managed-agents.md` is still dated 2026-05-20 (public beta), but `wiki/concepts/harness.md` already separately tracks an August 2026 GA milestone (computer use, browser tool, Skills API, Files API) that this tool page's own Recent-changes list hasn't caught up with. This source doesn't add anything the wiki doesn't already know more precisely, so this proposal leaves `claude-managed-agents.md` untouched — syncing its Recent-changes with the already-known August GA milestone would be a good separate follow-up proposal.
