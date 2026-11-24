---
type: proposal
source: raw/articles/2026-11-24-perplexityai-hub-blog-perplexity-computer-now-runs-fully-local-on-mac.md
sources:
  - raw/articles/2026-11-24-perplexityai-hub-blog-perplexity-computer-now-runs-fully-local-on-mac.md
  - raw/tweets/2026-11-24-xcom-perplexity-ai-2112571597798461920.md
  - raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
status: pending
created: 2026-11-24
---

# Proposal: Perplexity Computer runs fully local on Apple-silicon Macs

## Summary

### In short
A consumer computer-use agent can now keep the whole task on the user's own machine: since 20 October, Perplexity Computer runs its model, harness and execution entirely on supported Apple-silicon Macs, works across local files and Mac apps, and spends no cloud credits on local tasks. It is open to Pro, Max and Enterprise subscribers, not only the $200 Max tier the wiki records. The proposal updates **Perplexity Computer** and its leader line on **State of Computer Use**, and creates one source page. No red flags, apart from one detail the two Perplexity sources describe differently: which Qwen model sits under PPLX Pro.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 20 October 2026 Perplexity announced on its blog and on X that Computer, its multi-model background agent, can run fully local on a Mac. In this mode the AI model, the harness that drives it and the task execution all stay on the device. With the user's permission, Computer works across local files and Mac apps such as Notes, Messages, Mail and Numbers, without sending personal data to the cloud. Perplexity's examples are a portfolio review against private holdings, a client proposal built from confidential notes and a rate sheet, and a morning priorities list drawn from Messages and Mail.

The local models are Qwen 3.6 or PPLX Pro, Perplexity's post-trained version of Qwen; the launch thread on X names the base as Qwen 3.8. Local tasks consume no Computer credits. The feature is available to Pro, Max and Enterprise subscribers on supported Apple-silicon Macs, with 36 GB of unified memory or more recommended. It extends two earlier steps: Personal Computer for Mac in May, and Hybrid Compute in September, which starts a task in the cloud and hands private-file work to a local model. Even in local mode, the user can allow Computer to escalate to the cloud for current information, browser use and connected apps, so privacy depends on that setting. Code and tool execution run in isolated sandboxes in both the local and cloud versions. AINews carried the launch on 21 October and added that local mode works offline.

### What changes
The wiki describes Perplexity Computer as of late August: a Max-only cloud orchestration agent with a dedicated Mac mini "Personal Computer" variant.

- **Perplexity Computer** gains a Current-status bullet on fully local mode and Hybrid Compute; the Max-only line is scoped to cloud Computer, and one strength and one caveat are reworded to match. It gains a Recent-changes entry, and the page date moves from 29 August to 20 October.
- **State of Computer Use** has the Perplexity leader line rewritten to mention local execution, its date moved from 10 April to 20 October, and a Recent-changes entry; the oldest entry (5 May, the knowledge-work OS framing) moves to history because the list is at its cap. Page date stays 24 November.
- One new source page for the blog post.

### What to weigh
The blog says PPLX Pro is "a post-trained version of Qwen" and also offers Qwen 3.6, while the X thread says PPLX Pro is post-trained Qwen 3.8. The drafts give both, attributed. "Offline" comes from AINews, not from Perplexity's own wording, so the drafts say "on-device" and leave offline as AINews' claim.

## Intended changes

- [ ] **Update** `wiki/tools/perplexity-computer.md` — scope the Max bullet to cloud Computer; add one Current-status bullet; reword one Strength and one caveat; adds one Recent-changes entry dated 2026-10-20 (list goes to 5, no spill); append `perplexity-computer-local-mac-2026-10-20` to frontmatter `sources:` and one line to `## Sources`; `as_of` and Current-status stamp 2026-08-29 → 2026-10-20
    > See draft below

- [ ] **Update** `wiki/state-of/computer-use.md` — rewrite the Perplexity Computer leader line; adds one Recent-changes entry dated 2026-10-20 (list is at 10 of 10, so the oldest entry spills); append source id to frontmatter `sources:` and one line to `## Sources`; `as_of` stays 2026-11-24
    > **Before:** `- [Perplexity Computer](../tools/perplexity-computer.md) — Perplexity's persistent digital-proxy model: always-on dedicated Mac mini environment, remotely controllable from any device, 19-model orchestration, 400+ app and 12,000+ financial-institution connectivity *(as of 2026-04-10)*`
    > **After:** see draft below

- [ ] **Spill** `wiki/state-of/computer-use.md` → `wiki/history/state-of/computer-use.md` — the oldest Recent-changes entry (2026-05-05, knowledge-work OS framing; the Gemini downloadable-files entry already spilled today) moves to history

- [ ] **Create** `wiki/sources/articles/perplexity-computer-local-mac-2026-10-20.md` — source summary

## Page drafts

### wiki/tools/perplexity-computer.md (updated)

Frontmatter changes:

```
as_of: 2026-10-20
sources:
  - perplexity-computer-plaid
  - perplexity-personal-computer
  - finance-agent-workflows-2026-05-06
  - ainews-openai-shuts-off-cursor-2026-08-29
  - perplexity-computer-local-mac-2026-10-20
```

Heading change: `## Current status (as of 2026-08-29)` → `## Current status (as of 2026-10-20)`

First Current-status bullet, replaced:

```
- Cloud Computer is available on Perplexity Max ($200/month); 10,000 credits/month, consumption varies by task complexity
```

Insert after the Personal Computer bullet:

