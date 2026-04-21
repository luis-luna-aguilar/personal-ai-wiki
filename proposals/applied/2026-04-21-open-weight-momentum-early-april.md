---
type: proposal
sources:
  - raw/newsletters/2026-04-03-ainews-gemma-4-the-best-small-multimodal-open-m.md
  - raw/newsletters/2026-04-05-gemma-4.md
  - raw/newsletters/2026-04-07-ainews-gemma-4-crosses-2-million-downloads.md
  - raw/tweets/2026-04-01-xcom-hcompany_aistatus2039021096649.md
  - raw/newsletters/2026-04-02-ainews-a-quiet-april-fools.md
status: pending
created: 2026-04-21
---

# Proposal: Open-weight momentum in early April

## Summary

The current wiki already tracks later-April open coding-model momentum via GLM, MiniMax, Qwen, and Kimi. This earlier batch adds a different layer: Gemma 4 as a meaningful open multimodal adoption signal, and Holo3 as an early open-weight computer-use contender with an explicit cost/performance claim.

The cleanest fit is a trend page rather than forcing thin model pages into the current schema.

## Intended changes

- [x] **Create** `wiki/trends/open-weight-momentum-broadens.md` — trend page for the early-April broadening of open-weight momentum beyond pure coding models
  > See full draft below.

- [x] **Update** `wiki/state-of/models.md` — add a recent-changes note linking Gemma 4 and the broader open-weight wave
  > See diff snippet below.

- [x] **Update** `wiki/state-of/computer-use.md` — add a recent-changes note that open-weight computer-use contenders are starting to appear
  > See diff snippet below.

- [x] **Update** `wiki/index.md` — add the new trend and refresh counts
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/open-weight-momentum-early-april.md` — source summary page
  > See full draft below.

## Page drafts

### wiki/trends/open-weight-momentum-broadens.md (new)

```markdown
---
title: Open-weight momentum broadens
type: trend
domains: [models, computer-use]
tags: [open-weights, google]
as_of: 2026-04-07
sources: [open-weight-momentum-early-april]
---

# Open-weight momentum broadens

The trend: by early April 2026, open-weight momentum was no longer only a coding-model story. Gemma 4 supplied a stronger open multimodal signal with visible adoption, while Holo3 suggested that even computer-use models were entering the open-weight competition with concrete benchmark and price claims.

## Current signal

- **Gemma 4** is the clearest open multimodal signal in this batch: repeated coverage plus a 2M-download milestone made it feel like more than a one-day launch blip.
- **Holo3** is the clearest open computer-use signal in this batch: an OSWorld-Verified claim, weights on Hugging Face, and a direct cost/performance comparison against frontier proprietary systems.
- The deeper point is breadth. Open-weight competition is spreading across more task categories, not staying confined to code-only releases.

## Why it matters

This changes how the wiki should read open-model progress. The story is no longer only "a few coding models are getting good." It is that open-weight systems are broadening into multimodal and agentic/computer-use territory, which could change where state-of pages start to see credible alternatives.

## What to watch

- Whether Gemma 4 becomes a durable reference point in open multimodal deployment rather than only a popular release
- Whether open computer-use models like Holo3 gain credible third-party validation beyond launch claims
- Whether this broadening leads to new stable subcategories or simply stronger challenger entries inside existing ones

## Sources

- [[sources/newsletters/open-weight-momentum-early-april]]
```

### wiki/state-of/models.md (updated snippet)

```markdown
## Recent changes

- [2026-04-07] Early-April open-weight momentum broadened beyond coding-only releases: Gemma 4 became a notable open multimodal adoption signal; see [[trends/open-weight-momentum-broadens]]
- [2026-04-13] Added [[models/minimax-m2-7]] and [[models/glm-5-1]] under `Coding models`; earlier April sources show open coding-model momentum was broader than the later Qwen/Kimi cluster alone
- [2026-04-08] Mythos / Glasswing cluster suggests a new trend: frontier capability may increasingly be deployed selectively rather than broadly — see [[trends/restricted-frontier-deployment]]
- [2026-04-21] Added [[models/qwen-3-6-35b-a3b]] under `Coding models`; practical local-agent baseline on 24GB-class hardware
- [2026-04-21] Anthropic/AWS: 5 GW compute secured, $5B investment, up to $20B more — see [[trends/compute-infrastructure]]
```

### wiki/state-of/computer-use.md (updated snippet)

```markdown
## Recent changes

- [2026-04-07] Early open-weight contender signal: Holo3 claimed 78.9% on OSWorld-Verified with weights released, suggesting computer-use may not remain proprietary-only for long
- [2026-04-10] Page created with [[tools/perplexity-computer]] as first entry after triaging Superhuman AI newsletter
```

### wiki/index.md (updated snippet)

```markdown
## Trends

- [[trends/agents-reshape-organizations]] — leverage moves from individual to org as autonomous agents take coordination work *(as_of: 2026-04-21)*
- [[trends/ai-in-science]] — biology and drug discovery now provide the clearest current signal: Noetik and GPT-Rosalind *(as_of: 2026-04-21)*
- [[trends/compute-infrastructure]] — frontier compute scale diverging; Anthropic/AWS 5 GW deal as inflection point *(as_of: 2026-04-21)*
- [[trends/open-weight-momentum-broadens]] — open-weight competition is spreading beyond coding into multimodal and computer-use systems *(as_of: 2026-04-07)*
- [[trends/proprietary-data-becomes-model-moat]] — proprietary operational data, domain evals, and narrow training loops may become a stronger moat as model quality converges *(as_of: 2026-04-10)*
- [[trends/restricted-frontier-deployment]] — frontier labs may increasingly withhold or selectively deploy their highest-capability systems rather than ship them broadly *(as_of: 2026-04-08)*

## Page count

- state-of: 7 (6 populated, 1 skeleton)
- models: 7
- tools: 17
- benchmarks: 0
- workflows: 2
- concepts: 8
- trends: 6
- training: 2

**Total content pages: 49.** The wiki is still in the early stage, but no longer below the initial bootstrap threshold.
```

### wiki/sources/newsletters/open-weight-momentum-early-april.md (new)

```markdown
---
title: Open-weight momentum in early April
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-03-ainews-gemma-4-the-best-small-multimodal-open-m.md
ingested: 2026-04-21
domains: [models, computer-use]
---

# Open-weight momentum in early April

This source summary captures an early-April shift in open-weight momentum. The signal is broader than open coding models alone: Gemma 4 became a meaningful open multimodal adoption story, while Holo3 suggested that computer-use systems were also entering the open-weight competition.

## Influenced pages

- [[trends/open-weight-momentum-broadens]] — tracks the broadening of the open-weight wave beyond coding
- [[state-of/models]] — adds Gemma 4 as an early-April open multimodal signal
- [[state-of/computer-use]] — adds Holo3 as an early open computer-use contender signal

## Key claims extracted

- Gemma 4 had both repeated positive coverage and a visible 2M-download adoption milestone
- Holo3 positioned itself as an open-weight computer-use model with a concrete OSWorld-Verified claim and weights release
- The broader signal is that open-weight competition is widening across capability categories, not staying confined to code generation
```
