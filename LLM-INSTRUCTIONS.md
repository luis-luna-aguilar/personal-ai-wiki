# AI Wiki — Schema & Operating Manual

This file tells you (the LLM) how to operate on this wiki. It is **not** user documentation — user docs live in `manual/`. Follow these rules strictly.

**This file is the single source of truth for how the LLM operates on this wiki.** `CLAUDE.md` is only a pointer to this file. **Any modifications to the operating rules must be made here, in `LLM-INSTRUCTIONS.md`** — never in `CLAUDE.md`.

## Purpose

This is a personal knowledge base that tracks the fast-moving AI landscape: tools, models, benchmarks, workflows, concepts, trends, and training guidance across business areas. Your job is to keep it current, organized, and token-efficient. The user curates sources and asks questions; you do the reading, filing, cross-referencing, and bookkeeping.

## Operating principles

1. **Current state first.** Main pages are present-tense. History is capped, mostly off-page, and only read when explicitly requested.
2. **Dates are load-bearing.** Every claim has an `as_of` date. Confidence is derived from age at query time, never assigned during ingest.
3. **Source date beats ingest date.** If the source provides a publication date (article publish date, tweet date, paper date, release date, etc.), use that date for `as_of` on the pages derived from it. Only fall back to the ingest date when the source date is unknown.
4. **Trust the sources.** Do not evaluate source credibility at ingest. Record what the source says, and keep publication date separate from ingestion date.
5. **Reuse over fragmentation.** Prefer updating existing pages to creating new ones. Most sources update 3–8 existing pages and create 0–1 new ones.
6. **Ambiguity is valid.** Subcategories can have multiple top players. Do not force a single winner unless the sources clearly support one.
7. **Dry-run by default.** Never write to `wiki/` directly in response to a new source. Always write a proposal to `proposals/` first and wait for user approval.
8. **Token efficiency.** Do not read `wiki/history/` unless asked. Do not walk the whole wiki — use `wiki/index.md` to find the right pages.
9. **Use Claude Code's or Codex's native search tools** (Grep, Glob, Read). Do not build or use a custom search CLI.
10. **Prefer the substantive source.** If a tweet mainly points to a linked article, paper, repo, or similar fuller source, ingest the fuller source and ignore the tweet unless the tweet adds unique information.
11. **State-of claims are replaceable.** When a source changes who leads a subcategory, update the current state-of page to reflect the new leader set rather than accumulating stale "best" claims. Preserve the change in `## Recent changes` (and `wiki/history/` if needed), and keep multiple leaders only when the source-backed current state is genuinely ambiguous.

## Directory layout

```
raw/                       # Immutable sources. You READ but never modify.
  articles/  tweets/  papers/  podcasts/  repos/  newsletters/  deep-research/  meetings/  notes/
  assets/                  # Images from Obsidian Web Clipper / fetch_url.py

wiki/                      # You own this. Current state.
  index.md                 # Catalog of all wiki pages. Read this first on every query.
  log.md                   # Chronological append-only record.
  state-of/                # Dashboards per domain. Read-me-first pages.
  models/                  # One page per foundation model.
  tools/                   # One page per tool.
  benchmarks/              # Benchmark pages with leaderboards.
  workflows/               # Reusable patterns & recipes.
  concepts/                # Ideas (RAG, context engineering, etc.).
  trends/                  # Things being watched.
  training/                # Practical guidance for teaching teams and businesses to use AI well.
  sources/                 # One lightweight summary page per ingested source.
  history/                 # Archived old versions. Mirrors wiki/ structure.
  _schema/                 # Controlled vocabulary files. See below.

personal/                  # User's opinions. Separate from the factual wiki.
  philosophies/
  takes/

proposals/                 # Dry-run diffs awaiting user approval.
  triage/                  # Newsletter triage files.
  triage/applied/
  applied/
  rejected/

scripts/                   # Python maintenance utilities.
manual/                    # User-facing HTML docs. Do NOT modify unless asked.
config.yml                 # Thresholds and settings.
CLAUDE.md                  # Pointer to LLM-INSTRUCTIONS.md. Do not edit directly.
LLM-INSTRUCTIONS.md        # This file. The real operating manual.
```

## Controlled vocabulary

Four files in `wiki/_schema/` define the valid terms:

- **`tags.md`** — valid tags for frontmatter `tags:` field
- **`domains.md`** — valid values for `domains:` field (e.g. `coding`, `agents`, `models`)
- **`subcategories.md`** — valid `subcategory:` values for tools/models/workflows
- **`source-types.md`** — per-type ingest playbooks

