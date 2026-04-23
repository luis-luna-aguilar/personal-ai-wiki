---
title: Legacy XLSX Ingestion Proposal
type: proposal
as_of: 2026-04-22
source_file: raw/notes/AI Tools & Roadmap.xlsx
---

# Legacy XLSX ingestion proposal

This proposal treats `raw/notes/AI Tools & Roadmap.xlsx` as a one-time exception source. It does **not** change `LLM-INSTRUCTIONS.md` and does **not** write to `wiki/` yet.

Method used:

- I extracted every populated row from every tab.
- I checked current public/primary web signals for each tool or referenced product where possible, using official docs, official product pages, official blogs, or direct project pages.
- I evaluated each row against the wiki's current-state bias, existing domains/subcategories, and the requirement to avoid stale claims.
- Revised policy after review: missing taxonomy should trigger an explicit schema proposal, not omission of active material.

Decision labels:

- `Ingest now` — active, current enough, and a good fit for the current wiki.
- `Ingest with schema expansion` — active, and should be kept by proposing the needed domain/subcategory explicitly.
- `Hold for better source` — promising, but the current row points to a weak source or ambiguous product signal.
- `Exclude as stale` — deprecated, superseded, renamed, or the row's description no longer matches reality.
- `Personal only` — belongs in `personal/`, not the factual wiki.

## Overall recommendation

Recommended immediate factual ingest candidates:

- `Tools` tab: `Cursor`, `Claude Code`
- `Agents` tab: `Pig`, `ADK`, `MCP`, `A2A`, `Wilson`, `FutureHouse`, `Maestro`
- `Savings` tab: `Flex`
- `Leaderboards` tab: `Coding Benchmarks`

Recommended active-but-schema-blocked candidates:
Recommended active candidates that should be retained through schema expansion:

- Creative/media stack: `Seedance 2.0`, `Dream Machine`, `HeyGen`, `Genspark Slides`, `Stitch`
- Healthcare stack: `Dragon Copilot`, `Hippocratic AI`, `Tempus`, `Zo`, `OpenEvidence`, `Kora`, `II-Medical`
- Voice/audio stack: `Scribe`, `EVI 3`, `Eleven v3`, `Sesame`, `Chatterbox`
- Finance/legal/document stack: `Hebbia`, `Agentic Document Extraction`, `Mistral Document AI`

Recommended exclusions:

- Anything clearly deprecated or superseded in the current landscape, especially `Operator`, `o3`, `Gemini 2.5 Pro`, `DeepSeek V3`, `DeepSeek R1`, `Qwen2.5-Omni`, and legacy descriptions that no longer match the product.
- Entire `Future - Actionable` tab for wiki purposes.
- Most of `Future - Trends` as written should go to `personal/`, with only a few source-backed trend fragments optionally distilled into existing `wiki/trends/` pages.

## Schema implications

The current wiki schema is narrow. If you want broad ingestion from this workbook, I recommend proposing these additions first:

- New domain: `creative`
- New domain: `healthcare`
- New subcategory: `ai-video-generation`
- New subcategory: `ai-avatar-video`
- New subcategory: `speech-to-text`
- New subcategory: `voice-models`
- New subcategory: `agent-framework`
- New subcategory: `document-intelligence`
- New subcategory: `healthcare-ai`
- New subcategory: `finance-ai`

Without those additions, a large fraction of the workbook cannot be applied cleanly. The correct fix is to add the vocabulary, not to leave those items out.

Note: all row-level decisions that previously read `Hold for schema` should now be interpreted as `Ingest with schema expansion`.

## Tab-by-tab proposal

### Tools