```
- **Fully local on Mac (2026-10-20):** the model, harness and task execution can all run on supported Apple-silicon Macs (36 GB+ unified memory recommended), working across local files and Mac apps such as Notes, Messages, Mail and Numbers with permission. Local models are Qwen 3.6 or PPLX Pro, a post-trained Qwen ([Qwen 3.8](../models/qwen-3-8.md) per Perplexity's X thread); local tasks use no Computer credits, and the mode is open to Pro, Max and Enterprise subscribers. Hybrid Compute (September) instead starts in the cloud and hands private-file work to a local model, and a local task can be allowed to escalate to the cloud for current information, browser use and connected apps.
```

In `## Strengths`, the last bullet is replaced:

```
- Fully local mode keeps planning, reasoning and file processing for sensitive work on the user's Mac, and Personal Computer covers continuity-sensitive workloads better than purely ephemeral sessions
```

In `## Weaknesses / caveats`, the first bullet is replaced:

```
- Cloud Computer's $200/month Max price limits it to power users and enterprises; the local mode reaches Pro subscribers but needs a 36 GB-class Apple-silicon Mac
```

In `## Recent changes`, insert at the top:

```
- [2026-10-20] Computer runs fully local on Apple-silicon Macs (Qwen 3.6 or PPLX Pro, no credits used, 36 GB+ recommended) for Pro, Max and Enterprise; Hybrid Compute splits tasks between cloud and local models.
```

In `## Sources`, append:

```
- [Perplexity — Perplexity Computer now runs fully local on Mac](../sources/articles/perplexity-computer-local-mac-2026-10-20.md)
```

### wiki/state-of/computer-use.md (updated)

Frontmatter changes: `as_of` unchanged (2026-11-24); `sources:` appends `perplexity-computer-local-mac-2026-10-20`.

In `### Computer use`, the Perplexity Computer line is replaced:

```
- [Perplexity Computer](../tools/perplexity-computer.md) — Perplexity's persistent digital-proxy agent: 19-model orchestration, 400+ app and 12,000+ financial-institution connectivity, remote control from any device; can now also run fully on-device on Apple-silicon Macs with a Perplexity-tuned Qwen model, using no credits, for Pro, Max and Enterprise *(as of 2026-10-20)*
```

In `## Recent changes`, insert directly below the 2026-11-24 Cua entry (date order):

```
- [2026-10-20] Perplexity Computer can run fully local on Apple-silicon Macs: model, harness and execution on-device across local files and Mac apps, no credits used, open to Pro, Max and Enterprise.
```

Then remove the oldest entry (the cap is 10):

```
- [2026-05-05] Added knowledge-work OS framing: left-sidebar desktop app + agentic terminal is emerging as a universal knowledge-work interface pattern; sticky workflow state creates switching costs
```

In `## Sources`, append:

```
- [Perplexity — Perplexity Computer now runs fully local on Mac](../sources/articles/perplexity-computer-local-mac-2026-10-20.md)
```

### wiki/history/state-of/computer-use.md (updated)

The file already ends with a 2026-11-24 archive block (holding the Gemini downloadable-files entry); if applied on that date, add the entry to that block, otherwise open a new `## Archived from current page on <apply date>` block:

```
- [2026-05-05] Added knowledge-work OS framing: left-sidebar desktop app + agentic terminal is emerging as a universal knowledge-work interface pattern; sticky workflow state creates switching costs
```

### wiki/sources/articles/perplexity-computer-local-mac-2026-10-20.md (new)

```
---
title: Perplexity — Perplexity Computer now runs fully local on Mac
type: source
source_type: article
source_file: raw/articles/2026-11-24-perplexityai-hub-blog-perplexity-computer-now-runs-fully-local-on-mac.md
url: https://www.perplexity.ai/hub/blog/perplexity-computer-now-runs-fully-local-on-mac
published: 2026-10-20
ingested: 2026-11-24
domains: [computer-use]
---

# Perplexity — Perplexity Computer now runs fully local on Mac

Perplexity's launch post for running Computer entirely on a Mac: model, harness and task execution on-device, working across local files and native apps with permission, so sensitive data stays local and local tasks spend no credits. Read with Perplexity's same-day X thread (raw/tweets/2026-11-24-xcom-perplexity-ai-2112571597798461920.md) and AINews' 2026-10-21 "Agent Infrastructure" item.

## Influenced pages
- [Perplexity Computer](../../tools/perplexity-computer.md) — fully local mode, Hybrid Compute, plan scope
- [State of Computer Use](../../state-of/computer-use.md) — Perplexity leader line mentions local execution

## Key claims extracted
- Computer can run the AI model, harness and task execution entirely on supported Apple-silicon Macs
- With permission it works across local files and apps including Notes, Messages, Mail and Numbers
- Local model options: Qwen 3.6 or PPLX Pro, "a post-trained version of Qwen"; Perplexity's X thread says PPLX Pro is post-trained Qwen 3.8
- Local tasks don't consume Computer credits (X thread)
- Available to Pro, Max and Enterprise subscribers; 36 GB+ unified memory recommended
- Hybrid Compute (September 2026) starts in the cloud and hands private-file work to local models; users can authorize a local task to escalate to the cloud for current information, browser use and connected apps, where the orchestrator can call 15+ frontier models
- Code and tool execution run in isolated sandboxes, as in the cloud version
- Earlier step: Personal Computer for Mac (May 2026)
- AINews (2026-10-21) reports local mode also works offline
```

## Schema / vocabulary additions

None.

## Open questions

None.
