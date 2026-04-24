---
type: proposal
source: raw/deep-research/2026-04-24 QA Tooling for Software Agents.md
status: applied
created: 2026-04-24
---

# Proposal: QA tooling layer for software-agent verification

## Summary

The wiki now has good high-level guidance on coding-agent evals, but it is still thin on the concrete tooling and workflow layer that turns QA work into reusable agent-verification infrastructure. This proposal expands `wiki/training/evals-for-agentic-software-development.md` from "what to evaluate" into "how teams actually implement it" by adding sandboxed execution, a dual-track trajectory/output pattern, QA-to-eval pipelines, browser self-verification, and proof artifacts. It also adds a source summary for the deep-research report.

The main claims are supported by the report plus primary-source verification from E2B, Stagehand, Browserbase, and Agentrial docs. Vendor-specific pricing and benchmark-style stack recommendations are intentionally omitted.

## Intended changes

- [x] **Create** `wiki/sources/deep-research/2026-04-24-qa-tooling-for-software-agents.md`
  > New source summary page for the report

- [x] **Update** `wiki/training/evals-for-agentic-software-development.md`
  > Add:
  > - `## Tooling layer`
  > - `## QA-to-eval pipeline`
  > - stronger browser / proof-artifact guidance
  > - a more explicit trajectory-vs-output implementation split

- [x] **Update** `wiki/training/ai-enablement-software-development.md`
  > Add one guidance bullet and one proven-pattern bullet on QA becoming a producer of reusable eval artifacts rather than only a downstream manual-testing function

- [x] **Update** `wiki/index.md`
  > Refresh the blurb for `[[training/evals-for-agentic-software-development]]` so it mentions sandboxing, QA artifacts, and browser self-verification

## Drafts

### `wiki/sources/deep-research/2026-04-24-qa-tooling-for-software-agents.md` (new)

```md
---
title: Practical tooling layer for evals in agentic software development
type: source
source_type: deep-research
source_file: raw/deep-research/2026-04-24 QA Tooling for Software Agents.md
published: 2026-04-24
ingested: 2026-04-24
domains: [coding, agents, computer-use]
---

# Practical tooling layer for evals in agentic software development

Deep-research synthesis focused on the concrete verification stack for software agents: secure execution environments, trajectory evaluators, QA-to-test conversion, browser self-verification, and proof artifacts. Treat it as a tooling map and workflow synthesis rather than as a canonical source for specific pricing, latency, or vendor-ranking claims.

## Influenced pages

- [[training/evals-for-agentic-software-development]] — adds the tooling layer: sandboxes, dual-track evals, QA artifact capture, browser verification, and proof artifacts
- [[training/ai-enablement-software-development]] — adds a clearer role for QA as a producer of reusable eval artifacts
- [[tools/e2b]] — isolated sandbox runtime for agent execution and test runs
- [[tools/agentrial]] — multi-trial statistical eval runner for agent consistency and regression detection
- [[tools/stagehand]] — browser automation framework for self-verification loops
- [[tools/browserbase]] — browser infrastructure for agent browser sessions, artifact capture, and end-to-end testing

## Key claims extracted

- Execution-based evals matter more than generic reasoning benchmarks for coding agents
- Teams should separate trajectory evaluation from output verification
- QA should capture structured telemetry (HAR, DOM, Playwright traces), not just screen recordings and bug prose
- Frontend-changing agents increasingly need browser-based self-verification plus trace/video proof
- Proof artifacts and lineage are becoming first-class eval infrastructure, not optional debugging extras
```

### `wiki/training/evals-for-agentic-software-development.md` (update)

Add after `## Layered eval stack`:

```md
## Tooling layer

The practical eval stack for coding agents now splits cleanly into two tracks:

- **Trajectory tooling** evaluates *how* the agent worked: tool selection, file navigation, retries, and where the path broke.
- **Output verification** evaluates *what* the agent produced: does the patch compile, pass tests, and behave correctly in a real environment?

This makes the earlier trajectory-vs-result distinction operational rather than conceptual. A good stack usually combines:

- **Isolated execution runtimes** such as E2B-style sandboxes so agent-generated code runs away from the host machine
- **Trajectory evaluators** such as Agentrial-style multi-trial runners that measure consistency and identify which step diverged between passing and failing runs
- **Output harnesses** such as SWE-bench-style patch execution or the team's own repo-native test suite
- **Browser verification** for frontend-changing work, using Playwright directly or AI-assisted layers such as Stagehand

The key design rule: do not let agent-generated code be evaluated only as text. Run it in an isolated environment, test it, and capture the artifacts.
```

