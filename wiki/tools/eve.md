---
title: eve
type: tool
domains: [agents]
subcategory: agent-framework
tags: [agentic]
as_of: 2026-07-03
sources: [vercel-agents-new-software-2026-07-03]
---

# eve

eve is Vercel's framework for building agents, described by Andrew Qu as the result of Vercel turning hard-won v0 and internal-agent patterns into reusable primitives.

## Current status (as of 2026-07-03)

- Built around agent primitives Vercel found missing: model/provider switching, fallbacks, resumability, filesystem agents, skills, compaction, subagents, sandboxes, and long-running jobs.
- Deploying eve to Vercel is described as providing observability and evaluations out of the box.
- Vercel frames agents as a new kind of software with dynamic interfaces and outputs, not just web apps with an AI layer.

## Strengths

- Strong platform fit: Vercel is building eve from production experience with v0 and internal agents.
- Emphasizes resumability, long-running work, and current product knowledge through skills.

## Weaknesses / caveats

- Current source is interview coverage rather than official docs.
- It is not yet clear how much of the framework is public, stable, or broadly adopted.

## Recent changes

- [2026-07-03] Andrew Qu described eve as Vercel's prescriptive agent framework.

## Sources

- [Vercel's Andrew Qu on why agents are a new kind of software](../sources/newsletters/vercel-agents-new-software-2026-07-03.md)
