---
type: proposal
sources:
  - raw/newsletters/2026-09-01-vibe-check-fable-51anthropic-is-so-back-again.md
  - raw/newsletters/2026-09-02-ainews-claude-fablemythos-51-new-sota-model.md
status: pending
created: 2026-09-09
---

# Proposal: Claude Fable 5.1 / Mythos 5.1 launch

## Summary

### The source

On 2026-09-01, Anthropic launched Claude Fable 5.1 and Claude Mythos 5.1 as paired flagship releases — Fable 5.1 for delegated, long-horizon coding and knowledge work, Mythos 5.1 for knowledge work specifically. Every's Katie Parrott and Dan Shipper reviewed it the same day: faster, clearer, less resistant to correction than Fable 5, enough that several Every staff moved work back to Claude from ChatGPT/Codex, though it still overruns briefs, invents quotations, and sometimes keeps working past a stop request. AINews' deeper AI-Twitter-recap piece the next day adds the numbers: pricing holds at $10/$50/$12.5 per million input/output/cache-write tokens, but cache-read pricing drops 75% to $0.25/M — a targeted win for agentic workflows that repeatedly re-read cached context. Artificial Analysis put its Intelligence Index at 66, ahead of Opus 5 (63), Fable 5 (62), and GPT-5.6 Sol (61), with Terminal-Bench-Science more than doubling (24.7% → 52.6%). The catch: output-token usage rose ~1.7x, so per-task cost is actually ~20% higher than Fable 5 despite the cache cut. A new safety layer, Enterprise Frontier Safeguards, gives enterprises cross-session agent observability but produced real false positives — one tester couldn't finish evaluating the model because benign technical prompts kept triggering flags. The most technically interesting thread: credible community analysis (@eliebakouch) holds that Fable and Mythos 5.1 are literally the same weights, with a safety classifier deciding whether a request escalates and falls back to Opus 4.8 — a claim Artificial Analysis's own evaluation indirectly corroborates (it recorded ~4% of output tokens served by fallback) without confirming the "same weights" claim outright.

### What changes

The wiki currently treats Claude Fable 5 (as_of 2026-07-02) as Anthropic's coding flagship. This proposal supersedes it.

- **New page** `models/claude-fable-5-1.md` documents both Fable 5.1 and Mythos 5.1 together as one paired release, including the same-weights/different-routing debate and a note distinguishing this Mythos 5.1 from the older, unrelated `claude-mythos-preview.md` (a restricted-access cybersecurity model from Project Glasswing).
- **Claude Fable 5**'s full content moves to `wiki/history/models/claude-fable-5.md` with a superseded-by pointer, following the same pattern already used for GLM-5.2 → GLM-5.3.
- **State of Models** swaps its Frontier-models leader line from Fable 5 to Fable 5.1/Mythos 5.1 and adds one Recent-changes entry; because that list is already at its 10-entry cap, the oldest entry spills to history.
- **Claude Mythos Preview** gains one short disambiguation note pointing to the new page, so a reader doesn't conflate the two "Mythos" names.
- Two new source pages capture the Every and AINews coverage.

### What to weigh

Both sources are secondary/community coverage (Every's own review, and AINews' aggregation of X threads including Artificial Analysis's numbers) rather than an Anthropic primary announcement — no Anthropic blog post URL was captured in either source. The "same weights, different routing" claim, while corroborated indirectly by Artificial Analysis's fallback-routing measurement, remains a community inference (@eliebakouch), not an Anthropic statement, and is presented on the new page as such. The naming collision between this Mythos 5.1 and the pre-existing, unrelated Claude Mythos Preview page is a judgment call — I've added a disambiguation note rather than merging or renaming either page, since current sources don't establish a lineage relationship between them.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Create** `wiki/models/claude-fable-5-1.md` — new current page for Fable 5.1 / Mythos 5.1
    > See draft below

- [ ] **Spill** `wiki/models/claude-fable-5.md` → `wiki/history/models/claude-fable-5.md` — full page archived, superseded-by pointer added, live page removed
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — swap Fable 5 leader line for Fable 5.1/Mythos 5.1; add 1 Recent-changes entry (list is at the 10-entry cap, so the oldest entry spills to `wiki/history/state-of/models.md`)
    > See draft below

- [ ] **Update** `wiki/models/claude-mythos-preview.md` — add a short disambiguation note and one Recent-changes entry; append the new source to `sources:`
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-fable-51-vibe-check-2026-09-01.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/ainews-fablemythos-51-2026-09-02.md` — source summary (also influences other pending proposals in this digest batch: Qwen 3.8, Open-weight momentum, AGI timeline claims, Agent safety and alignment research)

## Page drafts

### wiki/models/claude-fable-5-1.md (new)

```md
---
title: Claude Fable 5.1 / Mythos 5.1
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [anthropic, frontier]
as_of: 2026-09-02
sources: [every-fable-51-vibe-check-2026-09-01, ainews-fablemythos-51-2026-09-02]
---

# Claude Fable 5.1 / Mythos 5.1

Anthropic's flagship refresh, launched 2026-09-01, superseding [Claude Fable 5](../history/models/claude-fable-5.md). Fable 5.1 targets delegated, long-horizon coding and knowledge work; Mythos 5.1 is a paired release positioned for knowledge work. Credible community analysis (@eliebakouch, corroborated by Artificial Analysis' own fallback-routing note) holds that Fable and Mythos 5.1 are the same underlying weights, differentiated by a safety-classifier threshold rather than distinct base models — flagged requests fall back to Opus 4.8.

