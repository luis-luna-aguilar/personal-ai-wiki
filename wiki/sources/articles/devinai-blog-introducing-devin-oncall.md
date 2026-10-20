---
title: "Cognition — Introducing Devin Oncall"
type: source
source_type: article
source_file: raw/articles/2026-10-19-devinai-blog-introducing-devin-oncall.md
url: https://devin.ai/blog/introducing-devin-oncall
ingested: 2026-10-19
domains: [agents, coding]
---

# Cognition — Introducing Devin Oncall

Cognition makes Devin Oncall generally available: Devin investigates alerts and bug reports, diagnoses production incidents and mitigates them. Its Responders product is explicitly "the next generation of Auto-Triage" (see [Devin Auto-Triage launch](devin-auto-triage-2026-05.md)): the same parent/child alert-stream design, now with issue memory that skips repeat investigations, plus a separate Incidents product for live incident channels. Cognition argues that runbooks, custom graph architectures and SRE post-training age badly as models improve, so the core should be a strong general coding agent with context, tools and workflows, and it organizes Oncall into core intelligence, company context and agent behavior. The post carries no date; it cites an SREGym leaderboard snapshot from 15 October 2026.

## Influenced pages

- [Devin](../../tools/devin.md) — Auto-Triage bullets replaced by Oncall (Responders, Incidents, review agent, context layers, results)
- [State of Agents](../../state-of/agents.md) — Devin line updated under Agent orchestration; added under Agentic DevOps
- [Agentic infrastructure operations](../../training/agentic-infrastructure-operations.md) — first production evidence and a new failure mode

## Key claims extracted

- Devin Oncall generally available; handles thousands of production alerts per day
- SREGym-Lite (17 faults, root cause plus live mitigation): Devin Oncall 100% end-to-end; fastest with Opus 5.5 at 2m 21s; GPT-6 Astra 100%, GPT-6.1 Sol 94.1%, Fable 5.1 85.3% in Devin; CloudThinker also reached 100% with GPT-6 Astra on the public leaderboard (as of 2026-10-15)
- Responders: hidden parent Devin watches the alert stream, launches fresh-context child investigations for new issues; skips ~60% of investigations, more than halving cost; Alert Responders and Support + Bug Responders
- Incidents: parent investigates in the background and maintains a live incident doc; child Devins answer direct questions; messages relevance-filtered
- Asynchronous review agent checks for correlation-as-causation, dismissed contradictory telemetry, trigger-vs-cause confusion
- Context layers: per-responder memory, per-org generated skills, per-org memory from post-processed investigations
- Reducto: Devin opened an incident before production alerts fired; handles most engineering alerts first
- RV Tech: Devin does the first-pass investigation of customer vehicle reports, freeing several engineers for product work
- AngelList: 3.5x more correct root causes than in-house harness Sky; 50% of incidents end-to-end; Sky deprecated
