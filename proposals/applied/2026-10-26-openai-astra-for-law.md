---
type: proposal
source: raw/articles/2026-10-26-openaicom-index-astra-for-law.md
sources:
  - raw/articles/2026-10-26-openaicom-index-astra-for-law.md
  - raw/tweets/2026-10-26-harvey-2100680142297424117.md
status: pending
created: 2026-10-26
---

# Proposal: OpenAI launches Astra for Law; Harvey builds on it

## Summary

### In short

A frontier lab now sells its own legal AI and still supplies the legal-AI companies. OpenAI's Astra for Law combines GPT-6 Astra with a U.S. legal search index, built-in legal-writing instructions and firm-grade controls. On a legal-research benchmark it passed 54.0% of questions, against 38.7% for plain Astra with web search. Harvey launched a ChatGPT Enterprise plugin the same day and says it will build on the configuration. The proposal adds an Astra for Law page and updates Harvey, State of Legal and GPT-6 Astra. Reason to hesitate: filing a model configuration as a tool is a judgment call.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

On 17 September OpenAI introduced Astra for Law. It is a configuration, not a new model: GPT-6 Astra plus a legal search index, plus instructions for legal analysis and writing. The index covers U.S. case law, statutes, regulations, court rules and administrative decisions across more than 230 million URLs. It includes the Free Law Project's CourtListener collection, which holds over 99.9% of published U.S. precedential case law. OpenAI tested on 200 questions from the private validation set of Vals AI's Legal Research Bench. At the highest reasoning effort, Astra for Law passed the correctness check on 54.0% of questions, against 38.7% for GPT-6 Astra using only web search. It also found 24% more reference cases. In two side-by-side memo examples, Claude Fable 5.1 cited a holding that had been reversed on appeal, and in the other said it found no matching case.

Access starts with selected law firms through a Trusted Access Program in ChatGPT and Codex. The API, as `gpt-6-astra-law`, is "coming soon". Eligible firms get Zero Data Retention, and Latham & Watkins is helping design ethical walls and permissions. OpenAI's forward-deployed engineers built firm-specific tools, such as Sullivan & Cromwell's agreement analyzer and Cooley's IPO-filing assistant. The launch also includes 26 partner plugins, among them iManage, Relativity, Clio and Thomson Reuters. Harvey's same-day thread says its ChatGPT Enterprise plugin lets lawyers reach Harvey from ChatGPT, and that Harvey will build on the new configuration in its own products.

### What changes

The wiki's legal coverage is three tools, last updated in June, with Harvey known mainly for a model-routing benchmark.

- New page `tools/astra-for-law.md` covers the configuration, the benchmark results, access and controls, the plugin ecosystem, the firm builds, and why the lab-as-vendor-and-supplier position matters.
- **State of Legal** adds an Astra for Law leader line and extends the Harvey line with the plugin. It gets a Recent-changes entry, and its page date moves to 17 September.
- **Harvey** gains a status bullet on the plugin and on building on Astra for Law, an updated coverage caveat, and a Recent-changes entry. Its page date moves to 17 September.
- **GPT-6 Astra** gets one Recent-changes entry pointing to the new page. Its date stays 19 October.
- The index gains one tool line and updates two others. Two new source pages are added.

### What to weigh

Astra for Law is filed as a `legal-ai` tool rather than a model, because OpenAI describes it as a model plus tools plus instructions. The comment replies below Harvey's thread, which debate whether Harvey is being "cooked", are left out as opinion.

## Intended changes

- [ ] **Create** `wiki/tools/astra-for-law.md` — new legal-AI configuration from OpenAI; no existing page
    > See draft below

- [ ] **Update** `wiki/state-of/legal.md` — add an Astra for Law line under `### Legal AI` and extend the Harvey line; add one Recent-changes entry dated 2026-09-17 at the top; append two source ids and two Sources links; `as_of` 2026-06-04 → 2026-09-17
    > See draft below

- [ ] **Update** `wiki/tools/harvey.md` — one sentence added to the lead, one Current-status bullet, status heading to 2026-09-17, refreshed coverage caveat; add one Recent-changes entry dated 2026-09-17 at the top; append two source ids and two Sources links; `as_of` 2026-06-04 → 2026-09-17
    > See draft below

- [ ] **Update** `wiki/models/gpt-6-astra.md` — add one Recent-changes entry dated 2026-09-17 (between the 2026-10-19 and 2026-09-08 entries); append one source id and one Sources link; `as_of` unchanged (2026-10-19)
    > See draft below

- [ ] **Update** `wiki/index.md` — add the `tools/astra-for-law` line; update the `tools/harvey` and `state-of/legal` lines; tools count +1, total +1
    > See draft below

