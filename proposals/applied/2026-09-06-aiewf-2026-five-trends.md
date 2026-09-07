---
type: proposal
source: raw/newsletters/2026-07-14-5-trends-that-defined-ai-engineering-at-worlds-fa.md
status: pending
created: 2026-09-06
---

# Proposal: AI Engineer World's Fair 2026 — five trends

## Summary

### The source

swyx's post-conference synthesis of the 2026 AI Engineer World's Fair names five trends. Two are genuinely new material for this wiki; three land on pages that already cover the same ground, so the value here is corroboration and a few sharp named quotes rather than a new thesis. (1) The field's center of gravity has moved from the agent to the harness around it — swyx contrasts Lilian Weng's 2023 essay "LLM Powered Autonomous Agents" (planning/memory/tool-use, AutoGPT-era) with her 2026 "Harness Engineering for Self-Improvement," and cites Anthropic's Thariq Shihipar describing Claude Fable as "grown, not designed," with unpredictable "capability overhead." (2) "Loop engineering" is named as the new control layer, formalizing an inner-loop/outer-loop split with quotes from Introspection's Roland Gavrilescu, OpenClaw's Peter Steinberger ("the agent runs the inner execution loop; I set the direction... in the outer loop"), HumanLayer's Dex Horthy ("the hype is outrunning the discipline"), and Ralph Loop creator Geoffrey Huntley's "locomotive engineer" analogy. (3) Enterprise adoption is arriving via "forward deployed engineers" — named examples from Sierra (Natalie Meurer), Cursor (Pauline Brunet, on ROI-strict engagements), and Warp's new "Oz" software-factory platform (Zach Lloyd). (4) Coding agents have replaced IDEs as the daily interface, including Vercel's new "eve" agent framework. (5) Every agent platform is converging on "skills" as the packaging unit — Addy Osmani's definition, named tools (Impeccable, SkillCenter), and warnings about "skills hell."

### What changes

Two live pages get genuinely new content; the rest is reinforcement, added as named-source detail rather than a new pattern claim.

