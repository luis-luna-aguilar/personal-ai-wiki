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
- [State of Coding](../../state-of/coding.md) — new "AI end-to-end testing" section
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