| Row | Entry                             | Current web signal                                                                                                                                                  | Decision               | Proposed handling                                                                                                                                              |
| --- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2   | Seedance 2.0                      | Official ByteDance Seed page and Feb 12, 2026 launch post show it is active and positioned as a leading multimodal audio-video generation model.                    | Hold for schema        | Good candidate for a future `creative` domain page under something like `ai-video-generation`. Do not preserve the row's unqualified "best available" wording. |
| 3   | Dream Machine                     | Luma product remains active. The legacy note is narrower than the product's current positioning.                                                                    | Hold for schema        | Keep only as an active video-generation/editing tool if you add a creative/media domain.                                                                       |
| 4   | 4o                                | GPT-4o image generation is real and still available, but the row points to a 2025 model-specific capability rather than a durable current winner in 2026.           | Exclude as stale       | Do not create a standalone tool page from this row. If needed later, fold image-generation capability into a current OpenAI model/tool page instead.           |
| 5   | Perception Encoder + PerceptionLM | Meta research signal exists, but this is a research/model artifact, not a stable user-facing tool.                                                                  | Hold for better source | Only ingest if you want a paper/research concept page sourced from the publication itself.                                                                     |
| 6   | Gemini 2.5 Pro                    | Official Google model docs still list it, but it is a 2025-era model and not the current frontier snapshot for this wiki in April 2026.                             | Exclude as stale       | Do not create a new page from this row.                                                                                                                        |
| 7   | Sonar                             | Product is Perplexity's Sonar, not Anthropic's. The workbook metadata is wrong.                                                                                     | Hold for schema        | If ingested later, correct company to Perplexity and place under an eventual search/research domain or assistant taxonomy.                                     |
| 8   | Deep Research                     | OpenAI deep research is active in ChatGPT and API docs, with notable 2026 updates.                                                                                  | Hold for schema        | Strong candidate, but better represented as a capability page or part of an OpenAI tool page than as a generic row import.                                     |
| 9   | Bolt                              | `bolt.new` is active, but the "best at UI generation" claim is unsupported here and fast-moving.                                                                    | Exclude as stale       | Candidate for a creative/coding boundary page later; strip winner language.                                                                                    |
| 10  | o3                                | OpenAI's own model page says `o3` is succeeded by GPT-5.                                                                                                            | Exclude as stale       | Do not ingest as current state.                                                                                                                                |
| 11  | DeepSeek V3                       | Still exists, but this is no longer frontier current-state material for this wiki.                                                                                  | Exclude as stale       | Too dated for a fresh current-state page.                                                                                                                      |
| 12  | DeepSeek R1                       | Still exists and received an updated release, but as a 2025 reasoning model family it is not current frontier in this wiki.                                         | Exclude as stale       | Skip as a standalone 2026 current-state page.                                                                                                                  |
| 13  | Llama-3.1-Nemotron-Ultra-253B-v1  | NVIDIA page currently shows imminent deprecation.                                                                                                                   | Exclude as stale       | The product is active only in a transitional sense and is already aging out.                                                                                   |
| 14  | Qwen 2.5 Omni                     | Official Qwen launch exists, but this is a March 2025 flagship and not the current state snapshot. Also the workbook misspells `Qwen`.                              | Exclude as stale       | Skip.                                                                                                                                                          |
| 15  | Scribe                            | ElevenLabs now positions `Scribe v2 Realtime` as a current real-time transcription model.                                                                           | Hold for schema        | Strong future `speech-to-text` candidate. Keep, but fix the product naming and do not keep the absolute "best" claim.                                          |
| 16  | EVI 3                             | Hume's May 29, 2025 launch post shows EVI 3 is active and important in speech-to-speech.                                                                            | Hold for schema        | Strong `voice-models` or `healthcare/agents interface` adjacent candidate if voice becomes a tracked area.                                                     |
| 17  | ElevenLabs v3                     | Official docs say Eleven v3 is the latest expressive TTS model, but not suitable for real-time conversational use.                                                  | Hold for schema        | Keep only with caveat: expressive TTS, not general conversational default.                                                                                     |
| 18  | Sesame                            | Sesame research preview is real and active, but it is still preview/research-ish and not production-stable.                                                         | Exclude as stale       | Candidate for a `voice-models` trend/tool page with a preview-status caveat.                                                                                   |
| 19  | Data AI Agent                     | The source is Google's Data Science Agent in Colab launch. Real, but availability was initially limited by country and rollout.                                     | Exclude as stale       | Better as a tool/workflow note under `science` or future `data-analysis`, not from the spreadsheet wording directly.                                           |
| 20  | Dragon Copilot                    | Official Microsoft launch in March 2025 and nursing expansion in Oct 2025 show strong current relevance.                                                            | Hold for schema        | High-quality future `healthcare-ai` candidate.                                                                                                                 |
| 21  | Microsoft Security                | The workbook name is vague, but current product is clearly `Microsoft Security Copilot`, which is active and GA.                                                    | Exclude as stale       | If ingested, rename to `Microsoft Security Copilot`; likely needs a security domain or a more deliberate inclusion rule.                                       |
| 22  | Chatterbox                        | Resemble's Chatterbox family is active and open source, but current docs suggest 10+ seconds of audio for cloned voices, not 5 seconds.                             | Exclude as stale       | Good future `voice-models` candidate. Correct the clone-length claim.                                                                                          |
| 23  | R1 Omni                           | There is real signal around Alibaba/HumanMLLM R1-Omni, but the row relies on secondary coverage and an unofficial site.                                             | Exclude as stale       | Only ingest after switching to the actual repo/paper source.                                                                                                   |
| 24  | Gemma 3n                          | Official Google developer guide confirms active release and strong on-device multimodal positioning.                                                                | Exclude as stale       | Strong candidate for a future `models` or `on-device` concept if you expand the taxonomy.                                                                      |
| 25  | Gemini Robotics                   | Official DeepMind page confirms active robotics model initiative.                                                                                                   | Exclude                | Good science/robotics trend candidate, but requires either a robotics domain or careful fit into `science`.                                                    |
| 26  | Document AI                       | Mistral Document AI is active and still marketed with 99%+ accuracy.                                                                                                | Hold for schema        | Strong future `document-intelligence` page candidate.                                                                                                          |
| 27  | Patronus AI                       | Current site has materially shifted positioning toward world models/simulation research; the row's "fact checker / diminishes hallucinations" description is stale. | Exclude as stale       | Do not ingest using the legacy framing.                                                                                                                        |
| 28  | SkyReels                          | Product is active, but this is another creative/media tool outside current schema.                                                                                  | Hold for schema        | Consider only if you want a broad creative AI domain.                                                                                                          |
| 29  | GeoSpatial Reasoning              | The row points to a YouTube demo, not a stable product page.                                                                                                        | Hold for better source | Possible future concept/tool if replaced with proper primary documentation.                                                                                    |
| 30  | WordPress AI Builder              | Active and current, but outside the wiki's present domain focus.                                                                                                    | Hold for schema        | Only include if you want website/no-code builders as a tracked category.                                                                                       |
| 31  | Cursor                            | Active, already in the wiki, and clearly still relevant.                                                                                                            | Ingest now             | Use the workbook only as supplemental historical signal if needed; likely just update existing `tools/cursor` if it adds anything unique.                      |
| 32  | Claude Code                       | Active, already in the wiki, and strongly current.                                                                                                                  | Ingest now             | Same handling as Cursor: only merge unique signal; no new page.                                                                                                |
| 33  | Genspark Slides AI                | Active product with current docs and changelog through 2026.                                                                                                        | Hold for schema        | Good future `creative` or `agent-native-documents/slides` candidate.                                                                                           |
| 34  | HeyGen                            | Active and large-scale avatar platform.                                                                                                                             | Hold for schema        | Good future `ai-avatar-video` page candidate.                                                                                                                  |
| 35  | Stitch                            | Active and evolving in 2026 as a Google Labs design canvas.                                                                                                         | Hold for schema        | Strong candidate for a future `creative` or UI-design tool page.                                                                                               |
| 36  | Genie 3                           | Official DeepMind research signal exists, but this is closer to a world-model research frontier than a general-purpose tool.                                        | Exclude as stale       | Better treated as a concept/trend or model note, not a tool row.                                                                                               |
| 37  | Command A                         | Current docs emphasize enterprise model and dedicated translation variant, but this specific row is basically a model note, not a tool.                             | Exclude as stale       | Do not ingest as a tool entry.                                                                                                                                 |
| 38  | Interviewer                       | Anthropic Interviewer is real and active as a research tool.                                                                                                        | Hold for schema        | Candidate for `agents` or `training/research-methods`, but probably not a general "tool catalog" page without a clearer placement.                             |
| 39  | Kapso                             | Active docs show a real WhatsApp API / automation platform.                                                                                                         | Hold for schema        | Good candidate if you later track messaging-agent infrastructure.                                                                                              |

