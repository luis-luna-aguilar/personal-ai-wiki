---
type: proposal
source: raw/articles/2026-11-24-bloggoogle-introducing-gemini-4-neon.md
sources:
  - raw/articles/2026-11-24-bloggoogle-introducing-gemini-4-carbon.md
  - raw/articles/2026-11-24-bloggoogle-introducing-gemini-4-hydrogen.md
  - raw/articles/2026-11-24-bloggoogle-introducing-gemini-4-neon.md
  - raw/newsletters/2026-11-10-vibe-check-gemini-4-carbons-coding-outpaces-its.md
  - raw/newsletters/2026-11-15-the-age-of-artisanal-ai-is-coming.md
  - raw/newsletters/2026-11-20-mini-vibe-check-four-new-geminis-when-should-you.md
  - raw/newsletters/2026-11-22-stop-telling-ai-how-you-write-show-it.md
status: pending
created: 2026-11-24
---

# Proposal: Gemini 4 Carbon, Neon and Hydrogen

## Summary

### In short
Google now sells Gemini 4 as a tiered lineup rather than one flagship: Carbon for the longest, hardest jobs, Neon as a cheaper midweight that Google says matches it, and Hydrogen as the fast default for everyone. Neon scores 61 on Artificial Analysis's index at $3/$15, and Hydrogen beats Argon at $1.50/$7.50. The proposal creates Carbon and Neon pages, swaps Hydrogen in for the stale Gemini 3.5 Flash line, and updates State of Models, Gemini, State of Cybersecurity, Argon and GPT-6.2 Astra. Reason to hesitate: Every's two reviews were read only as free previews and recaps.

