---
type: proposal
source:
  - raw/newsletters/2026-05-29-ainews-anthropic-raises-965b-series-h-releases.md
  - raw/newsletters/2026-05-28-vibe-check-opus-48anthropic-shouldve-rounded-u.md
  - raw/newsletters/2026-06-18-how-anthropic-makes-claude-more-reliable.md
  - raw/tweets/2026-07-08-claudedevs-2067391951725629941.md
status: pending
created: 2026-07-08
---

# Proposal: Opus 4.8 benchmarks and Dynamic Workflows

## Summary

The approved signals refine the existing Claude Opus 4.8 and Claude Code pages rather than creating a new topic. The main update is to add stronger benchmark/economics detail for Opus 4.8 and to connect Dynamic Workflows to practical Figma/design-sync and reviewer-agent use cases.

## Intended changes

- [ ] **Update** `wiki/models/claude-opus-4-8.md` - add benchmark, pricing, efficiency, and calibration detail from AINews and Every.
- [ ] **Update** `wiki/state-of/models.md` - sharpen the Claude Opus 4.8 frontier-model line with accessible-flagship benchmark context.
- [ ] **Update** `wiki/tools/claude-code.md` - add June 18 dynamic-workflow reliability case studies and July 8 Claude Design sync.
- [ ] **Update** `wiki/tools/claude-design.md` - add bidirectional Claude Code / Claude Design sync note.
- [ ] **Update** `wiki/workflows/agentic-orchestration-patterns.md` - add Dynamic Workflows as productized orchestration evidence.
- [ ] **Create** `wiki/sources/newsletters/ainews-opus-48-dynamic-workflows-2026-05.md` - source summary.
- [ ] **Create** `wiki/sources/newsletters/every-claude-dynamic-workflows-reliability-2026-06.md` - source summary.
- [ ] **Create** `wiki/sources/tweets/claude-code-design-sync-2026-07.md` - source summary.

## Page drafts

### wiki/models/claude-opus-4-8.md (updated sections)

```md
---
title: Claude Opus 4.8
type: model
domains: [models]
subcategory: frontier-model
tags: [anthropic, closed-source]
as_of: 2026-05-29
sources: [every-opus-48-june-2026, vending-bench-andon-june-2026, ainews-opus-48-dynamic-workflows-2026-05]
---

## Current status (as of 2026-05-29)

- Released alongside **Dynamic Workflows** (the `ultracode` agent orchestration pattern)
- Reported 1M-token context; AINews cites Artificial Analysis pricing of $5 / $25 per million input / output tokens, cache writes at $6.25/M, and cache hits at $0.50/M
- Reported benchmarks: SWE-Bench Pro 69.2%, APEX-SWE 45.3% Pass@1, GDPval-AA 1890 Elo, AA Intelligence Index 61.4, plus gains on Terminal-Bench Hard and telecom τ²-Bench
- Efficiency nuance: AINews reports higher GDPval performance with 15% fewer turns and 35% fewer output tokens than Opus 4.7, but still about 30% more turns than GPT-5.5 in the same analysis
- Practitioner split: Every found strong senior-engineer and writing-test results, but also notes that model quality depends heavily on the surrounding product surface and harness
- Caveat: still slower and higher-token than some GPT-5.5/Codex workflows for straightforward tasks

## Recent changes

- [2026-05-29] AINews launch coverage adds benchmark, pricing, efficiency, and calibration detail for Opus 4.8; Dynamic Workflows launched in Claude Code at the same time.
- [2026-06-04] Vending Bench / Andon Labs finding added as a model-behavior caveat for the Claude 4.6+ line.
- [2026-06-03] Released; Dynamic Workflows and Figma MCP at launch; early practitioner pulse check by Every.

## Sources

- [AINews - Anthropic raises Series H, releases Opus 4.8 and Dynamic Workflows](../sources/newsletters/ainews-opus-48-dynamic-workflows-2026-05.md)
- [Every - Claude Opus 4.8 pulse check (June 3)](../sources/newsletters/every-opus-48-june-2026.md)
- [Andon Labs / Vending Bench (June 4)](../sources/newsletters/vending-bench-andon-june-2026.md)
```