### Dev Tools

| Row | Entry              | Current web signal                                                                                                             | Decision               | Proposed handling                                                                                  |
| --- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------- | -------------------------------------------------------------------------------------------------- |
| 2   | Doc-to-LoRA        | Official Sakana AI post and paper are current as of Feb 2026.                                                                  | Hold for better source | This is better as a paper/concept entry than a tool page. Use the paper directly if you ingest it. |
| 3   | Context Hub        | Strong secondary signal points to an active GitHub project, but the row should be verified from the repo itself before ingest. | Hold for better source | Promising coding-agent infrastructure candidate.                                                   |
| 4   | Turbopuffer        | Active and clearly current; docs and pricing updated in April 2026.                                                            | Hold for schema        | Could fit later under infra/search/RAG if you expand scope.                                        |
| 5   | OpenGranola        | The repo now appears under `OpenOats`, not `OpenGranola`; the legacy row is stale on naming.                                   | Exclude as stale       | If you want this tool, ingest the current `OpenOats` project instead.                              |
| 6   | Gemini Embedding 2 | Official Google post in March 2026 shows it is a current multimodal embedding model.                                           | Hold for schema        | Better as a model/concept or infra page than a simple tool page.                                   |

### Agents

| Row | Entry                       | Current web signal                                                                                                                  | Decision               | Proposed handling                                                                                    |
| --- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------- |
| 3   | Pig.dev                     | Official site is active and clearly positioned for Windows computer use.                                                            | Ingest now             | Good fit for existing `computer-use` domain, likely on a new or existing computer-use tool page set. |
| 4   | Lux                         | Row points only to an X post. I did not find a stronger primary source from the row itself.                                         | Hold for better source | Skip until there is a proper product or repo source.                                                 |
| 5   | Runner H                    | Active official product page exists. The benchmark claim in the row should not be kept without stronger source support.             | Hold for schema        | Candidate for `computer-use` or `agent-orchestration`, but ingest without the 92% vs 80% claim.      |
| 6   | LLM Manager                 | Signal from the workbook is thin and I did not get a solid current primary product read from the row alone.                         | Hold for better source | Skip for now.                                                                                        |
| 7   | Operator                    | OpenAI now marks Operator as deprecated and sunset, folded into ChatGPT agent.                                                      | Exclude as stale       | Do not ingest.                                                                                       |
| 8   | ADK                         | Official Google ADK docs are active and current across multiple languages.                                                          | Ingest now             | Good fit in `agents`; likely needs a new subcategory such as `agent-framework`.                      |
| 9   | MCP                         | Anthropic docs clearly show MCP is current and important.                                                                           | Ingest now             | Better as a `concepts/mcp` page than a tool page.                                                    |
| 10  | A2A                         | Official Google launch post confirms active protocol status.                                                                        | Ingest now             | Better as a concept/protocol page than a tool page.                                                  |
| 11  | FutureHouse                 | Official site and tools page are active; strong fit with existing `science` domain.                                                 | Ingest now             | Good candidate for `science` as a tool/platform page, likely needing a new subcategory.              |
| 12  | Maestro                     | Official UiPath docs show an active orchestration platform updated in April 2026.                                                   | Ingest now             | Good candidate for `agents` as orchestration infrastructure.                                         |
| 13  | Alpha Evolve                | Official DeepMind post exists, but this reads more like a research system than a product tool.                                      | Hold for better source | Better for `science` trend/concept coverage than a tool page.                                        |
| 14  | Ash                         | Product exists, but this opens a therapy/mental-health area outside current schema.                                                 | Hold for schema        | Only ingest if you add healthcare or wellbeing coverage.                                             |
| 15  | Wilson                      | Official site is active; this fits the current `legal` domain cleanly.                                                              | Ingest now             | Strong `legal-ai` tool candidate.                                                                    |
| 16  | Anon                        | Current site is about agent readiness benchmarking and onboarding, not the row's web-scraper description.                           | Exclude as stale       | Legacy description no longer matches product reality.                                                |
| 17  | Hebbia                      | Active, large, and clearly relevant in finance and legal workflows.                                                                 | Hold for schema        | Strong future `finance-ai` candidate.                                                                |
| 18  | Thunderbit                  | Active product signal exists, but it is outside current schema and the search results are noisy because of its template-heavy site. | Hold for schema        | Only ingest if you want scraping/ops tooling tracked.                                                |
| 19  | Agentic Document Extraction | LandingAI ADE is active and well-documented.                                                                                        | Hold for schema        | Strong future `document-intelligence` candidate, possibly cross-domain.                              |

