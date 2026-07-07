---
type: proposal
sources:
  - raw/newsletters/2026-07-03-altman-wants-ai-to-pay-america.md
status: pending
created: 2026-07-06
---

# Proposal: Expert prompts and domain fine-tuning in finance

## Summary

The approved Bridgewater/Thinking Machines signal is useful as a training and finance pattern: expert-written prompts plus fine-tuning can outperform larger frontier models on subjective domain tasks while being materially cheaper. The proposal keeps this as a case study rather than overpromoting a single vendor page.

## Intended changes

- [x] **Update** `wiki/training/cost-aware-ai-task-routing.md` - add finance case study on domain-specific fine-tuning beating frontier defaults.
- [x] **Update** `wiki/state-of/finance.md` - add domain-tuned expert workflow signal if the page has an appropriate subcategory.
- [x] **Create** source summary `wiki/sources/newsletters/altman-ai-pay-america-2026-07-03.md`.

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (snippet)

```md
## Evidence from practice

- **Bridgewater / Thinking Machines finance case.** Newsletter coverage reports that expert prompts plus a fine-tuned Qwen3-235B variant reached 85% on a subjective finance task while costing about 14x less than a frontier baseline. Treat the exact numbers as source-reported, but the routing lesson is durable: for repeated expert-judgment tasks, domain examples and smaller tuned models can beat generic frontier defaults on both quality and cost.

## Current guidance
- When a task has repeated domain-specific judgment and stable evaluation examples, compare three routes before defaulting to frontier models: expert prompt on a frontier model, expert prompt on a cheaper strong model, and fine-tuned/open-weight model with task-specific examples.
```

### wiki/state-of/finance.md (snippet)

```md
## Recent changes
- [2026-07-03] Bridgewater/Thinking Machines case study suggests expert prompts plus domain fine-tuning can beat larger frontier models on subjective finance tasks at lower cost; preserve exact benchmark numbers as source-reported until primary materials are verified.
```

### Source summary (new)

```md
---
title: Altman wants AI to pay America
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-03-altman-wants-ai-to-pay-america.md
published: 2026-07-03
ingested: 2026-07-06
domains: [finance, models, training]
---

# Altman wants AI to pay America

Newsletter issue containing a Bridgewater/Thinking Machines case study where expert prompts and fine-tuning reportedly beat frontier baselines on a subjective finance evaluation at materially lower cost.

## Influenced pages
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) - domain-tuned model routing case
- [State of Finance](../../state-of/finance.md) - finance workflow signal

## Key claims extracted
- Expert prompts plus fine-tuning can outperform a larger frontier model on a subjective domain task.
- The reported tuned Qwen3-235B result was 85% and about 14x cheaper than a frontier baseline.
- The strategic lesson is to evaluate cost per accepted expert judgment, not model prestige.
```

## Open questions

- This proposal should be verified against the underlying Bridgewater/Thinking Machines source before the exact 85% and 14x claims are promoted beyond source-reported language.
	- Ok, verify it.
