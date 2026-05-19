---
type: proposal
sources:
  - raw/newsletters/2026-05-14-anthropic-faces-developers-backlash.md
  - raw/newsletters/2026-05-15-tavus-turns-any-image-into-an-ai-human.md
status: pending
created: 2026-05-18
---

# Proposal: Forward-deployed engineer (FDE) hiring race — Anthropic, OpenAI, Google (lightweight)

## Summary

In the same week, Anthropic launched a $1.5B venture with Blackstone and Goldman Sachs to embed engineers inside mid-sized firms; OpenAI started its own Deployment Company; Google announced hiring hundreds of FDEs. The model is Palantir's "Deltas" playbook: engineers embed at customer sites for months writing production code, not presentations. Salesforce committed to 1,000 FDEs. Strategic logic: once embedded, the integration becomes near-impossible to remove, creating critical infrastructure revenue. Deloitte State of AI 2026: companies with 40%+ of AI in production set to double in six months, but skills gap is the #1 barrier.

## Intended changes

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add FDE model as an enterprise adoption pattern; add Deloitte stat; update `as_of`; add source
    > **as_of:** `2026-05-13` → `2026-05-15`
    >
    > **Add new section or to Proven patterns:**
    > ```markdown
    > ## Forward-deployed engineer (FDE) model
    >
    > As of May 2026, all three leading frontier labs (Anthropic, OpenAI, Google) have simultaneous hiring or JV programs for embedding engineers directly inside customer organizations. The model was pioneered by Palantir ("Deltas"): FDEs work on-site for months, writing production code in the customer's environment — part engineer, part consultant, bridging the gap between AI provider capability and customer domain knowledge.
    >
    > **Why it matters for enablement:**
    > - FDE integration transforms AI tools into critical infrastructure that is nearly impossible to remove, securing multi-year enterprise revenue
    > - Deloitte State of AI 2026: the share of companies with 40%+ of AI projects in production is set to double in six months; the "AI skills gap" is the #1 reported barrier to integration
    > - Salesforce: committed to 1,000 FDEs. Anthropic: $1.5B joint venture with Blackstone and Goldman Sachs for mid-sized firms. OpenAI: Deployment Company. Google: hiring hundreds of FDEs.
    > - Software development job postings linked to AI were up 14% YoY in April 2026 (Indeed Hiring Lab)
    >
    > **Pattern implication:** deep AI deployment at enterprise scale still requires human embedding — AI tools alone don't self-integrate into customer workflows, data, and compliance constraints.
    > ```
    >
    > **Add to sources list:** `fde-race-may-2026`

- [x] **Create** `wiki/sources/newsletters/fde-race-may-2026.md` — source summary

## Page drafts

### wiki/sources/newsletters/fde-race-may-2026.md (new)

```markdown
---
title: "FDE hiring race — Anthropic, OpenAI, Google (May 2026)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-14-anthropic-faces-developers-backlash.md
published: 2026-05-14
ingested: 2026-05-18
domains: [agents]
---

# FDE hiring race — Anthropic, OpenAI, Google (May 2026)

The Code and Superhuman newsletters covered simultaneous FDE (forward-deployed engineer) hiring announcements from Anthropic ($1.5B JV with Blackstone and Goldman), OpenAI (Deployment Company), and Google (hundreds of FDEs hired). Palantir's "Deltas" playbook is the template: embed engineers on-site for months to write production code inside client environments, creating stickiness that transforms AI tools into critical infrastructure.

## Influenced pages

- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — FDE model added as enterprise deployment pattern

## Key claims extracted

- Anthropic: $1.5B JV with Blackstone and Goldman Sachs to embed engineers in mid-sized firms
- OpenAI: own Deployment Company announced same week
- Google: hiring hundreds of FDEs
- Salesforce: committed to 1,000 FDEs
- Palantir FDE model ("Deltas"): on-site, months-long, writes production code, not presentations; 640% stock return from 2022 lows
- Strategic logic: integration → critical infrastructure → difficult to remove → multi-year revenue
- Deloitte State of AI 2026: 40%+ of AI in production set to double in 6 months; skills gap is #1 barrier
- Indeed Hiring Lab: software dev jobs linked to AI up 14% YoY in April 2026
```
