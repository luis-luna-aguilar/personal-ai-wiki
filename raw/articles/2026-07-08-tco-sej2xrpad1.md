---
title: 🦀 Crabbox Docs - Crabbox Docs
type: source
source_type: article
url: https://t.co/SEj2XRpaD1
fetched: 2026-07-08
---

# 🦀 Crabbox Docs - Crabbox Docs

# 🦀 Crabbox Docs

**Warm a box, sync the diff, run the suite.**

## [#](#what-crabbox-is)What Crabbox is

Crabbox is a generic remote software testing and execution control plane. It keeps the local developer story unchanged: edit, save, run. The difference is where the command executes. Crabbox moves tests, builds, browser checks, platform validation, and review evidence onto owned or provider-backed remote capacity, then streams the result back to the caller.

It is for maintainers, contributors, and automation that need a repeatable way to run repository commands on a machine other than the local laptop. A `crabbox run` leases a brokered cloud machine, reuses a static SSH host, or delegates to a sandbox provider; syncs your tracked, non-ignored local files; executes the command remotely; streams stdout and stderr back; records evidence; and then releases or unclaims the target.

Use Crabbox when local compute is too small or slow, when a workflow needs a fresh disposable runner, when the target platform is remote, or when an AI agent or reviewer needs auditable command output from the exact environment that ran. It is not a CI service, a package manager, a production deployment platform, a hostile multi-tenant sandbox, or a tool that automatically sanitizes secrets from command output and artifacts.

An optional coordinator owns cloud provider credentials, lease state, cleanup, usage accounting, and cost guardrails so individual machines and CLIs never hold those. The coordinator runs either on Cloudflare Workers with a Durable Object or on Node.js with PostgreSQL.

## [#](#how-it-fits-together)How it fits together

```
your laptop                 coordinator runtime              cloud provider
-------------               -------------------              --------------
crabbox CLI    -- HTTPS --> Cloudflare + Durable Object  --> Hetzner / AWS / Azure / GCP / Daytona
   |                      or Node.js + PostgreSQL              |
   |                                                           |
   +------------- SSH + rsync to leased runner <---------------+Copy
```

The CLI is a Go binary (`cmd/crabbox`, `internal/cli`). Shared coordinator behavior lives in `worker/src`; Cloudflare and Node/PostgreSQL provide runtime adapters. Lease lifecycle calls go through the coordinator over HTTPS, but the data plane — SSH, rsync, and command execution — goes **directly from the CLI to the runner host**. Runners hold no coordinator credentials; they are leaf nodes.

Crabbox selects one of three execution modes per provider:

* **Brokered** — for `aws`, `azure`, `gcp`, and `hetzner` when a broker URL is

configured (`CRABBOX_COORDINATOR`). The coordinator provisions and tracks leases; the CLI still drives sync and command execution over SSH.

* **Direct SSH** — the same SSH-lease providers without a broker, plus static

hosts (`provider: ssh`) and self-hosted/local providers. The CLI talks to the cloud or host API itself.

* **Delegated** — sandbox/proof runners (for example dynamic-session and

Firecracker providers) that own sync and run end to end; there is no SSH lease.

Brokered Linux runners are vanilla Ubuntu boxes prepared by cloud-init with SSH, Git, rsync, and `/work/crabbox`. AWS and Azure can also broker Windows (normal and WSL2) and, on AWS, EC2 Mac desktop targets. Project runtimes come from Actions hydration or repo-owned setup.

## [#](#a-run-end-to-end)A run, end to end

1. The CLI loads config from flags, env, repo, user, and defaults.
2. The CLI mints a per-lease SSH key and slug, then `POST /v1/leases` on the

broker (brokered mode) or provisions directly (direct mode).

3. The coordinator checks active-lease and monthly spend caps, reserves

worst-case TTL cost, provisions a server with region/market fallback, and returns host / port / user / workdir / expiry / slug.

4. The CLI waits for the `crabbox-ready` marker, seeds remote Git when possible,

rsyncs the Git file-list manifest, runs sync guardrails, and hydrates the configured base ref.

5. The CLI runs the command over SSH, streams output, records run events, and

sends heartbeats.

6. The CLI releases the lease unless `--keep` is set. Kept leases still

auto-release after the idle timeout, and the broker frees reserved cost when the lease closes.

See [How Crabbox Works](how-it-works.html) for the full picture, including warm-box reuse and the brokered-vs-direct paths. See the [Source Map](source-map.html) to trace any documented behavior back to code.

## [#](#install)Install

```
brew install openclaw/tap/crabboxCopy
```

Verify with `crabbox --version`.

## [#](#quick-start)Quick start

```
# log in once per machine — stores a broker token in user config
crabbox login --url https://broker.example.com

# one-shot run on a fresh leased box
crabbox run -- pnpm test

# keep a warm box around for repeated runs; output includes an id and a slug
crabbox warmup
crabbox run --id swift-crab -- pnpm test:changed
crabbox ssh --id swift-crab
crabbox stop swift-crabCopy
```

