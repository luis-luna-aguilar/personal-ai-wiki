---
type: proposal
source:
  - raw/tweets/2026-07-08-mattpocockuk-2059934011124826124.md
  - raw/articles/2026-07-08-tco-sej2xrpad1.md
  - raw/newsletters/2026-05-28-the-age-of-async-agents-cognitions-walden-yan.md
  - raw/newsletters/2026-05-30-ainews-founders-and-forward-deployed-engineers.md
  - raw/newsletters/2026-05-27-ainews-new-ai-infra-decacorns-fireworks-basete.md
status: pending
created: 2026-07-08
---

# Proposal: Code review, remote execution, and harness effectiveness

## Summary

The approved code-review and harness signals point to the same operational layer: agents need stronger verification environments, proof artifacts, historical replay, and harness metrics. This proposal updates the dedicated AI PR/code-review page, coding-agent eval guidance, and harness concept page.

## Intended changes

- [x] **Update** `wiki/workflows/ai-pr-code-review.md` - add remote execution/proof artifacts and Cursor deep-review signal.
- [x] **Update** `wiki/training/evals-for-agentic-software-development.md` - add remote execution control planes as proof-artifact infrastructure.
- [x] **Update** `wiki/concepts/harness.md` - add Effective Feedback Compute and model-specific harness profiles.
- [x] **Update** `wiki/concepts/agent-evals.md` - add harness metrics beyond token/tool counts.
- [x] **Create** `wiki/tools/crabbox.md` - tool page for Crabbox as a remote software testing and execution control plane.
- [x] **Update** `wiki/index.md` - add Crabbox under Tools.
- [x] **Create** `wiki/sources/articles/crabbox-remote-execution-2026-07.md` - source summary.
- [x] **Create** `wiki/sources/newsletters/effective-feedback-compute-harness-2026-05.md` - source summary.
- [x] **Create** `wiki/sources/newsletters/cognition-async-agents-testing-2026-05.md` - source summary.

## Page drafts

### wiki/workflows/ai-pr-code-review.md (updated sections)

```md
---
as_of: 2026-07-08
sources: [..., crabbox-remote-execution-2026-07, cognition-async-agents-testing-2026-05]
---

## Review execution stack

Add after deterministic checks:

3. **Remote execution evidence** - run tests, builds, browser checks, and platform validation on a repeatable remote machine or sandbox when local execution is too slow, too small, or not representative.
4. **Proof artifact capture** - attach logs, screenshots, videos, traces, and exact command output so the human reviewer can inspect what actually ran.

## Review artifacts

Add:

- Remote-run transcripts from tools such as Crabbox, showing the leased machine, command, output, and release/cleanup state
- Cloud or sandbox evidence from async agents, including screenshots and video proof for PRs where runtime behavior matters

## Evidence from practice

- Crabbox documents a remote execution control plane for tests, builds, browser checks, and review evidence, keeping the local developer story unchanged while running commands on leased or provider-backed machines.
- Cognition's Walden Yan frames testing and proof artifacts as central to async coding-agent trust: screenshots, videos, and command results become the review surface, not just generated code.
- Cursor's "/thermo-nuclear-code-review" signal suggests deep AI code review is becoming a productized mode, though the fetched source is only a thin tweet and should be treated as directional.

## Recent changes

- [2026-07-08] Added remote execution and proof artifacts as first-class PR-review infrastructure for agent-authored work.
```

### wiki/training/evals-for-agentic-software-development.md (updated sections)

```md
---
as_of: 2026-07-08
sources: [..., crabbox-remote-execution-2026-07, cognition-async-agents-testing-2026-05]
---

## Tooling layer

Add:

- **Remote execution control planes** such as Crabbox when the eval needs a fresh machine, remote platform, larger compute, Windows/macOS/Linux target, or auditable command output from an exact environment.

## Browser self-verification and proof artifacts

Add:

Proof artifacts should identify where they ran, not only what they showed. For coding-agent PRs, a useful artifact includes the command, environment, runner identity, stdout/stderr, screenshots or video when relevant, and whether the runner was released or retained for debugging.

## Recent changes

- [2026-07-08] Added remote execution control planes as part of the coding-agent eval/proof-artifact stack.
```

