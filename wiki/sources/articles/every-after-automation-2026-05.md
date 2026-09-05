---
title: '"After Automation" — Dan Shipper (Every)'
type: source
source_type: article
source_file: raw/articles/2026-08-25-everyto-p-after-automation.md
url: https://every.to/p/after-automation
published: 2026-05-21
ingested: 2026-08-25
domains: [training, agents]
---

# "After Automation" — Dan Shipper (Every)

Every CEO Dan Shipper argues AI progress increases, not decreases, demand for human expert work. Core mechanism: models commoditize the "residue" of past human competence; that cheap competence gets rapidly adopted and produces "sameness" (slop); sameness creates demand for differentiated, human-judgment-driven work; and — because "the frame is not the framer" — this repeats even under a strong operational definition of AGI, since a human always supplies the goal a model optimizes toward. The essay grounds this in Every's own internal evidence: the "Senior Engineer benchmark" (GPT-5.5 scores 62/100, about 30 points above Opus 4.7, still roughly 30 points below human senior engineers), the "human sandwich" pattern (human frames the task, agent executes, human judges and extends), named coworker agents (Claudie, Andy, Viktor) versus embedded agents (Fin, which closed 40.1% of actionable customer-service conversations without a human in a recent week), and a critique of "chart psychosis" — reading benchmark trend lines as proof of imminent job replacement without accounting for how the benchmark is framed.

## Influenced pages
- [Agent evals](../../concepts/agent-evals.md) — added the benchmark-framing / "chart psychosis" critique section
- [AI work delegation modes](../../training/ai-work-delegation-modes.md) — added the agent-employee taxonomy (coworker/embedded) and human-sandwich pattern as concrete evidence, plus a personal-agent-staleness failure mode

## Key claims extracted
- GPT-5.5 scores 62/100 on Every's in-house Senior Engineer benchmark, ~30 points above Claude Opus 4.7; human senior engineers score in the high 80s to low 90s
- Fin (the agent embedded in Every's customer-service platform) closed 40.1% of actionable support conversations without a human in a recent week in May (participated in 65% of 202 conversations, closing 81)
- Every's "agent employees" come in two flavors: coworker agents you tag and ask for work (Claudie for consulting, Andy for editorial, Viktor general-purpose) and embedded agents living inside a product workflow (Fin)
- Human-agent collaboration in Codex, Claude Code, and Claude Cowork follows the "human sandwich" (Kieran Klaassen's term): a human sets the frame, the agent collapses the task, a human judges and extends the result
- Every gave every employee a personal agent, then moved back to team- or company-owned agents because personal agents need heavy maintenance and went stale once their owners gave up on them; a dedicated AI-engineering team keeps agents working
- OpenClaw's GitHub repo had 44,469 pull requests by May 16, 2026 (12,430 since April 1), versus Kubernetes' 5,200 PRs in all of 2022
- One of Every's PowerPoint-generation automations needs 24 skills and 18 scripts, and costs $62 in tokens per deck
- Senior Engineer benchmark scores are prompt-sensitive: removing the "structural rewrite" / "document collaboration" / "invariants" hints lowers the score, and replacing the prompt with "solve all of the errors that keep popping up" drops it to near zero; giving exact filenames to delete or asking for self-verification raises it
- GDPval tasks embed "smuggled intelligence": the prompt already supplies the expert framing (which sample-size formula, confidence level, risk-weighted entities, output format), so the benchmark measures work inside an expert-framed problem, not the framing itself
- Argues benchmarks measure performance "inside a frame"; saturating a frame shifts demand to the next frame rather than eliminating expert work — a pattern the essay argues holds even under strong AGI ("the frame is not the framer")
