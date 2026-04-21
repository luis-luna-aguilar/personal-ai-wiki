# Wiki Log

Chronological append-only record of wiki activity. Entries start with:

```
## [YYYY-MM-DD] <op> | <subject> | <summary>
```

Valid ops: `ingest`, `triage`, `reject`, `apply`, `lint`, `query-verify`, `schema`.

To see the most recent activity:

```bash
grep "^## \[" wiki/log.md | tail -20
```

---

## [2026-04-09] schema | wiki bootstrap | initial scaffold created (CLAUDE.md, config.yml, _schema/, state-of placeholders, scripts/, manual/)

## [2026-04-09] schema | added subcategory `spec-driven-development`; added tags `github`, `open-source`, `cli`, `beta`, `spec-driven`

## [2026-04-09] ingest | Fowler — Understanding SDD (Kiro, spec-kit, Tessl) | 1 page updated, 5 created (state-of/coding updated; concepts/spec-driven-development, tools/kiro, tools/spec-kit, tools/tessl, sources/articles/sdd-3-tools-fowler created)

## [2026-04-09] schema | added subcategories `agentic-coding-workspace`, `agent-orchestration-ui`, `coding-model`; added tags `closed-source`, `agentic`

## [2026-04-09] ingest | Cursor 3 launch — "Meet the new Cursor" | 2 pages updated, 3 created (state-of/coding, state-of/agents updated; tools/cursor, models/composer-2, sources/articles/cursor-3-launch created)

## [2026-04-09] schema | added domain `legal`; added subcategory `legal-ai`

## [2026-04-09] ingest | Harvey — "Legal is Next" (Pereyra) | 0 pages updated, 4 created (state-of/legal, tools/harvey, trends/agents-reshape-organizations, sources/articles/harvey-legal-is-next created); manual updated (proposals-workflow.html); DEFERRED.md appended (readability extraction bug)

## [2026-04-09] apply | fetch_url.py readability fallback | DEFERRED.md item resolved: length-based fallback to body.innerText wired through fetch_with_playwright → html_to_markdown → main; also fixed latent arg-count bug in the call site

## [2026-04-09] schema | added subcategory `model-orchestration`; added tag `anthropic`

## [2026-04-09] ingest | Anthropic — "The advisor strategy" | 2 pages updated, 2 created (state-of/agents, wiki/index updated; workflows/advisor-strategy, sources/articles/advisor-strategy created)

## [2026-04-09] schema | added subcategory `agentic-devops`

## [2026-04-09] ingest | Stripe CLI `projects` developer preview | 3 pages updated, 2 created (state-of/coding, state-of/agents, wiki/index updated; tools/stripe-cli, sources/articles/stripe-cli created)

## [2026-04-10] ingest | LangChain — "The Agent Improvement Loop Starts with a Trace" | 1 page updated, 2 created (wiki/index updated; concepts/agent-improvement-loop, sources/articles/trace-agent-improvement-loop created)

## [2026-04-10] schema | added subcategory `agent-orchestration`

## [2026-04-10] ingest | Anthropic — "Scaling Managed Agents: Decoupling the brain from the hands" | 2 pages updated, 2 created (state-of/agents, wiki/index updated; tools/claude-managed-agents, sources/articles/managed-agents created)

## [2026-04-10] apply | source-date normalization | LLM-INSTRUCTIONS updated to prefer source publication date over ingest date for `as_of`; Harvey-derived pages backdated from 2026-04-09 to 2026-04-02 and source summary now records `published`

## [2026-04-10] apply | source-date normalization (user-supplied dates) | Cursor-derived pages backdated to 2026-04-02; Fowler SDD-derived pages backdated to 2025-10-15; Managed Agents-derived pages backdated to 2026-04-09; source summaries now record `published`

## [2026-04-10] ingest | Anthropic — "Emotion concepts and their function in a large language model" | 1 page updated, 2 created (wiki/index updated; concepts/functional-emotions, sources/articles/emotion-concepts-function created)

## [2026-04-10] triage | Superhuman AI 2026-04-10 | 3 proposals (Perplexity Computer, Gemini visualizations, AI in science), 6 skipped

