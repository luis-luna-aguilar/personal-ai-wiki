---
type: proposal
source: raw/newsletters/2026-02-25-ainews-the-unreasonable-effectiveness-of-closing.md
status: pending
created: 2026-04-22
---

# Proposal: Qwen 3.5 medium models in late February

## Summary

This is a lightweight-ingest candidate that strengthens an existing page rather than creating a new model. The useful signal is that the practical local-agent threshold story was already visible in the Qwen 3.5 medium release cycle before the later Qwen 3.6 framing in the wiki.

## Intended changes

- [x] **Update** `wiki/models/qwen-3-6-35b-a3b.md` — add the earlier Qwen 3.5 medium context that established the local-threshold story
- [x] **Update** `wiki/state-of/models.md` — note that the practical local-agent threshold narrative started in the late-February 3.5 medium cycle
- [x] **Create** `wiki/sources/newsletters/qwen-3-5-medium-february.md` — source summary page

## Page drafts

### wiki/models/qwen-3-6-35b-a3b.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- The "practical local-agent threshold" framing was already visible in the late-February Qwen 3.5 medium release cycle: a 35B-A3B MoE small enough for roughly 24GB-class hardware while still feeling strong enough to matter for coding and agent workflows
...
```

### wiki/state-of/models.md (updated snippet)

```markdown
### Coding models

- [[models/qwen-3-6-35b-a3b]] — Alibaba; the practical local-agent-threshold story started in the late-February Qwen 3.5 medium cycle and sharpened further by the later 3.6 framing *(as of 2026-02-25)*
```

### wiki/sources/newsletters/qwen-3-5-medium-february.md (new)

```markdown
---
title: Qwen 3.5 medium models in late February
type: source
source_type: newsletter
source_file: raw/newsletters/2026-02-25-ainews-the-unreasonable-effectiveness-of-closing.md
published: 2026-02-25
ingested: 2026-04-22
domains: [models, coding]
---

# Qwen 3.5 medium models in late February

This source cluster makes an important practical claim: Qwen's medium MoE release pushed open coding models toward a real local-agent threshold. The point is less "benchmark leader" than "small enough to run on accessible hardware while strong enough to matter for coding and agent workflows."

## Influenced pages

- [[models/qwen-3-6-35b-a3b]] — adds earlier context for the local-threshold framing
- [[state-of/models]] — sharpens the timing of the Qwen local-agent story

## Key claims extracted

- Qwen 3.5 medium models emphasized intelligence-per-watt, not only benchmark scale
- The 35B-A3B release was framed as viable on roughly 24GB-class hardware
- The local-agent baseline story predates the later Qwen 3.6 coverage already in the wiki
```

## Open questions

- None.
