---
title: 'Is Bash All You Need? An Empirical Study of Tool Interfaces for Enterprise Digital Worker Agents'
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-html-260911999.md
url: https://arxiv.org/abs/2609.11999
published: 2026-09-10
ingested: 2026-11-24
domains: [agents]
---

# Is Bash All You Need? (Microsoft)

**The everyday question.** When you build an office-work agent, do you give it a neat catalog of typed tools ("send_email", "read_spreadsheet"), or a shell and let it script? Typed tools feel safer and easier to govern. Shells are what coding agents use, but office work also means jumping between apps, messaging coworkers and analysing documents.

**What the authors did.** Six Microsoft researchers ran Opus 4.8 and GPT-5.5 at default reasoning on TheAgentCompany (a simulated company with coworkers and internal apps) and APEX-Agents (professional analysis over documents). They compared five interfaces: typed tools only; typed tools plus bash; bash only; bash plus tools the agent writes and keeps for later tasks; and programmatic tool calling (PTC), where the agent writes a program but every action must go through the typed catalog.

**What they found.**
- Bash only beat typed tools only on both benchmarks: +21.8 to +24.5 points on TheAgentCompany and +4.8 to +7.4 on APEX-Agents, using 19–72% fewer total tokens. On TheAgentCompany with Opus 4.8, for example, the score rose from 44.9% to 69.4% and the estimated cost per task fell from $1.20 to $0.37.
- Adding typed tools or agent-synthesized tools on top of bash gave no detectable pooled gain and usually cost more tokens. Agents used most tools they created, but fewer of those tools reached later tasks.
- PTC used fewer tokens than direct typed calls at broadly similar scores, but generally trailed bash on quality and cost.
- The models differed. Opus 4.8 did best shell-only on coding-like and cross-app work, while GPT-5.5 was the token-efficient choice for direct typed calls. The authors warn these model recommendations may not carry over to later releases.

**Practical translation.** Default to a shell inside a sandbox. Reach for a fixed, typed catalog (ideally called from code, PTC-style) only when security or compliance demands that the agent can do nothing outside a known list.

## Influenced pages
- [Harness vs model](../../concepts/harness-vs-model.md) — new "Tool surface: bash vs typed tools" subsection

## Key claims extracted
- Five interfaces compared on TheAgentCompany and APEX-Agents with Opus 4.8 and GPT-5.5
- Bash alone vs typed tools: +21.8–24.5 pp (TheAgentCompany), +4.8–7.4 pp (APEX-Agents), 19–72% fewer tokens
- Typed tools or persistent synthesized tools added to bash: no detectable pooled score gain
- PTC: fewer tokens than direct typed calls, similar scores, generally below bash on quality and cost efficiency
- Recommendation: bash when arbitrary execution can be isolated; PTC when policy requires a fixed tool catalog
