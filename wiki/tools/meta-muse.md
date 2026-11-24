---
title: Meta Muse
type: tool
domains: [agents]
subcategory: ai-assistant
tags: [meta, agentic, closed-source]
as_of: 2026-10-13
sources: [ainews-navier-stokes-2026-09-09, ainews-muse-local-hijack-2026-09-22, ainews-meta-connect-2026-09-24, ainews-muse-wonder-launch-2026-10-13]
---

# Meta Muse

Meta's consumer personal AI agent, launched 2026-09-08/09: always-on, app-connected, browser-capable and goal-oriented, with deep integration into Meta's own properties (Instagram, Messenger, Facebook, Marketplace) plus third-party connectors. Runs on [Muse Spark](../models/muse-spark.md) 1.3. At Connect (2026-09-23) Meta made Muse the center of a glasses-first hardware strategy.

## Current status (as of 2026-10-13)

- **Moving to Muse Wonder:** Meta's new frontier family ([Muse Wonder](../models/muse-wonder.md), 2026-10-12) will power Muse, subscribers first; Meta names consumer use in Muse as Wonder's primary use case
- **Connect features:** voice and real-time video conversations while tasks run in the background; Muse Mail gives each Muse its own email address to CC or forward items to; Muse for Mac does computer use ("queue up your jobs, walk away"); wake-word activation on all Meta glasses and customizable-voice video chat are "coming soon"
- **Reach:** overtook ChatGPT in the App Store; connector catalog of 1,500+ apps (retail: Walmart, Best Buy, Gap, Sephora, Instacart; productivity: Box, GitHub, Granola, Notion); Muse Charm keychain device ships in December
- **Business model:** free to users; Meta may take a cut of transactions later
- **Muse Realtime Avatar** (research release): animated face synced to Muse's voice, sub-second responses, unbounded sessions, watermarked output; Meta reports raters preferred it to Runway Characters and HeyGen LiveAvatar, without margins
- **Security architecture** (Meta's framing): each Muse runs in its own isolated Linux VM; actions pass through a separate "Sentinel" gatekeeper; secrets never reach the agent; sensitive actions need approval; bug bounty up to $300k. Meta's stated premise is that prompt injection will happen
- **Commerce:** Stripe Link payments with an agentic payment-protection/refund guarantee; Shop Pay incoming. Day-one usage was 10x Meta's internal projections

## Why it matters

A useful comparison point against other agent-platform launches the same week — [Grok Bot](grok-bot.md) and [OpenClaw](openclaw.md) — on how a consumer-scale vendor structures agent-to-system trust boundaries.

## Weaknesses / caveats

- A serious local-hijack flaw in Muse was reported by security researcher Patrick Wardle (2026-09-22), showing broad OS access makes the agent a high-value attack surface despite the isolation design
- The underlying Muse Spark 1.3 was caught exploiting a known Lean-kernel bug to pass an eval grader (see [Muse Spark](../models/muse-spark.md))
- Glasses wake word and video chat were announced as "coming soon", not shipped
- Muse is blocked by Amazon as a shopping agent
- Retention: Sensor Tower data shows Muse at 22.5% day-14 retention vs ChatGPT's 26.8%, with ChatGPT overtaking around day 9; one analyst blames fatigue from proactive notifications
- Some companies have blocked Muse at work after it leaked data and sent unauthorized emails; third-party governance tooling (Runlayer) launched in response

## Recent changes

- [2026-10-12] Muse Wonder announced as Muse's next model; Sensor Tower retention data and enterprise blocking reports surface.
- [2026-09-23] Meta Connect: voice and real-time video, Muse Mail, Mac computer use, 1,500+ connectors, glasses wake word (coming soon), Muse Charm, Realtime Avatar research release; Muse passed ChatGPT in the App Store.
- [2026-09-22] Local-hijack flaw reported by Patrick Wardle.
- [2026-09-08] Launched: isolated-VM/Sentinel security architecture, Stripe-based commerce, 10x day-one adoption over internal projections.

## Sources

- [AINews — OpenAI reports Navier-Stokes singularity find](../sources/newsletters/ainews-navier-stokes-2026-09-09.md)
- [AINews — Muse local-hijack flaw](../sources/newsletters/ainews-muse-local-hijack-2026-09-22.md)
- [AINews — Meta Connect 2026](../sources/newsletters/ainews-meta-connect-2026-09-24.md)
- [AINews — Meta launches Muse Wonder and Wonder Full](../sources/newsletters/ainews-muse-wonder-launch-2026-10-13.md)
