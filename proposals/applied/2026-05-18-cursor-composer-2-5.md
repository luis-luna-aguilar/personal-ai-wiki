---
type: proposal
source: raw/articles/2026-05-18-cursorcom-blog-composer-2-5.md
status: pending
created: 2026-05-18
---

# Proposal: Cursor Composer 2.5

## Summary

Cursor shipped Composer 2.5, upgrading the long-horizon coding model. Built on the same Kimi K2.5 base as Composer 2 but trained with targeted RL + textual hints, 25× more synthetic tasks, and a new "feature deletion" task type. Adds a fast-inference pricing tier. Next model is in training at SpaceX scale on Colossus 2.

## Intended changes

- [x] **Update** `wiki/tools/cursor.md` — update `as_of`, add source to frontmatter, update Composer reference in Current status, add Recent changes entry
    > **`as_of`:** `2026-05-05` → `2026-05-18`
    >
    > **Sources frontmatter:** add `cursor-composer-2-5-launch`
    >
    > **In Current status — replace Composer 2 line:**
    > **Before:** `- Backed by [Composer 2](../models/composer-2.md), Cursor's own coding model for complex long-horizon tasks; late-March coverage adds reported 61.7 TerminalBench 2.0, 73.7 SWE-bench Multilingual, low input-token pricing, and the now-disclosed Kimi-k2.5 base-model lineage`
    > **After:** `- Backed by **Composer 2.5**, Cursor's in-house coding model (upgraded from Composer 2, May 2026): same Kimi K2.5 base, trained with targeted RL + textual hint injection at trajectory problem points, 25× more synthetic tasks than Composer 2, new "feature deletion" task type; pricing: $0.50/M input · $2.50/M output standard, $3.00/M · $15.00/M fast variant; next model in training at SpaceX/Colossus 2 scale (million H100-equivalents)`
    >
    > **Add to Recent changes (top):**
    > `- [2026-05-18] Composer 2.5: targeted RL with textual hints + KL distillation; 25× synthetic tasks; fast-tier pricing ($3/$15 per M); next model in training at SpaceX/Colossus 2 scale`

- [x] **Spill** `wiki/tools/cursor.md` → `wiki/history/tools/cursor.md` — Recent changes at cap (10); oldest entry falls off
    > **Create** `wiki/history/tools/cursor.md` (does not exist yet) with the spilled entry:
    >
    > ```md
    > # Cursor — History
    >
    > - [2026-04-02] Cursor 3 announced — rebuilt agent-first interface, multi-repo, local↔cloud handoff, Composer 2, plugin marketplace
    > ```

- [x] **Create** `wiki/sources/articles/cursor-composer-2-5-launch.md`
    > See draft below

## Page drafts

### wiki/sources/articles/cursor-composer-2-5-launch.md (new)

```md
---
title: Cursor Composer 2.5 — launch post
type: source
source_type: article
source_file: raw/articles/2026-05-18-cursorcom-blog-composer-2-5.md
url: https://cursor.com/blog/composer-2-5
published: 2026-05-18
ingested: 2026-05-18
domains: [coding]
---

# Cursor Composer 2.5 — launch post

Cursor's engineering post announcing Composer 2.5, the upgraded version of their in-house long-horizon coding model. Built on Kimi K2.5, trained with targeted RL using textual hints inserted at specific trajectory failure points plus KL distillation between a hinted teacher and an unhinted student. 25× more synthetic tasks than Composer 2, including a new "feature deletion" task type. Sharded Muon + dual mesh HSDP optimizer. Fast variant pricing: $3.00/M input · $15.00/M output. Next model: SpaceX training partnership on Colossus 2 (targeting million H100-equivalents).

## Influenced pages

- [Cursor](../../tools/cursor.md) — Composer 2 → 2.5 upgrade, training method, pricing, next model

## Key claims extracted

- Kimi K2.5 base (same as Composer 2)
- Targeted RL with textual feedback: hints inserted at problem trajectory points; KL distillation between hinted teacher and unhinted student
- 25× more synthetic tasks than Composer 2
- New "feature deletion" synthetic task type
- Sharded Muon + dual mesh HSDP optimizer; step time 0.2s on 1T model
- Standard pricing: $0.50/M input, $2.50/M output; fast variant: $3.00/M, $15.00/M
- SpaceX training partnership; next model on Colossus 2 (million H100-equivalents)
```
