---
type: proposal
source: raw/articles/2026-10-19-anthropiccom-engineering-redesigning-source-control.md
status: pending
created: 2026-10-19
---

# Proposal: Anthropic — Redesigning source control (Scion)

## Summary

### In short
Once agents write most of the code, developer infrastructure built for humans, starting with git and the merge queue, becomes the bottleneck, and a small team with Claude can now replace it outright. Anthropic's merges rose from about 2,500 a day in May to over 30,000 in September; seven people built a git replacement and migrated the monorepo in five months. The proposal adds the case study to the engineering evidence page and a bottleneck pattern plus an adversarial-review caveat to the engineering enablement page. One reason to hesitate: the article carries only an update date, so the page date is inferred.

[[#Open questions|Open questions: none.]]

### The source
Anthropic's source-control team published "Redesigning source control" on its engineering blog; the captured version is marked as updated on 15 October 2026. Merges to its monorepo went from about 2,500 a day in May to more than 30,000 a day in September. Git assumes every clone is a complete offline copy, but Anthropic's clients are almost all agents and jobs that are always online, and the repository outgrew that model: main-branch history near 100 GB and roughly 25 million CI checkouts a day, which at peak took several hundred internal git mirrors to serve.

So the team built Scion. The server answers history and blame questions and performs commits, merges and rebases; clients keep a small cache and check out only the directories they need, or none at all, since every source-control query is also an API. Reported results: infrastructure 200 times smaller than the mirror fleet, checkouts in seconds rather than minutes, and a 25% CI capacity gain.

The lessons go beyond source control. An early Claude Mythos Preview rewrote the hand-written ingestion pipeline, unprompted, to use 20 times less memory and run four times faster. Engineers now rate Claude a better code writer than themselves, but their job was often to tell it "no": agents broke core system constraints, and adversarial review sometimes pushed over-defensive complexity. Humans still review every change, for intent rather than line by line. Per-component Claude "superfan" channels watch telemetry, and the merge queue gave way to post-merge testing. Anthropic says the design only suits enormous monorepos, that its token spend is unusual, and that it will not release Scion; it wants git platforms to adopt server-side APIs instead.

### What changes
The wiki already carries Anthropic's earlier CI case (rebuilding a test-selection service rather than patching it) on both engineering pages; nothing yet covers source control or the merge queue.

- **Engineering AI adoption: evidence from practice** gains a Scion case-study bullet next to the CI case; its scale-data section, now too long to stay flat, gets three subheads with no text changed. One Recent-changes entry; page date moves to 15 October.
- **AI enablement — software development** gains a pattern on human-scale developer infrastructure as the next bottleneck, and its Adversarial-review bullet gains the over-engineering caveat. One Recent-changes entry brings the list to its cap of 10, no spill; page date moves to 15 October.
- The **index** line for the evidence page names the new case.
- One new source page.

### What to weigh
The publication date is inferred: the file gives only the 15 October update, so that date is used throughout. Scope: Software factory and Agent runtime platforms were left alone, since this is company developer infrastructure rather than an agent pipeline or the runtime around a harness.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/engineering-ai-adoption-evidence.md` — one new bullet under `## Scale data and large-scale case studies` after the Anthropic CI bullet plus three `###` subheads grouping that section's existing bullets (it would otherwise exceed the 800-word flat-section trigger), frontmatter `as_of` 2026-09-14 → 2026-10-15 and one source id appended, adds one Recent-changes entry dated 2026-10-15 (list goes 5 → 6, no spill), appends one Sources link
    > See draft below

- [ ] **Update** `wiki/training/ai-enablement-software-development.md` — one new bullet under `### Scale, cost, and CI`, one appended caveat on the Adversarial-review bullet, frontmatter `as_of` 2026-09-14 → 2026-10-15 and one source id appended, adds one Recent-changes entry dated 2026-10-15 (list goes 9 → 10, at cap, no spill), appends one Sources link
    > See draft below

- [ ] **Update** `wiki/index.md` — refresh the `training/engineering-ai-adoption-evidence` line and its as_of
    > See draft below

- [ ] **Create** `wiki/sources/articles/anthropic-redesigning-source-control-2026-10-15.md` — source summary

## Page drafts

### wiki/training/engineering-ai-adoption-evidence.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-15
sources: [shopify-latent-space-april-2026, ramp-ai-adoption-playbook, garrytan-gstack-repo, lennysan-simonw-interview, agentic-coding-trap-may-2026, stanford-labor-june-2026, shopify-claude-code-bessemer-2026-05, github-kyle-daigle-june-2026, ainews-june-05-2026, cognitioncom-blog-ai-productivity, bun-rust-rewrite-2026-07-16, openais-new-model-for-cyber-attacks-2026-07-16, anthropic-ci-test-impact-analysis-2026-09-14, anthropic-redesigning-source-control-2026-10-15]
```

`## Scale data and large-scale case studies` — full section. Adds the Scion bullet after the Anthropic CI bullet and, because the section would otherwise pass the 800-word flat-section trigger, groups its existing bullets under three `###` subheads (no existing text changes):

```
## Scale data and large-scale case studies

### Adoption and volume data

- Stanford Digital Economy Lab (June 2026): 25,000-firm study; AI-exposed early-career (22-25) jobs declining 3.8%/yr since 2022; least-exposed jobs growing 2.0%; junior software devs and customer service hardest hit. Hiring implications live on [AI-native hiring and the junior talent pipeline](ai-native-hiring-and-junior-talent.md).
- Shopify (May 2026, Bessemer conference, @darkzodchi synthesis): LLM proxy, CLAUDE.md discipline, critique loop, permission config deployed fleet-wide across 23,000 engineers. Reported 20% productivity gain. Strategy-to-execution ratio flipped from 30%/70% (2024) to 70%/30% (2026). Q3 2026 target: 90% autonomous coding.
- GitHub commit volume (June 2026): 275M AI-generated commits per week in April 2026, on pace for 14B in 2026 vs 1B in 2025. At this scale, CI/CD (GitHub Actions, specifically CPU capacity) is the bottleneck — not model capability or developer willingness.

### Anthropic internal data and infrastructure

- Anthropic internal RSI data (June 2026): The strongest first-party self-reported numbers from a frontier lab. Claude writes 80%+ of Anthropic's merged code commits. Engineers report shipping 8x more code per quarter than pre-Claude. Internal automated task success rate improved from 26% -> 76% over 6 months of harness iteration. Mythos Preview achieved a 52x speedup on a training script optimization task vs. 3x for Claude Opus 4 on the same task. Mythos gave better "next step" suggestions than humans 64% of the time. Caveat: self-reported, no independent verification.
- Anthropic's test-impact-analysis (test-selection) service (September 2026): as Claude came to author 80%+ of merged code and engineers shipped 8x more code per quarter, total tests grew 10x and CI jobs grew 25x over six months, repeatedly overloading the "listener/selector" service that decides which tests run on each PR. Three sequential patches — a bigger machine, package-level sharding, then daily restarts — bought 70 days, then 29 days, then under a day, before the team redesigned the service around an external in-memory data store so listener workers could be stateless and horizontally scalable; the redesign took three weeks for one engineer versus an estimated quarter a year earlier, which is the post's central point: overhauling infrastructure is now often cheaper than patching it, because writing the replacement is no longer the bottleneck. A long-running, service-dedicated Claude Tag session monitored the listener, paged the engineer, and retained context across months whenever lag crossed a threshold, repeatedly arguing for the eventual overhaul before the team acted on it. Anthropic's stated lesson: assume 25x load within two quarters, keep state out of any process meant to scale, and instrument services as "Claude's eyes and ears."
- Anthropic's Scion source-control system (October 2026): merges to Anthropic's monorepo grew from about 2,500 a day in May 2026 to more than 30,000 a day in September, and git, designed for offline clients that each hold a full copy, stopped fitting a repo with ~100 GB of main-branch history, a 25 GB+ compressed working copy, and on the order of 25 million CI checkouts a day (600+ PB/day if fetched naively), served at peak by several hundred internal git mirrors. A team of seven built Scion, an in-house version control system designed for always-online agent and job clients, plus a code-review tool (Antique) and half a dozen related systems, and fully migrated the monorepo off git in five months while daily merge volume grew 10x. The design moves the work to the server (history, blame, commits, merges, rebases), keeps clients to a bounded cache with sparse or virtualized checkouts, exposes every source-control query as an API so many CI jobs need no checkout at all (which is what makes automated bisect and revert pipelines practical), and makes commits cheap, incremental, and lock-free, discouraging branches and tags; it builds on Google's Piper and Meta's Sapling/Mononoke. Reported results: infrastructure 200x smaller in CPU and memory than the git mirrors, CI and research checkouts in seconds instead of minutes, and a 25% CI CPU capacity win. An early Claude Mythos Preview snapshot, asked with no further instructions to rewrite the hand-written git-to-Scion ingestion pipeline, produced a version using 20x less memory and running 4x faster while preserving its ordering invariants. Operations rely on per-component Claude Tag "superfan" Slack channels that watch telemetry and logs and catch subtle issues conventional alerts miss. Anthropic also dropped the global-lock merge queue in favor of post-merge and pre-deploy automated testing, letting Claude fix the concurrent-change conflicts that result. Anthropic's own limits: the design only makes sense for enormous monorepos, its internal token spend is far beyond what other businesses would choose, and Scion will not be released; it instead proposes git servers adopt comprehensive server-side APIs and composable sparse and shallow checkouts, and expects other AI-heavy organizations to hit this class of problem within six to twelve months.

### Measurement and large rewrites

- Cognition (Devin, July 2026): built an automated system estimating human-engineering-hours-equivalent per completed session, validated against 258 self-reported sessions from 126 users across enterprise customers, reaching `r_log = 0.74` on held-out data — stronger than Anthropic's ticket-text-only approach (0.46) though behind METR's smaller-sample internal study (0.83); deliberately calibrated to underestimate; now running in production with customers. See [Economic agent evals](../concepts/economic-agent-evals.md) for the full methodology comparison.
- Bun's Zig→Rust rewrite (Jarred Sumner, July 2026): a documented large-scale case study in adversarial-review-driven agentic refactoring. One Claude session implemented each change; two more, in fresh context windows with no visibility into the implementer's reasoning, reviewed the diff alone with the sole job of finding reasons it might fail — under a standing rule that a workaround needing a paragraph-long justifying comment is presumptively wrong. A shared porting guide and struct-lifetime table kept agents consistent across the 1,448-file codebase, which Sumner piloted on just 3 files before scaling up; Bun's own TypeScript test suite, unaffected by the underlying language, graded the port from the outside. Peak throughput ~1,300 lines/minute; total cost ~$165,000 in tokens.
```

`## Recent changes` — adds one entry dated 2026-10-15, placed below the 2026-10-19 entry (list goes 5 → 6). Full section:

```
## Recent changes

- [2026-10-19] Page created, split out of [AI enablement — software development](ai-enablement-software-development.md)'s "Evidence from practice" section; the origin keeps the guidance, patterns, and failure modes this evidence supports.
- [2026-10-15] Added Anthropic's Scion source-control case study (2,500 → 30,000+ merges/day, git replaced in five months by a seven-person team, 200x smaller infrastructure, merge queue replaced by post-merge testing); grouped the scale-data section under three subheads.
- [2026-09-14] Added Anthropic's test-impact-analysis CI-scaling case study (25x CI job growth, three successive patches, a three-week stateless redesign, a dedicated Claude Tag monitoring session).
- [2026-07-16] Added the Bun Zig→Rust rewrite case study: one implementer and two fresh-context adversarial reviewers, pilot-then-scale, ~$165K in tokens.
- [2026-07-14] Added Cognition's production session-productivity estimator (`r_log = 0.74`) as evidence that hours/dollar-denominated AI engineering ROI measurement is moving from research into deployed practice.
- [2026-06-05] Anthropic internal RSI evidence added: 80%+ merged code by Claude, 8x code/quarter, task success 26% -> 76%, Mythos 52x speedup on a training-script optimization task
```

`## Sources` — appends one link:

```
- [Redesigning source control at Anthropic](../sources/articles/anthropic-redesigning-source-control-2026-10-15.md)
```

### wiki/training/ai-enablement-software-development.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-15
sources: [ramp-ai-adoption-playbook, shopify-latent-space-april-2026, lennysan-simonw-interview, agentic-cognitive-overhead, the-code-2026-04-23, qa-tooling-for-software-agents-deep-research, agent-review-artifacts-2026-05-13, agentic-coding-trap-may-2026, ai-stack-fungibility-hashimoto-2026-05, shopify-claude-code-bessemer-2026-05, github-kyle-daigle-june-2026, software-factories-fde-2026-07, dashbench-code-review-understanding-2026-07, openais-new-model-for-cyber-attacks-2026-07-16, bun-rust-rewrite-2026-07-16, ubereng-software-factory-2026-08-28, anthropic-ci-test-impact-analysis-2026-09-14, anthropic-redesigning-source-control-2026-10-15]
```

`### Review and critique loops` — the Adversarial-review bullet, in full, with one appended caveat (last two sentences are new):

```
- **Adversarial review (implementer + fresh-context reviewers).** For high-stakes rewrites, split the work across roles instead of one agent doing both: one session implements each change, then one or more separate sessions — given only the diff, no access to the implementer's reasoning — review it with the sole job of finding reasons it might fail. A standing rule that a workaround needing a paragraph-long justifying comment is presumptively wrong keeps reviewers from rubber-stamping. Shared reference documents (a porting guide, a data-structure/lifetime table) keep every session consistent across a large effort; piloting the process on a handful of files before scaling to the full codebase catches process bugs cheaply. See the Bun Zig→Rust rewrite on [Engineering AI adoption: evidence from practice](engineering-ai-adoption-evidence.md) for the fullest documented example. The technique can be myopic: Anthropic's source-control team found adversarial review pushing Claude into excessive validation and complexity against hypothetical concerns, and agents breaking core system constraints to satisfy an existing pattern, so a large part of the engineers' role was telling Claude "no." Humans there still review every change, but for its intent rather than line by line.
```

`### Scale, cost, and CI` — appends one bullet after "Plan CI/test infrastructure for the exponential":

```
- **Expect human-scale developer infrastructure, not code, to be the next bottleneck.** Once agents write most of the code, source control, builds, CI, and the merge queue become the constraint, because they were designed for human clients working offline at human pace. Anthropic rebuilt rather than patched: a seven-person team replaced git for its monorepo in five months with a server-centric system built for always-online agent clients, exposed every source-control query as an API so jobs stop needing local checkouts, and swapped the global-lock merge queue for post-merge and pre-deploy testing, letting Claude resolve the resulting conflicts. Anthropic expects other AI-heavy organizations to hit this within six to twelve months; for most, its suggested route is pushing git platforms toward server-side APIs and better sparse checkouts rather than leaving git. Numbers on [Engineering AI adoption: evidence from practice](engineering-ai-adoption-evidence.md).
```

`## Recent changes` — adds one entry dated 2026-10-15, placed below the two 2026-10-19 entries (list goes 9 → 10, at cap, no spill). Full section:

```
## Recent changes

- [2026-10-19] Split "Evidence from practice" out to [Engineering AI adoption: evidence from practice](engineering-ai-adoption-evidence.md) and grouped Proven patterns under `###` subheads.
- [2026-10-19] Split "Hiring AI-native engineers" and "The junior talent problem" out to [AI-native hiring and the junior talent pipeline](ai-native-hiring-and-junior-talent.md), a separate audience (hiring managers and talent leads).
- [2026-10-15] Added "Expect human-scale developer infrastructure, not code, to be the next bottleneck" (Anthropic's Scion source-control rebuild) and a caveat on Adversarial review: it can be myopic and push over-engineering, so engineers say "no" and review intent rather than every line.
- [2026-09-14] Added Anthropic's test-impact-analysis CI-scaling case study: 25x CI job growth over six months, three successive patches (70/29/<1 days), a three-week stateless redesign (rebuilding now often cheaper than patching), and a dedicated Claude Tag monitoring session; new Proven-patterns bullet on planning CI/test infrastructure for exponential rather than linear growth.
- [2026-08-28] Added Uber's Software Factory adoption numbers (70%+ PRs agent-attributed, 3,600+ agent skills, 30K executions/day, 7x WAU growth) and its core strategic argument: eliminating wasted token consumption, not just cheaper unit prices, is what let usage scale 7x while unit costs fell.
- [2026-07-16] Corrected the Bun Zig→Rust rewrite figures in the Stack-fungibility bullet (535,496 lines, 11 days, ~$165K in tokens) and added a full case study of its one-implementer/two-adversarial-reviewer methodology, plus a new "Adversarial review" pattern generalizing the technique.
- [2026-07-08] Added AI PR/code-review workflow as a first-class enablement concern: historical PR replay, local review standards, and understanding-preserving review artifacts.
- [2026-07-01] Added software-factory/FDE rollout pattern: enterprise agent adoption needs workflow integration capacity, not only developer tooling.
- [2026-06-02] GitHub 14x agent commit growth added: 275M AI-generated commits/week in April 2026; CI/CD CPU capacity becomes bottleneck; micro-skills pattern added
- [2026-05-19] Shopify fleet patterns (Bessemer): LLM proxy, CLAUDE.md ~60-line cap, explicit allow/deny permission config; 20% productivity gain; strategy-to-execution ratio 70%/30% (was 30%/70%); Q3 target 90% autonomous coding
```

`## Sources` — appends one link:

```
- [Redesigning source control at Anthropic](../sources/articles/anthropic-redesigning-source-control-2026-10-15.md)
```

### wiki/index.md (updated)

Replaces the `training/engineering-ai-adoption-evidence` line:

```
- [training/engineering-ai-adoption-evidence](training/engineering-ai-adoption-evidence.md) — engineering AI adoption case studies and scale data: Shopify, Ramp, Garry Tan, Simon Willison, StrongDM, Lars Faye/Airbnb, GitHub commit volume, Anthropic RSI, CI scaling, and Scion source control, Cognition's productivity estimator, Bun's Zig→Rust rewrite *(as_of: 2026-10-15)*
```

### wiki/sources/articles/anthropic-redesigning-source-control-2026-10-15.md (new)

```
---
title: Redesigning source control at Anthropic
type: source
source_type: article
source_file: raw/articles/2026-10-19-anthropiccom-engineering-redesigning-source-control.md
url: https://www.anthropic.com/engineering/redesigning-source-control
published: 2026-10-15
ingested: 2026-10-19
domains: [coding, agents]
---

# Redesigning source control at Anthropic

An Anthropic engineering post on Scion, the in-house version control system that replaced git for Anthropic's monorepo once agent-written code pushed merges from ~2,500 to 30,000+ a day. It sets out the design principles for source control whose clients are always-online agents and jobs, how Scion's data model and tiered caches work, and broader lessons about building with Claude: small teams shipping large migrations fast, engineers steering rather than writing code, Claude "superfan" monitoring channels, and replacing the merge queue. The captured version is marked "Updated October 15"; the original publication date is not in the file, so `published:` uses the update date.

## Influenced pages

- [Engineering AI adoption: evidence from practice](../../training/engineering-ai-adoption-evidence.md) — Scion case-study bullet
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — new developer-infrastructure bottleneck pattern; adversarial-review caveat

## Key claims extracted

- Coding is no longer Anthropic's bottleneck; source control, builds, and CI (infrastructure built for human scale) are
- Merges per day: ~2,500 in May 2026, 30,000+ in September 2026; growth expected to continue
- Monorepo: main-branch history ~100 GB, compressed working copy 25 GB+, ~25M CI checkouts/day (600+ PB/day of git traffic if naive); several hundred internal git mirrors at peak
- Scion principles: clients always online; client-server asymmetry (server does history, blame, commits, merges, rebases); every source-control query exposed as an API; everything horizontally scalable, no fully materialized repo copy; cheap, incremental, lock-free commits with refs discouraged; working copy optional and sparse/virtualized by design
- Prior art: Google Piper, Meta Sapling (Mononoke server, Bonsai data model)
- Data model: changesets in a write-ahead log storing changed files vs first parent plus content-addressed blob pointers; "derived data" (blame, path history, commit-graph skip lists) computed recursively and eagerly or lazily
- Architecture: Spanner-backed scion-servers, regional scion-cache tier, per-node scion-daemon; identical RPCs across tiers; 99%+ cache hit rate per tier
- Results: infrastructure 200x smaller (CPU and memory) than git mirroring; checkouts in seconds instead of minutes; 25% CI CPU capacity win
- Seven people built Scion, Antique (code review), and half a dozen related systems and migrated in five months while daily merges grew 10x
- Early Claude Mythos Preview rewrote the hand-written ingestion pipeline with no further instructions: 20x less memory, 4x faster, invariants preserved
- Engineers rate Claude better at writing code than themselves; their role is often telling Claude "no" when agents violate system constraints or adversarial review drives over-engineering; humans review every change for intent, not every line
- Hermetic simulations, fuzzing, and rate limiting made Scion among the best-tested codebases the team has worked on
- Directory-level permissions and semantic approval constraints in code review (e.g. comment-only vs logic changes)
- Per-component Claude Tag "superfan" Slack channels monitor telemetry and logs and catch issues alerts miss
- Global-lock merge queue abandoned for post-merge and pre-deploy automated testing; Claude fixes concurrent-change conflicts
- Limits stated by Anthropic: only sensible for enormous monorepos; Anthropic's internal token spend is unusual; Scion will not be released; recommends git servers adopt server-side RPCs and composable sparse/shallow features; expects the problem class to spread within 6-12 months
```

## Schema / vocabulary additions

None.

## Open questions

None.
