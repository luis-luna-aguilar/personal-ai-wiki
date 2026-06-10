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

agents/               # Python agents, MCP server, and ontology compiler

podcast/               # AI-generated podcast scripts built from wiki content for NotebookLM

research-requests/     # Deep-research prompts generated from the information gaps in the wiki

skills/                # Skill definitions for wiki workflows
```

## Key files

| File | Purpose |
|------|---------|
| `AGENTS.md` | Operating rules for the LLM agent — single source of truth (read natively by Codex and other agents) |
| `CLAUDE.md` | Symlink to `AGENTS.md` so Claude Code loads the same rules |
| `wiki/index.md` | Catalog of every wiki page — read this before querying |
| `wiki/log.md` | Chronological record of all changes |
| `config.yml` | Wiki-wide configuration |

## Settings

All tunable behavior lives in [`config.yml`](./config.yml). Edit values there — nothing is hard-coded outside these keys. The main sections:

| Section | Purpose |
|---------|---------|
| `stale_thresholds_days` | Per-type age (in days) after which a page is considered stale; also drives query-time confidence bands. |
| `query.confidence_bands` | Ratios that map page age to `high` / `medium` / `stale` confidence in answers. |
| `history.recent_changes_cap` | Max "Recent changes" bullets a page keeps before the oldest spills to `wiki/history/`. |
| `stale` | Which directories the staleness scan includes/excludes. |
| `orphans` | Which paths the orphan check scans, and which are exempt. |
| `source_types` | Per-source-type ingest playbooks (raw dir, ingest style, notes). |
| `fetch_url` | URL fetching via `scripts/fetch_url.py` — see below. |
| `log_file` | Location of the append-only change log. |
| `gmail` | Account list, scopes, sender whitelist, and Email Me forward detection for `scripts/gmail_fetch.py`. |

### `fetch_url`

| Key | Default | Purpose |
|-----|---------|---------|
| `profile_dir` | `~/.cache/ai-wiki-playwright` | Persistent Chromium profile so logged-in/paywalled sites keep working across runs. |
| `timeout` | `30` | Page-load timeout in seconds. |
| `wait_for` | `networkidle` | Playwright wait strategy before extraction. |
| `coverage_min_ratio` | `0.5` | Truncation guard: if readability's extracted text covers less than this fraction of the full rendered page (`document.body.innerText`), fall back to innerText instead of saving a partial article. Lower = more tolerant of partial extraction; higher = more aggressive fallback. |
| `download_images` | `true` | Download and rewrite images to local paths under `images_dir`. |
| `images_dir` | `raw/assets` | Where fetched images are stored. |

## Personal folder

The `personal/` directory is tracked in git so contributors can keep the same structure for their own notes, but its contents are gitignored. Add your own files freely — they will never be committed.

## LLM agent rules (summary)

- **Dry-run by default.** All wiki changes go to `proposals/` first.
- **Dates are load-bearing.** Every wiki claim carries an `as_of` date.
- **Source date beats ingest date.** Use the publication date from the source, not the date it was added.
- **Reuse over fragmentation.** Most sources update existing pages; new pages are rare.
- **Current state first.** History is kept but not loaded unless explicitly requested.

Full rules in [`AGENTS.md`](./AGENTS.md).
