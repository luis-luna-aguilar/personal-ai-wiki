---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-04-22
sources: [cursor-3-launch, advisor-strategy, stripe-cli, managed-agents, agentic-thinking-lin, curiosity-driven-imagination, openai-agents-sdk-evolution, ainews-2026-04-21, ainews-2026-04-22, claude-cowork-launch, every-managed-agents-vibe-check, claude-design-launch, orca-homepage, anthropic-platform-expansion-april-2026, coding-agent-control-planes, claude-productivity-surfaces, open-agent-orchestration-late-march, proof-agent-native-documents, cursor-cloud-agents-march, cursor-cloud-agents-february]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

## Subcategories

### Agent orchestration UIs

Surfaces (desktop, web, mobile, chat) where humans supervise, hand off, and review work across multiple AI agents running in parallel.

- [[tools/claude-design]] — Anthropic; research-preview artifact-generation surface for prototypes, slides, and one-pagers, pushing Claude toward generated business artifacts rather than chat-only output *(as of 2026-04-21)*
- [[tools/claude-cowork]] — Anthropic; desktop knowledge-work agent with Live Artifacts, released alongside [[tools/claude-design]] as part of a broader push toward generated dashboards, reports, and prototypes; the earlier Claude for Word beta suggests this artifact/productivity direction started before Cowork itself *(as of 2026-04-21)*
- [[tools/cursor]] — Cursor's cloud-agent walkthrough made the orchestration-ui thesis explicit before the April 3.1 polish pass: agents run remotely, test their own work, return videos, and hand the human a supervision layer over many coding agents rather than a single-agent IDE *(as of 2026-03-06)*
- [[tools/orca]] — Open-source desktop surface for supervising multiple coding agents across isolated worktrees, with live status reporting, diff review, and CI visibility *(as of 2026-04-21)*

### Agent orchestration

Platforms that run or coordinate long-horizon agents across execution environments, instead of only exposing a local loop or a thin UI over one agent.

- [[tools/claude-managed-agents]] — Anthropic's public-beta hosted runtime separates session, harness, and sandbox; the surrounding April product cadence makes it look like the platform backbone behind a broader Anthropic agent stack, not just an isolated architecture post *(as of 2026-04-15)*
- [[tools/openai-agents-sdk]] — OpenAI's updated SDK combines a model-native harness with native sandbox execution, durable checkpoint / rehydration, provider-neutral manifests, and built-in support for MCP, skills, AGENTS.md, shell, and `apply_patch` *(as of 2026-04-15)*
- [[tools/hermes-agent]] — NousResearch; open-source autonomous agent framework; 100K+ GitHub stars; four-layer memory with periodic consolidation; stateless sub-agent parallelism, LLM-driven replanning, directory-local context injection *(as of 2026-04-21)*

### Model orchestration

Patterns that combine models of different sizes or costs inside a single agentic task. Concerned with *how* agents are structured internally (which model runs the loop, which model steps in when), not with the user-facing surface.

- [[workflows/advisor-strategy]] — Anthropic: a small executor (Sonnet or Haiku) drives the loop and escalates to Opus as an *advisor* only when stuck. Shipped as a server-side `advisor_20260301` tool on the Claude API, making it a one-line change to a Messages request. Reported +2.7% on SWE-bench Multilingual *and* −11.9% cost for Sonnet+Opus-advisor vs Sonnet alone *(as of 2026-04-09)*

### Agentic DevOps

Agent-compatible tools that let a model provision external services and receive credentials through a repeatable CLI workflow instead of clicking through SaaS dashboards.

- [[tools/stripe-cli]] — Stripe explicitly pitches the CLI `projects` flow for "you or your agents": provision services across providers, sync credentials back to the environment, and manage upgrades or billing from the CLI *(as of 2026-04-09)*

### Agent-native documents

Document surfaces built for humans and agents to collaborate inside the same working artifact, with revision, provenance, and comments happening in-place instead of around pasted AI output.

- [[tools/proof]] — Every's web document editor is the clearest current example of the "agent-native document" thesis: plans, memos, and working docs are treated as shared human/AI artifacts with provenance, comments, and tracked edits built into the document itself *(as of 2026-03-15)*

### Autonomous research agents

Agents that close the full research loop end-to-end — reading literature, collecting data, running experiments, evaluating results, and iterating — with minimal human steering between steps.

- [[tools/hf-ml-intern]] — Hugging Face; open-source ML post-training research loop agent; reads papers, collects datasets, launches training jobs, evaluates, and iterates; GPQA 10% → 32% in <10 hours on Qwen3-1.7B *(as of 2026-04-22)*

## Recent changes

- [2026-04-22] Added `Autonomous research agents` subcategory; [[tools/hf-ml-intern]] is the first publicly verified agent to close the full ML post-training loop end-to-end
- [2026-04-22] Google Deep Research Max scores (93.3% DeepSearchQA) and HF ml-intern autonomous loop mark the emergence of a distinct "full-stack research agent" tier — see [[tools/gemini]] and [[tools/hf-ml-intern]]
- [2026-02-25] Cursor's cloud-agent rollout already showed the orchestration-ui pattern in product form: remote agent computers, self-verification, and video artifacts for human review
- [2026-03-06] Cursor's cloud-agent walkthrough made the category's supervision thesis explicit before the later 3.1 control-plane polish: remote agents, review videos, and human oversight over many workers
- [2026-04-22] Added `Agent-native documents` to capture document surfaces built for shared human/agent drafting; [[tools/proof]] is the first example
- [2026-04-21] Added [[tools/orca]] under `Agent orchestration UIs`; worktree-first desktop supervision layer for Claude Code, Codex, and similar agents
- [2026-03-31] Backfilled late-March signal: open-agent stacks were already converging on CLI-first execution, worktree coordination, and packaged reusable agents before the April orchestration/control-plane wave became clearer
- [2026-04-21] Added earlier Anthropic productivity-surface precursor: Claude for Word beta helps explain Cowork / Live Artifacts as expansion of an existing direction
- [2026-04-15] Anthropic's Managed Agents now reads as part of a broader platform cluster: hosted runtime, custom agents, and Claude Code long-running monitor/loop patterns
- [2026-04-14] Cursor 3.1 added tiled multi-agent supervision and stronger control-plane UX, reinforcing the shift from AI-enhanced IDEs toward agent workspaces