## [2026-04-10] schema | added domains `computer-use`, `finance`, `science`; added subcategories `computer-use`, `ai-assistant`; added tags `perplexity`, `google`

## [2026-04-10] apply | Perplexity Computer — Plaid integrations | 2 pages updated (state-of/computer-use created, wiki/index), 3 created (tools/perplexity-computer, state-of/finance, sources/articles/perplexity-computer-plaid); enriched via web research

## [2026-04-10] apply | Gemini visualizations & notebooks | 2 pages updated (state-of/models, wiki/index), 1 created (tools/gemini)

## [2026-04-10] apply | AI in Science trend | 1 page updated (wiki/index), 2 created (trends/ai-in-science, state-of/science)

## [2026-04-10] triage | The Code Newsletter 2026-04-10 | 5 proposals generated, 8 skipped

## [2026-04-10] apply | Claude Code Monitor tool | 2 pages updated (state-of/coding, wiki/index), 2 created (tools/claude-code, sources/articles/claude-code-monitor); new subcategory terminal-coding-agent

## [2026-04-10] apply | Cursor PR demos | 1 page updated (tools/cursor), 1 created (sources/articles/cursor-pr-demos)

## [2026-04-10] apply | OpenAI $100/mo Pro plan | 2 pages updated (state-of/coding, wiki/index), 2 created (tools/codex, sources/articles/openai-pro-100)

## [2026-04-10] apply | Agentic thinking (Junyang Lin) | 2 pages updated (state-of/agents, trends/agents-reshape-organizations), 2 created (concepts/agentic-thinking, sources/articles/agentic-thinking-lin)

## [2026-04-10] apply | LangChain Better-Harness | 1 page updated (concepts/agent-improvement-loop), 1 created (sources/articles/langchain-better-harness)

## [2026-04-10] schema | added subcategory terminal-coding-agent, tag openai

## [2026-04-10] apply | Harness concept | 1 page updated (wiki/index), 1 created (concepts/harness)

## [2026-04-10] ingest | Every / Playtesting — "The Market for Making AI Better" | 1 page updated, 2 created (wiki/index updated; trends/proprietary-data-becomes-model-moat, sources/articles/market-for-making-ai-better created)

## [2026-04-10] apply | tool-page concision guidance | LLM-INSTRUCTIONS updated so routine tool/model/workflow ingests default to shorter pages and fewer repeated sections

## [2026-04-10] schema | added subcategory `agent-toolkits`

## [2026-04-10] ingest | Shopify AI Toolkit | 2 pages updated, 2 created (state-of/coding, wiki/index updated; tools/shopify-ai-toolkit, sources/articles/shopify-ai-toolkit created)

## [2026-04-10] schema | added page type `training` | new `wiki/training/` and `wiki/history/training/` directories; LLM-INSTRUCTIONS, config.yml, source-type guidance, and wiki/index updated to support training pages for organizational AI enablement

## [2026-04-10] ingest | Ramp AI adoption playbook | 2 pages updated, 2 created (wiki/trends/agents-reshape-organizations, wiki/index updated; wiki/training/company-wide-ai-enablement, wiki/sources/articles/ramp-ai-adoption-playbook created); personal/takes/test-backlog appended with customer PR backlog item

## [2026-04-10] triage | The Code Newsletter — Managed Agents / Muse Spark | 3 proposals generated (Muse Spark, Cursor Bugbot learned rules, Postman AI-org-chart signal), 4 skipped

## [2026-04-15] apply | Cursor Bugbot learned rules | 3 pages updated (tools/cursor, concepts/agent-improvement-loop, state-of/coding), 1 created (sources/articles/cursor-bugbot-learning); index updated

## [2026-04-15] schema | added subcategory `frontier-multimodal-model`

## [2026-04-15] ingest | Muse Spark | 2 pages updated, 2 created (state-of/models, wiki/index updated; models/muse-spark, sources/articles/muse-spark created)

## [2026-04-15] ingest | Postman AI-era org-chart signal | 1 page updated, 1 created (trends/agents-reshape-organizations updated; sources/tweets/postman-ai-org-chart created)

