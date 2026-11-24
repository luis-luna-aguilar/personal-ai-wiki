---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-11-23
sources: [cursor-3-launch, advisor-strategy, stripe-cli, managed-agents, agentic-thinking-lin, curiosity-driven-imagination, openai-agents-sdk-evolution, ainews-2026-04-21, ainews-2026-04-22, claude-cowork-launch, every-managed-agents-vibe-check, claude-design-launch, orca-homepage, anthropic-platform-expansion-april-2026, coding-agent-control-planes, claude-productivity-surfaces, open-agent-orchestration-late-march, proof-agent-native-documents, cursor-cloud-agents-march, cursor-cloud-agents-february, google-adk, openai-deep-research, gemini-deep-research-max, futurehouse-homepage, uipath-maestro-introduction, anthropic-mcp, google-a2a, legacy-ai-tools-roadmap-xlsx, microsoft-foundry-agents-2026, google-cloud-next-2026, superhuman-2026-04-23, awsai-cowork-bedrock-2026-04-23, microsoft-copilot-agent-mode-office, claude-managed-agents-memory, agentic-devops-deep-research, agent-infrastructure-harness-2026-05-01, codex-for-work-2026-05-01, ai-managed-orchestration-local-browser-agents-2026-04-28, inference-inflection-agent-runtime-2026-04-30, persistent-cloud-computers-agents-2026-05-01, production-agent-orchestration-2026-04-29, hermes-openclaw-persistent-agents-2026-05-11, metr-long-horizon-2026-05-12, thinking-machines-interaction-2026-05-12, frontier-labs-deployment-services-2026-05-13, multica-repo, notion-external-agents-api-may-2026, langchain-interrupt-may-2026, devin-auto-triage-2026-05, papercliping, ainews-june-06-2026, vercel-agents-new-software-2026-07-03, ainews-not-much-happened-2026-07-02, the-code-devin-security-2026-07-02, claude-tag-slack-agent-2026-06, claude-cowork-mobile-2026-07, gemini-managed-agents-2026-07, kimi-goal-mode-creative-agents-2026-06, railway-agent-native-cloud-2026-05-20, daytona-giving-agents-computers-2026-05-21, modal-agent-experience-2026-07-08, ainews-new-ai-infra-unicorns-2026-05-22, chatgpt-work-launch-2026-08-04, ainews-spacexai-grok-46-and-grok-bot-2026-08-13, mastra-ai-mastra-2026-09-09, deeplethe-utopia-2026-09-09, expand-fetch-launch-2026-10, harness2-recursive-harnessing-2026-10, devinai-blog-introducing-devin-oncall, helixdb-helix-foundry-2026-10-19, ainews-pi-10-pi-durable-2026-10-02, latent-space-stacklok-mecatl-2026-10-07, ainews-meta-connect-2026-09-24, every-copilot-seat-in-org-chart-2026-09-25, ainews-openai-devday-2026-dots-2026-09-30, every-chatgpt-operating-system-dots-2026-10-04, latent-space-claude-dynamic-workflows-2026-10-12, claude-cowork-is-now-claude-2026-09-16, claudeai-cowork-chat-merge-2026-09-16, digitalocean-managed-agents-public-preview-2026-09-22, fabio-rovai-open-ontologies-2026-10-28, palantir-autoresearch-fine-tuning-ontology-2026-10-24, devinai-bots, vercel-board-launch-2026-11-18]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

_Coding-agent leadership is tracked in [Coding](../state-of/coding.md). This page only includes coding-adjacent systems when they are also relevant as agent orchestration, framework, or deployment surfaces._

## Subcategories

### Agent orchestration

Platforms, surfaces, and patterns for running, supervising, or routing AI agents — spanning hosted runtimes, human-supervision UIs, and multi-model coordination within a single agentic task.

