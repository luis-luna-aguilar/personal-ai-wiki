---
title: Cognition — Introducing Code Scans (X thread)
type: source
source_type: tweet
source_file: raw/tweets/2026-09-16-xcom-cognitionstatus210025354888580.md
url: https://x.com/cognition/status/2100253548885803404
published: 2026-09-16
ingested: 2026-11-24
domains: [coding, agents]
---

# Cognition — Introducing Code Scans (X thread)

Cognition's launch thread for Code Scans, codebase-wide audits toward a stated goal, powered by Agentic MapReduce. AINews mentioned the launch on 2026-09-17 (`raw/newsletters/2026-09-17-ainews-reality-checks-on-ai-news-yegge-shuts-do.md`). AINews on 2026-09-16 (`raw/newsletters/2026-09-16-ainews-jev-a-system-one-model-that-only-decid.md`) relayed the same week's cross-OS VM news from @jeffwang and @jkelleyrtp, and that item is recorded here too.

## Influenced pages
- [Devin](../../tools/devin.md) — Code Scans and cross-OS VM bullets
- [State of Coding](../../state-of/coding.md) — refreshed Devin leader line

## Key claims extracted
- Code Scans (`/scan`) are codebase-wide audits for any goal. Devin investigates, reports findings and opens PRs.
- Targets include slow paths and N+1 queries, untested flows and edge cases, dead code and stale feature flags, WCAG accessibility, and team coding standards. Devin helps scope what to inspect and what counts as a finding.
- In the Dioxus repo, debug build time fell from 58.6s to 21.0s (64%) across 22 workspace crates.
- AINews, 2026-09-16: Devin can spin up Mac VMs for end-to-end iOS development from Slack or the web UI. It is a cloud agent across macOS, Windows and Linux, with storage, networking, VNC and computer-use infrastructure rebuilt in Rust. Dioxus Labs is joining Cognition to work on Devin's VMs, computer use and testing (AINews, 2026-09-12).
