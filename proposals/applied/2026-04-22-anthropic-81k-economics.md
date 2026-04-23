---
type: proposal
sources:
  - raw/articles/2026-04-23-anthropiccom-research-81k-economics.md
  - raw/articles/2026-04-22-anthropiccom-research81k-economics.md
status: pending
created: 2026-04-23
---

# Proposal: Anthropic 81K-Person AI Economics Survey

## Summary

Anthropic published survey results from 81,000 Claude users on the economics of AI. The study provides the most direct empirical data the wiki has on AI's workforce impact. Key non-obvious findings: scope expansion (doing new tasks) is the primary productivity driver at 48%, ahead of speed at 40%; job threat concern is U-shaped relative to speedup (both those slowed *and* those with the largest speedups are most worried); and early-career workers are significantly worse off than senior workers in terms of personal benefit (60% vs 80%). These findings update the framing in `company-wide-ai-enablement.md` and warrant a new source page.

## Intended changes

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add empirical findings to `## Evidence from practice`; add source to frontmatter
- [x] **Create** `wiki/sources/articles/anthropic-81k-economics.md` — source summary

## Page drafts

### wiki/training/company-wide-ai-enablement.md (update — diff only)

> **Add to `sources` frontmatter:** `anthropic-81k-economics`

> **Add to `## Evidence from practice` (append):**
> ```markdown
> **Anthropic 81K-person economics survey (April 2026):** The largest direct survey of Claude users on AI's economic impact (80,508 respondents). Key quantified findings:
> - **Scope, not speed, is the primary productivity driver.** 48% of users who described productivity gains cited expanded scope (doing new or previously impossible tasks); 40% cited speed; quality and cost were minor. The common "AI makes you faster" framing understates the more significant "AI makes you capable of new things" effect.
> - **Mean self-reported productivity: 5.1/7** — "substantially more productive." ~3% reported negative or neutral impact.
> - **Job threat correlates with observed AI exposure.** People in occupations where Claude does the highest share of tasks worry about displacement 3× more often than those in low-exposure roles. Elementary school teachers were less worried than software engineers, consistent with task distribution data.
> - **U-shaped threat relationship with speedup.** Both those *slowed down* by AI (creative workers who find it stifling) and those experiencing the *largest speedups* express the most job displacement concern. The moderate-speedup middle group is least worried. If a role's tasks shrink dramatically in time required, workers sense future viability uncertainty.
> - **Benefits flow to workers more than employers.** Most respondents who named a beneficiary cited themselves. Only 10% said employers were extracting more work. But this is uneven across career stage.
> - **Early-career workers are worse positioned.** 60% of early-career respondents personally benefited from AI vs 80% of senior professionals. Early-career workers also expressed significantly higher job displacement concern, consistent with tentative signs of slowdowns in hiring of recent graduates.
> - **Wage-productivity relationship is U-shaped.** Highest-paid workers (software developers, management) report the largest gains. But some lowest-wage workers also report large gains — often for side projects or new capabilities. Mid-tier scientific and legal professionals are the least enthusiastic.
> ```

### wiki/sources/articles/anthropic-81k-economics.md (new)

````md
---
title: What 81,000 people told us about the economics of AI
type: source
source_type: article
source_file: raw/articles/2026-04-23-anthropiccom-research-81k-economics.md
url: https://www.anthropic.com/research/81k-economics
published: 2026-04-23
ingested: 2026-04-23
domains: [agents]
---

# What 81,000 people told us about the economics of AI

Anthropic survey of 80,508 Claude users on AI's economic impact. Respondents shared open-ended reflections; Claude-powered classifiers inferred occupation, career stage, productivity level, speedup, job threat, and beneficiary from free-form text.

## Influenced pages

- [[training/company-wide-ai-enablement]] — empirical evidence on productivity type, job threat patterns, career stage gap

## Key claims extracted

- Scope expansion = 48% of productivity gains; speed = 40%; quality and cost much smaller
- Mean self-reported productivity: 5.1/7 ("substantially more productive")
- Job threat correlates with observed exposure — 3× more concern in top-25% vs bottom-25% exposure quartile
- U-shaped job threat vs speedup: slowed workers and fastest-speedup workers worry most; moderate speedup is least worried
- Early-career workers: 60% personally benefit; senior workers: 80% personally benefit
- 10% of those who named a beneficiary said employers were extracting more work
- Highest-paid occupations (management, software) report largest gains; mid-tier scientific and legal the least enthusiastic
- Low-wage workers also report large gains — often from scope expansion into new capabilities

## Caveats noted by authors

- Limited to active Claude.ai users who chose to respond — likely over-represents those who perceive benefits flowing to themselves
- Occupation, career stage, and other variables are inferred from contextual clues, not directly asked
- Should be confirmed in structured surveys that ask directly about these dimensions
````