- [Claude app](../tools/claude-app.md) (formerly Claude Cowork) — Anthropic; delegated knowledge-work agent, merged with chat into one Claude app (Pro/Max rollout from 2026-09-16, Enterprise GA 2026-10-23): long-running and scheduled work from any conversation, with Claude Docs, Slides, and Design in the same thread *(as of 2026-10-23)*
- [Kimi Work](../tools/kimi-code.md) — Moonshot AI desktop agent companion to Kimi Code; Goal Mode keeps work running until a user-defined objective is reached, with progress tracking and redirection *(as of 2026-06-19)*
- [Claude Tag](../tools/claude-tag.md) — Anthropic; Slack-native multiplayer agent product where Claude joins selected channels as a named participant with chosen channel/tool/data/codebase access, async thread work, and in-channel team review *(as of 2026-06-24)*
- [Codex](../tools/codex.md) (ChatGPT Work) — OpenAI; Work runs on the Codex harness inside a persistent cloud microVM and connects to Slack, email, Drive, calendars, CRMs, and a 1,000+-entry plugin directory; reportedly crossed 10M users (with Codex) three weeks after its July 9 launch, and OpenAI has confirmed Work will merge into regular Chat by year-end *(as of 2026-08-04)*
- [Grok Bot](../tools/grok-bot.md) — xAI/SpaceXAI; "AI teammates with their own cloud computers" launched alongside Grok 4.6; tool/service login, Slack and GitHub Actions monitoring, scheduled routines, bot-spawning *(as of 2026-08-13)*
- [ChatGPT dots](../tools/chatgpt-dots.md) — OpenAI; always-on GPT-6 Astra agents, each with its own Linux cloud computer, 4,000+ connectors, Slack/Teams presence and do-alone / ask-first / never rules; early reviews find it useful but unreliable *(as of 2026-10-04)*
- [Devin Bots](../tools/devin-bots.md) — Cognition; engineering-focused AI teammates that split a goal across parallel Devin sessions, each on its own VM, until the PRs are mergeable; reachable by text, Slack or phone, with schedules, triggers and bot-to-bot handoff *(as of 2026-11-23)*
- [Meta Muse](../tools/meta-muse.md) — Meta; free consumer personal agent on Muse Spark 1.3 with its own email address, Mac computer use, 1,500+ connectors and glasses integration; passed ChatGPT in the App Store *(as of 2026-09-24)*
- [Orca](../tools/orca.md) — open-source desktop surface for supervising multiple coding agents across isolated worktrees, with live status, diff review, and CI visibility *(as of 2026-04-21)*
- [Claude Managed Agents](../tools/claude-managed-agents.md) — Anthropic's hosted runtime; separates session, harness, sandbox, and file-backed memory; self-hosted sandboxes and MCP tunnels; dynamic workflows ("flows", public beta) let a lead agent write its own orchestration across up to 1,000 subagents *(as of 2026-10-12)*
- [Claude Platform](../tools/claude-platform.md) — Anthropic's developer platform; linked billing (beta) replaces shared API keys with per-platform spend limits *(as of 2026-11-17)*
- [Microsoft Copilot](../tools/microsoft-copilot.md) — Microsoft; one Copilot app (Home, Code, Autopilot) since September 2026; Autopilot agents are named, persistent, and sit in the org chart under their owner, with enterprise permissions as both safeguard and blocker *(as of 2026-09-25)*
- [Microsoft Foundry Hosted Agents](../tools/microsoft-foundry-agents.md) — Microsoft; hosted runtime with per-session VM isolation, persistent filesystems, Entra Agent ID governance, MCP Toolbox, and multi-framework support *(as of 2026-04-23)*
- [UiPath Maestro](../tools/uipath-maestro.md) — enterprise orchestration for agents, robots, and people; stronger fit for operational process flows than pure research workloads *(as of 2026-04-22)*
- [Multica](../tools/multica.md) — open-source; vendor-neutral managed agents platform; assign GitHub-style issues to agent CLIs (Claude Code, Codex, Copilot, and 8 others); Squads for leader-delegated routing; reusable skill compounding *(as of 2026-05-18)*
- [Paperclip](../tools/paperclip.md) — open-source (MIT), self-hosted; org-chart model: agents get titles, reporting lines, monthly budgets, and heartbeat schedules; Kubernetes deployment for hosted agents; governance keeps humans as the board of directors; 69.9k GitHub stars *(as of 2026-06-10)*
- [Vercel Board](../tools/vercel-board.md) — Vercel; experimental headless task board for agent fleets across harnesses: claims with leases, task dependencies, watchers, Slack/GitHub two-way sync, per-board grants; v0's factory on it merges over 50% of PRs *(as of 2026-11-18)*
- [Advisor strategy](../workflows/advisor-strategy.md) — small executor drives the loop, escalates to a frontier advisor only when stuck; +2.7% SWE-bench Multilingual at −11.9% cost vs. the frontier model alone, externally validated by Harvey on legal tasks *(as of 2026-06-29)*
- [Devin](../tools/devin.md) — Cognition; parent/child fan-out across products: Oncall Responders (successor to Auto-Triage) dispatch fresh-context investigations from an alert stream, and Security Swarm (Agentic MapReduce) applies the same pattern to vulnerability discovery and fix PRs *(as of 2026-10-19)*

