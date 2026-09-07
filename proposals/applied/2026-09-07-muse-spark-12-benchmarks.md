---
type: proposal
source: raw/newsletters/2026-08-21-ainews-poolside-gets-12b-reverse-execuhire-to-n.md
status: pending
created: 2026-09-07
---

# Proposal: Muse Spark 1.2 picks up further third-party benchmark wins

## Summary

### The source
AINews's 2026-08-21 issue adds two more third-party benchmark data points for Muse Spark 1.2, beyond what's already on its wiki page: Agent Arena reports a +2.1% net improvement (up from +0.9% in v1.1), with a particularly strong Bash Recovery gain of +11.4%; and DesignArena ranks it #1 for Video-to-Website, #2 for Image-to-HTML, and #3 for Image-to-Frontend, describing it as sitting on the price/quality Pareto frontier.

### What changes
The wiki's Muse Spark page already covers 1.2's Vals Index and Finance Agent v2 results and its STEM Olympiad claims; this is an incremental extension, not a new story.

- **Muse Spark** gains one new sentence under its existing "Muse Spark 1.2" section and a Recent-changes entry. Page date moves to 21 August.
- Its Recent-changes list is already one over the 5-entry cap (6 live entries), so this proposal spills the 2 oldest entries (24 June and 10 April) to a new `wiki/history/models/muse-spark.md` file.
- This raw file's source page is created by the companion harness-cluster proposal, whose draft already lists this page under its Influenced pages — no separate action needed here.

### What to weigh
Nothing beyond the sourcing noted above — both figures are third-party benchmark providers (Agent Arena, DesignArena) relayed through AINews, consistent with how the rest of this page's benchmark data is already sourced.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/models/muse-spark.md` — one sentence added, Recent-changes entry, spill of 2 oldest entries to history, as_of bump
    > See draft below

- [ ] **Create** `wiki/history/models/muse-spark.md` — new history file with the 2 spilled entries
    > See draft below

## Page drafts

### wiki/models/muse-spark.md (updated)

```md
Frontmatter changes: as_of: 2026-08-21; sources: append ainews-poolside-nvidia-2026-08-21

## Muse Spark 1.2 breaks into frontier benchmarks (as of 2026-08-07) — one sentence appended at the end of this section

... Further third-party numbers followed on 2026-08-21: Agent Arena reported a +2.1% net improvement (up from +0.9% in v1.1), with a particularly strong Bash Recovery gain of +11.4%, and DesignArena ranked it #1 for Video-to-Website, #2 for Image-to-HTML, and #3 for Image-to-Frontend, describing it as sitting on the price/quality Pareto frontier.

## Recent changes (new entry, prepended; existing list re-capped to 5)

- [2026-08-21] Additional third-party benchmarks: Agent Arena +2.1% net improvement (Bash Recovery +11.4%); DesignArena #1 Video-to-Website, #2 Image-to-HTML, #3 Image-to-Frontend.
- [2026-08-11] Muse Glimmer ships as a smaller, open-weight (Apache 2.0) sibling model; Muse Spark 1.2's own weights promised "soon" — a reversal from Spark 1.1's closed API-only launch.
- [2026-08-07] Muse Spark 1.2 breaks into frontier-tier benchmarks: Vals Index top 5 at $0.69/test, first model above 60% on Finance Agent v2, five STEM Olympiad gold-medal-level results under no-tool conditions.
- [2026-07-09] Muse Spark 1.1 launches on the new Meta Model API — Meta's first paid, metered model; AA Intelligence Index 51 (+8 vs 1.0); Arena #9 Code Arena: Frontend.
- [2026-07-08] Muse Image launches in Meta AI, Instagram Stories, and WhatsApp; Muse Video previewed; AINews describes an agentic planning/tool-use/self-refinement generation loop.

<!-- The following 2 entries move to wiki/history/models/muse-spark.md: -->
<!-- [2026-06-24] Superhuman reports Meta Glasses launched with Muse Spark built in ... -->
<!-- [2026-04-10] Page created from Meta's Muse Spark introduction post -->
```

### wiki/history/models/muse-spark.md (new)

```md
# Muse Spark — History

## Archived from current page on 2026-09-07

- [2026-06-24] Superhuman reports Meta Glasses launched with Muse Spark built in; secondary coverage only.
- [2026-04-10] Page created from Meta's Muse Spark introduction post
```

## Open questions

None.
