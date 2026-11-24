---
type: proposal
source: raw/tweets/2026-10-26-dhravyashah-2103668051468300701.md
status: pending
created: 2026-10-26
---

# Proposal: Supermemory open-sources its company-brain harness

## Summary

### In short
A shared company agent is mostly a turn-taking problem, not a retrieval problem: Supermemory's open-sourced Slack harness spends its complexity on deciding when to speak, when to check first, when to stay silent and when to ask permission, and it keeps durable memory apart from live app state. The product itself was shut down on 10 September. The proposal rewrites the Supermemory example on Company brain, adds the turn-taking design to Multiplayer AI, a step-budget pattern to Agent loop design, a one-word status note to the knowledge-architectures hub, and one source page. Reason to hesitate: the hub is already past its length ceiling.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Dhravya Shah, founder of the memory startup Supermemory, published an X Article on 26 September 2026 (523K views). Two weeks earlier, on 10 September, Supermemory had discontinued its company-brain and personal-brain products, refunded customers, and said it would concentrate on its memory API for agents. Customers asked for the work to be released, so the harness is now open source on GitHub with a one-click Cloudflare deploy and the customer owning the data.

The article walks through the design, which runs on Cloudflare's Agents SDK. Each Slack message is filtered and then scored by a small triage model from 0 to 100 on usefulness, confidence, urgency, noise, interruption cost and similar factors. A deterministic evaluator turns those scores into one of four outcomes: answer, investigate, acknowledge with an emoji, or pass. An investigation that finds nothing ends silently rather than posting "I checked and found nothing".

When a teammate writes into a thread while the agent is working, a gate model decides whether to ignore the message, append it to the running turn, replace the request, or stop. Consequential actions suspend the turn behind an approve/deny card, and approval resumes the same reasoning loop with its context. Memory is split: durable company knowledge (decisions, ownership, project history) lives in Supermemory, scoped by channel, while live state such as issue status or the latest email is read from connected apps at answer time. Near the end of its step budget the agent is told how many steps remain, and on the last step its tools are removed so it has to answer. Shah frames the objective as value as a teammate: usefulness × correctness × timeliness, divided by noise × risk × interruption cost.

### What changes
The wiki lists Supermemory Company Brain as a live July product, with no word of the shutdown, and has no account of how a shared agent decides when to speak.

- **Company brain** rewrites the Supermemory bullet: the July launch facts stay; the shutdown, the open-source release, the durable-memory versus live-state split and channel-scoped memory are added. One Recent-changes entry dated 26 September; page date stays 2 October.
- **Multiplayer AI** gains one Current-status bullet on the triage scoring, the four outcomes and silent conclusions, the mid-task gate, and same-turn approval. Page date stays 10 October.
- **Agent loop design** gains a "step budget as an active control" pattern next to explicit stop criteria. Page date moves to 26 September.
- **Knowledge architectures** marks Supermemory Company Brain as discontinued with an open-source harness in the Company-brain row. Page date stays 19 October.
- One new source page for the article.

### What to weigh
The hub term map needs no new row: "company brain harness" is the existing Company brain row, and channel-scoped memory containers are the scoping step already on Agent memory. Even this four-word note grows a hub that is at 111% of its ceiling, under the 150% line where a split is required, so the split is offered below rather than drafted. The mechanics are spread across three pages instead of collected into a new tool page, because Supermemory no longer sells the product.

## Intended changes

- [ ] **Update** `wiki/concepts/company-brain.md` — replace the Supermemory Company Brain bullet; adds one Recent-changes entry dated 2026-09-26 (live list has 5, no spill); append one source id and one `## Sources` link; `as_of` stays 2026-10-02
    > See draft below

- [ ] **Update** `wiki/concepts/multiplayer-ai.md` — add one Current-status bullet; adds one Recent-changes entry dated 2026-09-26 (live list has 2, no spill); append one source id and link; `as_of` stays 2026-10-10
    > See draft below

- [ ] **Update** `wiki/workflows/agent-loop-design.md` — add one bullet after "Explicit stop criteria"; `as_of` moves to 2026-09-26; adds one Recent-changes entry dated 2026-09-26 (live list has 6, no spill); append one source id and link
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — annotate the Supermemory example in the Company brain row; adds one Recent-changes entry dated 2026-09-26 (live list has 7, no spill); append one source id and link; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Create** `wiki/sources/tweets/dhravyashah-company-brain-harness-open-source-2026-09-26.md` — source summary

## Page drafts

### wiki/concepts/company-brain.md (updated)

Frontmatter `sources:` (append one id; `as_of` unchanged):

```
sources: [lovable-future-of-saas-2026-08-26, cloudflare-os-launch-2026-09-07, femke-plantinga-company-brains-2026-08-27, cerebras-knowledge-base, dhravyashah-supermemory-company-brain-2026-07-28, latent-space-airbnb-inside-out-ai-2026-10-02, dhravyashah-company-brain-harness-open-source-2026-09-26]
```

