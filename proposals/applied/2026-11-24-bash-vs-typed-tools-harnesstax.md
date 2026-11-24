---
type: proposal
source: raw/papers/2026-11-24-arxivorg-html-260911999.md
sources:
  - raw/papers/2026-11-24-arxivorg-html-260911999.md
  - raw/papers/2026-11-24-arxivorg-abs-260911999.md
  - raw/articles/2026-11-24-arenaai-blog-coding-agents-harness-tax.md
  - raw/papers/2026-11-24-arxivorg-abs-260920804.md
  - raw/papers/2026-11-24-arxivorg-abs-260916461.md
  - raw/newsletters/2026-09-16-ainews-jev-a-system-one-model-that-only-decid.md
  - raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
  - raw/newsletters/2026-09-17-ainews-reality-checks-on-ai-news-yegge-shuts-do.md
status: pending
created: 2026-11-24
---

# Proposal: Bash beats typed tool catalogs; harness choice moves cost more than success

## Summary

### In short
A smaller tool surface is usually the better one: giving an agent bash alone beat a catalog of typed tools on enterprise-work benchmarks while using fewer tokens. The same September studies found that the choice of harness changes cost far more than it changes success. The proposal adds a "tool surface" subsection and Arena's HarnessTax result to Harness vs model, puts a protocol-preserving context-trimming result on Context editing, and creates four small source pages. The reason to hesitate is length: Harness vs model lands at about 110% of its ceiling, the edge of the band where a split is offered.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Four papers and studies from mid-September 2026, all surfaced through AINews, look at what a harness should hand the model. The main one is a Microsoft paper, "Is Bash All You Need?" (10 September). It ran Opus 4.8 and GPT-5.5 on TheAgentCompany and APEX-Agents, two benchmarks of office work: moving between apps, coordinating with simulated coworkers, and analysing documents. It compared five tool interfaces. Bash alone scored 21.8–24.5 points higher than a typed tool catalog on TheAgentCompany and 4.8–7.4 points higher on APEX-Agents, with 19–72% fewer tokens. Adding typed tools, or tools the agent wrote and kept, on top of bash gave no measurable gain. Programmatic tool calling is code the agent writes that can only call a fixed catalog. It saved tokens against direct typed calls but trailed bash on quality and cost. The authors recommend bash where execution can be sandboxed and programmatic tool calling where compliance requires a fixed tool list.

A second paper, "An Empirical Study of Harness Design for Coding Agents" (17 September), varied one harness component at a time across four models. It found that predefined tools help models that are weak at bash, while bash-capable models do as well with bash only, at much lower cost.

Arena's HarnessTax study (16 September) ran seven models through Claude Code, Codex CLI and Pi on SWE-bench Lite and Terminal-Bench 2.0. The harness moved success by only about 2–5 points, but the same model could cost up to five times more. Pi, which offers only read, write, edit and bash, sat on the cost-performance frontier. The fourth paper tested ways to trim an agent's context. Keeping protocol-critical state intact beat recency and summarization trimming on task success.

### What changes
Harness vs model measures how much a harness moves a score, but it says nothing about which tools a harness should expose. Context editing, the page that holds in-session context management, covers compaction only through one deletion-based plugin.

- **Harness vs model** gains a "Tool surface: bash vs typed tools" subsection under Current status. Arena's HarnessTax result goes into the dissent section beside Alex Zhang, because it cuts against the claim that harnesses move success rates sharply. One Recent-changes entry dated 17 September is added. The page date stays 6 October.
- **Context editing** gains one bullet on protocol-preserving trimming under Research and tools and one Recent-changes entry dated 15 September. The page date stays 26 October.
- The index line for Harness vs model names the new evidence.
- Four new source pages: the Microsoft paper, the harness-design study, Arena's HarnessTax post and the trimming paper.

### What to weigh
The harness-design study and the trimming paper were read from their arXiv abstracts only, so their wiki lines stay at abstract level. The HarnessTax numbers come from the full Arena post. HarnessTax and the older evidence on the page point in different directions. Earlier studies saw 20-point swings from the harness, and HarnessTax sees almost none. The draft presents this as a dissent rather than settling it.

## Intended changes

- [ ] **Update** `wiki/concepts/harness-vs-model.md` — new `### Tool surface: bash vs typed tools` subsection under Current status; one paragraph on HarnessTax appended to "The harness cycle and its dissent"; adds one Recent-changes entry dated 2026-09-17, inserted between the 2026-09-30 and 2026-09-09 entries (list goes from 7 to 8, no spill); append four source ids to `sources:` and four Sources lines; `as_of` stays 2026-10-06
    > See draft below