## [2026-04-15] ingest | Curiosity-Driven Imagination paper | 3 pages updated, 2 created

## [2026-04-16] triage | The Code 2026-04-16 | 1 proposals, 5 skipped
## [2026-04-16] ingest | OpenAI — "The next evolution of the Agents SDK" | 3 pages updated, 2 created

## [2026-04-21] triage | AI digest 2026-04-20 to 2026-04-21 | 8 proposals generated, 2 skipped (Google DeepMind strike team, Qwen3.6-Max-Preview)
## [2026-04-21] ingest | McKinsey — "AI is Everywhere. The Agentic Organization Isn't Yet." | 2 pages updated, 1 created
## [2026-04-21] ingest | LeWorldModel (LeWM) — Stable End-to-End JEPA from Pixels | 1 page updated, 2 created
## [2026-04-21] apply | Kimi K2.6 | 2 pages updated (state-of/models, wiki/index), 3 created (models/kimi-k2-6, sources/articles/kimi-k2-6-blog, sources/newsletters/ainews-2026-04-21); added tags `moonshot-ai`, `open-weights`; clarified state-of leader replacement rules in LLM-INSTRUCTIONS
## [2026-04-21] apply | Codex Chronicle | 2 pages updated (tools/codex, trends/proprietary-data-becomes-model-moat); reused existing source summary `sources/newsletters/ainews-2026-04-21`
## [2026-04-21] apply | Hermes Agent | 2 pages updated (state-of/agents, wiki/index), 1 created (tools/hermes-agent); reused existing source summary `sources/newsletters/ainews-2026-04-21`
## [2026-04-21] apply | Claude Opus 4.7 | 2 pages updated (state-of/models, wiki/index), 1 created (models/claude-opus-4-7); reused existing source summary `sources/newsletters/ainews-2026-04-21`
## [2026-04-21] apply | Claude Cowork | 2 pages updated (state-of/agents, wiki/index), 3 created (tools/claude-cowork, sources/articles/claude-cowork-launch, sources/tweets/aakash-gupta-cowork); applied without adding a new subcategory per proposal comments
## [2026-04-21] triage | Personal digest 2026-04-15 to 2026-04-21 | 9 proposals generated, 1 skipped
## [2026-04-21] apply | Anthropic/AWS compute infrastructure | 2 pages updated (state-of/models, wiki/index), 1 created (trends/compute-infrastructure); reused existing source summary `sources/newsletters/ainews-2026-04-21`
## [2026-04-21] ingest | Every Mini-Vibe Check on Claude Managed Agents | 3 pages updated, 1 created
## [2026-04-21] ingest | Qwen 3.6 35B-A3B crosses into practical local-agent territory | 2 pages updated, 2 created
## [2026-04-21] ingest | Knowledge layer | 1 page updated, 2 created
## [2026-04-21] ingest | Gemini browser and utility updates | 2 pages updated, 1 created
## [2026-04-21] apply | Gemini Deep Research and Deep Research Max | 1 page updated (tools/gemini), 1 created (sources/articles/gemini-deep-research-max)
## [2026-04-21] ingest | Claude Opus 4.7 — capability gains with reliability tradeoffs | 3 pages updated, 2 created
## [2026-04-21] ingest | Claude Design and live artifacts expand Anthropic beyond chat | 4 pages updated, 2 created
## [2026-04-21] ingest | AI in biology — Noetik and GPT-Rosalind | 3 pages updated, 2 created
## [2026-04-21] ingest | Every — We Need to Talk About AI Autopilot | 2 pages updated, 4 created
## [2026-04-21] ingest | Agentic orchestration patterns | 2 pages updated, 5 created; added subcategory `agentic-orchestration-patterns`
## [2026-04-21] ingest | Agentic coding UIs converge on supervision, not editing | 4 pages updated, 2 created
## [2026-04-21] apply | Orca | 3 pages updated (state-of/coding, state-of/agents, wiki/index), 2 created (tools/orca, sources/articles/orca-homepage)

