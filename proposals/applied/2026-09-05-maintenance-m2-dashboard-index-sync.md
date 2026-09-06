---
type: proposal
source: proposals/2026-09-05-maintenance-findings.md
status: pending
created: 2026-09-05
---

# Proposal: Maintenance M2 — dashboard and index sync

## Summary

### The source

This is the second proposal from the 2026-09-05 maintenance pass — the first (M1) fixed twenty places where pages flatly contradicted each other. This one is quieter: it's about dashboards that fell behind the pages they point to. A tool or model page gets updated, a Recent-changes entry gets added, and the dashboard line that summarizes it for a reader never gets touched. Nothing here is wrong so much as out of date — Cursor's dashboard line doesn't mention Grok 4.5 even though Cursor's own page has covered the launch since July; Codex's line on three different dashboards each freeze a different month of its evolution; the wiki's own index and its append-only log have the same problem at the meta level, tracking dates and counts that drifted the moment the pages under them moved on.

Re-checking against the live wiki (not the maintenance report's original quotes, several of which M1 already resolved) turned up fewer real gaps than the report estimated — several flagged lines turned out to already state the newest fact available on their target page, just with an older date attached to a claim that hasn't actually changed. Those are left alone; dating a still-true fact by when it was first sourced isn't a bug.

### What changes

- **State of Coding** picks up Grok 4.5 on the Cursor and Grok Build lines, Codex's July reframing as a general-purpose workspace agent, Kimi Code's new desktop companion, and Shopify's "agent-ready SaaS" repositioning.
- **State of Models** updates GLM-5.2 (its own coding environment, an APEX-SWE benchmark lead), Qwen 3.6 35B-A3B (a May community comparison), and Muse Spark (Muse Image's launch and Meta Glasses, both already on the model's own page but never reflected here).
- **State of Agents** updates five lines: Codex, Claude Managed Agents (self-hosted sandboxes, MCP tunnels), Microsoft Copilot (Cowork's GA and Autopilot), Advisor strategy (Harvey's external validation and the sidekick-pattern contrast), and Devin's line, broadened from Auto-Triage alone to include Security Swarm.
- **State of Finance** loses a duplicate: Perplexity Computer is listed twice with two different dates. One entry, in Personal finance AI where its subcategory actually sits.
- **State of Creative** picks up Claude Design's `/design-sync` bidirectional sync. **Genspark Slides**' own page gets the fix in the other direction — the dashboard already carries a caution about polished decks needing human review that the tool's own page never recorded.
- **Claude Mythos Preview** is the other reverse case: the dashboard has known since June that it was suspended under export controls; the model's own page doesn't say so yet.
- **The wiki index** gets 32 `as_of` dates brought back in line with what the pages actually say, two descriptions that were flatly wrong (GPT-5.6 Sol still called "restricted-preview," Grok Build still saying the joint model was "coming"), and a page-count block that undercounts the wiki by seven pages.
- **The activity log** gets reordered into one consistent chronology (it currently runs newest-first for its first stretch and oldest-first for the rest, with thirteen date inversions where the split happens) and fourteen entries that are missing their third field get one added.

### What to weigh

A few dashboard lines the original maintenance report flagged as stale turned out, on rereading the actual pages, to already state the newest available fact — GPT-5.5's science claims, Codex's cybersecurity line, and the computer-use dashboard's Gemini and Perplexity Computer lines among them. Those are left untouched rather than given a cosmetic date bump with nothing new to say. The log reorder is the largest mechanical change in this proposal — the draft shows the complete corrected file rather than a line-by-line diff, since a 350-entry reorder isn't reviewable any other way; the fourteen malformed-entry fixes are called out individually within it.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/coding.md` — refresh the Cursor, Codex, Grok Build, Kimi Code, and Shopify AI Toolkit lines to their linked pages' current content
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — refresh the GLM-5.2, Qwen 3.6 35B-A3B, and Muse Spark lines
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — refresh the Codex, Claude Managed Agents, Microsoft Copilot, Advisor strategy, and Devin lines
    > See draft below

- [ ] **Update** `wiki/state-of/finance.md` — consolidate the duplicate Perplexity Computer entry into one line under Personal finance AI
    > See draft below

- [ ] **Update** `wiki/state-of/science.md` — refresh the Claude Science line
    > See draft below

- [ ] **Update** `wiki/state-of/creative.md` — refresh the Claude Design line to include `/design-sync`
    > See draft below

- [ ] **Update** `wiki/tools/genspark-slides.md` — add the presentation-automation caveat and source that `state-of/creative.md` already cites but this page never recorded; bump `as_of`
    > See draft below

- [ ] **Update** `wiki/index.md` — bring 32 `as_of` dates in line with their pages' current frontmatter, fix two stale descriptions (GPT-5.6 Sol, Grok Build), and correct the page-count block (178 → 185; models 23 → 25; benchmarks 11 → 12)
    > See draft below

- [ ] **Update** `wiki/log.md` — reorder the entire file into one consistent oldest-first chronology (currently split: newest-first for the first ~140 lines, oldest-first after) and fix 14 entries missing their third `| summary` field
    > See draft below — full corrected file, since a reorder of this size isn't reviewable as a line diff

## Page drafts

### wiki/state-of/coding.md (updated)

`### Terminal / agentic coding` section — five lines updated:

> **Before (Cursor):**
> `- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK exposes the runtime headlessly; iOS beta adds mobile launch/control for always-on cloud and desktop agents; acquired by SpaceX ($60B, June 2026); Cursor Origin launched for agent-native code hosting *(as of 2026-06-30)*`
>
> **After:**
> `- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK exposes the runtime headlessly; iOS beta adds mobile launch/control for always-on cloud and desktop agents; acquired by SpaceX ($60B, June 2026); Cursor Origin launched for agent-native code hosting; Grok 4.5, the jointly trained SpaceXAI/Cursor model, launched July 2026 and is available across all Cursor surfaces *(as of 2026-07-08)*`

> **Before (Codex):**
> `- [Codex](../tools/codex.md) — OpenAI; cloud coding agent via CLI, ChatGPT, and now mobile (iOS/Android preview); remote SSH GA; direction increasingly spills into broader computer-work workflows *(as of 2026-05-15)*`
>
> **After:**
> `- [Codex](../tools/codex.md) — OpenAI; cloud coding agent via CLI, ChatGPT, and now mobile (iOS/Android preview); remote SSH GA; parallel subagents keep the main context clean on independent task parts; direction increasingly spills into broader computer-work workflows — Every now frames it as a general-purpose workspace agent beyond coding (inbox, CRM, writing) *(as of 2026-07-01)*`

> **Before (Grok Build):**
> `- [Grok Build](../tools/grok-build.md) — xAI; early beta CLI coding agent; plan mode (step-by-step diff review); parallel subagents in isolated git worktrees; SuperGrok Heavy subscribers only *(as of 2026-05-15)*`
>
> **After:**
> `- [Grok Build](../tools/grok-build.md) — xAI; early beta CLI coding agent; plan mode (step-by-step diff review); parallel subagents in isolated git worktrees; SuperGrok Heavy subscribers only; Grok 4.5 launched July 2026 as the default model — Coding Agent Index 76, on par with GPT-5.5 in Codex *(as of 2026-07-08)*`

> **Before (Kimi Code):**
> `- [Kimi Code](../tools/kimi-code.md) — Moonshot AI; open-source; 1-line CLI; video-as-coding-context; ACP support; IDE integration; powered by Kimi K2.7-Code model *(as of 2026-06-09)*`
>
> **After:**
> `- [Kimi Code](../tools/kimi-code.md) — Moonshot AI; open-source; 1-line CLI; video-as-coding-context; ACP support; IDE integration; powered by Kimi K2.7-Code model; companion Kimi Work desktop agent added Goal Mode for long-running tasks that continue until the objective is reached *(as of 2026-06-19)*`

> **Before (Shopify AI Toolkit):**
> `- [Shopify AI Toolkit](../tools/shopify-ai-toolkit.md) — Shopify packages platform docs, API schemas, and validation for Claude Code, Codex, Cursor, Gemini CLI, and VS Code via plugin, skills, or local Dev MCP; Codex support is skills/MCP only *(as of 2026-04-10)*`
>
> **After:**
> `- [Shopify AI Toolkit](../tools/shopify-ai-toolkit.md) — Shopify packages platform docs, API schemas, and validation for Claude Code, Codex, Cursor, Gemini CLI, and VS Code via plugin, skills, or local Dev MCP; Codex support is skills/MCP only; reframed as an example of "agent-ready SaaS" — product context and actions packaged for user-chosen external agents *(as of 2026-06-29)*`

### wiki/state-of/models.md (updated)

`### Open-weight models` / `### Coding models` — GLM-5.2 line:

> **Before:**
> `- [GLM-5.2](../models/glm-5-2.md) — Z.ai; MIT open-weight 744B/40B MoE with 1M context; strongest current open-weight coding/agent contender, now operationalized across hosted inference and agent harnesses, but still behind Fable/Opus on the hardest long-horizon knowledge-work tasks *(as of 2026-06-23)*`
>
> **After:**
> `- [GLM-5.2](../models/glm-5-2.md) — Z.ai; MIT open-weight 744B/40B MoE with 1M context; strongest current open-weight coding/agent contender, now operationalized across hosted inference and agent harnesses; ZCode launched as its official coding environment; APEX-SWE reports it leading the Integration category at 55.3% Pass@1; still behind Fable/Opus on the hardest long-horizon knowledge-work tasks *(as of 2026-07-02)*`

`### Coding models` — Qwen 3.6 35B-A3B line:

> **Before:**
> `- [Qwen 3.6 35B-A3B](../models/qwen-3-6-35b-a3b.md) — Alibaba; MoE variant; practical local-agent baseline on 24GB-class hardware; benchmark lead now held by 27B dense sibling *(as of 2026-04-22)*`
>
> **After:**
> `- [Qwen 3.6 35B-A3B](../models/qwen-3-6-35b-a3b.md) — Alibaba; MoE variant; practical local-agent baseline on 24GB-class hardware; benchmark lead now held by 27B dense sibling; May 2026 community benchmarks (r/LocalLLaMA) rank it strongest in the ~20GB local tier on paper-to-code and long-context tasks against Gemma 4 26B and Nvidia Nemotron 3 Nano *(as of 2026-05-13)*`

`### Frontier models` — Muse Spark line:

> **Before:**
> `- [Muse Spark](../models/muse-spark.md) — Meta's new multimodal model; the captured launch source emphasizes scaling efficiency and claims Llama 4 Maverick-level capability with over an order of magnitude less training compute *(as of 2026-04-10)*`
>
> **After:**
> `- [Muse Spark](../models/muse-spark.md) — Meta's multimodal model; the original launch source emphasized scaling efficiency and claimed Llama 4 Maverick-level capability with over an order of magnitude less training compute; Meta Glasses shipped with Muse Spark built in (June 2026), and Muse Image/Muse Video launched across Meta AI, Instagram Stories, and WhatsApp with an agentic planning/tool-use/self-refinement generation loop *(as of 2026-07-08)*`

### wiki/state-of/agents.md (updated)

> **Before (Codex):**
> `- [Codex](../tools/codex.md) (Workspace Agents) — OpenAI; shareable team agents in Slack and ChatGPT for scheduling, research, drafting, coding, and data analysis; now positioned as a broader computer-work agent (docs, sheets, slides, browser flows, connected apps) beyond software engineering *(as of 2026-05-01)*`
>
> **After:**
> `- [Codex](../tools/codex.md) (Workspace Agents) — OpenAI; shareable team agents in Slack and ChatGPT for scheduling, research, drafting, coding, and data analysis; now positioned as a broader computer-work agent (docs, sheets, slides, browser flows, connected apps) beyond software engineering; Every's July coverage frames it as a general-purpose workspace agent spanning inbox, CRM, healthcare coordination, writing, and personal-knowledge workflows *(as of 2026-07-01)*`

> **Before (Claude Managed Agents):**
> `- [Claude Managed Agents](../tools/claude-managed-agents.md) — Anthropic's hosted runtime; separates session, harness, sandbox, and now file-backed built-in memory with shared stores and auditability *(as of 2026-04-24)*`
>
> **After:**
> `- [Claude Managed Agents](../tools/claude-managed-agents.md) — Anthropic's hosted runtime; separates session, harness, sandbox, and file-backed built-in memory with shared stores and auditability; added self-hosted sandboxes (public beta, including Cloudflare/Daytona/Modal/Vercel) and MCP tunnels (research preview) *(as of 2026-05-20)*`

> **Before (Microsoft Copilot):**
> `- [Microsoft Copilot](../tools/microsoft-copilot.md) — Microsoft; agentic default mode inside Word, Excel, and PowerPoint; takes multi-step native actions in documents, worksheets, and presentations while users stay in control *(as of 2026-04-22)*`
>
> **After:**
> `- [Microsoft Copilot](../tools/microsoft-copilot.md) — Microsoft; agentic default mode inside Word, Excel, and PowerPoint; takes multi-step native actions in documents, worksheets, and presentations while users stay in control; Copilot Cowork reached general availability in June 2026 (Microsoft claims 30-40% cheaper per prompt than Claude Cowork), and Microsoft Autopilot launched as a hosted long-running agent runtime with OpenClaw and Hermes Agent as early examples *(as of 2026-06-17)*`

> **Before (Advisor strategy):**
> `- [Advisor strategy](../workflows/advisor-strategy.md) — small executor (Sonnet/Haiku) drives the loop; escalates to Opus only when stuck; +2.7% SWE-bench Multilingual, −11.9% cost vs Sonnet alone *(as of 2026-04-09)*`
>
> **After:**
> `- [Advisor strategy](../workflows/advisor-strategy.md) — small executor (Sonnet/Haiku) drives the loop; escalates to Opus only when stuck; +2.7% SWE-bench Multilingual, −11.9% cost vs Sonnet alone; externally validated by Harvey on legal tasks (18% vs 14% all-pass, $368 vs $954 per 100 tasks); Cognition's sidekick pattern is offered as a contrasting approach that avoids the advisor tool's per-call cache-miss cost *(as of 2026-06-29)*`

> **Before (Devin Auto-Triage):**
> `- [Devin Auto-Triage](../tools/devin.md) — Cognition; always-on persistent agent that monitors Slack channels and investigates bugs as reported; parent Devin filters noise and dispatches focused sub-sessions; shared long-term memory for deduplication across repeat reports; early users (Modal) describe it as more useful than homegrown triage automations *(as of 2026-05-19)*`
>
> **After:**
> `- [Devin](../tools/devin.md) — Cognition; Auto-Triage is an always-on persistent agent that monitors Slack channels and investigates bugs as reported, with parent Devin dispatching focused sub-sessions and shared long-term memory for deduplication; early users (Modal) describe it as more useful than homegrown triage automations; Security Swarm extends the same fan-out pattern (Agentic MapReduce) to vulnerability discovery, exploitability validation, and fix-PR generation *(as of 2026-07-14)*`

### wiki/state-of/finance.md (updated)

`### Finance AI` — remove the Perplexity Computer line (moves to Personal finance AI below):

> **Before:**
> ```
> - [Hebbia](../tools/hebbia.md) — document-heavy knowledge-work platform with especially strong practical relevance in finance analysis and modeling workflows *(as of 2026-04-22)*
> - **Anthropic finance agent templates** — secondary newsletter coverage describes templates for pitch generation, valuation review, KYC, and month-end close with market-data integrations; pending primary Anthropic verification *(as of 2026-05-06)*
> - [Perplexity Computer](../tools/perplexity-computer.md) — professional-finance positioning now reportedly combines licensed finance data with packaged workflows; current signal is newsletter coverage pending primary verification *(as of 2026-05-06)*
> - **Bridgewater / Thinking Machines expert-judgment model** — expert-labeled financial information-filtering tasks fine-tuned on Qwen3-235B; trained model reached 84.7% average accuracy and 13.8x lower inference cost per task than frontier baselines in the public Thinking Machines report *(as of 2026-07-02)*
> ```
>
> **After:**
> ```
> - [Hebbia](../tools/hebbia.md) — document-heavy knowledge-work platform with especially strong practical relevance in finance analysis and modeling workflows *(as of 2026-04-22)*
> - **Anthropic finance agent templates** — secondary newsletter coverage describes templates for pitch generation, valuation review, KYC, and month-end close with market-data integrations; pending primary Anthropic verification *(as of 2026-05-06)*
> - **Bridgewater / Thinking Machines expert-judgment model** — expert-labeled financial information-filtering tasks fine-tuned on Qwen3-235B; trained model reached 84.7% average accuracy and 13.8x lower inference cost per task than frontier baselines in the public Thinking Machines report *(as of 2026-07-02)*
> ```

`### Personal finance AI` — merge both Perplexity Computer facts into one entry:

> **Before:**
> `- [Perplexity Computer](../tools/perplexity-computer.md) — Perplexity Computer connects to 12,000+ financial institutions via Plaid, letting users build custom budgeting/tracking tools inside an AI chat interface *(as of 2026-04-10)*`
>
> **After:**
> `- [Perplexity Computer](../tools/perplexity-computer.md) — connects to 12,000+ financial institutions via Plaid, letting users build custom budgeting/tracking tools inside an AI chat interface; also reportedly moving toward a professional-finance positioning combining licensed finance data with packaged workflows (newsletter coverage, pending primary verification) *(as of 2026-05-06)*`

### wiki/state-of/science.md (updated)

> **Before (Claude Science):**
> `- [Claude Science](../tools/claude-science.md) — Anthropic beta science workbench for analysis, database search, reproducible artifacts, reviewer agents, scientific visualizations, 60+ databases, BioNeMo/Boltz/OpenFold-style integrations, and local/HPC compute; case studies now include Manifold Bio, Allen Institute, and UCSF workflows *(as of 2026-07-01)*`
>
> **After:**
> `- [Claude Science](../tools/claude-science.md) — Anthropic beta science workbench for analysis, database search, reproducible artifacts, persistent kernels, reviewer agents, scientific visualizations, 60+ databases, BioNeMo/Boltz/OpenFold-style integrations, and local/HPC compute; case studies now include Manifold Bio, Allen Institute, and UCSF workflows *(as of 2026-07-06)*`

The GPT-5.5 line on this page is left unchanged — its science-specific claims (BixBench, GeneBench) haven't been superseded by anything newer on `models/gpt-5-5.md`, even though that page's overall `as_of` moved for an unrelated coding-benchmark fix in M1.

### wiki/state-of/creative.md (updated)

> **Before (Claude Design):**
> `- [Claude Design](../tools/claude-design.md) — Anthropic; research preview for collaborative prototype, slide, one-pager, and marketing-asset creation; powered by Opus 4.7; brand onboarding from codebase + design files; Pro/Max/Team/Enterprise; connectors for Adobe, Blender, Fusion, Ableton, Splice, SketchUp, Affinity, Resolume now reported *(as of 2026-04-29, secondary coverage)*`
>
> **After:**
> `- [Claude Design](../tools/claude-design.md) — Anthropic; research preview for collaborative prototype, slide, one-pager, and marketing-asset creation; powered by Opus 4.7; brand onboarding from codebase + design files; Pro/Max/Team/Enterprise; connectors for Adobe, Blender, Fusion, Ableton, Splice, SketchUp, Affinity, Resolume now reported; syncs bidirectionally with Claude Code via \`/design-sync\` *(as of 2026-07-08)*`

### wiki/tools/genspark-slides.md (updated)

Frontmatter — bump `as_of`, add the source id:

```yaml
as_of: 2026-06-29
sources: [genspark-slides, legacy-ai-tools-roadmap-xlsx, powerpoint-agent-skill-failure-mode-2026-06]
```

`## Current status` — add one bullet (the dashboard has carried this caution since it was written; the tool's own page never recorded it):

> **Before:**
> ```
> ## Current status (as of 2026-04-22)
>
> - Presentation-generation is a first-class product use case
> - Useful as a slides-specific knowledge-work surface, not only a creative toy
> ```
>
> **After:**
> ```
> ## Current status (as of 2026-06-29)
>
> - Presentation-generation is a first-class product use case
> - Useful as a slides-specific knowledge-work surface, not only a creative toy
> - Industry coverage of AI presentation-generation broadly (Every, June 2026) cautions that polished enterprise decks still need narrative cohesion, brand/style precision, and near-zero defect rates that thin prompting doesn't reliably deliver — supporting files, scripts, and human review remain part of the loop
> ```

Add a `## Recent changes` section (page has none today):

```md
## Recent changes

- [2026-06-29] Added industry caution (Every, via the PowerPoint-agent-skill-failure-mode piece) that polished enterprise decks require more than thin prompting.
```

`## Sources` — add the new link:

> **Before:**
> ```
> ## Sources
>
> - [Genspark Slides product page](../sources/articles/genspark-slides.md)
> - [AI Tools & Roadmap legacy workbook](../sources/notes/legacy-ai-tools-roadmap-xlsx.md)
> ```
>
> **After:**
> ```
> ## Sources
>
> - [Genspark Slides product page](../sources/articles/genspark-slides.md)
> - [AI Tools & Roadmap legacy workbook](../sources/notes/legacy-ai-tools-roadmap-xlsx.md)
> - [PowerPoint remains hard for agents](../sources/newsletters/powerpoint-agent-skill-failure-mode-2026-06.md)
> ```

### wiki/index.md (updated)

Header `as_of` — bump to reflect this regeneration:

> **Before:** `as_of: 2026-07-08`
> **After:** `as_of: 2026-09-05`

32 entries get only their `(as_of: …)` date corrected to match the linked page's current frontmatter `as_of` — no wording changes except the two marked with an asterisk, which also get a corrected description:

| Page | Before | After |
|---|---|---|
| state-of/coding | 2026-07-02 | 2026-07-14 |
| state-of/models | 2026-07-02 | 2026-07-08 |
| state-of/legal | 2026-05-01 | 2026-06-04 |
| state-of/healthcare | 2026-06-16 | 2026-06-18 |
| state-of/cybersecurity | 2026-07-02 | 2026-07-14 |
| state-of/voice | 2026-06-16 | 2026-07-07 |
| models/claude-mythos-preview | 2026-05-19 | 2026-05-23 |
| models/claude-opus-4-8 | 2026-06-04 | 2026-07-02 |
| models/deepseek-v4 | 2026-04-25 | 2026-05-23 |
| models/gpt-5-5 | 2026-05-18 | 2026-07-02 |
| *models/gpt-5-6-sol | 2026-06-26 | 2026-07-09 |
| models/qwen-3-7 | 2026-05-19 | 2026-05-23 |
| tools/claude-code | 2026-07-01 | 2026-07-08 |
| tools/claude-design | 2026-05-05 | 2026-07-08 |
| tools/claude-managed-agents | 2026-05-13 | 2026-05-20 |
| tools/cursor | 2026-06-30 | 2026-07-08 |
| tools/devin | 2026-07-02 | 2026-07-14 |
| tools/gpt-realtime-2 | 2026-05-08 | 2026-07-07 |
| *tools/grok-build | 2026-06-17 | 2026-07-08 |
| benchmarks/frontiercode | 2026-06-09 | 2026-07-09 |
| benchmarks/swe-bench | 2026-04-23 | 2026-07-09 |
| benchmarks/terminal-bench | 2026-04-23 | 2026-07-09 |
| workflows/advisor-strategy | 2026-04-09 | 2026-06-29 |
| workflows/agentic-orchestration-patterns | 2026-07-08 | 2026-07-14 |
| concepts/agent-labs-vs-model-labs | 2026-06-11 | 2026-07-02 |
| concepts/agent-evals | 2026-07-08 | 2026-07-14 |
| trends/compute-infrastructure | 2026-07-02 | 2026-07-08 |
| trends/open-weight-momentum-broadens | 2026-06-30 | 2026-07-02 |
| trends/restricted-frontier-deployment | 2026-06-30 | 2026-07-09 |
| trends/voice-becomes-agent-interface | 2026-03-30 | 2026-07-07 |
| training/ai-enablement-software-development | 2026-07-08 | 2026-07-14 |
| training/ai-work-delegation-modes | 2026-05-13 | 2026-05-21 |

\* also gets a description fix:

> **Before:**
> `- [models/gpt-5-6-sol](models/gpt-5-6-sol.md) — OpenAI restricted-preview flagship; METR predeployment eval found high detected cheating and uncertain time-horizon estimates *(as_of: 2026-06-26)*`
>
> **After:**
> `- [models/gpt-5-6-sol](models/gpt-5-6-sol.md) — OpenAI flagship (Sol/Terra/Luna family); launched as a restricted preview, cleared for public rollout July 2026; METR predeployment eval found high detected cheating and uncertain time-horizon estimates *(as_of: 2026-07-09)*`

> **Before:**
> `- [tools/grok-build](tools/grok-build.md) — xAI early beta CLI coding agent with plan mode and parallel worktree subagents; SuperGrok Heavy only; jointly trained model with Cursor/SpaceX coming *(as_of: 2026-06-17)*`
>
> **After:**
> `- [tools/grok-build](tools/grok-build.md) — xAI early beta CLI coding agent with plan mode and parallel worktree subagents; SuperGrok Heavy only; Grok 4.5, the jointly trained Cursor/SpaceX model, launched July 2026 as the default *(as_of: 2026-07-08)*`

`## Page count` section:

> **Before:**
> ```
> - state-of: 11
> - models: 23
> - tools: 84
> - benchmarks: 11
> - workflows: 6
> - concepts: 19
> - trends: 12
> - training: 13
> - use-cases: 3
>
> **Total content pages: 178.** The wiki is still in the early stage, but no longer below the initial bootstrap threshold.
> ```
>
> **After:**
> ```
> - state-of: 11
> - models: 25
> - tools: 84
> - benchmarks: 12
> - workflows: 6
> - concepts: 19
> - trends: 12
> - training: 13
> - use-cases: 3
>
> **Total content pages: 185.**
> ```

### wiki/log.md (updated — full file, reordered)

The file currently runs newest-first for roughly its first 140 lines, then switches to oldest-first for the rest (the switch point is marked by a stray "To see the most recent activity" usage tip that was evidently appended once, at the moment the convention changed, and never relocated). This draft re-sorts the entire file into one consistent oldest-first order — matching the append-only framing in the file's own header and how every entry from this session onward has actually been added — and relocates that usage tip to sit permanently right after the header, where it now correctly describes the whole file (`tail -20` on an oldest-first file already gives the most recent entries, so the command itself needs no change).

Fourteen entries were missing their third `| summary` field (13 `schema` entries, 1 `apply` entry) — each gets a minimal field added without changing what it already said:

- `[2026-06-17] **apply** | AI review skills deleted by user — omitted` → `[2026-06-17] **apply** | AI review skills | deleted by user before this apply step ran — omitted`
- `[2026-05-13] **schema** | added subcategory \`ai-music-generation\`` → `[2026-05-13] **schema** | vocabulary addition | added subcategory \`ai-music-generation\``
- The same `vocabulary addition |` fix applies to the twelve other bare `**schema** | added …` lines (2026-04-09 ×5, 2026-04-10 ×4, 2026-04-15 ×1, 2026-04-22 ×2) — each keeps its original description verbatim as the summary field.

No entry's date, op, subject, or summary content is otherwise changed — this is a reorder plus the fourteen field additions above, nothing else. The file's own header includes a fenced `grep`/`tail` example, so the full draft below is wrapped in a longer fence per convention. Full corrected file:

````md
# Wiki Log

Chronological append-only record of wiki activity. Entries start with:

```
- [YYYY-MM-DD] **<op>** | <subject> | <summary>
```

Valid ops: `ingest`, `triage`, `reject`, `apply`, `lint`, `query-verify`, `schema`.

To see the most recent activity:

```bash
grep "^- \[" wiki/log.md | tail -20
```
- [2026-04-09] **schema** | wiki bootstrap | initial scaffold created (CLAUDE.md, config.yml, _schema/, state-of placeholders, scripts/, manual/)
- [2026-04-09] **schema** | vocabulary addition | added subcategory `spec-driven-development`; added tags `github`, `open-source`, `cli`, `beta`, `spec-driven`
- [2026-04-09] **ingest** | Fowler — Understanding SDD (Kiro, spec-kit, Tessl) | 1 page updated, 5 created (state-of/coding updated; concepts/spec-driven-development, tools/kiro, tools/spec-kit, tools/tessl, sources/articles/sdd-3-tools-fowler created)
- [2026-04-09] **schema** | vocabulary addition | added subcategories `agentic-coding-workspace`, `agent-orchestration-ui`, `coding-model`; added tags `closed-source`, `agentic`
- [2026-04-09] **ingest** | Cursor 3 launch — "Meet the new Cursor" | 2 pages updated, 3 created (state-of/coding, state-of/agents updated; tools/cursor, models/composer-2, sources/articles/cursor-3-launch created)
- [2026-04-09] **schema** | vocabulary addition | added domain `legal`; added subcategory `legal-ai`
- [2026-04-09] **ingest** | Harvey — "Legal is Next" (Pereyra) | 0 pages updated, 4 created (state-of/legal, tools/harvey, trends/agents-reshape-organizations, sources/articles/harvey-legal-is-next created); manual updated (proposals-workflow.html); DEFERRED.md appended (readability extraction bug)
- [2026-04-09] **apply** | fetch_url.py readability fallback | DEFERRED.md item resolved: length-based fallback to body.innerText wired through fetch_with_playwright → html_to_markdown → main; also fixed latent arg-count bug in the call site
- [2026-04-09] **schema** | vocabulary addition | added subcategory `model-orchestration`; added tag `anthropic`
- [2026-04-09] **ingest** | Anthropic — "The advisor strategy" | 2 pages updated, 2 created (state-of/agents, wiki/index updated; workflows/advisor-strategy, sources/articles/advisor-strategy created)
- [2026-04-09] **schema** | vocabulary addition | added subcategory `agentic-devops`
- [2026-04-09] **ingest** | Stripe CLI `projects` developer preview | 3 pages updated, 2 created (state-of/coding, state-of/agents, wiki/index updated; tools/stripe-cli, sources/articles/stripe-cli created)
- [2026-04-10] **ingest** | LangChain — "The Agent Improvement Loop Starts with a Trace" | 1 page updated, 2 created (wiki/index updated; concepts/agent-improvement-loop, sources/articles/trace-agent-improvement-loop created)
- [2026-04-10] **schema** | vocabulary addition | added subcategory `agent-orchestration`
- [2026-04-10] **ingest** | Anthropic — "Scaling Managed Agents: Decoupling the brain from the hands" | 2 pages updated, 2 created (state-of/agents, wiki/index updated; tools/claude-managed-agents, sources/articles/managed-agents created)
- [2026-04-10] **apply** | source-date normalization | LLM-INSTRUCTIONS updated to prefer source publication date over ingest date for `as_of`; Harvey-derived pages backdated from 2026-04-09 to 2026-04-02 and source summary now records `published`
- [2026-04-10] **apply** | source-date normalization (user-supplied dates) | Cursor-derived pages backdated to 2026-04-02; Fowler SDD-derived pages backdated to 2025-10-15; Managed Agents-derived pages backdated to 2026-04-09; source summaries now record `published`
- [2026-04-10] **ingest** | Anthropic — "Emotion concepts and their function in a large language model" | 1 page updated, 2 created (wiki/index updated; concepts/functional-emotions, sources/articles/emotion-concepts-function created)
- [2026-04-10] **triage** | Superhuman AI 2026-04-10 | 3 proposals (Perplexity Computer, Gemini visualizations, AI in science), 6 skipped
- [2026-04-10] **schema** | vocabulary addition | added domains `computer-use`, `finance`, `science`; added subcategories `computer-use`, `ai-assistant`; added tags `perplexity`, `google`
- [2026-04-10] **apply** | Perplexity Computer — Plaid integrations | 2 pages updated (state-of/computer-use created, wiki/index), 3 created (tools/perplexity-computer, state-of/finance, sources/articles/perplexity-computer-plaid); enriched via web research
- [2026-04-10] **apply** | Gemini visualizations & notebooks | 2 pages updated (state-of/models, wiki/index), 1 created (tools/gemini)
- [2026-04-10] **apply** | AI in Science trend | 1 page updated (wiki/index), 2 created (trends/ai-in-science, state-of/science)
- [2026-04-10] **triage** | The Code Newsletter 2026-04-10 | 5 proposals generated, 8 skipped
- [2026-04-10] **apply** | Claude Code Monitor tool | 2 pages updated (state-of/coding, wiki/index), 2 created (tools/claude-code, sources/articles/claude-code-monitor); new subcategory terminal-coding-agent
- [2026-04-10] **apply** | Cursor PR demos | 1 page updated (tools/cursor), 1 created (sources/articles/cursor-pr-demos)
- [2026-04-10] **apply** | OpenAI $100/mo Pro plan | 2 pages updated (state-of/coding, wiki/index), 2 created (tools/codex, sources/articles/openai-pro-100)
- [2026-04-10] **apply** | Agentic thinking (Junyang Lin) | 2 pages updated (state-of/agents, trends/agents-reshape-organizations), 2 created (concepts/agentic-thinking, sources/articles/agentic-thinking-lin)
- [2026-04-10] **apply** | LangChain Better-Harness | 1 page updated (concepts/agent-improvement-loop), 1 created (sources/articles/langchain-better-harness)
- [2026-04-10] **schema** | vocabulary addition | added subcategory terminal-coding-agent, tag openai
- [2026-04-10] **apply** | Harness concept | 1 page updated (wiki/index), 1 created (concepts/harness)
- [2026-04-10] **ingest** | Every / Playtesting — "The Market for Making AI Better" | 1 page updated, 2 created (wiki/index updated; trends/proprietary-data-becomes-model-moat, sources/articles/market-for-making-ai-better created)
- [2026-04-10] **apply** | tool-page concision guidance | LLM-INSTRUCTIONS updated so routine tool/model/workflow ingests default to shorter pages and fewer repeated sections
- [2026-04-10] **schema** | vocabulary addition | added subcategory `agent-toolkits`
- [2026-04-10] **ingest** | Shopify AI Toolkit | 2 pages updated, 2 created (state-of/coding, wiki/index updated; tools/shopify-ai-toolkit, sources/articles/shopify-ai-toolkit created)
- [2026-04-10] **schema** | added page type `training` | new `wiki/training/` and `wiki/history/training/` directories; LLM-INSTRUCTIONS, config.yml, source-type guidance, and wiki/index updated to support training pages for organizational AI enablement
- [2026-04-10] **ingest** | Ramp AI adoption playbook | 2 pages updated, 2 created (wiki/trends/agents-reshape-organizations, wiki/index updated; wiki/training/company-wide-ai-enablement, wiki/sources/articles/ramp-ai-adoption-playbook created); personal/takes/test-backlog appended with customer PR backlog item
- [2026-04-10] **triage** | The Code Newsletter — Managed Agents / Muse Spark | 3 proposals generated (Muse Spark, Cursor Bugbot learned rules, Postman AI-org-chart signal), 4 skipped
- [2026-04-15] **apply** | Cursor Bugbot learned rules | 3 pages updated (tools/cursor, concepts/agent-improvement-loop, state-of/coding), 1 created (sources/articles/cursor-bugbot-learning); index updated
- [2026-04-15] **schema** | vocabulary addition | added subcategory `frontier-multimodal-model`
- [2026-04-15] **ingest** | Muse Spark | 2 pages updated, 2 created (state-of/models, wiki/index updated; models/muse-spark, sources/articles/muse-spark created)
- [2026-04-15] **ingest** | Postman AI-era org-chart signal | 1 page updated, 1 created (trends/agents-reshape-organizations updated; sources/tweets/postman-ai-org-chart created)
- [2026-04-15] **ingest** | Curiosity-Driven Imagination paper | 3 pages updated, 2 created
- [2026-04-16] **triage** | The Code 2026-04-16 | 1 proposals, 5 skipped
- [2026-04-16] **ingest** | OpenAI — "The next evolution of the Agents SDK" | 3 pages updated, 2 created
- [2026-04-21] **triage** | AI digest 2026-04-20 to 2026-04-21 | 8 proposals generated, 2 skipped (Google DeepMind strike team, Qwen3.6-Max-Preview)
- [2026-04-21] **ingest** | McKinsey — "AI is Everywhere. The Agentic Organization Isn't Yet." | 2 pages updated, 1 created
- [2026-04-21] **ingest** | LeWorldModel (LeWM) — Stable End-to-End JEPA from Pixels | 1 page updated, 2 created
- [2026-04-21] **apply** | Kimi K2.6 | 2 pages updated (state-of/models, wiki/index), 3 created (models/kimi-k2-6, sources/articles/kimi-k2-6-blog, sources/newsletters/ainews-2026-04-21); added tags `moonshot-ai`, `open-weights`; clarified state-of leader replacement rules in LLM-INSTRUCTIONS
- [2026-04-21] **apply** | Codex Chronicle | 2 pages updated (tools/codex, trends/proprietary-data-becomes-model-moat); reused existing source summary `sources/newsletters/ainews-2026-04-21`
- [2026-04-21] **apply** | Hermes Agent | 2 pages updated (state-of/agents, wiki/index), 1 created (tools/hermes-agent); reused existing source summary `sources/newsletters/ainews-2026-04-21`
- [2026-04-21] **apply** | Claude Opus 4.7 | 2 pages updated (state-of/models, wiki/index), 1 created (models/claude-opus-4-7); reused existing source summary `sources/newsletters/ainews-2026-04-21`
- [2026-04-21] **apply** | Claude Cowork | 2 pages updated (state-of/agents, wiki/index), 3 created (tools/claude-cowork, sources/articles/claude-cowork-launch, sources/tweets/aakash-gupta-cowork); applied without adding a new subcategory per proposal comments
- [2026-04-21] **triage** | Personal digest 2026-04-15 to 2026-04-21 | 9 proposals generated, 1 skipped
- [2026-04-21] **apply** | Anthropic/AWS compute infrastructure | 2 pages updated (state-of/models, wiki/index), 1 created (trends/compute-infrastructure); reused existing source summary `sources/newsletters/ainews-2026-04-21`
- [2026-04-21] **ingest** | Every Mini-Vibe Check on Claude Managed Agents | 3 pages updated, 1 created
- [2026-04-21] **ingest** | Qwen 3.6 35B-A3B crosses into practical local-agent territory | 2 pages updated, 2 created
- [2026-04-21] **ingest** | Knowledge layer | 1 page updated, 2 created
- [2026-04-21] **ingest** | Gemini browser and utility updates | 2 pages updated, 1 created
- [2026-04-21] **apply** | Gemini Deep Research and Deep Research Max | 1 page updated (tools/gemini), 1 created (sources/articles/gemini-deep-research-max)
- [2026-04-21] **ingest** | Claude Opus 4.7 — capability gains with reliability tradeoffs | 3 pages updated, 2 created
- [2026-04-21] **ingest** | Claude Design and live artifacts expand Anthropic beyond chat | 4 pages updated, 2 created
- [2026-04-21] **ingest** | AI in biology — Noetik and GPT-Rosalind | 3 pages updated, 2 created
- [2026-04-21] **ingest** | Every — We Need to Talk About AI Autopilot | 2 pages updated, 4 created
- [2026-04-21] **ingest** | Agentic orchestration patterns | 2 pages updated, 5 created; added subcategory `agentic-orchestration-patterns`
- [2026-04-21] **ingest** | Agentic coding UIs converge on supervision, not editing | 4 pages updated, 2 created
- [2026-04-21] **apply** | Orca | 3 pages updated (state-of/coding, state-of/agents, wiki/index), 2 created (tools/orca, sources/articles/orca-homepage)
- [2026-04-21] **triage** | Personal digest 2026-04-08 to 2026-04-14 | 7 proposals generated, 1 skipped
- [2026-04-21] **apply** | Anthropic platform expansion | 2 pages updated (tools/claude-managed-agents, state-of/agents), 1 created (sources/newsletters/anthropic-platform-expansion-april-2026); clarified Anthropic custom agents/productivity-surface context
- [2026-04-21] **apply** | Coding agent control planes | 4 pages updated (tools/cursor, state-of/coding, state-of/agents, wiki/index), 1 created (sources/newsletters/coding-agent-control-planes)
- [2026-04-21] **apply** | Harness engineering patterns | 2 pages updated (concepts/harness, workflows/agentic-orchestration-patterns), 1 created (sources/newsletters/harness-engineering-patterns)
- [2026-04-21] **apply** | AI adoption is management | 2 pages updated (training/company-wide-ai-enablement, trends/agents-reshape-organizations), 1 created (sources/newsletters/ai-adoption-is-management)
- [2026-04-21] **apply** | Open agentic coding models | 2 pages updated (state-of/models, wiki/index), 3 created (models/glm-5-1, models/minimax-m2-7, sources/newsletters/open-agentic-coding-models)
- [2026-04-21] **apply** | Restricted frontier deployment | 1 page updated (state-of/models), 2 created (trends/restricted-frontier-deployment, sources/newsletters/restricted-frontier-deployment)
- [2026-04-21] **apply** | Claude productivity surfaces | 3 pages updated (tools/claude-cowork, state-of/agents, tools/claude-managed-agents), 1 created (sources/tweets/claude-productivity-surfaces)
- [2026-04-21] **triage** | Personal digest 2026-04-01 to 2026-04-07 | 5 proposals generated, 3 skipped
- [2026-04-21] **apply** | Claude Code leak architecture lessons | 3 pages updated (tools/claude-code, concepts/harness, state-of/coding), 1 created (sources/newsletters/claude-code-leak-architecture)
- [2026-04-21] **apply** | Cursor 3 orchestration bet | 2 pages updated (tools/cursor, state-of/coding), 1 created (sources/newsletters/cursor-3-orchestration-bet)
- [2026-04-21] **apply** | Harness engineering in early April | 2 pages updated (concepts/harness, workflows/agentic-orchestration-patterns), 1 created (sources/newsletters/harness-engineering-early-april)
- [2026-04-21] **apply** | Agent-native organizations in early April | 2 pages updated (training/company-wide-ai-enablement, trends/agents-reshape-organizations), 1 created (sources/newsletters/agent-native-organizations-early-april)
- [2026-04-21] **apply** | Open-weight momentum in early April | 3 pages updated (state-of/models, state-of/computer-use, wiki/index), 2 created (trends/open-weight-momentum-broadens, sources/newsletters/open-weight-momentum-early-april)
- [2026-04-21] **triage** | Personal digest 2026-03-24 to 2026-03-31 | 6 proposals generated, 1 skipped
- [2026-04-21] **apply** | Claude computer use in late March | 2 pages updated (state-of/computer-use, tools/claude-code), 1 created (sources/newsletters/claude-computer-use-late-march)
- [2026-04-21] **apply** | Agent coworkers as an operating pattern | 2 pages updated (training/company-wide-ai-enablement, trends/agents-reshape-organizations), 1 created (sources/newsletters/agent-coworkers-operating-pattern)
- [2026-04-21] **apply** | Open-agent orchestration in late March | 2 pages updated (workflows/agentic-orchestration-patterns, state-of/agents), 1 created (sources/newsletters/open-agent-orchestration-late-march)
- [2026-04-21] **apply** | Voice becomes an agent interface | 1 page updated (wiki/index), 2 created (trends/voice-becomes-agent-interface, sources/newsletters/voice-becomes-agent-interface)
- [2026-04-21] **apply** | Runtime improvements improve agent economics | 1 page updated (trends/compute-infrastructure), 1 created (sources/newsletters/runtime-improvements-improve-agent-economics)
- [2026-04-21] **apply** | AI-native product-building lessons in late March | 1 page updated (training/company-wide-ai-enablement), 1 created (sources/newsletters/ai-native-product-building-lessons-late-march)
- [2026-04-21] **triage** | Personal digest 2026-03-17 to 2026-03-23 | 6 proposals generated, 1 skipped
- [2026-04-21] **ingest** | Anthropic desktop-agent expansion in late March | 3 pages updated, 1 created
- [2026-04-21] **ingest** | Late-March small coding models | 5 pages updated, 1 created
- [2026-04-21] **ingest** | Agent memory without vector databases | 1 page updated, 2 created
- [2026-04-21] **ingest** | Skills and plugin packaging in late March | 4 pages updated, 1 created
- [2026-04-21] **ingest** | AI style guides | 1 page updated, 2 created
- [2026-04-21] **ingest** | AI-native product building | 1 page updated, 2 created
- [2026-04-22] **triage** | Personal digest 2026-03-10 to 2026-03-16 | 5 proposals, 0 skipped
- [2026-04-22] **ingest** | AI for boring businesses | 1 page updated, 1 created
- [2026-04-22] **ingest** | Coding agents shift toward review and concurrent supervision | 2 pages updated, 1 created
- [2026-04-22] **ingest** | Harness engineering as a systems problem | 2 pages updated, 1 created
- [2026-04-22] **ingest** | Perplexity Personal Computer | 2 pages updated, 1 created
- [2026-04-22] **apply** | Proof as an agent-native document tool | 2 pages updated (state-of/agents, wiki/index), 2 created (tools/proof, sources/newsletters/proof-agent-native-documents); added subcategory `agent-native-documents`
- [2026-04-22] **triage** | Personal digest 2026-03-03 to 2026-03-09 | 7 proposals generated, 0 skipped
- [2026-04-22] **ingest** | Cursor cloud agents and the supervision workspace thesis | 3 pages updated, 1 created
- [2026-04-22] **ingest** | Claude Code scheduled tasks and `/loop` | 2 pages updated, 1 created
- [2026-04-22] **ingest** | Codex Security | 2 pages updated, 1 created
- [2026-04-22] **ingest** | GPT-5.4 | 2 pages updated, 2 created
- [2026-04-22] **ingest** | OpenClaw as an operating pattern | 2 pages updated, 1 created
- [2026-04-22] **ingest** | AI work intensification | 2 pages updated, 1 created
- [2026-04-22] **ingest** | Harness engineering debate in March | 1 page updated, 1 created
- [2026-04-22] **triage** | Personal digest 2026-02-24 to 2026-03-02 | 8 proposals generated, 0 skipped
- [2026-04-22] **ingest** | Cursor cloud agents in late February | 2 pages updated, 1 created
- [2026-04-22] **ingest** | Anthropic persistent workflow surfaces in late February | 2 pages updated, 1 created
- [2026-04-22] **ingest** | Desktop and mobile computer-use surfaces in late February | 1 page updated, 1 created
- [2026-04-22] **ingest** | OpenClaw operating pattern in late February | 2 pages updated, 1 created
- [2026-04-22] **ingest** | Memory versus context rot in late February | 2 pages updated, 1 created
- [2026-04-22] **ingest** | Post-vibe-coding verification and cognitive debt in late February | 2 pages updated, 1 created
- [2026-04-22] **ingest** | Anthropic Pentagon deployment boundaries in late February | 1 page updated, 1 created
- [2026-04-22] **ingest** | Qwen 3.5 medium models in late February | 2 pages updated, 1 created
- [2026-04-22] **triage** | AI Email Digest 2026-04-21 to 2026-04-22 | 8 proposals generated, 3 skipped (Cursor/SpaceX acquisition, Anthropic Mythos leak, Monologue Notes)
- [2026-04-22] **ingest** | Shopify AI phase transition — Latent Space (April 2026) | 2 pages updated (harness, company-wide-ai-enablement), 2 created (ai-enablement-software-development, shopify-latent-space-april-2026)
- [2026-04-22] **ingest** | Gemini Deep Research Max benchmarks — AINews | 2 pages updated (tools/gemini, state-of/agents)
- [2026-04-22] **ingest** | Qwen 3.6 community reception + Max Preview | 2 pages updated (models/qwen-3-6-35b-a3b, state-of/models)
- [2026-04-22] **ingest** | HF ml-intern autonomous research agent | 1 page updated (state-of/agents), 1 created (tools/hf-ml-intern); schema: autonomous-research-agent
- [2026-04-22] **ingest** | Hermes Agent expansion + Claude Code recap + harness additions | 3 pages updated (tools/hermes-agent, tools/claude-code, concepts/harness), 1 created (sources/thecode-april-22-2026)
- [2026-04-22] **ingest** | GPT-Image-2 launch | 1 page updated (state-of/models), 2 created (models/gpt-image-2, sources/ainews-2026-04-22); schema: image-generation-model
- [2026-04-22] **ingest** | AI security surface — vibe-coding defaults + agent-as-watchdog | 1 page updated (training/anti-autopilot-review-friction), 1 created (sources/every-vibe-check-april-21-2026)
- [2026-04-22] **ingest** | Agent org patterns — trust batteries, AI sandwich, tokenmaxxing | 2 pages updated (trends/agents-reshape-organizations, training/company-wide-ai-enablement), 1 created (sources/every-ai-sandwich-april-2026)
- [2026-04-22] **triage** | URL batch 2026-04-22 | 15 proposals generated, 53 skipped; Glasswing/Mythos, Claude Design, Cursor 3rd era, slopsquatting, gstack, Simon Willison/Lenny, Prof Devs Control, Every 4 agents, Spec Is New Code, Claude Code features, Codex updates, self-improving skills, cognitive overhead, Nano Banana 2, quantization
- [2026-04-22] **schema** | vocabulary addition | added domain `cybersecurity`
- [2026-04-22] **ingest** | slopcop / slopsquatting — LLM hallucinated packages as supply chain attack | 2 pages updated (state-of/coding, state-of/cybersecurity), 3 created (concepts/slopsquatting, state-of/cybersecurity, sources/repos/slopcop-repo)
- [2026-04-22] **ingest** | "The Spec Is the New Code" — SDD ecosystem convergence | 1 page updated (concepts/spec-driven-development), 1 created (sources/tweets/spec-is-new-code)
- [2026-04-22] **ingest** | Simon Willison / Lenny — AI coding inflection takeaways | 2 pages updated (training/ai-enablement-software-development, training/anti-autopilot-review-friction), 1 created (sources/tweets/lennysan-simonw-interview)
- [2026-04-22] **ingest** | Self-improving agent skills — auto-improvement loops | 1 page updated (concepts/agent-improvement-loop), 1 created (sources/tweets/self-improving-skills)
- [2026-04-22] **ingest** | Quantization — ngrok blog explainer | 2 created (concepts/quantization, sources/articles/ngrok-quantization)
- [2026-04-22] **schema** | vocabulary addition | added subcategory `visual-design-prototyping`
- [2026-04-22] **ingest** | Agentic cognitive overhead — Addy Osmani / Simon Willison | 1 page updated (training/ai-enablement-software-development), 1 created (sources/tweets/agentic-cognitive-overhead)
- [2026-04-22] **ingest** | Claude Code features — worktrees, /autofix-pr, Remote Control | 1 page updated (tools/claude-code), 1 created (sources/tweets/claude-code-worktree-autofix)
- [2026-04-22] **ingest** | Claude Design full launch — Anthropic Labs | 2 pages updated (tools/claude-design, state-of/creative), 1 created (sources/articles/claude-design-anthropic-labs); schema: visual-design-prototyping
- [2026-04-22] **ingest** | Codex updates — subagents, usage-based pricing, PR review | 1 page updated (tools/codex), 1 created (sources/tweets/codex-updates-april-2026)
- [2026-04-22] **ingest** | Cursor third era — Truell essay + Shipper vibe check | 3 pages updated (tools/cursor, state-of/coding, trends/agents-reshape-organizations), 1 created (sources/tweets/cursor-third-era)
- [2026-04-22] **ingest** | Every — 25-person company on four Notion agents | 1 page updated (training/company-wide-ai-enablement), 1 created (sources/articles/every-four-agents)
- [2026-04-22] **ingest** | Project Glasswing — Claude Mythos Preview | 4 pages updated (state-of/models, state-of/cybersecurity, trends/restricted-frontier-deployment, state-of/models), 2 created (models/claude-mythos-preview, sources/articles/glasswing)
- [2026-04-22] **ingest** | gstack — Garry Tan's Claude Code virtual team config | 2 pages updated (training/ai-enablement-software-development), 2 created (tools/gstack, sources/repos/garrytan-gstack-repo)
- [2026-04-22] **ingest** | Nano Banana 2 — Google image generation model | 1 page updated (state-of/models), 2 created (models/nano-banana-2, sources/tweets/nano-banana-2-tweet)
- [2026-04-22] **ingest** | Professional devs control — field research N=99 | 1 page updated (training/anti-autopilot-review-friction), 1 created (sources/tweets/prof-devs-control)
- [2026-04-23] **apply** | Personal Wiki Agent framework research (reusable subset) | 3 pages updated (workflows/agentic-orchestration-patterns, concepts/mcp, wiki/index), 4 created (sources/articles/deep-agents-overview, sources/articles/goose-platform, sources/articles/anthropic-mcp-deployment-surfaces, sources/articles/openai-chatgpt-mcp-surfaces)
- [2026-04-23] **apply** | OpenAI Workspace Agents | 3 pages updated (tools/codex, state-of/agents, wiki/index), 1 created (sources/newsletters/superhuman-2026-04-23)
- [2026-04-23] **apply** | GPT-5.5 launch | 6 pages updated (tools/codex, state-of/models, models/claude-opus-4-7, state-of/cybersecurity, state-of/science, wiki/index), 4 created (models/gpt-5-5, history/models/gpt-5-4, sources/articles/openai-gpt-5-5-launch, sources/tweets/danshipper-gpt-5-5-vibe-check), 1 removed from current (models/gpt-5-4); operating rule updated in LLM-INSTRUCTIONS for superseded versions
- [2026-04-23] **apply** | Anthropic MCP production guidance + Cowork on Bedrock | 4 pages updated (concepts/mcp, tools/claude-cowork, state-of/agents, wiki/index), 2 created (sources/articles/anthropic-mcp-production-systems, sources/tweets/awsai-cowork-bedrock-2026-04-23)
- [2026-04-23] **apply** | Google Cloud Next 2026 | 6 pages updated (tools/gemini, tools/google-adk, trends/compute-infrastructure, state-of/agents, state-of/models, wiki/index), 1 created (sources/articles/google-cloud-next-2026)
- [2026-04-23] **schema** | structural reorganization | merged agent-orchestration-ui + agent-orchestration + model-orchestration → agent-orchestration; moved claude-design to creative only; moved Deep Research content from gemini to deep-research; fixed genspark-slides placement in state-of/creative
- [2026-04-23] **apply** | AI-native engineering interviews | 2 pages updated (training/ai-enablement-software-development, wiki/index)
- [2026-04-23] **apply** | Microsoft Foundry Hosted Agents | 2 pages updated (state-of/agents, wiki/index), 2 created (tools/microsoft-foundry-agents, sources/articles/microsoft-foundry-agents-2026)
- [2026-04-23] **apply** | Qwen 3.6 27B | 2 pages updated (state-of/models, models/qwen-3-6-35b-a3b), 3 created (models/qwen-3-6-27b, sources/newsletters/ainews-2026-04-23, sources/newsletters/the-code-2026-04-23)
- [2026-04-23] **apply** | Skillify — Agent Reliability Pattern | 1 page updated (state-of/agents), 2 created (workflows/skillify-agent-reliability, sources/tweets/garrytan-skillify-2026-04-23)
- [2026-04-23] **triage** | Email Digest — Ai — 2026-04-22 to 2026-04-23 | 3 new proposals, 1 existing proposal updated, 0 skipped; signals: Anthropic 81K economics survey, Microsoft Foundry Hosted Agents, Claude Code /ultrareview, Google GEAP full blog (merged into 2026-04-23-google-cloud-next.md)
- [2026-04-23] **triage** | Email Digest — Ai — 2026-04-23 | 8 proposals generated, 2 skipped (SpaceX/Cursor, Claude Mythos); signals: Qwen3.6-27B, OpenAI Workspace Agents, Google Cloud Next, OpenAI Privacy Filter, Anthropic MCP+Cowork/Bedrock, Skillify pattern, Tokenmaxxing, AI-native engineering interviews
- [2026-04-23] **apply** | Anthropic 81K Economics Survey | 1 page updated (training/company-wide-ai-enablement), 1 created (sources/articles/anthropic-81k-economics)
- [2026-04-23] **apply** | Claude Code /ultrareview | 1 page updated (tools/claude-code), 1 created (sources/articles/claude-code-ultrareview)
- [2026-04-23] **apply** | OpenAI Privacy Filter | 2 pages updated (state-of/models, wiki/index), 1 created (models/openai-privacy-filter); schema: utility-model subcategory added
- [2026-04-23] **apply** | Tokenmaxxing — Tasteful vs. Wasteful | 1 page updated (training/company-wide-ai-enablement: Jensen Huang quote added to tokenmaxxing failure mode, "tasteful tokenmaxxing" proven pattern added)
- [2026-04-23] **lint** | wiki-wide contradiction and categorization audit | 16 issues resolved: 5 schema fixes (tags, domains, subcategories); 6 domain corrections (codex +cybersecurity, perplexity-computer +finance, voice tools +voice, shopify-ai-toolkit +agents); hermes-agent reclassified agent-orchestration→agent-framework; cowork removed from computer-use; state-of/coding terminal-agent dates updated; "Agent orchestration UIs" label corrected; 6 new pages (state-of/voice, benchmarks/swe-bench, concepts/deep-research, tools/openai-deep-research, tools/gemini-deep-research); tools/deep-research retired to redirect; cross-links added between harness, agent-improvement-loop, skillify, knowledge-layer, agent-memory
- [2026-04-24] **apply** | Broaden agentic DevOps tooling coverage | 4 pages updated (wiki/_schema/subcategories, state-of/agents, state-of/coding, wiki/index), 4 created (tools/kagent, tools/k8sgpt, tools/skyflo, tools/checkly); proposal archived
- [2026-04-24] **apply** | Training page for safe agentic infrastructure operations | 3 pages updated (training/company-wide-ai-enablement, training/anti-autopilot-review-friction, wiki/index), 2 created (training/agentic-infrastructure-operations, sources/deep-research/2026-04-24-agentic-devops); proposal archived
- [2026-04-24] **apply** | QA tooling layer for software-agent verification | 3 pages updated (training/evals-for-agentic-software-development, training/ai-enablement-software-development, wiki/index); reused existing source summary wiki/sources/deep-research/2026-04-24-qa-tooling-for-software-agents; proposal archived
- [2026-04-24] **apply** | Core tool pages for software-agent verification infrastructure | 1 page updated (wiki/index), 5 created (tools/e2b, tools/agentrial, tools/stagehand, tools/browserbase, sources/deep-research/2026-04-24-qa-tooling-for-software-agents); proposal archived
- [2026-04-24] **apply** | Agent eval taxonomy and trajectory framing | 3 pages updated (concepts/harness, wiki/sources/deep-research/2026-04-23-agents-evals, wiki/index), 1 created (concepts/agent-evals); proposal archived
- [2026-04-24] **apply** | Autonomy ladder and eval-gated permission governance | 4 pages updated (training/company-wide-ai-enablement, training/anti-autopilot-review-friction, wiki/sources/deep-research/2026-04-23-agents-evals, wiki/index); proposal archived
- [2026-04-24] **apply** | Agent benchmark map | 4 pages updated (wiki/benchmarks/swe-bench, wiki/benchmarks/swe-polybench, wiki/sources/deep-research/2026-04-23-agents-evals, wiki/index), 6 created (benchmarks/osworld, benchmarks/webarena, benchmarks/tau-bench, benchmarks/gaia, benchmarks/toolbench, benchmarks/terminal-bench); proposal archived
- [2026-04-24] **apply** | Eval lifecycle expansion | 3 pages updated (wiki/concepts/agent-improvement-loop, wiki/sources/deep-research/2026-04-23-agents-evals, wiki/index); proposal archived
- [2026-04-24] **apply** | Evals for agentic software development | 2 pages updated (wiki/index, training/ai-enablement-software-development), 1 created (training/evals-for-agentic-software-development)
- [2026-04-24] **apply** | Google ADK 2.0 orchestration patterns | 2 pages updated (tools/google-adk, workflows/agentic-orchestration-patterns), 1 created (sources/tweets/googlecloudtech-adk-2-orchestration-patterns); wiki/index blurbs refreshed
- [2026-04-24] **apply** | Evals for workflow and task agents | 2 pages updated (wiki/index, training/company-wide-ai-enablement), 1 created (training/evals-for-agentic-work)
- [2026-04-24] **triage** | Email Digest — Ai — 2026-04-23 to 2026-04-24 | 2 full-ingest candidates, 2 verify-first, 1 lightweight, 1 hold; skipped as duplicates/promos: GPT-5.5 repeat coverage, McKinsey repeat coverage, Every Codex camp promo; signals: DeepSeek V4 Preview, Managed Agents memory, Codex broader computer-work surface, Claude Code one-time scheduling, Microsoft Copilot agent mode
- [2026-04-24] **triage** | Email Digest — Ai — 2026-04-23 to 2026-04-24 (processed) | 5 proposals generated, 0 skipped; proposals: DeepSeek V4 Preview, Claude Managed Agents memory, Codex broader computer-work surface, Claude Code one-time scheduling, Microsoft Copilot agent mode in Office
- [2026-04-24] **triage** | Agent Evals Research Report — 2026-04-23 | 7 proposals generated, 0 skipped; signals: agent eval taxonomy (concept page), coding evals training page, autonomy ladder (training updates), workflow evals training page, benchmark map (6 new + 2 updated), eval tool pages (Braintrust/Promptfoo/Langfuse), eval lifecycle update; signal 5 (LLM-as-judge) folded into proposals 2 and 4
- [2026-04-24] **triage** | QA Tooling for Software Agents Research Report — 2026-04-24 | 6 proposals generated, 0 skipped; signals: execution sandboxes, dual-track trajectory/output tooling, QA-to-eval pipeline, browser self-verification, proof-artifact lineage, selective tooling map (E2B/Agentrial/Stagehand/Browserbase as strongest candidates)
- [2026-04-24] **triage** | Agentic DevOps Research Report — 2026-04-24 | 7 proposals generated, 0 skipped; signals: broader agentic-devops category framing, tri-state execution governance, deterministic policy engines, MCP/A2A operations context, Kubernetes/observability agent tooling shortlist, mandatory sandboxing, and a likely training-page gap around safe infrastructure operations
- [2026-04-24] **triage** | QA Tooling for Software Agents Research Report — 2026-04-24 (processed) | 2 proposal files created; scope split into training/process guidance and selective tool-page promotion
- [2026-04-24] **triage** | Agentic DevOps Research Report — 2026-04-24 (processed) | 2 proposal files created; scope split into training guidance and selective tool/state-of expansion
- [2026-04-24] **ingest** | Copilot's agentic capabilities in Word, Excel, and PowerPoint are generally available | 2 pages updated, 2 created
- [2026-04-24] **ingest** | DeepSeek V4 Preview | 3 pages updated, 2 created
- [2026-04-24] **ingest** | Codex broadens into computer work | 3 pages updated, 1 created
- [2026-04-24] **ingest** | Built-in memory for Claude Managed Agents | 3 pages updated, 1 created
- [2026-04-24] **ingest** | Claude Code one-time scheduling | 1 page updated, 1 created
- [2026-04-24] **ingest** | Eval observability tool pages (Braintrust, Promptfoo, Langfuse) | 1 page updated, 4 created; schema: agent-eval-tooling
- [2026-04-25] **ingest** | Google-Anthropic compute report | 3 pages updated, 0 created
- [2026-04-25] **ingest** | AINews DeepSeek V4 release follow-through | 4 pages updated, 1 created
- [2026-04-25] **triage** | Email Digest — Ai — 2026-04-25 (processed) | 2 proposals generated, 0 skipped; proposals: DeepSeek V4 release follow-through, Google-Anthropic compute report
- [2026-04-25] **triage** | Email Digest — Ai — 2026-04-25 | 1 full-ingest candidate, 1 lightweight; skipped as out of scope/promo: Superhuman robotics special, Every Sparkle email
- [2026-05-05] **triage** | AI Email Digest 2026-05-01 | 8 proposals generated, 1 skipped (Contra Labs Human Creativity Benchmark unchecked)
- [2026-05-05] **triage** | AI Email Digest 2026-04-30 to 2026-05-01 | 11 proposals generated, 1 skipped
- [2026-05-05] **triage** | AI Email Digest 2026-04-29 to 2026-05-01 | 7 proposals generated, 5 skipped
- [2026-05-05] **triage** | AI Email Digest 2026-04-28 to 2026-05-01 | 12 proposals generated, 1 skipped
- [2026-05-13] **apply** | Remaining pending proposals batch | 10 pages updated (state-of/science, state-of/voice, state-of/models, state-of/agents, state-of/cybersecurity, tools/hermes-agent, models/claude-mythos-preview, models/qwen-3-6-35b-a3b, wiki/index, wiki/log), 1 tool page created, 7 sources created; proposals archived
- [2026-05-13] **apply** | Perplexity agent skill methodology | 1 page created (training/agent-skill-methodology), 1 source created, index updated
- [2026-05-13] **apply** | Claude Code /goal, fast mode, and FleetView | 2 pages updated (tools/claude-code, state-of/coding), 1 source created, 1 history page created
- [2026-05-13] **apply** | End of finetuning debate | 2 pages updated (state-of/models, state-of/coding), 1 source created
- [2026-05-13] **apply** | Arena leaderboard May 2026 | 1 page updated (state-of/models — Opus 4.7, GPT-5.5, Gemini 3.1 Pro, Grok 4.20, Meta Spark, Veo 3.1 added/updated), 1 source created
- [2026-05-13] **apply** | Anthropic SpaceX compute deal + Claude Managed Agents Dreams | 3 pages updated (tools/claude-managed-agents, state-of/models, tools/claude-code), 1 source created
- [2026-05-13] **apply** | AI work delegation modes | 1 page created (training/ai-work-delegation-modes), 1 source created, index updated
- [2026-05-13] **apply** | Google DeepMind AI Co-Mathematician | 1 page updated (state-of/science), 1 source created
- [2026-05-13] **triage** | AI digest 2026-05-07 to 2026-05-13 | 14 proposals generated, 6 signals trimmed (signal-quality audit); triage moved to applied/
- [2026-05-13] **apply** | Symphony and Devin terminal orchestration | 2 pages updated (tools/codex, state-of/coding), 1 created (sources/newsletters/symphony-devin-terminal-orchestration-2026-04-28)
- [2026-05-13] **apply** | Stripe agent-native commerce and compute fraud | 2 pages updated (state-of/finance, trends/compute-infrastructure), 1 created (sources/newsletters/stripe-agent-native-commerce-fraud-2026-04-29)
- [2026-05-13] **apply** | Production agent orchestration primitives (Mistral Workflows) | 2 pages updated (workflows/agentic-orchestration-patterns, state-of/agents), 1 created (sources/newsletters/production-agent-orchestration-2026-04-29)
- [2026-05-13] **apply** | Persistent cloud computers for agents (Manus) | 2 pages updated (state-of/agents, trends/compute-infrastructure), 1 created (sources/newsletters/persistent-cloud-computers-agents-2026-05-01)
- [2026-05-13] **apply** | Parallel Web Systems agent web API market signal | 1 page updated (trends/compute-infrastructure), 1 created (sources/newsletters/parallel-web-agent-apis-2026-04-30)
- [2026-05-13] **apply** | Opus 4.7 tokenizer economics | 2 pages updated (models/claude-opus-4-7, training/evals-for-agentic-software-development), 1 created (sources/newsletters/opus-4-7-tokenizer-economics-2026-04-30)
- [2026-05-13] **apply** | Open-weight pricing pressure on closed-frontier | 2 pages updated (trends/open-weight-momentum-broadens, state-of/models), 1 created (sources/newsletters/open-weight-pricing-pressure-2026-04-29)
- [2026-05-13] **apply** | Open-weight economics fragmenting by deployment constraint | 2 pages updated (trends/open-weight-momentum-broadens, state-of/models), 1 created (sources/newsletters/open-weight-economics-fragmenting-2026-04-30)
- [2026-05-13] **apply** | NVIDIA Nemotron 3 Nano Omni (caveated signal) | 1 page updated (trends/open-weight-momentum-broadens), 1 created (sources/newsletters/nvidia-nemotron-3-nano-omni-2026-04-29)
- [2026-05-13] **apply** | Meta Ads MCP and CLI (source only; wiki updates deferred pending primary verification) | 0 pages updated, 1 created (sources/tweets/meta-ads-mcp-cli-2026-04-30)
- [2026-05-13] **apply** | Local and offline agents become more credible | 2 pages updated (trends/open-weight-momentum-broadens, concepts/quantization), 1 created (sources/newsletters/local-offline-agents-2026-04-29)
- [2026-05-13] **apply** | Knowledge-work OS agent apps | 2 pages updated (state-of/computer-use, trends/agents-reshape-organizations), 1 created (sources/newsletters/knowledge-work-os-agent-apps-2026-04-28)
- [2026-05-13] **apply** | Inference inflection and agent runtime bottlenecks | 2 pages updated (trends/compute-infrastructure, state-of/agents), 1 created (sources/newsletters/inference-inflection-agent-runtime-2026-04-30)
- [2026-05-13] **apply** | Gemini downloadable file generation | 2 pages updated (tools/gemini, state-of/computer-use), 1 created (sources/newsletters/gemini-downloadable-files-2026-04-30)
- [2026-05-13] **apply** | Cursor SDK as programmable coding-agent runtime | 2 pages updated (tools/cursor, state-of/coding), 1 created (sources/newsletters/cursor-sdk-agent-runtime-2026-04-30)
- [2026-05-13] **apply** | Cost-aware agent evaluation | 2 pages updated (training/evals-for-agentic-software-development, concepts/agent-evals), 1 created (sources/newsletters/cost-aware-agent-evaluation-2026-04-28)
- [2026-05-13] **apply** | Claude creative tool connectors (Adobe, Blender, Ableton, etc.) | 2 pages updated (tools/claude-design, state-of/creative), 1 created (sources/newsletters/claude-creative-tool-connectors-2026-04-29)
- [2026-05-13] **apply** | Claude Code for product-management workflows | 2 pages updated (tools/claude-code, training/company-wide-ai-enablement), 1 created (sources/newsletters/claude-code-product-management-2026-05-01)
- [2026-05-13] **apply** | China-origin open agent-model releases | 1 page updated (trends/open-weight-momentum-broadens), 1 created (sources/newsletters/china-open-agent-models-2026-04-28)
- [2026-05-13] **apply** | Amazon Quick work-context assistant (caveated stub) | 1 page updated (state-of/computer-use), 2 created (tools/amazon-quick, sources/newsletters/amazon-quick-work-context-assistant-2026-04-29)
- [2026-05-13] **apply** | AI-managed orchestration and local browser agents | 2 pages updated (workflows/agentic-orchestration-patterns, state-of/agents), 1 created (sources/newsletters/ai-managed-orchestration-local-browser-agents-2026-04-28)
- [2026-05-13] **apply** | Big Tech earnings and AI capex signal | 1 page updated (trends/compute-infrastructure), 1 created (sources/newsletters/ai-earnings-capex-2026-04-30)
- [2026-05-13] **apply** | Qwen 3.6 27B Artificial Analysis follow-up | 2 pages updated (models/qwen-3-6-27b, state-of/models), 1 created (sources/newsletters/qwen-3-6-27b-aa-2026-05-01)
- [2026-05-13] **apply** | Microsoft Word Legal Agent | 4 pages updated (state-of/legal, tools/microsoft-copilot, wiki/index, _schema note), 2 created (tools/microsoft-word-legal-agent, sources/articles/microsoft-word-legal-agent)
- [2026-05-13] **apply** | Codex for Work positioning | 4 pages updated (tools/codex, state-of/computer-use, state-of/agents, wiki/index n/a), 1 created (sources/newsletters/codex-for-work-2026-05-01)
- [2026-05-13] **apply** | AI security scanners as first-class products | 2 pages updated (state-of/cybersecurity, tools/cursor), 1 created (sources/newsletters/ai-security-scanners-2026-05-01)
- [2026-05-13] **apply** | AI music as commercial category | 2 pages updated (state-of/creative, wiki/_schema/subcategories), 3 created (trends/ai-music-commercialization, sources/newsletters/ai-music-commercialization-2026-05-01); schema addition: ai-music-generation subcategory
- [2026-05-13] **schema** | vocabulary addition | added subcategory `ai-music-generation`
- [2026-05-13] **apply** | AI coding dictionary (Matt Pocock) | 2 pages updated (concepts/harness, wiki/index), 2 created (training/ai-coding-vocabulary, sources/repos/mattpocock-dictionary-of-ai-coding)
- [2026-05-13] **apply** | Agent infrastructure harness and deployment primitives | 3 pages updated (concepts/harness, workflows/agentic-orchestration-patterns, state-of/agents), 1 created (sources/newsletters/agent-infrastructure-harness-2026-05-01)
- [2026-05-13] **triage** | Manual URL Batch 2026-05-13 | 8 proposals, 4 skipped
- [2026-05-13] **triage** | AI Email Digest 2026-04-14 to 2026-05-13 | 12 proposals, 3 skipped
- [2026-05-13] **ingest** | Claude Managed Agents same-day platform features | 1 page updated, 1 created
- [2026-05-13] **ingest** | Agent-generated HTML artifacts | 2 pages updated, 2 created
- [2026-05-13] **ingest** | Agentic security tooling category | 2 pages updated, 1 created
- [2026-05-13] **ingest** | AI-native organizations as operating model | 2 pages updated, 1 created
- [2026-05-13] **ingest** | Claude Code Agent View | 2 pages updated, 1 created
- [2026-05-13] **ingest** | Agent-native product management workflows | 2 pages updated, 1 created
- [2026-05-13] **ingest** | Purpose-built review artifacts for agent work | 2 pages updated, 1 created
- [2026-05-13] **ingest** | Agent skills, progressive context, evals, and migration discipline | 1 page updated, 1 created
- [2026-05-13] **ingest** | Codex and Claude Code as workflow operating systems | 3 pages updated, 0 created; unchecked source summary skipped
- [2026-05-13] **ingest** | Peekaboo 3.0 macOS computer-use release | 2 pages updated, 2 created
- [2026-05-13] **ingest** | Model-harness fit as product moat | 2 pages updated, 1 created
- [2026-05-13] **ingest** | OpenAI Daybreak for cyber defenders | 2 pages updated, 1 created
- [2026-05-13] **ingest** | Onboarding videos as an agent-skill use case | 2 pages updated, 2 created; unchecked training example skipped
- [2026-05-13] **ingest** | Frontier labs as deployment-service firms | 2 pages updated, 1 created
- [2026-05-13] **ingest** | GPT-5.5 Instant as ChatGPT default | 2 pages updated, 1 created
- [2026-05-13] **ingest** | Finance as packaged agent-workflow vertical | 2 pages updated, 1 created
- [2026-05-13] **ingest** | Cost discipline shifts to task routing | 1 page updated, 2 created
- [2026-05-13] **ingest** | Physical AI and robotics deployment curve | 1 page updated, 2 created
- [2026-05-18] **triage** | Email Digest AI 2026-05-12 to 2026-05-18 | 7 proposals generated (cursor-composer-2-5, claude-code-best-practices, claude-mythos-m5, chatgpt-personal-finance, ai-stack-fungibility, cerebras-ipo, codex-adoption-ecosystem), 1 signal skipped; triage moved to applied/
- [2026-05-18] **apply** | Notion External Agents API | 1 tool page created (tools/notion), 1 source created (sources/newsletters/notion-external-agents-api-may-2026), state-of/agents updated (Agent-native documents + Recent changes), wiki/index updated
- [2026-05-18] **apply** | Multica repo ingest | 1 tool page created (tools/multica), 1 source created (sources/repos/multica-ai-multica), state-of/agents updated (Agent orchestration + Recent changes), wiki/index updated
- [2026-05-18] **triage** | Email Digest AI 2026-05-09 to 2026-05-15 | 9 proposals generated, 5 signals skipped; triage moved to applied/
- [2026-05-19] **apply** | Codex Zoom + mobile updates | 1 page updated (tools/codex — Zoom plugin, keep-awake, recent changes), 1 source created; proposal archived
- [2026-05-19] **apply** | Cloudflare Project Glasswing | 3 pages updated (models/claude-mythos-preview — Glasswing section, state-of/cybersecurity — Mythos line + harness table, concepts/harness — narrow-scope agents pattern), 1 source created; proposal archived
- [2026-05-19] **apply** | Claude Code Fast mode default + spec-drift logging | 2 pages updated (tools/claude-code — fast mode default + Console diagnostics, training/anti-autopilot-review-friction — spec-drift pattern), 1 source created; proposal archived
- [2026-05-19] **apply** | Devin Auto-Triage | 2 pages updated (state-of/agents — Persistent coding agents + Recent changes, index), 2 created (tools/devin, sources/articles/devin-auto-triage-2026-05); proposal archived
- [2026-05-19] **apply** | Gas City software factory patterns | 2 pages updated (concepts/harness — 3 new patterns, workflows/agentic-orchestration-patterns — 2 new patterns), 1 source created (sources/newsletters/gas-city-software-factory-2026-05); proposal archived
- [2026-05-19] **apply** | Qwen 3.7 Arena preview | 3 pages updated (state-of/models, index), 2 created (models/qwen-3-7, sources/newsletters/qwen-3-7-arena-2026-05); proposal archived
- [2026-05-19] **apply** | Shopify Claude Code fleet patterns | 2 pages updated (training/ai-enablement-software-development — 3 patterns + evidence, concepts/harness — LLM proxy pattern), 1 source created (sources/articles/shopify-claude-code-bessemer-2026-05); proposal archived
- [2026-05-19] **triage** | Email Digest AI 2026-05-13 to 2026-05-19 — processed | 7 proposals generated (Cloudflare Glasswing harness, Devin Auto-Triage, Shopify Claude Code fleet patterns, Gas City software factory, Claude Code fast mode default, Qwen 3.7 Arena, Codex Zoom/mobile), 2 skipped (Anthropic/Stainless unchecked, HTML-over-Markdown unchecked)
- [2026-05-19] **triage** | Email Digest AI 2026-05-13 to 2026-05-19 | 9 signals generated (Cloudflare Mythos writeup, Devin Auto-Triage, Shopify Claude Code patterns, Anthropic/Stainless acquisition, Gas City patterns, Claude Code Fast mode default, HTML-over-Markdown, Qwen 3.7 Arena, Codex Zoom plugin), 5 signals skipped (Gen Z sentiment, MTP llama.cpp, context pruning, spec-drift pattern, Google I/O preview)
- [2026-05-19] **apply** | Codex-maxxing usage patterns (jxnl) | 1 page updated (tools/codex — Usage patterns section, second spill), 1 source created (sources/articles/codex-maxxing-jxnl-2026-05); proposal archived
- [2026-05-19] **apply** | Codex adoption metrics + ecosystem expansion | 2 pages updated (tools/codex — adoption bullets + spill, history/state-of/coding — spill), 2 created (history/tools/codex, sources/newsletters/codex-adoption-ecosystem-2026-05); proposal archived
- [2026-05-19] **apply** | Claude for Small Business + Legal | 2 pages updated (tools/claude-cowork — vertical bundles section, state-of/agents — Cowork line), source creation skipped (unchecked); proposal archived
- [2026-05-19] **apply** | Claude Mythos M5 MIE bypass | 2 pages updated (models/claude-mythos-preview — M5 section, state-of/models — Mythos entry), 1 source created (sources/newsletters/claude-mythos-m5-bypass-2026-05); proposal archived
- [2026-05-19] **apply** | Claude Code best practices (Anthropic engineering) | 1 page updated (tools/claude-code — Best practices section), 1 source created (sources/articles/anthropic-claude-code-best-practices-2026-05); proposal archived
- [2026-05-19] **apply** | ChatGPT @Finances personal finance agent | 2 pages updated (models/gpt-5-5 — @Finances section, state-of/finance — Personal finance AI entry), 1 source created (sources/newsletters/chatgpt-personal-finance-2026-05); proposal archived
- [2026-05-19] **apply** | Agentic coding trap — skill atrophy and supervision paradox | 1 page updated (training/ai-enablement-software-development), 1 source created (sources/newsletters/agentic-coding-trap-may-2026); personal draft created (takes/study-the-machine-agentic-engineering)
- [2026-05-19] **apply** | Agent-first IDE convergence (GitHub Copilot App, VS Code Agents, Cursor cloud envs) | 2 pages updated (tools/cursor, state-of/coding), 1 source created
- [2026-05-19] **apply** | AI stack fungibility + AI psychosis — Hashimoto | 1 page updated (training/ai-enablement-software-development), 1 source created
- [2026-05-19] **apply** | Opus 4.7 fast mode + return-from-Codex signal | 1 page updated (models/claude-opus-4-7), 1 source created
- [2026-05-19] **apply** | LangChain Interrupt cluster — LangSmith Engine, SmithDB, LangChain Labs | 3 pages updated (concepts/agent-improvement-loop, state-of/agents, wiki/index), 2 created (tools/langchain-langsmith, sources/newsletters/langchain-interrupt-may-2026); 1 history entry spilled
- [2026-05-19] **apply** | Karpathy coding-agent failure modes + CLAUDE.md success-criteria pattern | 1 page updated (training/ai-enablement-software-development); source creation skipped (unchecked)
- [2026-05-19] **lint** | maintenance pass | cap: 15 pages spilled to history (8 new history files created); schema: 2 tags added (xai, collaboration), 1 domain added (training); index: grok-build.md added; links: 1 broken link fixed (claude-cowork, multica source renamed); tag: qwen-3-7 open-weight→open-weights; 2 source orphans remain (ii-medical, meta-ads-mcp-cli) — require manual triage
- [2026-06-03] **ingest** | Introducing dynamic workflows in Claude Code | 3 pages updated (tools/claude-code, state-of/coding, workflows/agentic-orchestration-patterns), 1 created (sources/articles/dynamic-workflows-claude-code); wiki/index as_of bumps; no spill (recent-changes cap is 10, pages now at 6)
- [2026-06-10] **ingest** | Paperclip homepage | 2 pages updated (state-of/agents — Agent orchestration + as_of, index), 2 created (tools/paperclip, sources/articles/papercliping)
- [2026-06-16] **apply** | Stanford AI labor market data — junior worker displacement | 3 updated (training/ai-enablement-software-development — Stanford data block + evidence bullet + source, trends/agents-reshape-organizations — Stanford bullet + recent change + source), 1 created (sources/newsletters/stanford-labor-june-2026)
- [2026-06-17] **apply** | Cartesia Sonic-3.5 + Ink-2 | 1 page updated (state-of/voice — Cartesia entry + recent change), 2 created (tools/cartesia, sources/newsletters/cartesia-voice-june-2026); proposal archived
- [2026-06-17] **triage** | Email Digest AI 2026-06-12 to 2026-06-17 | 12 proposals generated (fable-mythos-ban, glm-52-release, spacex-cursor-acquisition, loopcraft-agent-native, model-neutrality, openai-economics, copilot-cowork-ga, databricks-summit, stanford-labor-market, kimi-k27-code, cartesia-voice, ai-referred-shoppers), 0 skipped; triage moved to applied/
- [2026-06-17] **apply** | LLMs as commercial discovery channel | 2 created (trends/llm-as-discovery-channel, sources/newsletters/ai-referred-shoppers-june-2026); index updated
- [2026-06-17] **apply** | Microsoft Copilot Cowork GA | 1 updated (tools/microsoft-copilot — Cowork GA bullets + recent change), 1 created (sources/newsletters/copilot-cowork-ga-june-2026)
- [2026-06-17] **apply** | Claude Fable 5 / Mythos 5 export control ban | 4 updated (trends/restricted-frontier-deployment — export controls section, state-of/models — Fable 5 entry + Mythos update, state-of/coding — Claude Code DeepSWE note), 2 created (models/claude-fable-5, sources/newsletters/fable-ban-june-2026)
- [2026-06-17] **apply** | GLM-5.2 release | 1 updated (state-of/models — GLM-5.2 entry), 2 created (models/glm-5-2, sources/newsletters/ainews-glm-52-june-2026), 1 archived (models/glm-5-1 → history/)
- [2026-06-17] **apply** | Kimi K2.7-Code release | 1 updated (state-of/models — Kimi K2.7-Code entry), 2 created (models/kimi-k2-7-code, sources/newsletters/kimi-k27-code-june-2026), 1 archived (models/kimi-k2-6 → history/)
- [2026-06-17] **apply** | Loopcraft / agent-native architecture | 2 updated (training/ai-native-product-building — loop-first guidance + patterns + evidence, workflows/agentic-orchestration-patterns — 3 new patterns + surfaced section), 1 created (sources/newsletters/loopcraft-june-2026); loopcraft-june-2026 source also wired into concepts/harness (deferred from model-neutrality proposal)
- [2026-06-17] **apply** | Databricks Data + AI Summit — Genie One, Unity AI Gateway, Lakebase | 2 created (tools/databricks, sources/newsletters/databricks-summit-june-2026); index updated
- [2026-06-17] **apply** | SpaceX acquires Cursor + Cursor Origin | 4 updated (tools/cursor — acquisition + Origin section, tools/grok-build — jointly trained model note, state-of/coding — Cursor entry, trends/open-weight-momentum-broadens — model sovereignty section), 1 created (sources/newsletters/spacex-cursor-june-2026)
- [2026-06-17] **triage** | Email Digest AI 2026-06-01 to 2026-06-07 | 15 signals (12 full ingest, 3 lightweight); 5 URL stubs JS-blocked or broken, skipped; triage at proposals/triage/2026-W23-ai-digest.md
- [2026-06-17] **apply** | Model neutrality as architectural imperative | 1 updated (concepts/harness — model neutrality bullet); loopcraft source reference deferred pending loopcraft-agent-native proposal
- [2026-06-17] **apply** | OpenAI financial situation + AI subscription economics | 2 updated (state-of/models — AI economics snapshot section, trends/open-weight-momentum-broadens — fable-ban source added), 1 created (sources/newsletters/openai-economics-june-2026)
- [2026-06-17] **apply** | AI review skills | deleted by user before this apply step ran — omitted
- [2026-06-17] **apply** | Agents' Last Exam (ALE) benchmark | 1 created (benchmarks/agents-last-exam), 1 updated (trends/agents-reshape-organizations — ALE bullet + recent change)
- [2026-06-17] **apply** | Kimi Code + Kimi Work | 1 created (tools/kimi-code), 1 updated (state-of/coding — Kimi Code entry added)
- [2026-06-17] **apply** | 8 levels of AI adoption (Every/Mike Taylor) | 1 updated (training/company-wide-ai-enablement — AI adoption maturity model section + 5-step exec plan), 1 created (sources/newsletters/every-ai-adoption-levels)
- [2026-06-17] **apply** | Agent Labs vs Model Labs (Sarah Guo) | 1 created (concepts/agent-labs-vs-model-labs), 1 updated (trends/open-weight-momentum-broadens — Sarah Guo framing + 4-month lag + source)
- [2026-06-17] **apply** | Self-driving labs (Radical AI) | 2 updated (trends/ai-in-science — self-driving labs section, state-of/science — new subcategory + Radical AI entry), 1 created (sources/newsletters/self-driving-lab-radical-ai)
- [2026-06-17] **apply** | DiffusionGemma | 1 created (models/diffusiongemma), 1 updated (state-of/models — Architecture experiments section), 1 created (sources/newsletters/ainews-open-models-june-2026)
- [2026-06-17] **apply** | FrontierCode benchmark | 1 created (benchmarks/frontiercode), 1 updated (state-of/coding — FrontierCode ref added to Claude Code entry), 1 created (sources/newsletters/ainews-frontiercode-june-2026)
- [2026-06-17] **apply** | Claude Fable 5 launch details | 1 updated (models/claude-fable-5 — full benchmark record, pricing, usage posture), 1 updated (state-of/models — Fable 5 entry with specific scores), 2 created (sources/newsletters/ainews-fable5-june-2026, sources/articles/every-fable5-vibe-check)
- [2026-06-17] **triage** | Email Digest AI 2026-06-07 to 2026-06-12 (processed) | 9 proposals generated (fable-5-launch, frontiercode, diffusiongemma, self-driving-labs, agent-labs-vs-model-labs, ai-adoption-levels, kimi-code-work, agents-last-exam, ai-review-skills), 1 skipped (Mayo REDMOD); triage moved to applied/
- [2026-06-17] **triage** | Email Digest AI 2026-06-07 to 2026-06-12 | 9 signals generated (Fable 5 launch, FrontierCode benchmark, DiffusionGemma, self-driving labs, Agent Labs vs Model Labs, 8 levels of adoption, Kimi Code/Work, ALE benchmark, Mayo REDMOD); 4 sources skipped (promo, paywall, failed fetch, out-of-scope)
- [2026-06-17] **ingest** | "I Solved My Mystery Fatigue with AI" — Amy Deng | 1 page updated (state-of/healthcare — Patient-side AI section), 2 created (use-cases/ai-personal-health-investigation, sources/articles/2026-06-16-metalearn-mystery-fatigue-ai)
- [2026-06-24] **apply** | NVIDIA Cosmos 3 + Ideogram 4.0 | 4 pages updated (state-of/models — Image generation section + recent changes, state-of/creative — AI image generation subcategory + recent changes), 4 created (models/cosmos-3, models/ideogram-4, sources/newsletters/ainews-cosmos-nemotron-june-2026, sources/newsletters/ainews-ideogram-june-2026); index updated; proposal archived
- [2026-06-24] **apply** | Video agents as next frontier — Ethan He on Grok Imagine Agent | 1 page updated (state-of/creative — Grok Imagine Agent entry + recent change), 2 created (trends/video-agents-next-frontier, sources/newsletters/video-agents-ethan-he-june-2026); proposal archived
- [2026-06-24] **triage** | 2026-W23 AI Digest (Jun 1–7) | 14 proposals, 0 skipped (signal 13 "AI adoption levels" already handled in 2026-06-17 batch)
- [2026-07-06] **apply** | AI digest 2026-06-28 to 2026-07-02 approved proposals | Applied 11 proposals: Sonnet/Fable enrichment, Claude Science official details, software factories/FDE, autoresearch recipes, Codex/Claude Code general-work agents, local AI infrastructure, GPT-5.6 Sol restricted preview, agent-ready SaaS/MCP, Cursor iOS, PowerPoint skill failure mode, and explicit AI strategy bets; 26 existing pages updated, 11 source summaries created; proposals archived
- [2026-07-06] **triage** | Email Digest AI 2026-06-28 to 2026-07-02 | 11 proposals generated (Sonnet/Fable enrichment, Claude Science, software factories/FDE, autoresearch, Codex/Claude Code work agents, local AI infrastructure, GPT-5.6 Sol restricted preview, agent-ready SaaS/MCP, Cursor iOS, PowerPoint skill failure mode, AI strategy bets), 4 skipped unchecked; triage moved to applied/
- [2026-07-06] **apply** | LLM Wikis / PaperWiki | 1 page updated (concepts/knowledge-layer — LLM Wiki implementation pattern), 1 source created; proposal archived
- [2026-07-06] **apply** | RL harness quality | 1 page updated (concepts/harness — RL training-environment harness failure taxonomy), 1 source created; proposal archived
- [2026-07-06] **apply** | W23 approved proposals batch | Applied 11 approved proposals: new/updated model pages (Claude Opus 4.8, MiniMax M3, Nemotron 3 Ultra, MAI-Thinking-1), Axiom Math, SWE-Marathon, Harvey routing, Vending Bench evals, enterprise spend controls, GitHub scaling signal, Anthropic RSI; archived superseded Claude Opus 4.7 and MiniMax M2.7; left RL harness quality proposal pending for user feedback.
- [2026-07-06] **triage** | AI Email Digest 2026-07-02 to 2026-07-06 | 8 proposals, 7 skipped
- [2026-07-06] **apply** | Agent-readable web | 2 pages updated (state-of/computer-use, wiki/index), 1 created (concepts/agent-readable-web), 2 sources created
- [2026-07-06] **apply** | Anthropic model routing and Sonnet 5 | 3 pages updated (models/claude-fable-5, state-of/models, state-of/coding), 1 created (models/claude-sonnet-5), 2 sources created; subcategory renamed frontier-multimodal-model → frontier-model
- [2026-07-06] **apply** | Devin Security Swarm | 3 pages updated (tools/devin, state-of/cybersecurity, state-of/agents), 1 source created
- [2026-07-06] **apply** | Bridgewater / Thinking Machines domain finetuning | 2 pages updated (training/cost-aware-ai-task-routing, state-of/finance), 2 sources created; primary Thinking Machines source verified
- [2026-07-06] **apply** | Agent control layer and evals | 4 pages updated (workflows/agentic-orchestration-patterns, concepts/agent-evals, concepts/harness, state-of/agents), 1 created (tools/shepherd), 2 sources created
- [2026-07-06] **apply** | Open coding models, ZCode, and inference | 3 pages updated (models/glm-5-2, state-of/coding, trends/compute-infrastructure), 1 created (tools/zcode), 2 sources created
- [2026-07-06] **apply** | Claude Science dogfooding | 2 pages updated (state-of/science, trends/ai-in-science), 1 created (tools/claude-science), 2 sources created; primary Claude Science page fetched
- [2026-07-06] **apply** | Agent memory, skills, and Eve | 5 pages updated (concepts/knowledge-layer, training/agent-skill-methodology, state-of/agents, workflows/agentic-orchestration-patterns, wiki/index), 3 created (tools/openwiki, tools/impeccable, tools/eve), 3 sources created
- [2026-07-06] **apply** | Claude Code loops taxonomy | 2 pages updated (tools/claude-code, workflows/agentic-orchestration-patterns), 1 source created
- [2026-07-07] **triage** | AI Email Digest latest 20 unprocessed | 10 proposals, 6 skipped
- [2026-07-08] **apply** | Approved July 8 proposal batch | Applied 11 checked proposals: Claude Cowork web/mobile, Gemini managed agents, AI PR/code-review workflow, Meta Muse Image/Video, Cloudflare agent monetization, efficiencymaxxing, Fable unknowns routing, GLM-5.2 ecosystem signal, Gray Swan AI security, Kimi Goal Mode/creative agents, and AI delegation management; 20 existing wiki/index pages updated, 3 content pages created, 12 source summaries created; proposals archived
- [2026-07-08] **triage** | Email Digest AI latest 20 unprocessed as of 2026-07-08 | 11 proposals generated from checked signals; 3 unchecked signals skipped; triage moved to applied/
- [2026-07-08] **apply** | Approved July 7 proposal batch | 19 pages updated, 3 content pages created (models/gpt-5-6-sol, tools/claude-tag, concepts/model-internal-workspace), 9 sources created; loop source moved from tmp/ to raw/articles/
- [2026-07-08] **triage** | AI Email Digest latest 25 unprocessed | 7 proposals, 8 skipped
- [2026-07-08] **ingest** | Code review, remote execution, and harness effectiveness | 4 pages updated (workflows/ai-pr-code-review, training/evals-for-agentic-software-development, concepts/harness, concepts/agent-evals), 1 created (tools/crabbox), 3 source summaries created; wiki/index.md updated
- [2026-07-08] **ingest** | Compound engineering and cheap competence | 3 pages updated (training/ai-native-product-building, training/company-wide-ai-enablement, workflows/agentic-orchestration-patterns), 2 source summaries created
- [2026-07-08] **ingest** | ESMFold2 and protein world models | 2 pages updated (state-of/science, trends/ai-in-science), 1 source created; 1 history entry spilled (state-of/science, cap enforcement)
- [2026-07-08] **ingest** | GPT-Live | 3 pages updated (state-of/voice, trends/voice-becomes-agent-interface, wiki/index), 2 created (tools/gpt-live, source summary); source promoted from tmp/ to raw/articles/2026-07-07-openaicom-index-introducing-gpt-live.md
- [2026-07-08] **ingest** | Healthcare imaging infrastructure and AI-assisted triage | 2 pages updated (state-of/healthcare, wiki/index), 3 created (use-cases/ai-assisted-healthcare-triage, 2 source summaries)
- [2026-07-08] **ingest** | Open-weight adoption as access-risk mitigation | 2 pages updated (trends/open-weight-momentum-broadens, state-of/models), 1 source created
- [2026-07-08] **ingest** | Opus 4.8 benchmarks and Dynamic Workflows | 5 pages updated (models/claude-opus-4-8, state-of/models, tools/claude-code, tools/claude-design, workflows/agentic-orchestration-patterns), 3 sources created; state-of/models.md recent-changes cap enforced (4 entries spilled across this and the open-weight/outputmaxxing proposals combined)
- [2026-07-08] **ingest** | Outputmaxxing and compute utilization | 2 pages updated (trends/compute-infrastructure, state-of/models), 1 source created; standalone concepts/outputmaxxing page flagged as follow-up, not created (no draft existed in the proposal)
- [2026-07-14] **ingest** | Cognition/Devin batch — Agentic MapReduce, Windsurf Adaptive, Devin Fusion, productivity estimator | 9 pages updated (tools/devin, benchmarks/frontiercode, state-of/cybersecurity, workflows/agentic-orchestration-patterns, workflows/advisor-strategy, state-of/coding, concepts/agent-evals, training/ai-enablement-software-development, wiki/index), 6 created (tools/windsurf, 4 source summaries, 1 new history file); 2 recent-changes cap spills performed (agentic-orchestration-patterns: 3 entries total across this and the opus-48 proposal; state-of/coding: 5 entries, per proposal's own instructions)
- [2026-08-25] **triage** | Email Digest AI oldest 25 unprocessed as of 2026-08-25 | 13 proposals generated from 17 checked signals (Google I/O gap-fill, Cohere Command A+/China pricing, GPT-5.6 public launch, Anthropic agent infra/harness/MCP, AI cybersecurity Glasswing/GitHub breach, Cognition SWE-1.7, Grok 4.5 launch, agent R&D/science/memory benchmarks, agent-native compute infrastructure, Figma/Runway/Cartesia creative, OpenAI Erdős conjecture, After Automation essay, Tempo growth agent); 3 signals skipped (Andrej Karpathy joins Anthropic — left unchecked; cmux/muxy and ElevenLabs WhatsApp docs — checked but confirmed skip per thin/no-news content); triage moved to applied/
- [2026-09-05] **ingest** | Dan Shipper's "After Automation" (Every) | 2 pages updated (training/ai-work-delegation-modes, concepts/agent-evals), 1 source created
- [2026-09-05] **ingest** | Agent-native compute infrastructure becomes its own category | 2 pages updated (trends/compute-infrastructure, state-of/agents), 9 created (trends/agent-native-compute, tools/daytona, tools/modal, tools/railway, 5 source summaries), 1 schema addition (`agent-sandbox-infra` subcategory); state-of/agents.md recent-changes cap enforced (4 entries spilled to a new 2026-09-05 history block)
- [2026-09-05] **ingest** | New agent benchmarks: InferenceBench, Terminal-Bench Science, MINTEval | 2 pages updated (benchmarks/terminal-bench, concepts/agent-memory), 5 created (benchmarks/inferencebench, 2 paper source summaries, 1 article source summary, 1 newsletter source summary)
- [2026-09-05] **ingest** | AI cybersecurity cuts both ways — Glasswing's 10,000+ vulnerabilities and the GitHub breach | 2 pages updated (models/claude-mythos-preview, state-of/cybersecurity), 2 created (tweet source summaries)
- [2026-09-05] **ingest** | Anthropic agent infrastructure — sandboxes, MCP tunnels, Stainless acquisition, and the harness/agent-labs thesis | 5 pages updated (tools/claude-managed-agents, concepts/harness, concepts/mcp, concepts/agent-labs-vs-model-labs, workflows/agentic-orchestration-patterns), 8 source summaries created; 1 spill to workflows/agentic-orchestration-patterns history (appended to existing 2026-08-25 block); 1 source-page dedup (ainews-new-ai-infra-unicorns-2026-05-22, extended rather than duplicated)
- [2026-09-05] **ingest** | Cognition ships SWE-1.7, a budget frontier coding model for Devin | 2 pages updated (tools/devin, benchmarks/frontiercode), 1 source created
- [2026-09-05] **ingest** | Cohere Command A+ (fully open Apache 2.0) and Chinese frontier models close the price/capability gap | 1 page created (models/cohere-command-a-plus), 4 pages updated (models/deepseek-v4, models/qwen-3-7, state-of/models, trends/open-weight-momentum-broadens), 1 source page created, 2 dedup'd (extended ainews-erdos-benchmarks-cluster-2026-05-21 and ainews-all-model-labs-are-now-agent-labs rather than duplicated); 2 history spills (state-of/models, trends/open-weight-momentum-broadens — both new 2026-09-05 blocks); 1 schema addition (`cohere` tag)
- [2026-09-05] **ingest** | Figma's in-canvas design agent, Runway Aleph 2.0, and Cartesia Sonic-3.5's second #1 ranking | 2 pages updated (state-of/creative, tools/cartesia), 1 new history file created (state-of/creative, 2 entries spilled — page was pre-existing over the 10-entry cap); 3 source-page dedups (extended google-io-agents-agents-agents, ainews-new-ai-infra-unicorns-2026-05-22, and ainews-all-model-labs-are-now-agent-labs rather than duplicating)
- [2026-09-05] **ingest** | Google I/O 2026 — Gemini 3.5 Flash, Antigravity 2.0, Gemini Spark, Search AI-Mode | 2 pages updated (tools/gemini, state-of/models), 3 source summaries created; 1 spill to state-of/models history (new 2026-05-19 entry recorded directly in history since it was oldest-by-date, appended to the existing 2026-09-05 block)
- [2026-09-05] **ingest** | GPT-5.6 clears public launch after export-control restriction lifts | 2 pages updated (models/gpt-5-6-sol, trends/restricted-frontier-deployment), 2 source summaries created
- [2026-09-05] **ingest** | Grok 4.5 launches — xAI's (now SpaceXAI's) first model co-trained with Cursor | 1 page created (models/grok-4-5), 3 pages updated (state-of/models, tools/cursor, tools/grok-build), 2 source summaries created; 1 spill to state-of/models history (oldest entry [2026-05-29], appended to the existing 2026-09-05 block)
- [2026-09-05] **ingest** | OpenAI model disproves 80-year-old Erdős unit-distance conjecture | 2 pages updated (state-of/science, trends/ai-in-science), 1 source summary created; 1 spill to state-of/science history (new 2026-09-05 block, oldest entry [2026-04-22])
- [2026-09-05] **ingest** | Tempo's autonomous "AI head of growth" agent | 1 page updated (trends/agents-reshape-organizations); 1 source-page dedup (extended existing superhuman-autonomous-growth-agent-2026-05-21 rather than creating superhuman-tempo-growth-agent-2026-05, fixed its now-false "not actioned" scoping sentence)
- [2026-09-05] **ingest** | Maintenance M1 — truth fixes | 22 pages updated (state-of/models, state-of/cybersecurity, state-of/legal, trends/restricted-frontier-deployment, trends/open-weight-momentum-broadens, concepts/agent-labs-vs-model-labs, models/glm-5-2, concepts/harness, models/claude-opus-4-8, models/gpt-5-5, benchmarks/terminal-bench, benchmarks/swe-bench, tools/claude-code, tools/claude-managed-agents, tools/gpt-realtime-2, concepts/agent-evals, models/cosmos-3, tools/cartesia, training/ai-enablement-software-development, training/anti-autopilot-review-friction, tools/harvey, wiki/index), 1 created (models/composer-2-5), 1 archived (models/composer-2 -> history, superseded by Composer 2.5), 5 history files updated (state-of/models, state-of/cybersecurity, trends/open-weight-momentum-broadens, tools/claude-code, models/composer-2); resolves 17 wiki-internal contradictions surfaced by the 2026-09-05 maintenance pass; 3 findings (Grok 4.5 predecessor name, Opus 4.8 release date, Meta Spark vs Muse Spark) left as open questions with no draft
````

## Open questions

- **Claude Mythos Preview vs. "Mythos 5."** `wiki/state-of/models.md` says Claude Mythos Preview was "also suspended globally under US export controls (June 2026)," but `wiki/models/claude-mythos-preview.md` (a restricted-preview research model from Project Glasswing, as of 2026-05-23, described as "not publicly available... operates above the current Opus 4.7 tier") has no suspension entry. Meanwhile `wiki/models/claude-fable-5.md` describes a *different* model, "Mythos 5," as launching generally available on June 9 2026 alongside Fable 5, and states that "Claude Fable 5 and Mythos 5" (not "Mythos Preview") were the two suspended in June. It's not clear from what's in the wiki whether "Mythos Preview" and "Mythos 5" are the same model under two names (in which case the dashboard's suspension note is correct and the Preview page needs it added), or genuinely different releases (in which case the dashboard's suspension note may be misattributed to the wrong page). No draft is included for this until it's resolved — the earlier M1 proposal left two similarly-shaped naming questions open (Grok 4.20 vs. 4.3; Meta Spark vs. Muse Spark) for the same reason.
