---
type: proposal
sources:
  - raw/repos/larsencundric-slopcop.md
  - raw/tweets/2026-04-22-baselismail-2039677597311996389.md
  - raw/tweets/2026-04-22-larsencc-2040165623737770378.md
status: pending
created: 2026-04-22
---

# Proposal: Slopsquatting + slopcop — LLM hallucinated packages as supply chain attack

## Summary

A USENIX Security 2025 study found 19.7% of LLM package recommendations reference non-existent packages. Attackers are pre-registering these hallucinated names on PyPI/npm with malware payloads. `slopcop` is a CLI tool that checks packages before installation. This is a new, empirically-grounded security concept worth capturing in the wiki.

## Intended changes

- [x] **Create** `wiki/concepts/slopsquatting.md` — new concept page
    > See draft below

- [x] **Update** `wiki/state-of/coding.md` — add a security note to the `Terminal coding agent` subcategory
    > **Add new `### AI coding security` section after `### Agent toolkits`:**
    > ```markdown
    > ### AI coding security
    >
    > A surface-specific risk layer emerging as coding agents become standard. See [[concepts/slopsquatting]] for the most-documented current attack vector.
    >
    > - **Slopsquatting** — LLMs hallucinate ~20% of package names; attackers pre-register them with malware. Tool: [[tools/slopcop-cli]] or the `slopcop` npm package. *(as of 2026-04-22)*
    > ```
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added `AI coding security` subcategory; slopsquatting documented with USENIX 2025 evidence and slopcop mitigation tool
    > ```
    > **Update `as_of: 2026-04-22`.**

- [x] **Create** `wiki/sources/repos/slopcop.md` — source summary
    > See draft below

## Page drafts

### wiki/concepts/slopsquatting.md (new)

```md
---
title: Slopsquatting
type: concept
domains: [coding, agents]
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

This is not hypothetical. The 19.7% base rate means roughly 1 in 5 AI-suggested package names may not exist — and some of the gaps have been filled with malware. Anyone using Claude Code, Codex, Cursor, or any LLM to help write code is in the target window.

## Mitigation: slopcop

`slopcop` is a CLI tool (Node.js 18+) that intercepts this kill chain by checking a package before anything installs. Checks performed:

- Registry publication age (newly registered = suspicious)
- Lifetime download count (low downloads = suspicious)
- Presence of `postinstall` scripts (which run arbitrary code)
- Levenshtein distance from popular packages (detects name-squatting)
- Missing or mismatched repository links

```bash
npm install -g slopcop
slopcop check <package-name>
```

## Caveats

- USENIX study scope: 576,000 samples, but model mix and task type affect the hallucination rate
- `slopcop` heuristics are signals, not guarantees — a well-aged, high-download slopsquat package would pass
- Attack is asymmetric: registering a hallucinated name is trivial; defending requires per-install vigilance

## Sources

- [[sources/repos/slopcop-repo]]
```

### wiki/sources/repos/slopcop.md (new)

```md
---
title: slopcop — CLI tool against LLM-hallucinated malicious packages
type: source
source_type: repo
source_file: raw/repos/larsencundric-slopcop.md
url: https://github.com/LarsenCundric/slopcop
published: 2026-04-22
ingested: 2026-04-22
domains: [coding, agents]
---

# slopcop

CLI tool that checks npm/PyPI packages for slopsquatting signals before installation. Built by Larsen Cundric. Cites USENIX Security 2025 study as evidence base (19.7% hallucination rate across 576,000 code-generation samples).

Secondary source: Basel Ismail's PSA tweet (`raw/tweets/2026-04-22-baselismail-2039677597311996389.md`) popularized the attack concept.

## Influenced pages

- [[concepts/slopsquatting]] — new page created
- [[state-of/coding]] — new `AI coding security` subcategory added

## Key claims extracted

- 19.7% of LLM package recommendations reference non-existent packages (USENIX 2025)
- Slopsquatting: attackers register hallucinated names on PyPI/npm with malicious postinstall scripts
- slopcop checks: registry age, download count, postinstall presence, Levenshtein distance, repo match
- Node.js 18+; no native dependencies; macOS/Linux/Windows
```

## Schema / vocabulary additions

None required. The concept page doesn't need a subcategory (concepts don't require it). The state-of section note is informal.

## Open questions

- The state-of/coding update adds an `### AI coding security` section. This is an informal grouping within a state-of page, not a formal subcategory. No schema change needed. Confirm?
	- lets add a subcategory for security and a state of cybersecurity separate from coding. move there stuff in state of coding that is related to cyber.
