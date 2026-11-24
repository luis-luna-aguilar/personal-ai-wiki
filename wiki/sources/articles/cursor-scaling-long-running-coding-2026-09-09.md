---
title: Cursor — Scaling long-running autonomous coding
type: source
source_type: article
source_file: raw/articles/2026-09-09-cursorcom-blog-scaling-agents.md
url: https://cursor.com/blog/scaling-agents
ingested: 2026-10-20
domains: [agents, coding]
---

# Cursor — Scaling long-running autonomous coding

Cursor's first post on running hundreds of concurrent coding agents on one project for weeks; its later "Towards self-driving codebases" post builds on it. It covers why flat self-coordination failed (locks, then optimistic concurrency with risk-averse agents), the planner/worker/judge pipeline that replaced it, the browser, Solid-to-React and video-renderer runs, model choice by role, and open problems. The page shows no publication date; it predates the 9 September 2026 posts already in the wiki and was fetched on that date.

## Influenced pages

- [Long-running agent swarms](../../workflows/long-running-agent-swarms.md) — optimistic-concurrency failure, run sizes, model choice by role, open problems

## Key claims extracted

- Flat self-coordination through a shared file with locks: locks held too long or never released; 20 agents slowed to the throughput of 2–3; brittle failure modes
- Optimistic concurrency control was simpler and more robust, but with no hierarchy agents became risk-averse, avoided hard tasks, and churned without progress
- Planners explore and create tasks and can spawn sub-planners; workers complete one task and push; a judge decides at each cycle's end whether to continue; each cycle starts fresh
- Browser from scratch: close to a week, over 1M lines across 1,000 files, hundreds of concurrent workers pushing to one branch with minimal conflicts (github.com/wilsonzlin/fastrender)
- Solid-to-React migration in Cursor's codebase: 3+ weeks, +266K/−193K edits, passing CI and early checks, still needing review
- Video rendering made 25x faster with a Rust version; merged
- GPT-5.2 better than Opus 4.5 for extended autonomous work; Opus 4.5 stops earlier and takes shortcuts; GPT-5.2 a better planner than GPT-5.1-Codex; model chosen per role
- Removing the integrator role helped; the right structure is in the middle; prompts matter more than harness and models
- Open problems: planners should wake when tasks complete; agents sometimes run too long; periodic fresh starts still needed
