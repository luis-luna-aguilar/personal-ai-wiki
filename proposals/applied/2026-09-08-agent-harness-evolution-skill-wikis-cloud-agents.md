---
type: proposal
sources:
  - raw/newsletters/2026-08-28-ainews-openai-to-reach-agi-bar-by-end-2026.md
  - raw/newsletters/2026-08-29-ainews-openai-shuts-off-cursor.md
status: pending
created: 2026-09-08
---

# Proposal: Agent harness evolution — portable skill-wikis and cloud-resident agents

## Summary

### The source

Two consecutive AINews digests (2026-08-28, 2026-08-29) add fresh evidence for the wiki's ongoing thesis that agent improvement increasingly comes from the scaffolding around a model rather than the model itself. Google DeepMind researchers described separating raw agent execution traces, a persistent accumulated-knowledge "wiki," and executable skills distilled from it — with the wiki carrying much of the measured performance gain, and skills transferring across different model families, sometimes outperforming skills a model evolved for itself. Separately, a production team at T3 Code reported that fine-tuning `agents.md`/`claude.md` instruction files measurably improved pull-request quality, with the single biggest gain being better PR names and descriptions rather than the code itself. Google's Gemini team named new "AGY" harness patterns for iterative coding, document review, long formal proofs, and self-verification. Alongside these, several threads describe local CLI agents giving way to cloud-resident "persistent computer" agents with shared context and memory across sessions: Claude Code shipped `/resume` for desktop terminal-session continuity, Kimi Code added experimental Remote Control, OpenAI introduced "appshots" for richer app-context grounding, and Ollama began positioning a hosted GLM-5.3-Flash backend for harnesses like Claude, OpenCode, and Hermes. A smaller cluster of items — JIT-Agent (a harness the model synthesizes over memory/planning/tool-orchestration modules), finite-state-machine induction from agent traces, Anthropic's Claude Managed Agents + Vercel Chat SDK cookbook, Perplexity's new Agent API connectors, and Nous's Hermes Agent gaining real-Chrome-profile browsing — round out the same theme of harness-layer productization.

### What changes

`concepts/harness.md` already carries an August 2026 "model/harness co-evolution theory" section from the prior digest. This proposal adds a new section documenting the skill-wiki/instruction-fine-tuning evidence and the cloud-resident-agent shift, folds the smaller harness-productization items into the existing bulleted list, bumps `as_of` to 2026-08-29, and adds one Recent-changes entry — which, since the page's 10-entry cap is already full, spills its oldest entry (the 2026-06-22 Gray Swan item) to `wiki/history/concepts/harness.md`.

### What to weigh

CommerceAgentBench (Alibaba Accio's 107-task benchmark, checking what an agent actually changed/saved/submitted rather than what it claims) is included here as a supporting data point rather than given its own bullet or moved to `agent-evals.md`, since the triage signal grouped it with the harness-evolution cluster; a future proposal could split it out if the wiki wants a dedicated benchmark treatment. Otherwise, all claims here are relayed through AINews' own reporting/tweet-recap coverage rather than primary papers or vendor posts, consistent with how most of this page is already sourced.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/harness.md` — add skill-wiki/cloud-agent section, extend "What good harness engineering looks like" list, bump `as_of`, add Recent-changes entry, spill oldest entry
    > See draft below

- [ ] **Spill** `wiki/concepts/harness.md` → `wiki/history/concepts/harness.md` — oldest Recent-changes entry falls off the 10-entry cap
    > See draft below

Note: both source pages referenced here (`ainews-openai-agi-bar-2026-08-28.md`, `ainews-openai-shuts-off-cursor-2026-08-29.md`) are created by other proposals in this batch, which own them; this proposal only references their slugs.

## Page drafts

### wiki/concepts/harness.md (updated)

```md
---
as_of: 2026-08-29
sources: [..., ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29]
---

## What good harness engineering looks like

(... existing bullets unchanged ...)

- **JIT-Agent.** The model synthesizes its own harness over modules for memory, planning, action protocol, and tool orchestration at runtime, reporting gains over off-the-shelf agent scaffolds — a step further than a fixed harness the developer designs upfront.
- **FSM induction from agent traces.** Compact finite-state machines can be induced from recorded agent traces, suggesting an agent's behavioral "shape" is often determined more by the deployment scaffold than by the underlying model.
- **Real-session browsing as a harness capability.** Nous's Hermes Agent can now browse using a managed copy of the user's real Chrome profile and logins — a notable usability escalation for browser-use agents that also collapses auth friction, raising the importance of scoped-permission design at the harness layer.
- **Managed-agent cookbooks as harness distribution.** Anthropic published a cookbook connecting Claude Managed Agents to Vercel's Chat SDK, giving a unified chat layer with server-side harness, session management, and memory — packaging a harness pattern as a reusable recipe rather than bespoke integration work. Perplexity separately added Agent API connectors for GitHub, Slack, Google Drive, and Datadog.
- **Task-completion benchmarks as a harness-evaluation surface.** Alibaba Accio's open-sourced CommerceAgentBench (107 tasks spanning procurement, listings, operations, fulfillment, after-sales) checks what an agent actually changed, saved, or submitted rather than what it claims — the best observed run passed only 61.7% of tasks, underscoring how far current harnesses are from dependable business automation.

## Portable skill-wikis and cloud-resident agents (August 2026)

Google DeepMind researchers described a harness design that separates three layers: raw execution traces, a persistent accumulated-knowledge "wiki," and executable skills distilled from it. The key ablation result: the wiki itself carries much of the measured performance gain, and skills transfer across different model families — sometimes outperforming skills a model evolved for itself. This reinforces the wiki's existing point that portable skills and harness patterns are proving more durable than fine-tunes, since frontier open bases change too quickly for many fine-tunes to amortize.

A production data point in the same direction: a team at T3 Code reported that fine-tuning `agents.md`/`claude.md` instruction files measurably improved pull-request quality, with the largest gain coming from better PR names and descriptions rather than the underlying code generation — evidence that the instruction layer, not just tools or model choice, is a real harness-quality lever. Google's Gemini team separately named new "AGY" harness patterns for iterative coding, document review, long formal proofs, and self-verification.

In parallel, several practitioners describe local CLI agents giving way to cloud-resident "persistent computer" agents with shared context and memory across sessions: Claude Code shipped `/resume` for desktop terminal-session continuity, Kimi Code added experimental Remote Control, OpenAI introduced "appshots" for richer app-context grounding, and Ollama began positioning a hosted GLM-5.3-Flash backend as a private cloud harness endpoint for Claude, OpenCode, and Hermes.

## Recent changes

- [2026-08-29] Added Google's skill-wiki ablation result (wiki carries most of the gain; skills transfer cross-model-family), T3 Code's agents.md/claude.md fine-tuning result, Google's AGY harness patterns, and the cloud-resident-agent shift (Claude Code `/resume`, Kimi Code Remote Control, OpenAI appshots, Ollama-hosted GLM-5.3-Flash backend); also added JIT-Agent, FSM trace induction, Hermes Agent's real-Chrome-profile browsing, Claude Managed Agents + Vercel Chat SDK cookbook, and CommerceAgentBench.
- (... existing entries follow, oldest entry spilled below ...)
```

### wiki/history/concepts/harness.md (updated)

```md
## Archived from current page on 2026-09-08

- [2026-06-22] Gray Swan security coverage adds prompt injection, exfiltration, identity, permissions, and automated red teaming as harness-boundary concerns for tool-using agents.
```
