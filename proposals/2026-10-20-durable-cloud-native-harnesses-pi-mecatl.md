---
type: proposal
source: raw/newsletters/2026-10-07-can-a-cloud-native-harness-make-agents-reliable-be.md
sources:
  - raw/newsletters/2026-10-07-can-a-cloud-native-harness-make-agents-reliable-be.md
  - raw/newsletters/2026-10-02-ainews-pi-10-pi-durable-and-aie-nyc.md
  - raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
  - raw/newsletters/2026-10-02-academia-is-for-ambition-alex-zhang-mit.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Durable, cloud-native harnesses (Pi 1.0, Pi Durable, Stacklok Mecatl)

## Summary

### In short
The agent harness is being pulled apart so it can run as server infrastructure: Pi Durable records every step as a checkpointed task so agents resume after a crash, and Stacklok's Mecatl keeps the agent loop separate from the model provider, state store and execution environment so enterprises can govern sessions centrally. The proposal creates a `tools/pi.md` page (Pi is already cited on six pages with nothing to link to), adds a durable-harness section to Agent runtime platforms, a harness-swap data point and a dissenting view to Harness vs model, and lists Pi on State of Agents. Reason to hesitate: one new tool page.

[[#Open questions|Open questions: 1 to answer.]]

### The source
On 2 October 2026 AINews led with Pi, the open-source minimal coding harness (now part of the company Earendil), shipping version 1.0 and a sibling called Pi Durable. Pi 1.0 adds a "code mode" with native MCP, Jev and image-model support, deferred tool loading, prompt-cache warming for Anthropic models, and system messages that can change mid-conversation. Pi Durable is a rewrite of Pi in about 15,000 lines of TypeScript around a small task-based workflow engine. Every step is a checkpoint, so agents and subagents pick up where they stopped after a crash. Storage is pluggable (memory, SQLite, JSONL), it runs on Bun or Cloudflare Durable Objects, one harness can hold several parallel conversation branches, app state sits next to the transcript so several people or UIs can watch and steer one agent. The 6 October issue adds that control is separated from execution and that the authors skipped the Effect.ts library because it offers no durability.

On 7 October Latent Space interviewed Kubernetes co-creators Craig McLuckie and Joe Beda about Stacklok's open-source Mecatl, a "cloud-native harness" started in June. Their argument: desktop-first harnesses run the loop, tool execution and session state in one process, and simply moving that process into a VM or sandbox breaks the agent's lifecycle, for example pausing it safely while it waits for a person. Mecatl keeps the loop apart from the client, model provider, state store and execution environment, so sessions and memory live in managed systems rather than JSONL files on disk. Beda expects companies to govern agent conversations the way they govern email. Mecatl sits beside ToolHive (MCP server management) and an AI gateway for access, budgets and provider routing.

The same 6 October issue reports a Hugging Face proxy that turns ten unmodified harnesses into RL training environments: the same weights scored 62% under Mini-SWE-Agent and 33% under Claude Code (one task family, one seed). And on a 2 October podcast MIT's Alex Zhang argued that Claude Code, Codex and Pi are structurally the same loop, so for a strong model the differences mostly come down to cost.

### What changes
Today Pi appears only in passing, as the base of Flue and Prime Agent and as the cheapest harness in two cost comparisons, and the runtime page has no durable-execution or cloud-native harness entry.

- New page `tools/pi.md`: Pi 1.0, Pi Durable, and the existing cost evidence, dated 6 October.
- **Agent runtime platforms** gains a Current-status bullet and a "Durable and cloud-native harnesses" section (Pi Durable, Mecatl, Stacklok's governance stack). Page date moves to 7 October.
- **Harness vs model** gains one paragraph with the Hugging Face result and Zhang's dissent. Page date moves to 6 October.
- **State of Agents** adds Pi under Agent frameworks; its Recent changes spill the oldest entry to history.
- **Flue** links its Pi mention to the new page.
- Four source pages.

### What to weigh
Whether Pi earns a tool page or should stay a mention; the case for one is that six pages already cite it. Mecatl gets no page, since one interview is thin. The runtime page ends near 1,250 body words, about 104% of its ceiling, inside the warning band. Pi 1.0's own release post was not fetched; its features come from AINews.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/tools/pi.md` — new tool page (subcategory `agent-framework`)
    > See draft below

- [ ] **Update** `wiki/concepts/agent-runtime-platforms.md` — add one Current-status bullet; insert a new `## Durable and cloud-native harnesses` section after `## Execution runtimes`; Current-status stamp and `as_of` move to 2026-10-07; adds one Recent-changes entry dated 2026-10-07 (live list has 3, no spill); append three source ids and links
    > See draft below

- [ ] **Update** `wiki/concepts/harness-vs-model.md` — add one paragraph at the end of the Current-status prose (before the vocabulary paragraph); Current-status stamp and `as_of` move to 2026-10-06; adds one Recent-changes entry dated 2026-10-06 (live list has 5, no spill); append two source ids and links
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — add a Pi line under `### Agent frameworks`; adds one Recent-changes entry dated 2026-10-06 (live list has 10, so the oldest entry spills); append source id; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — the oldest Recent-changes entry at apply time (currently `[2026-07-08] Claude Cowork beta expands to web/mobile…`)
    > See draft below

- [ ] **Update** `wiki/tools/flue.md` — link the Pi mention in Current status to the new page (no date change, no Recent-changes entry)
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-pi-10-pi-durable-2026-10-02.md` — story-specific source page

- [ ] **Create** `wiki/sources/newsletters/ainews-pi-durable-harness-rl-2026-10-06.md` — story-specific source page (Pi Durable design note, Hugging Face multi-harness RL proxy)

- [ ] **Create** `wiki/sources/newsletters/latent-space-stacklok-mecatl-2026-10-07.md` — source page

- [ ] **Create** `wiki/sources/newsletters/latent-space-alex-zhang-rlm-2026-10-02.md` — source page (harness section only)

## Page drafts

### wiki/tools/pi.md (new)

```
---
title: Pi
type: tool
domains: [agents]
subcategory: agent-framework
tags: [agentic]
as_of: 2026-10-06
sources: [ainews-pi-10-pi-durable-2026-10-02, ainews-pi-durable-harness-rl-2026-10-06, latent-space-alex-zhang-rlm-2026-10-02, databricks-benchmarking-coding-agents-2026-07, anthropic-riemann-hypothesis-2026-08-11, flue-2-react-for-agents-2026-08-15, primeintellect-prime-agent-2026-08-05]
---

# Pi

Pi is an open-source minimal coding-agent harness, now developed under the company Earendil. It is the unopinionated base layer other projects build on ([Flue](flue.md), Prime Intellect's Prime Agent), and it keeps turning up as the cheapest harness in cost comparisons. Pi Durable is a sibling rewrite that turns the same loop into a crash-proof server process.

## Current status (as of 2026-10-06)

- **Pi 1.0 (October 2026):** "code mode" with native support for MCP, Jev and image models; extension support for virtual models; deferred tool loading; prompt-cache warming for Anthropic models; mid-conversation system messages that change prompts and tools based on the transcript; full-screen TUI by default.
- **Pi Durable:** a ~15K-line TypeScript port built on a small task-based workflow engine. Every step is a checkpointed task, so agents and subagents resume from their last state after a crash or restart. Pluggable storage (memory, SQLite, JSONL); runs on Node, Bun or Cloudflare Durable Objects; control is separated from local or remote execution environments.
- Pi Durable also runs parallel branching conversations in one harness, stores app state (such as a to-do list) beside the transcript so several users or UIs can watch and steer one agent, compacts old messages in the background, and hot-swaps tool and extension code mid-run. The authors skipped Effect.ts because it does not provide durability.
- **Cost evidence:** Databricks found the same model at the same effort cost more than 2x as much through Claude Code or Codex as through Pi, because Pi sent about 3x less context per turn; Composio found Pi the cheapest and best-performing of four harnesses running DeepSeek V4 Flash (both mid-2026).

## Why it matters

Pi is the reference point for the "thin harness" position: MIT's Alex Zhang uses it as his baseline because "all other harnesses are basically just Pi". Pi Durable is the clearest open-source example of the split described on [Agent runtime platforms](../concepts/agent-runtime-platforms.md), where the loop, its state and its execution environment become separately managed parts.

## Recent changes

- [2026-10-06] Pi Durable design details: ~15K lines of TypeScript, SQLite/JSONL storage, Bun or Cloudflare Durable Objects, control separated from execution.
- [2026-10-02] Pi 1.0 released (code mode, deferred tool loading, cache warming, mid-conversation system messages) alongside Pi Durable.

## Related

- [Flue](flue.md) — agent framework built on Pi
- [Harness vs model](../concepts/harness-vs-model.md) — the harness-swap measurements Pi appears in
- [Agent runtime platforms](../concepts/agent-runtime-platforms.md) — durable and cloud-native harnesses

## Sources

- [AINews — Pi 1.0 and Pi Durable](../sources/newsletters/ainews-pi-10-pi-durable-2026-10-02.md)
- [AINews — Pi Durable design and multi-harness RL](../sources/newsletters/ainews-pi-durable-harness-rl-2026-10-06.md)
- [Latent Space — Alex Zhang, MIT (RLMs and harnesses)](../sources/newsletters/latent-space-alex-zhang-rlm-2026-10-02.md)
- [Databricks — Benchmarking coding agents](../sources/articles/databricks-benchmarking-coding-agents-2026-07.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement (Composio harness bake-off)](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
- [Flue 2 — React for agents](../sources/newsletters/flue-2-react-for-agents-2026-08-15.md)
- [Prime Intellect — Prime Agent](../sources/tweets/primeintellect-prime-agent-2026-08-05.md)
```

### wiki/concepts/agent-runtime-platforms.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-07
sources: [thecode-april-22-2026, ainews-2026-04-22, shopify-claude-code-bessemer-2026-05, ainews-death-of-params-glm-53-2026-08-20, ainews-poolside-nvidia-2026-08-21, ainews-andrew-ng-ai-engineering-2026-08-25, gemini-managed-agents-2026-07, claude-managed-agents-updates-2026-05, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29, cloudflare-computer-launch-2026-09-07, skills-and-plugin-packaging-late-march, openai-agents-sdk-evolution, agent-infrastructure-harness-2026-05-01, ainews-navier-stokes-2026-09-09, claude-tag-slack-agent-2026-06, ainews-fal-h3-max-live-2026-09-01, ainews-pi-10-pi-durable-2026-10-02, ainews-pi-durable-harness-rl-2026-10-06, latent-space-stacklok-mecatl-2026-10-07]
```

`## Current status` heading and one new bullet appended at the end of its list:

```
## Current status (as of 2026-10-07)

- Open-source harnesses are being rebuilt to run as server infrastructure: the agent loop is split from its state and its execution environment so sessions survive crashes and can be governed centrally ([Pi](../tools/pi.md) Durable, Stacklok's Mecatl).
```

New section inserted between `## Execution runtimes` and `## Fleet management and governance`:

```
## Durable and cloud-native harnesses

- **Checkpoint every step.** [Pi](../tools/pi.md) Durable rebuilds a minimal coding harness around a small task-based workflow engine: each step is a checkpointed task, so agents and subagents resume from their exact state after a crash. Storage is pluggable (memory, SQLite, JSONL), the same code runs on Bun or Cloudflare Durable Objects, and app state stored beside the transcript lets several people or UIs watch and steer one agent.
- **Separate the loop from everything it touches.** Stacklok's open-source Mecatl, from Kubernetes co-creators Craig McLuckie and Joe Beda, keeps the agent loop independent of the client, model provider, state store, and execution environment. Their argument is that desktop-first harnesses run loop, tools, and session state in one process, so "lift and shift" into a VM or sandbox breaks lifecycle tasks such as pausing an agent safely while it waits for a person. Session state and memory move from JSONL files on disk into managed systems, and agent conversations become company records governed like email. This is the open-source counterpart of the OpenAI Agents SDK's harness/compute split above.
- **The surrounding control plane.** Stacklok pairs Mecatl with ToolHive (running and governing MCP servers on Kubernetes) and an AI gateway for access control, budgets, reporting, and provider routing. The gateway deliberately does not pick models per task; McLuckie wants that choice made inside the harness, which has more context.
```

`## Recent changes` — insert one entry directly below the two 2026-10-19 entries:

```
- [2026-10-07] Added a "Durable and cloud-native harnesses" section: Pi Durable's checkpointed workflow engine and Stacklok's Mecatl (loop separated from client, model, state, and execution), plus Stacklok's ToolHive and AI-gateway control plane.
```

`## Sources` — append:

```
- [AINews — Pi 1.0 and Pi Durable](../sources/newsletters/ainews-pi-10-pi-durable-2026-10-02.md)
- [AINews — Pi Durable design and multi-harness RL](../sources/newsletters/ainews-pi-durable-harness-rl-2026-10-06.md)
- [Latent Space — Can a cloud-native harness make agents reliable beyond the desktop? (Stacklok)](../sources/newsletters/latent-space-stacklok-mecatl-2026-10-07.md)
```

### wiki/concepts/harness-vs-model.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-06
sources: [langchain-better-harness, latent-space-agent-harness-evolution-2026-08-22, anthropic-riemann-hypothesis-2026-08-11, ainews-openai-agi-bar-2026-08-28, ainews-muse-spark-13-2026-09-03, ainews-navier-stokes-2026-09-09, model-harness-fit-2026-05-13, ainews-pi-durable-harness-rl-2026-10-06, latent-space-alex-zhang-rlm-2026-10-02]
```

Heading change: `## Current status (as of 2026-09-09)` → `## Current status (as of 2026-10-06)`.

New paragraph, inserted after the train → absorb → shed paragraph and before the vocabulary paragraph:

```
October 2026 adds a fresh measurement and a dissent. Hugging Face built a capture proxy that speaks the OpenAI, Anthropic, and Gemini API formats, so ten unmodified harnesses can serve as RL training environments; the same weights scored 62% under Mini-SWE-Agent and 33% under Claude Code, and training a small model (LFM2.5-2.6B) across four harnesses lifted first-attempt solves from 42% to 54% (one task family, one seed). MIT's Alex Zhang, author of the recursive-language-model (RLM) work, argues the other side: Claude Code, Codex, and [Pi](../tools/pi.md) are structurally the same "trajectory as a prompt" loop, where the whole rollout stays in the main model's context, so for a strong enough model the differences between them come down mostly to cost. Real gains, in his view, need a different class of harness (such as RLMs, where code is the only tool and the model calls itself as a subagent) and models post-trained for it.
```

`## Recent changes` — insert one entry directly below the two 2026-10-19 entries:

```
- [2026-10-06] Added Hugging Face's multi-harness RL proxy (same weights 62% vs 33% across harnesses; 42%→54% from training across four) and Alex Zhang's view that mainstream coding harnesses are structurally the same loop.
```

`## Sources` — append:

```
- [AINews — Pi Durable design and multi-harness RL](../sources/newsletters/ainews-pi-durable-harness-rl-2026-10-06.md)
- [Latent Space — Alex Zhang, MIT (RLMs and harnesses)](../sources/newsletters/latent-space-alex-zhang-rlm-2026-10-02.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter `sources:` — append `ainews-pi-10-pi-durable-2026-10-02` to the end of the live list (`as_of` unchanged).

`### Agent frameworks` — append after the Harness² line:

```
- [Pi](../tools/pi.md) — Earendil; open-source minimal coding harness that Flue and Prime Agent build on; Pi 1.0 plus Pi Durable, a checkpointed rewrite that resumes after crashes *(as of 2026-10-06)*
```

`## Recent changes` — insert one entry between the 2026-10-09 and 2026-09-09 entries (list goes to 11, so the oldest entry spills):

```
- [2026-10-06] Added [Pi](../tools/pi.md) to Agent frameworks: Pi 1.0 and Pi Durable (checkpointed, crash-resuming harness on Bun or Cloudflare Durable Objects).
```

Remove from `## Recent changes` (spilled, see below):

```
- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

### wiki/history/state-of/agents.md (updated)

Append under the `## Archived from current page on <apply date>` block (open a new block if none exists for the apply date):

```
- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

### wiki/tools/flue.md (updated)

`## Current status` — second bullet, link added:

```
- Built on top of [Pi](pi.md), an open-source minimal harness — Schott treats Pi's role as analogous to Vite underneath Astro: a foundational, unopinionated layer Flue adds developer-facing opinions on top of.
```

### wiki/sources/newsletters/ainews-pi-10-pi-durable-2026-10-02.md (new)

```
---
title: AINews — Pi 1.0 and Pi Durable
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-02-ainews-pi-10-pi-durable-and-aie-nyc.md
published: 2026-10-02
ingested: 2026-10-20
domains: [agents, coding]
---

# AINews — Pi 1.0 and Pi Durable

The lead story of the 2 October 2026 AINews issue: Earendil, which the Pi harness joined, shipped Pi 1.0 and Pi Durable, both reaching the Hacker News front page. The issue lists Pi 1.0's features and describes Pi Durable as a TypeScript port that externalizes all of Pi's stateful components.

## Influenced pages

- [Pi](../../tools/pi.md) — new page
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — durable-harness section
- [State of Agents](../../state-of/agents.md) — Pi added under Agent frameworks

## Key claims extracted

- Pi 1.0: code mode (native MCP, Jev, image models), extension support for virtual models, deferred tool loading, cache warming for Anthropic models, mid-conversation system messages, new TUI theme, full-screen by default
- Pi Durable: every step recorded as a checkpointed task; agents and subagents resume from their last exact state after a failure or restart
- Runs on any JavaScript runtime (Node, Bun, Cloudflare); pluggable storage (memory, SQLite, JSONL); local or remote execution environments
- Parallel branching conversations in one harness; installable Extensions bundling prompts, tools, hooks, and durable tasks
- Background compaction; app state stored beside transcripts for multiplayer steering; hot-swapping tool and extension code mid-run
```

### wiki/sources/newsletters/ainews-pi-durable-harness-rl-2026-10-06.md (new)

```
---
title: AINews — Pi Durable design and multi-harness RL
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
published: 2026-10-06
ingested: 2026-10-20
domains: [agents]
---

# AINews — Pi Durable design and multi-harness RL

Two items from the "Agent Harnesses, RL Environments and Developer Tooling" section of the 6 October 2026 AINews issue: a design note on Pi Durable, and Hugging Face's proxy that turns unmodified coding harnesses into RL environments.

## Influenced pages

- [Pi](../../tools/pi.md) — Pi Durable design details
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — durable-harness section
- [Harness vs model](../../concepts/harness-vs-model.md) — same-weights harness swap and multi-harness training result

## Key claims extracted

- Pi Durable is built around a small task-based workflow engine so long-running, multiplayer agents can suspend and resume anywhere
- Core is ~15K lines of TypeScript with SQLite/JSONL storage; runs on Bun or Cloudflare Durable Objects; control separated from execution environments
- The authors skipped Effect.ts because it does not provide durability
- Hugging Face capture proxy speaks OpenAI Chat, OpenAI Responses, Anthropic, and Gemini formats, forwards to vLLM, records token IDs and logprobs for TRL; 10 unmodified harnesses become RL environments
- Same weights: 62% under Mini-SWE-Agent, 33% under Claude Code
- Training LFM2.5-2.6B across 4 harnesses lifts first-attempt solves from 42% to 54%; a tool-call bonus cuts calls by 31%; SFT on 3,189 rollouts plateaus at 47.5%
- Caveat in the source: one task family, one seed
```

### wiki/sources/newsletters/latent-space-stacklok-mecatl-2026-10-07.md (new)

```
---
title: Latent Space — Can a cloud-native harness make agents reliable beyond the desktop? (Stacklok)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-07-can-a-cloud-native-harness-make-agents-reliable-be.md
url: https://www.latent.space/p/stacklok
published: 2026-10-07
ingested: 2026-10-20
domains: [agents]
---

# Latent Space — Can a cloud-native harness make agents reliable beyond the desktop? (Stacklok)

Latent Space interview with Kubernetes co-creators Craig McLuckie and Joe Beda about Stacklok, which pivoted from software supply-chain security to Kubernetes-based agent infrastructure. Its main product is Mecatl, an open-source "cloud-native harness" (started June 2026) that separates the agent loop from client, model provider, state store, and execution environment so enterprises can run and govern agents centrally, the way Kubernetes did for containers.

## Influenced pages

- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — Mecatl and the Stacklok control plane in the durable-harness section

## Key claims extracted

- Desktop-first harnesses run the loop, local execution, and session state in one process or tightly coupled processes, even when pluggable
- "Lift and shift" into VMs, containers, or sandboxes causes problems with agent lifecycle and with quiescing (safely pausing while waiting for human input)
- Mecatl keeps the agent loop independent of client, model provider, state store, and execution environment; session management and memory move out of JSONL files on disk into manageable systems
- Beda: enterprise agent interactions belong to the enterprise and will be managed and governed like email
- Goal includes reducing enterprise dependency on frontier-lab harnesses (Codex, Claude Code, GitHub Copilot)
- ToolHive: open-source platform for running and governing MCP servers, now with a Kubernetes gateway, registry, and operator
- AI Gateway (not yet open source): access control, budgets, reporting, provider routing; no semantic per-task model routing, which McLuckie prefers inside the harness
- Customers are mostly regulated industries (banks, semiconductor companies, telcos); the commercial product is the "enterprise spine" control plane for identity, authorization, policy, and auditing
```

### wiki/sources/newsletters/latent-space-alex-zhang-rlm-2026-10-02.md (new)

```
---
title: Latent Space — Academia is for Ambition (Alex Zhang, MIT)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-02-academia-is-for-ambition-alex-zhang-mit.md
url: https://www.latent.space/p/rlm
published: 2026-10-02
ingested: 2026-10-20
domains: [agents]
---

# Latent Space — Academia is for Ambition (Alex Zhang, MIT)

Long podcast transcript with MIT PhD student Alex Zhang, author of the Recursive Language Models (RLM) work, covering GPU kernels, research taste, RLMs, Prime Agent, and harness design. Only the harness section ("Why Claude Code, Codex, and Pi are so similar", "Harnesses as compositional generalizers") was used for this ingest.

## Influenced pages

- [Harness vs model](../../concepts/harness-vs-model.md) — the "all mainstream harnesses are the same loop" dissent
- [Pi](../../tools/pi.md) — Pi as the reference harness

## Key claims extracted

- Claude Code, Codex, Pi, Oh My Pi, and Prime Agent make mostly the same design choices; Zhang uses Pi as the reference because "all other harnesses are basically just Pi"
- He calls this harness class "trajectory as a prompt": the whole rollout stays in the main model's context, even with subagents
- As models improve, putting a strong model in another mainstream harness mostly changes cost, not outcome
- Frontier labs likely train only in their own harnesses; open models need to be trained in a harness to use it well
- An RLM is a harness whose only tool is code; the model can call itself as a subagent, and other tools are functions in code
- Harnesses can act as compositional generalizers: a strategy learned on short tasks transferred to tasks 8–30x longer
- Prime Agent is Pi restricted to IPython as the only tool, plus a continual-harness mechanism
```

## Open questions

- Should Stacklok's Mecatl get its own `tools/` page now, or wait for a second source (assumed: wait; it lives on Agent runtime platforms for now)?
