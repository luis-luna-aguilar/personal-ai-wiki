---
title: Claude Mythos Preview
type: model
domains: [models, cybersecurity]
subcategory: frontier-multimodal-model
tags: [anthropic, closed-source, beta]
as_of: 2026-04-22
sources: [glasswing]
---

# Claude Mythos Preview

Anthropic's restricted-preview frontier model, demonstrated through Project Glasswing. Not publicly available. Operates above the current Opus 4.7 tier in autonomous cybersecurity capability.

## Current status (as of 2026-04-22)

- Not publicly available; accessible only via Anthropic's Project Glasswing partner program
- Used to autonomously identify thousands of zero-day vulnerabilities in every major OS and web browser — without human steering
- Partners confirmed: Cisco, AWS, Microsoft
- Substantially outperforms Claude Opus 4.6 on the CyberGym benchmark
- Anthropic is disclosing vulnerabilities responsibly: patched vulns released; unpatched vulns hashed for future release

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

## Sources

- [Project Glasswing](../sources/articles/glasswing.md)
