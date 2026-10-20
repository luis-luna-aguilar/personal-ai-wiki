---
title: TesterArmy e2e
type: tool
domains: [coding]
subcategory: ai-e2e-testing
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
