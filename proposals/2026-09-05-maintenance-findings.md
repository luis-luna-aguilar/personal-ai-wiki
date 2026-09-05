---
type: maintenance-report
status: pending
created: 2026-09-05
---

# Maintenance findings — 2026-09-05

Read-only analysis after applying 13 proposals. Nothing below has been changed yet. Mechanical probes (stock scripts + a custom consistency script) plus six semantic scans covering every state-of page, its linked pages, all concept/trend/training/workflow pages, sources, history, benchmarks, index and log.

**Baseline that is clean:** 0 broken links (591 pages), index accounts for all 185 live pages, 0 orphan pages, 0 pages over the 10-entry cap, superseded model pages (Opus 4.7, GPT-5.4, GLM-5.1, Kimi K2.6, MiniMax M2.7) correctly archived, most cross-page numbers agree (Opus 4.8 / Fable 5 / Grok 4.5 / GLM-5.2 pricing and scores; Glasswing counts; Erdős details; Devin recall; Deep Research figures).

---

## A. Contradictions a reader would be misled by (fix first)

| # | Where | What contradicts what | Fix |
|---|---|---|---|
| A1 | `state-of/models.md:24` vs `models/gpt-5-6-sol.md` | Dashboard: "restricted-preview flagship" *(06-26)*. Page (07-09): cleared for public rollout, $5/$30, SOTA on TB 2.1 | Rewrite line, bump to 07-09, add Recent-changes entry |
| A2 | `state-of/cybersecurity.md:85` offensive-frontier section | Still presents GPT-5.5 (04-23) as OpenAI's cyber frontier and Mythos Preview as the only Mythos-class model; `gpt-5-6-sol.md`, `claude-fable-5.md`, `openai-privacy-filter.md` all carry `cybersecurity` domain and say otherwise | Add Sol + Fable 5 leader lines, demote GPT-5.5 wording, reword Mythos "above Opus 4.7 tier" |
| A3 | `trends/restricted-frontier-deployment.md`, `trends/open-weight-momentum-broadens.md`, `concepts/agent-labs-vs-model-labs.md`, `models/glm-5-2.md:29`, `concepts/harness.md:69` | Fable 5 ban described as in force; `claude-fable-5.md` records return 07-02. Restricted-frontier's "Sol was the first resolution-toward-access" claim is therefore false | One Recent-changes entry + wording fix on each |
| A4 | `models/claude-opus-4-8.md:13` | "Fable 5 and Mythos remain restricted or unavailable" — Fable returned 07-02 | Rewrite intro |
| A5 | `state-of/models.md:37`, `models/composer-2.md` | Composer 2 is the live page/dashboard entry; `tools/cursor.md` and `models/grok-4-5.md` say Composer 2.5 superseded it in May | Create/convert to Composer 2.5, archive Composer 2 (rule 12) |
| A6 | `state-of/models.md:20,23` | Fable 5 "#1 AA Index, TB 2.1 88%" sits beside GPT-5.5 "leads on Terminal-Bench 2.0, GDPval…" — two "leads" claims side by side (rule 11); `gpt-5-5.md:21` still says "Opus 4.7 still leads on SWE-Bench Pro" in present tense | Demote GPT-5.5 to area-specific leader; re-tense |
| A7 | `benchmarks/terminal-bench.md:17` | "Frontier models score below 65%" vs GPT-5.5 82.7 (TB 2.0), Fable 5 88.0, GLM-5.2 81.0, Gemini 3.5 Flash 76.2 (TB 2.1) on their own pages; page conflates TB 2.0 / 2.1 / Hard | Rebuild leaderboard with Variant + date columns |
| A8 | `benchmarks/swe-bench.md` | Leaderboard (04-23) lists Qwen 3.6 27B as top on Pro (53.5%); missing Fable 5 80.3% and Opus 4.8 69.2% (both on `state-of/models.md`); links archived models as current | Rebuild |
| A9 | `tools/claude-code.md` | Frozen at May: heading 05-13 vs as_of 07-01; still "Opus 4.7 fast mode (now default)" (4.7 archived); never mentions Sonnet 5 / Fable 5 / Opus 4.8 although `state-of/coding.md:48` says it does; 11 Recent-changes entries, out of order | Refresh Current status to 07-08 |
| A10 | `tools/claude-managed-agents.md:13,104` | Intro/caveats: "not yet a mature product… engineering architecture post"; same page: public beta, dashboard, self-hosted sandboxes, MCP tunnels, 8 sources | Rewrite intro/caveats present-tense |
| A11 | `tools/gpt-realtime-2.md:17,41` vs `tools/gpt-live.md:18` | "ChatGPT voice upgrade coming soon / still older model" vs GPT-Live-1 became default ChatGPT Voice 07-07 | Update + Recent-changes entry |
| A12 | `concepts/agent-evals.md:22` | Heading "Five eval categories"; list has seven | Retitle or fold |
| A13 | `models/cosmos-3.md:13` | "GPT-Image-2 (Nano Banana 2)" — OpenAI and Google models conflated; two unqualified "#1 open image" claims (Cosmos on AA, Ideogram on Arena) | Fix parenthetical; qualify both with leaderboard |
| A14 | `tools/cartesia.md:35-36` | "[06-16] Sonic-3.5 launched" but "[05-23] Speech Arena #1 for Sonic-3.5" — ranked three weeks before launch; 06-16 is a newsletter-mention date | Reword |
| A15 | `state-of/models.md:28` vs `models/grok-4-5.md:13` | Predecessor named "Grok 4.20" on dashboard, "Grok 4.3" on page; Gemini 3.1 Pro and Grok 4.20 both "lead Arena creative writing" in the same May snapshot | Verify against Arena source, use one name |
| A16 | `models/claude-opus-4-8.md` | Release dated both ~05-28 (with Dynamic Workflows) and 06-03 | Settle date |
| A17 | `state-of/models.md:44` "Meta Spark" (unlinked) vs `[Muse Spark]` (linked, line 29) | Probably the same model, two entries | Merge |
| A18 | `training/ai-enablement-software-development.md` vs `training/anti-autopilot-review-friction.md` | Anthropic comprehension study: "47% drop in debugging" vs "50% vs 67%" — two secondary reports, never reconciled | Add reconciliation note, one canonical home |
| A19 | `concepts/harness.md:69` | "LangSmith Engine … fine-tuned judge, 10-100× cheaper" — appears in no source page; other pages describe it as a trace-clustering/fix-proposing engine | Source or remove |
| A20 | `tools/harvey.md` | as_of 04-02 but body/heading 06-04 (hybrid-routing results); legal dashboard and index still call it a "thin stub" | Complete the 07-06 apply |

