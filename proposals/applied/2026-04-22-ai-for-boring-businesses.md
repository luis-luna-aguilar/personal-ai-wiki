---
type: proposal
sources:
  - raw/newsletters/2026-03-10-ai-for-boring-businesses.md
  - raw/newsletters/2026-03-15-the-never-done-machine.md
  - raw/newsletters/2026-03-10-anthropic-drops-claude-code-review.md
status: pending
created: 2026-04-22
---

# Proposal: AI for boring businesses

## Summary

This cluster adds a grounded adoption layer the wiki should keep. The strongest lesson is that some of the best real-world AI opportunities are in operationally messy service businesses, not only in software-native demos. The supporting Every and Superhuman signals reinforce two adjacent points: teams should reward outcomes rather than AI usage itself, and AI often expands work/attention instead of cleanly removing it.

This should refine the existing enablement page rather than open a new concept.

## Intended changes

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add Main Street / operational-complexity guidance, outcome-over-usage framing, and one more human-adoption caveat
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/ai-for-boring-businesses.md` — source summary page for the cluster
  > See full draft below.

## Page drafts

### wiki/training/company-wide-ai-enablement.md (updated snippet)

```markdown
## Current guidance

- Start with a clear expectation from leadership that AI use is part of how work gets done
- Treat adoption as management and workflow design, not as software procurement
- Reward outcomes, speed, and quality improvements — not AI usage metrics by themselves
- Lower the activation barrier with one preconfigured agent surface, SSO, and pre-connected workplace tools
- Pair a small central platform team with distributed builders in each function

## Proven patterns

- **Operational-complexity targeting.** Some of the highest-leverage AI opportunities sit inside messy, regulated, service-heavy businesses where software is only one piece of the workflow.
- **Reward outcomes, not AI usage.** Teams stall or drift when "used AI" becomes the goal; quality and throughput improvements are the only metrics that matter.
- **Concrete example promotion.** A single visible example of someone using AI to rethink the work itself can unlock broader adoption better than generic encouragement to "use AI more."

## Failure modes

- Treating AI-usage metrics as the goal, which encourages outsourcing judgment to weak outputs
- Assuming an apparently replaceable human workflow will be accepted when automated; customers and coworkers are often more forgiving of humans making the same mistakes

## Evidence from practice

- Boulton and Watt argues operationally complex "boring businesses" such as funeral homes and aesthetic-clinic platforms may be stronger AI targets than software-native demos because software is becoming easier to build while real-world workflow complexity stays scarce
- Their examples suggest AI compresses market research and iteration cycles materially, but reliability and integration into live systems remain the hard part
- Their receptionist pilot found that customers churned more under AI even when error rates matched humans, reinforcing that perceived tolerance and trust shape adoption
```

### wiki/sources/newsletters/ai-for-boring-businesses.md (new)

```markdown
---
title: AI for boring businesses
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-10-ai-for-boring-businesses.md
published: 2026-03-10
ingested: 2026-04-22
domains: [agents, coding]
---

# AI for boring businesses

This source summary groups a small March cluster on practical AI adoption outside software-native glamour. The common thread is that AI creates leverage in operationally messy real businesses, but only when teams redesign work around outcomes, tolerate the human side of adoption, and avoid mistaking AI usage itself for progress.

## Influenced pages

- [[training/company-wide-ai-enablement]] — adds Main Street targeting, outcome-over-usage guidance, and a stronger trust/adoption caveat

## Key claims extracted

- Operationally complex service businesses may offer stronger AI opportunities than pure software businesses because real-world workflow complexity remains defensible even as software gets cheaper to build
- AI can compress research, prototyping, and iteration cycles substantially, but integration and reliability inside real systems remain the bottleneck
- Rewarding AI usage directly can lead teams to outsource judgment instead of improving outcomes
- Customers and coworkers are often more forgiving of human error than equivalent AI error, which makes adoption partly a trust problem rather than only a cost or accuracy problem
```

## Open questions

- None.
