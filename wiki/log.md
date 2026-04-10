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
