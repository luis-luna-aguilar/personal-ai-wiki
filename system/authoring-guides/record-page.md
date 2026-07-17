# Authoring Guide — `wiki/sources/*.md` Sidecars

Read this before writing a sidecar for a `wiki/sources/**/*.md` page (a dated summary of an ingested external source — an article, tweet, newsletter, paper, podcast, or repo). This is this deployment's analog of the source project's Pipeline 4 ("Historical/Static") record pages — the sidecar pattern is deliberately minimal, matching how thin these pages are meant to be: a source page exists to record *what was ingested, when, and which wiki pages it influenced*, not to duplicate content that belongs on the tool/model/concept pages themselves.

---

## The pattern

```turtle
aiw:claude-code-monitor a prov:Entity ;
    rdfs:label "Claude Code Monitor tool announcement"@en ;
    rdfs:comment "Tweet from Noah Zweben (Anthropic) announcing the Monitor tool for Claude Code: background scripts that wake the agent on events instead of polling."@en ;
    dct:date "2026-04-10"^^xsd:date ;
    prov:wasDerivedFrom aiw:claude-code .
```

- [ ] The source page itself is **`prov:Entity`** — never a bespoke native class. A source summary is upstream PROV's "a thing produced by an activity" (the ingestion); there is no wiki-specific shape this needs beyond what `prov:Entity` + the three properties below already say.
- [ ] `dct:date` carries the source's own date as `xsd:date` — use the frontmatter `published` date (the date the external document/tweet/article actually went out) when known; fall back to `ingested` only if the source itself is undated.
- [ ] `prov:wasDerivedFrom` — one triple per tool, model, benchmark, or concept the source's content is actually **about** and that already exists (or is being created in the same proposal) as its own individual — not every page merely mentioned in passing. This maps directly onto the page's own **"Influenced pages"** section: each entry there that names a page with its own individual becomes a `wasDerivedFrom` target. A `wiki/state-of/*.md` page mentioned in "Influenced pages" only gets a target here once/if that page type itself has a modeled individual — don't invent one just to complete this triple.
- [ ] `rdfs:comment` is a genuine one-sentence gloss of what the source covers — per the repo's comment-discipline rule, any fact worth stating beyond this gloss belongs as a real triple elsewhere (e.g. a benchmark score the source reports goes through `aiw:BenchmarkResult`'s reified pattern on the model/tool page, not into this comment).
- [ ] Beyond identity + `wasDerivedFrom`, a source page's *content* facts (the "Key claims extracted" bullets) belong on the pages of the tools/models/concepts the source derives into, following whatever pattern fits that content — a benchmark result, a new feature, a relationship. The source's own sidecar does not duplicate them.

---

## Before minting anything, check for reuse

- [ ] **Does the source introduce a fact that already exists elsewhere in the graph?** A source page frequently repeats a benchmark score, a feature, or a relationship already stated on a tool/model page from an earlier source. Point at the existing individual (`prov:wasDerivedFrom` already establishes the provenance link) rather than re-minting it here.
- [ ] **Do not mint a native `aiw:Source`/`aiw:Summary` class.** `prov:Entity` is the correct, sufficient upstream type for every source page in this project.

---

## Naming convention

- [ ] Source individual: `aiw:<slug>` where slug is the filename without extension, in kebab-case (`claude-code-monitor.md` → `aiw:claude-code-monitor`) — same page-slug rule as every other wiki page, no date-prefix stripping needed since these filenames aren't date-prefixed the way the source project's `wiki/records/YYYY-MM-DD-*.md` were.

## Before finishing

- [ ] Confirmed the source is typed `prov:Entity` only.
- [ ] Confirmed every substantive tool/model/concept the source is about is captured via `prov:wasDerivedFrom`, matching the page's own "Influenced pages" section.
- [ ] Confirmed no content fact (a benchmark score, a feature, a relationship) is duplicated here instead of on its owning tool/model page.
