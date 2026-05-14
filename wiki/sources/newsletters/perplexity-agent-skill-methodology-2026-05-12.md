---
title: Perplexity agent skill methodology — evals-first, principles over procedures
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-12-the-fallacy-of-the-16-hour-agent.md
published: 2026-05-12
ingested: 2026-05-13
domains: [agents]
---

# Perplexity agent skill methodology — evals-first, principles over procedures

Newsletter "The Fallacy of the 16-Hour Agent" (May 12) covers Perplexity's published methodology alongside the METR benchmark analysis. Primary URL: https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity

## Influenced pages

- [Agent skill methodology](../../training/agent-skill-methodology.md) — new training page created

## Key claims extracted

- Write 5-10 test cases before writing the skill, including negative examples: queries that must not trigger the skill.
- Phrase triggers in natural user language, not technical phrases or internal workflow names.
- Write the skill body as principles and direction, not step-by-step procedures.
- When the agent fails in production, codify the failure as a standing instruction in the skill file.
- After review, cut every line the agent would get right without it to reduce noise and improve diagnosability.
- Source: Perplexity internal production methodology, published as a research article.
- Context in newsletter: cited alongside METR benchmark data as an example of the "reliability is engineered, not assumed" theme.