## Current status (as of 2026-09-02)

- Pricing unchanged from Fable 5: $10/$50/$12.5 per million input/output/cache-write tokens; cache-read price cut 75% ($1.00 → $0.25/M), a targeted win for agentic workloads that repeatedly re-read cached context.
- Artificial Analysis Intelligence Index 66 (Fable 5: 62; Opus 5: 63; GPT-5.6 Sol: 61) — back on the frontier ceiling after Fable 5's mid-pack showing against GPT-5.6 Sol.
- HLE 65% with tools; Terminal-Bench v2.1 91.4%; Terminal-Bench-Science more than doubled, 24.7% → 52.6%.
- Output-token usage rose ~1.7x versus Fable 5, so per-task cost is ~20% higher despite the cache-read cut ($3.76/task at max effort).
- New Enterprise Frontier Safeguards (EFS) add cross-session agent observability; several practitioners — including one who could not complete testing — hit false-positive safety flags on benign technical/theoretical prompts.
- Widely reported stylistic shift toward "less Claudese" (fewer em dashes and hyphenated compounds, per ValsAI lexical stats), though outputs also got longer overall (e.g. Terminal-Bench task outputs: 961 → 1299 words).

## Same weights, different routing

Community technical analysis converged on: Fable and Mythos 5.1 share weights; internal activations are inspected and escalate to a larger safety classifier, with dangerous requests falling back to Opus 4.8. Artificial Analysis independently confirmed fallback routing in its own evaluation (~4% of output tokens served by fallback) without confirming the "exact same weights" claim directly. If accurate, which benchmark line is labeled Fable vs. Mythos is closer to a safety-routing artifact than a distinct-model comparison — a live open question in system-card interpretation.

Note: this Mythos 5.1 is a new, publicly available paired release, distinct from [Claude Mythos Preview](claude-mythos-preview.md), Anthropic's earlier restricted-access cybersecurity-research model (Project Glasswing). The two share a name but not, per current sources, an established lineage.

## Strengths

- Frontier-ceiling benchmark gains, especially on hard agentic/science coding tasks (Terminal-Bench-Science)
- Cache-read cost cut materially helps long-running agent sessions that repeatedly re-read prior context
- Practitioner-reported writing-quality improvement: clearer prose, fewer "AI tells"

## Weaknesses / caveats

- Net cost per task is higher, not lower, due to increased output-token usage
- Enterprise Frontier Safeguards produced real false positives on benign prompts in first-week use
- Fable/Mythos routing ambiguity makes some system-card benchmark lines hard to attribute to "the model" vs. "the safety path"

## Recent changes

- [2026-09-01] Fable 5.1 / Mythos 5.1 launched, superseding Fable 5: AA Intelligence Index 66, 75% cache-read price cut, same-weights/different-routing debate, EFS false positives.

## Sources

- [Every — Vibe Check: Fable 5.1](../sources/newsletters/every-fable-51-vibe-check-2026-09-01.md)
- [AINews — Claude Fable/Mythos 5.1: new SOTA model](../sources/newsletters/ainews-fablemythos-51-2026-09-02.md)
```

### wiki/history/models/claude-fable-5.md (new)

```md
---
title: Claude Fable 5
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [anthropic, frontier]
as_of: 2026-07-07
sources: [fable-ban-june-2026, ainews-fable5-june-2026, every-fable5-vibe-check, ainews-not-much-happened-2026-07-02, every-tale-of-two-models-2026-07-05, claude-sonnet-5-official-2026-06-30, fable-unknowns-routing-2026-07]
---