### wiki/state-of/models.md (updated sections)

```md
---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-05-29
sources: [..., ainews-opus-48-dynamic-workflows-2026-05]
---

### Frontier models

- [Claude Opus 4.8](../models/claude-opus-4-8.md) - Anthropic's current accessible flagship after 4.7; AINews cites 1M context, SWE-Bench Pro 69.2%, APEX-SWE 45.3% Pass@1, GDPval-AA 1890 Elo, and Dynamic Workflows in Claude Code; stronger than 4.7 but still cost/turn-count sensitive vs GPT-5.5 in some workloads *(as of 2026-05-29)*

## Recent changes

- [2026-05-29] Opus 4.8 launch coverage adds benchmark/pricing detail and positions Dynamic Workflows as the companion Claude Code systems feature.
```

### wiki/tools/claude-code.md (updated sections)

```md
---
title: Claude Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-07-08
sources: [..., ainews-opus-48-dynamic-workflows-2026-05, every-claude-dynamic-workflows-reliability-2026-06, claude-code-design-sync-2026-07]
---

## Dynamic workflows

Add to this section:

- **Reliability pattern:** Every's June 18 case study frames Dynamic Workflows as the productized version of manually coordinating a lead agent plus reviewer subagents through local files. Instead of hoping a prompt will reliably create multiple reviewers, Claude writes an orchestration script that instantiates the subagents and verification steps each time.
- **Design-to-code use case:** Every describes using Dynamic Workflows to split a large Figma redesign into 11 sections, assign dedicated subagents, extract assets/details, generate code, and compare outputs to the source design.
- **Claude Design sync:** Claude Code and Claude Design now sync both directions through `/design-sync`: pull a design system into the repo, build against existing components, or push built work back into a Claude Design canvas.

## Recent changes

- [2026-07-08] Claude Code and Claude Design add bidirectional `/design-sync` between repo work and Claude Design canvases.
- [2026-06-18] Every case studies show Dynamic Workflows replacing manual subagent coordination for reviewer agents and large Figma-to-code work.
- [2026-05-28] Dynamic workflows added (research preview): the `ultracode` effort setting (xhigh) lets Claude write orchestration scripts running tens-to-hundreds of parallel subagents that plan, verify, and iterate to convergence.

## Sources

- [AINews - Anthropic raises Series H, releases Opus 4.8 and Dynamic Workflows](../sources/newsletters/ainews-opus-48-dynamic-workflows-2026-05.md)
- [Every - How Anthropic makes Claude more reliable](../sources/newsletters/every-claude-dynamic-workflows-reliability-2026-06.md)
- [Claude Code and Claude Design sync](../sources/tweets/claude-code-design-sync-2026-07.md)
```

### wiki/tools/claude-design.md (updated sections)

```md
---
as_of: 2026-07-08
sources: [..., claude-code-design-sync-2026-07]
---

## Current status (as of 2026-07-08)

- Claude Design now syncs with Claude Code in both directions through `/design-sync`: design systems can be pulled into a repo for implementation work, and built work can be pushed back into the Claude Design canvas.

## Recent changes

- [2026-07-08] Claude Code / Claude Design bidirectional sync announced through `/design-sync`.
```

### wiki/workflows/agentic-orchestration-patterns.md (updated sections)

```md
---
as_of: 2026-06-18
sources: [..., every-claude-dynamic-workflows-reliability-2026-06]
---

## Current patterns

- **Scripted subagent orchestration.** Dynamic Workflows show an emerging product pattern: the model writes a reusable orchestration script for a large task, then uses that script to create worker and reviewer subagents consistently. This is more reliable than relying on prompt pressure to make the model remember to spawn separate verifiers.

## Recent changes

- [2026-06-18] Every case studies add scripted-subagent orchestration as a practical Dynamic Workflows reliability pattern.
```

