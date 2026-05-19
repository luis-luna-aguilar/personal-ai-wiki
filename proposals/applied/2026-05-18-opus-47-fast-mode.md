---
type: proposal
source: raw/newsletters/2026-05-14-opus-47-reels-us-back-in.md
status: pending
created: 2026-05-18
---

# Proposal: Opus 4.7 fast mode + return-from-Codex signal

## Summary

Anthropic released fast mode for Opus 4.7 on May 13: same model at 2.5× speed for ~6× the per-token cost. Separately, Every team members who had migrated to Codex after GPT-5.5 are returning — describing Opus 4.7 as a "senior magazine editor" versus Codex's "AP fact checker." This confirms fast mode as a meaningful quality/latency tier change, not just a speed tweak.

## Intended changes

- [x] **Update** `wiki/models/claude-opus-4-7.md` — add fast mode to Current status, add return-from-Codex quality signal, update `as_of` to 2026-05-13, add Recent changes entry
    > **as_of:** change `2026-05-05` → `2026-05-13`
    >
    > **Add to Current status (after the existing bullets):**
    > ```
    > - **Fast mode** (May 2026, research preview): 2.5× faster output at ~6× the per-token cost; same model depth as standard Opus 4.7; available via API and Claude Code
    > - Quality vibe shift: several Every team members who migrated to Codex after GPT-5.5 are returning; practitioner framing — Opus 4.7 feels like a "senior magazine editor," Codex like an "AP fact checker"; Opus remains stronger on planning, creative, and multi-step work
    > ```
    >
    > **Add to Recent changes:**
    > `- [2026-05-13] Fast mode shipped (research preview): 2.5× faster at ~6× cost; vibe checks report practitioners returning from Codex for planning and creative work`
    >
    > **Update sources list to include:** `opus-47-reels-us-back-in`

- [x] **Create** `wiki/sources/newsletters/opus-47-reels-us-back-in.md` — source summary

## Page drafts

### wiki/sources/newsletters/opus-47-reels-us-back-in.md (new)

```markdown
---
title: "Opus 4.7 Reels Us Back In — Every (Context Window)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-14-opus-47-reels-us-back-in.md
published: 2026-05-14
ingested: 2026-05-18
domains: [models, coding]
---

# Opus 4.7 Reels Us Back In — Every (Context Window)

Every's Context Window newsletter reports that several team members who migrated to Codex after GPT-5.5 are returning to Opus 4.7 — attributing it partly to fast mode (2.5× speed, ~6× cost, same model depth) and partly to a perceived quality resurgence in planning, creative, and multi-step work. The "senior magazine editor" vs. "AP fact checker" framing captures the qualitative distinction practitioners are drawing.

## Influenced pages

- [Claude Opus 4.7](../../models/claude-opus-4-7.md) — fast mode added; quality vibe signal

## Key claims extracted

- Anthropic released fast mode for Opus 4.7 on May 13, 2026
- Fast mode: 2.5× faster, ~6× cost per token, "same depth as 4.7"
- Multiple Every team members returning from Codex after fast mode + quality improvement signals
- Opus 4.7 described as "senior magazine editor"; Codex as "AP fact checker" (AP fact checker = fast but thin)
- Model performance may fluctuate by time of year (Mollick's "May is better than December" hypothesis noted)
```

## Open questions

- None.
