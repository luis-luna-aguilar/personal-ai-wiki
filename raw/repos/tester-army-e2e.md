---
title: tester-army/e2e: Next generation e2e testing framework for web and mobile apps. · GitHub
type: source
source_type: repo
url: https://github.com/tester-army/e2e
fetched: 2026-10-19
---

# tester-army/e2e: Next generation e2e testing framework for web and mobile apps. · GitHub

[![e2e, the open source AI testing framework by TesterArmy](/tester-army/e2e/raw/main/.github/assets/readme-banner.png)](https://tester.army/e2e?utm_source=e2e&utm_medium=github&utm_campaign=readme_banner)

[![Made by TesterArmy](/tester-army/e2e/raw/main/.github/assets/made-by-testerarmy.svg)](https://tester.army?utm_source=e2e&utm_medium=github&utm_campaign=readme_badge)
[![npm version](https://camo.githubusercontent.com/20d73ae04bbc2c1d29874dabf67df45658babf1459e06ba72febd288e95275a3/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6532652e7376673f7374796c653d666f722d7468652d6261646765266c6162656c436f6c6f723d303030303030)](https://www.npmjs.com/package/e2e)
[![License: Apache-2.0](https://camo.githubusercontent.com/622fb3cb28678c01d3eba3a3b5da9bade8dbea4ebd5a828e334d774060a77e47/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4170616368652d2d322e302d677265656e2e7376673f7374796c653d666f722d7468652d6261646765266c6162656c436f6c6f723d303030303030)](/tester-army/e2e/blob/main/LICENSE)
[![Join the community on Discord](https://camo.githubusercontent.com/a59f4344de8e7229b97b72ce7fb75550b6a009b59674b479bacc3204786761d6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6f696e253230746865253230636f6d6d756e6974792d3538363546322e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d303030303030)](https://tester.army/discord)

[![GitHub Trending Repository of the Day](https://camo.githubusercontent.com/919ca8902f29cebbc87ca559ef60161e4613096803e6acd8277de035e1d5a823/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f62616467653f7265706f3d7465737465722d61726d792f65326526747970653d7472656e64696e67)](https://www.star-history.com/tester-army/e2e)

[e2e](https://tester.army/e2e?utm_source=e2e&utm_medium=github&utm_campaign=readme_intro) is an end-to-end testing framework for web and mobile apps. Describe a goal in natural language and an agent drives the app to reach it. Check the result with locators and assertions in the same test.

```
// tests/checkout.e2e.ts
import { test, expect } from 'e2e';

test('a member upgrades to Pro', async ({ app, agent, screen }) => {
  await app.open('/settings/billing');

  await agent.act('upgrade the workspace to the Pro plan');
  await agent.assert('the invoice preview shows a prorated amount');

  await expect(screen.getByRole('status')).toContainText('Pro');
});
```

An agent step that a later assertion verifies records its actions, and the
next run replays them with no model calls until the app changes. Tests
without agent steps need no model. Bring your own subscription, API key, or
local model.

`init` asks for an engine, web or mobile, and a model provider, then writes a
config and an example test. The
[quickstart](https://e2e.tester.army/docs/quickstart) covers the rest.

To see a finished setup in your stack, open
[`examples/`](https://github.com/tester-army/e2e/tree/main/examples):
Vite, Next.js, Astro, Expo, SwiftUI, Jetpack Compose, Kotlin Multiplatform,
Flutter, and .NET MAUI, each a standalone project with a passing suite.

| Package | What it does |
| --- | --- |
| [`e2e`](https://www.npmjs.com/package/e2e) | The SDK, runner, and CLI. |
| [`@e2e-dev/web`](https://www.npmjs.com/package/@e2e-dev/web) | Browser engine: Chromium, Firefox, and WebKit through Playwright. |
| [`@e2e-dev/mobile`](https://www.npmjs.com/package/@e2e-dev/mobile) | iOS and Android engine: simulators and emulators through agent-device. |
| [`@e2e-dev/github`](https://www.npmjs.com/package/@e2e-dev/github) | Reporter that posts results as a pull request comment. |
| [`@e2e-dev/kernel`](https://www.npmjs.com/package/@e2e-dev/kernel) | Kernel hosted browsers for the web engine. |
| [`@e2e-dev/lightpanda`](https://www.npmjs.com/package/@e2e-dev/lightpanda) | Lightpanda, the open-source headless browser, started per run for the web engine. |
| [`@e2e-dev/limrun`](https://www.npmjs.com/package/@e2e-dev/limrun) | Limrun hosted iOS simulators and Android emulators for mobile tests. |
| [`@e2e-dev/eas`](https://www.npmjs.com/package/@e2e-dev/eas) | EAS Simulators hosted iOS simulators and Android emulators for the mobile engine. |
| [`@e2e-dev/smol`](https://www.npmjs.com/package/@e2e-dev/smol) | smol machines browsers for the web engine: by default, each attempt branches a warm Chromium microVM. |
| [`@e2e-dev/decision`](https://e2e.tester.army/docs/decision-models) | Decision-model executors for bounded semantic actions and assertions. |
| [`@e2e-dev/testmu`](https://www.npmjs.com/package/@e2e-dev/testmu) | TestMu AI (formerly LambdaTest) hosted Android emulators, iOS simulators, and real devices for the mobile engine. |

[e2e.tester.army/docs](https://e2e.tester.army/docs). The `e2e` package ships
every page, so coding agents can read them offline in `node_modules/e2e/docs`.

See [CONTRIBUTING.md](/tester-army/e2e/blob/main/CONTRIBUTING.md). Questions go to
[Discord](https://tester.army/discord).

Please don't open public issues for security vulnerabilities. Follow
[SECURITY.md](/tester-army/e2e/blob/main/SECURITY.md) and report them to
[security@tester.army](mailto:security@tester.army).

The CLI sends anonymous usage data, such as which commands and engines run and
where runs fail, but no test content, app content, or credentials. Opt out with
`npx e2e telemetry disable` or `E2E_TELEMETRY_DISABLED=1`.
[Telemetry](https://e2e.tester.army/docs/telemetry) lists every field.

Note

e2e is in active development on the way to 1.0. APIs and config can still
change between minor releases.

e2e is built by [TesterArmy](https://tester.army/?utm_source=e2e&utm_medium=github&utm_campaign=readme_footer),
the agentic testing platform that runs natural language tests on web and mobile
apps, on every pull request or on a schedule.

Apache-2.0.