- [ ] **Update** `wiki/concepts/context-editing.md` — one bullet appended to "Research and tools"; adds one Recent-changes entry dated 2026-09-15 at the bottom, after the 2026-10-19 entry (list goes from 3 to 4, no spill); append one source id and one Sources line; `as_of` stays 2026-10-26
    > See draft below

- [ ] **Update** `wiki/index.md` — refresh the harness-vs-model description (date unchanged)
    > See draft below

- [ ] **Create** `wiki/sources/papers/is-bash-all-you-need-2026-09.md` — source summary (Microsoft paper)

- [ ] **Create** `wiki/sources/papers/harness-design-empirical-study-2026-09.md` — source summary

- [ ] **Create** `wiki/sources/articles/arena-harnesstax-2026-09.md` — source summary

- [ ] **Create** `wiki/sources/papers/protocol-preserving-context-trimming-2026-09.md` — source summary

## Page drafts

### wiki/concepts/harness-vs-model.md (updated)

Frontmatter: append `is-bash-all-you-need-2026-09, harness-design-empirical-study-2026-09, arena-harnesstax-2026-09` to `sources:`. `as_of` unchanged.

Insert a new subsection after the "Computer use shows the same split from inside a lab…" paragraph and before `### The harness cycle and its dissent`:

```md
### Tool surface: bash vs typed tools

A September 2026 Microsoft paper compared five tool interfaces on two office-work benchmarks (TheAgentCompany, APEX-Agents) with Opus 4.8 and GPT-5.5. Bash alone beat a typed tool catalog by 21.8–24.5 points on TheAgentCompany and 4.8–7.4 points on APEX-Agents, using 19–72% fewer tokens. Adding typed or agent-written tools on top of bash gave no measurable gain. Programmatic tool calling, where the agent writes code that may only call a fixed catalog, saved tokens over direct typed calls but trailed bash on quality and cost. The authors' rule: bash where execution can be sandboxed, programmatic tool calling where compliance requires a fixed tool list. A component-level study of coding harnesses adds a condition: predefined tools help bash-weak models, while bash-capable models do as well with bash only, at much lower cost.
```

Append to `### The harness cycle and its dissent`, after the paragraph ending "…and models post-trained for it.":

```md
Arena's HarnessTax study (September 2026) had already measured that cost gap. Seven models ran in Claude Code, Codex CLI and Pi on SWE-bench Lite and Terminal-Bench 2.0. The harness moved success by only ±2–5 points, but the same model could cost up to 5x more. Claude Code cost about twice as much as Pi on SWE-bench Lite, with over 10x Pi's initial context. Pi, with only read, write, edit and bash, sat on the cost-performance frontier on both, and a non-native harness gave the best success in 9 of 12 vendor-model comparisons. The authors note the benchmarks may be in training data.
```

Recent changes: insert between the 2026-09-30 and 2026-09-09 entries:

```md
- [2026-09-17] Added tool-surface evidence (Microsoft: bash alone beats typed tool catalogs on enterprise-work benchmarks with fewer tokens; a component study: predefined tools help only bash-weak models) and Arena's HarnessTax (harness choice moves success ±2–5 points but cost up to 5x; Pi's four tools on the frontier) to the dissent.
```

Sources: append:

```md
- [Is Bash All You Need? — Microsoft (arXiv)](../sources/papers/is-bash-all-you-need-2026-09.md)
- [An Empirical Study of Harness Design for Coding Agents (arXiv)](../sources/papers/harness-design-empirical-study-2026-09.md)
- [Arena — HarnessTax: How much does the harness matter for coding agents?](../sources/articles/arena-harnesstax-2026-09.md)
```

### wiki/concepts/context-editing.md (updated)

Frontmatter: append `protocol-preserving-context-trimming-2026-09` to `sources:`. `as_of` unchanged.

Append as the last bullet of `## Research and tools`:

```md
- **Trim by protocol, not by recency.** A September 2026 paper compared five ways to trim an agent's context in multi-step tool workflows. Recency, relevance and summarization saved about 60% of tokens, but task success fell to 66.6–77.3%. Keeping protocol-critical state intact and compressing the rest reached 92.2%, and adding an adaptive budget guardrail reached 96.0% success with 56.0% token savings. Keeping 25% or less of the context raised the odds of failure 10.92-fold against keeping half or more, and complex workflows needed more of it.
```

