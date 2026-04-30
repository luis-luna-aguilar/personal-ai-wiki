---
title: Slopsquatting
type: concept
domains: [coding, agents, cybersecurity]
tags: [open-source]
as_of: 2026-04-22
sources: [slopcop-repo]
---

# Slopsquatting

A supply-chain attack where adversaries pre-register package names that AI coding assistants are known to hallucinate, loading them with malicious payloads. Named by analogy with typosquatting, but the attack surface is LLM hallucination rather than human typos.

## Current status (as of 2026-04-22)

- USENIX Security 2025 study: **19.7%** of LLM package recommendations reference non-existent packages across 576,000 code-generation samples
- Attack pattern confirmed active on PyPI and npm: attackers monitor LLM outputs, identify repeatedly hallucinated names, and register them before developers notice
- Payloads typically run arbitrary code via `postinstall` scripts — before the developer opens an editor
- The packages look plausible, install cleanly, and pass cursory review

## Why it matters

The 19.7% base rate means roughly 1 in 5 AI-suggested package names may not exist — and some of the gaps have been filled with malware. Anyone using Claude Code, Codex, Cursor, or any LLM to help write code is in the target window.

## Mitigation: slopcop

`slopcop` is a CLI tool (Node.js 18+) that intercepts this kill chain by checking a package before anything installs.

```bash
npm install -g slopcop
slopcop check <package-name>
```

Checks performed: registry publication age, lifetime download count, presence of `postinstall` scripts, Levenshtein distance from popular packages, missing or mismatched repository links.

## Caveats

- USENIX study scope: 576,000 samples, but model mix and task type affect the hallucination rate
- `slopcop` heuristics are signals, not guarantees — a well-aged, high-download slopsquat package would pass
- Attack is asymmetric: registering a hallucinated name is trivial; defending requires per-install vigilance

## Sources

- [slopcop — CLI tool against LLM-hallucinated malicious packages](../sources/repos/slopcop-repo.md)