### wiki/concepts/harness.md (updated sections)

```md
---
as_of: 2026-05-30
sources: [..., effective-feedback-compute-harness-2026-05]
---

## What good harness engineering looks like

- **Measure effective feedback, not only activity.** Raw token counts, tool counts, and trace length are weak proxies for agent success. AINews coverage of Effective Feedback Compute argues that the useful signal is whether the harness gives the model actionable feedback that improves the next step.
- **Model-specific harness profiles.** LangChain Deep Agents coverage suggests that Qwen, Kimi, DeepSeek, and frontier closed models can require different prompts, tools, and memory layouts. A cheaper model can become viable when the harness matches its operating style.

## Harness vs model

Add:

The practical model/harness split is now measurable: the same model can underperform in a mismatched product surface, while a cheaper model can approach frontier behavior in a tuned harness. Treat benchmark results as model + harness + environment, not model-only.

## Recent changes

- [2026-05-30] Added Effective Feedback Compute and model-specific harness profiles as harness-quality signals beyond token/tool counts.
```

### wiki/concepts/agent-evals.md (updated sections)

```md
---
as_of: 2026-05-30
sources: [..., effective-feedback-compute-harness-2026-05]
---

## Five eval categories

Add under Cost and variance:

- **Feedback quality** - whether the harness supplies feedback that lets the agent improve its next action. This is distinct from how many tokens or tools the agent used.

## How this changes eval design

Add:

Effective Feedback Compute is a useful direction because it evaluates the information value of feedback inside the loop. Long traces and many tool calls can still be low-value if they do not change the agent's trajectory toward success.

## Recent changes

- [2026-05-30] Added feedback-quality framing from Effective Feedback Compute: agent evals should measure whether the harness improves the next step, not only how much activity occurred.
```

### wiki/tools/crabbox.md (new)

```md
---
title: Crabbox
type: tool
domains: [coding, agents]
subcategory: agentic-devops
tags: [cli, agentic]
as_of: 2026-07-08
sources: [crabbox-remote-execution-2026-07]
---

# Crabbox

Crabbox is a remote software testing and execution control plane. It keeps the local developer workflow as edit, save, run, but moves the actual command execution to owned or provider-backed remote capacity.

## Current status (as of 2026-07-08)

- CLI-driven workflow: `crabbox run -- <command>` leases or reuses a remote runner, syncs tracked non-ignored files, executes the command, streams output, records evidence, and releases or retains the target.
- Supports tests, builds, browser checks, platform validation, and review evidence when local compute is too slow, too small, or not representative.
- Execution modes include brokered cloud leases, direct SSH/static hosts, and delegated sandbox/proof runners.
- Brokered mode keeps cloud-provider credentials, lease state, cleanup, usage accounting, and cost guardrails in a coordinator rather than on individual machines.
- The docs explicitly position it as not being CI, a package manager, a production deployment platform, a hostile multi-tenant sandbox, or an automatic secret-sanitization layer.

## Strengths

- Gives AI agents and reviewers auditable command output from the environment that actually ran.
- Fits PR review and eval workflows where proof artifacts matter more than local reproduction.
- Supports heterogeneous targets, including cloud Linux runners, Windows/WSL2, EC2 Mac, static SSH hosts, and sandbox providers.

## Weaknesses / caveats

- The source is documentation, not adoption evidence; durability and ecosystem use still need more signals.
- Remote execution can expose secrets through command output or artifacts if teams do not design guardrails.
- It complements CI but does not replace CI policy, production deployment controls, or hostile sandbox isolation.

## Recent changes

- [2026-07-08] Crabbox docs captured as a remote execution / proof-artifact control plane for coding agents and PR review workflows.

## Sources

- [Crabbox remote execution docs](../sources/articles/crabbox-remote-execution-2026-07.md)
```