Add after `## Converting real artifacts into eval cases`:

```md
## QA-to-eval pipeline

The most useful new role for QA in agentic development is not maintaining brittle manual click scripts. It is curating the artifacts that become durable regression cases for coding agents.

Practical pattern:

1. QA performs exploratory testing in staging
2. Capture structured telemetry: HAR, DOM snapshots, console logs, or Playwright traces
3. Convert those artifacts into deterministic Playwright tests
4. Commit the generated tests into the repo
5. Run them as CI gates for future agent-authored changes

The important lesson is negative as well as positive: pure "video-to-test" is not enough. Video is useful for human context, but reusable agent evals need structural traces, not just pixels.

This changes the QA boundary. QA becomes a producer of eval datasets and proof artifacts, not only the final downstream checker of a completed feature.
```

Replace the final paragraph of `## Minimum Viable Eval Suite (MVES)` with:

```md
As the agent matures: add visual regression and browser-based verification for frontend changes, dynamic test generation (agent writes a failing test before writing the fix), and proof-artifact capture so successful runs leave behind replayable traces, screenshots, or videos rather than only a green checkmark.
```

Add near the end, before `## Proven patterns`:

```md
## Browser self-verification and proof artifacts

For frontend-changing work, "tests passed" is not enough. A stronger pattern is:

1. The agent writes the code
2. The agent opens the app in a browser
3. The agent verifies the intended UI or workflow
4. The run emits trace, screenshot, or video artifacts for human review

This can be done with deterministic Playwright alone, but AI-assisted browser layers are increasingly useful when selectors are unstable or the agent needs to reason over page semantics. The output should still be a replayable artifact, not only a verbal claim that the feature worked.

Proof artifacts matter for two reasons:

- they make review faster because humans can inspect the run without reproducing it locally
- they improve the eval loop because the exact browser trace can become the next regression case
```

### `wiki/training/ai-enablement-software-development.md` (update)

Add under `## Current guidance`:

```md
- Treat QA as part of the eval system: capture structured browser/session artifacts that can be converted into durable regression tests for coding agents
```

Add under `## Proven patterns`:

```md
- **QA as dataset maintainer.** In AI-native engineering teams, QA creates leverage by turning exploratory sessions, HAR files, DOM traces, and browser runs into reusable eval cases. The role shifts from "last manual check before merge" toward maintaining the highest-signal regression corpus.
```

### `wiki/index.md` (update)

Replace the current training blurb:

```md
- [[training/evals-for-agentic-software-development]] — eval stack for coding agents: deterministic gates, task-specific patterns, MVES, shadow mode, trace mining *(as_of: 2026-04-23)*
```

With:

```md
- [[training/evals-for-agentic-software-development]] — eval stack for coding agents: deterministic gates, sandboxed execution, QA artifact capture, browser self-verification, MVES, and trace mining *(as_of: 2026-04-24)*
```

## Verification notes

- **E2B:** official docs confirm isolated agent sandboxes, SDK-based execution, and CI/CD / computer-use examples
- **Agentrial:** official GitHub README confirms multi-trial evaluation, Wilson confidence intervals, Fisher exact test attribution, and CI blocking
- **Stagehand:** official docs confirm the `act` / `extract` / `observe` / `agent` primitives and explicit Playwright integration
- **Browserbase:** official docs confirm cloud browsers, Playwright/browser sessions, and automated-testing positioning

## Open questions

- The report also surfaces Momentic, Checksum.ai, and ZeroStep, but those are more vendor-shaped and less central than the patterns above. I recommend mentioning them in body text later only if the user wants broader market coverage.
	- Lets skip them

## Comments

* Now we have tool pages for e2b, agentrial, stagehand and browserbase. Make sure to link them.
* A previous proposal added the source file in here, so you will need to merge that effort and keep just one.