**Rules:**
- Never use a tag, domain, or subcategory that isn't in these files.
- To add a new one, propose it explicitly in a proposal file: *"I'd like to add a new subcategory `terminal-coding-agent` — approve?"*. The user approves by checking the box; you then update the schema file as part of applying the proposal.
- `scripts/tag_compliance.py` enforces this — run it when asked.

## Frontmatter schema

Every wiki page has YAML frontmatter:

```yaml
---
title: Claude Opus 4.6
type: model          # model | tool | benchmark | workflow | concept | trend | training | state-of | source
domains: [coding, agents]
subcategory: frontier-model    # required for type: tool | model | workflow; optional elsewhere
tags: [anthropic, frontier]
as_of: 2026-04-09
sources: [claude-opus-46-launch, swe-bench-april]   # IDs matching files in wiki/sources/
---
```

**Required fields by type:**
- `title`, `type`, `as_of` — always required
- `domains` — required for `tool`, `model`, `workflow`, `state-of`, `trend`; optional for `training`
- `subcategory` — required for `tool`, `model`, `workflow`
- `sources` — required once a page has any content derived from a source

**Date rule for `as_of`:**
- If the source has a clear publication/date-of-record, use that date for `as_of` on derived wiki pages.
- If multiple sources support a page, `as_of` should reflect the newest source-backed claim currently represented on the page.
- If the source date is unavailable, use the ingest date as a fallback.

**Do not add fields for confidence.** Confidence is computed at query time from `as_of` + `config.yml` thresholds.

## Page body conventions

### State-of pages

State-of pages (`wiki/state-of/*.md`) are dashboards organized by **subcategory**, not flat rankings. Each subcategory lists 1..N leaders. Ambiguity is valid. Format:

```markdown
# State of Coding

## Terminal / agentic coding
- [[Claude Code]] — Anthropic; terminal-first agent loop *(as of 2026-04-09)*
- [[Codex]] — OpenAI direct competitor *(as of 2026-04-09)*

## IDE-integrated pair programming
- [[Cursor]] — Leads SWE-bench at 74% *(as of 2026-04-09)*
- [[Windsurf]] — Close competitor *(as of 2026-03-28)*

## Recent changes
- [2026-04-09] Cursor 3 released, 74% SWE-bench (was 68%)
- [2026-03-22] Claude Code 1.2 adds native subagents
```

A tool belongs to a state-of page if its frontmatter `domains:` includes that page's domain. State-of pages do not list tools whose subcategories aren't represented — add a new subcategory section only when a tool exists in it.

When a new source says something is now state-of-the-art / leading / best-in-class in a subcategory:
- Update the relevant leader line(s) in place so the page remains a snapshot of the current state, not an accumulation of outdated winners.
- If the previous leader is no longer clearly leading, demote or remove the old wording rather than leaving two contradictory "leader" claims side by side.
- Record the transition in `## Recent changes` with enough detail to understand what changed and when.
- If the new evidence is mixed rather than decisive, keep multiple entries and phrase them as co-leaders or area-specific leaders instead of forcing a single winner.

### Tool / model / workflow pages

```markdown
---
title: Cursor
type: tool
domains: [coding]
subcategory: ide-pair-programming
tags: [ide, vscode-fork]
as_of: 2026-04-09
sources: [cursor-3-release]
---

# Cursor

Brief present-tense description. Current version, what it is, what it's good at.

## Current status (as of 2026-04-09)
- Version 3.0, released 2026-04-05
- Leads SWE-bench at 74%
- Strongest in [specific tasks]
- Pricing: $20/mo Pro tier

## Strengths
- ...

## Weaknesses / caveats
- ...

## Recent changes
- [2026-04-09] v3 release, SWE-bench to 74% (was 68%)
- [2026-03-22] v2.5 added inline chat
- [2026-03-01] Pricing change to $20/mo
<!-- max 5 entries; oldest spills to wiki/history/tools/cursor.md -->

## Sources
- [[sources/articles/cursor-3-release]]
- [[sources/articles/cursor-vs-windsurf-review]]
```

Tool, model, and workflow pages should be concise by default once the wiki is past the earliest bootstrap stage.

