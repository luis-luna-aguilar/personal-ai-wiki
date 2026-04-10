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