## [2026-04-21] triage | Personal digest 2026-04-08 to 2026-04-14 | 7 proposals generated, 1 skipped
## [2026-04-21] apply | Anthropic platform expansion | 2 pages updated (tools/claude-managed-agents, state-of/agents), 1 created (sources/newsletters/anthropic-platform-expansion-april-2026); clarified Anthropic custom agents/productivity-surface context
## [2026-04-21] apply | Coding agent control planes | 4 pages updated (tools/cursor, state-of/coding, state-of/agents, wiki/index), 1 created (sources/newsletters/coding-agent-control-planes)
## [2026-04-21] apply | Harness engineering patterns | 2 pages updated (concepts/harness, workflows/agentic-orchestration-patterns), 1 created (sources/newsletters/harness-engineering-patterns)
## [2026-04-21] apply | AI adoption is management | 2 pages updated (training/company-wide-ai-enablement, trends/agents-reshape-organizations), 1 created (sources/newsletters/ai-adoption-is-management)
## [2026-04-21] apply | Open agentic coding models | 2 pages updated (state-of/models, wiki/index), 3 created (models/glm-5-1, models/minimax-m2-7, sources/newsletters/open-agentic-coding-models)
## [2026-04-21] apply | Restricted frontier deployment | 1 page updated (state-of/models), 2 created (trends/restricted-frontier-deployment, sources/newsletters/restricted-frontier-deployment)
## [2026-04-21] apply | Claude productivity surfaces | 3 pages updated (tools/claude-cowork, state-of/agents, tools/claude-managed-agents), 1 created (sources/tweets/claude-productivity-surfaces)
## [2026-04-21] triage | Personal digest 2026-04-01 to 2026-04-07 | 5 proposals generated, 3 skipped
## [2026-04-21] apply | Claude Code leak architecture lessons | 3 pages updated (tools/claude-code, concepts/harness, state-of/coding), 1 created (sources/newsletters/claude-code-leak-architecture)
## [2026-04-21] apply | Cursor 3 orchestration bet | 2 pages updated (tools/cursor, state-of/coding), 1 created (sources/newsletters/cursor-3-orchestration-bet)
## [2026-04-21] apply | Harness engineering in early April | 2 pages updated (concepts/harness, workflows/agentic-orchestration-patterns), 1 created (sources/newsletters/harness-engineering-early-april)
## [2026-04-21] apply | Agent-native organizations in early April | 2 pages updated (training/company-wide-ai-enablement, trends/agents-reshape-organizations), 1 created (sources/newsletters/agent-native-organizations-early-april)
## [2026-04-21] apply | Open-weight momentum in early April | 3 pages updated (state-of/models, state-of/computer-use, wiki/index), 2 created (trends/open-weight-momentum-broadens, sources/newsletters/open-weight-momentum-early-april)
## [2026-04-21] triage | Personal digest 2026-03-24 to 2026-03-31 | 6 proposals generated, 1 skipped
## [2026-04-21] apply | Claude computer use in late March | 2 pages updated (state-of/computer-use, tools/claude-code), 1 created (sources/newsletters/claude-computer-use-late-march)
## [2026-04-21] apply | Agent coworkers as an operating pattern | 2 pages updated (training/company-wide-ai-enablement, trends/agents-reshape-organizations), 1 created (sources/newsletters/agent-coworkers-operating-pattern)
## [2026-04-21] apply | Open-agent orchestration in late March | 2 pages updated (workflows/agentic-orchestration-patterns, state-of/agents), 1 created (sources/newsletters/open-agent-orchestration-late-march)
## [2026-04-21] apply | Voice becomes an agent interface | 1 page updated (wiki/index), 2 created (trends/voice-becomes-agent-interface, sources/newsletters/voice-becomes-agent-interface)
## [2026-04-21] apply | Runtime improvements improve agent economics | 1 page updated (trends/compute-infrastructure), 1 created (sources/newsletters/runtime-improvements-improve-agent-economics)
## [2026-04-21] apply | AI-native product-building lessons in late March | 1 page updated (training/company-wide-ai-enablement), 1 created (sources/newsletters/ai-native-product-building-lessons-late-march)
