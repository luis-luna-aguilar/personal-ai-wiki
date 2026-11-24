---
title: trycua/cua GitHub README
type: source
source_type: repo
source_file: raw/repos/trycua-cua.md
url: https://github.com/trycua/cua
ingested: 2026-11-24
domains: [computer-use, agents]
---

# trycua/cua GitHub README

The monorepo for Cua's computer-use stack: Cua Spaces (desktop app giving agents full macOS/Linux desktops), Cua Driver (background control of native apps on macOS, Windows and Linux), the `cua` SDK and CLI (Python, TypeScript, Rust), Lume (Apple-silicon VMs), cua-bench, and the CUA-S1 decision models. Fetched 2026-11-23 at Cua Spaces 0.9.4; the README carries no publication date.

## Influenced pages
- [Cua](../../tools/cua.md) — new tool page
- [State of Computer Use](../../state-of/computer-use.md) — Cua leader line
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — Spaces as a self-hosted agent runtime
- [Decision models](../../concepts/decision-models.md) — CUA-S1-FORMS

## Key claims extracted
- Spaces run locally on a Mac, on other computers the user owns, or in their own AWS, Google Cloud or Modal account; signed-in apps can be teleported in; people and agents share a desktop with separate cursors.
- Pricing: free for individuals; Pro $18/month; Teams $30/seat/month.
- Licensing: Spaces is FSL-1.1-MIT (MIT two years after each release); the rest of the repo is MIT.
- CUA-S1 is a family of small "System 1" models for bounded computer-use decisions; CUA-S1-FORMS scores form decisions from structured UI elements and document values; application code orders actions and Cua Driver executes them.
- CUA-S1 is an early, source-only research release; weights and a synthetic dataset are on Hugging Face.
- Several older packages are deprecated; `cuabot` has known security issues and should be uninstalled.
