---
title: Introducing Astra for Law (OpenAI)
type: source
source_type: article
source_file: raw/articles/2026-10-26-openaicom-index-astra-for-law.md
url: https://openai.com/index/astra-for-law/
published: 2026-09-17
ingested: 2026-10-26
domains: [legal]
---

# Introducing Astra for Law (OpenAI)

OpenAI's launch post for Astra for Law, a configuration of GPT-6 Astra with a U.S. legal search index, legal analysis and writing instructions, and law-firm controls, offered to firms in ChatGPT and Codex and as a foundation for legal-tech companies.

## Influenced pages

- [Astra for Law](../../tools/astra-for-law.md) — new page
- [State of Legal](../../state-of/legal.md) — new leader line
- [Harvey](../../tools/harvey.md) — builds on Astra for Law; Grupen quote
- [GPT-6 Astra](../../models/gpt-6-astra.md) — legal configuration

## Key claims extracted

- Astra for Law = GPT-6 Astra + legal search index + instructions for legal analysis and writing; API customers including Harvey and Legora can build on it; legal capabilities to carry to later frontier models
- Index: U.S. case law, statutes, regulations, court rules, administrative decisions; 230M+ URLs, sources added daily; Free Law Project / CourtListener covering >99.9% of published U.S. precedential case law; complements licensed content (Thomson Reuters)
- Vals AI Legal Research Bench, 200 private-validation questions, highest reasoning effort: 54.0% overall correctness pass vs. 38.7% for GPT-6 Astra with web search (40% relative); 24% more reference cases on case-law questions; up to 54% more relevant passages at equal effort
- Side-by-side examples: Claude Fable 5.1 returned a holding reversed on appeal (litigation) and found no case (transactional); Astra for Law returned two closely matching precedents
- Access: selected law firms via Trusted Access in ChatGPT and Codex ("GPT-6 Astra Law"); API `gpt-6-astra-law` coming soon
- Controls: ZDR on the API for eligible firms; ChatGPT Enterprise excluded from human review by default; Latham & Watkins collaboration on permissions, ethical walls, client instructions, oversight
- FDE-built firm tools: Sullivan & Cromwell agreement analyzer, Ropes & Gray deal diligence system, Cooley GO Public; Skadden and Wachtell named
- 26 partner plugins (iManage, Intapp, DeepJudge, Relativity, Clio; Thomson Reuters HighQ and a forthcoming CoCounsel Legal connector); 9 community plugins with 47 skills (LegalQuants, LECG, Skills.law); ChatGPT for Word generally available