- [ ] **Create** `wiki/sources/articles/openai-astra-for-law-2026-09-17.md` — source summary for OpenAI's launch post

- [ ] **Create** `wiki/sources/tweets/harvey-astra-for-law-plugin-2026-09-17.md` — source summary for Harvey's thread

## Page drafts

### wiki/tools/astra-for-law.md (new)

```
---
title: Astra for Law
type: tool
domains: [legal]
subcategory: legal-ai
tags: [openai, closed-source]
as_of: 2026-09-17
sources: [openai-astra-for-law-2026-09-17, harvey-astra-for-law-plugin-2026-09-17]
---

# Astra for Law

OpenAI's legal configuration of [GPT-6 Astra](../models/gpt-6-astra.md): the model plus a legal search index, built-in instructions for legal analysis and writing, and governance controls for law firms. Firms use it directly in ChatGPT and Codex, and legal-tech companies such as [Harvey](harvey.md) and Legora build their own products on it.

## Current status (as of 2026-09-17)

- Launched 2026-09-17 for selected law firms through a Trusted Access Program in ChatGPT and Codex ("GPT-6 Astra Law" in the model picker); API access as `gpt-6-astra-law` is "coming soon". OpenAI says it will carry the legal settings forward to later frontier models.
- **Legal search index:** U.S. case law, statutes, regulations, court rules, and administrative decisions across 230M+ URLs, updated daily, including Free Law Project's CourtListener collection (over 99.9% of published U.S. precedential case law). Positioned as a complement to licensed content such as Thomson Reuters.
- **Research results:** on 200 questions from the private validation set of Vals AI's Legal Research Bench, at the highest reasoning effort, 54.0% passed the overall correctness check vs. 38.7% for GPT-6 Astra with web search alone; 24% more reference cases found on case-law questions; up to 54% more relevant passages retrieved from the correct opinions.
- **Precedent matching:** in OpenAI's two side-by-side memo examples, Astra for Law returned closely matching precedents, while Claude Fable 5.1 cited a holding reversed on appeal (litigation) and reported no matching case (transactional).
- **Controls:** Zero Data Retention on the API for eligible firms; ChatGPT Enterprise usage excluded from human review by default; information permissions, ethical walls, client instructions, and firm oversight being designed with Latham & Watkins.
- **Ecosystem:** 26 partner-built plugins (including iManage, Intapp, DeepJudge, Relativity, Clio, Harvey, and Thomson Reuters HighQ with a coming CoCounsel Legal connector), 9 community plugins carrying 47 adaptable skills (LegalQuants, LECG, Skills.law), and ChatGPT for Word generally available.

## Firm builds

OpenAI's forward-deployed engineers adapted ChatGPT Enterprise with custom interfaces and proprietary-data integrations for individual firms (see [Forward-deployed engineering](../training/forward-deployed-engineering.md)): Sullivan & Cromwell's agreement analyzer applies the firm's negotiating playbooks and precedents to a new deal, spots risks that appear when provisions are read together, and drafts redlines and client advice; Ropes & Gray's diligence system works through a data room and traces findings to source, such as customer contracts that require notice or consent; Cooley's GO Public supports IPO preparation and carries deal changes across the filing. Wachtell, Lipton, Rosen & Katz is working with OpenAI's research and engineering teams on legal judgment.

## Why it matters

A frontier lab is now both a vendor in legal AI and the supplier to legal-AI specialists. Harvey ships a plugin inside ChatGPT Enterprise and also builds on Astra for Law in its own products, so the question for specialists becomes what they add on top of the lab's own legal configuration: workflow, matter context, governance, or proprietary content. OpenAI frames its approach as "open and composable", meant to grow the ecosystem rather than replace it.

## Weaknesses / caveats

- The benchmark comparison is against GPT-6 Astra with web search, not against Harvey, CoCounsel, or other legal-AI products, and uses Vals AI's private validation set.
- Access is limited to selected firms at launch, and the API has no date.
- The search index covers U.S. law only.

## Recent changes

- [2026-09-17] Launched for selected firms in ChatGPT and Codex: GPT-6 Astra plus a U.S. legal search index, legal instructions, firm controls, and 26 partner plugins; 54.0% vs. 38.7% on Vals AI Legal Research Bench validation questions.

## Sources

- [Introducing Astra for Law (OpenAI)](../sources/articles/openai-astra-for-law-2026-09-17.md)
- [Harvey (@harvey) — Harvey plugin for Astra for Law in ChatGPT Enterprise](../sources/tweets/harvey-astra-for-law-plugin-2026-09-17.md)
```

### wiki/state-of/legal.md (updated)

Frontmatter: `as_of: 2026-09-17`; `sources:` append `openai-astra-for-law-2026-09-17, harvey-astra-for-law-plugin-2026-09-17`.