### Agent frameworks

SDKs and development kits for building custom agents with tools, multi-agent patterns, and runtime scaffolding.

- [Gemini](../tools/gemini.md) / Gemini API managed agents — Google; hosted managed-agent interface with MCP support, background execution, custom function calling, credential refresh, and Interactions API statefulness *(as of 2026-07-08)*
- [Google ADK](../tools/google-adk.md) — Google; open-source ADK now positioned as the developer layer inside Gemini Enterprise Agent Platform; Agent Studio adds a low-code wrapper, and Model Garden expands the surrounding stack to 200+ models *(as of 2026-04-23)*
- [Hermes Agent](../tools/hermes-agent.md) — NousResearch; open-source; brain+muscle architecture (separate reasoning and execution layers); Kanban supervision dashboard, weekly automated skill pruning, local-first memory, and 118 bundled skills *(as of 2026-05-13)*
- [LangChain / LangSmith](../tools/langchain-langsmith.md) — LangChain; open-source agent framework and observability platform; LangSmith Engine closes the trace→improvement loop automatically; SmithDB is a purpose-built agent-trace database *(as of 2026-05-15)*
- [eve](../tools/eve.md) — Vercel; prescriptive agent framework built around model/provider switching, fallbacks, resumability, filesystem agents, skills, compaction, subagents, sandboxes, long-running jobs, observability, and evals *(as of 2026-07-03)*
- [OpenAI Agents SDK](../tools/openai-agents-sdk.md) — model-native harness with native sandbox execution, durable checkpoint / rehydration, and provider-neutral manifests *(as of 2026-04-15)*
- **OpenClaw** — viral open-source framework (345K stars); deep messaging-app integrations; **security advisory (May 2026):** 341 malicious registry entries planted in coordinated attack; Microsoft recommends enterprise customers avoid on work machines *(as of 2026-05-13)*
- [Mastra](../tools/mastra.md) — YC-backed open-source TypeScript agent framework; model routing across 40+ providers, graph-based workflow engine alongside the agent abstraction, human-in-the-loop suspend/resume, Observational Memory, MCP server authoring *(as of 2026-09-09)*
- [Harness²](../tools/harness2.md) — Google Cloud AI Research; open-source research framework that refines an agent's harness per task without an answer key and keeps a cross-task lessons library *(as of 2026-10-09)*
- [Pi](../tools/pi.md) — Earendil; open-source minimal coding harness that Flue and Prime Agent build on; Pi 1.0 plus Pi Durable, a checkpointed rewrite that resumes after crashes *(as of 2026-10-06)*
- [Mecatl](../tools/mecatl.md) — Stacklok; open-source "cloud-native harness" that separates the agent loop from client, model provider, state store, and execution so enterprises can run and govern sessions centrally *(as of 2026-10-07)*

### Deep research tools

Longer-horizon research agents that plan, search, read, synthesize, and return multi-step research outputs rather than answer in one pass. See [Deep Research (concept)](../concepts/deep-research.md) for the category concept.

- [OpenAI Deep Research](../tools/openai-deep-research.md) — OpenAI's productized deep research agent; available via ChatGPT and API *(as of 2026-04-22)*
- [Gemini Deep Research](../tools/gemini-deep-research.md) — Gemini Deep Research and Deep Research Max; most fully benchmarked public implementation (93.3% DeepSearchQA, 85.9% BrowseComp on Max tier); MCP support for internal data *(as of 2026-04-22)*

### Agent web data extraction

APIs that fetch, clean, and extract web pages for agents, so agents read sites that don't serve agent-native formats. See [Agent-readable web](../concepts/agent-readable-web.md) for the publisher side.

- [Expand Fetch](../tools/expand-fetch.md) — URL → Markdown via a trained page-reading model (Iris), plus hidden-JSON extraction, citable snapshots, Crawl and WebSync; vendor-run benchmark puts it ahead of Exa and Firecrawl *(as of 2026-10-14)*

### Agentic DevOps

