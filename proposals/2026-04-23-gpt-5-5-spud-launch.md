---
type: proposal
sources:
  - raw/articles/Introducing GPT-5.5_ OpenAI.pdf
  - raw/tweets/2026-04-23-danshipper-2047375686688473134.md
status: pending
created: 2026-04-23
---

# Proposal: GPT-5.5 launch — OpenAI announcement + Every vibe check

## Summary

OpenAI released GPT-5.5 on April 23, 2026, billing it as "our smartest and most intuitive to use model yet." It leads on Terminal-Bench 2.0 (82.7%), GDPval knowledge work (84.9%), FrontierMath, BixBench, ARC-AGI-2, and CyberGym among publicly available models. Claude Opus 4.7 retains edges on SWE-Bench Pro (64.3% vs 58.6%), MCP Atlas, FinanceAgent, and long-context graph tasks. Every's 3-week vibe check adds practitioner color: step-change on coding and writing, first OpenAI model to pull writers back from Claude in ~1 year, but Opus 4.7 still wins on plan quality and front-end/full-stack work. Two variants: GPT-5.5 (broadly available) and GPT-5.5 Pro (harder tasks, higher accuracy, Pro/Business/Enterprise in ChatGPT).

## Intended changes

- [ ] **Create** `wiki/models/gpt-5-5.md` — new model page
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — replace GPT-5.4 line with GPT-5.5 under `Frontier multimodal models`; add recent-changes entry; update `as_of`
    > **Before:** `- [[models/gpt-5-4]] — OpenAI's March frontier update looked like the strongest general-purpose reasoning / browsing / agent model in the captured source cycle, though the same coverage still gives Claude the edge on writing, personality, and design-heavy work *(as of 2026-03-08)*`
    > **After:**  `- [[models/gpt-5-5]] — OpenAI's April 2026 frontier model; leads on Terminal-Bench 2.0 (82.7%), GDPval (84.9%), FrontierMath, BixBench, ARC-AGI-2, and CyberGym; Claude Opus 4.7 leads on SWE-Bench Pro, MCP Atlas, FinanceAgent, and long-context; GPT-5.5 Pro variant available for harder tasks *(as of 2026-04-23)*`
    >
    > Add to `## Recent changes`:
    > `- [2026-04-23] GPT-5.5 released; supersedes GPT-5.4; leads knowledge work and coding speed benchmarks; Claude Opus 4.7 retains SWE-Bench Pro, MCP Atlas, FinanceAgent edges`
    >
    > Update `as_of:` to `2026-04-23`

- [ ] **Update** `wiki/models/claude-opus-4-7.md` — add competitive benchmarking note; update `as_of`
    > Add to `## Weaknesses / caveats`:
    > `- GPT-5.5 (April 2026) leads on Terminal-Bench 2.0 (82.7% vs 69.4%), GDPval, FrontierMath, and ARC-AGI-2; Opus 4.7 retains leads on SWE-Bench Pro (64.3% vs 58.6%), MCP Atlas (79.1% vs 75.3%), FinanceAgent (64.4% vs 60.0%), and long-context graph tasks; also leads on plan quality and front-end/full-stack work per practitioner vibe check (Every)`
    >
    > Add to `## Recent changes`:
    > `- [2026-04-23] GPT-5.5 released; beats Opus 4.7 on Terminal-Bench 2.0, GDPval, FrontierMath, and writing; Opus 4.7 retains SWE-Bench Pro, MCP Atlas, FinanceAgent, long-context, and planning quality edges`
    >
    > Update `as_of:` to `2026-04-23`

- [ ] **Update** `wiki/tools/codex.md` — note GPT-5.5 now powers Codex; add Fast mode; add internal-usage stat; update `as_of`
    > Add to `## Current status`:
    > `- GPT-5.5 now powers Codex across Plus/Pro/Business/Enterprise/Edu/Go plans; 400K context window`
    > `- Fast mode: 1.5× faster token generation, 2.5× cost`
    > `- OpenAI reports 85%+ of the company uses Codex every week across software engineering, finance, comms, marketing, data science, and product`
    > `- Codex was used to help optimize GPT-5.5's own inference (load balancing improvements contributed to >20% token generation speed gain)`
    >
    > Add to `## Recent changes`:
    > `- [2026-04-23] GPT-5.5 now powers Codex; Fast mode added; 85%+ internal OpenAI weekly usage reported`
    >
    > Update `as_of:` to `2026-04-23`

- [ ] **Update** `wiki/state-of/cybersecurity.md` — add GPT-5.5 to frontier cyber capabilities; add Trusted Access for Cyber; update `as_of`
    > Under `## Subcategories → Frontier model capabilities (offensive)`, add:
    > `- [[models/gpt-5-5]] — CyberGym: 81.8% (Claude Opus 4.7: 73.1%); CTF tasks (internal): 88.1%; bio/chem and cyber capabilities rated "High" under Preparedness Framework; deployed publicly with tighter classifiers rather than restricted-access-only *(as of 2026-04-23)*`
    >
    > Add new subsection or note under existing:
    > `**Trusted Access for Cyber:** OpenAI's verified-access program for defenders — organizations protecting critical infrastructure can apply at chatgpt.com/cyber for expanded GPT-5.5 cyber capabilities with fewer restrictions *(as of 2026-04-23)*`
    >
    > Add to `## Recent changes`:
    > `- [2026-04-23] GPT-5.5 leads CyberGym (81.8%) among publicly available models; OpenAI launches Trusted Access for Cyber for verified defenders; bio/chem+cyber rated High under Preparedness Framework`
    >
    > Update `as_of:` to `2026-04-23`

