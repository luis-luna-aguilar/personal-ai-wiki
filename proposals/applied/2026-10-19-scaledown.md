---
type: proposal
source: raw/articles/2026-10-19-scaledownai.md
status: pending
created: 2026-10-19
---

# Proposal: ScaleDown homepage (task-specific small models)

## Summary

### In short

Narrow, single-task small models are now sold as a cheap commodity API, which makes the wiki's advice to send classification and extraction to small models easy to act on. ScaleDown offers four such models (classify, extract, summarize, compress) at $0.05 per million input tokens, with free output and a 1M-token context. The proposal adds one evidence bullet to Cost-aware AI task routing and a source page, not a model page. Reason to hesitate: the homepage has no date, and its benchmark charts lost their values in capture.

[[#Open questions|Open questions: 1 to answer.]]

### The source

ScaleDown describes itself as an applied research lab that builds task-specific models, one model and one architecture per task. Its homepage, captured on 19 October 2026, lists four: Classify sorts text and images against a label set you write in plain text and returns calibrated label probabilities; Extract pulls structured fields from text; Summarize writes length-controlled summaries; Compress shortens prompts and chat context before they are sent to a larger model. The site calls them constrained-decoding models, meaning the model can only emit outputs from a fixed valid set, such as your label list or field schema.

Pricing is flat: $0.05 per million text input tokens ($0.15 for images), output free, 1M-token context, and 1M free tokens for new accounts. The models are reachable through ScaleDown's own API or OpenRouter, and enterprises can get a dedicated instance or a license to self-host. The page headlines "state-of-the-art accuracy, 467x cheaper, 200x faster" and shows comparison charts against small frontier models such as Claude Haiku and GPT-5.4 Mini on the CLINC OOS intent-classification benchmark, but the captured text lost which bar belongs to which model. A banner also announces diet_code, a tool for saving tokens in Claude Code.

### What changes

The routing page already advises using small or open models for cheap classification and extraction, with case studies such as Arkadium's tiny game model and Bridgewater's tuned Qwen; it names no off-the-shelf product for that tier.

- **Cost-aware AI task routing** gains one bullet under "Routing as infrastructure" naming ScaleDown as a packaged form of that advice, with its pricing and the compression model as a way to trim context before frontier calls. It gets one Recent-changes entry dated 19 October (two entries become three, no spill), and its page date moves from 7 September to 19 October. Body length rises from about 2,390 to about 2,460 words, just under the 2,500 ceiling for training pages.
- New source page `wiki/sources/articles/scaledown-homepage-2026-10.md`.

### What to weigh

A homepage has no publication date, so 19 October, the capture date, stands in for it. The bigger call is scope: the `utility-model` subcategory fits ScaleDown exactly, so a `models/scaledown.md` page would need no schema change, but the only comparable page, OpenAI Privacy Filter, was built from two independent write-ups, while this would rest on one marketing page whose benchmark values did not survive capture. I chose a single bullet and left the page as an open question. The diet_code tool is mentioned but not developed, since the homepage gives only its name and one line.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add one bullet at the end of `### Routing as infrastructure`; adds one Recent-changes entry dated 2026-10-19 (3 of 10, no spill); append source id to frontmatter `sources:` and one link to `## Sources`; `as_of` 2026-09-07 → 2026-10-19
- [ ] **Create** `wiki/sources/articles/scaledown-homepage-2026-10.md` — source summary

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter (changed fields only; `sources:` appends `scaledown-homepage-2026-10`):

```
as_of: 2026-10-19
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, local-ai-infrastructure-2026-06, token-tightening-ai-finops-2026-06, efficiencymaxxing-model-routing-2026-07, fable-unknowns-routing-2026-07, the-code-databricks-coding-benchmark-2026-07-10, databricks-benchmarking-coding-agents-2026-07, the-code-eval-data-moat-2026-07-13, ainews-devin-fusion-router-moat-2026-07-14, arkadium-game-lab-small-model-economics-2026-07-19, zawinskis-law-multiagents-2026-08-08, ai-cost-spike-token-budgets-2026-08-17, ainews-stripe-openrouter-2026-08-17, glean-model-routing-2026-08-18, ainews-poolside-nvidia-2026-08-21, ainews-andrew-ng-ai-engineering-2026-08-25, every-cloning-your-coworkers-2026-08-26, cursor-agent-swarm-economics-2026-09-07, ubereng-software-factory-2026-08-28, ainews-2026-04-23, every-33-questions-executives-2026-08-28, scaledown-homepage-2026-10]
```

`### Routing as infrastructure` — new bullet, appended after the "AT&T's open-model routing at scale" bullet:

```
- **Task-specific small models as a commodity API.** ScaleDown sells four single-task models (classify, extract, summarize, compress) at a flat $0.05 per million input tokens, output free, 1M-token context, through its own API or OpenRouter, with a self-hosted option. It packages this page's advice to route classification and extraction to small models; its compress model trims prompts and chat context before a frontier call. The vendor claims state-of-the-art accuracy at 467x lower cost.
```

`## Recent changes` (adds one entry dated 2026-10-19 at the top):

```
- [2026-10-19] Added ScaleDown as an example of task-specific small models sold as a commodity API (classify, extract, summarize, compress at $0.05 per million input tokens).
- [2026-10-19] Merged the "Cost and model routing" proven-patterns group from [Company-wide AI enablement](company-wide-ai-enablement.md): tasteful tokenmaxxing (depth over breadth), route by task novelty, and token allocation as governance (folded into AI FinOps controls); its efficiencymaxxing bullet duplicated this page's Current guidance and was not repeated.
- [2026-07-08] Added efficiencymaxxing: stage-level model routing, token audits, and one-variable reruns as a company-wide AI cost-control practice.
```

`## Sources` (appends one link):

```
- [ScaleDown AI — Task-specific SLMs (homepage)](../sources/articles/scaledown-homepage-2026-10.md)
```

### wiki/sources/articles/scaledown-homepage-2026-10.md (new)

```
---
title: 'ScaleDown AI | Task-specific SLMs (homepage)'
type: source
source_type: article
source_file: raw/articles/2026-10-19-scaledownai.md
url: https://scaledown.ai/
ingested: 2026-10-19
domains: [models]
---

# ScaleDown AI — Task-specific SLMs (homepage)

Product homepage for ScaleDown, a self-described applied research lab selling four task-specific small models (classify, extract, summarize, compress) through a flat-priced API. No publication date; captured 2026-10-19.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — evidence bullet under "Routing as infrastructure"

## Key claims extracted

- One model, one architecture, one task: Classify (calibrated label probabilities, text and images, plain-text label taxonomy, no fine-tuning), Extract (structured fields), Summarize (length-controlled), Compress (shortens prompts and chat context)
- Described as constrained-decoding models
- Pricing: $0.05 per 1M text input tokens, $0.15 per 1M image input tokens, output free, 1M-token context; 1M free tokens for new accounts; flat, no tiers
- Available via ScaleDown API and OpenRouter; enterprise dedicated instance or self-hosting license
- Claims SOTA accuracy, "467x cheaper," "200x faster"; comparison charts on CLINC OOS against Claude Haiku, GPT-5.4 Mini, Qwen 27B, Grok 4.2, Gemini Lite, DS Flash (per-model values not recoverable from the captured text)
- Zero data retention, no training on customer data; built to SOC 2, HIPAA, GDPR, ISO 27001 standards
- Announces diet_code, a tool to save tokens in Claude Code (no further detail on the homepage)
```

## Schema / vocabulary additions

None.

## Open questions

- Should ScaleDown get its own page now, as `wiki/models/scaledown.md` with subcategory `utility-model` (no schema change needed)? I recommend waiting for a docs page, benchmark post, or independent write-up, so the page can carry readable benchmark numbers and a dated claim.
	- You can further navigate this website and get this done.
