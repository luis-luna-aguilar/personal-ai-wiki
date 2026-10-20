---
title: GitHub - openclaw/Peekaboo: Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models. · GitHub
type: source
source_type: repo
url: https://github.com/openclaw/Peekaboo
fetched: 2026-10-19
---

# GitHub - openclaw/Peekaboo: Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models. · GitHub

# Peekaboo 🫣 — Mac automation that sees the screen and does the clicks.

[![CI](https://camo.githubusercontent.com/949ee3e9c3823ec38aaed21680138e48f239b0d6f02dd056131f89c0a308b8c1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f6f70656e636c61772f5065656b61626f6f2f6d61636f732d63692e796d6c3f6272616e63683d6d61696e267374796c653d666c61742d737175617265266c6162656c3d6369)](https://github.com/openclaw/Peekaboo/actions/workflows/macos-ci.yml) [![npm](https://camo.githubusercontent.com/43710ce1548a93d4200b2664773e38e81edad457a1667d9ac62893fd8be5a428/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f25343073746569706574652532467065656b61626f6f3f7374796c653d666c61742d737175617265)](https://www.npmjs.com/package/@steipete/peekaboo) [![GitHub release](https://camo.githubusercontent.com/6178dd2186c31c8c862aa7deede0a275a1d4169a4531ca4ca8f518e76c80ab43/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6f70656e636c61772f5065656b61626f6f3f7374796c653d666c61742d737175617265)](https://github.com/openclaw/Peekaboo/releases/latest) [![macOS 15+](https://camo.githubusercontent.com/897843a2e81c22b0fb93f2f6e04cd51b6fd22aa9ddbaf5757778392c1dbeb3af/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61634f532d31352532422d3030373864373f6c6f676f3d6170706c65266c6f676f436f6c6f723d7768697465267374796c653d666c61742d737175617265)](/openclaw/Peekaboo/blob/main/docs/platform-support.md) [![Swift 6.2](https://camo.githubusercontent.com/d398caa3c72827ef2e3d17adb0f89f6f3a954115b8b58f9a6f5ca17ea6edbf28/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53776966742d362e322d4630353133383f6c6f676f3d7377696674266c6f676f436f6c6f723d7768697465267374796c653d666c61742d737175617265)](https://swift.org/) [![Node](https://camo.githubusercontent.com/fa803ed92267d6b9ed006b31a3954457c75037fbaea6252c41a5c9bfda52ef51/68747470733a2f2f696d672e736869656c64732e696f2f6e6f64652f762f25343073746569706574652532467065656b61626f6f3f7374796c653d666c61742d737175617265)](https://nodejs.org/) [![License](https://camo.githubusercontent.com/ee93445315d4eb69d9c9e2f8cd273ad220e45ad75c24f1052a0de70d34ae3682/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6f70656e636c61772f5065656b61626f6f3f7374796c653d666c61742d737175617265)](/openclaw/Peekaboo/blob/main/LICENSE) [![Homebrew](https://camo.githubusercontent.com/2d56ac43cd76f3a2389a03b46de44e00660e977caf529b9616c994c41654aba0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f486f6d65627265772d6f70656e636c61772532467461702d6232386636323f6c6f676f3d686f6d6562726577266c6f676f436f6c6f723d7768697465267374796c653d666c61742d737175617265)](https://github.com/openclaw/homebrew-tap) [![Ask DeepWiki](https://camo.githubusercontent.com/2db54e97cb0e3c43121504735a9be28db62a330a722aa14be3fee6ca64cd13a7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f41736b2d4465657057696b692d3030383863633f7374796c653d666c61742d737175617265)](https://deepwiki.com/openclaw/Peekaboo)

Peekaboo is a macOS CLI and menu-bar app for screen capture, accessibility inspection, and native UI automation. Use it directly, let its agent plan multi-step work, or expose the same toolset to MCP clients.

[![Peekaboo banner](/openclaw/Peekaboo/raw/main/assets/peekaboo.png)](/openclaw/Peekaboo/blob/main/assets/peekaboo.png)

The released CLI and app require macOS 15 or later.

```
brew install openclaw/tap/peekaboo
```

The npm package requires Node.js 22 or later and includes the CLI plus its MCP launcher.

```
npx -y @steipete/peekaboo --version
```

See [MCP setup](/openclaw/Peekaboo/blob/main/docs/MCP.md) to connect it to Codex, Claude Code, Cursor, or another MCP client.

Download the signed DMG from the [latest GitHub release](https://github.com/openclaw/Peekaboo/releases/latest). The menu-bar app provides permission onboarding, visual feedback, and agent sessions; install the CLI separately when you also need `peekaboo` on `PATH`.

For source builds and alternative install details, see the [installation guide](/openclaw/Peekaboo/blob/main/docs/install.md).

Check the permissions available to Peekaboo, then take a screenshot:

```
peekaboo permissions status
peekaboo see --no-elements --mode screen --path /tmp/peekaboo-screen.png
```

Screen capture requires Screen Recording permission. Accessibility permission enables UI inspection and control; the [permissions guide](/openclaw/Peekaboo/blob/main/docs/permissions.md) covers setup and the additional permission used for synthetic input.

Inspect a running app to get a structured UI map with opaque element IDs:

```
peekaboo see --app Finder --json
```

That is the core loop: observe the current screen, choose an element from the result, and act on it.

Peekaboo 4.9.5 is a fix release. Unsigned source builds, such as Homebrew core's `peekaboo` formula, now run commands in-process immediately instead of waiting on or aborting at a daemon they cannot trust, and developers can opt in to trusting their own exact-binary daemon with `PEEKABOO_ALLOW_UNSIGNED_DAEMON=1`. Commands no longer start an on-demand daemon that a granted Peekaboo.app would outrank, `see` stops flagging complete Accessibility reads as incomplete, and released CLI binaries no longer carry the build machine's toolchain path. See the changelog for details.

List Safari's windows, copy the intended `window_id` (`12345` below), then keep the entire interaction pinned to
that exact window:

```
peekaboo window list --app Safari --json
peekaboo click "Address and search bar" --app Safari --window-id 12345
peekaboo type "github.com/openclaw/Peekaboo" --app Safari --window-id 12345
peekaboo press Return --app Safari --window-id 12345
```

Targeted semantic and typed CLI input uses background delivery when Peekaboo can resolve the process, so the app does
not have to become frontmost. Raw CLI `press` chords can also stay background with an exact window selector. The CLI
also accepts a fresh exact non-dialog snapshot; that snapshot is required by background-only Agent/MCP policy.
App/PID-only and targetless chords require explicit foreground consent, as do window-selector-only Agent/MCP chords.
Prefer a semantic action such as `menu click` when one exists. See the
[automation guide](/openclaw/Peekaboo/blob/main/docs/automation.md) for element IDs, coordinates, snapshots, waits, and input behavior.

The agent combines the same observation and action tools into a natural-language run:

```
peekaboo agent "Open Safari, go to github.com, and search for Peekaboo" --allow-foreground
```

Agent runs need a configured model provider. See [agent setup](/openclaw/Peekaboo/blob/main/docs/commands/agent.md) for providers and sessions, or [MCP setup](/openclaw/Peekaboo/blob/main/docs/MCP.md) to expose Peekaboo's tools to another client.

| Goal | Commands | Guide |
| --- | --- | --- |
| Observe the desktop | `see`, `screen list`, `window list` | [Capture and inspection](/openclaw/Peekaboo/blob/main/docs/quickstart.md) |
| Interact with UI | `click`, `type`, `press`, `scroll`, `drag`, `set-value`, `action` | [Automation](/openclaw/Peekaboo/blob/main/docs/automation.md) |
| Control macOS | `app`, `window`, `menu`, `menubar`, `dock`, `dialog`, `space` | [Command reference](/openclaw/Peekaboo/blob/main/docs/commands/README.md) |
| Run workflows | `agent`, `capture` | [Agent](/openclaw/Peekaboo/blob/main/docs/commands/agent.md) · [Capture](/openclaw/Peekaboo/blob/main/docs/commands/capture.md) |
| Integrate with clients | `mcp`, `browser`, `tools` | [MCP](/openclaw/Peekaboo/blob/main/docs/MCP.md) |

Run `peekaboo help <command>` for live CLI help. The [complete command index](/openclaw/Peekaboo/blob/main/docs/commands/README.md) links to flags, examples, and troubleshooting for every command.

Peekaboo stores provider credentials and settings under `~/.peekaboo`. Use `peekaboo config` to inspect or change them, and consult the [configuration guide](/openclaw/Peekaboo/blob/main/docs/configuration.md) for profiles, environment variables, and custom providers. The [provider reference](/openclaw/Peekaboo/blob/main/docs/providers.md) covers hosted, compatible, and local model backends.

Shell completions for zsh, bash, and fish come from `peekaboo completions`; see the [completion guide](/openclaw/Peekaboo/blob/main/docs/commands/completions.md) for persistent setup.

## Community

Source builds require macOS 15 or later, Swift 6.2 or later, Node.js 22 or later, and the repository's submodules.

```
pnpm install --frozen-lockfile
pnpm run build:cli
pnpm run lint:docs
pnpm run test:safe
```

More build, signing, and test details live in [docs/building.md](/openclaw/Peekaboo/blob/main/docs/building.md).

MIT. See [LICENSE](/openclaw/Peekaboo/blob/main/LICENSE).