Each lease has a canonical id (`cbx_<12 hex>`) and a friendly slug (`<adjective>-<noun>`); most commands accept either via `--id`. Run `crabbox doctor` to validate local config, broker/provider reachability, and SSH key availability before a long workflow, and `crabbox usage` to summarize recent spend by user, org, provider, and server type.

## [#](#where-to-read-next)Where to read next

Pick whichever matches your intent:

* **Start here:** [Getting started](getting-started.html),

[How Crabbox Works](how-it-works.html), [Concepts and glossary](concepts.html).

* **Get the mental model:** [Vision](vision.html),

[Architecture](architecture.html), [Orchestrator](orchestrator.html), [Runtime adapter stack](features/runtime-adapter-stack.html), [Broker auth and routing](features/broker-auth-routing.html), [Coordinator](features/coordinator.html), [Bring your own infrastructure](features/bring-your-own-infrastructure.html), [Slurm academic sandboxes](features/slurm-academic-sandboxes.html).

* **Deploy the coordinator:** [Infrastructure](infrastructure.html),

[Portable coordinator](features/portable-coordinator.html), [Operations](operations.html), [Security](security.html).

* **Use the CLI:** [CLI overview](cli.html),

[Command reference](commands/index.html), [Feature reference](features/index.html), [Configuration](features/configuration.html), [Jobs](features/jobs.html), [Pond](features/pond.html), [Actions hydration](features/actions-hydration.html), [Capsules](features/capsules.html), [Checkpoints](features/checkpoints.html), [Browser portal](features/portal.html), [Runtime adapter stack](features/runtime-adapter-stack.html), [Capabilities](features/capabilities.html), [Interactive desktop and VNC](features/interactive-desktop-vnc.html), [Telemetry](features/telemetry.html), [Sync](features/sync.html).

* **Pick or add a target:** [Provider reference](providers/index.html),

[Providers feature overview](features/providers.html), [Provider selection](features/provider-selection.html), [Provider landscape](features/provider-landscape.html), [Provider live smoke](features/provider-live-smoke.html), [Provider authoring](features/provider-authoring.html), [Provider backends](provider-backends.html), [Capacity fallback](features/capacity-fallback.html), [Slurm academic sandboxes](features/slurm-academic-sandboxes.html), [Network](features/network.html), [Tailscale](features/tailscale.html). Per-provider: [AWS](providers/aws.html), [Azure](providers/azure.html), [Azure Dynamic Sessions](providers/azure-dynamic-sessions.html), [Google Cloud](providers/gcp.html), [Hetzner](providers/hetzner.html), [DigitalOcean](providers/digitalocean.html), [Linode](providers/linode.html), [Vultr](providers/vultr.html), [Proxmox](providers/proxmox.html), [XCP-ng](providers/xcp-ng.html), [Incus](providers/incus.html), [Parallels](providers/parallels.html), [Local Container](providers/local-container.html), [Multipass](providers/multipass.html), [Static SSH](providers/ssh.html), [Railway](providers/railway.html), [RunPod](providers/runpod.html), [Blacksmith Testbox](providers/blacksmith-testbox.html), [KubeVirt](providers/kubevirt.html), [External](providers/external.html), [Namespace Devbox](providers/namespace-devbox.html), [Namespace Compute Instance](providers/namespace-instance.html), [Semaphore](providers/semaphore.html), [Sprites](providers/sprites.html), [Tenki](providers/tenki.html), [Coder](providers/coder.html), [Daytona](providers/daytona.html), [Islo](providers/islo.html), [E2B](providers/e2b.html), [Modal](providers/modal.html), [Agent Sandbox](providers/agent-sandbox.html), [OpenComputer](providers/opencomputer.html), [Freestyle](providers/freestyle.html), [Anthropic Sandbox Runtime](providers/anthropic-sandbox-runtime.html), [Tensorlake](providers/tensorlake.html), [Upstash Box](providers/upstash-box.html), [Weights & Biases](providers/wandb.html), [Cloudflare](providers/cloudflare.html).

* **Operate it:** [Operations](operations.html),

[Observability](observability.html), [Troubleshooting](troubleshooting.html), [Performance](performance.html), [Cost and usage](features/cost-usage.html), [Lifecycle and cleanup](features/lifecycle-cleanup.html).

* **Set it up or audit it:** [Infrastructure](infrastructure.html),

[Portable coordinator](features/portable-coordinator.html), [Security](security.html), [Auth and admin](features/auth-admin.html), [Repository onboarding](features/repository-onboarding.html), [SSH keys](features/ssh-keys.html), [Source Map](source-map.html).

## [#](#about-these-docs)About these docs

Markdown in this directory is the user-facing documentation source. Implementation truth stays in code; the [Source Map](source-map.html) lists the files behind each documented behavior. The GitHub Pages site at <https://openclaw.github.io/crabbox/> is generated from these Markdown files by `scripts/build-docs-site.mjs` and deployed by `.github/workflows/pages.yml`. Pages must be enabled on the repository or organization for the workflow to publish.

Build and check the docs site locally:

```
scripts/check-docs.sh
open dist/docs-site/index.htmlCopy
```
