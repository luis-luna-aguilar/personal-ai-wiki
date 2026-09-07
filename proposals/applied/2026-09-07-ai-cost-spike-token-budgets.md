---
type: proposal
source: raw/newsletters/2026-08-17-our-ai-costs-jumped-230-percent-im-not-setting-t.md
status: pending
created: 2026-09-07
---

# Proposal: Every's AI cost spike — "not setting token budgets yet"

## Summary

### The source

Every's head of operations, Arielle Shipper, writes about a real cost incident from early July: she woke to a flood of OpenAI and Ramp alerts saying the company's payment card had been declined overnight, its credit balance zeroed out despite a full balance and active auto-reload the night before. The cause turned out to be Every CEO Dan Shipper running GPT-5.6 Sol (ultra) on senior-engineer-level tasks for a Vibe Check review. Spend didn't return to normal afterward: across the first five full days after Sol's rollout, Every's daily credit usage rose from 11,520 to 26,685 credits — almost 2.5x the previous week's baseline — on top of an already-large Fable-driven baseline she'd been separately bracing for. Colleague reactions ranged from "let it ride" to "impose hard limits now and explore local models." Shipper's decision was to do neither, for a specific reason: Every doesn't standardize on one model, so staff pick whichever works best for a given job, and the cost mix shifts too fast for a fixed allocation scheme to stay current — "any intricate allocation scheme I devised would be obsolete in days, if not hours." The essay is mostly paywalled past this point; the concrete numbers and reasoning above are all in the free preview.

### What changes

`training/cost-aware-ai-task-routing.md` currently documents six evidence-from-practice case studies (Bridgewater/Thinking Machines, Spiral, Fable-for-unknowns, the eval-data-moat argument, Databricks' coding-agent benchmark, Databricks' internal FinOps breakdown) plus Arkadium's Game Lab, all supporting deliberate routing and cost controls.

- **Cost-aware AI task routing** gains a seventh Evidence-from-practice entry: Every's Sol-driven cost spike and Shipper's explicit choice not to impose hard token budgets, because model-fit-per-task and a fast-shifting cost mix make fixed allocation schemes go stale almost immediately. Page date moves to 17 August. Frontmatter `sources:` gains one new id.
- New source page for the Every essay.

### What to weigh

The source is mostly paywalled — everything usable here is from the free preview, and it's a single first-person account with no independent validation of the credit numbers. It's included as a deliberate counterpoint to the page's harder-cap examples (Uber, Cloudflare) rather than a new routing mechanism: the useful signal is that flexible, closely-watched spend can beat a rigid budget when task-to-model fit is still unsettled, not a new technique.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add Every cost-spike case study to Evidence from practice, bump `as_of`, append source id
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ai-cost-spike-token-budgets-2026-08-17.md` — source summary

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter changes:
```
as_of: 2026-08-17
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, local-ai-infrastructure-2026-06, token-tightening-ai-finops-2026-06, efficiencymaxxing-model-routing-2026-07, fable-unknowns-routing-2026-07, the-code-databricks-coding-benchmark-2026-07-10, databricks-benchmarking-coding-agents-2026-07, the-code-eval-data-moat-2026-07-13, ainews-devin-fusion-router-moat-2026-07-14, arkadium-game-lab-small-model-economics-2026-07-19, zawinskis-law-multiagents-2026-08-08, ai-cost-spike-token-budgets-2026-08-17]
```

New bullet appended to the end of `## Evidence from practice` (after the Arkadium's Game Lab entry):
```
- **Every's Sol cost spike.** Every's head of operations, Arielle Shipper, reports daily AI credit usage rose from 11,520 to 26,685 credits (~2.3x) in the first five full days after GPT-5.6 Sol rolled out — an unbudgeted spike on top of an already-elevated Fable-driven baseline, briefly zeroing out the company's payment card overnight. Her explicit choice: no hard token budgets yet, because staff use whichever model works best for a given job (no single-model standardization) and the cost mix shifts too fast — any fixed allocation scheme "would be obsolete in days, if not hours." A counterpoint to this page's harder-cap examples: flexible, closely-watched spend can beat a rigid budget when task-to-model fit is still unsettled.
```

New line appended to `## Sources`:
```
- [Every — Our AI costs jumped 230 percent. I'm not setting token budgets—yet.](../sources/newsletters/ai-cost-spike-token-budgets-2026-08-17.md)
```

### wiki/sources/newsletters/ai-cost-spike-token-budgets-2026-08-17.md (new)

```md
---
title: "Every — Our AI costs jumped 230 percent. I'm not setting token budgets—yet."
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-17-our-ai-costs-jumped-230-percent-im-not-setting-t.md
url: https://every.to/p/our-ai-costs-jumped-230-percent-i-m-not-setting-token-budgets-yet
published: 2026-08-17
ingested: 2026-09-07
domains: [agents, models]
---

# Every — Our AI costs jumped 230 percent. I'm not setting token budgets—yet.

Every's head of operations, Arielle Shipper, recounts an overnight cost incident where testing GPT-5.6 Sol on senior-engineer tasks zeroed out the company's AI payment card, then kept daily credit usage elevated: 11,520 to 26,685 credits (~2.3x) over the following five days, on top of an already-large Fable-driven baseline. Rather than impose hard token budgets, she chose to keep spend flexible, reasoning that staff intentionally use whichever model fits a given job best and that the cost mix shifts too fast for a fixed allocation scheme to stay current.

## Influenced pages

- [training/cost-aware-ai-task-routing](../../training/cost-aware-ai-task-routing.md) — new Evidence-from-practice case study on deliberately not imposing hard token budgets

## Key claims extracted

- Every's daily AI credit usage rose from 11,520 to 26,685 credits (~2.3x previous-week baseline) over the first five full days after GPT-5.6 Sol's rollout
- The spike was triggered by CEO Dan Shipper testing GPT-5.6 Sol (ultra) on senior-engineer-level tasks for a Vibe Check review, which briefly zeroed out the company's OpenAI/Ramp payment balance overnight
- Every deliberately does not impose hard token budgets, because staff use whichever model works best for a given job rather than standardizing on one, and the cost mix shifts too fast for a fixed allocation scheme to stay current
```

## Open questions

None.