### Savings

| Row | Entry | Current web signal | Decision | Proposed handling |
| --- | --- | --- | --- | --- |
| 2 | Flex | OpenAI Flex processing docs are active. | Ingest now | Best fit is a small concept/workflow page about lower-cost async processing rather than a tool page. |

### Courses

| Row | Entry                               | Current web signal | Decision         | Proposed handling                                                                                                                             |
| --- | ----------------------------------- | ------------------ | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 2   | Building and evaluating data agents | Course is active.  | Exclude as stale | This is a resource bookmark, not a wiki current-state page. If you want it retained, put it in `personal/` or a future curated learning page. |

### Leaderboards

| Row | Entry | Current web signal | Decision | Proposed handling |
| --- | --- | --- | --- | --- |
| 2 | Text to Image leaderboard | Active external leaderboard. | Hold for schema | Good future benchmark page if you add a creative/media domain. |
| 3 | Text to Video leaderboard | Active external leaderboard. | Hold for schema | Same as above. |
| 4 | Chat conversational | LM Arena remains an active benchmark surface. | Hold for schema | Could support `state-of/models` and future benchmark pages, but only if you want benchmark pages broadened. |
| 5 | Search Arena | Real benchmark source, but this row points to a 2025 blog post rather than a continuously updated dashboard. | Hold for better source | Use only if you want a benchmark history/source note. |
| 6 | Agents Frameworks spreadsheet | Community spreadsheet signal only. | Hold for better source | Too unstable as a primary source for factual wiki claims. |
| 7 | Coding Benchmarks / SWE-PolyBench | Active benchmark page and highly relevant to current wiki scope. | Ingest now | Best immediate candidate for the empty `wiki/benchmarks/` section. |