[[#Open questions|Open questions: 2 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Google DeepMind shipped three more Gemini 4 models in about five weeks after Argon went generally available on 13 October. Gemini 4 Carbon was announced on 28 October as Google's strongest model, built for long engineering tasks that can run for days and for cyber defense. It went first to cyber defenders in the Fairwind Program, Google's vetted-access scheme, at Argon's introductory price of $2/$10 per million tokens. Google reported first place on the new version 5.0 of the Artificial Analysis Intelligence Index (59) and 88.2% on SEC-bench Pro, a vulnerability-finding test. By early November Carbon was in wider use.

Hydrogen followed on 12 November for every tier, including free users and Google Search. At $1.50/$7.50 it replaces Gemini 3.8 Flash, with 57% against 18.2% on Terminal-Bench 4.1, and it edges Argon on the Artificial Analysis index (51 against 50). Antigravity, Google's coding app, gained Orchestrator, which switches between Carbon and Hydrogen inside one session. Neon arrived on 18 November as the midweight model, priced at $3/$15. It scores 61 on the index at its highest thinking level, third overall, and is second on the Vals Index. Google also reports first place on Artificial Analysis's Coding Agent Index, and Glean found it matched Carbon at three times the speed.

Every's testers saw the same split. Carbon is a much stronger coder than Argon but does not know when to stop: told to take only the clearest backlog tickets, it ran for more than four hours until stopped. Every also found low thinking beat medium and high. Neon showed more taste than any earlier Gemini when a person steered it and made the best Gemini slide deck Every had seen. Left alone on long, detail-heavy jobs it drifted, and it burns tokens.

### What changes
The wiki's newest Gemini is Argon. State of Models still lists Gemini 3.5 Flash from May, and the GPT-6.2 Astra page notes Carbon has no page.

- New pages `models/gemini-4-carbon.md` and `models/gemini-4-neon.md`: launch, pricing, Google's figures and Every's verdict.
- **State of Models** adds Carbon and Neon under Frontier models and shortens the Argon line, which stays because Google still offers Argon. Hydrogen replaces the Gemini 3.5 Flash line under Small / fast models. One Recent-changes entry dated 18 November; the oldest (the 16 October US open-weight entry) moves to history. Page date stays 23 November.
- **Gemini** replaces its Argon section with a four-model lineup section that covers Hydrogen and Orchestrator. Three Recent-changes entries are added, the three oldest (April) move to history, and the page date moves to 18 November.
- **State of Cybersecurity** widens the Fairwind line to Carbon and Neon's cyber variant. One Recent-changes entry is added and the oldest moves to history.
- **Gemini 4 Argon** gains a sibling pointer and its rescored index value. Its date moves to 12 November.
- **GPT-6.2 Astra** links its Carbon mention.
- Seven source pages.

### What to weigh
Artificial Analysis rescored its index to version 5.0 around Carbon's launch. The new numbers (Carbon 59, Neon 61, Argon 50) are not comparable with older lines such as Argon's 53 or Opus 5.5's Coding Agent Index 66, so the drafts do not move any leader claim on the strength of them. Carbon's date of wide availability is inferred from Every's 10 November review and Hydrogen's 12 November post. Google's "Carbon is now available" post was not read.

## Intended changes

- [ ] **Create** `wiki/models/gemini-4-carbon.md` — new page for Google's strongest Gemini 4 model
    > See draft below

- [ ] **Create** `wiki/models/gemini-4-neon.md` — new page for the midweight Gemini 4 model
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — add Carbon and Neon lines under Frontier models; shorten the Argon line; replace the Gemini 3.5 Flash line with Gemini 4 Hydrogen under Small / fast models; append four source ids to `sources:`; adds one Recent-changes entry dated 2026-11-18 (list is at the cap of 10, so the oldest entry spills); `as_of` stays 2026-11-23
    > See draft below

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — oldest Recent-changes entry (2026-10-16, US open-weight push; the 2026-10-13 Argon entry already spilled today)
    > See draft below

- [ ] **Update** `wiki/tools/gemini.md` — replace the "Gemini 4 Argon" status section with a "Gemini 4 lineup" section; `as_of` and Current-status stamp to 2026-11-18; append three source ids and Sources links; adds three Recent-changes entries dated 2026-11-18, 2026-11-12 and 2026-10-28 (list is at the cap, so the three oldest spill)
    > See draft below

- [ ] **Spill** `wiki/tools/gemini.md` → `wiki/history/tools/gemini.md` — three oldest Recent-changes entries (2026-04-23, 2026-04-22, 2026-04-21)
    > See draft below

- [ ] **Update** `wiki/state-of/cybersecurity.md` — rewrite the Google Fairwind Program line to cover Carbon and Neon; append two source ids; adds one Recent-changes entry dated 2026-10-28 (list is at the cap, so the oldest entry spills); `as_of` stays 2026-11-23
    > See draft below

- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — oldest Recent-changes entry (2026-09-30, the Fairwind Program entry; the GLM-5.3 / OpenShell entry already spilled today)
    > See draft below

- [ ] **Update** `wiki/models/gemini-4-argon.md` — sibling pointer in the intro, AA v5.0 rescore, one Recent-changes entry dated 2026-11-12; `as_of` to 2026-11-12; append one source
    > See draft below

- [ ] **Update** `wiki/models/gpt-6-2-astra.md` — link the Gemini 4 Carbon mention in Weaknesses / caveats
    > See draft below

- [ ] **Create** `wiki/sources/articles/google-introducing-gemini-4-carbon.md` — source summary

- [ ] **Create** `wiki/sources/articles/google-introducing-gemini-4-hydrogen.md` — source summary

- [ ] **Create** `wiki/sources/articles/google-introducing-gemini-4-neon.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-vibe-check-gemini-4-carbon-2026-11-10.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-carbon-verdict-recap-2026-11-15.md` — source summary (story page for the Carbon item in the 11-15 Every digest)

- [ ] **Create** `wiki/sources/newsletters/every-mini-vibe-check-gemini-4-neon-2026-11-20.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-neon-verdict-recap-2026-11-22.md` — source summary (story page for the Neon item in the 11-22 Every digest)

## Page drafts

### wiki/models/gemini-4-carbon.md (new)

```
---
title: Gemini 4 Carbon
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [google, closed-source]
as_of: 2026-11-15
sources: [google-introducing-gemini-4-carbon, google-introducing-gemini-4-hydrogen, every-vibe-check-gemini-4-carbon-2026-11-10, every-carbon-verdict-recap-2026-11-15]
---

# Gemini 4 Carbon

Google DeepMind's strongest Gemini 4 model, announced 2026-10-28, two weeks after [Gemini 4 Argon](gemini-4-argon.md) went GA. Built for long-horizon engineering (Google says it runs for days on root-causing and patching bugs in large codebases) and for cyber defense. Sits at the top of a four-model lineup with Argon, the midweight [Gemini 4 Neon](gemini-4-neon.md) and the fast Hydrogen (see [Gemini](../tools/gemini.md)).

## Current status (as of 2026-11-15)

- **Rollout:** first to a subset of cyber defenders through Google's Fairwind Program, then trusted partners, while Google refined guardrails; in wider use by 2026-11-10 (Every's Vibe Check) and selectable in Antigravity's Orchestrator by 2026-11-12
- **Pricing:** launched at Argon's introductory $2 / $10 per 1M input/output tokens; cached input 95% off
- **Google's figures:** #1 on Artificial Analysis Intelligence Index v5.0 at launch (59); WebDev Arena #4 (1768, +89 over Argon); cyber: SEC-bench Pro 88.2%, ExploitGym 54.8%, CWE-bench 71.0%, more than 2x Argon's secure-code success rate
- **Alignment claims:** 0.0% successful cheating on Terminal-Bench 4.0 (0.4% attempts); about 80% fewer high-severity misalignment alerts in internal coding; about half Argon's unsupported claims; 0.0% attack success on Gray Swan's indirect prompt-injection benchmark

## Reception

Every's seven testers found Carbon a much stronger coder than Argon and "a win for Google's loyalists", but poor at knowing when to stop: told to take only the clearest tickets in a backlog, it ran for more than four hours until stopped. Every's advice: give it one big job with a clear finish line, start at low thinking (it beat medium and high on timed tasks), and check what it touched afterwards.

## Weaknesses / caveats

- Overruns scope on open-ended agent work despite Google's reported 26% cut in overreach
- Benchmark figures are Google's; Artificial Analysis's v5.0 rescoring makes them incomparable with earlier index numbers in this wiki
- Every's full review (ratings and benchmark breakdown) is paywalled; only the preview and recap were read

## Recent changes

- [2026-11-15] Every's verdict: stronger coder than Argon, does not stop on its own; start at low thinking.
- [2026-10-28] Announced as Google's strongest model; Fairwind defenders first; AA Intelligence Index v5.0 59; $2/$10 introductory.

## Sources

- [Google — Introducing Gemini 4 Carbon](../sources/articles/google-introducing-gemini-4-carbon.md)
- [Google — Introducing Gemini 4 Hydrogen](../sources/articles/google-introducing-gemini-4-hydrogen.md)
- [Every — Vibe Check: Gemini 4 Carbon](../sources/newsletters/every-vibe-check-gemini-4-carbon-2026-11-10.md)
- [Every — Carbon verdict recap](../sources/newsletters/every-carbon-verdict-recap-2026-11-15.md)
```

### wiki/models/gemini-4-neon.md (new)

```
---
title: Gemini 4 Neon
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [google, closed-source]
as_of: 2026-11-22
sources: [google-introducing-gemini-4-neon, every-mini-vibe-check-gemini-4-neon-2026-11-20, every-neon-verdict-recap-2026-11-22]
---

# Gemini 4 Neon

Google DeepMind's midweight Gemini 4 model, launched 2026-11-18 and the newest of four Gemini 4 models shipped in about five weeks. Google places it between [Gemini 4 Carbon](gemini-4-carbon.md) (hardest, longest jobs) and Hydrogen (fast everyday work), as frontier-level reasoning at lower cost and higher speed. In Antigravity it can act as an orchestrator directing parallel Hydrogen subagents.

## Current status (as of 2026-11-18)

- **Availability:** Gemini API (paid tier) in AI Studio and Android Studio, Gemini for business, Antigravity (paid Pro/Ultra), Gemini app (Pro/Ultra); a cyber variant is rolling out to Fairwind Program defenders
- **Pricing:** $3 / $15 per 1M input/output tokens, cached input $0.15 (95% off); 1M-token context; four thinking levels, high by default
- **Google's figures:** AA Intelligence Index v5.0 61 at xhigh (#3 overall); #2 Vals Index (70.9%), #1 Legal Research Bench and Tax Agent Bench; #2 Agent Arena (1336); Google reports #1 on the AA Coding Agent Index (58.6); Terminal-Bench 4.1 65.2%; FrontierCode 2.0 46.2% at high; SEC-bench Pro 90.5%
- **Cost:** 32% lower cost per task than Carbon at high; Glean found it matched or beat Carbon at 3x the speed and 60% of the cost

## Reception

Every's Mini-Vibe Check: with a person steering, Neon shows more taste than any earlier Gemini, made the best Gemini slide deck Every has seen, and is now paired with Opus 5.5 for coding at the keyboard by one Every engineer. Every would pick Neon for work it can steer, Hydrogen for cheaper runs and Carbon for longer builds.

## Weaknesses / caveats

- Drifts on long, detail-heavy jobs left unattended
- Token-hungry, which matters most when paying per token rather than through a Google subscription
- Every's full review is paywalled; only the preview and recap were read
- Index figures are on Artificial Analysis's v5.0 scale and not comparable with older numbers in this wiki

## Recent changes

- [2026-11-22] Every's verdict: best for steered work, drifts and burns tokens when left alone.
- [2026-11-18] Launched at $3/$15; AA Intelligence Index 61 at xhigh, #2 Vals Index, #2 Agent Arena.

## Sources

- [Google — Introducing Gemini 4 Neon](../sources/articles/google-introducing-gemini-4-neon.md)
- [Every — Mini-Vibe Check: Gemini 4 Neon](../sources/newsletters/every-mini-vibe-check-gemini-4-neon-2026-11-20.md)
- [Every — Neon verdict recap](../sources/newsletters/every-neon-verdict-recap-2026-11-22.md)
```

### wiki/state-of/models.md (updated)

Frontmatter: append to `sources:` → `google-introducing-gemini-4-carbon, google-introducing-gemini-4-neon, google-introducing-gemini-4-hydrogen, every-neon-verdict-recap-2026-11-22`. `as_of` stays 2026-11-23.

Under `### Frontier models`, replace the Gemini 4 Argon line with these three lines:

```
- [Gemini 4 Carbon](../models/gemini-4-carbon.md) — Google's strongest model, announced 2026-10-28 (Fairwind defenders first); #1 on the AA Intelligence Index v5.0 at launch (59), SEC-bench Pro 88.2%; $2/$10 introductory; Every: a much stronger coder than Argon that does not know when to stop *(as of 2026-11-15)*
- [Gemini 4 Neon](../models/gemini-4-neon.md) — Google midweight, launched 2026-11-18 at $3/$15; AA Intelligence Index v5.0 61 at xhigh (#3), #2 Vals Index and Agent Arena; Glean: matches Carbon at 3x the speed; Every: tasteful when steered, drifts unattended, token-hungry *(as of 2026-11-22)*
- [Gemini 4 Argon](../models/gemini-4-argon.md) — Google; GA 2026-10-13 and still offered beside Carbon; #1 Vals Index and Text Arena at launch, 1M-token output; weak monitorability *(as of 2026-10-16)*
```

Under `### Small / fast models`, replace the Gemini 3.5 Flash line with:

```
- [Gemini 4 Hydrogen](../tools/gemini.md) — Google, launched 2026-11-12 for every tier including free users and Search; replaces Gemini 3.8 Flash at $1.50/$7.50 flat over 1M context; AA Intelligence Index v5.0 51 (Argon 50); Terminal-Bench 4.1 57% vs 18.2% for 3.8 Flash *(as of 2026-11-12)*
```

`## Recent changes`: insert between the 2026-11-23 and 2026-11-09 entries, then drop the oldest entry (2026-10-16) to history:

```
- [2026-11-18] Gemini 4 Carbon (announced 2026-10-28, AA Intelligence Index v5.0 59) and Gemini 4 Neon ($3/$15, AA 61 at xhigh) added to Frontier models beside Argon; Gemini 4 Hydrogen ($1.50/$7.50, launched 2026-11-12) replaces Gemini 3.5 Flash in Small / fast models.
```

### wiki/history/state-of/models.md (updated)

Append under the existing `## Archived from current page on 2026-11-24` block at the end of the file (or a new block with the apply date if that differs):

```
- [2026-10-16] US open-weight push: Meta's Muse Spark Open (816B/42B, AA 39, top US open model) and Reflection Beam 1.0 (501B/23B, Apache 2.0, AA 30) added to Open-weight models, both behind GLM-5.3 (45) and Kimi K3 (44); Mistral Large 4 (AA 38, previewed 2026-10-07, weights pending) added alongside.
```

### wiki/tools/gemini.md (updated)

Frontmatter: `as_of: 2026-11-18`; append to `sources:` → `google-introducing-gemini-4-carbon, google-introducing-gemini-4-hydrogen, google-introducing-gemini-4-neon`.

Change the heading `## Current status (as of 2026-10-14)` to `## Current status (as of 2026-11-18)`, and replace the whole `### Gemini 4 Argon (as of 2026-10-14)` section with:

```
### Gemini 4 lineup (as of 2026-11-18)

Google shipped four Gemini 4 models in about five weeks, now sold as tiers:

- [Gemini 4 Carbon](../models/gemini-4-carbon.md) (announced 2026-10-28) — strongest model, for long-horizon engineering and cyber defense; defenders first through the Fairwind Program
- [Gemini 4 Argon](../models/gemini-4-argon.md) (GA 2026-10-13) — still offered as a frontier model beside Carbon
- [Gemini 4 Neon](../models/gemini-4-neon.md) (2026-11-18) — midweight at $3/$15, aimed at complex, high-frequency work
- **Gemini 4 Hydrogen** (2026-11-12) — fast everyday model for all tiers, including free users, Gemini for business, the Gemini app and Search; replaces Gemini 3.8 Flash at $1.50/$7.50 flat across its 1M-token context, with up to 1M output tokens. Google reports AA Intelligence Index v5.0 51 at high and 54 at xhigh (Argon 50), Terminal-Bench 4.1 57% (3.8 Flash 18.2%), 2.5x faster task completion than 3.8 Flash, and 5x fewer fabricated claims; four thinking levels (low, medium, high default, xhigh)

**Orchestrator in Antigravity** (2026-11-12) switches between models such as Carbon and Hydrogen inside one session: on Terminal-Bench 4.0 it came close to Carbon's success rate using 24% less quota and finishing 19% faster. For parallel work Carbon or Neon coordinates while Hydrogen runs worker and verifier agents. Argon's GA brought the Antigravity coding interface to the Gemini macOS app and 40+ connected apps.
```

`## Recent changes`: insert these three entries at the top, then drop the three oldest (2026-04-23, 2026-04-22, 2026-04-21) to history:

```
- [2026-11-18] Gemini 4 Neon launched as the midweight model at $3/$15; AA Intelligence Index v5.0 61 at xhigh, #2 Vals Index.
- [2026-11-12] Gemini 4 Hydrogen launched for every tier and Search, replacing Gemini 3.8 Flash at $1.50/$7.50; Orchestrator in Antigravity switches between Carbon and Hydrogen within a session.
- [2026-10-28] Gemini 4 Carbon announced as Google's strongest model; Fairwind defenders first, at Argon's $2/$10 introductory price.
```

`## Sources`: append

```
- [Google — Introducing Gemini 4 Carbon](../sources/articles/google-introducing-gemini-4-carbon.md)
- [Google — Introducing Gemini 4 Hydrogen](../sources/articles/google-introducing-gemini-4-hydrogen.md)
- [Google — Introducing Gemini 4 Neon](../sources/articles/google-introducing-gemini-4-neon.md)
```

### wiki/history/tools/gemini.md (updated)

Append under a new `## Archived from current page on <apply date>` header:

```
- [2026-04-23] Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; Agent Studio, 200+ models, Workspace Intelligence GA, Knowledge Catalog, Gemini Embedding 2 GA, and broader agent governance stack
- [2026-04-22] Added benchmark scores for Deep Research Max (93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE); added collaborative planning and code execution capabilities from AINews coverage
- [2026-04-21] Added Deep Research and Deep Research Max: Gemini API public preview, MCP support, multimodal grounding, and native visual reports
```

### wiki/state-of/cybersecurity.md (updated)

Frontmatter: append to `sources:` → `google-introducing-gemini-4-carbon, google-introducing-gemini-4-neon`. `as_of` stays 2026-11-23.

Under `### Trusted defensive access`, replace the Google Fairwind Program line with:

```
- **Google Fairwind Program** — Google's vetted-defender access for Gemini 4: [Argon](../models/gemini-4-argon.md) went to government users and 650+ defenders first (2026-09-30), then GA on 2026-10-13; [Carbon](../models/gemini-4-carbon.md) followed the same path from 2026-10-28 (SEC-bench Pro 88.2%, ExploitGym 54.8%); a cyber variant of [Neon](../models/gemini-4-neon.md) is rolling out to members since 2026-11-18 *(as of 2026-11-18)*
```

`## Recent changes`: insert in date order (above the 2026-10-22 entry, below the 2026-11-09 entry), then drop the oldest entry to history: the 2026-09-30 Fairwind entry, whose content this proposal's new entry and leader line carry forward:

```
- [2026-10-28] Fairwind Program extended to Gemini 4 Carbon (defenders first, SEC-bench Pro 88.2%) and, from 2026-11-18, a cyber variant of Gemini 4 Neon.
```

### wiki/history/state-of/cybersecurity.md (updated)

Append under the existing `## Archived from current page on 2026-11-24` block at the end of the file (or a new block with the apply date if that differs):

```
- [2026-09-30] Added Google's Fairwind Program to Trusted defensive access: Gemini 4 Argon shipped first to government users and 650+ vetted defenders, then went GA on 2026-10-13.
```

### wiki/models/gemini-4-argon.md (updated)

Frontmatter: `as_of: 2026-11-12`; append `google-introducing-gemini-4-hydrogen` to `sources:`.

Append to the intro paragraph:

```
Since late October it has three siblings: the stronger [Gemini 4 Carbon](gemini-4-carbon.md), the midweight [Gemini 4 Neon](gemini-4-neon.md) and the fast Hydrogen; Google still offers Argon as a frontier model beside Carbon, and on Artificial Analysis's rescored v5.0 index Argon sits at 50, just below Hydrogen's 51.
```

`## Recent changes`: insert at the top:

```
- [2026-11-12] Google's Hydrogen post puts Argon at 50 on AA Intelligence Index v5.0 (Hydrogen 51) and keeps it beside Carbon as a frontier model.
```

`## Sources`: append

```
- [Google — Introducing Gemini 4 Hydrogen](../sources/articles/google-introducing-gemini-4-hydrogen.md)
```

### wiki/models/gpt-6-2-astra.md (updated)

Under `## Weaknesses / caveats`, replace

`- OpenAI's comparisons name [Claude Fable 5.2](claude-fable-5-2.md) and Gemini 4 Carbon; Gemini 4 Carbon has no page in this wiki yet.`

with

```
- OpenAI's comparisons name [Claude Fable 5.2](claude-fable-5-2.md) and [Gemini 4 Carbon](gemini-4-carbon.md).
```

### wiki/sources/articles/google-introducing-gemini-4-carbon.md (new)

```
---
title: Introducing Gemini 4 Carbon
type: source
source_type: article
source_file: raw/articles/2026-11-24-bloggoogle-introducing-gemini-4-carbon.md
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
published: 2026-10-28
ingested: 2026-11-24
domains: [models, coding, cybersecurity]
---

# Google — Introducing Gemini 4 Carbon

Koray Kavukcuoglu's launch post for Gemini 4 Carbon, Google's strongest model, aimed at long-horizon engineering and cyber defense. Access starts with Fairwind Program defenders while guardrails are refined.

## Influenced pages

- [Gemini 4 Carbon](../../models/gemini-4-carbon.md) — new page
- [State of Models](../../state-of/models.md) — Carbon frontier line
- [Gemini](../../tools/gemini.md) — Gemini 4 lineup section
- [State of Cybersecurity](../../state-of/cybersecurity.md) — Fairwind line

## Key claims extracted

- Announced 2026-10-28, two weeks after Argon; Fairwind defenders first, then trusted partners
- #1 on AA Intelligence Index v5.0 (59); WebDev Arena #4 (1768)
- SEC-bench Pro 88.2%, ExploitGym 54.8%, CWE-bench 71.0%; more than 2x Argon's secure-code success rate
- Introductory price $2/$10, cached input 95% off
- 0.0% successful cheating on Terminal-Bench 4.0; about 80% fewer high-severity misalignment alerts; 0.0% Gray Swan IPI attack success
```

### wiki/sources/articles/google-introducing-gemini-4-hydrogen.md (new)

```
---
title: Introducing Gemini 4 Hydrogen
type: source
source_type: article
source_file: raw/articles/2026-11-24-bloggoogle-introducing-gemini-4-hydrogen.md
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
published: 2026-11-12
ingested: 2026-11-24
domains: [models, coding]
---

# Google — Introducing Gemini 4 Hydrogen

Launch post for Gemini 4 Hydrogen, Google's fast everyday Gemini 4 model, available to every tier including free users and Search, and for Orchestrator in Antigravity, which switches models within a session.

## Influenced pages

- [State of Models](../../state-of/models.md) — Hydrogen replaces the Gemini 3.5 Flash line
- [Gemini](../../tools/gemini.md) — Hydrogen and Orchestrator in the lineup section
- [Gemini 4 Argon](../../models/gemini-4-argon.md) — v5.0 index value, still offered beside Carbon
- [Gemini 4 Carbon](../../models/gemini-4-carbon.md) — Orchestrator availability

## Key claims extracted

- Launched 2026-11-12; $1.50/$7.50 flat across a 1M-token context; up to 1M output tokens
- AA Intelligence Index v5.0 51 at high, 54 at xhigh; Argon 50
- Replaces Gemini 3.8 Flash: 2.5x faster, Terminal-Bench 4.1 57% vs 18.2%, 5x fewer fabricated claims
- Orchestrator on Terminal-Bench 4.0: near-Carbon success, 24% less quota, 19% faster
- Four thinking levels, new xhigh tier; Search upgraded to Hydrogen globally
```

### wiki/sources/articles/google-introducing-gemini-4-neon.md (new)

```
---
title: Introducing Gemini 4 Neon
type: source
source_type: article
source_file: raw/articles/2026-11-24-bloggoogle-introducing-gemini-4-neon.md
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
published: 2026-11-18
ingested: 2026-11-24
domains: [models, coding, cybersecurity]
---

# Google — Introducing Gemini 4 Neon

Launch post for Gemini 4 Neon, the midweight Gemini 4 model, positioned between Carbon and Hydrogen for complex, high-frequency work at lower cost.

## Influenced pages

- [Gemini 4 Neon](../../models/gemini-4-neon.md) — new page
- [State of Models](../../state-of/models.md) — Neon frontier line
- [Gemini](../../tools/gemini.md) — lineup section
- [State of Cybersecurity](../../state-of/cybersecurity.md) — Neon cyber variant via Fairwind

## Key claims extracted

- Launched 2026-11-18; $3/$15, cached input $0.15; 1M context; four thinking levels
- AA Intelligence Index v5.0 61 at xhigh (#3 overall); #2 Vals Index (70.9%); #2 Agent Arena (1336)
- Google reports #1 on AA Coding Agent Index (58.6); Terminal-Bench 4.1 65.2%; FrontierCode 2.0 46.2% at high
- SEC-bench Pro 90.5%; cyber variant rolling out to Fairwind defenders
- 32% lower cost per task than Carbon at high; Glean: matches or beats Carbon at 3x speed and 60% of cost
```

### wiki/sources/newsletters/every-vibe-check-gemini-4-carbon-2026-11-10.md (new)

```
---
title: "Vibe Check: Gemini 4 Carbon's Coding Outpaces Its Judgment"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-10-vibe-check-gemini-4-carbons-coding-outpaces-its.md
url: https://every.to/vibe-check/vibe-check-gemini-4-carbon-doesn-t-know-when-to-stop
published: 2026-11-10
ingested: 2026-11-24
domains: [models]
---

# Every — Vibe Check: Gemini 4 Carbon

Every's Vibe Check of Gemini 4 Carbon after seven staff tested it across coding, writing, design and knowledge work. Only the free preview was available; ratings and benchmark breakdowns are paywalled.

## Influenced pages

- [Gemini 4 Carbon](../../models/gemini-4-carbon.md) — reception, wide-availability date

## Key claims extracted

- Carbon is "a stronger coder and a win for Google's loyalists"
- It arrives just as Fable 5.2 "raises the bar again"
```

### wiki/sources/newsletters/every-carbon-verdict-recap-2026-11-15.md (new)

```
---
title: 'Every Sunday recap: Gemini 4 Carbon verdict'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-15-the-age-of-artisanal-ai-is-coming.md
url: https://every.to/vibe-check/vibe-check-gemini-4-carbon-doesn-t-know-when-to-stop
published: 2026-11-15
ingested: 2026-11-24
domains: [models]
---

# Every — Carbon verdict recap (2026-11-15)

The Carbon item in Every's 15 November Sunday digest ("The Age of Artisanal AI Is Coming"), summarizing the paywalled Vibe Check's verdict.

## Influenced pages

- [Gemini 4 Carbon](../../models/gemini-4-carbon.md) — reception and usage advice

## Key claims extracted

- Carbon is a much stronger coder than Gemini 4 Argon but does not know when to stop
- Told to take only the clearest backlog tickets, it ran more than four hours until stopped
- Low thinking beat medium and high on timed tasks; give it one big job with a clear finish line and check what it touched
```

### wiki/sources/newsletters/every-mini-vibe-check-gemini-4-neon-2026-11-20.md (new)

```
---
title: 'Mini-Vibe Check: Four New Geminis. When Should You Pick Neon?'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-20-mini-vibe-check-four-new-geminis-when-should-you.md
url: https://every.to/vibe-check/mini-vibe-check-four-new-geminis-when-should-you-pick-neon
published: 2026-11-20
ingested: 2026-11-24
domains: [models]
---

# Every — Mini-Vibe Check: Gemini 4 Neon

Every's short review of Gemini 4 Neon on drafts, decks and code. Only the free preview was available.

## Influenced pages

- [Gemini 4 Neon](../../models/gemini-4-neon.md) — reception

## Key claims extracted

- Pick Neon for work you can steer, Hydrogen for cheaper runs, Carbon for longer builds
- With a person steering, Neon shows more taste than any Gemini Every has tested; left alone on a long, detail-heavy job it does worse
- Token cost is a catch, mostly when paying per token rather than via a Google subscription
```

### wiki/sources/newsletters/every-neon-verdict-recap-2026-11-22.md (new)

```
---
title: 'Every Sunday recap: Gemini 4 Neon verdict'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-22-stop-telling-ai-how-you-write-show-it.md
url: https://every.to/vibe-check/mini-vibe-check-four-new-geminis-when-should-you-pick-neon
published: 2026-11-22
ingested: 2026-11-24
domains: [models]
---

# Every — Neon verdict recap (2026-11-22)

The Neon item in Every's 22 November Sunday digest ("Stop Telling AI How You Write. Show It."), summarizing the paywalled Mini-Vibe Check.

## Influenced pages

- [Gemini 4 Neon](../../models/gemini-4-neon.md) — reception
- [State of Models](../../state-of/models.md) — Neon line

## Key claims extracted

- Google added four models to the Gemini 4 lineup in little more than five weeks; Neon is the newest, midweight model
- Every would pick Neon for work it can steer; Kieran Klaassen pairs it with Opus 5.5 for coding at the keyboard
- Mike Taylor calls its slide deck the best he has seen from a Gemini model, but it burns through tokens
```

## Schema / vocabulary additions

None.

## Open questions

- Hydrogen gets a lineup entry on the Gemini page and a State of Models line, not its own page. Should it get `models/gemini-4-hydrogen.md` now that Google's launch post gives it full specs (assumed no, since every other small/fast Gemini lives on the Gemini page)?
	- Ok.
- The Gemini page is at about 1,370 of 1,500 body words (91%) after this change, and its own caveats already say it mixes assistant, enterprise-platform and API layers. Should a later refactor split it (assumed not now)?
	- Ok, later.