- [ ] **Update** `wiki/state-of/science.md` — add frontier model scientific research subcategory with GPT-5.5; update `as_of`
    > Add new subcategory:
    > ```
    > ### Frontier model scientific capabilities
    >
    > General-purpose frontier models with benchmark-validated scientific research performance.
    >
    > - [[models/gpt-5-5]] — BixBench (bioinformatics data analysis): 80.5%, leading among models with published scores; GeneBench (multi-stage genetics): 25.0% vs GPT-5.4's 19%; discovered new proof about Ramsey numbers (verified in Lean); used by researchers for gene-expression analysis, algebraic geometry, and drug discovery *(as of 2026-04-23)*
    > ```
    >
    > Add to `## Recent changes`:
    > `- [2026-04-23] GPT-5.5 leads BixBench (80.5%) and shows meaningful GeneBench gains; Ramsey number proof discovery verified in Lean; adds `Frontier model scientific capabilities` subcategory`
    >
    > Update `as_of:` to `2026-04-23`

- [ ] **Create** `wiki/sources/articles/openai-gpt-5-5-launch.md` — article source summary
    > See draft below

- [ ] **Update** `wiki/sources/tweets/danshipper-gpt-5-5-vibe-check.md` — add reference to official article as primary source
    > Add to frontmatter `sources:` field and note in body that the article is the primary canonical source

## Page drafts

### wiki/models/gpt-5-5.md (new)

````md
---
title: GPT-5.5
type: model
domains: [models, coding, agents]
subcategory: frontier-multimodal-model
tags: [openai, closed-source]
as_of: 2026-04-23
sources: [openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check]
---

# GPT-5.5

OpenAI's April 2026 frontier model, described as "our smartest and most intuitive to use model yet." Leads on terminal/command-line coding (Terminal-Bench 2.0: 82.7%), knowledge work (GDPval: 84.9%), advanced math (FrontierMath Tier 4: 35.4%), bioinformatics (BixBench: 80.5%), and abstract reasoning (ARC-AGI-2: 85.0%) among publicly available models. Claude Opus 4.7 retains edges on SWE-Bench Pro, MCP Atlas, FinanceAgent, and long-context tasks. Available in two variants: GPT-5.5 and GPT-5.5 Pro.

## Current status (as of 2026-04-23)

- Released April 23, 2026; available in ChatGPT (Plus/Pro/Business/Enterprise) and Codex (all plans); API access coming soon
- **GPT-5.5 Pro** variant available to Pro/Business/Enterprise in ChatGPT for harder tasks and higher-accuracy work
- **GPT-5.5 Thinking** available in ChatGPT for complex problems
- 400K context window in Codex; also available in Fast mode (1.5× faster, 2.5× cost)
- API pricing (coming soon): $5/M input, $30/M output; 1M context window
- Co-designed and served on NVIDIA GB200/GB300 NVL72; uses fewer tokens than GPT-5.4 for same tasks
- OpenAI reports 85%+ of the company uses Codex weekly with GPT-5.5

## Benchmark highlights vs Claude Opus 4.7 and GPT-5.4

| Benchmark | GPT-5.5 | GPT-5.4 | Claude Opus 4.7 |
|---|---|---|---|
| Terminal-Bench 2.0 | **82.7%** | 75.1% | 69.4% |
| SWE-Bench Pro (Public)* | 58.6% | 57.7% | **64.3%** |
| Expert-SWE (Internal) | **73.1%** | 68.5% | — |
| GDPval (knowledge work) | **84.9%** | 83.0% | 80.3% |
| FinanceAgent v1.1 | 60.0% | 56.0% | **64.4%** |
| MCP Atlas | 75.3% | 70.6% | **79.1%** |
| OSWorld-Verified | **78.7%** | 75.0% | 78.0% |
| BixBench | **80.5%** | 74.0% | — |
| FrontierMath Tier 4 | **35.4%** | 27.1% | 22.9% |
| ARC-AGI-2 | **85.0%** | 73.3% | 75.8% |
| CyberGym | **81.8%** | 79.0% | 73.1% |

*SWE-Bench Pro footnote: labs have noted evidence of memorization on this eval.

## Strengths

