---
title: Forward-deployed engineering (FDE)
type: training
domains: [agents]
tags: [agentic]
as_of: 2026-09-29
sources: [fde-race-may-2026, eng-leadership-openai-fde-2026-09-14, eugenalpeza-fde-boom-product-gap-2026-09-29]
---

# Forward-deployed engineering (FDE)

Forward-deployed engineering is the deployment model in which an AI provider embeds its own engineers inside a customer organization for months, writing production code in the customer's environment — part engineer, part consultant — to bridge the gap between what the provider's models can do and the customer's domain, data, and compliance constraints. This page is for deployment and go-to-market leaders deciding whether and how to run, staff, or buy FDE capacity. The model was pioneered by Palantir ("Deltas").

## Current status (as of 2026-09-29)

- As of May 2026, all three leading frontier labs (Anthropic, OpenAI, Google) run simultaneous hiring or joint-venture programs for embedding engineers directly inside customer organizations.
- Salesforce has committed to 1,000 FDEs. Anthropic has a $1.5B joint venture with Blackstone and Goldman Sachs for mid-sized firms. OpenAI has its Deployment Company. Google is hiring hundreds of FDEs.
- Deloitte State of AI 2026: the share of companies with 40%+ of AI projects in production is set to double in six months; the "AI skills gap" is the #1 reported barrier to integration.
- Software development job postings linked to AI were up 14% YoY in April 2026 (Indeed Hiring Lab).
- A counter-thesis from two former Palantir FDE leads (September 2026): FDE demand is a sign of a missing product, because the work is translating operators' judgment into agent instructions, which operators could maintain themselves (see "The product-gap argument" below).

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

## The product-gap argument

Eugen Alpeza and Yannis, who led forward-deployed AI engineering at Palantir and now run Edra, argue the industry is "hiring its way around a missing product". An FDE's core job is translation: the operator explains how the company works, the FDE turns that into instructions an agent follows, and every operating change needs the engineer again. Connecting agents to company history (a context graph) does not remove the need, because history records mistakes and legitimate exceptions alike.

- **Worked example.** A telecom's equipment-order history showed units of one voltage usually, but not always, being replaced. Only the owners of the work could say which departures were mistakes (often people unaware the procedure existed) and which were legitimate regional practice the written procedure never captured.
- **ContextOps.** Their name for doing this continuously: agents read case history and draft candidate rules with supporting and contradicting cases attached; the process owner decides which judgments become standing instructions; instructions are tested on representative cases before deployment, carry an owner and a version, and can be rolled back. The process owner is accountable for what the instructions say, and engineering maintains the systems that execute them.
- **Executable coverage.** The share of cases in a process that an agent can handle correctly with current, approved procedures, without someone supplying missing judgment. Measure it on a sample of about a hundred cases before committing a process to agents.
- **The learning loop.** Escalation, resolution with recorded reasoning, a proposed procedure update with evidence, owner approval: each pass expands coverage for every agent using that procedure, and the company owns the loop instead of renting it from an FDE team.
- **Why not fine-tune.** Company history contains bad habits as well as good ones, and every new supplier, region, or policy means retraining. An operator can maintain a written procedure but cannot fine-tune a behaviour out of a model.

The authors' implication for deployment leaders: FDE capacity buys the first translation, and the lasting asset is a process that lets operators change the instructions without an engineer in the middle.

## Recent changes

- [2026-10-19] Page created, split out of [Company-wide AI enablement](company-wide-ai-enablement.md)'s "Forward-deployed engineer (FDE) model" section.
- [2026-09-29] Added "The product-gap argument" (Eugen Alpeza, Edra): FDE work as translation operators could own, ContextOps, executable coverage, the escalation-to-procedure learning loop, and the case against fine-tuning on company history.
- [2026-09-14] Added OpenAI's FDE org in practice (Colin Jarvis interview): 2->140 headcount growth, the ~200-person OpenAI Deployment Company spinout, the outcome-focused/domain-expert-mixing staffing philosophy, a Japan COBOL-to-Java migration example, and the specific customer-failure-to-training-data feedback loop.

## Related

- [Company-wide AI enablement](company-wide-ai-enablement.md) — the broader adoption playbook FDE capacity plugs into
- [AI enablement — software development](ai-enablement-software-development.md) — forward-deployed workflow engineering as an engineering rollout pattern
- [Agents reshape organizations](../trends/agents-reshape-organizations.md) — frontier labs and agent vendors moving downstream into deployment services
- [Knowledge layer](../concepts/knowledge-layer.md) — the maintained, human-approved operating-rules layer that ContextOps keeps current

## Sources

- [FDE hiring race — Anthropic, OpenAI, Google (May 2026)](../sources/newsletters/fde-race-may-2026.md)
- [Inside OpenAI's Forward Deployed Engineer Role — Eng Leadership](../sources/newsletters/eng-leadership-openai-fde-2026-09-14.md)
- [Eugen Alpeza on X — The FDE boom is a product gap](../sources/tweets/eugenalpeza-fde-boom-product-gap-2026-09-29.md)