- Prefer a compact synthesis over a long product brief.
- Keep `## Current status` to 3-6 bullets unless the user explicitly wants depth.
- Add only the sections that materially change understanding; do not repeat the same point under "Current status", "Strengths", and "What it is trying to solve".
- Default target is roughly 150-300 words of body content for routine ingests unless the source genuinely introduces multiple distinct ideas that need separate treatment.
- If the source is mostly setup, positioning, or one core claim, prefer a shorter page and rely on the source summary / raw source for extra detail.

### Concept / trend pages

Concept and trend pages should be **more concise** than tool pages by default. Prefer a compact synthesis over an essay.

- Start with a short definition paragraph.
- Keep `## Current status` to 3–5 bullets.
- Add only the sections that materially help understanding; avoid repeating the same idea under multiple headings.
- Default target is roughly 150–300 words of body content unless the user explicitly wants depth or the concept genuinely needs more structure.
- If a source is mostly one core idea plus a few implications, prefer one "Why it matters" section over several thematic sections.

### Training pages

Training pages (`wiki/training/*.md`) capture practical guidance for helping teams, functions, or entire businesses use AI better. They are neither product pages nor pure concepts: the goal is operational enablement.

- Use these for playbooks, rollout guidance, evidence-backed adoption patterns, and synthesized "what worked for other teams" pages.
- Default to concise, practical writing. Prefer checklists, patterns, and failure modes over essays.
- Good page shapes include:
  - team enablement playbooks
  - function-specific training guidance (for example legal, finance, support, engineering)
  - evidence pages that compile reported wins, rollout patterns, and anti-patterns across sources
- `domains` is optional. Use it when the page is clearly tied to a domain already represented in the wiki; omit it when the page is cross-functional.
- Suggested sections:
  - `## Current guidance`
  - `## Proven patterns`
  - `## Failure modes`
  - `## Evidence from practice`
  - `## Open questions`

### Recent changes cap