- Agentic coding: holds complex plans across hours of work; strong on multi-file refactors requiring deletion and reimagining of existing codebases (Dan Shipper: "first coding model with serious conceptual clarity")
- Knowledge work breadth: documents, spreadsheets, slide presentations, operational research
- Scientific research: leading bioinformatics benchmark; capable of multi-stage data analysis that previously took expert teams months
- Token efficiency: delivers better results with fewer tokens than GPT-5.4 for most Codex tasks
- Writing quality: first OpenAI model in ~1 year to pull writers away from Claude (per Every vibe check)
- Cybersecurity: highest CyberGym score among publicly available models (81.8%)

## Weaknesses / caveats

- Loses to Claude Opus 4.7 on SWE-Bench Pro, MCP Atlas, and FinanceAgent
- Long-context graph tasks at 1M tokens: Claude Opus 4.6 still leads (Graphwalks parents 1mil: Claude 72.0% vs GPT-5.5 58.5%)
- Loses to Opus 4.7 on plan quality, front-end/full-stack product work, and underspecified vibe coding (per Every vibe check)
- Not great writing Ruby
- Bio/chem and cyber capabilities rated "High" (not Critical) under OpenAI's Preparedness Framework; tighter classifiers deployed that may produce occasional over-refusals

## Recent changes

- [2026-04-23] Released; OpenAI calls it "smartest and most intuitive to use model yet"; leads on Terminal-Bench 2.0, GDPval, BixBench, FrontierMath, ARC-AGI-2; Claude Opus 4.7 retains SWE-Bench Pro, MCP Atlas, FinanceAgent edges

## Sources

- [[sources/articles/openai-gpt-5-5-launch]]
- [[sources/tweets/danshipper-gpt-5-5-vibe-check]]
````

### wiki/sources/articles/openai-gpt-5-5-launch.md (new)

````md
---
title: Introducing GPT-5.5 — OpenAI
type: source
source_type: article
source_file: raw/articles/Introducing GPT-5.5_ OpenAI.pdf
url: https://openai.com/index/introducing-gpt-5-5/
published: 2026-04-23
ingested: 2026-04-23
domains: [models, coding, agents, science, cybersecurity]
---

# Introducing GPT-5.5 — OpenAI

Official launch announcement for GPT-5.5. Covers model capabilities, benchmark tables across coding/professional/computer-use/tool-use/academic/cybersecurity/long-context/abstract reasoning, availability and pricing, internal OpenAI usage examples, and safety framing. Also introduces GPT-5.5 Pro (harder tasks) and GPT-5.5 Thinking (ChatGPT) variants.

## Influenced pages

- [[models/gpt-5-5]] — created; full benchmark table, strengths, pricing, availability
- [[state-of/models]] — updated frontier multimodal leader line; GPT-5.4 → GPT-5.5
- [[models/claude-opus-4-7]] — added competitive positioning
- [[tools/codex]] — GPT-5.5 now powers Codex; Fast mode; internal usage stat
- [[state-of/cybersecurity]] — GPT-5.5 CyberGym score + Trusted Access for Cyber program
- [[state-of/science]] — BixBench, GeneBench, Ramsey proof; new subcategory added

## Key claims extracted

- GPT-5.5 released April 23, 2026; "smartest and most intuitive to use model yet"
- Two variants: GPT-5.5 (broad availability) and GPT-5.5 Pro (harder tasks, Pro/Business/Enterprise in ChatGPT)
- Terminal-Bench 2.0: 82.7% (GPT-5.4: 75.1%, Claude Opus 4.7: 69.4%)
- SWE-Bench Pro: 58.6% vs Claude Opus 4.7's 64.3% (Claude leads; memorization footnote)
- GDPval knowledge work: 84.9% (Claude Opus 4.7: 80.3%)
- MCP Atlas tool use: 75.3% vs Claude Opus 4.7's 79.1% (Claude leads)
- FinanceAgent: 60.0% vs Claude Opus 4.7's 64.4% (Claude leads)
- FrontierMath Tier 4: 35.4% (Claude: 22.9%) — significant gap
- ARC-AGI-2: 85.0% (Claude: 75.8%)
- CyberGym: 81.8% (Claude Opus 4.7: 73.1%)
- BixBench: 80.5% (GPT-5.4: 74.0%); leading among published scores
- Long-context at 1M tokens (Graphwalks parents): GPT-5.5 58.5% vs Claude Opus 4.6 72.0% — Claude still leads
- 400K context in Codex; API $5/M input, $30/M output, 1M context (coming soon)
- Co-designed/trained/served on NVIDIA GB200/GB300; token-efficient vs GPT-5.4
- 85%+ of OpenAI uses Codex weekly; Finance team used it to process 24,771 K-1 forms, accelerating task by 2 weeks
- Trusted Access for Cyber: chatgpt.com/cyber, expanded cyber capabilities for verified defenders
- Bio/chem and cybersecurity capabilities rated High (not Critical) under Preparedness Framework
- Discovered new proof about Ramsey numbers (verified in Lean)
````

## Open questions

- Should I keep `[[models/gpt-5-4]]` as a demoted/superseded entry in `state-of/models.md`, or remove it entirely? (Currently proposing replacement.)
- The `Frontier model scientific capabilities` subcategory in `state-of/science.md` is new — approve addition to `wiki/_schema/subcategories.md`?