Under `### Legal AI`, replace the Harvey line and add the Astra for Law line directly after it:

> **Before:** `- [Harvey](../tools/harvey.md) — legal AI platform; June 2026 hybrid-routing benchmark shows a GLM 5.1 + Opus 4.7 advisor combination reaching an 18% all-pass rate at ~60% lower cost than pure Opus 4.7 (14% all-pass) *(as of 2026-06-04)*`

```
- [Harvey](../tools/harvey.md) — legal AI platform; June 2026 hybrid-routing benchmark shows a GLM 5.1 + Opus 4.7 advisor combination reaching an 18% all-pass rate at ~60% lower cost than pure Opus 4.7 (14% all-pass); since 2026-09-17 also a ChatGPT Enterprise plugin, building on Astra for Law *(as of 2026-09-17)*
- [Astra for Law](../tools/astra-for-law.md) — OpenAI; GPT-6 Astra plus a U.S. legal search index, legal-writing instructions, and firm controls; 54.0% vs. 38.7% (Astra with web search) on Vals AI Legal Research Bench validation questions; selected firms first, API coming *(as of 2026-09-17)*
```

In `## Recent changes`, insert at the top:

```
- [2026-09-17] Added [Astra for Law](../tools/astra-for-law.md) under `Legal AI`: OpenAI's legal configuration of GPT-6 Astra, offered to firms directly and as a foundation for Harvey and Legora; Harvey line notes its new ChatGPT Enterprise plugin.
```

Append to `## Sources`:

```
- [Introducing Astra for Law (OpenAI)](../sources/articles/openai-astra-for-law-2026-09-17.md)
- [Harvey (@harvey) — Harvey plugin for Astra for Law in ChatGPT Enterprise](../sources/tweets/harvey-astra-for-law-plugin-2026-09-17.md)
```

### wiki/tools/harvey.md (updated)

Frontmatter: `as_of: 2026-09-17`; `sources:` append `openai-astra-for-law-2026-09-17, harvey-astra-for-law-plugin-2026-09-17`.

Append to the lead paragraph:

```
Since September 2026 it also sits on top of, and inside, OpenAI's legal stack: a Harvey plugin runs in ChatGPT Enterprise, and Harvey builds on OpenAI's [Astra for Law](astra-for-law.md) configuration.
```

Rename `## Current status (as of 2026-06-04)` to `## Current status (as of 2026-09-17)` and add as its last bullet:

```
- **OpenAI partnership (2026-09-17):** Harvey's plugin inside ChatGPT Enterprise lets lawyers reach Harvey from ChatGPT, and Harvey will build on [Astra for Law](astra-for-law.md) in its own products. Harvey's Head of Applied Research, Niko Grupen, said early Astra for Law testing showed strength in grounding answers in on-point authorities, precise citation, and practical advisory guidance.
```

In `## Weaknesses / caveats`, replace the second bullet:

> **Before:** `- Source coverage remains limited — the April 2026 page creation and June 2026 benchmark are the only two ingested data points`

```
- Source coverage remains limited: the April 2026 post, the June 2026 benchmark, and the September 2026 OpenAI partnership are the ingested data points
```

In `## Recent changes`, insert at the top:

```
- [2026-09-17] Launched a Harvey plugin inside ChatGPT Enterprise and said it will build on OpenAI's Astra for Law configuration in its own products.
```

Append to `## Sources`:

```
- [Introducing Astra for Law (OpenAI)](../sources/articles/openai-astra-for-law-2026-09-17.md)
- [Harvey (@harvey) — Harvey plugin for Astra for Law in ChatGPT Enterprise](../sources/tweets/harvey-astra-for-law-plugin-2026-09-17.md)
```

### wiki/models/gpt-6-astra.md (updated)

Frontmatter: `sources:` append `openai-astra-for-law-2026-09-17`. `as_of` unchanged.

In `## Recent changes`, insert between the `[2026-10-19]` and `[2026-09-08]` entries:

```
- [2026-09-17] OpenAI launched [Astra for Law](../tools/astra-for-law.md), a legal configuration of GPT-6 Astra (legal search index, legal-writing instructions, firm controls); 54.0% vs. 38.7% for Astra with web search on Vals AI Legal Research Bench validation questions.
```

Append to `## Sources`:

```
- [Introducing Astra for Law (OpenAI)](../sources/articles/openai-astra-for-law-2026-09-17.md)
```

### wiki/index.md (updated)

Under `## State of`, replace the `state-of/legal` line:

```
- [state-of/legal](state-of/legal.md) — current state of AI in legal practice *(as_of: 2026-09-17)*
```

Under `## Tools`, replace the `tools/harvey` line and add the Astra for Law line directly after it:

