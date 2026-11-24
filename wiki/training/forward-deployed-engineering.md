---
title: Forward-deployed engineering (FDE)
type: training
domains: [agents]
tags: [agentic]
as_of: 2026-11-19
sources: [fde-race-may-2026, eng-leadership-openai-fde-2026-09-14, eugenalpeza-fde-boom-product-gap-2026-09-29, every-fde-openings-trueup-2026-11-13, every-ode-field-evidence-2026-11-11, every-rollouts-fail-on-people-2026-11-19, latent-space-ganesh-fde-best-practices-2026-09-12]
---

# Forward-deployed engineering (FDE)

Forward-deployed engineering is the deployment model in which an AI provider embeds its own engineers inside a customer organization for months, writing production code in the customer's environment — part engineer, part consultant — to bridge the gap between what the provider's models can do and the customer's domain, data, and compliance constraints. This page is for deployment and go-to-market leaders deciding whether and how to run, staff, or buy FDE capacity. The model was pioneered by Palantir ("Deltas").

## Current status (as of 2026-11-19)

- Open FDE roles grew 4.6x over the year to November 2026 while front-end roles fell 51% and iOS roles 46% (TrueUp data, via Every). Every's reading: specialists were hired partly to split systems no one person could hold; agents now hold them, leaving people to direct agents and work with customers.
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

## Field evidence from deployments

- **Ode (November 2026).** Hugh Wimberly, a staff engineer at Ode, which Every describes as the enterprise AI services firm Anthropic launched with Blackstone and Hellman & Friedman, reports no layoffs across six client projects. At one B2B company, onboarding a new customer took up to ~100 hours, mostly clicking through a UI; an agent cut it to ~30, and cheaper onboarding opened a segment that could not previously afford the service, so the team wants more staff. At an accounting client, the direction is agents searching clients' financial records for new opportunities, moving accountants toward advisory work. Some offshore jobs that consisted of repetitive clicking did go, and his clients chose to change rather than having it imposed.
- **Rollouts fail on people, not models.** Wimberly and Anthropic's Jeremy Hadfield (Thesis: 2027): automate the part of the job people dislike first and let them watch it work; at one client, 20-year veterans ignored the assistant until new hires outpaced them with it.

## Telling a real FDE role from a relabelled one

Vinoo Ganesh (Kepler CEO; at Palantir he ran Project Frontline, the rotation about 250 engineers went through to become FDEs) argues the title now covers sales engineers, quota-carrying reps who code, and consultants with a statement of work (September 2026). His test:

- **The FDE collects nouns and verbs.** Nouns are what the business treats as real (a position, a counterparty), defined differently in every company; verbs are how those things move (how a trade gets booked, who signs off on an exception). Almost none of it is written down, and it is learned by watching people work.
- **The output is product, not one happy customer.** Keeping an account happy is the solutions architect's job. An engagement that changes nothing upstream is consulting under a better title; a one-off fix shipped without folding it into the platform becomes something you maintain for years.
- **Report to product, not sales.** Pointed at sales, the incentive is closing the account in front of you; pointed at product, every deployment must leave something the next one can start from.

This agrees with OpenAI's "make yourself unneeded" norm above and with the product-gap argument's view that the lasting asset is the platform, not the engagement.

## Recent changes

- [2026-11-19] Added role-demand data (FDE openings 4.6x; front-end −51%, iOS −46%), field evidence from Ode (onboarding ~100 → ~30 hours, no layoffs across six clients; rollouts fail on people), and Vinoo Ganesh's test for a real FDE role (nouns and verbs, product output, report to product, not sales).
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
- [Every — The engineering job that's up 4.6x](../sources/newsletters/every-fde-openings-trueup-2026-11-13.md)
- [Every — Ode field evidence from Thesis: 2027](../sources/newsletters/every-ode-field-evidence-2026-11-11.md)
- [Every — AI rollouts fail on people, not models](../sources/newsletters/every-rollouts-fail-on-people-2026-11-19.md)
- [Latent Space — The Rise of the Forward Deployed Engineer (Vinoo Ganesh)](../sources/newsletters/latent-space-ganesh-fde-best-practices-2026-09-12.md)
