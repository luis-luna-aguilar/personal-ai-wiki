---
title: gstack
type: tool
domains: [coding, agents]
subcategory: agent-toolkits
tags: [open-source, anthropic, agentic]
as_of: 2026-04-22
sources: [garrytan-gstack-repo]
---

# gstack

Garry Tan's open-source Claude Code configuration. 23 slash commands that turn Claude Code into a virtual engineering team: CEO (product rethinking), designer (AI slop detection), eng manager (architecture lock), release manager, QA lead (real browser), security officer (OWASP/STRIDE), and more. Free, MIT-licensed.

## Current status (as of 2026-04-22)

- 23 slash commands, all Markdown, all free, MIT license
- Roles included: CEO, designer, eng manager, doc engineer, QA lead, security officer, release manager
- Garry Tan's reported productivity: 810× his 2013 coding pace (logical-code-change metric); 3 production services + 40+ features in 60 days part-time while running YC
- More than one-third of his PRs from agents
- Includes 8 "power tools" beyond the role slash commands
- Methodology and LOC controversy addressed in `/docs/ON_THE_LOC_CONTROVERSY.md`

## Why it matters

gstack is one of the first open-source, practitioner-validated Claude Code setups with published productivity numbers and a replicable methodology. The 810× claim is more credible than typical hype because the metric is logical-code-change (not raw LOC, which inflates with AI) and Tan published the methodology for reproduction. The role-simulation approach shows a practical way to avoid "blank prompt" paralysis in agentic development.

## Caveats

- Productivity numbers are self-reported by Tan; methodology is published but unverified independently
- Works with Claude Code; may need adaptation for other coding agents
- 810× is Tan's personal run rate — transferability to other developers depends heavily on experience and project type

## Sources

- [gstack — Garry Tan's Claude Code virtual engineering team](../sources/repos/garrytan-gstack-repo.md)
