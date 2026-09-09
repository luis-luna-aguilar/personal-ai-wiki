---
type: proposal
source: raw/tweets/2026-09-07-primeintellect-2085086999267144083.md
status: pending
created: 2026-09-08
---

# Proposal: Prime Intellect open-sources Prime Agent

## Summary

### The source

Prime Intellect launched **Prime Agent**, an open-source, general-purpose coding/agentic harness built on their "pi" framework, combining three ideas the launch thread names explicitly: Recursive-Language-Model-native programmatic tool calling, where a persistent IPython kernel is the model's only tool — letting it program over its own history, call tools, and launch sub-agents, treating long sessions as a programming problem rather than a context-window problem; persistent multi-agent orchestration; and a self-modifiable "Continual Harness," where the harness can rewrite its own state rather than staying fixed. Reported results: 95.5% on ARC-AGI-3, above the human-expert baseline the thread cites, with the gain described as not benchmark-specific — Prime Intellect reports "major improvements" across models compared to their existing proprietary harnesses. On EmulatorBench, it built working SEGA Genesis and Game Boy Color emulators from scratch in Rust, reproducing target hardware behavior against diagnostic tests. Prime Intellect frames it as usable for both day-to-day coding work and standalone evals, and beyond coding for general long-horizon agentic tasks (cited examples: Factorio, MazeBench). The repository and installer are public.

### What changes

`concepts/harness.md` already catalogs several open-source, self-modifying, or novel-framing harnesses (Headlong, exo, DeepSeek Harness/Cordis). This proposal adds Prime Agent as a new bullet in the same list, bumps `as_of` to 2026-08-05 (the source's own tweet date), and adds a Recent-changes entry — spilling the page's oldest entry, since three proposals in this batch each independently add one entry to an already-full 10-entry cap.

### What to weigh

All of the benchmark numbers here (95.5% ARC-AGI-3, the EmulatorBench results) are Prime Intellect's own self-reported figures from its launch thread, not independently verified — consistent with how most vendor-launch content is already flagged elsewhere on this page.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/harness.md` — add Prime Agent bullet, bump `as_of`, add Recent-changes entry, spill oldest entry
    > See draft below

- [ ] **Spill** `wiki/concepts/harness.md` → `wiki/history/concepts/harness.md` — oldest Recent-changes entry falls off the 10-entry cap (whichever is oldest at apply time)
    > See draft below

- [ ] **Create** `wiki/sources/tweets/primeintellect-prime-agent-2026-08-05.md` — source summary

## Page drafts

### wiki/concepts/harness.md (updated)

```md
---
as_of: 2026-08-05
sources: [..., primeintellect-prime-agent-2026-08-05]
---

## What good harness engineering looks like

(... existing bullets unchanged ...)

- **Prime Agent: context as a variable, self-modifiable harness.** Prime Intellect's open-source Prime Agent (built on "pi") combines Recursive-Language-Model-native programmatic tool calling — a persistent IPython kernel as the model's only tool, letting it program over its own history and launch sub-agents, treating long sessions as a programming problem rather than a context-window problem — with persistent multi-agent orchestration and a self-modifiable "Continual Harness." Reported (vendor-claimed, self-reported): 95.5% on ARC-AGI-3, above the cited human-expert baseline, with gains described as not benchmark-specific; on EmulatorBench it built working SEGA Genesis and Game Boy Color emulators from scratch in Rust.

## Recent changes

- [2026-08-05] Added Prime Intellect's open-source Prime Agent: RLM-native programmatic tool calling (context as a variable), persistent multi-agent orchestration, self-modifiable Continual Harness; reported 95.5% ARC-AGI-3 (vendor-claimed).
- (... existing entries follow, oldest entry spilled below ...)
```

### wiki/history/concepts/harness.md (updated)

```md
## Archived from current page on 2026-09-08

- (whichever Recent-changes entry is oldest on the live page at apply time)
```

### wiki/sources/tweets/primeintellect-prime-agent-2026-08-05.md (new)

```md
---
title: "Prime Intellect on X: \"Introducing Prime Agent: A self-improving RLM harness\""
type: source
source_type: tweet
source_file: raw/tweets/2026-09-07-primeintellect-2085086999267144083.md
url: https://x.com/primeintellect/status/2085086999267144083?s=12
published: 2026-08-05
ingested: 2026-09-08
domains: [agents]
---

# Prime Intellect — Introducing Prime Agent

Launch thread for Prime Agent, an open-source RLM-native, self-modifiable coding/agentic harness reporting 95.5% on ARC-AGI-3 and working SEGA Genesis/Game Boy Color emulators built from scratch on EmulatorBench.

## Influenced pages

- [Harness (agent)](../../concepts/harness.md) — Prime Agent bullet

## Key claims extracted

- Combines RLM-native programmatic tool calling, persistent multi-agent orchestration, and a self-modifiable Continual Harness
- 95.5% on ARC-AGI-3 (vendor-claimed), above cited human-expert baseline
- Built working SEGA Genesis and Game Boy Color emulators from scratch in Rust on EmulatorBench
- Open-source, built on "pi"; public repo and installer
```