### wiki/index.md (updated section)

```md
## Tools

- [tools/crabbox](tools/crabbox.md) - remote software testing and execution control plane for running tests, builds, browser checks, platform validation, and review evidence on leased or provider-backed machines *(as_of: 2026-07-08)*
```

### wiki/sources/articles/crabbox-remote-execution-2026-07.md (new)

```md
---
title: Crabbox remote execution docs
type: source
source_type: article
source_file: raw/articles/2026-07-08-tco-sej2xrpad1.md
url: https://openclaw.github.io/crabbox/
published: 2026-07-08
ingested: 2026-07-08
domains: [coding, agents]
---

# Crabbox remote execution docs

Crabbox is documented as a generic remote software testing and execution control plane. It leases or reuses remote machines, syncs tracked local files, executes repository commands remotely, streams output, records evidence, and releases or retains the target.

## Influenced pages

- [Crabbox](../../tools/crabbox.md) - tool page
- [AI PR and code review](../../workflows/ai-pr-code-review.md) - remote execution evidence
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) - proof-artifact infrastructure

## Key claims extracted

- Crabbox supports tests, builds, browser checks, platform validation, and review evidence on remote capacity.
- Brokered mode keeps cloud credentials in a coordinator rather than the CLI or runner.
- The data plane uses SSH/rsync directly from CLI to runner for SSH-backed providers.
```

### wiki/sources/newsletters/effective-feedback-compute-harness-2026-05.md (new)

```md
---
title: Effective Feedback Compute and harness profiles
type: source
source_type: newsletter
source_file:
  - raw/newsletters/2026-05-30-ainews-founders-and-forward-deployed-engineers.md
  - raw/newsletters/2026-05-27-ainews-new-ai-infra-decacorns-fireworks-basete.md
url: https://www.latent.space/p/ainews-founders-and-forward-deployed-engineers
published: 2026-05-30
ingested: 2026-07-08
domains: [agents]
---

# Effective Feedback Compute and harness profiles

AINews summarizes a cluster of harness-engineering claims around Effective Feedback Compute, model-specific agent profiles, and the idea that harness quality can dominate raw model choice for agent performance and cost.

## Influenced pages

- [Harness](../../concepts/harness.md) - feedback-quality and model-specific harness profile additions
- [Agent evals](../../concepts/agent-evals.md) - feedback quality as an eval dimension

## Key claims extracted

- Raw token counts and tool counts can be weak predictors of agent success.
- Effective Feedback Compute is presented as a better signal for whether an agent loop is improving.
- LangChain Deep Agents profiles suggest cheaper models can perform strongly when matched with an appropriate harness.
```

### wiki/sources/newsletters/cognition-async-agents-testing-2026-05.md (new)

```md
---
title: Cognition async agents and testing proof
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-28-the-age-of-async-agents-cognitions-walden-yan.md
url: https://www.latent.space/p/the-age-of-async-agents-cognitions
published: 2026-05-28
ingested: 2026-07-08
domains: [coding, agents]
---

# Cognition async agents and testing proof

Latent Space's interview with Cognition's Walden Yan frames async coding agents around delegated work and evidence. The practical signal is that trust in generated code increasingly comes from testing, screenshots, video proof, and orchestration rather than from watching a model type.

## Influenced pages

- [AI PR and code review](../../workflows/ai-pr-code-review.md) - proof artifacts and async review surface
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) - verification artifacts

## Key claims extracted

- Async coding agents require proof artifacts that humans can inspect.
- Testing is central to trust; no single frontier model handles every end-to-end testing situation.
- Screenshots and videos can become part of PR evidence.
```

## Open questions

- The proposal uses existing subcategory `agentic-devops` for Crabbox. If this kind of tool becomes common, we may later want a narrower subcategory such as `remote-execution-control-plane`.
