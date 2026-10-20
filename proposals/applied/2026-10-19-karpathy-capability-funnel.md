---
type: proposal
source: raw/tweets/2026-10-19-karpathy-2109361546505966046.md
status: pending
created: 2026-10-19
---

# Proposal: Karpathy's LLM capability funnel

## Summary

### In short

The gap between what AI can do and what most people have seen it do is widening, which is why executives and engineers keep talking past each other about it. Andrej Karpathy estimates that about 75% of people have barely touched LLMs, 20% use free chatbots casually, and 0.2% use frontier agents professionally in math and code; he traces the spread to problem ambition, uneven capability and access tier. The proposal adds the funnel to AI labor-market effects and to Agent autonomy and governance. Reason to hesitate: it overlaps Every's existing note that most people sit at the chatbot levels.

[[#Open questions|Open questions: 1 to answer.]]

### The source

On 11 October 2026 Andrej Karpathy reposted a tweet of his from 9 April with a new argument on top. In April he had said people were "speaking past each other": those who tried free ChatGPT once judge AI by its quirks, while those who pay for frontier agents such as Codex and Claude Code for programming or research watch them finish days of work in an hour, and take the capability far more seriously.

In October he says the two-group picture has become a funnel. By his napkin math about 6 billion people (75%) have barely met an LLM. One to two billion (20%) are casual free-tier users who treat it as a better search box or writing aid; many professionals outside math and code sit here, including executives, who understand the shift intellectually but only second-hand. About 20 million (0.2%) use frontier models professionally in math and code and see projects that took weeks finished from a prompt. And roughly 5,000 people with internal access at the labs see swarms of agents working for weeks on large software, security and mathematics projects, with human review starting to fall behind.

He names three causes. Impact grows with the size and horizon of the problems you bring. Capability is "jagged": it peaks where tasks are digital, checkable and commercially valuable, because models are trained with reinforcement learning on verifiable rewards chosen for revenue. And access differs by tier: free, paid, internal.

### What changes

The wiki has no page on this tweet or its April predecessor. Its closest material is Every's note, on the governance page, that most people sit at the chatbot levels of an 8-level adoption ladder.

- **Agent autonomy and governance** gains a paragraph after that note giving Karpathy's population-scale funnel and its three drivers as enablement levers, plus his April point that views formed on last year's free tier understate current agents. One Recent-changes entry (two become three); page date moves from 28 August to 11 October.
- **AI labor-market effects** gains one Current-status bullet with the funnel's tiers and causes, and one Recent-changes entry (four become five). Its page date stays at 19 October.
- One new source page covering both tweets.

### What to weigh

The date is the post's "last edited" stamp; the capture gives no original posting time, so the post may be a few hours older. The funnel lands on two pages that already discuss adoption rather than on a new page; Karpathy's idea of jagged capability appears only as a driver, with a concept page left as the open question. His claims about the internal tier (agent swarms, the "OpenAI-HF incident", 722 mathematics manuscripts) stay on the source page only.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/agent-autonomy-and-governance.md` — add one paragraph in `## AI adoption and fluency levels`, after the "Where people sit" paragraph; adds one Recent-changes entry dated 2026-10-11 after the two 2026-10-19 entries (2 → 3, no spill); append source id to frontmatter `sources:` and one link to `## Sources`; `as_of` 2026-08-28 → 2026-10-11
- [ ] **Update** `wiki/trends/ai-labor-market-effects.md` — add one bullet at the end of `## Current status (as of 2026-10-19)`; adds one Recent-changes entry dated 2026-10-11 (4 → 5, no spill), placed after the two 2026-10-19 entries; append source id to frontmatter `sources:` and one link to `## Sources`; `as_of` stays 2026-10-19
- [ ] **Create** `wiki/sources/tweets/karpathy-capability-funnel-2026-10-11.md` — source summary

## Page drafts

### wiki/training/agent-autonomy-and-governance.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-11
sources: [agents-evals-deep-research, mckinsey-agentic-org, ramp-ai-adoption-playbook, ai-for-boring-businesses, token-tightening-ai-finops-2026-06, every-ai-sandwich-april-2026, every-cheap-competence-after-automation-2026-05, every-33-questions-executives-2026-08-28, every-ai-adoption-levels, karpathy-capability-funnel-2026-10-11]
```

`## AI adoption and fluency levels` — new paragraph inserted after the "**Where people sit (Every consulting, August 2026):**" paragraph and before "This ladder measures how people and teams use AI…":

```
**The population-scale view (Andrej Karpathy, October 2026).** Karpathy describes the same spread across everyone as a funnel: about 75% of people have barely used an LLM, about 20% are casual free-tier users (including many professionals outside math and code, and executives who know the shift mostly second-hand), about 0.2% use frontier agents professionally in math and code, and a few thousand people see unreleased systems inside the labs. His three drivers double as enablement levers. Impact scales with the size and horizon of the problems people bring, so a team needs real, large problems to see the upside. Capability is jagged, peaking where work is digital, checkable and commercially valuable, so functions outside engineering should expect smaller gains. And access tier caps what anyone can see: views formed on last year's free chatbot understate what current paid agents do.
```

`## Recent changes` (adds one entry dated 2026-10-11; the two live entries are dated 2026-10-19, so date order puts it last):

```
- [2026-10-19] Added Every's 8-level adoption maturity model from [Company-wide AI enablement](company-wide-ai-enablement.md), merged with the AI-fluency ladder that described the same framework.
- [2026-10-19] Page created, split out of [Company-wide AI enablement](company-wide-ai-enablement.md): its "Autonomy ladder" and "Humans in the loop vs. above the loop" sections and the "Governance, autonomy, and reliability" proven-patterns group.
- [2026-10-11] Added Karpathy's capability funnel (≈75% barely touched LLMs, ≈20% casual free-tier, ≈0.2% professional frontier-agent users) and its three drivers as the population-scale counterpart to Every's "where people sit".
```

`## Sources` (appends one link):

```
- [Andrej Karpathy on X — the LLM capability funnel](../sources/tweets/karpathy-capability-funnel-2026-10-11.md)
```

### wiki/trends/ai-labor-market-effects.md (updated)

Frontmatter (changed fields only; `as_of` unchanged at 2026-10-19):

```
sources: [ai-adoption-is-management, ramp-ai-adoption-playbook, mckinsey-agentic-org, stanford-labor-june-2026, anthropic-81k-economics, ainews-fable5-june-2026, anthropic-employment-report-2026-10, karpathy-capability-funnel-2026-10-11]
```

`## Current status (as of 2026-10-19)` — new bullet appended after the "Anthropic's internal employment report" bullet:

```
- **Exposure is a steep funnel, not a split (Karpathy, October 2026).** Andrej Karpathy's estimate: about 6B people (~75%) have barely touched LLMs; 1–2B (~20%) are casual free-tier users who treat them as a better search or writing aid, including many professionals outside math and code; about 20M (~0.2%) use frontier agents professionally in math and code and see weeks of work finished from a prompt; about 5,000 have internal access to unreleased systems. He traces the spread to problem ambition, capability that peaks in verifiable, commercially valuable domains, and access tier, and says the gap is widening.
```

`## Recent changes` (adds one entry dated 2026-10-11, after the two 2026-10-19 entries):

```
- [2026-10-19] Page created, split out of [Agents reshape organizations](agents-reshape-organizations.md)'s "Adoption, labor, and economic evidence" subsection, which had grown into its own topic.
- [2026-10-19] Added Anthropic's internal employment report: junior technical hiring share 27% → 9%, within-person productivity gains from coding-agent adoption with no measured quality drop.
- [2026-10-11] Added Karpathy's capability funnel: ~75% barely touched LLMs, ~20% casual free-tier, ~0.2% professional frontier-agent users, ~5,000 with internal access.
- [2026-06-16] Stanford 25,000-firm study: AI-exposed early-career workers (22-25) declining 3.8%/yr since 2022; junior software devs and customer service hardest hit; hollow pipeline concern is now data-backed
- [2026-06-10] Added ALE benchmark: 1,500+ tasks, 55 occupations, 300+ domain experts; top agents 2.6% on hardest tier — measurement of the gap between benchmark coding performance and real occupational task performance
```

`## Sources` (appends one link):

```
- [Andrej Karpathy on X — the LLM capability funnel](../sources/tweets/karpathy-capability-funnel-2026-10-11.md)
```

### wiki/sources/tweets/karpathy-capability-funnel-2026-10-11.md (new)

```
---
title: 'Andrej Karpathy on X — the LLM capability funnel'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-19-karpathy-2109361546505966046.md
url: https://x.com/karpathy/status/2109361546505966046
published: 2026-10-11
ingested: 2026-10-19
domains: [agents]
---

# Andrej Karpathy on X — the LLM capability funnel

Karpathy reposts his 9 April 2026 tweet (people "speaking past each other" about AI capability) and argues the gap has since widened into a funnel: most of the world has barely used LLMs, a large minority sees only free chatbots, a small professional group in math and code sees frontier agents finish weeks of work, and a few thousand lab insiders see far more. He attributes the funnel to problem ambition, jagged capability, and access tier. The date is the post's "last edited" stamp (11 October 2026); the original posting time is not in the capture. The quoted April tweet and the staysaasy post it quotes are covered here rather than as separate sources.

## Influenced pages

- [Agent autonomy and governance](../../training/agent-autonomy-and-governance.md) — population-scale funnel and its drivers added to the adoption and fluency levels section
- [AI labor-market effects](../../trends/ai-labor-market-effects.md) — new Current-status bullet on the distribution of exposure

## Key claims extracted

- The gap in shared understanding of LLM capability is widening: less "two groups speaking past each other", more "a sharp funnel"
- ~6B people (~75%) have barely come in contact with LLMs
- ~1–2B (~20%) are casual, infrequent free-tier users who see "derpy chatbots" used like a better Google search or writing aid; many professionals outside math and code are here, and executives understand the shift intellectually but second-hand
- ~20M (~0.2%) use frontier-grade LLMs professionally in math and code; projects that took weeks or months now finish from a prompt; Karpathy says he was still writing code by hand less than a year earlier
- ~5,000 people have internal access to frontier systems; he describes swarms of thousands of agents working for weeks on software, security and mathematics, with human review and comprehension starting to fall behind (citing the "OpenAI-HF incident" and 722 frontier-mathematics manuscripts)
- Drivers: (1) impact scales with ambition, problem size and horizon; (2) jaggedness: capability peaks in digital, verifiable, economically valuable domains because it comes from reinforcement learning on verifiable rewards over an environment mix chosen for revenue; (3) access: free, paid, internal
- Quoted April 9 tweet: views formed on old free-tier models (e.g. Advanced Voice Mode) understate current agentic tools such as Codex and Claude Code; paid frontier models are still "peaky" in technical domains; professional technical users assign far more gravity to capability and its cyber implications
- staysaasy (8 April, quoted in the April tweet): "The degree to which you are awed by AI is perfectly correlated with how much you use AI to code."
```

## Schema / vocabulary additions

None.

## Open questions

- Should Karpathy's "jagged capability" (capability peaking in verifiable, commercially valuable domains because of reinforcement learning on verifiable rewards) get its own concept page, or stay as one driver inside these two pages until a fuller source on it is ingested?
	- Stay as is
