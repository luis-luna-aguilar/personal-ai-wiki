---
type: proposal
source: raw/newsletters/2026-03-02-how-to-kill-the-code-review.md
status: pending
created: 2026-04-22
---

# Proposal: Post-vibe-coding verification and cognitive debt in late February

## Summary

This is the strongest training/workflow signal in the batch. The core claim is that once agents write most of the code, the scarce human work moves upstream: specifications, acceptance criteria, deterministic verification, and understanding enough of the generated system to avoid cognitive debt.

## Intended changes

- [x] **Update** `wiki/training/ai-native-product-building.md` — add upstream verification and acceptance-criteria guidance
- [x] **Update** `wiki/training/anti-autopilot-review-friction.md` — add the "review specs and verifiers, not diffs" framing
- [x] **Create** `wiki/sources/newsletters/post-vibe-coding-verification-february.md` — source summary page

## Page drafts

### wiki/training/ai-native-product-building.md (updated snippet)

```markdown
## Proven patterns

- **Move judgment upstream.** As agents generate more code, the most valuable human work shifts toward writing specs, acceptance criteria, and deterministic verification steps instead of skimming large diffs after the fact
- **Fight cognitive debt deliberately.** Use walkthroughs, explanations, and other artifacts that make generated systems understandable enough to extend safely later
```

### wiki/training/anti-autopilot-review-friction.md (updated snippet)

```markdown
## Proven patterns

- **Review the gates, not only the output.** In agent-heavy coding workflows, judgment increasingly belongs on specs, acceptance criteria, and verification scripts instead of only on generated diffs
```

### wiki/sources/newsletters/post-vibe-coding-verification-february.md (new)

```markdown
---
title: Post-vibe-coding verification and cognitive debt in late February
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-02-how-to-kill-the-code-review.md
published: 2026-03-02
ingested: 2026-04-22
domains: [coding]
---

# Post-vibe-coding verification and cognitive debt in late February

This source cluster argues that the bottleneck after vibe coding is no longer writing code faster, but defining what success means and verifying it deterministically. Related material adds that generated systems also create cognitive debt unless teams deliberately produce walkthroughs and explanations that keep the architecture legible.

## Influenced pages

- [[training/ai-native-product-building]] — adds upstream verification and cognitive-debt guidance
- [[training/anti-autopilot-review-friction]] — shifts review judgment toward specs and verifiers

## Key claims extracted

- Manual diff review does not scale once agents write most of the code
- Acceptance criteria and verification artifacts should be defined before implementation
- Generated systems create cognitive debt unless teams actively improve understanding
```

## Open questions

- None.
