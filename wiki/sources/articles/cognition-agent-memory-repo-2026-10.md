---
title: Cognition — Agent Memory Repo
type: source
source_type: article
source_file: raw/articles/2026-10-20-cognitioncom-agent-memory-repo.md
url: https://cognition.com/agent-memory-repo
ingested: 2026-10-20
domains: [agents]
---

# Cognition — Agent Memory Repo

Cognition's page for Agent Memory Repo, the open git-and-markdown format behind Devin's memory. The page carries no date; AINews reported the launch on 6 October 2026. It explains the format through one worked example: four agents investigating why 1 checkout request in 100 takes 2.4 s share a swarm folder inside the user's memory repo (README with goal and rules, `findings.md`, `questions.md`, one notes file per agent, one shared benchmark script). Each finding is one line with a link to the session that produced it. The shared questions file connects three separate symptoms into one cause, git handles concurrent writes, and the finished swarm folder is linked from `MEMORY.md` for later sessions to reuse.

## Influenced pages

- [Agent memory](../../concepts/agent-memory.md) — new Current-status bullet
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — Agent memory row example
- [Knowledge term map](../../concepts/knowledge-term-map.md) — "memory repo" term-map row
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — memory-repo swarm-workspace pattern
- [Devin](../../tools/devin.md) — Memory subsection

## Key claims extracted

- Memory repo layout: `MEMORY.md` with an `## Index`, topic files (team structure, projects), and a `swarms/` folder with one subfolder per swarm
- Swarm folder: `README.md` (goal and rules), `findings.md`, `questions.md`, `agents/<name>.md` per agent, `scripts/bench.sh` as the one shared benchmark
- Rules in the example README: measure only with the shared script; pull and read findings and questions before each step; record what you rule out; ask when another agent's area might explain what you see
- Every entry is one line ending in `[source: <session link>]`; files cross-link with wiki-style double-bracket links
- Worked example: price-cache refresh rebuilds a ~2 GB table every 10 s → ~400 ms GC freeze → queued requests exhaust a 20-connection pool; fix (refresh only changed prices) takes the slowest 1% from 2.4 s to 310 ms
- Git merges most concurrent commits; when two agents edit the same line the second push is rejected and that agent reads both versions before writing
- The finished swarm folder stays in the repo and is indexed in `MEMORY.md`; later sessions follow the link and reuse the benchmark