Recent changes: append as the last (oldest) entry, after the 2026-10-19 entry:

```md
- [2026-09-15] Added protocol-preserving context trimming: keeping identifiers, constraints and open commitments intact beats recency and summarization trimming on task success at similar token savings.
```

Sources: append:

```md
- [Protocol-Preserving Context Trimming for Agentic Workflows (arXiv)](../sources/papers/protocol-preserving-context-trimming-2026-09.md)
```

### wiki/index.md (updated)

Replace the harness-vs-model line:

```md
- [concepts/harness-vs-model](concepts/harness-vs-model.md) — how much of a benchmark score comes from harness choice rather than the model, with SWE-bench Pro/Composio/Harness-Bench/Harvey RLM/openJiuwen numbers, bash vs typed tool catalogs (Microsoft), OpenAI's computer-use model/harness split, Hugging Face's multi-harness RL proxy, Alex Zhang's same-loop dissent and Arena's HarnessTax cost gap, and the train→absorb→shed co-evolution theory *(as_of: 2026-10-06)*
```

### wiki/sources/papers/is-bash-all-you-need-2026-09.md (new)

```md
---
title: 'Is Bash All You Need? An Empirical Study of Tool Interfaces for Enterprise Digital Worker Agents'
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-html-260911999.md
url: https://arxiv.org/abs/2609.11999
published: 2026-09-10
ingested: 2026-11-24
domains: [agents]
---

# Is Bash All You Need? (Microsoft)

**The everyday question.** When you build an office-work agent, do you give it a neat catalog of typed tools ("send_email", "read_spreadsheet"), or a shell and let it script? Typed tools feel safer and easier to govern. Shells are what coding agents use, but office work also means jumping between apps, messaging coworkers and analysing documents.

**What the authors did.** Six Microsoft researchers ran Opus 4.8 and GPT-5.5 at default reasoning on TheAgentCompany (a simulated company with coworkers and internal apps) and APEX-Agents (professional analysis over documents). They compared five interfaces: typed tools only; typed tools plus bash; bash only; bash plus tools the agent writes and keeps for later tasks; and programmatic tool calling (PTC), where the agent writes a program but every action must go through the typed catalog.

**What they found.**
- Bash only beat typed tools only on both benchmarks: +21.8 to +24.5 points on TheAgentCompany and +4.8 to +7.4 on APEX-Agents, using 19–72% fewer total tokens. On TheAgentCompany with Opus 4.8, for example, the score rose from 44.9% to 69.4% and the estimated cost per task fell from $1.20 to $0.37.
- Adding typed tools or agent-synthesized tools on top of bash gave no detectable pooled gain and usually cost more tokens. Agents used most tools they created, but fewer of those tools reached later tasks.
- PTC used fewer tokens than direct typed calls at broadly similar scores, but generally trailed bash on quality and cost.
- The models differed. Opus 4.8 did best shell-only on coding-like and cross-app work, while GPT-5.5 was the token-efficient choice for direct typed calls. The authors warn these model recommendations may not carry over to later releases.

**Practical translation.** Default to a shell inside a sandbox. Reach for a fixed, typed catalog (ideally called from code, PTC-style) only when security or compliance demands that the agent can do nothing outside a known list.

## Influenced pages
- [Harness vs model](../../concepts/harness-vs-model.md) — new "Tool surface: bash vs typed tools" subsection

## Key claims extracted
- Five interfaces compared on TheAgentCompany and APEX-Agents with Opus 4.8 and GPT-5.5
- Bash alone vs typed tools: +21.8–24.5 pp (TheAgentCompany), +4.8–7.4 pp (APEX-Agents), 19–72% fewer tokens
- Typed tools or persistent synthesized tools added to bash: no detectable pooled score gain
- PTC: fewer tokens than direct typed calls, similar scores, generally below bash on quality and cost efficiency
- Recommendation: bash when arbitrary execution can be isolated; PTC when policy requires a fixed tool catalog
```

### wiki/sources/papers/harness-design-empirical-study-2026-09.md (new)