Agent-compatible infrastructure tools and control planes for provisioning, diagnosing, operating, and verifying live systems through repeatable, auditable interfaces.

- [Stripe CLI](../tools/stripe-cli.md) — early provisioning/control-plane example: provision services across providers, sync credentials back to the environment, and manage upgrades or billing from a CLI designed for humans or agents *(as of 2026-04-09)*
- [Kagent](../tools/kagent.md) — Kubernetes-native agent runtime / governance layer with MCP tool servers, tracing, and human-in-the-loop control *(as of 2026-04-24)*
- [K8sGPT](../tools/k8sgpt.md) — Kubernetes diagnosis and triage surface that turns cluster problems into agent-usable plain-English context *(as of 2026-04-24)*
- [Skyflo](../tools/skyflo.md) — approval-gated AI control layer for Kubernetes and CI/CD; strongest current example of explicit mutate-with-approval ops design *(as of 2026-04-24)*
- [Checkly](../tools/checkly.md) — outside-in post-deploy verification via synthetic monitoring and Playwright-based checks *(as of 2026-04-24)*
- [Devin](../tools/devin.md) — Cognition; Devin Oncall (GA) investigates and mitigates production alerts and incidents with a review agent and per-org memory and skills; 100% end-to-end on SREGym-Lite *(as of 2026-10-19)*

### Agent sandbox / compute infrastructure

Managed compute providers whose core product is execution environments purpose-built for agents: instant-start, stateful, isolated sandboxes and agent-operable cloud primitives that scale from zero to tens of thousands of concurrent instances for background-agent and RL/eval workloads. See [Agent-native compute infrastructure](../trends/agent-native-compute.md) for the trend view.

- [Daytona](../tools/daytona.md) — bare-metal sandboxes on its own scheduler; ~60ms startup, 50K sandboxes in ~75s, largest customer ~850K/day; RL/eval now ~50% of usage; Windows/macOS computer-use sandboxes in progress *(as of 2026-05-22)*
- [Modal](../tools/modal.md) — serverless AI cloud reframing from developer to "agent experience"; 100K-sandbox RL rollouts, sidecars, 17-cloud capacity pool; $355M Series C *(as of 2026-07-08)*
- [Railway](../tools/railway.md) — bare-metal deployment platform with copy-on-write production forks, progressive rollouts, and a CLI-first agent interface *(as of 2026-05-20)*
- [E2B](../tools/e2b.md) — isolated sandbox runtime for AI agents; disposable Linux VMs exposed as a programmable execution layer via SDK; command execution, SSH/terminal access, persistence/snapshots, BYOC deployment *(as of 2026-04-24)*
- [DigitalOcean Managed Agents](../tools/digitalocean-managed-agents.md) — public preview; runs your own harness (Claude Code, Codex CLI, OpenCode) in pausable Firecracker microVMs billed on active CPU, with an MCP gateway that keeps credentials out of the sandbox *(as of 2026-09-22)*
- [NVIDIA OpenShell](../tools/nvidia-openshell.md) — NVIDIA; open-source, self-run runtime sandbox for local and open agents rather than a managed provider; 100+ firms joined its safety platform; telemetry on by default *(as of 2026-09-30)*

### Agent-native documents

Document surfaces built for humans and agents to collaborate inside the same working artifact, with revision, provenance, and comments happening in-place instead of around pasted AI output.

- [Proof](../tools/proof.md) — Every's web document editor is the clearest current example of the "agent-native document" thesis: plans, memos, and working docs are treated as shared human/AI artifacts with provenance, comments, and tracked edits built into the document itself *(as of 2026-03-15)*
- [Notion](../tools/notion.md) — Notion; External Agents API lets Claude Code, Cursor, Codex, Devin, Warp, and Decagon operate directly inside Notion as a shared context layer; Workers run in secure sandbox; CLI; free through August 2026 on Business/Enterprise *(as of 2026-05-14)*
- [ChatGPT Space](../tools/chatgpt-space.md) — OpenAI; ChatGPT-native docs, slides and spreadsheets shared by humans and agents, with dots tagged in comments; framed as OpenAI's answer to Notion and the office suite *(as of 2026-10-04)*
- [ChatGPT Pages](../tools/chatgpt-pages.md) — OpenAI; companion shared human/agent surface launched with Space and dots; sources do not yet describe it apart from Space *(as of 2026-09-30)*

### Knowledge platforms

