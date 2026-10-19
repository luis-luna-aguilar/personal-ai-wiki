---
title: Forward-deployed engineering (FDE)
type: training
domains: [agents]
tags: [agentic]
as_of: 2026-09-14
sources: [fde-race-may-2026, eng-leadership-openai-fde-2026-09-14]
---

# Forward-deployed engineering (FDE)

Forward-deployed engineering is the deployment model in which an AI provider embeds its own engineers inside a customer organization for months, writing production code in the customer's environment — part engineer, part consultant — to bridge the gap between what the provider's models can do and the customer's domain, data, and compliance constraints. This page is for deployment and go-to-market leaders deciding whether and how to run, staff, or buy FDE capacity. The model was pioneered by Palantir ("Deltas").

## Current status (as of 2026-09-14)

- As of May 2026, all three leading frontier labs (Anthropic, OpenAI, Google) run simultaneous hiring or joint-venture programs for embedding engineers directly inside customer organizations.
- Salesforce has committed to 1,000 FDEs. Anthropic has a $1.5B joint venture with Blackstone and Goldman Sachs for mid-sized firms. OpenAI has its Deployment Company. Google is hiring hundreds of FDEs.
- Deloitte State of AI 2026: the share of companies with 40%+ of AI projects in production is set to double in six months; the "AI skills gap" is the #1 reported barrier to integration.
- Software development job postings linked to AI were up 14% YoY in April 2026 (Indeed Hiring Lab).

## Why it matters

- FDE integration turns AI tools into critical infrastructure that is nearly impossible to remove, securing multi-year enterprise revenue.
- Deep AI deployment at enterprise scale still requires human embedding: AI tools alone don't self-integrate into customer workflows, data, and compliance constraints.

## OpenAI's FDE org in practice

Colin Jarvis, OpenAI's Global Head of Forward Deployed Engineering, described the org in September 2026:

- **Shape and scale.** The internal FDE org grew from 2 people to roughly 140, sitting between GTM and product/research as a two-way link. OpenAI spun out a separate ~200-person OpenAI Deployment Company specifically to scale customer integration work while keeping the internal FDE org small and insight-focused.
- **Outcome-focused definition.** The goal is to make yourself unneeded; being needed again on the same problem means it wasn't actually solved.
- **Staffing mix.** Teams deliberately mix domain experts with engineers who lack that domain background, on the theory that outsiders are more likely to challenge the status quo.
- **Worked example.** A Japan-based legacy-system migration (COBOL-to-Java, underlying systems worth hundreds of millions of dollars): an FDE spends one day with the customer's payments team, the next building tests based on that day's insights, and another writing the actual migration code.
- **Feedback loop to research.** FDEs convert a specific customer failure into a generalizable training-data request ("the model struggles with these types of COBOL-to-Java tasks") rather than just relaying the raw complaint.
- **On-site time norms.** Roughly 50% on average, rising to ~80% in UAE and Japan engagements.

## Recent changes

- [2026-10-19] Page created, split out of [Company-wide AI enablement](company-wide-ai-enablement.md)'s "Forward-deployed engineer (FDE) model" section.
- [2026-09-14] Added OpenAI's FDE org in practice (Colin Jarvis interview): 2->140 headcount growth, the ~200-person OpenAI Deployment Company spinout, the outcome-focused/domain-expert-mixing staffing philosophy, a Japan COBOL-to-Java migration example, and the specific customer-failure-to-training-data feedback loop.

## Related

- [Company-wide AI enablement](company-wide-ai-enablement.md) — the broader adoption playbook FDE capacity plugs into
- [AI enablement — software development](ai-enablement-software-development.md) — forward-deployed workflow engineering as an engineering rollout pattern
- [Agents reshape organizations](../trends/agents-reshape-organizations.md) — frontier labs and agent vendors moving downstream into deployment services

## Sources

- [FDE hiring race — Anthropic, OpenAI, Google (May 2026)](../sources/newsletters/fde-race-may-2026.md)
- [Inside OpenAI's Forward Deployed Engineer Role — Eng Leadership](../sources/newsletters/eng-leadership-openai-fde-2026-09-14.md)
