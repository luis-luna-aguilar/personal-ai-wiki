# Deferred decisions

Running list of design and schema decisions that have been postponed — usually because we need more data, more ingests, or more time to see how the wiki actually grows before committing.

This file lives **outside** `wiki/` on purpose. It's meta, not content. Revisit it every so often (especially after a batch of ingests) and either resolve the item or update it with new evidence.

## Format

Each entry:

```
### [YYYY-MM-DD] <short title>
- **Context:** what prompted the question
- **Options considered:** bulleted list of candidate approaches
- **Why deferred:** what we're waiting on
- **Revisit when:** the trigger that should make us come back to this
```

---

## Open

### [2026-04-09] Staleness modelling for `state-of/*` pages
- **Context:** `state-of/coding.md` (and siblings) aggregate many sub-items, each with its own freshness. A single page-level `as_of` is load-bearing but misleading — the page looks "fresh" if any one section was touched, even if the rest of the page is old. First observed while applying the Fowler SDD ingest, where the newly added `spec-driven-development` subcategory was the only thing with a recent `as_of` but the whole page inherited that date.
- **Options considered:**
  - **Per-bullet `as_of`** (current approach, inline in the page body) — simple, but leaves the page-level frontmatter `as_of` ambiguous
  - **Derived `as_of`** — stop storing page-level `as_of`; compute it at query time from the oldest linked tool/model/concept page
  - **Two frontmatter dates** — `as_of` (structural: when subcategories were last reshaped) + `data_as_of` (inherited freshest or oldest leaf)
  - **Status-section freshness** — make staleness a property of each subcategory section inside the page, not the page as a whole
- **Why deferred:** Only one ingest of evidence so far. Need to see how state-of pages evolve after several more ingests before picking a model. Possibly the answer differs by domain (fast-moving `coding` vs slower `concepts`).
- **Revisit when:** `state-of/coding.md` has been touched by 3+ separate ingests, OR we ingest something that contradicts a claim on a state-of page for the first time (that will stress-test whichever model we have).

---

## Resolved

### [2026-04-09] `fetch_url.py` readability mis-extraction on JS-rendered SPAs
- **Context:** While ingesting `https://www.harvey.ai/blog/autonomous-agents-legal-is-next`, `scripts/fetch_url.py` saved only the footer copyright (~75 chars). The full ~11k-char article body was actually present in `document.body.innerText` after page load — `readability-lxml` simply mis-identified the main content container on Harvey's SPA. The same root cause likely affects other modern JS-rendered blogs. Worked around for this one ingest by running Playwright manually and writing the raw file by hand.
- **Options considered:**
  - **Length-based fallback.** If `readability` returns markdown shorter than some threshold (say, < 500 chars when `body.innerText` is > 2000 chars), fall back to `body.innerText` (or markdownify the whole `<main>`/`<article>` element). Cheap and probably sufficient.
  - **Per-domain selectors.** Maintain a small map of `domain → CSS selector` for known-bad sites. More accurate but more maintenance.
  - **Replace readability entirely.** Use `trafilatura` or a different extractor known to handle SPAs better. Bigger change.
  - **Always dual-extract.** Run readability AND `body.innerText`, save both, let the LLM choose at ingest time. Loses the cleanliness of a single canonical raw file.
- **Resolution [2026-04-09]:** Went with the **length-based fallback** — cheapest option, no per-site maintenance, no dependency swap. Changes in `scripts/fetch_url.py`:
  - `fetch_with_playwright()` now also evaluates `document.body.innerText` after the page settles and returns it alongside `(title, html)`. Extraction is wrapped in try/except so a broken eval doesn't abort the fetch.
  - `html_to_markdown()` takes `body_text` as a second positional argument. After the normal readability→markdownify pipeline, if the resulting markdown is `< READABILITY_MIN_CHARS` (500) AND `body_text` is `>= INNERTEXT_MIN_CHARS` (2000) AND `body_text` is at least `INNERTEXT_RATIO` (4) × longer than the markdown, it swaps in `body_text` and prints a warning to stderr noting that heading/link structure is lost and the raw file may want manual cleaning.
  - `main()` wires the new `body_text` through.
  - Thresholds live as module-level constants so they're easy to tune if future failures have different shapes. Also fixed a latent bug: the function signature had been updated to take `body_text` earlier, but the call site in `main()` was still passing 3 args — the script would have crashed on next use until this patch.
- **Revisit if:** We see the fallback warning fire on a page that *wasn't* actually mis-extracted (false positive — thresholds too aggressive), or we see a page where readability returned > 500 chars of wrong content (false negative — length alone doesn't catch it, may need per-domain selectors or a real switch to trafilatura).
