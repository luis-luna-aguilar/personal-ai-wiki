---
type: proposal
source: raw/repos/tester-army-e2e.md
status: pending
created: 2026-10-19
---

# Proposal: TesterArmy e2e (agent-driven end-to-end testing framework)

## Summary

### In short

Agent-driven end-to-end tests no longer need a model call on every run: TesterArmy's open-source e2e framework records an agent step once a later assertion has verified it, then replays it with no model calls until the app changes. One test mixes plain-English goals ("upgrade the workspace to the Pro plan") with ordinary locators and assertions, on web through Playwright and on iOS and Android. The proposal adds a tool page, a State of Coding line, and one sentence on the coding-agent evals page. Reason to hesitate: no existing subcategory fits cleanly, and the date is the capture date.

[[#Open questions|Open questions: 1 to answer.]]

### The source

The source is the GitHub README of `e2e`, an Apache-2.0 testing framework from TesterArmy, a company that sells a hosted platform for natural-language tests on every pull request or on a schedule. An end-to-end test drives a real app the way a user would and checks what appears on screen. In e2e, a test can ask an agent to act ("upgrade the workspace to the Pro plan") or to judge ("the invoice preview shows a prorated amount"). It then checks the result with standard locators, such as an element's role and text.

The key design choice is caching. When an agent step is confirmed by a later assertion in the same test, the framework records the actions it took, and later runs replay those actions without calling a model until the app changes. Tests with no agent steps need no model at all. Users bring their own subscription, API key or local model. A separate package plugs in "decision models" for bounded semantic actions and assertions.

The framework runs web tests on Chromium, Firefox and WebKit through Playwright, and mobile tests on iOS simulators and Android emulators. Add-on packages connect hosted browsers and devices (Kernel, Lightpanda, Limrun, EAS, smol machines, TestMu AI) and post results as a pull-request comment. Example projects cover nine stacks, from Next.js to SwiftUI, Flutter and .NET MAUI. The docs ship inside the npm package so coding agents can read them offline. The CLI sends anonymous usage data unless switched off, and the project warns that APIs may still change before 1.0.

### What changes

The wiki's browser-verification guidance names Playwright, Stagehand and Browserbase. State of Coding's Agentic DevOps section lists Checkly as its one verification tool.

- New page `wiki/tools/tester-army-e2e.md`.
- **State of Coding** gains an e2e line under Agentic DevOps, next to Checkly, and one Recent-changes entry. The list is at its cap of ten, so the oldest entry (17 June, SpaceX's acquisition of Cursor) moves to history. Page date moves from 3 August to 19 October.
- **Evals for agentic software development** gains one sentence in its browser self-verification section, on mixing agent steps with deterministic assertions and replaying verified steps. It gets one Recent-changes entry (five become six) and its page date moves from 14 October to 19 October. Body length rises from about 2,495 to about 2,540 words, 102% of the 2,500 ceiling for training pages, within the warning band.
- One new source page for the repository.

### What to weigh

The README has no release or commit date, so 19 October, the capture date, is used. For the subcategory, `agent-eval-tooling` covers tools that evaluate agents, while e2e uses an agent to test an app. I filed it under `agentic-devops`, following Checkly, a Playwright-based verification tool already there, though that definition leans toward infrastructure. I left the AI PR review workflow alone; the pull-request reporter is one package and adds nothing to that page.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/tools/tester-army-e2e.md` — new tool page (subcategory `agentic-devops`)
- [ ] **Update** `wiki/state-of/coding.md` — add one leader line at the end of `### Agentic DevOps`; adds one Recent-changes entry dated 2026-10-19 at the top (list is at the cap of 10); append `tester-army-e2e` to frontmatter `sources:`; `as_of` 2026-08-03 → 2026-10-19
- [ ] **Spill** `wiki/state-of/coding.md` → `wiki/history/state-of/coding.md` — spills the oldest Recent-changes entry (2026-06-17, SpaceX acquires Cursor) under a new archive header
- [ ] **Update** `wiki/training/evals-for-agentic-software-development.md` — insert one sentence in `## Browser self-verification and proof artifacts`; adds one Recent-changes entry dated 2026-10-19 (6 of 10, no spill); append `tester-army-e2e` to frontmatter `sources:` and one link to `## Sources`; `as_of` 2026-10-14 → 2026-10-19
- [ ] **Create** `wiki/sources/repos/tester-army-e2e.md` — source summary

## Page drafts

### wiki/tools/tester-army-e2e.md (new)

```
---
title: TesterArmy e2e
type: tool
domains: [coding]
subcategory: agentic-devops
tags: [open-source, agentic]
as_of: 2026-10-19
sources: [tester-army-e2e]
---

# TesterArmy e2e

Open-source (Apache-2.0) end-to-end testing framework for web and mobile apps from TesterArmy. A test describes a goal in natural language, an agent drives the app to reach it, and standard locators and assertions check the result in the same test.

## Current status (as of 2026-10-19)

- `agent.act()` and `agent.assert()` steps sit alongside `expect(screen.getByRole(...))` assertions in one TypeScript test
- An agent step that a later assertion verifies has its actions recorded; subsequent runs replay them with no model calls until the app changes. Tests without agent steps need no model
- Bring your own subscription, API key, or local model; a decision-model package handles bounded semantic actions and assertions
- Web engine on Chromium, Firefox, and WebKit via Playwright; mobile engine on iOS simulators and Android emulators; add-ons for hosted browsers and devices (Kernel, Lightpanda, Limrun, EAS, smol machines, TestMu AI) and a GitHub PR-comment reporter
- Example suites for Vite, Next.js, Astro, Expo, SwiftUI, Jetpack Compose, Kotlin Multiplatform, Flutter, and .NET MAUI; docs ship inside the npm package for offline reading by coding agents

## Why it matters

It packages the browser self-verification pattern from [Evals for agentic software development](../training/evals-for-agentic-software-development.md) as a test runner: the agent absorbs unstable selectors and page semantics, deterministic assertions keep the oracle, and record-and-replay keeps repeat runs cheap and repeatable.

## Weaknesses / caveats

- Pre-1.0: APIs and config can change between minor releases
- CLI sends anonymous usage telemetry by default (opt out with `npx e2e telemetry disable` or `E2E_TELEMETRY_DISABLED=1`)
- Built by a company that sells a hosted agentic-testing platform on top of it

## Recent changes

- [2026-10-19] Page created from the GitHub README.

## Sources

- [tester-army/e2e GitHub repository](../sources/repos/tester-army-e2e.md)
```

### wiki/state-of/coding.md (updated)

Frontmatter (changed fields only; `sources:` appends `tester-army-e2e`):

```
as_of: 2026-10-19
sources: [sdd-3-tools-fowler, cursor-3-launch, stripe-cli, claude-code-monitor, openai-pro-100, cursor-pr-demos, shopify-ai-toolkit, cursor-bugbot-learning, claude-code-routines, openai-codex-ongoing-tasks, orca-homepage, coding-agent-control-planes, claude-code-leak-architecture, cursor-3-orchestration-bet, skills-and-plugin-packaging-late-march, cursor-cloud-agents-march, claude-code-scheduled-tasks-march, codex-security-march, agentic-devops-deep-research, cursor-sdk-agent-runtime-2026-04-30, symphony-devin-terminal-orchestration-2026-04-28, end-of-finetuning-debate-2026-05-13, claude-code-goal-fastmode-fleetview-2026-05-13, claude-code-agent-view-2026-05-13, model-harness-fit-2026-05-13, agent-first-ide-convergence-may-2026, dynamic-workflows-claude-code, fable-ban-june-2026, spacex-cursor-june-2026, ainews-frontiercode-june-2026, ainews-not-much-happened-2026-07-02, every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-code-getting-started-with-loops-2026-06-30, claude-sonnet-5-official-2026-06-30, cursor-ios-mobile-app-2026-06, devinai-blog-windsurf-adaptive, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, every-copilot-studio-microsoft-2026-08-03, tester-army-e2e]
```

`### Agentic DevOps` — new line appended after the Checkly line:

```
- [TesterArmy e2e](../tools/tester-army-e2e.md) — open-source pre-merge counterpart: natural-language agent steps plus deterministic assertions for web and mobile apps, with verified agent steps replayed without model calls *(as of 2026-10-19)*
```

`## Recent changes` (adds one entry dated 2026-10-19 at the top; the list is at its cap of 10, so the oldest entry, dated 2026-06-17, spills):

```
- [2026-10-19] Added TesterArmy e2e to Agentic DevOps: agent-driven end-to-end tests for web and mobile that record verified agent steps and replay them without model calls.
```

Entry removed from the bottom of the live list:

```
- [2026-06-17] SpaceX acquires Cursor ($60B all-stock); Cursor Origin launched (agent-native git/code hosting); jointly trained xAI model coming to both Cursor and Grok Build — completes a model + IDE + hosting vertical stack
```

### wiki/history/state-of/coding.md (updated)

Appended at the end of the file (spills whatever is oldest at apply time; at proposal time that is the entry below):

```

## Archived from current page on 2026-10-19

- [2026-06-17] SpaceX acquires Cursor ($60B all-stock); Cursor Origin launched (agent-native git/code hosting); jointly trained xAI model coming to both Cursor and Grok Build — completes a model + IDE + hosting vertical stack
```

### wiki/training/evals-for-agentic-software-development.md (updated)

Frontmatter (changed fields only; `sources:` appends `tester-army-e2e`):

```
as_of: 2026-10-19
sources: [agents-evals-deep-research, qa-tooling-for-software-agents-deep-research, cost-aware-agent-evaluation-2026-04-28, opus-4-7-tokenizer-economics-2026-04-30, agentic-security-tooling-2026-05-13, ai-code-review-eval-integrity-2026-06, dashbench-code-review-understanding-2026-07, crabbox-remote-execution-2026-07, cognition-async-agents-testing-2026-05, lavaee-verification-pyramid-2026-10, tester-army-e2e]
```

`## Browser self-verification and proof artifacts` — the second paragraph, with one sentence inserted after the Stagehand/Browserbase sentence:

```
Deterministic Playwright suffices for this, but AI-assisted browser layers such as [Stagehand](../tools/stagehand.md) and [Browserbase](../tools/browserbase.md) help when selectors are unstable or the agent must reason over page semantics. [TesterArmy e2e](../tools/tester-army-e2e.md) combines the two in one test: natural-language agent steps drive the web or mobile app, ordinary assertions check the result, and an agent step that an assertion verified is recorded and replayed without model calls until the app changes. The output should be a replayable artifact, not a verbal claim that the feature worked: it speeds review (humans inspect the run without reproducing it locally) and feeds the eval loop (the exact browser trace becomes the next regression case).
```

`## Recent changes` (adds one entry dated 2026-10-19 at the top; 6 of 10, no spill):

```
- [2026-10-19] Added TesterArmy e2e to browser self-verification: agent steps mixed with deterministic assertions, with verified steps replayed without model calls.
```

`## Sources` (appends one link):

```
- [tester-army/e2e GitHub repository](../sources/repos/tester-army-e2e.md)
```

### wiki/sources/repos/tester-army-e2e.md (new)

```
---
title: 'tester-army/e2e GitHub repository'
type: source
source_type: repo
source_file: raw/repos/tester-army-e2e.md
url: https://github.com/tester-army/e2e
ingested: 2026-10-19
domains: [coding]
---

# tester-army/e2e GitHub repository

README of TesterArmy's `e2e`, an Apache-2.0 end-to-end testing framework for web and mobile apps in which natural-language agent steps and deterministic assertions share one test, and verified agent steps are replayed without model calls. No release or commit date in the capture; captured 2026-10-19.

## Influenced pages

- [TesterArmy e2e](../../tools/tester-army-e2e.md) — new tool page
- [State of Coding](../../state-of/coding.md) — new Agentic DevOps line
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) — one sentence in browser self-verification

## Key claims extracted

- Tests combine `agent.act()` / `agent.assert()` with locator assertions (`expect(screen.getByRole(...))`)
- An agent step that a later assertion verifies records its actions; the next run replays them with no model calls until the app changes
- Tests without agent steps need no model; bring your own subscription, API key, or local model
- `init` picks engine (web or mobile) and model provider and writes config plus an example test
- Packages: `e2e` (SDK, runner, CLI), `@e2e-dev/web` (Playwright: Chromium, Firefox, WebKit), `@e2e-dev/mobile` (iOS/Android via agent-device), `@e2e-dev/github` (PR comment reporter), hosted browser/device adapters (Kernel, Lightpanda, Limrun, EAS, smol machines, TestMu AI), `@e2e-dev/decision` (decision-model executors)
- Examples for Vite, Next.js, Astro, Expo, SwiftUI, Jetpack Compose, Kotlin Multiplatform, Flutter, .NET MAUI
- Docs ship in the npm package (`node_modules/e2e/docs`) for offline agent reading
- Anonymous CLI telemetry, opt-out; pre-1.0, APIs may change between minor releases
- Built by TesterArmy, which sells a hosted agentic-testing platform; Apache-2.0
```

## Schema / vocabulary additions

None.

## Open questions

- Should agent-driven app testing get its own subcategory (for example `ai-e2e-testing`, parent domain `coding`) instead of sitting under `agentic-devops`? With one member I left it under the Checkly precedent; a second tool in this space would justify the split.
	- Yes, it should. This is a separate one.