# Claude Fable 5

Anthropic's frontier model, launched June 9 2026 as the first generally available Mythos-class model. Described by Anthropic as "at least 2× the size of Opus." Reached #1 across nearly all major benchmarks at launch, was briefly suspended worldwide under US government export controls, and returned online July 2 with safety fallback routing.

**Superseded by [Claude Fable 5.1 / Mythos 5.1](../../models/claude-fable-5-1.md), 2026-09-01.**

## Current status (as of 2026-07-02)

- Re-enabled after the June 2026 suspension, with demand immediately returning across coding-tool vendors.
- Anthropic is applying updated safety fallback routing: some cyber, biology, and chemistry requests may route to Opus 4.8 instead of Fable 5.
- Cursor reports Fable 5 still leads its internal coding evals but is the most expensive per completed task.
- Devin, Perplexity, Cursor, and other tooling surfaces restored Fable 5 shortly after relaunch.
- The operational lesson is model-routing resilience: teams should not build critical coding workflows around one frontier model with no fallback.

## Benchmark record (pre-ban)

- **SWE-Bench Pro:** 80.3% (vs GPT-5.5 58.6%)
- **DeepSWE index:** #1; Claude Code + Fable 5 [max] scored 77 on the Artificial Analysis DeepSWE index
- **FrontierCode Diamond:** 29.3% (Fable 5); 30.9% (Mythos 5) — vs prior best 13.4%
- **FrontierSWE:** #1
- **Terminal-Bench 2.1:** 88.0% (Cline; 4.6 points above GPT-5.5)
- **CursorBench:** SOTA 72.9% (8 points above prior best)
- **FrontierMath Tiers 1-4:** 87% / 88%
- **Humanity's Last Exam:** 53% — 7+ points ahead of next best; ~9% of HLE tasks triggered fallback
- **Artificial Analysis Intelligence Index:** #1 (64.9, ~5 points ahead of GPT-5.5)
- **GDPval-AA Elo:** 1932 (#1 agentic real-world knowledge work)
- **WeirdML:** 87.8%
- **Epoch Capabilities Index:** 161 (new all-time high at launch)
- **Every Senior Engineer benchmark:** 91/100 — vs Opus 4.8 (63) and GPT-5.5 (62)
- **Code Arena (frontend coding):** #1 (Fable unavailable → GLM-5.2 moved to #1)
- **Design Arena:** #1 (same)

## Pricing & access

- **API:** $10 per million input tokens; $50 per million output tokens (approx 2× Opus 4.8, 3× Sonnet 4.6)
- **Cache:** $12.50/M writes, $1/M reads
- **Context:** 1M tokens
- **No ZDR:** 30-day retention for all Mythos-class model traffic (not used for training; privacy controls applied; deletions after 30 days)
- **Subscription access:** Available in Pro/Max/Team/Enterprise until June 22 at launch, then credit-gated due to capacity constraints
- Silent RSI suppression: for frontier LLM development tasks (~0.03% of traffic), Anthropic may silently reduce effectiveness via prompt modification, steering vectors, or PEFT without notifying the user

## What Fable 5 was notable for

Practitioners described it as the first model they trusted for long, complex, minimally supervised tasks — whole-project delegation rather than function-level assistance.

- **Every Senior Engineer benchmark:** 91/100 — near human engineer range; Opus 4.8 scored 63, GPT-5.5 scored 62
- **Every's verdict:** "Strong closer that wants a clear target — treat it as an asynchronous agent, not a chat partner"
- Level 7–8 AI users found it paradigm-shifting; lower-level users struggled to find clear use cases
- One-shot app building: users built a 3D Library of Babel, a subscriber survey analysis app, and a custom Hubert Dreyfus lecture player with single prompts
- Ethan Mollick: could hand it a 15-page design document and it would work for 9+ hours autonomously
- Anthropic cited Stripe using Fable to complete a 50M-line Ruby migration in a day, replacing what would have taken a team over two months
- Usage profile: 500k–1M tokens per long-running task; Simon Willison described it as "slow, expensive and capable"
- Anthropic advised: default to `xhigh/high` effort; rewrite old CLAUDE.md instructions; give objectives/responsibilities rather than tasks; use Fable as an orchestrator delegating to smaller models via Claude Managed Agents

## What Fable 5 is best used for

Every's July 2026 guidance sharpens Fable's practical niche: do not reserve it only for the biggest tasks by size. Reserve it for tasks where the assignment may be incomplete, the standard is unstated, or the target itself may be wrong.

- Use Fable to surface "unknown knowns": criteria obvious to the user but not written in the prompt.
- Use Fable to surface "unknown unknowns": questions or invalid premises the user has not considered.
- Use cheaper models when the goal, constraints, and definition of good are already settled.
- Use Fable to turn a hard recurring job into scripts, skills, examples, and quality checks that cheaper models can execute later.

## Weaknesses / caveats

- Benchmark positions mostly come from launch/pre-ban coverage, but Fable 5 access has returned. Anthropic now applies safety fallback routing, so some sensitive or routine tasks may route to Opus 4.8 instead of Fable 5.
- The ban reveals a new structural risk: regulatory action can remove access to a frontier model faster than any vendor deprecation.
- Classifier over-sensitivity at launch: users reported "cancer" and "What does the heart do?" triggering biosecurity fallback; Anthropic reset rate limits after heavy demand.

## Recent changes

- [2026-09-01] Superseded by Claude Fable 5.1 / Mythos 5.1 — see [Claude Fable 5.1 / Mythos 5.1](../../models/claude-fable-5-1.md).
- [2026-07-07] Every frames Fable's premium use case as finding unknowns and invalid premises before execution, then converting recurring work into cheaper-model instructions and scripts.
- [2026-07-02] Fable 5 returned online; Anthropic added visible safety fallback routing to Opus 4.8 for some sensitive domains; major coding tools restored access.
- [2026-06-30] Sonnet 5 launch cluster also confirmed Fable 5 access had returned with fallback routing still relevant.
- [2026-06-17] Access suspended globally under US export controls; ban ongoing; Anthropic disputes scope of trigger jailbreak

## Sources

- [AINews — Claude Fable 5 / Mythos 5 launch (June 10)](../../sources/newsletters/ainews-fable5-june-2026.md)
- [Every vibe check: Fable 5 (June 8)](../../sources/articles/every-fable5-vibe-check.md)
- [Claude Fable 5 / Mythos ban coverage](../../sources/newsletters/fable-ban-june-2026.md)
- [AINews - not much happened today](../../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [Every - A Tale of Two Models](../../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
- [Claude Sonnet 5 official launch](../../sources/articles/claude-sonnet-5-official-2026-06-30.md)
- [Fable for unknowns and cheaper specialists for settled work](../../sources/newsletters/fable-unknowns-routing-2026-07.md)
```

### wiki/state-of/models.md (updated)

Frontier models bullet — replace:

```md
- [Claude Fable 5](../models/claude-fable-5.md) — Anthropic; SWE-Bench Pro 80.3%, FrontierCode Diamond 29.3%, HLE 53%, Terminal-Bench 2.1 88.0%, AA Intelligence Index #1 (64.9); re-enabled with safety fallback routing to Opus 4.8 for some sensitive domains *(as of 2026-07-02)*
```

with:

```md
- [Claude Fable 5.1 / Mythos 5.1](../models/claude-fable-5-1.md) — Anthropic; supersedes Fable 5; AA Intelligence Index 66, Terminal-Bench v2.1 91.4%, 75% cache-read price cut; same weights as Mythos 5.1 with different safety-classifier routing per community analysis *(as of 2026-09-02)*
```

Recent changes — add this entry at the top (list is at the 10-entry cap; the oldest entry, `[2026-07-24] Claude Opus 5 launched...`, spills to `wiki/history/state-of/models.md`):

```md
- [2026-09-01] Claude Fable 5.1 / Mythos 5.1 launched, superseding Fable 5: AA Intelligence Index 66 (was 62), 75% cache-read price cut, same-weights/different-safety-routing debate between the two paired model names.
```

### wiki/models/claude-mythos-preview.md (updated)

Add this section directly after the intro paragraph (before `## Current status (as of 2026-05-23)`):

```md
**Note:** In September 2026, Anthropic separately launched a public, paired knowledge-work model also named Mythos (Mythos 5.1, alongside Fable 5.1) — see [Claude Fable 5.1 / Mythos 5.1](../models/claude-fable-5-1.md). The two share a name but, per current sources, not an established lineage; this page's Mythos Preview remains the restricted-access Project Glasswing cybersecurity-research model.
```

Recent changes — add this entry at the top:

```md
- [2026-09-01] Anthropic launched a distinct, publicly available Mythos 5.1 alongside Fable 5.1 — added a disambiguation note; no lineage established between the two.
```

Frontmatter `sources:` — append `ainews-fablemythos-51-2026-09-02` to the existing list.

### wiki/sources/newsletters/every-fable-51-vibe-check-2026-09-01.md (new)

```md
---
title: "Every — Vibe Check: Fable 5.1"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-01-vibe-check-fable-51anthropic-is-so-back-again.md
url: https://every.to/vibe-check/fable-5-1-vibe-check
published: 2026-09-01
ingested: 2026-09-09
domains: [models, coding]
---

# Every — Vibe Check: Fable 5.1

Every's Katie Parrott and Dan Shipper review Anthropic's Fable 5.1 launch: faster, clearer, less argumentative than Fable 5, prompting several Every staff to move work back to Claude from ChatGPT/Codex — while flagging it still overruns briefs, can invent quotations, and sometimes keeps working past a stop request.

## Influenced pages

- [Claude Fable 5.1 / Mythos 5.1](../../models/claude-fable-5-1.md) — launch coverage and practitioner framing
- [State of Models](../../state-of/models.md) — leader-line update

## Key claims extracted

- Fable 5.1 released 2026-09-01, successor to Fable 5
- Faster, clearer prose, less resistant to course-correction than Fable 5
- Still overruns briefs, can invent quotations, sometimes keeps working when asked to stop
- Every's automated editing pipeline stays on Opus 5 rather than switching to Fable 5.1
```

### wiki/sources/newsletters/ainews-fablemythos-51-2026-09-02.md (new)

```md
---
title: "AINews — Claude Fable/Mythos 5.1: new SOTA model"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-02-ainews-claude-fablemythos-51-new-sota-model.md
url: https://www.latent.space/p/ainews-claude-fablemythos-51-new
published: 2026-09-02
ingested: 2026-09-09
domains: [models, agents]
---

# AINews — Claude Fable/Mythos 5.1: new SOTA model

AINews' AI Twitter recap deep-dive on Anthropic's Fable 5.1/Mythos 5.1 launch: benchmarks, pricing, the same-weights/different-safety-routing debate, Enterprise Frontier Safeguards false positives, and the "less Claudese" stylistic shift — plus same-day coverage of OpenAI's Astra preparedness/architecture debate, Qwen3.8-Max-0902's #1 WebDev result, and World Labs' Atlas world model.

## Influenced pages

- [Claude Fable 5.1 / Mythos 5.1](../../models/claude-fable-5-1.md) — primary launch coverage
- [State of Models](../../state-of/models.md) — leader-line update
- [Qwen 3.8](../../models/qwen-3-8.md) — Qwen3.8-Max-0902 #1 WebDev result
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Qwen3.8-Max-0902 data point
- [AGI timeline claims](../../trends/agi-timeline-claims.md) — Astra "Critical" cyber-capability preparedness milestone
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — Astra recurrent-depth/CoT-monitorability debate

## Key claims extracted

- Fable 5.1 pricing: $10/$50/$12.5 per MTok input/output/cache-write (unchanged), cache-read cut 75% to $0.25/MTok
- Artificial Analysis Intelligence Index 66 (Opus 5: 63, Fable 5: 62, GPT-5.6 Sol: 61); HLE 65% with tools; Terminal-Bench v2.1 91.4%
- Output tokens ~1.7x Fable 5's, so per-task cost ~20% higher despite cache cut ($3.76/task at max effort)
- Community claim (@eliebakouch): Fable and Mythos 5.1 are the same weights, differing by safety-classifier threshold; ~4% of output tokens fall back to Opus 4.8 per Artificial Analysis
- OpenAI's Astra hit the "Critical" cyber-capability threshold under OpenAI's Preparedness Framework; reporting describes a recurrent-depth/"looped transformer" architecture, disputed by OpenAI chief scientist @merettm (~2x GPT-4 computation-graph depth, CoT monitoring still a research priority)
- Alibaba's Qwen3.8-Max-0902 (2.4T params, 1M context, $2/$6 per MTok) debuted #1 on Arena's Code Arena: WebDev (1691), ahead of Claude Opus 5 Max and Kimi K3 Max
```

## Open questions

- Whether Anthropic ever publishes a primary blog post distinguishing Fable 5.1 from Mythos 5.1 more formally than the community "same weights, different routing" account — if so, the new page should be updated to cite it directly.
- Whether the pre-existing `claude-mythos-preview.md` page should eventually be renamed to reduce naming confusion with the new public Mythos 5.1, or left as-is now that a disambiguation note exists (assumed: leave as-is for now).
