---
title: OpenWiki
type: tool
domains: [agents, coding]
subcategory: knowledge-platform
tags: [open-source, agentic, knowledge-cluster]
as_of: 2026-07-02
sources: [ainews-not-much-happened-2026-07-02, the-code-devin-security-2026-07-02]
---

# OpenWiki

OpenWiki is a LangChain tool for generating and maintaining agent-consumable documentation for a codebase. It fits the emerging "wiki memory" pattern: agents need maintained, inspectable knowledge layers rather than only raw transcripts or retrieval over stale files. In the [Knowledge architectures](../concepts/knowledge-architectures.md) matrix it is a team-scope [knowledge layer](../concepts/knowledge-layer.md) for one codebase.

## Current status (as of 2026-07-02)

- AINews reports launch usage around `openwiki --init`.
- The Code frames it as a CLI that writes and maintains codebase documentation for agents.
- The tool is relevant to teams trying to make codebase context durable across threads and agents.

## Strengths

- Gives agents a structured codebase map that can be inspected and updated.
- Aligns with wiki-style memory rather than opaque vector-only recall.

## Weaknesses / caveats

- Current evidence is newsletter coverage; fetch the repository before applying detailed command or architecture claims.

## Recent changes

- [2026-09-09] Re-filed from `agent-toolkits` to the new `knowledge-platform` subcategory as part of the knowledge-cluster terminology reorganization; no product change.
- [2026-07-02] LangChain launched OpenWiki as an agent-readable codebase documentation tool.

## Related

- [Knowledge layer](../concepts/knowledge-layer.md) — the concept this tool implements for codebases

## Sources

- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [The Code - Cognition ships Devin for Security](../sources/newsletters/the-code-devin-security-2026-07-02.md)
