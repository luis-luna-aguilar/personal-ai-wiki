---
type: proposal
source: raw/tweets/2026-10-28-thorstenball-2114386050638336082.md
status: pending
created: 2026-10-28
---

# Proposal: Thorsten Ball — How I work with Agents

## Summary

### In short
Thorsten Ball's rule for coding agents is to stop steering the method and start demanding evidence. Agents should see and act on the whole software lifecycle, prove their work with walkthroughs and numbers, and get human code review only where a mistake would spread. The proposal folds his practices into six existing pages (AI delegation management, Software factory, AI PR and code review, Agent skill methodology, Company brain, and the Knowledge architectures hub) plus one source page, with no new concept pages. The reason to hesitate is spread: one short post, six thin additions, and two bullets that openly disagree with advice already on other pages.

[[#Open questions|Open questions: 3 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Thorsten Ball is an engineer at Amp, Sourcegraph's coding agent. On 25 October 2026 he posted an X Article called "How I work with Agents", fifteen short practices dated "as of October 2026", which passed 900,000 views.

The theme running through the post is that people should supervise outcomes and evidence, not keystrokes. He tells readers to use the newest models (a model wrong 10% of the time never says which 10%) and to describe what they want, not how to build it. He argues that tool calls are what stopped hallucination, so everything an engineer can see (production logs, deploys, rollouts, feature flags, bug reports, customer email) should be visible and actionable to the agent too; his team has built custom plugins for exactly those jobs, and he finds local development a poor fit because agents running end-to-end tests collide over resources. He suggests testing whether agents really use the `AGENTS.md` files and skills a codebase collects by spawning blind agents as control and treatment groups. He wants agents to build their own iteration tools (twenty variations and a page to compare them; four theories on a slowdown, all checked), and calls "ask for irrefutable proof" (walkthroughs, demo videos, before/after numbers) his biggest change.

On rhythm, he says to let agents wait on you rather than the reverse, to batch bigger tasks, and to use scheduled wake-ups heavily. He has stopped managing context by hand, since compaction works; one thread is one task, whether it runs 3 or 3,714 messages. In Amp, threads are linked to git commits and shared, and he calls them "your company memory". He is not worried about slop any more, and reviews only high-blast-radius code: fewer than five central files and database migrations.

### What changes
The wiki already covers spec-first delegation, Composio's view that slop compounds, deterministic gates before review, and with/without skill testing, but nothing from Ball and no Amp page.

- **AI delegation management** gains three Current-guidance bullets (strongest model, what-not-how, don't hand-manage context, the first and third written as counterpoints linking to the pages they disagree with), an expanded proof bullet, and two patterns: agent-built iteration tools and async work with scheduled wake-ups. Page date moves to 25 October.
- **Software factory** gains a "Lifecycle legibility" subsection (SDLC visibility, SDLC plugins, remote machines over local dev) and Ball's dissent on the slop failure mode.
- **AI PR and code review** gains a review-by-blast-radius bullet with his four questions.
- **Agent skill methodology** gains a ninth maintenance step: blind control/treatment checks on whether agents use the codebase's knowledge.
- **Company brain** gains "company memory" in Also called and a short paragraph on Amp's commit-linked threads; the **Knowledge architectures** hub maps the term in its term map.
- Each page gets one Recent-changes entry dated 25 October; none is at the cap, so nothing spills. Index dates move for all six. One new source page.

### What to weigh
Two of Ball's claims contradict wiki guidance: compaction over Anthropic's "start a new session when context fills", and always-latest models over cost-aware routing. The proposal records both as counterpoints on the delegation page instead of editing Claude Code practices or the routing page; you may prefer them there. Mapping Amp's threads to Company brain rather than Agent memory is a judgment call (raw team-wide transcripts, nothing extracted). "Don't let agents write for humans" stays on the source page only.

## Intended changes

- [ ] **Update** `wiki/training/ai-delegation-management.md` — three Current-guidance bullets, expanded interim-evidence bullet, two new Proven-patterns bullets; adds one Recent-changes entry dated 2026-10-25 (6 entries, no spill); `as_of` 2026-10-19 → 2026-10-25; appends source id and Sources link
- [ ] **Update** `wiki/workflows/software-factory.md` — new `### Lifecycle legibility` subsection after "Repository as the factory"; one sentence added to the "slop compounds" failure mode; adds one Recent-changes entry dated 2026-10-25 (6 entries, no spill); `as_of` 2026-10-19 → 2026-10-25; appends source id, Sources link
- [ ] **Update** `wiki/workflows/ai-pr-code-review.md` — one Current-guidance bullet; adds one Recent-changes entry dated 2026-10-25 (5 entries, no spill); `as_of` 2026-10-14 → 2026-10-25; appends source id, Sources link
- [ ] **Update** `wiki/training/agent-skill-methodology.md` — new step 9 under "Maintaining the library"; adds one Recent-changes entry dated 2026-10-25 (9 entries, no spill); `as_of` 2026-09-03 → 2026-10-25; appends source id, Sources link
- [ ] **Update** `wiki/concepts/company-brain.md` — "company memory" alias, one paragraph after the production-example list, status heading date; adds one Recent-changes entry dated 2026-10-25 (6 entries, no spill); `as_of` 2026-10-02 → 2026-10-25; appends source id, Sources link
- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — one term-map row, Amp threads added to the Company brain row's examples; adds one Recent-changes entry dated 2026-10-25 (8 entries, no spill); `as_of` 2026-10-19 → 2026-10-25; appends source id, Sources link
- [ ] **Update** `wiki/index.md` — refresh descriptions/dates for the six pages above (page count unchanged)
- [ ] **Create** `wiki/sources/tweets/thorstenball-how-i-work-with-agents-2026-10-25.md` — source summary

## Page drafts

### wiki/training/ai-delegation-management.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-25
sources: [management-as-ai-superpower-2026-07, andy-matuschak-agent-loop-tempo-2026-07, design-layer-framework-2026-08-04, vibe-coded-security-risk-2026-08-10, securing-ai-employee-guide-2026-08-14, next-era-of-great-work-2026-08-16, engineering-team-cost-of-codex-2026-08-19, rieseberg-how-to-be-more-ambitious, thorstenball-how-i-work-with-agents-2026-10-25]
```

`## Current guidance` — append three bullets after the existing "Write the spec before execution starts" bullet:

```
- **Use the strongest current model for delegated work.** Thorsten Ball (Amp, Oct 2026): a model that is wrong 10% of the time does not tell you which 10%, so a cheaper, weaker model costs you repeated attempts. This is a counterpoint to [cost-aware task routing](cost-aware-ai-task-routing.md); both treat the human's review and retry time as the real cost, and disagree on how often a cheaper executor is competent.
- **Prompt the what, not the how.** Describe the result and the bar ("make the bytecode compiler and VM as fast as you can; do not stop until it's 2x faster") rather than your own plan for reaching it; Ball reports better results. Altitude, under "Raising the ambition of a delegation" below, goes one step further, to the outcome behind the task.
- **Don't manage context by hand.** One thread per task, and let compaction handle length; Ball's threads range from 3 to 3,714 messages. This disagrees with Anthropic's Claude Code guidance to start a fresh session when the context fills ([Claude Code practices](../workflows/claude-code-practices.md)); which advice holds likely depends on how well a given harness compacts.
```

`## Proven patterns` — replace the existing bullet `- Ask for interim evidence when the cost of a wrong direction is high.` with the first bullet below, and insert the other two directly after it (rest of section unchanged):

```
- Ask for interim evidence when the cost of a wrong direction is high, and for **irrefutable proof** at the end: an end-to-end walkthrough, a demo video, before/after numbers. Thorsten Ball (Amp, Oct 2026) calls this his biggest change, says agents are good at producing such proof, and suggests writing what does *not* count as evidence into the team's `AGENTS.md`. Judging proof is an instinct built up over time.
- **Let the agent build the tools to iterate, instead of iterating with it.** Rather than "try this... no, try that", ask for "20 variations and a little page that lets me combine and test them". The same works on the problem side: "give me four theories on why this is slow, then check all four." (Thorsten Ball, Oct 2026)
- **Let agents wait on you, not the reverse.** Hand over bigger, batched tasks instead of back-and-forth, and use scheduled wake-ups ("check the logs in 2 hours", "let me know once this is live", "check every day at 9am"), which Ball names as a feature he missed badly once it was switched off. This is the slow delegated loop from Current guidance made routine.
```

`## Recent changes` — insert one entry at the top (list goes from 5 to 6 entries; no spill):

```
- [2026-10-25] Added Thorsten Ball's (Amp) delegation habits: strongest current model, prompt the what not the how, no manual context management (counterpoints to cost-aware routing and Anthropic's fresh-session advice), irrefutable proof with a "this is not evidence" rule, agent-built iteration tools, and async work with scheduled wake-ups.
```

`## Sources` — append:

```
- [Thorsten Ball (@thorstenball) — How I work with Agents](../sources/tweets/thorstenball-how-i-work-with-agents-2026-10-25.md)
```

### wiki/workflows/software-factory.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-25
sources: [gas-city-software-factory-2026-05, aiewf-loops-debate-2026-07-03, software-factories-fde-2026-07, aiewf-2026-five-trends-latentspace, latent-space-pr-not-welcome-2026-09-01, ubereng-software-factory-2026-08-28, composio-anti-slop-software-factory-2026-10-12, rauchg-gdp-ts-2026-10, thorstenball-how-i-work-with-agents-2026-10-25]
```

New subsection under `## Current patterns`, inserted after `### Repository as the factory` and before `### Contribution model`:

```
### Lifecycle legibility

- **Make the whole lifecycle legible to the agent.** Thorsten Ball (Amp) argues that tool calls are what stopped hallucination, because they let agents touch reality, and that whatever an agent cannot see it makes up. So let it run what it builds end to end, read production logs, deploy, watch the rollout, cut the release, flip the feature flag, triage the bug report, and email the customer: anything an engineer can see, the agent should see too. Amp's team backs this with custom plugins for bug reports, emailing users, an "is our system healthy?" check, and granting feature flags. It hands agents the deploy and release actions that the control-layer prerequisite above, and fleet policies such as Shopify's deny-list for `push` and `deploy` ([AI enablement — software development](../training/ai-enablement-software-development.md)), keep gated.
- **Remote machines over local dev.** Each agent should be able to install and run whatever its task needs and test end to end; on one laptop parallel agents run into resource conflicts, on remote machines they do not. *Source: Thorsten Ball, Amp (2026-10-25)*
```

`## Failure modes` — replace the "Letting slop compound" bullet with:

```
- Letting slop compound: running agents at scale in a repo whose conventions live only in instructions rather than enforced checks, so every plan-implement-self-review round builds on the previous round's slop and approvals slow down over time. Not everyone treats this as a current risk: Thorsten Ball (Oct 2026) says he is no longer convinced current models add slop, or that the result is unmaintainable if they do.
```

`## Recent changes` — insert one entry at the top (5 → 6 entries; no spill):

```
- [2026-10-25] Added "Lifecycle legibility" (agents see and act on logs, deploys, rollouts, flags, bug reports, and customer email through SDLC plugins; remote machines over local dev) and Thorsten Ball's dissent on the slop failure mode.
```

`## Sources` — append:

```
- [Thorsten Ball (@thorstenball) — How I work with Agents](../sources/tweets/thorstenball-how-i-work-with-agents-2026-10-25.md)
```

### wiki/workflows/ai-pr-code-review.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-25
sources: [ai-code-review-eval-integrity-2026-06, agent-review-artifacts-2026-05-13, dashbench-code-review-understanding-2026-07, crabbox-remote-execution-2026-07, cognition-async-agents-testing-2026-05, lavaee-verification-pyramid-2026-10, agents-evals-deep-research, thorstenball-how-i-work-with-agents-2026-10-25]
```

`## Current guidance` — append one bullet at the end of the list:

```
- **Review by blast radius, not by line.** Thorsten Ball (Amp, Oct 2026) reads only the few central files in his codebase (fewer than five) and database migrations, and no longer cares about closure versus class, a neater type, variable names, or even duplication. For everything else he asks four questions before deciding whether to read the code at all: does it work, does he understand it at the arrows-in-a-diagram level, did the agent test it end to end, and could he change it in a month. This keeps the goal of understanding-preserving review below (a mental model good enough to steer the next loop) while dropping line-level reading outside the risky core.
```

`## Recent changes` — insert one entry at the top (4 → 5 entries; no spill):

```
- [2026-10-25] Added review-by-blast-radius guidance from Thorsten Ball (Amp): read only central files and migrations, and gate the rest on four questions (works, understood at diagram level, tested end to end, changeable in a month).
```

`## Sources` — append:

```
- [Thorsten Ball (@thorstenball) — How I work with Agents](../sources/tweets/thorstenball-how-i-work-with-agents-2026-10-25.md)
```

### wiki/training/agent-skill-methodology.md (updated)

Frontmatter (changed fields; `sources:` gains one id at the end):

```
as_of: 2026-10-25
sources: [perplexity-agent-skill-methodology-2026-05-12, agent-html-artifacts-2026-05-13, agent-skills-context-evals-2026-05-13, skill-engineering-impeccable-2026-07-02, vercel-agents-new-software-2026-07-03, autoresearch-agent-recipes-2026-07, powerpoint-agent-skill-failure-mode-2026-06, gpt-56-raising-concerns-2026-07-15, case-against-skills-2026-07-16, swe-skills-bench-2026-07, wayfinder-skill-2026-08-20, every-cloning-your-coworkers-2026-08-26, skills-and-plugin-packaging-late-march, harness-engineering-early-april, googlecloudtech-adk-2-orchestration-patterns, ainews-andrew-ng-ai-engineering-2026-08-25, ainews-openai-shuts-off-cursor-2026-08-29, ainews-muse-spark-13-2026-09-03, thorstenball-how-i-work-with-agents-2026-10-25]
```

`### Maintaining the library` — append after step 8:

```
**9. Check that agents actually use the codebase's knowledge**
Codebases pile up `AGENTS.md` files, skills, scripts, and docs without anyone checking that agents read them. Thorsten Ball (Amp, Oct 2026) spawns five blind agents on the same task, split into a control group without the knowledge and a treatment group with it, and compares the results; agents are good at running such experiments themselves. This is the Skill Lift comparison under "What the benchmarks say" applied to any agent-facing knowledge, not only skills. Composio's conclusion that agents ignore written instructions, so rules belong in lint ([Software factory](../workflows/software-factory.md)), is one result such a test can produce.
```

`## Recent changes` — insert one entry at the top (8 → 9 entries; no spill):

```
- [2026-10-25] Added step 9, a blind control/treatment check on whether agents actually use `AGENTS.md` files, skills, and docs (Thorsten Ball, Amp).
```

`## Sources` — append:

```
- [Thorsten Ball (@thorstenball) — How I work with Agents](../sources/tweets/thorstenball-how-i-work-with-agents-2026-10-25.md)
```

### wiki/concepts/company-brain.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-25
sources: [lovable-future-of-saas-2026-08-26, cloudflare-os-launch-2026-09-07, femke-plantinga-company-brains-2026-08-27, cerebras-knowledge-base, dhravyashah-supermemory-company-brain-2026-07-28, latent-space-airbnb-inside-out-ai-2026-10-02, thorstenball-how-i-work-with-agents-2026-10-25]
```

`## Also called` — replace the line with:

```
Org brain, GBrain (Garry Tan's implementation), "the agent's brain" (Every's phrasing for interconnected Notion databases), context graph (Airbnb's Everest), company memory (Amp's phrasing for shared agent threads), content brain and brand brain (function-scope instances limited to marketing).
```

`## Current status` — heading becomes `## Current status (as of 2026-10-25)`; append one paragraph after the Airbnb Everest bullet (end of the production-example list):

```
A lighter variant needs no separate store. In Amp, agent threads are shared across the team and linked to the git commits they produced, so "why did we do this?" is answered by finding the thread. Thorsten Ball (Oct 2026) calls threads "your company memory" and says the knowledge multiplies, and duplicate work drops, as more of the team works in Amp. It covers the signals and searching functions from raw transcripts, with no remembering or pruning step.
```

`## Recent changes` — insert one entry at the top (5 → 6 entries; no spill):

```
- [2026-10-25] Added Amp's commit-linked shared threads ("threads are your company memory", Thorsten Ball) as a store-free variant covering signals and searching only; "company memory" added to Also called.
```

`## Sources` — append:

```
- [Thorsten Ball (@thorstenball) — How I work with Agents](../sources/tweets/thorstenball-how-i-work-with-agents-2026-10-25.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter (changed fields; `sources:` gains one id at the end):

```
as_of: 2026-10-25
sources: [knowledge-layer-architecture, llm-wikis-paperwiki-2026-07-06, agent-memory-systems-layer-2026-06, femke-plantinga-company-brains-2026-08-27, ontologies-agentic-systems-2026-07-30, dhravyashah-supermemory-company-brain-2026-07-28, posthog-semantic-layer-2026-08-21, deeplethe-utopia-2026-09-09, helixdb-helix-foundry-2026-10-19, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06, latent-space-airbnb-inside-out-ai-2026-10-02, thorstenball-how-i-work-with-agents-2026-10-25]
```

`## Canonical pages` — in the Company brain row, the "Examples tracked" cell becomes:

```
GBrain, Slite Agent, Gorgias Cortex, Lovable capabilities, Cloudflare OS, Supermemory Company Brain, Airbnb Everest, Amp's shared threads
```

`## Term map` — insert one row directly after the "context graph, organizational context graph" row:

```
| company memory, "threads are your company memory" | Company brain | Amp's phrasing (Thorsten Ball) for agent threads shared across a team and linked to git commits. The raw transcripts are searched as they are, with nothing extracted or pruned, so it is an organization-scope company brain covering signals and searching, not agent memory, which extracts facts from sessions |
```

`## Recent changes` — insert one entry at the top (7 → 8 entries; no spill):

```
- [2026-10-25] Mapped "company memory" (Amp's shared, commit-linked agent threads) to Company brain, and added Amp's shared threads to that row's examples.
```

`## Sources` — append:

```
- [Thorsten Ball (@thorstenball) — How I work with Agents](../sources/tweets/thorstenball-how-i-work-with-agents-2026-10-25.md)
```

### wiki/index.md (updated)

Replace the six existing lines (page count unchanged):

```
- [workflows/software-factory](workflows/software-factory.md) — end-to-end agent pipelines across the software lifecycle: software-factory loop, dark/light factory split, control layer first, repository as the factory (Composio: co-location, lint rules over skills, fast CI before cloud agents), lifecycle legibility (agents see logs, deploys, flags; remote machines over local dev), PRs closed by default in AI-native OSS (Vercel AI SDK, Astro/Flue, tldraw), FDE examples (Sierra, Cursor, Warp Oz), make unsafe agent code fail to compile (gdp-ts) *(as_of: 2026-10-25)*
- [workflows/ai-pr-code-review](workflows/ai-pr-code-review.md) — workflow for AI-assisted pull request analysis, code-review execution, review by blast radius, judge calibration, historical PR replay, and understanding-preserving review artifacts *(as_of: 2026-10-25)*
- [concepts/company-brain](concepts/company-brain.md) — per-organization agent system for persistent context, tools, and institutional memory; Lovable, Cloudflare OS, Cerebras, Airbnb Everest, Amp's shared threads, and a 9-implementation survey converge on the same four-function architecture *(as_of: 2026-10-25)*
- [concepts/knowledge-architectures](concepts/knowledge-architectures.md) — hub for the knowledge / memory / company-brain / ontology cluster: three-axis matrix, one canonical page per cell, and a term map from every source coinage (second brain, LLM wiki, memory layer, context graph, company memory, memory repo, dreaming, knowledge base, world model) to its canonical page *(as_of: 2026-10-25)*
- [training/agent-skill-methodology](training/agent-skill-methodology.md) — evals-first method for writing maintainable agent skills with natural triggers, principles, production lessons, pruning, portable domain judgment, blind control/treatment usage checks, and benchmark evidence (SkillsBench, SWE-Skills-Bench, Skill Lift, retrieval actual-use effect) *(as_of: 2026-10-25)*
- [training/ai-delegation-management](training/ai-delegation-management.md) — practical guidance for delegating work to agents using management fundamentals: scope, authority, loop tempo, review cost, definition of done, spec-first delegation, irrefutable proof, agent-built iteration tools, and async work with scheduled wake-ups *(as_of: 2026-10-25)*
```

### wiki/sources/tweets/thorstenball-how-i-work-with-agents-2026-10-25.md (new)

```
---
title: 'Thorsten Ball (@thorstenball) — How I work with Agents'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-28-thorstenball-2114386050638336082.md
url: https://x.com/thorstenball/status/2114386050638336082
published: 2026-10-25
ingested: 2026-10-28
domains: [coding, agents]
---

# Thorsten Ball (@thorstenball) — How I work with Agents

An X Article by Thorsten Ball, an engineer at Amp (Sourcegraph's coding agent), posted 25 October 2026 and listing fifteen working practices "as of October 2026" (about 900K views). The common thread is to supervise outcomes and evidence rather than method: use the newest models, describe what you want rather than how, give agents sight of and tools for the whole software lifecycle, demand irrefutable proof, work asynchronously with scheduled wake-ups, leave context management to compaction, treat shared threads as company memory, and review only high-blast-radius code.

## Influenced pages

- [AI delegation management](../../training/ai-delegation-management.md) — strongest model, what-not-how, no manual context management, irrefutable proof, agent-built iteration tools, async work and wake-ups
- [Software factory](../../workflows/software-factory.md) — "Lifecycle legibility" subsection; dissent on the slop failure mode
- [AI PR and code review](../../workflows/ai-pr-code-review.md) — review by blast radius and four gating questions
- [Agent skill methodology](../../training/agent-skill-methodology.md) — blind control/treatment check on agent use of AGENTS.md, skills, and docs
- [Company brain](../../concepts/company-brain.md) — Amp's commit-linked shared threads as company memory
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — "company memory" mapped to Company brain

## Key claims extracted

- Use the latest models: a model wrong 10% of the time does not say which 10%, so weaker models cost repeated attempts ("Who's still using Opus 4.5?")
- Stop worrying about slop: not convinced current agents add it, or that the result is unmaintainable if they do
- Prompt the what, not the how (e.g. "make the bytecode compiler and VM as fast as you can; do not stop until it's 2x faster")
- Make the whole SDLC legible: tool calls stopped hallucinations; let agents run end to end, read production logs, deploy, watch rollouts, cut releases, flip flags, triage bugs, and email customers
- Amp's team has custom plugins for bug reports, emailing users, "is our system healthy?", and granting feature flags
- Eval agentic knowledge: spawn five blind agents, control vs. treatment, to see whether AGENTS.md files, skills, scripts, and docs are used
- Local dev feels poor: agents need to install and run anything; remote machines avoid local resource conflicts in end-to-end testing
- Let agents build iteration tools ("20 variations and a little page to combine and test them"; "four theories on why this is slow, then check all four")
- Ask for irrefutable proof (end-to-end walkthroughs, demo videos, before/after numbers); put "this is not evidence" in AGENTS.md; called the biggest game changer
- Don't wait for agents, let them wait on you: bigger, batched, asynchronous tasks
- Automations, schedules, wake-ups, and heartbeats are a killer feature ("check the logs in 2hrs", "check every day at 9am")
- Stop managing context manually: compaction works; one thread = one task; threads range from 3 to 3,714 messages
- Threads are company memory in Amp: shared, connected to git commits, reduce duplicate work
- Don't let agents write for humans, except debugging steps, incident reports, and some mechanical docs
- Review only high-blast-radius code: fewer than five central files and database migrations; gate the rest on "does it work, do I understand it at the arrows-in-a-diagram level, was it tested end to end, can I change it in a month"
```

## Schema / vocabulary additions

None.

## Open questions

- Amp has no tool page. Should one be created (subcategory would need checking), or is a practitioner post the wrong basis for it? Assumed: no page for now.
	- Ok, no page
- "Threads are your company memory" is mapped to Company brain because the threads are shared team-wide and nothing is extracted from them. Would you rather treat it as an agent-memory example, or keep it as a note on the source page only?
	- Example
- The Knowledge architectures hub is already above its length ceiling (1,336 body words, 111%), and this proposal adds one term-map row to it. Should the hub be split now (for example, moving the term map to its own page), or left as is? Assumed: no split.
	- Add and split