Replace the `**Supermemory Company Brain (July 2026):**` bullet with:

```
- **Supermemory Company Brain (launched July 2026; discontinued 10 September, harness open-sourced 26 September):** a Slack bot built on Supermemory's [agent memory](agent-memory.md) tech that backfilled up to three months of channel history plus connected tools, answered sales/engineering/HR/research questions, tagged other bots to execute work, ran scheduled automations (e.g. a daily priority brief), and carried the same knowledge into Claude Code and Codex through a plugin. Supermemory shut the product down to concentrate on its memory API for agents, then released the harness as a one-click Cloudflare deployment where the customer owns the data. Its published design keeps durable company memory (decisions, ownership, project context, history) apart from live state read from connected apps at answer time (issue status, the latest email, deployments): a turn may use memory to work out what "the migration" refers to, then query Linear or GitHub for its current status, because storing live state in memory makes it stale and leaving history to live tools starves them of context. Memory is scoped by channel rather than by user: public channels share one organization container, each DM gets a per-user container, and each private channel or group DM gets its own. The turn-taking design (when to speak, investigate, or stay silent) is on [Multiplayer AI](multiplayer-ai.md).
```

`## Recent changes` — insert one entry between the 2026-10-02 and 2026-09-09 entries:

```
- [2026-09-26] Supermemory discontinued its Company Brain product (10 September) and open-sourced the harness: durable memory kept apart from live app state, memory scoped by channel; turn-taking design recorded on [Multiplayer AI](multiplayer-ai.md).
```

`## Sources` — append:

```
- [Dhravya Shah on X — We're open sourcing the company brain](../sources/tweets/dhravyashah-company-brain-harness-open-source-2026-09-26.md)
```

### wiki/concepts/multiplayer-ai.md (updated)

Frontmatter `sources:` (append one id; `as_of` unchanged):

```
sources: [multiplayer-ai-manifesto-2026-09-14, anthropic-human-agent-teams-2026-10, dhravyashah-company-brain-harness-open-source-2026-09-26]
```

`## Current status (as of 2026-10-10)` — append one bullet after the "A lab's own operating account" bullet:

```
- **An open-sourced multiplayer harness.** Supermemory released the Slack harness behind its discontinued [company brain](company-brain.md) (September 2026), built on Cloudflare's Agents SDK with one Durable Object per organization. It answers three questions the manifesto leaves open. *When to speak:* a small triage model scores each message 0–100 on usefulness, confidence, urgency, noise, interruption cost, investigation value, and reaction fit, and a deterministic evaluator turns the scores into answer, investigate, acknowledge with an emoji, or pass; an investigation that finds nothing ends silently instead of posting "I checked and found nothing", and an explicit @mention is never passed. *When a teammate speaks mid-task:* a gate model classifies each new message in an active thread as ignore, append (injected before the agent's next step), replace the request, or stop. *When an action needs consent:* the turn checkpoints and posts an approve/deny card, and approval resumes the same reasoning loop with its context, so the agent that proposed the action is the one that finishes it. Supermemory's stated objective is value as a teammate, roughly usefulness × correctness × timeliness over noise × risk × interruption cost, not answer quality alone.
```

`## Recent changes` — insert one entry between the 2026-10-10 and 2026-09-14 entries:

```
- [2026-09-26] Added Supermemory's open-sourced Slack harness: triage scores mapped to answer/investigate/acknowledge/pass with silent conclusions, a mid-task ignore/append/replace/stop gate, and approvals that resume the same turn.
```

`## Sources` — append:

```
- [Dhravya Shah on X — We're open sourcing the company brain](../sources/tweets/dhravyashah-company-brain-harness-open-source-2026-09-26.md)
```

### wiki/workflows/agent-loop-design.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-09-26
sources: [loopcraft-june-2026, aiewf-loops-debate-2026-07-03, claude-code-getting-started-with-loops-2026-06-30, what-the-hell-is-a-loop-anyway, andy-matuschak-agent-loop-tempo-2026-07, every-compound-engineering-upgrade-2026-05, aiewf-2026-five-trends-latentspace, dhravyashah-company-brain-harness-open-source-2026-09-26]
```

`## Loop design patterns` — insert directly after the "Explicit stop criteria" bullet:

```
- **Step budget as an active control.** Tell the agent how many steps remain as it nears its budget, and remove tool access on the final step so it must answer from what it already has instead of launching one more search and never replying. Supermemory's open-sourced Slack harness warns at three steps left and strips tools at the last one; it also runs one tool-free "salvage" pass when a turn ends with only progress text ("working on it") rather than an answer. *Source: Dhravya Shah (September 2026)*
```

`## Recent changes` — insert one entry between the 2026-10-19 and 2026-09-09 entries:

```
- [2026-09-26] Added the step-budget pattern (warn near the limit, remove tools on the final step, one tool-free salvage pass) from Supermemory's open-sourced company-brain harness.
```

