---
type: proposal
source: raw/newsletters/2026-09-01-ainews-fals-h3-max-live-breaks-the-infinite-vid.md
status: pending
created: 2026-09-09
---

# Proposal: Transluce raises the bar for multi-turn agent safety evals

## Summary

### The source

AINews' 2026-09-01 issue reports that Transluce released an independent evaluation of 77 model variants across major labs, testing how each responds to mental-health crisis scenarios across multi-turn conversations rather than single-turn prompts. Several researchers treated it as a template for future agent evals: OpenAI's Wojciech Zaremba argued evals must increasingly simulate users, networks, and internet environments over long horizons rather than scoring isolated exchanges; others emphasized the need for ongoing audits rather than one-time predeployment checks, since a model's behavior under sustained, escalating pressure can differ from its behavior on a single prompt.

### What changes

**Agent evals** gains a new short section on multi-turn behavioral evaluation, positioned alongside its existing dollar/hours-denominated eval sections as a third distinct evaluation approach, plus a Recent-changes entry.

### What to weigh

This is a single-source proposal (one AINews recap of Transluce's release); no direct link to Transluce's own eval report was captured, so the page cites the newsletter's characterization rather than Transluce's methodology write-up directly.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/agent-evals.md` — add a multi-turn behavioral evals section; add 1 Recent-changes entry
    > See draft below

## Page drafts

### wiki/concepts/agent-evals.md (updated)

Insert this new section directly after `## Human-hours-equivalent productivity estimation` (and its content) and before `## How this changes eval design`:

```md
## Multi-turn behavioral evals

Transluce released an independent evaluation of 77 model variants across major labs, testing responses to mental-health crisis scenarios across multi-turn conversations rather than single-turn prompts. Several researchers treated it as a template for future agent evals: OpenAI's Wojciech Zaremba argued evals must increasingly simulate users, networks, and internet environments over long horizons rather than scoring isolated exchanges; others emphasized the need for ongoing audits rather than one-time predeployment checks, since sustained, escalating pressure can surface behavior a single prompt never would. This extends the trajectory-evaluation argument above (see "Why trajectory matters") from single-session tool-use paths to extended, adversarial-context conversations.
```

Recent changes — add this entry at the top:

```md
- [2026-09-01] Added multi-turn behavioral evals: Transluce's 77-model-variant mental-health-crisis eval, framed by researchers as a template for long-horizon, user/environment-simulating agent evals.
```

Frontmatter `as_of:` → `2026-09-01`; `sources:` — append `ainews-fal-h3-max-live-2026-09-01`.

## Open questions

None beyond the sourcing note above.
