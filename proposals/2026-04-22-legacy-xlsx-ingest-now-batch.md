---
title: Legacy XLSX Expanded Ingest Batch
type: proposal
as_of: 2026-04-22
source_file: raw/notes/AI Tools & Roadmap.xlsx
---

# Legacy XLSX expanded ingest batch

This is the narrowed follow-up to [2026-04-22-legacy-xlsx-ingestion-proposal.md](./2026-04-22-legacy-xlsx-ingestion-proposal.md).

Revised rule for this batch:

- taxonomy gaps are **not** a reason to leave out active material
- when a current item does not fit the existing schema, the correct move is to **propose the schema expansion explicitly**

Goal: define the first batch that should be ingested from `raw/notes/AI Tools & Roadmap.xlsx`, including the schema additions required to do it cleanly.

## Proposed schema additions first

These additions unlock the highest-value active items from the workbook and avoid forcing unrelated tools into awkward categories.

### New domains

- `creative` — media generation, design tools, slides, avatar/video products
- `healthcare` — clinical, medical, provider, and healthcare operations AI

### New subcategories

- `agent-framework`
- `science-agent-platform`
- `speech-to-text`
- `voice-models`
- `ai-video-generation`
- `ai-avatar-video`
- `ui-generation`
- `document-intelligence`
- `healthcare-ai`
- `finance-ai`
- `messaging-agent-infrastructure`
- `multimodal-embedding-model`

## First applied batch after schema approval

This is the revised high-priority batch. It includes items that were previously held back only because the current vocabulary was too narrow.

### Concepts and protocols

- `wiki/concepts/mcp.md`
- `wiki/concepts/a2a.md`

Why:

- both are protocol-level concepts
- both already influence multiple tool ecosystems
- both have strong primary-source documentation

### Agents / developer infrastructure

- `wiki/tools/google-adk.md`
- `wiki/tools/pig.md`
- `wiki/tools/uipath-maestro.md`
- `wiki/tools/futurehouse.md`

Suggested mappings:

- `Google ADK` → domains: `[agents]`, subcategory: `agent-framework`
- `Pig` → domains: `[computer-use]`, subcategory: `computer-use`
- `UiPath Maestro` → domains: `[agents]`, subcategory: `agent-orchestration`
- `FutureHouse` → domains: `[science, agents]`, subcategory: `science-agent-platform`

Why:

- `ADK` is active and important enough that taxonomy should bend to it, not the reverse
- `FutureHouse` is one of the strongest science-agent signals in the workbook
- `Pig` and `Maestro` already fit cleanly and should remain in the first batch

### Legal / finance / document workflow

- `wiki/tools/wilson.md`
- `wiki/tools/hebbia.md`
- `wiki/tools/landingai-agentic-document-extraction.md`
- `wiki/tools/mistral-document-ai.md`

Suggested mappings:

- `Wilson` → domains: `[legal]`, subcategory: `legal-ai`
- `Hebbia` → domains: `[finance]`, subcategory: `finance-ai`
- `LandingAI Agentic Document Extraction` → domains: `[agents, finance]` or `[agents]`, subcategory: `document-intelligence`
- `Mistral Document AI` → domains: `[agents]`, subcategory: `document-intelligence`

Why:

- these are active products with durable workflow relevance
- document extraction / structured document understanding is clearly underrepresented in the current wiki

### Healthcare

- `wiki/tools/dragon-copilot.md`
- `wiki/tools/hippocratic-ai.md`
- `wiki/tools/tempus.md`
- `wiki/tools/zo.md`
- `wiki/tools/open-evidence.md`
- `wiki/tools/kora.md`
- `wiki/models/ii-medical.md` or `wiki/tools/ii-medical.md` after final classification

Suggested mappings:

- most of these map to domains: `[healthcare]`, subcategory: `healthcare-ai`

Why:

- this is one of the densest clusters of active products in the workbook
- several entries, especially `Dragon Copilot` and `OpenEvidence`, are strong enough that omitting them would distort the user's long-term knowledge base

### Voice / speech

- `wiki/tools/elevenlabs-scribe.md`
- `wiki/tools/hume-evi-3.md`
- `wiki/tools/eleven-v3.md`
- `wiki/tools/sesame.md`
- `wiki/tools/resemble-chatterbox.md`

Suggested mappings:

- `Scribe` → domains: `[agents]` or `[healthcare, agents]`, subcategory: `speech-to-text`
- `EVI 3`, `Eleven v3`, `Sesame`, `Chatterbox` → domains: `[agents]`, subcategory: `voice-models`

Why:

- voice has already emerged as a real cross-cutting interface trend in the existing wiki
- these entries are active and materially different from each other

### Creative / media

- `wiki/tools/seedance-2.md`
- `wiki/tools/dream-machine.md`
- `wiki/tools/heygen.md`
- `wiki/tools/genspark-slides.md`
- `wiki/tools/stitch.md`

Suggested mappings:

- `Seedance 2.0`, `Dream Machine` → domains: `[creative]`, subcategory: `ai-video-generation`
- `HeyGen` → domains: `[creative]`, subcategory: `ai-avatar-video`
- `Stitch` → domains: `[creative]`, subcategory: `ui-generation`
- `Genspark Slides` → domains: `[creative]`, subcategory: `agent-native-documents` or a new `slides-generation` if you want more precision

Why:

- these are active products and the workbook clearly treats them as important
- the only reason they were not in the first narrow batch was schema insufficiency

### Benchmarks and workflows

- `wiki/benchmarks/swe-polybench.md`
- `wiki/workflows/flex-processing.md`

Why:

- both fit immediately and remain worth doing

## Items that remain excluded even after schema expansion

These remain excluded for substantive reasons, not taxonomy reasons:

- `Cursor` — already covered; workbook adds no meaningful new signal
- `Claude Code` — already covered; workbook adds no meaningful new signal
- `Operator` — deprecated/sunset
- `o3` — superseded
- `DeepSeek V3` / `DeepSeek R1` / `Gemini 2.5 Pro` / `Qwen2.5 Omni` — too stale relative to the current wiki standard
- `Anon` — row description no longer matches current product positioning
- `Patronus AI` under the workbook's old "fact checker" framing — stale framing
- `OpenGranola` as named — stale naming; should be revisited via the current project name instead

## Existing pages that should stay as-is

- [cursor.md](/Users/luis/Obsidian/AI%20Wiki/wiki/tools/cursor.md)
- [claude-code.md](/Users/luis/Obsidian/AI%20Wiki/wiki/tools/claude-code.md)

## Proposed source handling

Because this is a one-off spreadsheet ingest rather than a normal article/paper/repo flow, I recommend:

- create one lightweight source summary page for the workbook exception
- cite that source page only for "this tool was present in the legacy workbook"
- use primary web sources for the actual factual claims in any applied pages

Proposed source page:

- `wiki/sources/notes/legacy-ai-tools-roadmap-xlsx.md`

## Apply order

1. Approve schema additions
2. Add source summary page for the workbook exception
3. Add protocol/concept pages: `mcp`, `a2a`
4. Add agent/platform pages: `google-adk`, `pig`, `uipath-maestro`, `futurehouse`
5. Add vertical workflow pages: `wilson`, `hebbia`, `landingai-agentic-document-extraction`, `mistral-document-ai`
6. Add healthcare pages
7. Add voice/speech pages
8. Add creative/media pages
9. Add `benchmarks/swe-polybench.md`
10. Add `workflows/flex-processing.md`
11. Update `wiki/index.md`
12. Update any affected `state-of/` pages or create new ones if the new domains are approved

## Recommendation

Approve the schema additions and this expanded first batch together. The earlier "current-schema only" framing was too conservative for this wiki's intended evolution.