```
- [tools/harvey](tools/harvey.md) — legal AI platform; June 2026 hybrid-routing benchmark shows a cost/accuracy win over pure-Opus routing; ChatGPT Enterprise plugin and builds on Astra for Law (Sept 2026) *(as_of: 2026-09-17)*
- [tools/astra-for-law](tools/astra-for-law.md) — OpenAI's legal configuration of GPT-6 Astra: U.S. legal search index, legal-writing instructions, firm controls, 26 partner plugins; 54.0% vs. 38.7% on Vals AI Legal Research Bench validation questions *(as_of: 2026-09-17)*
```

Under `## Page count`: `tools` +1 and `Total content pages` +1 (from the live values at apply time).

### wiki/sources/articles/openai-astra-for-law-2026-09-17.md (new)

```
---
title: Introducing Astra for Law (OpenAI)
type: source
source_type: article
source_file: raw/articles/2026-10-26-openaicom-index-astra-for-law.md
url: https://openai.com/index/astra-for-law/
published: 2026-09-17
ingested: 2026-10-26
domains: [legal]
---

# Introducing Astra for Law (OpenAI)

OpenAI's launch post for Astra for Law, a configuration of GPT-6 Astra with a U.S. legal search index, legal analysis and writing instructions, and law-firm controls, offered to firms in ChatGPT and Codex and as a foundation for legal-tech companies.

## Influenced pages

- [Astra for Law](../../tools/astra-for-law.md) — new page
- [State of Legal](../../state-of/legal.md) — new leader line
- [Harvey](../../tools/harvey.md) — builds on Astra for Law; Grupen quote
- [GPT-6 Astra](../../models/gpt-6-astra.md) — legal configuration

## Key claims extracted

- Astra for Law = GPT-6 Astra + legal search index + instructions for legal analysis and writing; API customers including Harvey and Legora can build on it; legal capabilities to carry to later frontier models
- Index: U.S. case law, statutes, regulations, court rules, administrative decisions; 230M+ URLs, sources added daily; Free Law Project / CourtListener covering >99.9% of published U.S. precedential case law; complements licensed content (Thomson Reuters)
- Vals AI Legal Research Bench, 200 private-validation questions, highest reasoning effort: 54.0% overall correctness pass vs. 38.7% for GPT-6 Astra with web search (40% relative); 24% more reference cases on case-law questions; up to 54% more relevant passages at equal effort
- Side-by-side examples: Claude Fable 5.1 returned a holding reversed on appeal (litigation) and found no case (transactional); Astra for Law returned two closely matching precedents
- Access: selected law firms via Trusted Access in ChatGPT and Codex ("GPT-6 Astra Law"); API `gpt-6-astra-law` coming soon
- Controls: ZDR on the API for eligible firms; ChatGPT Enterprise excluded from human review by default; Latham & Watkins collaboration on permissions, ethical walls, client instructions, oversight
- FDE-built firm tools: Sullivan & Cromwell agreement analyzer, Ropes & Gray deal diligence system, Cooley GO Public; Skadden and Wachtell named
- 26 partner plugins (iManage, Intapp, DeepJudge, Relativity, Clio; Thomson Reuters HighQ and a forthcoming CoCounsel Legal connector); 9 community plugins with 47 skills (LegalQuants, LECG, Skills.law); ChatGPT for Word generally available
```

### wiki/sources/tweets/harvey-astra-for-law-plugin-2026-09-17.md (new)

```
---
title: 'Harvey (@harvey) — Harvey plugin for Astra for Law in ChatGPT Enterprise'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-harvey-2100680142297424117.md
url: https://x.com/harvey/status/2100680142297424117
published: 2026-09-17
ingested: 2026-10-26
domains: [legal]
---

# Harvey (@harvey) — Harvey plugin for Astra for Law in ChatGPT Enterprise

Harvey's same-day thread supporting OpenAI's Astra for Law launch. Replies largely debate whether OpenAI's move threatens Harvey; those are opinion and not extracted.

## Influenced pages

- [Harvey](../../tools/harvey.md) — ChatGPT Enterprise plugin, builds on Astra for Law
- [State of Legal](../../state-of/legal.md) — Harvey line

## Key claims extracted

- Harvey's plugin within ChatGPT Enterprise gives lawyers a new way to access Harvey directly from ChatGPT
- With the plugin, Harvey will also build on the new legal configuration, bringing its capabilities into Harvey's products
```

## Schema / vocabulary additions

None.

## Open questions

- Astra for Law is filed as a `legal-ai` tool. The alternative is a model page under `domain-specialized-model`, but that subcategory's definition says "fine-tuned" and lists no `legal` parent domain, so it would need a schema change. Keep it as a tool (assumed)?
	- Its a tool