`## Sources` — append:

```
- [Dhravya Shah on X — We're open sourcing the company brain](../sources/tweets/dhravyashah-company-brain-harness-open-source-2026-09-26.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter `sources:` (append one id; `as_of` unchanged):

```
sources: [knowledge-layer-architecture, llm-wikis-paperwiki-2026-07-06, agent-memory-systems-layer-2026-06, femke-plantinga-company-brains-2026-08-27, ontologies-agentic-systems-2026-07-30, dhravyashah-supermemory-company-brain-2026-07-28, posthog-semantic-layer-2026-08-21, deeplethe-utopia-2026-09-09, helixdb-helix-foundry-2026-10-19, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06, latent-space-airbnb-inside-out-ai-2026-10-02, dhravyashah-company-brain-harness-open-source-2026-09-26]
```

`## Canonical pages` table, Company brain row, "Examples tracked" cell — replace `Supermemory Company Brain` with:

```
Supermemory Company Brain (discontinued; harness open-sourced)
```

`## Recent changes` — insert one entry between the 2026-10-02 and 2026-09-09 entries:

```
- [2026-09-26] Marked Supermemory Company Brain as discontinued with its harness open-sourced; no term-map change ("company brain harness" is the Company brain row).
```

`## Sources` — append:

```
- [Dhravya Shah on X — We're open sourcing the company brain](../sources/tweets/dhravyashah-company-brain-harness-open-source-2026-09-26.md)
```

### wiki/sources/tweets/dhravyashah-company-brain-harness-open-source-2026-09-26.md (new)

```
---
title: 'Dhravya Shah on X — We''re open sourcing the company brain: how we designed the multi-player harness'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-dhravyashah-2103668051468300701.md
url: https://x.com/dhravyashah/status/2103668051468300701
published: 2026-09-26
ingested: 2026-10-26
domains: [agents]
---

# Dhravya Shah on X — We're open sourcing the company brain

X Article (523K views) by Supermemory founder Dhravya Shah, two weeks after Supermemory discontinued its company-brain and personal-brain products (10 September 2026) to focus on its memory API for agents. It open-sources the Slack harness (github.com/supermemoryai/company-brain, one-click Cloudflare deploy, customer-owned data) and walks through its design: one Cloudflare Agents SDK Durable Object per organization; message filtering, then a small triage model scoring usefulness, confidence, urgency, noise, interruption cost, investigation value and reaction fit (0–100), turned by a deterministic evaluator into answer, investigate, acknowledge (emoji) or pass; silent conclusions for investigations that find nothing; an active-turn gate (ignore, append, replace, stop) for new messages during a running turn; approval cards that suspend and resume the same turn; progressive tool disclosure; a step budget that strips tools on the final step; and memory split between durable company knowledge and live connected-app state, scoped by channel.

## Influenced pages
- [Company brain](../../concepts/company-brain.md) — Supermemory example rewritten: shutdown, open-source release, durable-vs-live memory split, channel-scoped containers
- [Multiplayer AI](../../concepts/multiplayer-ai.md) — turn-taking design: triage outcomes, silent conclusion, active-turn gate, same-turn approval
- [Agent loop design](../../workflows/agent-loop-design.md) — step budget as an active control, salvage pass
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — Company brain row example marked discontinued, harness open-sourced

## Key claims extracted
- Supermemory discontinued its company brain and personal brain products on 2026-09-10, refunding customers, to focus on its memory API for agents
- The company-brain harness is open source with a one-click Cloudflare deploy; customers own their data
- Built on Cloudflare Agents SDK; `CompanyBrainAgent` is a Durable Object keyed by organization ID with durable local SQL for turns, inboxes, approvals, and traces
- Proactivity moved from a yes/no decision to 0–100 scores from a small triage model plus a deterministic evaluator with four outcomes: answer, investigate, acknowledge, pass
- An explicit @mention that triage would pass is coerced to answer; parse errors fall back to answer
- Investigations that find nothing end in a "silent conclusion" with no Slack message
- New messages in an active thread go through a gate model: ignore, append, replace, or stop
- Consequential tools pass an approval classifier; approval suspends the turn with serializable state and resumes the same model loop
- Sandbox and scheduler tool families stay hidden until the model enables them (activeTools)
- Step budget: warning at limit − 3, tools removed at limit − 1; a tool-free salvage pass runs when only progress text exists
- Memory separates durable org knowledge from live connected-app state; containers are scoped per public-channel org, per DM user, and per private channel
- Stated objective: agent value = usefulness × correctness × timeliness / (noise × risk × interruption cost)
```

## Schema / vocabulary additions

None.

## Open questions

- The knowledge-architectures hub is at 111% of its concept ceiling and this proposal grows it slightly. Should it be split now (for example, moving the term map to its own page), or left in the warning band until it nears 150%?
