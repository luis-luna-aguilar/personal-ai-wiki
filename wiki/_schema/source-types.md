# Source types — ingest playbooks

One playbook per source type. The LLM follows the playbook when ingesting. Settings live in `config.yml → source_types`; the per-type guidance below is the prose version.

## article

- **Raw folder:** `raw/articles/`
- **Filename:** `YYYY-MM-DD-slug.md`
- **Ingest style:** standard
- **Playbook:**
  1. Read fully.
  2. Extract key claims, version numbers, benchmark results, and dated facts.
  3. Identify wiki pages touched (usually 3–8). Articles about organizational rollout, enablement, or reported adoption patterns may fit `wiki/training/`.
  4. Draft a proposal in `proposals/`.
  5. Create a source summary at `wiki/sources/articles/<slug>.md`.

## tweet

- **Raw folder:** `raw/tweets/`
- **Filename:** `YYYY-MM-DD-handle-slug.md`
- **Ingest style:** lightweight
- **Playbook:**
  1. Tweets are usually single signals. Often touches 1 wiki page.
  2. Record the author, handle, and date — these matter more than for articles.
  3. If the tweet is just "X is out," add a one-line update to the relevant tool/model page and move on.
  4. Source summary is optional for tweets but preferred for consistency.

## paper

- **Raw folder:** `raw/papers/`
- **Filename:** `YYYY-MM-DD-first-author-slug.md`
- **Ingest style:** deep
- **Playbook:**
  1. Deep read. Papers often introduce concepts worthy of their own `concepts/` page.
  2. Extract: methodology, headline findings, limitations, datasets/benchmarks used.
  3. Propose concept pages for any new ideas. Update benchmark pages if new scores are reported.
  4. Full source summary required.

## podcast

- **Raw folder:** `raw/podcasts/`
- **Filename:** `YYYY-MM-DD-show-episode.md`
- **Ingest style:** summarize_first
- **Playbook:**
  1. Transcripts are long. First pass: aggressive summarization with speaker attribution.
  2. Treat the summary as the ingest unit.
  3. Extract opinions / predictions / anecdotes — podcasts are rich for `trends/`, `training/`, and `personal/takes/`.
  4. Source summary required.

## repo

- **Raw folder:** `raw/repos/`
- **Filename:** `owner-repo.md`
- **Ingest style:** readme_first
- **Playbook:**
  1. **Read the README first** — it is the primary source of truth for what the repo is.
  2. Capture: what it does, language/stack, license, activity, comparisons to alternatives.
  3. Most repos become `tools/` entries. Some become `workflows/` entries.
  4. Source summary required.

## newsletter

- **Raw folder:** `raw/newsletters/`
- **Filename:** `YYYY-MM-DD-newsletter-name.md`
- **Ingest style:** triage
- **Playbook:**
  1. **Never ingest directly.** Always write a triage file first at `proposals/triage/`.
  2. Produce a bulleted signal list with checkboxes. Recommend action per signal.
  3. Wait for the user to check boxes and say "process the triage."

## meeting

- **Raw folder:** `raw/meetings/`
- **Filename:** `YYYY-MM-DD-topic.md`
- **Ingest style:** personal
- **Playbook:**
  1. Meeting notes are usually personal context (decisions, opinions, priorities).
  2. Default target is `personal/`, not `wiki/`.
  3. If the user wants factual content extracted to the wiki, they'll say so explicitly. Team rollout lessons and repeated enablement patterns may fit `wiki/training/`.

## note

- **Raw folder:** `raw/notes/`
- **Filename:** `YYYY-MM-DD-slug.md`
- **Ingest style:** personal
- **Playbook:**
  1. User's own notes. Usually personal material.
  2. Default target is `personal/`. Do not push to wiki/ without explicit instruction.
  3. Treat with more care than public sources — the voice should be preserved. If the user explicitly wants reusable guidance extracted, `wiki/training/` is the likely target.
