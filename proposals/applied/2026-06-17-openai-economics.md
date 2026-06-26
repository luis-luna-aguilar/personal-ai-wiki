---
type: proposal
sources:
  - raw/newsletters/2026-06-12-new-report-exposes-ai-economics.md
  - raw/newsletters/2026-06-17-copilot-cowork-becomes-generally-available.md
status: pending
created: 2026-06-17
---

# Proposal: OpenAI financial situation + AI subscription economics

## Summary

Leaked audited financials: OpenAI posted $38.5B net loss in 2025 (7× worse than 2024) on $13B revenue; filed confidential S-1 for IPO; ChatGPT market share dipped below 50% for the first time. SemiAnalysis found that $200/mo subscriber plans cost Anthropic up to $8,000/mo and OpenAI up to $14,000/mo in compute. Scale's "6% Report" says only 6% of organizations have AI deployed at scale with measurable value.

## Intended changes

- [x] **Update** `wiki/state-of/models.md` — add economics / funding context section or note

## Page drafts

### wiki/state-of/models.md (updated section)

> **Add new subsection at the bottom (before ## Recent changes), or append to existing if one exists:**

```markdown
## AI economics snapshot (as of 2026-06-17)

Key economic signals that shape how frontier model access should be understood:

- **OpenAI FY2025 (leaked):** $38.5B net loss (7× worse than 2024's $5B); revenue $3.7B → $13B; ChatGPT market share dipped below 50% for first time; confidential S-1 filed for IPO; company considering drastic API price cuts ahead of anticipated Anthropic move (WSJ)
- **Subscriber compute costs (SemiAnalysis):** $200/mo Claude Max plan costs Anthropic up to $8,000/mo in compute; $200/mo ChatGPT Pro costs OpenAI up to $14,000/mo — both unlimited-usage tiers are structurally loss-leading at current usage rates
- **Enterprise deployment reality (Scale "6% Report"):** Only 6% of organizations have deployed AI at scale with measurable business value despite large spending; most are still in pilot stage
- **Oracle:** $19B quarterly revenue; largest cloud infrastructure beneficiary of frontier AI compute spending
```

> **Add to ## Recent changes (prepend):**
```
- [2026-06-17] OpenAI FY2025 leaked: $38.5B net loss, $13B revenue, below-50% ChatGPT market share; IPO S-1 filed; SemiAnalysis: $200/mo Claude Max costs Anthropic up to $8,000/mo compute; Scale 6% Report: only 6% of orgs at AI-at-scale stage
```

> **Frontmatter: update `as_of` to 2026-06-17; add new source `openai-economics-june-2026` to sources list.**

### wiki/sources/newsletters/openai-economics-june-2026.md (new)

````md
---
title: AI subscription economics and OpenAI financials (June 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-12-new-report-exposes-ai-economics.md
published: 2026-06-12
ingested: 2026-06-17
domains: [models]
---

# AI subscription economics and OpenAI financials (June 2026)

SemiAnalysis compute cost analysis, leaked OpenAI FY2025 financials, and Scale's enterprise deployment survey.

## Influenced pages

- [State of Models](../../state-of/models.md) — economics snapshot section

## Key claims extracted

- SemiAnalysis: $200/mo Claude Max plan costs Anthropic up to $8,000/mo in compute at heavy usage
- SemiAnalysis: $200/mo ChatGPT Pro costs OpenAI up to $14,000/mo in compute
- OpenAI FY2025 (leaked): $38.5B net loss; revenue $3.7B→$13B; ChatGPT <50% market share for first time
- OpenAI filed confidential S-1 for IPO; considering drastic API price cuts (WSJ)
- Scale "6% Report": only 6% of organizations deployed AI at scale with measurable business value
- Oracle quarterly revenue: $19B (largest infrastructure beneficiary)
````
