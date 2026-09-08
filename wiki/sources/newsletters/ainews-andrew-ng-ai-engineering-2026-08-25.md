---
title: "AINews — Andrew Ng gets into AI Engineering"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-25-ainews-andrew-ng-gets-into-ai-engineering.md
url: https://www.latent.space/p/ainews-andrew-ng-gets-into-ai-engineering
published: 2026-08-25
ingested: 2026-09-07
domains: [agents, training]
---

# AINews — Andrew Ng gets into AI Engineering

AINews issue leading with Andrew Ng's DeepLearning.AI relaunch around four "AI Engineering" skills, plus a Twitter/Reddit recap covering harness-design research (NVIDIA's Skill Lift metric, Headlong, exo, single-harness standardization), Anthropic's enterprise-managed MCP auth, continued Qwen3.8-27B momentum, and cost-normalized agent benchmarks (GLM-5.3 vs. Fable, Sol Max vs. Fable Max, Cline's Ox Alpha token-efficiency comparison).

## Influenced pages

- [Harness (agent)](../../concepts/harness.md) — Skill Lift, Headlong/exo, single-harness standardization, enterprise MCP auth bullets
- [AI Engineering skills](../../training/ai-engineering-skills.md) — new page, primary source for the Andrew Ng skills taxonomy
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — cost-normalized DeepSWE/Cline benchmark evidence

## Key claims extracted

- Andrew Ng relaunches DeepLearning.AI around four AI Engineering skills, based on 10,000+ job postings plus hiring-manager/recruiter interviews
- NVIDIA: structural skill checks correlate with judged usefulness at only Spearman ρ=0.14; proposes "Skill Lift" (task-completion delta with/without a skill) instead
- Headlong: open-source persistent/continuously-thinking agent harness; DAG-based trajectory storage; 48-minute unattended self-debugging repair reported; $1-2/hr background-thinking cost
- exo: harness for recursive self-improvement with an append-only event log and rollback-safe sandbox
- Anthropic enterprise-managed auth for MCP connectors (Asana, Atlassian, Canva, Datadog, Figma, Notion, Slack, Supabase), centralized via org identity provider
- Qwen3.8-27B: #9 on Code Arena: WebDev (1595 points), only model in its size class in the top 10
- Cost-normalized benchmarks: GLM-5.3 completes 5x more DeepSWE work than Fable 5 per fixed $100 budget; GPT-5.6 Sol Max 72.7% on DeepSWE v1.1 for $6.47/task vs. Fable 5 Max 69.7% for $21.63/task; Cline's Ox Alpha solved a bugfix using ~3x fewer output tokens than Fable
