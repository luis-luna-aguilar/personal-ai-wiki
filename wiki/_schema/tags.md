# Tags — controlled vocabulary

Valid values for the `tags:` field in frontmatter. Tags are for cross-cutting attributes that don't fit into domain or subcategory — company, modality, license, etc.

## Current tags

- **`anthropic`** — vendor/org: Anthropic
- **`github`** — vendor/org: GitHub (Microsoft)
- **`open-source`** — license/openness: publicly available source code under an OSS license
- **`closed-source`** — license/openness: proprietary, no public source
- **`cli`** — ecosystem: tool is distributed primarily as a command-line interface
- **`beta`** — flavor: pre-GA product (public or private beta)
- **`spec-driven`** — flavor: aligned with the spec-driven-development approach
- **`agentic`** — flavor: agent-centric product or workflow (multi-step, autonomous, tool-using)

## Conventions

- Tags are lowercase, hyphenated. Examples: `anthropic`, `open-source`, `frontier`, `voice`, `rag`.
- Prefer a small set of tags used widely over a large set of tags used once each.
- If you find yourself wanting a tag for a single page, consider whether it belongs in the page body instead.

## Categories of tags

As the wiki grows, tags tend to cluster into:

- **Vendor / org**: `anthropic`, `openai`, `google`, `meta`, `mistral`
- **License / openness**: `open-source`, `closed-source`, `open-weights`
- **Modality**: `text`, `voice`, `vision`, `multimodal`
- **Flavor / capability**: `frontier`, `reasoning`, `agentic`, `long-context`
- **Ecosystem**: `vscode-fork`, `cli`, `ide-extension`, `terminal`

## Adding a new tag

1. Propose in a proposal file under "Schema / vocabulary additions".
2. On approval, append here with a one-line description.
3. `scripts/tag_compliance.py` will flag any tag not listed in this file.
