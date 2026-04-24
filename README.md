# AI Wiki

A personal knowledge base that tracks the fast-moving AI landscape: models, tools, benchmarks, workflows, concepts, trends, and training guidance. Content is curated by a human and maintained by an LLM agent that reads sources, files updates, and keeps cross-references current.

## How it works

Sources are dropped into `raw/` and ingested via an LLM agent (Claude Code or Codex). The agent never writes to `wiki/` directly — it first proposes changes to `proposals/`, which the human reviews and approves. Once approved, the wiki is updated.

## Folder structure

```
raw/                   # Immutable source material — articles, tweets, papers,
│                      # podcasts, newsletters, meeting notes, deep-research
│  articles/
│  tweets/
│  papers/
│  podcasts/
│  newsletters/
│  deep-research/
│  meetings/
│  notes/
│  assets/             # Images (Obsidian Web Clipper / fetch_url.py)
│  repos/

wiki/                  # Current state of the knowledge base
│  index.md            # Catalog of all wiki pages — start here
│  log.md              # Append-only chronological change log
│  state-of/           # Domain dashboards (agents, models, tools, etc.)
│  models/             # One page per foundation model
│  tools/              # One page per AI tool or product
│  benchmarks/         # Benchmark pages with leaderboards
│  workflows/          # Reusable patterns and recipes
│  concepts/           # Ideas (RAG, context engineering, MCP, etc.)
│  trends/             # Things being watched
│  training/           # Guidance for teaching teams to use AI well
│  sources/            # Lightweight summary page per ingested source
│  history/            # Archived older versions (mirrors wiki/ structure)
│  _schema/            # Controlled vocabulary files

proposals/             # Pending wiki changes, awaiting human approval
│  triage/             # Newsletter triage drafts
│  applied/            # Already-approved proposals (moved here after merge)
│  rejected/           # Proposals that were reviewed and declined

personal/              # Personal notes — structure tracked, content private
│  philosophies/       # Long-form thinking and principles
│  takes/              # Short opinions and reactions

scripts/               # Python maintenance utilities
│  fetch_url.py        # Fetch and clip a URL into raw/
│  gmail_fetch.py      # Pull newsletters from Gmail
│  lint_all.py         # Schema and frontmatter linting
│  stale.py            # Flag pages with old as_of dates
│  orphans.py          # Find wiki pages not referenced in index.md

manual/                # User-facing HTML documentation

personal-wiki-agent/   # Python agent that provides CLI and MCP access

podcast/               # AI-generated podcast scripts built from wiki content for NotebookLM

research-requests/     # Deep-research prompts generated from the information gaps in the wiki

skills/                # Skill definitions for wiki workflows
```

## Key files

| File | Purpose |
|------|---------|
| `LLM-INSTRUCTIONS.md` | Operating rules for the LLM agent — single source of truth |
| `CLAUDE.md` | Points the Claude Code CLI to `LLM-INSTRUCTIONS.md` |
| `AGENTS.md` | Instructions for other AI agents (OpenAI Codex, etc.) |
| `wiki/index.md` | Catalog of every wiki page — read this before querying |
| `wiki/log.md` | Chronological record of all changes |
| `config.yml` | Wiki-wide configuration |

## Personal folder

The `personal/` directory is tracked in git so contributors can keep the same structure for their own notes, but its contents are gitignored. Add your own files freely — they will never be committed.

## LLM agent rules (summary)

- **Dry-run by default.** All wiki changes go to `proposals/` first.
- **Dates are load-bearing.** Every wiki claim carries an `as_of` date.
- **Source date beats ingest date.** Use the publication date from the source, not the date it was added.
- **Reuse over fragmentation.** Most sources update existing pages; new pages are rare.
- **Current state first.** History is kept but not loaded unless explicitly requested.

Full rules in [`LLM-INSTRUCTIONS.md`](./LLM-INSTRUCTIONS.md).