The "Recent changes" section is capped at `config.yml → history.recent_changes_cap` (default 5). When a 6th entry arrives, append the oldest one to the corresponding file under `wiki/history/` (create the file if it doesn't exist) and drop it from the main page.

### Sources pages

Every ingested source gets a tiny summary page in `wiki/sources/<type>/<id>.md`:

```markdown
---
title: Cursor 3 release announcement
type: source
source_type: article
source_file: raw/articles/2026-04-09-cursor-3-release.md
url: https://cursor.com/blog/cursor-3
published: 2026-04-05   # optional; include when the source provides it
ingested: 2026-04-09
domains: [coding]
---

# Cursor 3 release announcement

One-paragraph summary.

## Influenced pages
- [[tools/cursor]] — version bump, SWE-bench update
- [[state-of/coding]] — updated leader line
- [[benchmarks/swe-bench]] — new data point

## Key claims extracted
- Cursor 3 released 2026-04-05
- SWE-bench score: 74%
- New "agent mode" feature
```

This doubles as your "what have I actually read" log.

When a source provides a publication date, record it on the source summary page as `published:` and use that same date for `as_of` on the derived wiki pages.

## Workflows

### 1. Ingest (single source from file)

Triggered when the user drops a file into `raw/<type>/` and says **"ingest this"** (or similar) or gives you a specific file path.

**Steps:**
1. Read the source file.
2. Read `wiki/index.md` to find existing pages this source might touch.
3. Read the relevant existing pages (only the ones that look relevant; don't load the whole wiki).
4. Draft a proposal file at `proposals/YYYY-MM-DD-<slug>.md` using the format below.
5. Do **not** modify `wiki/`. Tell the user the proposal is ready for review.

### 2. Ingest from URL

Triggered when the user gives you a URL and says **"ingest"** or **"fetch and ingest"**.

**Steps:**
1. Run `python scripts/fetch_url.py --type <article|tweet|paper|repo> --url <URL>`. This uses a real browser (Playwright/Chromium) to avoid bot blocks.
2. The script saves the markdown to the appropriate `raw/` subfolder and prints the path.
3. Proceed as with file ingest, starting from step 2.

**If fetch fails:** tell the user, suggest they paste the content or use Obsidian Web Clipper. Do not fall back to `WebFetch`.

### 3. Triage (newsletter / batch of signals / research reports)

Triggered when the user drops a newsletter into `raw/newsletters/`, a research memo into `raw/deep-research/`, or a similar high-breadth source and says **"triage this"** or similar.

**Steps:**
1. Read the newsletter.
2. Write `proposals/triage/YYYY-MM-DD-<slug>.md` using the triage format below.
3. Do **not** create any ingest proposals yet. Wait for user to check boxes and say "process the triage."

**Special rule for deep-research reports:** treat them as synthesis artifacts, not as canonical sources. They are useful for topic discovery, source discovery, and clustering, but they may contain hallucinations, over-compressed taxonomies, or weak secondary sourcing. Never write wiki proposals from a research report alone when the claim depends on a specific framework, number, benchmark score, vendor practice, or named tool. Use the report to identify clusters and to find better primary sources behind those clusters.

**Triage file format:**

A triage file may reference a single source or multiple sources (e.g. when generated from a batch of emails). Use `source:` for a single file and `sources:` for a list. Each signal includes a `*Source:*` line pointing to the exact raw file it came from.

```markdown
---
type: triage
source: raw/newsletters/2026-04-09-the-batch.md   # single source
# — OR —
sources:                                            # multi-source (email digest)
  - raw/newsletters/2026-04-09-the-batch.md
  - raw/articles/2026-04-09-some-article.md
  - raw/tweets/2026-04-09-twitter-com-handle-status-123.md
status: pending
---

# Triage: The Batch — 2026-04-09

## Signals

- [ ] **[coding]** Cursor 3 released, 74% SWE-bench
    *Source:* `raw/newsletters/2026-04-09-the-batch.md`
    *Impact:* updates `state-of/coding.md`, `tools/cursor.md`; demotes previous leader line
    *Recommended:* full ingest

- [ ] **[models]** Anthropic announces Opus 4.7 preview
    *Source:* `raw/newsletters/2026-04-09-the-batch.md`
    *Impact:* new entry on `models/claude-opus.md` or separate page; bump `state-of/models.md`
    *Recommended:* full ingest

- [ ] **[marketing]** Vendor blog: "10 ways AI is changing X"
    *Source:* `raw/articles/2026-04-09-vendor-blog.md`
    *Impact:* nothing new
    *Recommended:* skip

- [ ] **[misc]** ChatGPT adds voice feature
    *Source:* `raw/newsletters/2026-04-09-the-batch.md`
    *Impact:* consumer side, outside current scope
    *Recommended:* skip
```

**Research-report triage format:** When the source is a deep-research report, cluster by topic area rather than by individual claim. Each signal should include a quick confidence judgment and a verification recommendation.

```markdown
---
type: triage
source: raw/deep-research/2026-04-23-agents-evals.md
status: pending
---

# Triage: Agent Evals Research Report — 2026-04-23

## Signals

- [ ] **[agents]** Agent eval taxonomy and operating model

    **What it is:** The report proposes a broad taxonomy covering capability, regression, trajectory, unit-level, and online evals, plus distinctions between coding and workflow agents.

    **Why it matters:** Strong fit for `concepts/` and `training/`; likely updates `concepts/harness.md` and `concepts/agent-improvement-loop.md`.

    **Evidence shape:** mixed synthesis; some likely grounded in strong sources, but framing appears normalized by the report author.
    **Source quality:** mixed primary and secondary
    **Verification:** verify before proposal
    **Recommended:** verify-first

- [ ] **[coding]** Evals for agentic software development

    **What it is:** Practical guidance for deterministic checks, coding-task-specific eval patterns, shadow mode, CI quality gates, and converting artifacts into eval cases.

    **Why it matters:** Strong fit for a training page on engineering evals and autonomy.

    **Evidence shape:** promising, with concrete named tools and company examples.
    **Source quality:** mixed primary and secondary
    **Verification:** verify before proposal
    **Recommended:** verify-first

- [ ] **[agents]** Benchmarks and eval tools landscape

    **What it is:** Benchmark families, observability/eval platforms, and supporting tools mentioned across the report.

    **Why it matters:** May create or update benchmark pages and selected tool pages.

    **Evidence shape:** useful source-discovery map, but too noisy to trust directly.
    **Source quality:** mixed, noisy
    **Verification:** required; use primary docs or benchmark papers
    **Recommended:** verify-first
```

**Processing a triage:** When the user says "process the triage" (or similar), re-read the triage file, then:

1. **Use already-fetched content.** For email digest triages (Workflow 4), URL content was already fetched during the triage step — use those existing `raw/` files. For standard newsletter triages, fetch now: run `scripts/fetch_url.py` for each checked item's primary URL. If a fetch fails, fall back to the newsletter summary and note the gap.
2. **Video check.** If a fetched source turns out to be primarily a video with no useful text (tweet with only a video embed, YouTube link, etc.), do not generate a proposal — note it as `[video — skip]` and move on.
3. **Generate proposals.** For each checked item that passed the video check, generate a proposal at `proposals/YYYY-MM-DD-<slug>.md` using the full source content. Thin signals still get a proposal — just a small one.
4. **Nothing is applied directly from a triage.** Every change goes through the proposal → approval → apply cycle. Unchecked items are ignored.

**Processing a research-report triage:** When the source is a deep-research report, the checked items follow a stricter path:

1. **Do not treat the report itself as sufficient evidence.** Re-open the checked report sections and note the key claims, but verify the important claims against better sources before writing proposals.
2. **Prioritize primary sources.** For each checked item, fetch and read the best available sources behind the report: official docs, benchmark papers/sites, engineering blogs from the relevant company, public repos, or authoritative technical writeups. Avoid relying on generic SEO blogs, thin Medium posts, or listicles when a stronger source exists.
3. **Use the report as a map, not the proof.** The report is acceptable as a supporting source summary page later, but the resulting proposal should be grounded mainly in the verified underlying sources.
4. **Split aggressively by topic cluster.** Research reports are usually too wide for one proposal. Prefer several focused proposals over one omnibus proposal.
5. **Create tool-specific proposals only when the tool clearly matters.** A tool mentioned in the report does not automatically deserve a `tools/` page. Only promote tools that appear durable, relevant to the wiki's scope, and well-supported by stronger sources.
6. **If verification fails, downgrade instead of forcing.** When a framework, metric, or named pattern cannot be grounded cleanly, either omit it from the proposal or leave it in the triage as `hold`.

Then move the triage file to `proposals/triage/applied/` and append a log entry: `## [YYYY-MM-DD] triage | <name> | N proposals, K skipped`.

### 4. Email digest (daily or weekly batch)

#### Step 1 — Fetch (script)

`scripts/gmail_fetch.py` saves each email as an individual `raw/` file and writes a **skeleton manifest** at `proposals/triage/<slug>.md` with `status: pending-analysis`. The manifest lists all saved files but has no signals — it is NOT a finished triage.

- Newsletter emails → `raw/newsletters/YYYY-MM-DD-<slug>.md`
- Email Me URL forwards → `raw/articles/` or `raw/tweets/` (stub only, `fetched: false`)

#### Step 2 — Triage this digest (Claude)

Triggered **automatically** whenever `gmail_fetch.py` completes and produces a manifest (i.e. whenever the script runs in a Claude Code session). Do NOT wait for the user to say "triage this" — proceed immediately. The user's intent in running the script is to get a finished triage report to read, not a skeleton.

**Steps:**

1. **Fetch all URL stubs.** For every source listed in the manifest frontmatter that has `fetched: false`, run `scripts/fetch_url.py --type <article|tweet> --url <URL>`. This replaces the stub with full content. Do this for ALL stubs upfront, in parallel if possible, before writing any signals. If a fetch fails, note it and continue.

2. **Read all newsletters.** Read every `raw/newsletters/` file listed in the manifest in full.

3. **Group by topic.** Across all fetched articles, tweets, and newsletters, identify the distinct topics and themes. If multiple sources mention the same thing (same model release, same tool, same debate), merge them into one signal. Do not create one signal per source — create one signal per topic.

4. **Write consolidated signals.** Overwrite the manifest's `## Signals` section. Each signal covers one topic and follows this format:

```markdown
- [ ] **[domain]** Topic title — one sharp sentence

    **What it is:** 2–4 sentences explaining the topic clearly enough that the user can decide whether to ingest. Include specifics: version numbers, benchmark scores, names, claims.

    **Why it matters:** 1–2 sentences on the relevance to the wiki's scope.

    **Sources:**
      - `raw/tweets/2026-04-21-xcom-example.md` — Jasper Polak tweet amplifying the McKinsey piece
      - `raw/newsletters/2026-04-21-ainews-...md` — AINews summary with additional context

    **Primary URL:** https://... (the most authoritative source to fetch for the proposal)
    **Recommended:** full ingest | lightweight ingest | skip
```

5. **Update frontmatter.** Change `status: pending-analysis` → `status: pending` once signals are written.

**Rules for signals:**
- Use the controlled vocabulary for `[domain]` tags (check `wiki/_schema/tags.md`). Use `[?]` only if truly unclassifiable.
- If a topic appears in 3+ sources, that's a strong signal — flag it as high-priority.
- Video-only content: mark `**Recommended:** skip — video` and do not create a signal for ingestion.
- Depth over breadth: 8 rich signals beat 20 shallow ones. Merge aggressively.
- The user cannot approve what they cannot understand. Every signal must have enough detail to make the approve/skip decision without opening the source files.

#### Step 3 — Process (same as standard triage)

When the user says "process the triage", follow standard Workflow 3 processing. URL content is already fetched from Step 2, so use the existing `raw/` files rather than re-fetching. Generate proposals for each checked item.

**Daily flow:**
```
gmail_fetch.py --account ai --days 1
→ raw/{newsletters,articles,tweets}/2026-04-21-*.md
→ proposals/triage/2026-04-21-ai-digest.md  (skeleton, status: pending-analysis)
→ "triage this digest" → Claude fetches URLs, reads newsletters, groups topics
→ user reviews and checks signals
→ "process the triage" → proposals generated
```

**Backlog flow (personal Gmail, week by week):**
```
gmail_fetch.py --account personal --week 2026-W01
→ raw/**/2026-01-*.md files
→ proposals/triage/2026-W01-personal-digest.md  (skeleton)
→ same triage → process flow
```

### 5. Proposal format (dry-run diff)

```markdown
---
type: proposal
source: raw/articles/2026-04-09-cursor-3-release.md
status: pending
created: 2026-04-09
---

# Proposal: Cursor 3 release

## Summary
Two-sentence TL;DR of the source.

## Intended changes

- [ ] **Update** `wiki/state-of/coding.md` — bump Cursor line, update as_of
    > **Before:** `- [[Cursor]] — Leads SWE-bench at 68% (as of 2026-03-22)`
    > **After:**  `- [[Cursor]] — Leads SWE-bench at 74% (as of 2026-04-09)`

- [ ] **Update** `wiki/tools/cursor.md` — version bump, new recent-change entry
    > See draft below

- [ ] **Create** `wiki/benchmarks/swe-bench.md` — no current page, 3 sources now reference it
    > See draft below

- [ ] **Create** `wiki/sources/articles/cursor-3-release.md` — source summary

- [ ] **Spill** `wiki/tools/cursor.md` → `wiki/history/tools/cursor.md` — oldest recent-change entry falls off

## Page drafts

### wiki/tools/cursor.md (updated)

```
<full proposed markdown content of the updated page>
```

### wiki/benchmarks/swe-bench.md (new)

```
<full proposed markdown content of the new page>
```

### wiki/sources/articles/cursor-3-release.md (new)

```
<full proposed markdown content of the source summary>
```

## Schema / vocabulary additions
- [ ] Add new subcategory `benchmarks/coding-benchmarks` to `wiki/_schema/subcategories.md`

## Open questions
- Should I merge Cursor 3 content into existing `tools/cursor.md` (assumed yes), or create a separate versioned page?
- The article mentions a new "agent mode" — worth its own page under `concepts/` or just a section in the tool page?
```

**Rules for proposals:**
- Every intended change is a checkbox. Unchecked = skip.
- Every draft appears **in full** inside the proposal, in a fenced code block. The user may edit drafts directly in the file before applying.
- If a draft contains fenced code examples, wrap the full draft in a longer fence such as ````md ... ```` so inner ```text blocks do not break proposal formatting.
- For **updated** pages, show only the relevant diff snippet in the proposal unless the user explicitly asks for the full file. Do not paste the entire unchanged page just to show a small edit.
- Include "Open questions" when you're uncertain — the user can answer inline.
- Include a "Schema / vocabulary additions" section whenever you want to introduce a new tag, domain, or subcategory. This requires explicit approval via checkbox.

**Paper proposal exception:** papers are usually harder to understand than articles, tweets, or product pages, so paper proposals should be more explanatory and simpler by default.

- The goal is not academic evaluation. The goal is to ingest the useful content in plain language so the user can understand it and consider whether it applies to their own projects.
- Do not compress a paper into only a TL;DR and a short claim list.
- Start from the everyday problem the paper addresses: "what breaks?", "what is the agent/system trying to do?", and "why is this hard?"
- Explain the core idea in simple words before using technical terms. If a technical term is necessary, define it immediately in practical language.
- Prefer concrete examples, analogies, and step-by-step walkthroughs over dense phrases from the paper.
- Include a `Why this is useful for our projects` or equivalent section when the idea can transfer beyond the paper's domain.
- The proposed `wiki/sources/papers/<slug>.md` source page should help the user understand and reuse the paper's idea. Include the plain-language thesis, the problem setup, the main loop or mechanism, examples, practical translation, reported results, and limits.
- Keep derived concept/trend pages readable as wiki state, but allow them to be longer than routine concept pages when the concept originates in a paper and needs more explanation.
- Do not overstate paper results. Clearly distinguish "the paper reports X" from "this is proven generally," and note simulation-only results, benchmark scope, assumptions, and unresolved limitations.
- Avoid unexplained academic shorthand such as "neuro-symbolic," "operator," "reward machine," "transition," "policy," or "LTL." Either replace it with simpler wording or define it in the same paragraph.

### 5. Apply proposal

Triggered by **"apply this proposal"** / **"apply proposals/xxx.md"**.

**Critical rule:** before applying, you must re-open and re-read the proposal file from disk immediately before making any changes. Assume the user may have edited the proposal in Obsidian or another editor after you last looked at it. Do **not** rely on your memory, prior tool output, or an earlier read of the file.

**Steps:**
1. Re-read the proposal file **from disk, as it is now, immediately before applying** (the user may have edited it externally).
2. For each **checked** item, perform the action using the draft content **as it now appears in the file** (the user may have edited drafts).
3. Update `wiki/index.md` with any new pages.
4. Update `wiki/_schema/` files for any approved vocabulary additions.
5. Append a log entry: `## [YYYY-MM-DD] ingest | <source title> | <N> pages updated, <M> created`.
6. Move the proposal file to `proposals/applied/`.
7. Run an inline wikilink sanity check on everything you wrote; fix any broken links before reporting done.
8. Report a short summary to the user.

**Never apply an unchecked item.** Never apply a draft that has been deleted from the file. If the file is in an inconsistent state (checked boxes reference deleted drafts), stop and ask. If what you see in the editor/session conflicts with the last version you remember, trust the fresh on-disk read.

### 6. Reject proposal

Triggered by **"reject this proposal"**. Move the file to `proposals/rejected/` with no further action. Log: `## [YYYY-MM-DD] reject | <proposal name>`.

### 7. Query (ask)

Triggered by **"ask:"**, **"based on the wiki..."**, or similar question-shaped prompts.

**Steps:**
1. Read `wiki/index.md` first.
2. Identify relevant pages (usually a state-of page + 2–5 specific pages, and training pages when the question is about adoption or enablement).
3. Read only those pages. Do not walk the tree.
4. Synthesize an answer with wikilinks to sources.
5. **Always include a confidence header** based on the freshness of the underlying pages:

```
**Confidence:** high — newest relevant page as of 2026-04-09 (6 days old, threshold 14d).
```

Compute confidence this way (also in `config.yml → query.confidence_bands`):
- `age <= threshold` → **high**
- `threshold < age <= 2 × threshold` → **medium** (caveat: "may be outdated")
- `age > 2 × threshold` → **stale** (strong "verify this" warning)

Use the oldest relevant page's `as_of` as the basis. If multiple pages disagree on age, report the worst.

### 8. Query with web verification (ask-verify)

Triggered by **"ask-verify:"**, **"check the web"**, **"verify against web"**.

**Steps:**
1. Answer from the wiki first (as in step 7).
2. Use `scripts/fetch_url.py` to pull relevant fresh web content **only if the user provides URLs**. If they don't, tell them what URLs would help.
3. Compare wiki to web. Report:
   - Where the wiki agrees with current web info
   - Where the wiki disagrees or is behind
   - Propose a dry-run update if anything new was found (don't apply automatically)

**Do not** use `WebFetch` as a fallback. The browser-based script is the only supported web path.

## History handling

**Default:** never read `wiki/history/`. Main pages are the only thing you load on queries and ingests.

**Exceptions — read history only when:**
- The user explicitly asks for historical analysis ("how has Cursor evolved?", "what was the top model 3 months ago?")
- You're running a trend analysis requested by the user
- A proposal requires spilling an entry from a main page into history (you open the history file to append, that's all)

When spilling: open the history file (or create it), append the spilled entry with its original date, save. Do not reformat or restructure history files.

## Maintenance

### Scripts (on-demand, free to run)

| Script | Purpose | Trigger phrase |
|---|---|---|
| `stale.py` | Report pages whose `as_of` exceeds threshold | "show stale pages", "what's stale" |
| `orphans.py` | Report pages with no inbound wikilinks | "find orphan pages" |
| `link_check.py` | Report broken `[[wikilinks]]` | "check links" |
| `tag_compliance.py` | Report tags/domains/subcategories not in `_schema/` | "check tag compliance" |
| `lint_all.py` | Chain all four | "run lint", "lint the wiki" |
| `build_podcast.sh <1\|2\|3\|all>` | Generate podcast markdown files from wiki content | "build podcast files", "generate podcasts", "rebuild podcast" |

Run via `python scripts/<name>.py` or `bash scripts/<name>.sh`. These are cheap — run them whenever asked.

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
   - This section in `LLM-INSTRUCTIONS.md`

### Semantic lint (LLM, costly, explicit only)

Run these **only when the user explicitly asks with one of these phrases**:

- **"find contradictions"** / **"scan for contradictions"** → read `wiki/index.md` + all state-of pages + referenced pages, look for claims that contradict each other, report findings
- **"missing page suggestions"** / **"what concepts need pages"** → find entities/concepts/training topics mentioned across multiple pages but lacking their own page, suggest which deserve promotion
- **"domain completeness"** / **"what's missing from state-of/X"** → given a domain, report subcategories that look thin or missing compared to mentions elsewhere

**Never run these automatically.** They consume serious tokens. Only on explicit request.

## Personal space rules

`personal/` is the user's opinions and philosophies. Rules:

- **Direction of links is asymmetric.** Personal pages may link *to* wiki pages. Wiki pages **must not** link to personal pages.
- **Personal pages do not decay the same way.** They have `as_of` but the staleness script skips `personal/` by default (controlled in `config.yml`).
- **Do not update personal pages from sources.** Sources drive wiki updates, never personal updates. The user writes personal content themselves or asks you to edit it directly (never via the proposal flow).
- **The LLM never creates personal pages on its own initiative.** Only on direct user request.

## Log format

`wiki/log.md` is append-only. Every entry starts with:

```
## [YYYY-MM-DD] <op> | <subject> | <summary>
```

Where `<op>` is one of: `ingest`, `triage`, `reject`, `apply`, `lint`, `query-verify`, `schema`.

Examples:
```
## [2026-04-09] ingest | Cursor 3 release | 3 pages updated, 2 created
## [2026-04-09] triage | The Batch 2026-04-09 | 3 full, 1 note, 1 skipped
## [2026-04-09] schema | added subcategory `coding-benchmarks`
## [2026-04-09] lint | stale: 2 pages, orphans: 0, broken links: 0
```

`grep "^## \[" wiki/log.md | tail -20` gives the last 20 events.

## Bootstrapping exception

When `wiki/index.md` lists fewer than **30 pages**, the fan-out discipline is relaxed:

- Early sources are **expected** to create many new pages and introduce new subcategories/tags.
- You should still search the index before creating, but the bar for "new page is justified" is lower.
- After 30+ pages, normal reuse-first discipline kicks in automatically — at that point, most sources should update 3–8 existing pages and create 0–1 new ones.

## Categorization discipline (post-bootstrap)

Once out of bootstrap:

1. **Always read `wiki/index.md` first** before creating anything.
2. **Prefer updating over creating.** Look for existing pages that could absorb the new information.
3. **New page only when**: the entity/concept does not exist yet, or extending an existing page would make it incoherent.
4. **Never create a page per source.** Sources get a tiny summary in `wiki/sources/<type>/`. They drive updates to conceptual pages; they are not conceptual pages themselves.
5. **Vocabulary is controlled.** Pick from `wiki/_schema/`. New tags/domains/subcategories require explicit approval in a proposal.
6. **Subcategories can have multiple top players.** Do not force single winners.

## Things you must NOT do

- Do not modify `raw/` files.
- Do not modify `wiki/` in response to new sources without going through a proposal.
- Do not create a custom search CLI in `scripts/`. Use Claude Code's or Codex's Grep/Glob/Read.
- Do not use `WebFetch` for source ingestion. Always use `scripts/fetch_url.py`.
- Do not add `confidence:` fields to source or wiki frontmatter. Confidence is query-time only.
- Do not run semantic lint operations unless explicitly requested.
- Do not read `wiki/history/` on routine queries.
- Do not create personal/ pages unless asked.
- Do not modify `manual/` unless asked — it is user documentation, not wiki content.
- Do not apply a proposal containing unchecked items or reorder its structure. Re-read the file as the user left it.
- **Do not edit `CLAUDE.md` to change operating rules.** `CLAUDE.md` is only a pointer. All rule changes belong in `LLM-INSTRUCTIONS.md`.
