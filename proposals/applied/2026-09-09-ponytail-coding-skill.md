---
type: proposal
source: raw/repos/dietrichgebert-ponytail.md
status: pending
created: 2026-09-09
---

# Proposal: Ponytail, a cross-agent minimal-code skill with a real agentic benchmark

## Summary

### The source

Ponytail is an open-source (MIT) plugin/skill package built around one idea: make a coding agent stop reaching for the fifty-line solution when a one-liner does the job, without ever cutting validation, error handling, security, or accessibility to get there. Its mechanism is a priority ladder the agent walks through before writing anything: does this need to exist at all (YAGNI)? Is it already in the codebase? Does the standard library do it? Does a native platform feature do it? Is it an installed dependency? Can it be one line? Only after exhausting those does it write the minimum that actually works — and the ladder runs after the agent understands the problem and traces the real code paths it touches, not instead of understanding it. What sets Ponytail apart from the many "write less code" prompts already circulating is that it ships a real agentic benchmark rather than a marketing claim: a headless Claude Code session (Haiku 4.5, n=4) doing twelve real feature tickets against tiangolo's full-stack-fastapi-template (a genuine FastAPI + React repo), scored on the actual git diff it leaves behind, compared against a no-skill baseline and two other arms (a "caveman" terse-prose control, and a bare "YAGNI + one-liners" prompt). Ponytail is the only arm that cut every measured metric versus the no-skill baseline — 54% fewer lines of code (mean; up to 94% where the baseline agent over-built, like a date picker), 22% fewer tokens, 20% lower cost, 27% less time — while holding 100% on a separate safety/adversarial tier, the same score as the baseline; the "YAGNI + one-liners" prompt cut more tokens/cost/time in isolation but dropped to 95% safety, and the terse-prose control actually rose above the baseline on tokens, cost, and time. The project is unusually candid about its own evidence: an earlier single-shot benchmark reported an 80-94% code reduction, and after a GitHub issue pointed out the bare-model baseline in that test padded its answers with prose and options (a conversational-baseline artifact, not a fair comparison), the maintainer published the corrected agentic numbers above as the "defensible version" rather than quietly dropping the old claim. Ponytail installs as a native plugin across at least a dozen agent hosts — Claude Code, Codex, Copilot CLI, Gemini/Antigravity, OpenCode, Grok Build, Devin, Hermes Agent, Qoder, and more — or works instruction-only via `AGENTS.md` on hosts without a plugin system.

### What changes

The wiki has no page for this kind of tool yet, and no subcategory that quite fits it either — the closest existing one, `agent-toolkits`, is specifically for toolkits that package a *specific developer platform's* docs/schemas/validation (its example is the Shopify AI Toolkit), whereas Ponytail packages a portable coding-discipline ruleset with no platform-specific docs, installed identically across a dozen unrelated agent hosts.

- New subcategory `coding-discipline-skill`, proposed below, to house this and future tools like it without stretching `agent-toolkits`' definition.
- New page `wiki/tools/ponytail.md`: the priority-ladder mechanism, the full agentic-benchmark table, and the self-corrected single-shot-vs-agentic distinction.
- One new source page for the GitHub repo.

### What to weigh

The benchmark is vendor-run (the tool's own maintainer, on their own chosen repo and task set) with a small sample (n=4, twelve tasks, one model family) — a real agentic methodology and unusually transparent about its own prior mistake, but not an independently reproduced result. The new subcategory is a genuine judgment call: `agent-toolkits` was close enough to consider stretching instead of adding a new slug — flagged for explicit approval rather than assumed.

## Intended changes

- [x] **Approve all**

- [ ] **Create** `wiki/tools/ponytail.md` — new tool page
    > See draft below

- [ ] **Create** `wiki/sources/repos/dietrichgebert-ponytail.md` — source summary

## Page drafts

### wiki/tools/ponytail.md (new)

````md
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
````

### wiki/sources/repos/dietrichgebert-ponytail.md (new)

```md
---
title: "DietrichGebert/ponytail: Makes your AI agent think like the laziest senior dev in the room"
type: source
source_type: repo
source_file: raw/repos/dietrichgebert-ponytail.md
url: https://github.com/DietrichGebert/ponytail
ingested: 2026-09-09
domains: [coding, agents]
---

# DietrichGebert/ponytail

Open-source (MIT) cross-agent coding-discipline skill: a priority ladder (YAGNI → reuse → stdlib → native feature → dependency → one line → minimum needed) applied after the agent understands the problem. Ships an agentic benchmark (Claude Code, Haiku 4.5, 12 real FastAPI+React feature tasks) showing -54% LOC / -22% tokens / -20% cost / -27% time vs. no-skill baseline at 100% safety, and openly corrects an earlier, weaker single-shot benchmark methodology.

## Influenced pages

- [Ponytail](../../tools/ponytail.md) — new page

## Key claims extracted

- Agentic benchmark: -54% LOC (up to -94%), -22% tokens, -20% cost, -27% time, 100% safety tier, vs. no-skill baseline
- Only tested arm (of three) to cut every metric while staying fully safe
- Installs across 12+ agent hosts via native plugin or AGENTS.md
- Corrected an earlier single-shot benchmark (80-94% claimed) after a baseline-fairness critique
```

## Schema / vocabulary additions

- [ ] Add new subcategory `coding-discipline-skill` to `wiki/_schema/subcategories.md`:
    - **Parent domain(s):** coding, agents
    - **Applies to types:** tool
    - **Definition:** Portable skill/rule packages that inject a coding discipline or behavioral ruleset into AI coding agents across multiple unrelated hosts (Claude Code, Codex, Copilot, Gemini, etc.) via plugins, hooks, or `AGENTS.md`-style instruction files — distinct from `agent-toolkits`, which packages a *specific developer platform's* docs, schemas, and validation rather than a general behavioral discipline.
    - **Examples:** [Ponytail](../tools/ponytail.md)

## Open questions

- Should `coding-discipline-skill` be approved as proposed, or is stretching `agent-toolkits`' definition to cover this preferable? Flagged as a genuine judgment call in "What to weigh" above.
