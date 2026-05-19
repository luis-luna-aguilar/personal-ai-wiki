---
type: proposal
source: raw/newsletters/2026-05-16-ainews-cerebras-60b-ipo-slowly-then-all-at-o.md
status: pending
created: 2026-05-18
---

# Proposal: Codex adoption metrics + ecosystem expansion

## Summary

Codex hit 4M+ weekly active users and 5× messages/user growth; 1M+ app downloads in first week. Ecosystem expansion: Ollama added Codex support, MagicPath canvas ships inside Codex, /goal extracted as portable MCP slash command, Zed supports ChatGPT subscription access. VS Code/Copilot team publicly confirmed the harness-over-model thesis.

_Note: `proposals/2026-05-18-codex-maxxing-patterns.md` also updates `wiki/tools/codex.md`. Apply this proposal first._

## Intended changes

- [x] **Update** `wiki/tools/codex.md` — update `as_of`, add source to frontmatter, update adoption metrics, add ecosystem items, add Recent changes entry
    > **`as_of`:** `2026-05-13` → `2026-05-18`
    >
    > **Sources frontmatter:** add `codex-adoption-ecosystem-2026-05`
    >
    > **Add to Current status (top bullet area):**
    > ```md
    > - 4M+ weekly active users; 5× messages/user growth; 1M+ app downloads in first week of launch
    > - Ollama added Codex app support, enabling local/open-model launch paths alongside cloud Codex
    > - MagicPath canvas now ships natively inside Codex for visual task planning
    > - /goal command extracted into portable MCP/slash-command form by community (@secemp9) — now usable outside ChatGPT
    > - Zed editor supports ChatGPT/Codex on existing ChatGPT subscription (same rate-limit model)
    > - GitHub Copilot App: agent merge feature; terminal commands get AI-generated risk assessment badges with explanations
    > - VS Code/Copilot team: "experience shaped by coding harness — context assembly, tool use, execution loops, memory — more than by the base model alone" — the harness-over-model thesis confirmed by a lab-adjacent team
    > ```
    >
    > **Add to Recent changes (top):**
    > `- [2026-05-16] 4M+ WAU, 5× messages/user, 1M+ app downloads; Ollama Codex support; MagicPath canvas; /goal as portable MCP; Zed subscription parity; VS Code/Copilot team confirms harness-over-model thesis`

- [x] **Spill** `wiki/tools/codex.md` → `wiki/history/tools/codex.md` — Recent changes at cap (10); oldest entry falls off
    > **Create** `wiki/history/tools/codex.md` (does not exist yet):
    >
    > ```md
    > # Codex — History
    >
    > - [2026-04-10] Page created from OpenAI Pro tier pricing announcement
    > ```

- [ ] **Update** `wiki/state-of/coding.md` — update `as_of`, add source to frontmatter, add harness-over-model confirmation, add Recent changes entry
    > **`as_of`:** `2026-05-13` → `2026-05-18`
    >
    > **Sources frontmatter:** add `codex-adoption-ecosystem-2026-05`
    >
    > **Add to Recent changes (top):**
    > `- [2026-05-16] VS Code/Copilot team confirms: competitive differentiation is harness (context assembly, tool use, execution loops, memory), not base model — harness-over-model thesis now lab-adjacent confirmed`

- [x] **Spill** `wiki/state-of/coding.md` → `wiki/history/state-of/coding.md` — Recent changes at cap (10); oldest entry falls off
    > File already exists. Append to `wiki/history/state-of/coding.md`:
    > `- [2026-03-07] Claude Code added local scheduled tasks and /loop, making recurring background coding work a first-class terminal-agent primitive`

- [x] **Create** `wiki/sources/newsletters/codex-adoption-ecosystem-2026-05.md`
    > See draft below

## Page drafts

### wiki/sources/newsletters/codex-adoption-ecosystem-2026-05.md (new)

```md
---
title: Codex adoption + ecosystem expansion — AINews coverage
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-16-ainews-cerebras-60b-ipo-slowly-then-all-at-o.md
published: 2026-05-16
ingested: 2026-05-18
domains: [coding]
---

# Codex adoption + ecosystem expansion — AINews coverage

AINews coverage of Codex growth and ecosystem expansion. Adoption: 4M+ weekly active users, 5× messages/user, 1M+ app downloads in first week. Ecosystem: Ollama added Codex app support for local/open-model paths; MagicPath canvas ships natively inside Codex; /goal extracted into portable MCP slash command by @secemp9; Zed editor supports ChatGPT subscription access with same rate-limit model; GitHub Copilot App added agent merge feature and terminal risk assessment badges. VS Code/Copilot team (@code, @pierceboggan): "experience shaped by coding harness — context assembly, tool use, execution loops, memory — more than by the base model alone." Same newsletter also covers Cerebras IPO.

## Influenced pages

- [Codex](../../tools/codex.md) — adoption metrics, ecosystem expansion
- [State of Coding](../../state-of/coding.md) — harness-over-model confirmed

## Key claims extracted

- 4M+ weekly active users; 5× messages/user; 1M+ app downloads in first week
- Ollama: Codex app support added (local/open-model paths)
- MagicPath canvas: ships natively inside Codex
- /goal: extracted into portable MCP slash command form by @secemp9
- Zed: ChatGPT subscription access with same rate-limit model
- GitHub Copilot App: agent merge feature; terminal risk assessment badges
- VS Code/Copilot team: "experience shaped by coding harness — context assembly, tool use, execution loops, memory — more than by the base model alone"
```
