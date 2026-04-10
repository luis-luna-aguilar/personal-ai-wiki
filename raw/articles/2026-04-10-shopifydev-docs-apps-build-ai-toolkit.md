---
title: Shopify AI Toolkit
type: source
source_type: article
url: https://shopify.dev/docs/apps/build/ai-toolkit
fetched: 2026-04-10
---

# Shopify AI Toolkit

# Shopify AI Toolkit

Ask assistant

The Shopify AI Toolkit connects your AI tools to the Shopify platform. With the Toolkit, you can build apps using Shopify's documentation, API schemas, and code validation, and manage your Shopify store through the CLI's store execute capabilities. The Toolkit ensures your agent works with Shopify correctly, rather than guessing at how things are implemented.

You can set up the AI Toolkit via our plugin, or manually with skills or MCP:

---

Before you install the Shopify AI Toolkit, make sure you have:

* Node.js 18 or higher installed on your system.
* A supported AI tool: Claude Code, Codex (skills and MCP only), Cursor, Gemini CLI, or Visual Studio Code

---

Plugins are the recommended way to install the AI Toolkit. The plugin bundles everything into a single install and updates automatically as new capabilities are released.

#### Claude Code

1. In Claude Code, enable the Shopify marketplace:
2. Then, install the plugin:

#### Gemini CLI

In your terminal, run `gemini extensions install`:

#### VS Code

1. Ensure the [Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins) preview is enabled in your VS Code settings.
2. Open the Command Palette (`Cmd+Shift+P` on MacOS, `Ctrl+Shift+P` on Windows/Linux) and run:
3. Enter the repository URL:

1. In Claude Code, enable the Shopify marketplace:
2. Then, install the plugin:

---

If you prefer to pick specific capabilities, you can manually add individual agent skills. You can [browse the full list of available skills](https://github.com/Shopify/Shopify-AI-Toolkit/tree/main/skills) on GitHub. Note that manually added skills don't auto-update, so you'll need to pull updates yourself.

To install all skills:

To install a single skill, use the `--skill` flag. For example, to install only the GraphQL Admin API skill:

---

If you prefer MCP, you can connect to Shopify's developer resources through the Dev MCP server. The server runs locally and doesn't require authentication.

#### Claude Code

1. In your terminal, tell `claude` to add the MCP server:
2. Restart Claude Code to load the new configuration.

#### Codex CLI

1. Add this configuration to your `~/.codex/config.toml` file:

   Codex uses TOML format with `mcp_servers` (snake\_case) instead of JSON with `mcpServers` (camelCase). For more information, see the [Codex MCP documentation](https://github.com/openai/codex/blob/main/docs/config.md#mcp_servers).

   **Note:**

   Codex uses TOML format with `mcp_servers` (snake\_case) instead of JSON with `mcpServers` (camelCase). For more information, see the [Codex MCP documentation](https://github.com/openai/codex/blob/main/docs/config.md#mcp_servers).
2. Restart Codex to load the new configuration.

#### Cursor

1. Open Cursor and go to **Cursor** > **Settings** > **Cursor Settings** > **Tools and MCP** > **New MCP server**.
2. Add this configuration to your MCP servers (or [use this link](https://cursor.com/en/install-mcp?name=shopify-dev-mcp&config=eyJjb21tYW5kIjoibnB4IC15IEBzaG9waWZ5L2Rldi1tY3BAbGF0ZXN0In0%3D) to add it automatically):

   If you see connection errors on Windows, try this alternative configuration:
3. Save your configuration and restart Cursor.

#### Gemini CLI

1. Add this configuration to your `settings.json` file:

   **Note:**

   To make the server available across all projects, add the `--scope user` flag. For more information, see the [Gemini CLI MCP documentation](https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html).
2. Restart Gemini CLI to load the new configuration.

#### VS Code

1. Open VS Code and open the Command Palette (`Cmd+Shift+P` on MacOS, `Ctrl+Shift+P` on Windows/Linux).
2. Search for and select **MCP: Open User Configuration**.
3. Add this configuration to your user-level `mcp.json` file:
4. Save your configuration and restart VS Code.

1. In your terminal, tell `claude` to add the MCP server:
2. Restart Claude Code to load the new configuration.

---

---

Was this page helpful?

YesNo
