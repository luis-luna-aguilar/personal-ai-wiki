---
title: Astra for Law
type: tool
domains: [legal]
subcategory: legal-ai
tags: [openai, closed-source]
as_of: 2026-11-23
sources: [openai-astra-for-law-2026-09-17, harvey-astra-for-law-plugin-2026-09-17, openai-introducing-gpt-6-2-astra-sol]
---

# Astra for Law

OpenAI's legal configuration of [GPT-6.2 Astra](../models/gpt-6-2-astra.md) (launched on [GPT-6 Astra](../history/models/gpt-6-astra.md)): the model plus a legal search index, built-in instructions for legal analysis and writing, and governance controls for law firms. Firms use it directly in ChatGPT and Codex, and legal-tech companies such as [Harvey](harvey.md) and Legora build their own products on it.

## Current status (as of 2026-11-23)

- Launched 2026-09-17 for selected law firms through a Trusted Access Program in ChatGPT and Codex ("GPT-6 Astra Law" in the model picker); API access as `gpt-6-astra-law` is "coming soon". OpenAI says it will carry the legal settings forward to later frontier models.
- **Legal search index:** U.S. case law, statutes, regulations, court rules, and administrative decisions across 230M+ URLs, updated daily, including Free Law Project's CourtListener collection (over 99.9% of published U.S. precedential case law). Positioned as a complement to licensed content such as Thomson Reuters.
- **Research results:** on 200 questions from the private validation set of Vals AI's Legal Research Bench, at the highest reasoning effort, 54.0% passed the overall correctness check vs. 38.7% for GPT-6 Astra with web search alone; 24% more reference cases found on case-law questions; up to 54% more relevant passages retrieved from the correct opinions.
- **Precedent matching:** in OpenAI's two side-by-side memo examples, Astra for Law returned closely matching precedents, while Claude Fable 5.1 cited a holding reversed on appeal (litigation) and reported no matching case (transactional).
- **Controls:** Zero Data Retention on the API for eligible firms; ChatGPT Enterprise usage excluded from human review by default; information permissions, ethical walls, client instructions, and firm oversight being designed with Latham & Watkins.
- **Ecosystem:** 26 partner-built plugins (including iManage, Intapp, DeepJudge, Relativity, Clio, Harvey, and Thomson Reuters HighQ with a coming CoCounsel Legal connector), 9 community plugins carrying 47 adaptable skills (LegalQuants, LECG, Skills.law), and ChatGPT for Word generally available.
- **Model upgrade (2026-11-23):** now configured on GPT-6.2 Astra, as OpenAI said it would carry the legal settings forward. OpenAI says it scores higher than GPT-6.2 Astra on Harvey LAB-AA v1.1, where 6.2 Astra alone more than doubles Claude Fable 5.2's pass rate at about a sixth of the cost. LAB-AA credits a deliverable only if it meets every grading criterion with no material hallucinations.

## Firm builds

OpenAI's forward-deployed engineers adapted ChatGPT Enterprise with custom interfaces and proprietary-data integrations for individual firms (see [Forward-deployed engineering](../training/forward-deployed-engineering.md)): Sullivan & Cromwell's agreement analyzer applies the firm's negotiating playbooks and precedents to a new deal, spots risks that appear when provisions are read together, and drafts redlines and client advice; Ropes & Gray's diligence system works through a data room and traces findings to source, such as customer contracts that require notice or consent; Cooley's GO Public supports IPO preparation and carries deal changes across the filing. Wachtell, Lipton, Rosen & Katz is working with OpenAI's research and engineering teams on legal judgment.

## Why it matters

A frontier lab is now both a vendor in legal AI and the supplier to legal-AI specialists. Harvey ships a plugin inside ChatGPT Enterprise and also builds on Astra for Law in its own products, so the question for specialists becomes what they add on top of the lab's own legal configuration: workflow, matter context, governance, or proprietary content. OpenAI frames its approach as "open and composable", meant to grow the ecosystem rather than replace it.

## Weaknesses / caveats

- The benchmark comparison is against GPT-6 Astra with web search, not against Harvey, CoCounsel, or other legal-AI products, and uses Vals AI's private validation set.
- Access is limited to selected firms at launch, and the API has no date.
- The search index covers U.S. law only.

## Recent changes

- [2026-11-23] Moved to GPT-6.2 Astra; OpenAI reports it scores above the base model on Harvey LAB-AA.
- [2026-09-17] Launched for selected firms in ChatGPT and Codex: GPT-6 Astra plus a U.S. legal search index, legal instructions, firm controls, and 26 partner plugins; 54.0% vs. 38.7% on Vals AI Legal Research Bench validation questions.

## Sources

- [Introducing Astra for Law (OpenAI)](../sources/articles/openai-astra-for-law-2026-09-17.md)
- [Harvey (@harvey) — Harvey plugin for Astra for Law in ChatGPT Enterprise](../sources/tweets/harvey-astra-for-law-plugin-2026-09-17.md)
- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
