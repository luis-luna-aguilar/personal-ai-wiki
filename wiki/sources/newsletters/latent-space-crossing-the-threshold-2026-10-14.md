---
title: "Latent Space — Crossing the Threshold: How OpenAI and Anthropic Approach Autonomy and Safety in Financial Agents"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-14-crossing-the-threshold-how-openai-and-anthropic-a.md
url: https://www.latent.space/p/crossing-the-threshold
published: 2026-10-14
ingested: 2026-10-20
domains: [finance, agents]
---

# Latent Space — Crossing the Threshold: autonomy and safety in financial agents

Write-up of the AI Engineer New York finance keynotes from OpenAI, Two Sigma, Anthropic, and Bloomberg. Central thesis: safe agent autonomy depends on where controls and human judgment are placed, not on how many restrictions are imposed.

## Influenced pages

- [Agent autonomy and governance](../../training/agent-autonomy-and-governance.md) — "Place controls where they enable autonomy" subsection
- [State of Finance](../../state-of/finance.md) — ChatGPT for Financial Services and Claude for Financial Advisors lines

## Key claims extracted

- OpenAI (Joseph Kim, Head of ChatGPT for Financial Services): "threshold of usefulness" where a model becomes reliable enough to save time; predicts 2027 agents doing investment idea generation and trading and less reliance on Excel/PowerPoint; traceability built into review; HITL is a product-design question
- Two Sigma (John Feminella, SVP Architecture): five composable controls; "approval fatigue" holds back innovation and adds risk; auto-mode classifiers handle routine calls and escalate important ones; deterministic rules for clear cases; "brakes let you go fast and stop safely"
- Anthropic (Belinda Neal, Keon Shahab): Claude for Financial Advisors announced the prior month; trust layer = identity/permissions, sandbox plus approval layer, stability as variables change; trade-break agent proposes order amendments, never makes them
- Bloomberg (Andrey Rybka): real agent incidents, including prompt injection via a marketplace review that led an agent to stock a product; defenses: scoped identities and credentials, tool-call controls, outbound traffic limits, audit trails, budgets, kill switches, input validation, provenance tracking, human approval for high-value actions; "deterministic controls outside the model"
