---
title: State of Coding
type: state-of
domains: [coding]
tags: []
as_of: 2026-08-03
sources: [sdd-3-tools-fowler, cursor-3-launch, stripe-cli, claude-code-monitor, openai-pro-100, cursor-pr-demos, shopify-ai-toolkit, cursor-bugbot-learning, claude-code-routines, openai-codex-ongoing-tasks, orca-homepage, coding-agent-control-planes, claude-code-leak-architecture, cursor-3-orchestration-bet, skills-and-plugin-packaging-late-march, cursor-cloud-agents-march, claude-code-scheduled-tasks-march, codex-security-march, agentic-devops-deep-research, cursor-sdk-agent-runtime-2026-04-30, symphony-devin-terminal-orchestration-2026-04-28, end-of-finetuning-debate-2026-05-13, claude-code-goal-fastmode-fleetview-2026-05-13, claude-code-agent-view-2026-05-13, model-harness-fit-2026-05-13, agent-first-ide-convergence-may-2026, dynamic-workflows-claude-code, fable-ban-june-2026, spacex-cursor-june-2026, ainews-frontiercode-june-2026, ainews-not-much-happened-2026-07-02, every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-code-getting-started-with-loops-2026-06-30, claude-sonnet-5-official-2026-06-30, cursor-ios-mobile-app-2026-06, devinai-blog-windsurf-adaptive, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, every-copilot-studio-microsoft-2026-08-03]
---

# State of Coding

Current state of AI tools for software development. Organized by subcategory — each subcategory can have multiple top players. Ambiguity is expected.

## Subcategories

### Spec-driven development

Tools where a structured natural-language spec is the primary input to AI coding agents. The term is contested and the field is early — no clear leader. See [Spec-Driven Development (SDD)](../concepts/spec-driven-development.md) for the concept and taxonomy.

- [Kiro](../tools/kiro.md) — VS Code-based; requirements → design → tasks; lightest-weight, mostly spec-first *(as of 2025-10-15)*
- [spec-kit](../tools/spec-kit.md) — GitHub; CLI scaffolder + slash commands; constitution → specify → plan → tasks; most customizable *(as of 2025-10-15)*
- [Tessl Framework](../tools/tessl.md) — CLI + MCP server; only tool pursuing spec-as-source; private beta *(as of 2025-10-15)*

### Agentic coding workspace

Coding tools whose primary UI is built around managing one or more AI coding agents (local and cloud), rather than file-centric editing with AI assistance bolted on.

- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK exposes the runtime headlessly; iOS beta adds mobile launch/control for always-on cloud and desktop agents; acquired by SpaceX ($60B, June 2026); Cursor Origin launched for agent-native code hosting; Grok 4.5, the jointly trained SpaceXAI/Cursor model, launched July 2026 and is available across all Cursor surfaces; version 3.11 adds side chats for parallel research without interrupting the main agent *(as of 2026-07-13)*
- [ZCode](../tools/zcode.md) — Z.ai's official GLM-5.2 coding workspace; converts open coding model momentum into a first-party product surface for long-running coding sessions *(as of 2026-07-02)*
- [Orca](../tools/orca.md) — Open-source worktree IDE for running Claude Code, Codex, and other coding agents side by side with built-in terminals, file review, diff review, and CI/PR status tracking *(as of 2026-04-21)*
- **GitHub Copilot App** (technical preview) — GitHub; desktop surface for parallel workstreams, PR/repo lifecycle management, and model flexibility; agent-first rather than IDE-first *(as of 2026-05-15)*
- **VS Code Agents window** — Microsoft; multi-agent, multi-project workflows from one window; browser/mobile access via vscode.dev/agents; BYOK and compressed terminal output *(as of 2026-05-15)*
- [Windsurf](../tools/windsurf.md) — Cognition (Devin's parent); Adaptive model router auto-selects models to conserve quota at a flat per-token rate; transparent per-token pricing in the model picker; Max plan daily limits removed *(as of 2026-07-14)*

### Agentic DevOps

Tools that move AI coding systems closer to full software delivery by covering provisioning, diagnosis, deployment safety, and post-deploy verification rather than code generation alone.

- [Stripe CLI](../tools/stripe-cli.md) — provisioning-first example: agent-compatible CLI for standing up and managing app-stack services across providers *(as of 2026-04-09)*
- [K8sGPT](../tools/k8sgpt.md) — diagnosis surface for Kubernetes-heavy software teams; useful when coding-agent output needs operational interpretation and triage *(as of 2026-04-24)*
- [Skyflo](../tools/skyflo.md) — strongest current example of approval-gated execution for infrastructure mutations triggered from natural-language operational intent *(as of 2026-04-24)*
- [Checkly](../tools/checkly.md) — post-deploy verification layer that turns Playwright/browser checks into continuous synthetic validation *(as of 2026-04-24)*

### Terminal coding agent

CLI-based AI coding agents that still anchor in the terminal, but are increasingly expanding into supervised workspaces with repeatable workflows, background execution, and broader agent control surfaces.

- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows; now supports Sonnet 5 as a broadly available agentic default while Fable 5 remains the high-capability but fallback-routed tier, making model-routing resilience part of the coding-agent operating model; most-used AI coding tool at 63% of respondents per Pragmatic Engineer's May 2025-Feb 2026 developer survey *(as of 2026-08-03)*
- [Codex](../tools/codex.md) — OpenAI; folded into a new ChatGPT desktop "superapp" (Chat/Work/Codex modes) in July 2026, drawing power-user backlash; usage reportedly grew from ~6-7M to an estimated 10M users within a week of the GPT-5.6 Sol launch; remote SSH GA; parallel subagents keep the main context clean on independent task parts *(as of 2026-08-03)*
- [Grok Build](../tools/grok-build.md) — xAI; early beta CLI coding agent; plan mode (step-by-step diff review); parallel subagents in isolated git worktrees; SuperGrok Heavy subscribers only; Grok 4.5 launched July 2026 as the default model — Coding Agent Index 76, on par with GPT-5.5 in Codex *(as of 2026-07-08)*
- [Kimi Code](../tools/kimi-code.md) — Moonshot AI; open-source; 1-line CLI; video-as-coding-context; ACP support; IDE integration; powered by Kimi K2.7-Code model; companion Kimi Work desktop agent added Goal Mode for long-running tasks that continue until the objective is reached *(as of 2026-06-19)*
- [Devin](../tools/devin.md) — Cognition; Devin Fusion (preview) multi-model "sidekick" harness matches frontier performance at 35% lower cost (41% with Fable 5) on FrontierCode Extended; Security Swarm's Agentic MapReduce architecture now documented, reporting 72% recall on a CVE-pinned vulnerability benchmark *(as of 2026-07-14)*

### Agent toolkits

Toolkits that package a developer platform's docs, schemas, validation, and related capabilities for AI coding tools via plugins, skills, or MCP.

- [Shopify AI Toolkit](../tools/shopify-ai-toolkit.md) — Shopify packages platform docs, API schemas, and validation for Claude Code, Codex, Cursor, Gemini CLI, and VS Code via plugin, skills, or local Dev MCP; Codex support is skills/MCP only; reframed as an example of "agent-ready SaaS" — product context and actions packaged for user-chosen external agents *(as of 2026-06-29)*

## Recent changes

- [2026-08-03] Codex usage reportedly grew from ~6-7M to ~10M users within a week of the GPT-5.6 Sol launch; Pragmatic Engineer's May 2025-Feb 2026 survey found Claude Code the most-used AI coding tool at 63% of respondents, with GitHub Copilot losing the category lead it held since inventing it in 2021; separately, an Every hands-on account described Microsoft's Copilot Studio (no-code agent builder, distinct from the consumer Copilot app and GitHub Copilot) as capable but confusingly onboarded — secondary account, mostly paywalled.
- [2026-07-14] OpenAI folded Codex into a ChatGPT "superapp" (Chat/Work/Codex modes), drawing power-user backlash but reaching an estimated 6-7M users, ~10x growth year-to-date; Anthropic countered with a Claude Code browser, a third Fable 5 access extension, and higher Claude Code limits; Cursor 3.11 added side chats.
- [2026-07-14] Windsurf (Cognition) shipped Adaptive model router, transparent per-token pricing in the model picker, and removed daily quota limits for Max users.
- [2026-07-02] Fable 5 returned to coding-tool surfaces; Sonnet 5 testing reinforced cost-per-completed-task as a better routing metric than token list price.
- [2026-07-02] Z.ai launched ZCode for GLM-5.2, a signal that open coding models are building product ecosystems around long-context workflows rather than competing only as checkpoints.
- [2026-06-30] Cursor iOS beta adds mobile launch/control for always-on cloud agents and desktop agents.
- [2026-06-30] Official Sonnet 5 launch confirms Claude Code availability and `claude-sonnet-5` API access.
- [2026-06-30] Anthropic published a Claude Code loop taxonomy tying task type to primitives: turn-based prompts, `/goal`, `/loop` or `/schedule`, and proactive routines composed with skills, dynamic workflows, and auto mode.
- [2026-06-29] Devin Fusion (preview): multi-model "sidekick" harness matches frontier performance at 35% lower cost on FrontierCode Extended; Devin added to the Terminal coding agent subcategory alongside the newly documented Agentic MapReduce architecture.
- [2026-06-17] SpaceX acquires Cursor ($60B all-stock); Cursor Origin launched (agent-native git/code hosting); jointly trained xAI model coming to both Cursor and Grok Build — completes a model + IDE + hosting vertical stack
