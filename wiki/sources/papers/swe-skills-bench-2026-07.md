---
title: "SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?"
type: source
source_type: paper
source_file: raw/papers/2026-09-06-arxivorg-abs-260315401.md
url: https://arxiv.org/abs/2603.15401
published: 2026-03-16
ingested: 2026-09-06
domains: [agents]
---

# SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?

Han, Zhang, Song, Fang, Chen, Sun, and Hu (submitted 16 March 2026). The first requirement-driven benchmark isolating the marginal utility of agent skills in real software engineering: 49 public SWE skills paired with authentic GitHub repos pinned to fixed commits and requirement documents with explicit acceptance criteria, yielding ~565 task instances across six SE subdomains, scored by a deterministic execution-based verification framework (paired with/without-skill comparison).

## Influenced pages

- [Training — Agent skill methodology](../../training/agent-skill-methodology.md) — cited as a second, independent skills benchmark alongside SkillsBench

## Key claims extracted

- 39 of 49 skills yield zero pass-rate improvement; average gain across all 49 is only +1.2%
- Token overhead ranges from modest savings to +451%, independent of pass-rate change
- 7 skills produce meaningful gains (up to +30%) — all supplying specialized, otherwise-unavailable domain knowledge
- 3 skills degrade performance (up to -10%) due to version-mismatched guidance conflicting with the project's actual code