- **Harness** gets one new paragraph in "Why it matters": the Lilian Weng 2023-vs-2026 essay contrast and Anthropic's "grown, not designed" / "capability overhead" framing. This is a new angle on the page's existing thesis, not a repeat of it.
- **Agentic orchestration patterns** gets two additions to "Where these patterns surfaced" (not new pattern bullets — the underlying ideas are already covered): the loop-engineering quotes reinforce the page's existing "Oversight loop as the human layer" pattern with concrete named voices from AIEWF; the FDE quotes extend the page's existing "Software factory loop" pattern and its already-cited `software-factories-fde-2026-07` source with fresh named examples (Sierra, Cursor, Warp Oz). Page is at the 10-entry Recent-changes cap, so the oldest entry spills to history.
- **Trend 4** (coding agents replacing IDEs, Vercel's eve) isn't drafted — `agent-skill-methodology.md` already cites Vercel's eve in a different context, and this trend adds no new mechanism beyond restating that coding agents are now the default interface. Left as an Open Question.
- **Trend 5** (skills) is deliberately NOT drafted here even though it's a named AIEWF trend — the wiki's skill-methodology page is about to receive a separate, more substantive proposal from a SkillsBench research signal in the same digest, and folding thin AIEWF color (a definition, two named tools) into the same page in a second uncoordinated pass risks a messier merge than leaving it for that proposal or a follow-up to absorb.

### What to weigh

None of this is independently sourced beyond swyx's own recap — every quote here is secondhand (conference talks relayed by one writer), attributed as such in the drafts. The FDE and loop-engineering additions are corroboration of an existing thesis, not new claims, so the bar for accuracy is lower than a fresh capability claim would need. Trends 4 and 5 were deliberately left out rather than forced onto pages where they'd add little or risk duplicating a sibling proposal — say if you'd rather see them drafted anyway.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [x] **Update** `wiki/concepts/harness.md` — add the Lilian Weng 2023-vs-2026 essay contrast and Anthropic's "grown, not designed" framing to "Why it matters"; add one Recent-changes entry; add new source
    > See draft below

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add two "Where these patterns surfaced" bullets (loop-engineering named quotes; FDE named examples); add one Recent-changes entry (page is at the 10-entry cap — **spill required**); add new source
    > See draft below

- [x] **Spill** `wiki/workflows/agentic-orchestration-patterns.md` → `wiki/history/workflows/agentic-orchestration-patterns.md` — oldest entry `[2026-05-29]` falls off the cap
    > See draft below

- [x] **Create** `wiki/sources/newsletters/aiewf-2026-five-trends-latentspace.md` — source summary

## Page drafts

### wiki/concepts/harness.md (updated)

Frontmatter — bump `as_of` and add source:

```yaml
as_of: 2026-07-14
sources: [agentic-thinking-lin, langchain-better-harness, openai-agents-sdk-evolution, notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, claude-code-leak-architecture, harness-engineering-early-april, skills-and-plugin-packaging-late-march, harness-engineering-march, harness-debate-march, shopify-latent-space-april-2026, ainews-2026-04-22, thecode-april-22-2026, agent-infrastructure-harness-2026-05-01, mattpocock-dictionary-of-ai-coding, model-harness-fit-2026-05-13, shopify-claude-code-bessemer-2026-05, gas-city-software-factory-2026-05, cloudflare-glasswing-2026-05, loopcraft-june-2026, rl-harness-quality-june-2026, aiewf-loops-debate-2026-07-03, autoresearch-agent-recipes-2026-07, claude-tag-slack-agent-2026-06, gemini-managed-agents-2026-07, gray-swan-ai-security-2026-06, effective-feedback-compute-harness-2026-05, claude-managed-agents-updates-2026-05, code-as-agent-harness-paper, aiewf-2026-five-trends-latentspace]
```

Add to `## Why it matters` (new paragraph after the existing first paragraph):

```md
The shift is visible in how the field's own thinkers describe agents over time. Lilian Weng's influential 2023 essay, "LLM Powered Autonomous Agents," described an agent's anatomy as planning, memory, and tool use — proof-of-concept systems like AutoGPT and BabyAGI were the era's examples. Her 2026 essay, "Harness Engineering for Self-Improvement," argues the system *surrounding* the model — workflow management, context, permissions, evaluation, persistent state, continuous improvement — has become just as important as the model itself (AI Engineer World's Fair 2026, per Latent Space's recap). Anthropic's Thariq Shihipar made a related point about the model side of that boundary: Claude Fable is "grown, not designed," with a "capability overhead" — it gets smarter in a spiky, not fully predictable way — which is itself an argument for building the harness so it doesn't assume a single fixed model behavior.
```

`## Recent changes` (new entry at top):

```md
- [2026-07-14] Added the Lilian Weng 2023-vs-2026 essay contrast and Anthropic's "grown, not designed" framing, from AI Engineer World's Fair 2026 coverage.
```

`## Sources` (new entry appended):

```md
- [5 Trends That Defined AI Engineering at World's Fair 2026 — Latent Space](../sources/newsletters/aiewf-2026-five-trends-latentspace.md)
```

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Frontmatter — bump `as_of` and add source:

```yaml
as_of: 2026-07-14
sources: [notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, harness-engineering-early-april, open-agent-orchestration-late-march, skills-and-plugin-packaging-late-march, harness-engineering-march, deep-agents-overview, goose-platform, googlecloudtech-adk-2-orchestration-patterns, agent-infrastructure-harness-2026-05-01, ai-managed-orchestration-local-browser-agents-2026-04-28, production-agent-orchestration-2026-04-29, agent-html-artifacts-2026-05-13, gas-city-software-factory-2026-05, dynamic-workflows-claude-code, loopcraft-june-2026, aiewf-loops-debate-2026-07-03, shepherd-live-agent-rollback-2026-07-06, claude-code-getting-started-with-loops-2026-06-30, software-factories-fde-2026-07, ai-code-review-eval-integrity-2026-06, token-tightening-ai-finops-2026-06, what-the-hell-is-a-loop-anyway, dashbench-code-review-understanding-2026-07, andy-matuschak-agent-loop-tempo-2026-07, every-compound-engineering-upgrade-2026-05, every-claude-dynamic-workflows-reliability-2026-06, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, ainews-new-ai-infra-unicorns-2026-05-22, aiewf-2026-five-trends-latentspace]
```

Add to `## Where these patterns surfaced` (two new bullets, appended):

```md
- AI Engineer World's Fair 2026 named the inner-loop/outer-loop split explicitly: Introspection's Roland Gavrilescu frames "autoresearch" as an outer-loop system that studies and maintains a primary inner-loop system; OpenClaw's Peter Steinberger put it plainly — "the agent runs the inner execution loop; I set the direction and I make decisions in the outer loop." A stage debate on whether fully autonomous loops are ready surfaced real disagreement: HumanLayer's Dex Horthy argued "the hype is outrunning the discipline" (loops need to be deterministic, like Kubernetes' control loops, not "frontier thinking"), while Ralph Loop creator Geoffrey Huntley likened the AI engineer's job to a locomotive engineer's: "[We're] kind of like locomotive engineers now. That's our job: to keep the locomotive on the rails."
- AI Engineer World's Fair 2026 gave the software-factory/FDE pattern concrete named examples: Sierra's Natalie Meurer described forward-deployed-engineer work as managing "all the integrations and all the teams that contribute to the agent"; Cursor's Pauline Brunet framed FDE engagements around a "strict ROI" bar so customers don't turn the agents off after the engagement ends; Warp CEO Zach Lloyd described Oz, a new software-factory platform where organizations choose which lifecycle stages to automate and where humans stay in the loop for high-risk changes.
```

`## Recent changes` (full section — new entry inserted at top, oldest `[2026-05-29]` removed for the spill):

```md
## Recent changes

- [2026-07-14] Added named AI Engineer World's Fair 2026 detail to the loop-engineering and software-factory/FDE patterns: inner/outer loop framing (Introspection, OpenClaw), the autonomy-readiness stage debate (HumanLayer, Ralph Loop), and named FDE examples (Sierra, Cursor, Warp Oz).
- [2026-07-14] Expanded Agentic MapReduce from a passing mention into a full pattern entry: deterministic Plan/Shard/Map/Reduce (+Verify for Security Swarm) architecture, sourced from Cognition's engineering writeup, with three supporting whole-codebase-agent-limits research citations.
- [2026-07-08] Added loop-tempo selection from Andy Matuschak: fast controlled loops and slow delegated loops are easier to sustain than mid-speed partial-control loops.
- [2026-07-08] Linked PR review artifacts and repo-local review standards to the dedicated AI PR/code-review workflow.
- [2026-07-06] Shepherd proposal adds Git-like rollback/forking as a live-agent recovery primitive.
- [2026-07-04] Dhinakaran and Seldo map loop discourse into execution, task/Ralph, product/software-factory, system/autoresearch, and oversight loops; they emphasize exit signals and per-loop autonomy dials.
- [2026-06-29] Added Sidekick multi-model harness pattern: persistent frontier + cheaper sidekick agents, cache-aware mid-session model switching at compaction boundaries; contrasted with per-call advisor/smart-friend escalation.
- [2026-06-26] Added AI review standards and review-noise failure mode from code-review workflow coverage.
- [2026-06-24] Token-tightening coverage adds AI FinOps controls: budgets, model routing, prompt caching, cheaper defaults, checkpoints, and outcome-based spend review.
- [2026-06-18] Every case studies add scripted-subagent orchestration as a practical Dynamic Workflows reliability pattern.
```

`## Sources` (new entry appended):

```md
- [5 Trends That Defined AI Engineering at World's Fair 2026 — Latent Space](../sources/newsletters/aiewf-2026-five-trends-latentspace.md)
```

### wiki/history/workflows/agentic-orchestration-patterns.md (updated — spill append)

Append to the existing `## Archived from current page on 2026-08-25` section (that block already exists from an earlier spill; verify it's still the most recent block before appending, and append rather than create a new dated block since this proposal's `created` date is 2026-09-06 but the actual apply date governs which block this lands in — if applying after 2026-08-25, use a new `## Archived from current page on <apply date>` block instead):

```md
- [2026-05-29] Every updated compound engineering from a four-step loop to an eight-step loop that explicitly includes ideation and polish around the agentic work phase.
```

### wiki/sources/newsletters/aiewf-2026-five-trends-latentspace.md (new)

```md
---
title: "5 Trends That Defined AI Engineering at World's Fair 2026 — Latent Space"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-14-5-trends-that-defined-ai-engineering-at-worlds-fa.md
url: https://www.latent.space/p/aiewf26trends
published: 2026-07-14
ingested: 2026-09-06
domains: [agents, coding, training]
---

# 5 Trends That Defined AI Engineering at World's Fair 2026 — Latent Space

swyx's post-conference synthesis of AI Engineer World's Fair 2026, organized around five trends rather than individual product announcements: the shift from agent to harness (contrasting Lilian Weng's 2023 and 2026 essays), "loop engineering" as the new control layer (inner-loop/outer-loop framing, a stage debate on autonomy readiness), enterprise adoption via forward-deployed engineers and "software factories," coding agents replacing IDEs as the daily interface, and the convergence of every agent platform around "skills" as the packaging unit.

## Influenced pages

- [Harness (agent)](../../concepts/harness.md) — added the Weng essay contrast and Anthropic's "grown, not designed" framing
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — added named quotes reinforcing the existing loop-engineering and software-factory/FDE patterns

## Key claims extracted

- Lilian Weng's 2023 "LLM Powered Autonomous Agents" described agent anatomy as planning/memory/tool-use (AutoGPT, BabyAGI, GPT-Engineer as examples); her 2026 "Harness Engineering for Self-Improvement" argues the surrounding system (workflow, context, permissions, evaluation, persistent state, continuous improvement) is now equally important
- Anthropic's Thariq Shihipar: Claude Fable is "grown, not designed," with a "capability overhead" where it "gets smarter in a spiky way"
- "Loop engineering" named as the AIEWF buzzword of the event; Introspection's Roland Gavrilescu frames "autoresearch" as an outer loop studying/maintaining a primary inner loop; OpenClaw's Peter Steinberger: "the agent runs the inner execution loop; I set the direction and I make decisions in the outer loop"
- Stage debate: HumanLayer's Dex Horthy — "the hype is outrunning the discipline," loops need to be deterministic like Kubernetes control loops; Ralph Loop creator Geoffrey Huntley — AI engineers are like locomotive engineers keeping the locomotive on the rails
- Enterprise adoption via forward-deployed engineers (FDEs): Sierra's Natalie Meurer on managing integrations across an agentic ecosystem; Cursor's Pauline Brunet on strict-ROI engagements; Warp's Zach Lloyd on the "Oz" software-factory platform where orgs choose which lifecycle stages to automate
- Coding agents (Claude Code, Codex, Gemini CLI, Cursor, Warp) have replaced IDEs as the daily developer interface; Vercel released "eve," a new agent framework comparable to Next.js
- "Skills" convergence: Addy Osmani defines skills as encoding "the workflows, quality gates, and best practices that senior engineers use"; named tools include Impeccable (open-source design skills system, Paul Bakaus) and SkillCenter (a package manager/index for agent skills); Matt Pocock warns of "skills hell" comparable to "frameworks hell" and advises fewer, smaller, more structured skills; Y Combinator's Garry Tan urges AI-native companies to encode business functions (sales, support, finance) as maintained skills