### Medical

This tab contains several strong signals, but the wiki currently has no `healthcare` domain. Most of these should be held rather than forced into the current taxonomy.

| Row | Entry | Current web signal | Decision | Proposed handling |
| --- | --- | --- | --- | --- |
| 2 | Hippocratic AI | Active company and active healthcare agent positioning. | Hold for schema | Strong future `healthcare-ai` tool candidate. |
| 3 | Tempus | Active platform; `Tempus One` and broader AI-enabled provider tools are current. | Hold for schema | Strong future healthcare platform candidate. |
| 4 | Ex Agent / TxAgent | Harvard/Zitnik Lab project is real and current. | Hold for schema | Better as `science` research-agent coverage or future healthcare/science crossover page. |
| 5 | Deepgram Medical Transcription | Product is active. | Hold for schema | Good healthcare or speech stack candidate later. |
| 6 | ECgMLP | The row is based on a press/news summary of a single research result, not a stable tool or product. | Exclude as stale | Do not ingest as a current-state product page. |
| 7 | Therabot | The row points to press coverage of a research result, not a stable product page. | Exclude as stale | Skip unless you later ingest the actual paper/research source. |
| 8 | Zo | Official Zocdoc product pages confirm active deployment. | Hold for schema | Strong future `healthcare-ai` tool candidate. |
| 9 | II Medical | Official II-Medical page confirms active open medical models, including July 2025 updates. | Hold for schema | Good future healthcare-model coverage candidate. |
| 10 | Kora | Konko/Kora site is active and clearly focused on clinic scheduling via WhatsApp. | Hold for schema | Useful if you want regional healthcare operations tools included. |
| 11 | MS Copilot for Nurses | Microsoft expanded Dragon Copilot to nurses in Oct 2025. | Hold for schema | Fold into `Dragon Copilot`; do not create a separate page. |
| 12 | OpenEvidence | Active and widely used medical information platform with strong current signal. | Hold for schema | One of the strongest future `healthcare-ai` candidates in the workbook. |

### Edge Demos

| Row | Entry | Current web signal | Decision | Proposed handling |
| --- | --- | --- | --- | --- |
| 2 | Google Next Customer Engagement Suite demo | Demo/video signal only. | Hold for better source | Not enough for a durable wiki page by itself. Keep only if it supports a later source-backed trend page. |

