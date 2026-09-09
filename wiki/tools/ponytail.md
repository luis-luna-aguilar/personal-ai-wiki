---
title: Ponytail
type: tool
domains: [coding, agents]
subcategory: coding-discipline-skill
tags: [open-source, agentic]
as_of: 2026-09-09
sources: [dietrichgebert-ponytail]
---

# Ponytail

An open-source (MIT) plugin/skill that injects a "write only what the task needs" discipline into coding agents across a dozen-plus hosts, without cutting validation, error handling, security, or accessibility. Before writing code, the agent walks a priority ladder: does this need to exist (YAGNI)? Already in the codebase? Stdlib? Native platform feature? Installed dependency? One line? Only then, the minimum that works — applied after the agent has read the touched code and traced the real flow, never instead of understanding it.

## Current status (as of 2026-09-09)

- Agentic benchmark (Haiku 4.5, n=4, 12 real feature tickets against a real FastAPI+React repo, scored on actual git diff): -54% LOC (mean; up to -94% on over-build-prone tasks like a date picker), -22% tokens, -20% cost, -27% time vs. a no-skill baseline, while holding 100% on a separate safety/adversarial tier — the only one of three tested arms (a terse-prose control, a bare "YAGNI + one-liners" prompt, and Ponytail) that cut every metric while staying fully safe
- Installs as a native plugin on Claude Code, Codex, Copilot CLI, Gemini/Antigravity, OpenCode, Grok Build, Devin, Hermes Agent, Qoder, and more; works instruction-only via `AGENTS.md` on hosts without a plugin system
- Injects into subagents spawned via the Agent tool by default; scopable to specific agent types via an environment variable matcher
- Ships four intensity levels (`lite`/`full`/`ultra`/`off`) plus review/audit/debt/gain/help commands (e.g. `/ponytail-review` hands back a delete-list for the current diff)
- Openly corrected its own earlier single-shot benchmark (originally reported 80-94% code reduction) after a GitHub issue showed the bare-model baseline padded its answers with prose — the agentic numbers above are the maintainer's published "defensible version"

## Why it matters

Most "write less code" prompts ship as unverified claims. Ponytail is unusual for shipping a reproducible agentic (not single-shot) benchmark methodology, and for publishing a corrected, weaker result after public critique rather than quietly dropping the original number.

## Weaknesses / caveats

- Vendor-run benchmark: the maintainer's own repo/task selection, small sample (n=4, one model family)
- Not independently reproduced yet

## Recent changes

- [2026-09-09] Page created: agentic benchmark results, cross-host plugin install, self-corrected single-shot claim.

## Sources

- [DietrichGebert/ponytail — GitHub](../sources/repos/dietrichgebert-ponytail.md)
