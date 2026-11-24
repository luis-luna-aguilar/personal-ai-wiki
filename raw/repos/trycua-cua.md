---
title: GitHub - trycua/cua: Scale computer-use 2.0 with open-source drivers, cross-OS sandboxes, and benchmarks for training, evaluation, and data generation. · GitHub
type: source
source_type: repo
url: https://github.com/trycua/cua
fetched: 2026-11-23
---

# GitHub - trycua/cua: Scale computer-use 2.0 with open-source drivers, cross-OS sandboxes, and benchmarks for training, evaluation, and data generation. · GitHub

Bring your own agent and model, or explore CUA-S1 for specialized decisions. Cua provides the computer and automation tools. [Computer-Use 2.0](https://cua.ai/docs/cua-driver/concepts/how-cua-driver-works) describes an agent moving between code, APIs, and graphical interfaces within the same task.

---

**Combine your existing computers into one supercomputer.** Your computers, shared by your team and its agents.

Cua Spaces is a desktop app that gives your agents full desktops. Each desktop is a Space: a macOS VM built locally on your Mac, or a Linux or Omarchy image. Spaces run on your Mac, on other computers you own, and in [your own cloud account](https://cua.ai/docs/cua-sdk/guides/local-runtimes#your-own-cloud) (AWS, Google Cloud or Modal), and the app keeps them in your menu bar and notch.

* **Teleport.** Move a signed-in app, such as Chrome or Slack, into a Space and it opens there still signed in. Your sessions stay in the Cua Keyvault, encrypted on your Mac, and reach a Space only after you approve.
* **Multiplayer.** You and your agents work on the same desktop, each with your own cursor. Step in to make a choice, then hand the desktop back.
* **Agent-ready images.** Spaces images ship with [cua-spacesd](/trycua/cua/blob/main/libs/cua-spacesd/README.md), so agents get processes, files, screenshots and input as soon as a Space starts.

cua-spaces-demo.mp4

[
](https://private-user-images.githubusercontent.com/3820588/663571723-a2ccc86b-10d0-48c0-bee6-7ae652ba1c59.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTU0OTIxMDgsIm5iZiI6MTc5NTQ5MTgwOCwicGF0aCI6Ii8zODIwNTg4LzY2MzU3MTcyMy1hMmNjYzg2Yi0xMGQwLTQ4YzAtYmVlNi03YWU2NTJiYTFjNTkubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MTEyNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjExMjRUMDM0MzI4WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YmQ4MTU4ZWFjYjIxYTVjZDUwNjc1ZTNjODJhZmVjMTg1NmVkMjJhZTFmMTc4ZTZiYjAzMDJlZGZlN2Q3MTI2NiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGbXA0In0.rGCdPffsHB6Dgwh0pJp9e-5Y74NsnwR7-1opVxTUEy4)

**Install on macOS 26 or later**

```
curl -fsSL https://cua.ai/install.sh | sh
```

On macOS the installer selects the Cua Spaces app by default and adds the `cua` CLI. You can also [download the signed `.dmg`](https://github.com/trycua/cua/releases/download/cua-spaces-v0.9.4/cua-spaces-0.9.4-darwin-universal.dmg), or get the `.pkg` from the [Cua Spaces 0.9.4 release](https://github.com/trycua/cua/releases/tag/cua-spaces-v0.9.4).

Spaces is free for individuals. Pro is $18 a month and Teams is $30 per seat a month, available now from 1 seat. See [pricing](https://cua.ai/pricing). The app is source-available under [FSL-1.1-MIT](#licensing).

**[Quickstart](https://cua.ai/docs/spaces/quickstart)** | **[Teleport an app](https://cua.ai/docs/spaces/guides/teleport-an-app)** | **[Share a Space](https://cua.ai/docs/spaces/guides/share-a-space)** | **[Host Spaces on a spare Mac (relay, Tailscale or SSH)](https://cua.ai/docs/spaces/guides/add-a-computer#use-a-spare-mac-to-host-spaces)** | **[Your own cloud](https://cua.ai/docs/cua-sdk/guides/local-runtimes#your-own-cloud)** | **[App source](/trycua/cua/blob/main/apps/cua-spaces-macos/README.md)**

---

Give your agent tools to inspect and operate native desktop apps and browsers on macOS, Windows, and Linux. Connect through the CLI, MCP, or typed SDKs. Background delivery lets agents work without moving your pointer or taking focus when the app and platform support it; see [platform support](https://cua.ai/docs/cua-driver/concepts/platform-support) for the boundaries.

**macOS / Linux**

```
/bin/bash -c "$(curl -fsSL https://cua.ai/driver/install.sh)"
```

**Windows (PowerShell)**

```
irm https://cua.ai/driver/install.ps1 | iex
```

**Your first result:** connect your agent, ask it to compute 6 × 7 in Calculator, and have it verify that the app displays 42. The tutorial covers platform setup, permissions, and agent connection.

**[Drive your first app](https://cua.ai/docs/cua-driver/quickstart)** | **[Installation](https://cua.ai/docs/cua-driver/quickstart)** | **[CLI Reference](https://cua.ai/docs/cua-driver/reference/cli)**

Using Claude Code, Codex, Cursor, OpenClaw, or another agent? [Find your integration](https://cua.ai/docs/cua-driver/guides/connect-your-agent). Source documentation and architecture notes live in [`libs/cua-driver/README.md`](/trycua/cua/blob/main/libs/cua-driver/README.md).

Two Cua Driver sessions select cells in LibreOffice Calc and objects in Inkscape on an Omarchy desktop while a terminal stays in the foreground. Watch the 50-second demo.

recording.mp4

[
](https://private-user-images.githubusercontent.com/195596869/647521424-b4e5517c-d2db-4758-b4cf-07131b0753b2.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTU0OTIxMDgsIm5iZiI6MTc5NTQ5MTgwOCwicGF0aCI6Ii8xOTU1OTY4NjkvNjQ3NTIxNDI0LWI0ZTU1MTdjLWQyZGItNDc1OC1iNGNmLTA3MTMxYjA3NTNiMi5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTEyNFQwMzQzMjhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yOGZhMTg2ZjUxOWVlODIxOThiNjYzZTc1YTg1YmM3MWZkZTFjYjc0NDUyZGI0NjczMDRiZTg1NzFhZGM2OTVkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9dmlkZW8lMkZtcDQifQ.UUvXE2epN8NrmbbUQ1ODwWQO19Q3QjjLz3dEAS8dYhQ)

---

Create and manage local macOS and Linux VMs on Apple Silicon using Apple's Virtualization.Framework.

```
/bin/bash -c "$(curl -fsSL https://cua.ai/lume/install.sh)"
```

**Your first result:** create a vanilla macOS Tahoe VM from an Apple restore image, start it, and connect over SSH. The tutorial uses the Lume CLI directly and explains the unattended setup defaults.

**[Create your first Lume VM](https://cua.ai/docs/lume/quickstart)** | **[Installation](https://cua.ai/docs/lume/quickstart)** | **[CLI reference](https://cua.ai/docs/lume/reference/cli)**

---

One SDK and one `cua` command for local VMs and containers, and for any computer that runs [cua-spacesd](/trycua/cua/blob/main/libs/cua-spacesd/README.md).

**macOS / Linux**

```
curl -fsSL https://cua.ai/install.sh | sh
```

**Windows (PowerShell)**

```
irm https://cua.ai/install.ps1 | iex
```

In a terminal the script first says what Cua Spaces is. The command-line tools (the `cua` program) are always installed; you choose whether to add the Cua Spaces app (on by default) and Cua Driver, which lets AI agents use your apps while you keep working (off by default). It then runs `cua auth login`, which signs you in and offers to set up your AI coding agents (Claude Code, Codex, Cursor, and others). The app asks on its first run whether your other devices may use this computer. Add Cua Driver with `sh -s -- --select cua-driver`, or skip the choice with `--only cua-driver`. See [the installer options](/trycua/cua/blob/main/scripts/install/README.md).

```
cua sb create ubuntu --name dev          # a gVisor container, set up on first use
cua sb exec dev uname -a
cua sb screenshot dev
cua sb rm dev
```

The same sandbox from Python:

```
from cua_sandbox import Image, Sandbox

async with Sandbox.ephemeral(Image.linux(), local=True) as sb:
    print((await sb.shell.run("uname -a")).stdout)
```

* **SDK:** the same API in Python (`pip install cua`), TypeScript (`@trycua/cua`) and Rust (`cua-sdk`), running embedded in your process or through a shared `cua daemon`. Swift and Kotlin bindings are not yet released.
* **Sandboxes need no agent inside.** Readiness comes from the runtime and optional port probes. Images that ship cua-spacesd (port 3211) add processes, files, screenshots, input through cua-driver, and low-latency video and audio streaming. There is no agent layer in the SDK either: drive sandboxes from your own harness ([guide](https://cua.ai/docs/cua-sdk/guides/own-harness)).
* **Your own computers.** `cua host setup` makes this computer reachable through the cua.ai relay with no port forwarding.

**[SDK README](/trycua/cua/blob/main/libs/cua/README.md)** | **[Quickstart](https://cua.ai/docs/cua-sdk/quickstart)** | **[CLI reference](https://cua.ai/docs/cua-cli/reference/cli)** | **[Sandbox SDK reference](https://cua.ai/docs/cua-sdk/reference/sandbox)**

---

CUA-S1 is our family of small, specialized System 1 models for computer use. We use "System 1" as an engineering analogy for fast, bounded decisions, such as choosing which value belongs in a field or whether to leave an element alone. It is not a strict classification of model architectures or a replacement for a general-purpose agent's planning and reasoning.

The first research profile focuses on forms: scoring decisions from structured interface elements and document values rather than generating a response token by token. Application code orders the actions, and the optional Cua Driver integration handles execution with explicit action boundaries.

The project includes Python model code, synthetic-data generation, training, and evaluation. The GitHub component is an early, source-only research release; model weights are hosted separately on Hugging Face. The source is MIT-licensed. Check each model and dataset card for its scope, limitations, and artifact-specific license.

**[Explore CUA-S1](/trycua/cua/blob/main/libs/cua-s1)** | **[Model card](/trycua/cua/blob/main/libs/cua-s1/MODEL_CARD.md)** | **[Safety and deployment guidance](/trycua/cua/blob/main/libs/cua-s1/SECURITY.md)**

**CUA-S1-FORMS on Hugging Face:** **[Model weights](https://huggingface.co/cua-ai/cua-s1-forms)** | **[Dataset](https://huggingface.co/datasets/cua-ai/cua-s1-forms)**

---

Build computer-use tasks, evaluate agents, and export trajectories for training. Start with a simulated task that requires no VM, Docker, or model API key.

With Python 3.12 or 3.13 and [uv](https://docs.astral.sh/uv/) installed:

```
uv tool install 'cua-bench[browser]'
uv tool run --from 'cua-bench[browser]' playwright install chromium
```

**Your first result:** create a small task, run its reference solution, and verify that its evaluator reports a reward of `1.0`. Then try the same task yourself.

**[Build your first task](https://cua.ai/docs/cua-bench/quickstart)** | **[What is Cua-Bench?](https://cua.ai/docs/cua-bench)** | **[CLI reference](https://cua.ai/docs/cua-bench/reference/cli)** | **[Partner with us](https://cuabench.ai/)**

---

| Package | Description |
| --- | --- |
| [cua-driver](/trycua/cua/blob/main/libs/cua-driver/README.md) | Background computer-use agent for macOS, Windows, and Linux |
| [cua SDK and CLI](/trycua/cua/blob/main/libs/cua/README.md) | Rust core and the `cua` command: sandboxes, local runtimes, images, Spaces |
| [cua (Python)](/trycua/cua/blob/main/libs/cua/python/README.md) | The cua SDK for Python (`pip install cua`) |
| [@trycua/cua](/trycua/cua/blob/main/libs/cua/typescript/README.md) | The cua SDK for Node and the browser, plus `@trycua/cua/spaces` |
| [Cua (Swift)](/trycua/cua/blob/main/libs/cua/swift/README.md) | The cua SDK for Swift (SwiftPM, XCFramework; not yet released) |
| [cua-sandbox](/trycua/cua/blob/main/libs/python/cua-sandbox/README.md) | High-level Python `Sandbox`/`Image`/`Pool` API, a thin wrapper over the cua SDK |
| [cua-spacesd](/trycua/cua/blob/main/libs/cua-spacesd/README.md) | In-sandbox daemon on port 3211: processes, files, desktop, streaming (gRPC) |
| [Cua Spaces for macOS](/trycua/cua/blob/main/apps/cua-spaces-macos/README.md) | The Spaces app on macOS: menu bar and notch, live streams, teleport, agent threads |
| [Cua Spaces core](/trycua/cua/blob/main/apps/cua-spaces/README.md) | The shared Spaces app core, and the Tauri app for Linux and Windows |
| [cua-bench](/trycua/cua/blob/main/libs/cua-bench/README.md) | Benchmarks and RL environments for computer-use |
| [lume](https://cua.ai/docs/lume/reference/cli) | macOS/Linux VM management on Apple Silicon |

Cua no longer maintains these. They will not receive updates or fixes, their CI/CD is switched off, and existing releases and image tags stay on npm, PyPI and Docker Hub. See [Migrate from deprecated packages](https://cua.ai/docs/cua-sdk/guides/cua-cloud-ended#deprecated-packages).

| Package | Registry | Use instead |
| --- | --- | --- |
| [cuabot](/trycua/cua/blob/main/libs/cuabot/README.md) | npm | **Do not run it:** it has known security issues. Stop it and uninstall it ([how](/trycua/cua/blob/main/libs/cuabot/README.md)), then use Cua Driver or the `cua` CLI. |
| `cua-computer` | PyPI | The [`cua` SDK](#cua-sdk-and-cli) for sandboxes, [Cua Driver](#cua-driver) for the computer you are on |
| `cua-computer-server` | PyPI | Images that ship [cua-spacesd](/trycua/cua/blob/main/libs/cua-spacesd/README.md), or [Cua Driver](#cua-driver) |
| [cua-agent](/trycua/cua/blob/main/libs/python/agent/README.md) | PyPI | A coding agent with the [Cua Driver MCP](https://cua.ai/docs/cua-driver/guides/connect-your-agent), or `sandbox.agents()` in the `cua` SDK |
| [cua-som](/trycua/cua/blob/main/libs/python/som/README.md) | PyPI | [Cua Driver](#cua-driver) |
| [cua-core](/trycua/cua/blob/main/libs/python/core/README.md) | PyPI | [Cua Driver](#cua-driver) or the [`cua` SDK](#cua-sdk-and-cli); [cua-bench](/trycua/cua/blob/main/libs/cua-bench/README.md) still uses the last release |
| [cua-bench-ui](/trycua/cua/blob/main/libs/python/bench-ui/README.md) | PyPI | Nothing: only [cua-bench](/trycua/cua/blob/main/libs/cua-bench/README.md) uses it, at its last release |
| [cua-sandbox-apps](/trycua/cua/blob/main/libs/python/cua-sandbox-apps/README.md) | PyPI | The [`cua` SDK](#cua-sdk-and-cli) |
| [@trycua/core](/trycua/cua/blob/main/libs/typescript/core/README.md), `@trycua/playground` | npm | [`@trycua/cua`](/trycua/cua/blob/main/libs/cua/typescript/README.md) |
| [lumier](/trycua/cua/blob/main/libs/lumier/README.md) | Docker Hub | [Lume](https://cua.ai/docs/lume/reference/cli), or a sandbox from the [`cua` SDK](#cua-sdk-and-cli) |
| [xfce](/trycua/cua/blob/main/libs/xfce/README.md), [xfce-cua](/trycua/cua/blob/main/libs/xfce-cua/README.md), [kasm](/trycua/cua/blob/main/libs/kasm/README.md), [qemu-docker](/trycua/cua/blob/main/libs/qemu-docker/README.md) images | Docker Hub | The images in [libs/images](/trycua/cua/blob/main/libs/images/README.md) (`ghcr.io/trycua/linux`, `windows`, `macos`) through the [`cua` SDK](#cua-sdk-and-cli) |

---

If Cua supports your research, please cite the software:

```
@software{cua2025,
  author  = {{Cua AI, Inc.}},
  title   = {Cua},
  year    = {2025},
  url     = {https://github.com/trycua/cua},
  license = {MIT}
}
```

For reproducibility, include the Cua release or commit used in your experiments. Citation metadata is also available in [`CITATION.cff`](/trycua/cua/blob/main/CITATION.cff).

We welcome contributions. See our [Contributing Guidelines](/trycua/cua/blob/main/.github/CONTRIBUTING.md) for details.

Everything outside Cua Spaces and Cua Driver Bench is MIT-licensed ([LICENSE](/trycua/cua/blob/main/LICENSE.md)): the cua SDK and its Python, TypeScript, Swift and Kotlin packages, the `cua` command and `cua daemon`, Cua Driver, Lume and the rest of this repository unless a directory says otherwise.
Cua Spaces is source-available under [FSL-1.1-MIT](https://fsl.software): the Spaces apps, cua-spacesd, the Cua Keyvault, teleport, Cua Volume (`cua-volume`) and the streaming client, codecs and viewers. The streaming wire protocol stays MIT. It is free to use, self-host and build on, with no competing hosted service, and each release becomes MIT two years after it ships.
Cua Driver Bench (`libs/cua-driver-bench`) is under the same [FSL-1.1-MIT](/trycua/cua/blob/main/libs/cua-driver-bench/LICENSE); versions published before 11 Oct 2026 (#4973, #4978) were MIT.
The MIT parts never depend on the FSL parts. Some subdirectories carry their own licence; [LICENSING.md](/trycua/cua/blob/main/legal/LICENSING.md) lists each one and how the two fit together.
Offering Spaces, or Cua Driver Bench, as a hosted or managed service? See [COMMERCIAL.md](/trycua/cua/blob/main/legal/COMMERCIAL.md). For use of our names and logo, see [TRADEMARKS.md](/trycua/cua/blob/main/legal/TRADEMARKS.md).

Third-party components have their own licenses:

* [Kasm](/trycua/cua/blob/main/libs/kasm/LICENSE) (MIT)
* [`cua-som`](/trycua/cua/blob/main/libs/python/som) is an optional package licensed under
  AGPL-3.0-or-later. Its Ultralytics dependency retains its own license; inspect
  the resolved dependency version and its notices before redistribution.
* The Microsoft OmniParser repository [states
  CC-BY-4.0](https://github.com/microsoft/OmniParser/blob/master/LICENSE) for its
  repository content. Model files downloaded from the separate OmniParser model
  repository are distinct artifacts; verify the terms published with the exact
  model revision before redistributing them.
* The optional `cua-perception` extension is installed separately from the MIT
  Cua Driver, from the signed assets of a `cua-perception-v<version>` GitHub
  release. Each release combines an AGPL-3.0-only OmniParser model artifact,
  Apache-2.0 PP-OCR model artifacts, and a separately packaged ONNX Runtime.
  The extension is not MIT licensed. Redistributing it, or offering it
  to users over a network, can trigger AGPL-3.0 source obligations. Cua does
  not relicense the detector and cannot grant other terms for it. Read the
  [perception third-party notices and precautions](/trycua/cua/blob/main/libs/cua-driver/docs/perception-third-party-notices.md)
  before you install, redistribute, or host an extension artifact.

Apple, macOS, Ubuntu, Canonical, and Microsoft are trademarks of their respective owners. This project is not affiliated with or endorsed by these companies.

---

## Sponsors
