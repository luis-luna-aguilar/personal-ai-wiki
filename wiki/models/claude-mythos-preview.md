---
title: Claude Mythos Preview
type: model
domains: [models, cybersecurity, agents]
subcategory: frontier-multimodal-model
tags: [anthropic, closed-source, beta]
as_of: 2026-05-12
sources: [glasswing, metr-long-horizon-2026-05-12]
---

# Claude Mythos Preview

Anthropic's restricted-preview frontier model, demonstrated through Project Glasswing. Not publicly available. Operates above the current Opus 4.7 tier in autonomous cybersecurity capability.

## Current status (as of 2026-05-12)

- Not publicly available; accessible only via Anthropic's Project Glasswing partner program
- Used to autonomously identify thousands of zero-day vulnerabilities in every major OS and web browser — without human steering
- Partners confirmed: Cisco, AWS, Microsoft
- Substantially outperforms Claude Opus 4.6 on the CyberGym benchmark

## METR long-horizon benchmark (May 2026)

METR's time-horizon task benchmark measures how reliably an AI model can complete tasks that METR rates by how long an equivalent task would take a human software engineer.

- **50% success at "16+ hours"** — Mythos Preview is the first model to hit 50% at the top category of METR's current scale, effectively breaking the ceiling
- **80% reliability threshold ≈ 3 human-hours** — at the more operationally useful 80% bar (the point where the agent succeeds reliably enough to delegate without close supervision), Mythos handles tasks worth roughly 3 hours of human-equivalent work
- **Nearest competitor: Gemini 3.1 Pro at ~1.5 human-hours** at the 80% threshold
- **Duration is a difficulty proxy** — METR cautions that the "hours" metric measures task complexity, not literal wall-clock time; AI agents complete these tasks faster than the human baseline

## What it found (sample)

- **OpenBSD:** 27-year-old remote-crash flaw — remote crash of any machine running the OS
- **FFmpeg:** 16-year-old bug missed by automated tools 5 million times
- **Linux kernel:** Chained multiple vulns to escalate from ordinary user to full machine control — autonomously, without human steering

## Why it matters

Mythos Preview is the first public evidence of an Anthropic model operating autonomously at a capability threshold that materially changes the cyber-threat model for critical infrastructure. It confirms the [Restricted frontier deployment](../trends/restricted-frontier-deployment.md) pattern: Anthropic chose partner-access-only rather than broad public release, framing the announcement as a safety mobilization event.

## Caveats

- All capabilities reported by Anthropic; no independent benchmark replication
- "Thousands of zero-days" includes varying severity; only highest-impact examples disclosed so far
- Deployment policy could evolve; partner list may expand

## Recent changes

- [2026-05-12] METR long-horizon benchmark: 50% at 16+ hours (breaks scale ceiling); 80% reliability threshold ~3 human-hours; Gemini 3.1 Pro closest competitor at ~1.5 hours
- [2026-04-22] Initial page created from Project Glasswing; cybersecurity capabilities documented

## Sources

- [Project Glasswing](../sources/articles/glasswing.md)
- [METR long-horizon benchmark — The Fallacy of the 16-Hour Agent](../sources/newsletters/metr-long-horizon-2026-05-12.md)