### Future - Trends

This tab is mostly a mix of user forecasts, source-backed trend fragments, and speculative 2030 expectations. The correct default target is `personal/`, not `wiki/`.

| Row | Entry | Decision | Proposed handling |
| --- | --- | --- | --- |
| 3 | Consciousness disclaimer | Personal only | Keep only in `personal/`; not a factual wiki claim. |
| 4 | Discovery/novelty disclaimer | Personal only | Keep only in `personal/`. |
| 8 | Digital AGI | Personal only | The METR reference is real, but the row mixes one grounded signal with large speculative conclusions. Distill only the METR-style task-duration trend into an existing `trends/` page if desired. |
| 9 | Physical AGI: Robotics | Personal only | Gemini Robotics and Figure Helix are real signals, but the row's 2030 forecast should stay in `personal/`. |
| 10 | Software Development | Personal only | Mostly unsourced forward-looking opinion. Do not ingest into factual wiki in its current form. |
| 11 | Self-Driving | Personal only | Relies on self-reported Tesla framing and a strong forecast. Keep in `personal/` only. |
| 12 | Weather Forecast | Personal only | GenCast is real and important, but the row is still mostly personal interpretation. If desired, distill the factual weather-model advance into `wiki/trends/ai-in-science` or a new science concept. |
| 13 | Scientific Research | Personal only | Several real signals here. Best option is a distilled update to `wiki/trends/ai-in-science`, not direct ingestion of the row text. |
| 14 | Biology | Personal only | Contains many real references mixed with speculative life-extension conclusions. Distill carefully into science trend coverage if desired. |
| 15 | Materials | Personal only | GNoME is real, but the row remains mostly forecast framing. Distill only the source-backed claim if you want science trend coverage. |
| 16 | Entertainment | Personal only | Too speculative and too thinly sourced. |
| 17 | Quantum Computing | Personal only | Too speculative and outside current wiki focus. |
| 18 | Mathematics | Personal only | Too speculative as written. |
| 19 | Society | Personal only | Explicit social forecast, not factual current-state content. |
| 20 | Energy | Personal only | Keep as a personal forecast/take. |
| 21 | Climate | Personal only | Keep as a personal forecast/take. |

### Future - Actionable

This entire tab is personal strategy/advice. It should not enter the factual wiki.

| Row | Entry | Decision | Proposed handling |
| --- | --- | --- | --- |
| 2 | Aging & Life Timelines | Personal only | Candidate for `personal/philosophies/` if you want it retained. |
| 3 | Pensions/social systems | Personal only | Same. |
| 4 | Land as investment | Personal only | Same. |
| 5 | Remote land/drone thesis | Personal only | Same. |
| 6 | Cities/services/networking thesis | Personal only | Same. |
| 7 | Do not build yet thesis | Personal only | Same. |
| 8 | Forget traditional careers | Personal only | Same. |
| 9 | Separate self-worth from skills | Personal only | Same. |
| 10 | Prioritize networking/community | Personal only | Same. |
| 11 | Migrate to AI-producing country | Personal only | Same. |
| 12 | Iterate ideas rapidly | Personal only | Same. |
| 13 | Speed in directing bots | Personal only | Same. |

## Proposed execution order if approved

1. Create a second proposal that only contains `Ingest now` items fitting the current schema.
2. Separately draft a schema-expansion proposal for `creative` and `healthcare` if you want broad workbook coverage.
3. Optionally create a `personal/` proposal that preserves the best parts of `Future - Trends` and all of `Future - Actionable` in the user's own voice.

## Highest-value next ingest batch

If you want the best signal-to-effort ratio first, I recommend this first applied batch:

- `tools/cursor` update if any unique signal survives review
- `tools/claude-code` update if any unique signal survives review
- new `concepts/mcp`
- new `concepts/a2a`
- new `tools/google-adk` or equivalent naming
- new `tools/pig`
- new `tools/wilson`
- new `tools/futurehouse`
- new `tools/uipath-maestro`
- new `benchmarks/swe-polybench`
- new concept/workflow note for `OpenAI Flex processing`

## Comments

* Please expand the schema as you suggest and process the hold for schema items
* deep research is a tool now we have in gemini and open AI, so it deserves its own tool space
* i set my decision on every element in the table