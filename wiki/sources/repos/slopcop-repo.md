---
title: slopcop — CLI tool against LLM-hallucinated malicious packages
type: source
source_type: repo
source_file: raw/repos/larsencundric-slopcop.md
url: https://github.com/LarsenCundric/slopcop
published: 2026-04-22
ingested: 2026-04-22
domains: [coding, agents, cybersecurity]
---

# slopcop

CLI tool that checks npm/PyPI packages for slopsquatting signals before installation. Built by Larsen Cundric. Cites USENIX Security 2025 study as evidence base (19.7% hallucination rate across 576,000 code-generation samples).

Secondary source: Basel Ismail's PSA tweet (`raw/tweets/2026-04-22-baselismail-2039677597311996389.md`) popularized the attack concept.

## Influenced pages

- [Slopsquatting](../../concepts/slopsquatting.md) — new page created
- [State of Cybersecurity](../../state-of/cybersecurity.md) — new page created with `AI-specific attack surfaces` section

## Key claims extracted

- 19.7% of LLM package recommendations reference non-existent packages (USENIX 2025)
- Slopsquatting: attackers register hallucinated names on PyPI/npm with malicious postinstall scripts
- slopcop checks: registry age, download count, postinstall presence, Levenshtein distance, repo match
- Node.js 18+; no native dependencies; macOS/Linux/Windows
