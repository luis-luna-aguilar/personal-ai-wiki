---
type: proposal
source: raw/newsletters/2026-08-21-ainews-poolside-gets-12b-reverse-execuhire-to-n.md
status: pending
created: 2026-09-07
---

# Proposal: AT&T case study — hybrid open/closed routing already at 40% of usage

## Summary

### The source
AINews's 2026-08-21 issue relays a Twitter summary (@Hesamation) of AT&T's internal AI deployment: 40% of employee AI usage already routes to open models, with an explicit target of 60-70%, and coding costs reportedly down 56% for only a ~2% quality drop, at 45B tokens/day. The same summary frames this as a warning sign for OpenAI/Anthropic's enterprise moat, with Ollama publicly welcoming AT&T's adoption as validation for open-model deployment at scale.

### What changes
The wiki's cost-aware-routing training page already tracks several named-company case studies (Databricks' internal FinOps breakdown, Every's cost-spike response, Bridgewater/Thinking Machines) but has no example yet of a large enterprise's aggregate open-vs-closed routing split.

- **Cost-aware AI task routing** gains one new Evidence-from-practice bullet on AT&T's routing percentages and cost/quality tradeoff, with as_of moving to 21 August.
- This raw file's source page is created by the companion harness-cluster proposal, whose draft already lists this page under its Influenced pages — no separate action needed here.

### What to weigh
This is a secondhand Twitter summary relayed through a newsletter, not an AT&T statement or a fetched primary writeup — no AT&T press release or blog post could be located from the captured content. Treat the specific percentages (40%/60-70%/56%/45B tokens per day) as reported, not independently verified.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — new Evidence-from-practice bullet, as_of bump
    > See draft below

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

```md
Frontmatter changes: as_of: 2026-08-21; sources: append ainews-poolside-nvidia-2026-08-21

## Evidence from practice (new bullet, appended at the end)

- **AT&T's open-model routing at scale.** AT&T reportedly routes 40% of employee AI usage to open models today, with an explicit target of 60-70%, citing coding costs down 56% for only a ~2% quality drop at 45B tokens/day (via a Twitter summary of AT&T's internal deployment, not an AT&T primary statement). Framed by outside commentary as a warning sign for closed-frontier labs' enterprise moat, and cited by Ollama as validation for open-model adoption at scale — a named Fortune-500 data point alongside this page's Databricks and Every case studies.
```

## Open questions

None beyond the sourcing caveat above.
