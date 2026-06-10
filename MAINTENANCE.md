# Wiki Maintenance

This file defines all maintenance operations for the AI Wiki. The LLM reads this file when running maintenance. **Do not put operating rules here** — those live in `AGENTS.md`. This file is focused on periodic upkeep tasks.

---

## Automated script checks

Scripts in `scripts/` cover mechanical hygiene. They are cheap — run them whenever asked or as part of a full maintenance pass.

| Script | Purpose | Trigger phrase |
|---|---|---|
| `orphans.py` | Report pages with no inbound internal links | "find orphan pages" |
| `link_check.py` | Report broken Markdown links and editor-specific link syntax in wiki page bodies | "check links" |
| `tag_compliance.py` | Report tags/domains/subcategories not in `_schema/` | "check tag compliance" |
| `lint_all.py` | Chain orphans, link_check, and tag_compliance | "run lint", "lint the wiki" |
| `index_check.py` | Report pages on disk not in `wiki/index.md`, and index entries with no matching file | "check index", "index check" |
| `source_orphans.py` | Report source files not referenced by any wiki page frontmatter, and broken source refs | "check source orphans", "source orphans" |
| `recent_changes_cap.py` | Report pages whose `## Recent changes` section exceeds the 5-entry cap; shows which entries need to be spilled | "check cap", "recent changes cap" |

> **Note on `stale.py`:** Staleness is a query-time confidence signal, not a maintenance action. The script exists but is not part of the maintenance pass and not run automatically. Stale pages are never deleted or modified due to age alone — the wiki does not remove old data.

Run via `python scripts/<name>.py`. These are cheap — run them whenever asked.

---

## Recent-changes cap enforcement

The `## Recent changes` section on every wiki page is capped at **5 entries** (`config.yml → history.recent_changes_cap`). When a page accumulates more than 5 entries, the oldest entries must be spilled to the corresponding file under `wiki/history/` and removed from the main page.

**When to enforce:** during every maintenance pass via `python scripts/recent_changes_cap.py`. The script identifies violating pages and marks exactly which entries (oldest, past position 5) need to be spilled.

**How to spill (after the script identifies violators):**

1. For each page flagged by the script, open it and locate the entries marked `SPILL →`.
2. Open (or create) the mirrored history file at `wiki/history/<type>/<filename>.md`. Append each spilled entry — one bullet per line, preserving original dates. Do not reformat or restructure.
3. Remove the spilled entries from the main page's `## Recent changes`.
4. Log: `- [YYYY-MM-DD] **spill** | <page> | <N> entries moved to history`

**History file structure:** if the history file does not exist, create it with a single `# <Title> — History` heading and start appending entries below it. No frontmatter needed.

**Note:** the script detects violations; the LLM performs the actual file edits. Prefer batching spills during a maintenance pass rather than doing them piecemeal during ingests.

---

## Podcast workflow

The wiki is periodically exported as three ~40-minute podcast source files. The full spec lives in `podcast/directions.md`.

### Generate podcast files

Triggered by **"build podcast files"**, **"generate podcasts"**, **"rebuild podcast"**, or similar.

```bash
bash scripts/build_podcast.sh all
```

Output lands in `podcast/out/` (gitignored). Three files:
- `block-1-state-of-play.md` — state-of pages + model pages + benchmarks
- `block-2-tools-workflows.md` — tool pages + workflow pages
- `block-3-concepts-trends-training.md` — concept pages + trend pages + training pages

Each file begins with a framing intro from `podcast/block-N-*.md` so the podcast tool knows the episode objective.

### Analyze whether the split needs updating

Triggered by **"check podcast split"**, **"should I resplit the podcast"**, or similar.

Run this analysis **without modifying any files** — report only:

1. Word count per current block: `wc -w wiki/<dir>/*.md` for each dir in each block.
2. Flag any block that has grown past **15,000 words** — that block likely needs to be split.
3. Flag any wiki directory not currently assigned to a block (new folders are easy to miss).
4. Suggest a revised split if needed, showing which dirs move where and the estimated new word counts.
5. If the user approves a new split, update:
   - The relevant `podcast/block-N-*.md` intro file (title, objective, sources listed)
   - The `case` branch in `scripts/build_podcast.sh`
   - The block table in `podcast/directions.md`
   - This section in `MAINTENANCE.md`

---

## Semantic lint (LLM, costly, explicit only)

Run these **only when the user explicitly asks with one of these phrases**:

- **"find contradictions"** / **"scan for contradictions"** → read `wiki/index.md` + all state-of pages + referenced pages, look for claims that contradict each other, report findings
- **"missing page suggestions"** / **"what concepts need pages"** → find entities/concepts/training topics mentioned across multiple pages but lacking their own page, suggest which deserve promotion
- **"domain completeness"** / **"what's missing from state-of/X"** → given a domain, report subcategories that look thin or missing compared to mentions elsewhere

**Never run these automatically.** They consume serious tokens. Only on explicit request.

---

## Full maintenance pass

Triggered by **"run maintenance"**, **"do a maintenance pass"**, or similar.

Steps, in order:

1. Run `python scripts/lint_all.py` — mechanical hygiene (orphans, broken links, tag compliance)
2. Run `python scripts/index_check.py` — index completeness
3. Run `python scripts/source_orphans.py` — unreferenced source files and broken source refs
4. Run `python scripts/recent_changes_cap.py` — list pages over the 5-entry cap and which entries need spilling
5. Check the podcast block split (word counts, any block over 15K words?)
6. Report all findings to the user
7. Wait for user direction before making any changes

Do not run semantic lint as part of a routine maintenance pass unless explicitly requested.