## B. Dashboards lagging their own pages (systemic)

- **27 dashboard lines** carry an `*(as of)*` older than the linked page's `as_of` — worst: Codex on cybersecurity (03-09 vs 07-01), Cursor/Grok Build/Codex on coding, Managed Agents (04-24 vs 05-20), Devin (05-19 vs 07-14), Microsoft Copilot (04-22 vs 06-17: Cowork GA + Autopilot missing), Advisor strategy, Perplexity Computer, Muse Spark (04-10 vs 07-08), Claude Design, Claude Science. In several cases the dashboard's own Recent changes already records the newer event — the leader line was never touched.
- **3 lines newer than their page** (Mythos Preview suspension on dashboard, not on page; Genspark Slides; Claude Code).
- **Coding dashboard never absorbed Grok 4.5**; still says the joint model is "coming".
- **Both big dashboards stopped ~07-08/14** while leaf pages carry late-August claims. Today is 09-05.

## C. Tagging / vocabulary / filing

- **Undeclared subcategory:** `tools/cartesia.md` `voice-model` → `voice-models` (typo).
- **Undeclared tags (8):** `benchmark`, `labor-market` (agents-last-exam, frontiercode); `cognition` (frontiercode — worth declaring as vendor tag, then add to devin/windsurf); `competitive-dynamics`, `moats` (agent-labs); `enterprise` (databricks); `self-hosted` (paperclip); `voice` (cartesia — it's a domain, drop); `frontier` (fable-5 — subcategory covers it). Recommend: declare `cognition`, drop the rest.
- **Dead vendor tags (declared, never used):** `bytedance`, `elevenlabs`, `minimax`, `mistral`, `nousresearch` — the pages that should carry them (seedance-2, eleven-v3, elevenlabs-scribe, minimax-m3, mistral-document-ai, hermes-agent) don't.
- **`tag_compliance.py` counts example slugs in the "Categories" prose as declared** (36 vs 25 truly declared) — script gap.
- **Subcategory ↔ section misfits:** E2B is `agent-framework` but is a sandbox runtime (belongs in the new `agent-sandbox-infra`, absent from the section made for it); OpenAI Agents SDK is `agent-orchestration` but is an SDK; Gemini managed-agents line sits under Frameworks; OpenWiki under Frameworks with `agent-toolkits`; "Persistent coding agents" section on agents.md is not a schema subcategory and duplicates Hermes; Qwen 3.7 listed under Coding models with `frontier-model` frontmatter; DeepSeek V4 listed twice (Coding + Open-weight); Perplexity Computer listed twice on finance.
- **Schema rule vs reality:** `ai-assistant` and `agentic-coding-workspace` have no `agents` parent domain, yet Copilot/Gemini/Orca sit on the agents dashboard.
- **Domain ⇔ dashboard membership broken both ways:** 66 tool/model pages carry a domain whose dashboard doesn't list them (notably `claude-code`, `cursor`, `gpt-5-5`, `deepseek-v4`, `cohere-command-a-plus` on agents/coding; `impeccable`, `nano-banana-2` on creative; `gpt-5-6-sol`, `fable-5`, `privacy-filter` on cybersecurity; `mistral-document-ai`, `landingai` on finance/healthcare — the whole `document-intelligence` subcategory is on no dashboard). Conversely Devin is on cybersecurity without the domain; Codex on agents without it; GPT-Realtime-2 on models without it. **Decision needed:** are dashboards "leaders only" (then trim `domains:` on tool pages) or "everything in the domain" (then add sections)? AGENTS.md currently says the latter.
- `trends/llm-as-discovery-channel.md` has `domains: []` (required).
- 5 source pages filed in the wrong directory for their `source_type` (4 tweets + 1 newsletter under `articles/`).
- `wiki/history/tools/claude-code.md` has `type: history` (not a valid type).

## D. Index, log, docs

- **`wiki/index.md`:** 24 entries with stale `as_of` (voice trend 03-30→07-07, advisor 04-09→06-29, claude-design 05-05→07-08, deepseek-v4, terminal-bench, five state-of pages…); 3 factually stale descriptions (gpt-5-6-sol "restricted-preview", grok-build "joint model coming", harvey "thin stub"); page-count block says 178/23/11, actual 185/25/12; ~45 entries appended out of alphabetical order; unwritten "Anthropic block first" rule. → regenerate from frontmatter; extend `index_check.py` to flag `as_of` drift.
- **`wiki/log.md`:** two sort directions in one file (lines 11–150 newest-first, 151+ oldest-first; 13 inversions); 14 malformed entries (13 `schema`, 1 `apply`) missing the summary field; `spill` op used in practice but not in the allowed list.
- **Cap drift 5 vs 10:** `config.yml` says 10; "5" survives in `MAINTENANCE.md:19,29,31,104`, `AGENTS.md:181,227`, `manual/config-reference.html:75`.
- **Source-page frontmatter template vs reality:** 161/216 newsletter pages have no `url`; 35 article pages from the 04-22/23 deep-research batch have no `source_file` *and no body sections at all*; 4 pages use a list for `source_file` (undocumented; scripts may not resolve it); 2 tweet pages point to a profile instead of a status permalink (`brockman-model-not-product`, `mcp-2026-07-28-stateless-rc`).
- **One source page per raw file — undocumented convention conflict:** 24 newsletter raw files have 2–4 source pages each (one per signal). Today's apply doctrine says one page per raw file. Pick one rule and write it down. One genuine tweet duplicate: `agent-html-artifacts-2026-05-13` / `agent-review-artifacts-2026-05-13`.
- **3 orphaned source pages** (`ii-medical`, `meta-ads-mcp-cli-2026-04-30`, `opus-47-reels-us-back-in`); 2 source pages built on unfetched stubs.
- **History files:** three different archive-block orders across files; 4 files with headerless preambles; entries within blocks unsorted; one `[2025-10-15]` typo (should be 2026-04-09); archived model pages use two different "superseded" conventions.
- **`raw/` hygiene:** 230 `fetched: false` stubs (mostly `tco-*` redirects), 12 `-1.md` duplicate fetches, 62 fetched files referenced nowhere, **34 raw files cited by applied proposals that never got the promised source page**.
- **Benchmarks:** GAIA / OSWorld / WebArena / ToolBench are placeholder pages ("verify against leaderboard", single deep-research source, cited nowhere); tau-bench, swe-polybench, swe-marathon have no scores.

## E. Redundancy and sedimentation (concept/trend/training layer)

- `concepts/harness.md` (2,713 words) and `workflows/agentic-orchestration-patterns.md` (3,344 words, no `## Related`) are near-duplicates — a dozen verbatim-equivalent pattern bullets — and **do not link each other**.
- `training/company-wide-ai-enablement.md` (3,762 words) and `trends/agents-reshape-organizations.md` (1,677) share nine sources, duplicate Ramp/McKinsey/Claudie/AI-sandwich/OpenClaw material, and **do not link each other**; neither has inbound links from content pages.
- Same idea in 3–5 homes: Every's frame/framer + human sandwich (5 pages); model neutrality/sovereignty (4, near-identical sentence on 3); cost/token governance (3); cognitive debt (4); skills methodology (3–4); Hoop/Nadella/compound loop (2–3); eval mechanics incl. verbatim LLM-as-judge subsection (3); three autonomy ladders unreconciled on 2 pages.
- Zero-inbound content pages: `agent-labs-vs-model-labs`, `cost-aware-ai-task-routing`, `ai-delegation-management`, `a2a`, `agentic-thinking` (1), `prompt-injection` (stub while the "lethal trifecta" lives on anti-autopilot).
- Trend openers overtaken by their own bullets: open-weight-momentum ("by early April… Gemma 4"), voice ("late-March signal"), restricted-frontier (open question answered by its own Sol section), agents-reshape, compute-infrastructure (title says "decisive moat", half the bullets are counterforces; still carries 05-05 agent-runtime entries that belong on agent-native-compute).
- Bloat vs 300-word guideline: harness 2.7k, agent-evals 1.7k, agents-reshape 1.7k, agent-improvement-loop 1.5k; training essays company-wide 3.8k, ai-enablement-sw 2.8k, evals-sw 2.4k. Recent-changes sections on the hubs read as ingest changelogs.
- Dormant: healthcare and legal dashboards + 9 tool pages sit at 04-22 from the legacy workbook; finance carries two "pending verification" items since 05-06; `spec-driven-development` subcategory (3 tools) at 2025-10-15.

## F. Mechanical (batchable)

- 17 pages: `## Current status (as of X)` ≠ frontmatter `as_of` (claude-code, codex, claude-design, harvey, kimi-code, shopify, muse-spark, gpt-5-5, qwen-3-6-27b, qwen-3-6-35b, fable-5, glm-5-2, advisor-strategy, agent-improvement-loop, knowledge-layer, quantization, proprietary-data).
- 15 pages: Recent changes not newest-first (claude-code, codex, microsoft-copilot, claude-cowork, claude-science, company-wide, state-of/coding, state-of/computer-use, state-of/healthcare, opus-4-8, glm-5-2, sonnet-5, agents-last-exam, spec-driven-development, knowledge-layer).
- 5 pages: Recent-changes entry newer than `as_of` (claude-code, harvey, composer-2, swe-bench, knowledge-layer).
- 19 pages: frontmatter `sources:` ids with no matching `## Sources` link (worst: state-of/cybersecurity 11 ids, company-wide 8, state-of/computer-use 7); 21 source pages whose "Influenced pages" targets don't cite them back.
- 8 forward-looking claims to verify (qwen-3-7 "not yet released", grok-4-5 context "expected to be restored", gpt-5-5 "API coming soon", expired Codex/Notion promos still in Current status).
- 1 frontmatter YAML error: `sources/newsletters/end-of-finetuning-debate-2026-05-13.md` (unquoted title with quotes).
- `models/cosmos-3.md`, `models/ideogram-4.md`: `## Sources` links use `../../sources/` (resolves outside wiki) — link_check missed it because the target path exists relative to the vault root? Verify.
- 44 unlinked bold dashboard entries; several page-worthy (Gray Swan, TML-Interaction-Small, ESMFold2, AI Co-Mathematician, Figma Agent, Grok Imagine Agent); some misfiled (Gemini Magic Pointer under voice; Veo 3.1 under image; Genesis AI robotics on science).

---

## Root causes

1. **Apply never re-touched dashboards/index when leaf pages moved.** Proposals updated the tool page and added a Recent-changes entry but left the leader line's `*(as of)*` and text alone. → make "bump every dashboard line that links the updated page" an apply-time rule, and have `index_check.py` flag `as_of` drift.
2. **Newsletter clusters fanned out as full paragraphs to 3–5 pages** instead of one home + links. → enforce "one canonical page per idea; elsewhere one sentence + link" at proposal time.
3. **Warnings in proposals were read but the mechanical fixes weren't applied** (heading/as_of, ordering, Sources sync). Today's rebase doctrine now handles ordering/caps/sources at apply time; the backlog needs one normalization pass.
4. **Two undocumented conventions** (multi-page-per-newsletter; index ordering) and one stale number (cap 5) in the manuals.

## Suggested sequence

1. **Commit the 13 applied proposals now** — nothing found above was introduced by today's batch (the only new-page issues are pre-existing conventions: Cartesia typo, source-page-per-signal).
2. **Proposal M1 — truth fixes (A1–A20)**: one proposal, page drafts per item, so you can approve/skip individually.
3. **Proposal M2 — dashboard sync**: bump the 27 lagging lines + 3 reverse cases + Grok 4.5 on coding + index regeneration + log re-sort.
4. **Proposal M3 — vocabulary & filing**: the decisions in section C (leaders-only vs everything-in-domain; declare `cognition`; drop 7 tags; refile E2B/Agents SDK/OpenWiki; Persistent-agents section; document-intelligence on finance/healthcare).
5. **Proposal M4 — consolidation**: harness/orchestration split; company-wide/agents-reshape wiring; one home each for frame/framer, sovereignty, cost governance, cognitive debt, skills; trend-opener refresh.
6. **Script + doc fixes** (no proposal needed): cap 5→10 in 7 places; `tag_compliance.py` declared-list parsing; `index_check.py` as_of drift; add `spill` op; document source-page convention; `raw/` stub quarantine policy.
