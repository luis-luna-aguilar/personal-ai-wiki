---
title: Devin Bots
type: tool
domains: [agents, coding]
subcategory: agent-orchestration
tags: [cognition, agentic]
as_of: 2026-11-23
sources: [devinai-bots]
---

# Devin Bots

Cognition's entry into the AI-teammate category, alongside [Grok Bot](grok-bot.md), [Claude Tag](claude-tag.md) and [ChatGPT dots](chatgpt-dots.md), but built around engineering work rather than general office tasks. A Bot is a persistent manager agent on top of [Devin](devin.md): given a goal ("move checkout to the new payments API"), it breaks the work down and runs parallel Devin sessions, each on its own cloud VM, until every pull request passes tests and review.

## Current status (as of 2026-11-23)

- Reachable by text, Slack, phone call (spoken updates) or group chat; a "Needs you" queue surfaces only approvals, blockers and decisions (a production deploy, a missing API key, a keep-or-drop call).
- Runs on schedules and triggers, e.g. watching a support channel for customer bugs, checking CI health nightly, or watching Linear for blocked tickets.
- Bots hand work to one another in Slack: in Cognition's demo a QA Bot finds a bug, a Developer Bot fixes it, the QA Bot retests and a PM Bot reports progress.
- Built on Devin's existing stack (codebase understanding, a cloud computer per agent, Devin Review, automated browser testing); six launch templates: Software Factory, Android Engineer, Chief of Staff, Latency Optimizer, Product Engineer, QA Engineer.
- Enterprise controls: per-session VM, zero data retention with model providers, audit logs, RBAC/SSO/SCIM/OIDC, private networking.

## Evidence from practice

Bilt's VP of Engineering says its Bots merged about 1,600 PRs in one week; Fireworks AI says productivity tripled. Decagon and Reducto describe it as engineering-focused rather than a calendar or email summarizer. It ran as a beta before launch.

## Weaknesses / caveats

- No pricing published.
- The product page carries no launch date; 2026-11-23 (the fetch date) is used.
- Launch page only, no technical write-up of how the manager agent plans or splits work.

## Recent changes

- [2026-11-23] Launched: persistent AI teammates that split a goal across parallel Devin sessions on separate VMs, reachable by text, Slack or phone, with schedules, triggers and bot-to-bot handoff.

## Sources

- [Cognition — Devin Bots product page](../sources/articles/devinai-bots.md)
