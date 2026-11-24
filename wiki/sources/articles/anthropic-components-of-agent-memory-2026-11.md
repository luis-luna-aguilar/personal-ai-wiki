---
title: Anthropic — The components of agent memory
type: source
source_type: article
source_file: raw/articles/2026-11-23-anthropiccom-research-components-of-agent-memory.md
url: https://www.anthropic.com/research/components-of-agent-memory
ingested: 2026-11-24
domains: [agents]
---

# Anthropic — The components of agent memory

Anthropic research post on how Claude writes, corrects and organizes memory, with "dreaming" (an offline pass that reviews memory against session transcripts) as the consolidation step. It reports evals on CL-Bench 1.0, Pokémon Red, a Stainless internal-document corpus, a merger Q&A set and Harvey's LAB legal benchmark, and closes with open design questions. The page carries no date; it was forwarded on 2026-11-07, which the wiki uses as its date.

## Influenced pages
- [Agent memory](../../concepts/agent-memory.md) — new "How agents write memory, and dreaming" section
- [Knowledge layer](../../concepts/knowledge-layer.md) — dreamed-wiki bullet
- [Knowledge term map](../../concepts/knowledge-term-map.md) — the agent-memory definition's exclusion of compaction, cited in the context-editing row

## Key claims extracted
- Agent memory = knowledge gained from experience and retained between sessions as readable context; excludes weights, in-context learning and compaction
- CL-Bench 1.0: Sonnet 4.6 untested theories; Opus 4.7 consolidated notes; Sonnet 5 marked confirmed answers; Opus 5 first to close the loop with validated rules; Opus 5.5 and Sonnet 5.5 match it
- Pokémon Red at ~10,000 steps: Sonnet 3.7 413 files / 225 folders / 1 badge; Fable 5 nine files in two folders plus `global.md` / 4 badges; Opus 5.5 beat the game with a small memory folder
- Telling the model memory exists beats prescriptive rules; "record only failures" removed much of Opus 5's and Opus 4.7's gain; prompting Sonnet 4.6 to read memory and test theories nearly doubled its score; Sonnet 5 reads memory unprompted 9 of 10 times
- Dreaming corrected a wrong Mt. Moon note; the uncorrected run never reached Cerulean City
- Stainless corpus (~350k files, ~420M tokens): dreamed wiki 13%→48% of criteria over 2→128 sessions; wiki + search 61% vs 53% search alone; ~20k tokens saved per question
- Merger Q&A: wiki 87% vs search 73%; one LAB task no gain; on another the wiki grew larger than the documents
- Self-reflection loop on wiki instructions: brief from 72% (41/57 facts) to 100%
- Claude Code auto memory loads only the first 200 lines or 25 KB of `MEMORY.md`
- Cookbooks published for dreaming with a dynamic workflow and for knowledge wikis