- [OpenWiki](../tools/openwiki.md) — LangChain; maintained codebase documentation layer for agents, a team-scope knowledge layer *(as of 2026-07-02)*
- [Utopia](../tools/utopia.md) — DeepLethe; open-source bitemporal knowledge graph and ontology engine, air-gapped one-binary deployment, agent harness over MCP; marketed as an "enterprise world model" *(as of 2026-09-09)*
- [Helix Foundry](../tools/helix-foundry.md) — HelixDB; open-source local-first data workspace that matches records across a company's databases and SaaS tools into one graph (marketed as "one ontology") and answers with cited SQL; installed by a coding agent *(as of 2026-10-19)*
- [Open Ontologies](../tools/open-ontologies.md) — Tesseract Semantics; open-source (MIT) change control for production ontologies: semantic plan with blast radius, apply, rollback, and derivation certificates a Lean 4 checker re-verifies; MCP server *(as of 2026-10-28)*

### Autonomous research agents

Agents that close the full research loop end-to-end — reading literature, collecting data, running experiments, evaluating results, and iterating — with minimal human steering between steps.

- [HF ml-intern](../tools/hf-ml-intern.md) — Hugging Face; open-source ML post-training research loop agent; reads papers, collects datasets, launches training jobs, evaluates, and iterates; GPQA 10% → 32% in <10 hours on Qwen3-1.7B *(as of 2026-04-22)*
- [Palantir AutoResearch](../tools/palantir-autoresearch.md) — Palantir; closed post-training agent inside Palantir Foundry that trains models on an institution's own operational records and keeps datasets, recipes and weights as owned assets (the "Fine-Tuning Ontology") *(as of 2026-10-24)*

### Science agent platforms

Platforms built to support literature-driven or discovery-oriented scientific work, without necessarily closing the full autonomous experiment loop end to end.

- [FutureHouse](../tools/futurehouse.md) — science-agent platform aimed at research and discovery workflows, distinct from generic chat assistants with science demos *(as of 2026-04-22)*

## Recent changes

- [2026-11-23] Added [Devin Bots](../tools/devin-bots.md) to Agent orchestration, joining Grok Bot, Claude Tag and ChatGPT dots in the AI-teammate category: a persistent Bot splits a goal across parallel Devin sessions and brings only approvals, blockers and decisions back to the user.
- [2026-11-18] Added [Vercel Board](../tools/vercel-board.md) to Agent orchestration: Vercel's experimental headless coordination layer where agents from different harnesses claim leased tasks, wait on dependencies and sync with Slack and GitHub.
- [2026-10-28] Added [Open Ontologies](../tools/open-ontologies.md) to Knowledge platforms: open-source plan/apply/rollback for production ontologies, with derivation certificates an auditor can re-check offline.
- [2026-10-24] Added [Palantir AutoResearch](../tools/palantir-autoresearch.md) to Autonomous research agents: post-training on an institution's own Foundry records, with datasets and weights kept as licensable assets.
- [2026-10-23] Claude Cowork merged with chat into one Claude app (Pro/Max from 2026-09-16, Enterprise GA 2026-10-23); its leader line now points to the renamed [Claude app](../tools/claude-app.md) page.
- [2026-10-19] Added [Helix Foundry](../tools/helix-foundry.md) to Knowledge platforms: HelixDB's local-first data workspace that joins a company's data sources into one graph and answers with SQL cited to versioned snapshots.
- [2026-10-19] Devin added to Agentic DevOps: Devin Oncall (GA) investigates and mitigates production incidents, 100% end-to-end on SREGym-Lite; the Agent orchestration line now names Oncall Responders as Auto-Triage's successor.
- [2026-10-14] Added `Agent web data extraction` subcategory with [Expand Fetch](../tools/expand-fetch.md): agent-oriented fetch API with trained Markdown (Iris) and hidden-JSON (X-Ray) models; vendor-run MDBench 74.1% vs Exa 55.3%, Firecrawl 27.2%.
- [2026-10-12] Claude Managed Agents dynamic workflows ("flows") enter public beta: the lead agent writes its own orchestration program, up to 1,000 subagents per run; Devin shipped the same pattern as Dynamic Workflows a day later.
- [2026-10-09] Added [Harness²](../tools/harness2.md) to Agent frameworks: Google's open-source recursive harnessing framework, frozen weights, up to +11.5 points on WorkBuddy-Bench.