### wiki/sources/newsletters/ainews-opus-48-dynamic-workflows-2026-05.md (new)

```md
---
title: "AINews - Anthropic raises Series H, releases Opus 4.8 and Dynamic Workflows"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-29-ainews-anthropic-raises-965b-series-h-releases.md
url: https://www.latent.space/p/ainews-anthropic-raises-965b-series
published: 2026-05-29
ingested: 2026-07-08
domains: [models, coding, agents]
---

# AINews - Anthropic raises Series H, releases Opus 4.8 and Dynamic Workflows

AINews summarizes Anthropic's Opus 4.8 launch, benchmark/pricing reactions, and the accompanying Claude Code Dynamic Workflows feature. The coverage emphasizes that 4.8 improves over 4.7 on long-horizon coding, benchmark scores, efficiency, and calibration, while still carrying token/turn-count caveats against GPT-5.5 in some workflows.

## Influenced pages

- [Claude Opus 4.8](../../models/claude-opus-4-8.md) - benchmark, pricing, efficiency, and calibration update
- [State of Models](../../state-of/models.md) - frontier-model line update
- [Claude Code](../../tools/claude-code.md) - Dynamic Workflows launch detail

## Key claims extracted

- Opus 4.8 launched as an Opus 4.7 update with improved judgment, honesty, and longer autonomous work.
- AINews cites 1M context, $5/$25 per million input/output tokens, SWE-Bench Pro 69.2%, APEX-SWE 45.3% Pass@1, and GDPval-AA 1890 Elo.
- Dynamic Workflows let Claude Code write orchestration scripts and run large fleets of subagents for long-running work.
```

### wiki/sources/newsletters/every-claude-dynamic-workflows-reliability-2026-06.md (new)

```md
---
title: Every - How Anthropic makes Claude more reliable
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-18-how-anthropic-makes-claude-more-reliable.md
url: https://every.to/context-window/how-anthropic-makes-claude-more-reliable
published: 2026-06-18
ingested: 2026-07-08
domains: [coding, agents]
---

# Every - How Anthropic makes Claude more reliable

Every describes Dynamic Workflows as a reliability improvement for multi-agent Claude Code work. The piece compares the feature with earlier hand-rolled orchestrator/subagent setups and gives a design-to-code case study where a large Figma file was split into sections for parallel extraction, implementation, and verification.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) - practical Dynamic Workflows use cases
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) - scripted subagent orchestration pattern

## Key claims extracted

- Claude can write a workflow script that reliably creates multiple verifier subagents.
- Dynamic Workflows were used to process an 11-section Figma redesign with dedicated subagents.
- The feature replaces fragile prompt-only coordination for some large tasks.
```

### wiki/sources/tweets/claude-code-design-sync-2026-07.md (new)

```md
---
title: Claude Code and Claude Design sync
type: source
source_type: tweet
source_file: raw/tweets/2026-07-08-claudedevs-2067391951725629941.md
url: https://x.com/claudedevs/status/2067391951725629941
published: 2026-06-18
ingested: 2026-07-08
domains: [coding, creative]
---

# Claude Code and Claude Design sync

Claude Devs announced bidirectional sync between Claude Code and Claude Design. The `/design-sync` workflow can pull a design system into a repository, help build against existing components, or push implemented work back into a Claude Design canvas.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) - design-code workflow update
- [Claude Design](../../tools/claude-design.md) - bidirectional repo/canvas sync update

## Key claims extracted

- Claude Code and Claude Design can sync both directions.
- `/design-sync` can bring design-system context into code work.
- Built work can be pushed back into Claude Design.
```

## Open questions

- The Opus 4.8 source dates precede the current 2026-07-02 model dashboard state. Should the Opus line be updated only with benchmark detail, or should it stay visually secondary to newer Fable/Sonnet 5 entries?
