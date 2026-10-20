---
title: Getting Started with Local MCP Servers on Claude Desktop
type: source
source_type: article
url: https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop
fetched: 2026-10-19
---

# Getting Started with Local MCP Servers on Claude Desktop

Skip to main content
API docs
Release notes
How to get support
English
Français
Deutsch
Bahasa Indonesia
Italiano
日本語
한국어
Português
Pусский
简体中文
Español
繁體中文
English
Search
⌘
K
Claude
Pro and Max plans
Team and Enterprise plans
Identity management (SSO, JIT, SCIM)
Claude Cowork
Claude Code
Claude Desktop
General
Desktop extensions
Enabling and using the desktop extension allowlist
Deploying enterprise-grade MCP servers with desktop extensions
Getting Started with Local MCP Servers on Claude Desktop
Claude Mobile apps
Claude API and Console
Connectors
Claude in Chrome
Claude for Education
Privacy and legal
Safeguards
Amazon Bedrock
All Collections
Claude Desktop
Desktop extensions
Getting Started with Local MCP Servers on Claude Desktop
Getting Started with Local MCP Servers on Claude Desktop
Updated over 3 weeks ago
Copy for LLM

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. With the introduction of desktop extensions, installing and managing local MCP servers has become significantly easier.

 

Desktop Extensions

Desktop extensions provide a streamlined way to install and manage local MCP servers through single-click installable packages. Instead of manually configuring JSON files and managing dependencies, you can now install local MCP servers on your computer as easily as browser extensions.

Note: If you’re a developer who wants to list a desktop extension (a local MCP server for Claude Desktop) in the directory, submit it through the desktop extension submission form. To submit a plugin or a remote connector instead, use the developer portal. See Submitting your plugin for what each route accepts.

 

Installing desktop extensions from the directory

Navigate to Settings > Extensions on Claude Desktop.

Click “Browse extensions” to view our directory and click on any Anthropic-reviewed tools you want to use. Click "Install" on your desired extension.

Configure any required settings (like API keys) through the user-friendly interface.

The extension will automatically be available in your conversations.

 

Installing custom desktop extensions

Navigate to Settings > Extensions on Claude Desktop.

Click “Advanced settings” and find the Extension Developer section.

Click “Install Extension…”

Select the .mcpb file and follow the prompts to install.

 

Admin Controls for Desktop Extensions

Owners and Primary Owners of Team and Enterprise plans can manage team access to desktop extensions using two controls:

Enable or disable public desktop extensions depending on your organization’s security standards.

Upload custom desktop extensions and make them available to your team for one-click install.

These controls allow organizations to fully customize their registries by adding only the extensions the team needs to access, and removing any others.

 

Enabling/disabling specific extensions on Team and Enterprise plans

Owners and Primary Owners of Team and Enterprise organizations can manage which desktop extensions are enabled for your organization and accessible to other members via Claude Desktop. See Enabling and using the desktop extension allowlist

for specific instructions.

 

Create and upload custom extensions for your organization

Custom desktop extensions uploads allow Team and Enterprise plans to leverage organization-specific workflows that aren’t available in the public directory. After creating a custom desktop extension, Owners and Primary Owners can navigate to Settings > Extensions within Claude Desktop and click “Advanced settings”  to access the Extension Developer section:

 

 

Click “Install Extension…” and select the .mcpb file. Follow the prompts to install and configure your custom desktop extension. For more in-depth information, please refer to our desktop extension developer documentation.

 

Enterprise Policy Controls

Note: Enterprise policy controls at the user-machine level will override any in-app controls (blocklist and allowlist). If you want to use an in-app control, ensure isDesktopExtensionEnabled and isDesktopExtensionDirectoryEnabled are not set to "false" so the allowlist can populate the available registry.

For controlling desktop extensions through system policies, please refer to our desktop enterprise configuration documentation.

 

Troubleshooting desktop extension installation issues
Extension won't install

Ensure you're running the latest version of Claude Desktop.

Check that the extension file isn't corrupted by re-downloading it.

Verify you have sufficient disk space for the installation.

Extension appears installed but tools aren't available

Restart Claude Desktop to refresh the extension registry.

Check the extension's configuration settings for missing required fields.

Verify any API keys or authentication credentials are entered correctly.

Extension configuration issues

Navigate to Settings > Extensions and click on the extension to review its settings.

Ensure all required configuration fields are completed.

Check that file paths (if applicable) point to existing directories you have access to.

Permission or security errors

On macOS, check System Preferences > Security & Privacy if you receive security warnings.

On Windows and Linux, ensure Claude Desktop has necessary permissions to access required directories.

For enterprise environments, verify that desktop extensions are enabled through your organization's policies.

 

Developer FAQ
How do I check if my MCP servers are properly connected in Claude Desktop?

Click the "+" button on bottom the chat box within Claude Desktop, then select "Connectors." This will show you connected MCP servers and their tools. Alternatively, you can visit Developer settings (under Desktop app) to see connection status and look at the logs for any MCP servers.

 

How do I convert my existing MCP server to a desktop extension?

Add a manifest.json file to your MCP server directory with the required metadata.

Package it using the mcpb pack command.

See the MCPB documentation for detailed instructions.

What programming languages are supported for desktop extensions?

Desktop extensions support Node.js, Python, and binary MCP servers. Claude Desktop includes a built-in Node.js environment, so Node.js installation isn't required.

 

How do I handle sensitive configuration like API keys?

Mark configuration fields as "sensitive": true in your manifest.json. Claude Desktop will automatically encrypt these values using the operating system's secure storage (Keychain on macOS, Credential Manager on Windows, and your distro’s keychain manager on Linux).

 

Can I distribute my custom desktop extension privately?

Yes, you can share .mcpb files directly with specific users or teams. For broader distribution, you can submit extensions to the official directory.

 

How do I debug issues with my desktop extension?

Enable debug logging in Claude Desktop settings, check the extension logs in the Extensions settings panel, and refer to the MCP debugging guide for protocol-specific troubleshooting.

 

What happens when my extension needs updates?

Extensions from the official directory update automatically by default. For privately distributed extensions, users will need to install updated .mcpb files manually.

 

Interested in learning more about MCP?

For more in-depth information on building your own MCP clients and servers, we recommend reviewing the following resources:

MCP Quickstart Guide - A step-by-step tutorial perfect for getting started with basic MCP integration.

Model Context Protocol Github - Contains the complete technical documentation, code examples, and implementation guides.

Guide to debugging MCP integrations - Troubleshooting tips and solutions for common implementation challenges.

If you need further guidance, visit our guide on How to Get Support for additional support options.

Did this answer your question?
Disappointed Reaction
Neutral Reaction
Smiley Reaction
Related Articles
Install Claude Desktop
Get started with custom connectors using remote MCP
Use connectors to extend Claude's capabilities
Deploy Claude Desktop for macOS
Deploying enterprise-grade MCP servers with desktop extensions
On this page
Desktop Extensions
Installing desktop extensions from the directory
Installing custom desktop extensions
Admin Controls for Desktop Extensions
Enterprise Policy Controls
Troubleshooting desktop extension installation issues
Developer FAQ
Interested in learning more about MCP?
Product
Research
Company
News
Careers
Terms of Service - Consumer
Terms of Service - Commercial
Privacy Policy
Usage Policy
Responsible Disclosure Policy
Compliance
