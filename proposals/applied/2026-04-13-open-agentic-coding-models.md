---
type: proposal
source: internal — synthesized from raw/newsletters/2026-04-13-minimax-drops-open-weight-coding-model.md, raw/newsletters/2026-04-14-ainews-top-local-models-list-april-2026.md, raw/newsletters/2026-04-08-ainews-meta-superintelligence-labs-announces-mus.md
status: pending
created: 2026-04-13
---

# Proposal: Open agentic coding models

## Summary

The wiki's coding-model section currently tracks Qwen 3.6 and Kimi K2.6, but this earlier digest contains two important missing open-model signals: GLM-5.1 as an open-model benchmark contender and MiniMax M2.7 as an open-weight coding model paired with a CLI designed for tool-heavy use.

This is the one signal in the digest that most clearly still looks underrepresented in the current wiki.

## Intended changes

- [x] **Create** `wiki/models/glm-5-1.md` — model page for GLM-5.1 as an open coding/agent model contender
  > See full draft below.

- [x] **Create** `wiki/models/minimax-m2-7.md` — model page for MiniMax M2.7
  > See full draft below.

- [x] **Update** `wiki/state-of/models.md` — expand the `Coding models` subcategory with GLM-5.1 and MiniMax M2.7
  > See diff snippet below.

- [x] **Update** `wiki/index.md` — add the two new model pages and refresh counts
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/open-agentic-coding-models.md` — source summary page
  > See full draft below.

## Page drafts

### wiki/models/glm-5-1.md (new)

```markdown
---
title: GLM-5.1
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-04-08
sources: [open-agentic-coding-models]
---

# GLM-5.1

GLM-5.1 is an open-weight model positioned as a frontier open contender for coding and agentic engineering work. The captured source set emphasizes benchmark placement and ecosystem support rather than detailed product documentation.

## Current status (as of 2026-04-08)

- Positioned as a large open model for coding and tool-using workloads
- AINews summarizes it as a top open contender on SWE-Bench Pro and related agent/coding leaderboards
- The surrounding ecosystem discussion emphasizes fast follow-through in serving and local/open tooling support

## Strengths

- Strong benchmark/leaderboard positioning in the captured source set
- Reinforces that open models are now competing on agentic coding tasks, not just chat quality

## Weaknesses / caveats

- Current source coverage is newsletter-level, not a full technical release write-up
- Model size, serving constraints, and practical deployment details are thin in the saved sources

## Recent changes

- [2026-04-08] Page created from digest synthesis covering GLM-5.1's emergence as an open coding-model contender

## Sources

- [[sources/newsletters/open-agentic-coding-models]]
```

### wiki/models/minimax-m2-7.md (new)

```markdown
---
title: MiniMax M2.7
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-04-13
sources: [open-agentic-coding-models]
---

# MiniMax M2.7

MiniMax M2.7 is an open-weight coding model positioned for agentic engineering workloads. In the captured source set, its significance comes from the combination of credible coding-benchmark claims and an accompanying CLI that reduces setup friction for tool-heavy use.

## Current status (as of 2026-04-13)

- Open-weight coding model released on Hugging Face
- Source claims benchmark competitiveness on SWE-Pro and Terminal Bench 2
- Released alongside MMX-CLI, which is framed as providing native tool access without MCP setup

## Strengths

- Couples the model with an execution surface rather than shipping weights alone
- Reinforces the trend that open coding stacks are becoming more usable for practical agent workflows

## Weaknesses / caveats

- Benchmark claims are relayed through newsletter coverage in the captured source set
- Hardware and licensing details in the source set are incomplete and should be treated cautiously

## Recent changes

- [2026-04-13] Page created from digest synthesis covering M2.7's open-weight release and MMX-CLI pairing

## Sources

- [[sources/newsletters/open-agentic-coding-models]]
```

### wiki/state-of/models.md (updated snippet)

```markdown
### Coding models

- [[models/kimi-k2-6]] — ...
- [[models/qwen-3-6-35b-a3b]] — ...
- [[models/glm-5-1]] — open-weight contender described in the captured sources as a top benchmark performer for coding and agent workflows *(as of 2026-04-08)*
- [[models/minimax-m2-7]] — open-weight coding model paired with MMX-CLI; notable because the stack is pitched as runnable/usable, not just benchmarked *(as of 2026-04-13)*

## Recent changes

- [2026-04-13] Added [[models/minimax-m2-7]] and [[models/glm-5-1]] under `Coding models`; earlier April sources show open coding-model momentum was broader than the later Qwen/Kimi cluster alone
```

### wiki/sources/newsletters/open-agentic-coding-models.md (new)

```markdown
---
title: Open agentic coding models
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-13-minimax-drops-open-weight-coding-model.md
ingested: 2026-04-13
domains: [models, coding]
---

# Open agentic coding models

This source summary groups the earlier-April open-model cluster around GLM-5.1 and MiniMax M2.7. The durable signal is that open and open-weight models are increasingly being evaluated as real agentic coding components rather than hobbyist alternatives.

## Influenced pages

- [[models/glm-5-1]]
- [[models/minimax-m2-7]]
- [[state-of/models]]

## Key claims extracted

- GLM-5.1 is framed as a frontier open contender for coding and agent workflows
- MiniMax M2.7 is framed as an open-weight coding model with meaningful benchmark competitiveness
- MMX-CLI matters because it lowers tool-use friction around the model instead of shipping weights alone
```

### wiki/index.md (updated snippet)

```markdown
## Models

- [[models/claude-opus-4-7]] — ...
- [[models/composer-2]] — ...
- [[models/glm-5-1]] — open-weight coding/agent model contender from the early-April open-model wave *(as_of: 2026-04-08)*
- [[models/kimi-k2-6]] — ...
- [[models/minimax-m2-7]] — open-weight coding model paired with MMX-CLI for tool-heavy workflows *(as_of: 2026-04-13)*
- [[models/muse-spark]] — ...
- [[models/qwen-3-6-35b-a3b]] — ...

## Page count

- state-of: 7 (6 populated, 1 skeleton)
- models: 7
- tools: 17
- benchmarks: 0
- workflows: 2
- concepts: 8
- trends: 4
- training: 2

**Total content pages: 47.**
```

## Schema / vocabulary additions

- None proposed. Both new pages use existing `coding-model`.
