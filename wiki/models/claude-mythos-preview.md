---
title: Claude Mythos Preview
type: model
domains: [models, cybersecurity, agents]
subcategory: frontier-model
tags: [anthropic, closed-source, beta]
as_of: 2026-05-19
sources: [glasswing, metr-long-horizon-2026-05-12, claude-mythos-m5-bypass-2026-05, cloudflare-glasswing-2026-05]
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

## Cloudflare Project Glasswing operational findings (May 2026)

Cloudflare red-teamed 50+ of their own repositories with Mythos Preview. Key observations:

- **Exploit chain construction** — Mythos chains multiple low-severity bugs into a single, higher-severity working proof of concept. Previous frontier models would identify interesting bugs but stop short of chaining them. This is the capability gap that distinguishes Mythos from Opus 4.7 / GPT-5.5 for security work.
- **Proof generation loop** — Mythos writes PoC code, compiles it in a scratch environment, runs it, reads failure output, adjusts, and retries autonomously. Finding a bug and proving it exploitable are both within scope.
- **Organic refusals are probabilistically inconsistent** — same task framed differently or presented in a different context can produce opposite outcomes. Refusals are real but not sufficient as a complete safety boundary; additional safeguards are required for any general deployment.
- **Generic coding agents are the wrong tool** — pointing a single coding agent at a large repo produces poor coverage. Mythos requires a harness with many narrow-scope concurrent agents to achieve meaningful security coverage.

Cloudflare's architectural takeaway: "Patching faster is not the answer." Defenses-in-front, component isolation, and simultaneous rollout matter more than compressing the patch cycle.

## Apple M5 MIE bypass (May 2026)

- Calif research team (Vietnam) used Mythos Preview to defeat Apple's Memory Integrity Enforcement (MIE) — Apple's strongest-ever hardware security layer, first shipped on M5
- Timeline: under 5 days from start to first public kernel memory corruption exploit on M5 silicon
- Human expertise was essential for the MIE bypass itself; Mythos's role was surfacing bugs extremely quickly
- Access was restricted (non-public Mythos Preview); Calif + Anthropic are co-developing a patch; report delivered in person to Apple Cupertino
- Signal: "Apple built MIE in a world before Mythos Preview" — hardware defenses designed before frontier AI may need reassessment
- Broader pattern: small teams + frontier AI can now match security research throughput that previously required entire organizations

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

- [2026-05-19] Cloudflare Project Glasswing detailed writeup: exploit chain construction, proof generation loop, inconsistent organic refusals, and 8-stage narrow-scope harness architecture confirmed
- [2026-05-18] Apple M5 MIE bypass: Calif team + Mythos Preview defeated Memory Integrity Enforcement in <5 days — first public kernel memory corruption on M5; small team + frontier AI matches org-scale security research throughput
- [2026-05-12] METR long-horizon benchmark: 50% at 16+ hours (breaks scale ceiling); 80% reliability threshold ~3 human-hours; Gemini 3.1 Pro closest competitor at ~1.5 hours
- [2026-04-22] Initial page created from Project Glasswing; cybersecurity capabilities documented

## Sources

- [Project Glasswing](../sources/articles/glasswing.md)
- [METR long-horizon benchmark — The Fallacy of the 16-Hour Agent](../sources/newsletters/metr-long-horizon-2026-05-12.md)
- [Apple M5 MIE bypass — Claude Mythos Preview](../sources/newsletters/claude-mythos-m5-bypass-2026-05.md)
- [Project Glasswing: what Mythos showed us — Cloudflare](../sources/articles/cloudflare-glasswing-2026-05.md)
