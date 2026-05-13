---
type: proposal
source: raw/newsletters/2026-05-01-ainews-agents-for-everything-else-codex-for-kno.md
status: pending
created: 2026-05-05
---

# Proposal: Agent infrastructure shifts toward harness and deployment primitives

## Summary

AINews clusters three related infrastructure signals: Cursor describing how it tests and tunes its agent harness, LangChain packaging DeepAgents deployment through `deepagents.toml`, and Agent Collabs using Hugging Face buckets plus Spaces as lightweight shared workspaces for heterogeneous agents. The durable wiki update is to concepts/workflows, not individual tool pages for every project.

## Intended changes

- [x] **Update** `wiki/concepts/harness.md` — add a current-state note that production harness work is increasingly about runtime, evals, degradation repair, model-specific tuning, deployment config, auth, RBAC, credentials, and collaboration surfaces.

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add `Config-driven agent deployment` and `Artifact-backed agent collaboration` to current patterns.

- [x] **Update** `wiki/state-of/agents.md` — add a recent-change entry noting the shift from model wrappers toward engineered runtimes, deployment, isolation, credentials, and shared workspaces.

- [x] **Create** `wiki/sources/newsletters/agent-infrastructure-harness-2026-05-01.md` — source summary.

## Page drafts

### Draft additions

```markdown
## Current patterns

- **Config-driven agent deployment.** Production agent frameworks are starting to package sandboxing, auth, frontend, and runtime configuration into deployable manifests instead of leaving each deployment as bespoke glue.
- **Artifact-backed agent collaboration.** Multi-agent collaboration is becoming more concrete when agents exchange messages, artifacts, and progress through shared storage/workspaces rather than one shared transcript.
```

### wiki/sources/newsletters/agent-infrastructure-harness-2026-05-01.md (new)

```markdown
---
title: Agent infrastructure, harness engineering, and collaborative agent systems
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-01-ainews-agents-for-everything-else-codex-for-kno.md
published: 2026-05-01
ingested: 2026-05-05
domains: [agents]
---

# Agent infrastructure, harness engineering, and collaborative agent systems

AINews groups several infrastructure signals around Cursor's harness testing/tuning, LangChain DeepAgents deployment configuration, and Agent Collabs' shared workspace pattern using Hugging Face buckets and Spaces.

## Influenced pages

- [Harness](../../concepts/harness.md) — update production-harness responsibilities
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — add deployment and collaboration primitives
- [State of Agents](../../state-of/agents.md) — recent-change note

## Key claims extracted

- Agent builders are discussing runtime, evals, degradation repair, and model-specific customization as first-class harness work.
- Deployment concerns include sandboxing, auth, frontend configuration, credentials, data isolation, and RBAC.
- Shared workspaces and artifact exchange are emerging as practical multi-agent collaboration primitives.
```

## Feedback

- What is RBAC? Please state it when you mention it.
- Also, i dont know what are all these concepts, they need to be included in this wiki: DeepAgents, Agent Collabs, Hugging Face buckets & Spaces.
- "instead of leaving each deployment as bespoke glue" - i dont understand that, please do a solid example instead
- "shared storage/workspaces" can we link this to a concept in this wiki? or explain it further. im also far from that concept