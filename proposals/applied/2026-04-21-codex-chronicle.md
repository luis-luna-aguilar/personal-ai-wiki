---
type: proposal
sources:
  - raw/newsletters/2026-04-21-ainews-moonshot-kimi-k26-the-worlds-leading-o.md
status: pending
created: 2026-04-21
---

# Proposal: Codex Chronicle — Ambient Screen Memory for Coding Agents

## Summary

OpenAI shipped Codex Chronicle (research preview): background agents build memories from screenshots of recent screen activity, stored on-device with user inspection/editing. Rolling out to Pro users on macOS (not EU/UK/Switzerland). Harrison Chase (@hwchase17) immediately flagged "memory will be the great lock-in" — the competitive moat isn't the feature, it's the ambient context that accumulates over time.

## Intended changes

- [x] **Update** `wiki/tools/codex.md` — add Chronicle section; update `as_of`, `sources:`, and recent-change entry
    > **Frontmatter:** `as_of: 2026-04-21`, add `ainews-2026-04-21` to `sources:`
    >
    > **Add section after `## Pricing`:**
    > ```markdown
    > ## Codex Chronicle (as of 2026-04-21)
    >
    > Research preview. Background agents monitor recent screen activity, build memories from screenshots, and store them on-device. Users can inspect and edit stored memories.
    >
    > - Rollout: Pro users on macOS only; excluding EU, UK, Switzerland
    > - Shift from explicit chat history to passive ambient context capture
    > - Competitive framing: Harrison Chase ("memory will be the great lock-in") — ambient context accumulation becomes a switching cost, not just a convenience
    > ```
    >
    > **Add to `## Recent changes` (prepend):**
    > ```
    > - [2026-04-21] Codex Chronicle research preview — ambient screen memory; macOS Pro rollout
    > ```

- [x] **Update** `wiki/trends/proprietary-data-becomes-model-moat.md` — add ambient memory capture as a new variant of the data moat; bump `as_of`
    > **Add to the page body (under existing content, before or within a relevant section):**
    > ```
    > **Ambient memory capture as a new moat vector.** OpenAI's Codex Chronicle (April 2026) passively captures screen context and builds on-device memories from it. This is a different flavor of the proprietary data moat: the data isn't from a company's operational systems — it's from the individual user's work history. As context accumulates, switching tools means losing that context. Harrison Chase's framing: "memory will be the great lock-in."
    > ```
    > **Add to `## Recent changes` (prepend if section exists, or add it):**
    > ```
    > - [2026-04-21] Added ambient memory capture vector — Codex Chronicle as personal-context lock-in
    > ```
    > **Frontmatter:** add `ainews-2026-04-21` to `sources:`, update `as_of: 2026-04-21`

## Open questions

- Should "memory as lock-in" get its own trend page? Currently a note inside `proprietary-data-becomes-model-moat.md`, but it's a distinct mechanism (individual context vs. operational data). Flag if this trend grows in future sources.
	- Dont make it a page.

## Note

No new pages created. Source summary for AINews newsletter covered by the Kimi K2.6 proposal (`wiki/sources/newsletters/ainews-2026-04-21.md`).