```md
---
title: An Empirical Study of Harness Design for Coding Agents
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-abs-260920804.md
url: https://arxiv.org/abs/2609.20804
published: 2026-09-17
ingested: 2026-11-24
domains: [agents, coding]
---

# An Empirical Study of Harness Design for Coding Agents

Most harness comparisons test whole products against each other, so nobody learns which part made the difference. This paper (read from its arXiv abstract) fixes one lightweight coding harness and changes one component at a time: planning, the action space (which tools the model gets), and context management. It covers four models on SWE-Bench Verified and Terminal-Bench 2.1, in 176 matched settings.

## Influenced pages
- [Harness vs model](../../concepts/harness-vs-model.md) — the "bash-capable models don't need predefined tools" condition in the tool-surface subsection

## Key claims extracted
- Context management matters more as the context budget tightens; most of its benefit is preventing context-overflow failures
- Rule-based elision before LLM summarization is the most efficient context strategy tested; making elided content recoverable adds machinery models rarely use, with no accuracy gain
- Planning is an accuracy scaffold for weaker models and a cost saver for stronger ones
- Predefined tools help models with weak bash skills; bash-capable models work well with a bash-only interface at substantially lower cost, especially on command-line tasks
```

### wiki/sources/articles/arena-harnesstax-2026-09.md (new)

```md
---
title: 'Arena — HarnessTax: How much does the harness matter for coding agents?'
type: source
source_type: article
source_file: raw/articles/2026-11-24-arenaai-blog-coding-agents-harness-tax.md
url: https://arena.ai/blog/coding-agents-harness-tax
published: 2026-09-16
ingested: 2026-11-24
domains: [agents, coding]
---

# Arena — HarnessTax

Melissa Pan and co-authors (including Ion Stoica and Matei Zaharia), with Arena, ran 21 model–harness pairs: seven models in Claude Code, Codex CLI and Pi. Each pair did the same 30 sampled tasks from SWE-bench Lite and Terminal-Bench 2.0, three attempts each, at the harness's high effort setting and capped at 100 turns, with costs from one fixed price list. The "harness tax" is paying more for the same quality because of the default harness. The authors say the two open benchmarks may have been seen in training, and results may differ elsewhere.

## Influenced pages
- [Harness vs model](../../concepts/harness-vs-model.md) — HarnessTax paragraph in the dissent section

## Key claims extracted
- Harness choice moved success within about ±2% on SWE-bench Lite and about ±5% on Terminal-Bench 2.0; the same model could cost up to 5x more
- Across shared models, Claude Code cost about 2.0x Pi and 1.6x Codex on SWE-bench Lite, and 1.5x Pi on Terminal-Bench 2.0 (geometric means)
- Fable 5: 97.8% in Claude Code, 96.7% in Codex and Pi; Claude Code about twice Pi's cost at similar turn counts (15.3 vs 15.4)
- Claude Code's mean initial context is over 10x Pi's
- Pi (read, write, edit, bash) reaches the Pareto frontier on both benchmarks
- An alternative harness gave the highest success in 9 of 12 Anthropic/OpenAI model–benchmark comparisons (e.g. GPT-5.6 Sol 83.3% in Pi vs 78.9% in Codex on Terminal-Bench, at about half the cost)
```

### wiki/sources/papers/protocol-preserving-context-trimming-2026-09.md (new)

```md
---
title: 'Protocol-Preserving Context Trimming for Agentic Workflows: Benefits, Failure Regimes, and Budget Guardrails'
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-abs-260916461.md
url: https://arxiv.org/abs/2609.16461
published: 2026-09-15
ingested: 2026-11-24
domains: [agents]
---

# Protocol-Preserving Context Trimming for Agentic Workflows

Long agent runs keep growing their history, so harnesses trim it, and trimming is usually judged by how many tokens it removes. This single-author paper (read from its arXiv abstract) also checks whether the task still succeeds. It compares five strategies across retained-context levels and workflow complexity: recency, relevance, summarization, protocol-aware trimming (keep the state the workflow depends on, compress the rest) and adaptive budget guardrails.

## Influenced pages
- [Context editing](../../concepts/context-editing.md) — "Trim by protocol, not by recency" bullet

## Key claims extracted
- Conventional strategies: about 60% mean token savings, task success 66.6–77.3%, protocol adherence 85.5–88.6%
- Protocol-aware trimming: 92.2% task success; with adaptive guardrails 96.0% success, 96.3% protocol adherence, 1.0% cascading failure, 56.0% token savings
- Retaining 25% or less of context raised failure odds 10.92-fold vs 50% or more
- Critical context thresholds rise with workflow complexity
```

## Schema / vocabulary additions

None.

## Open questions

None.
