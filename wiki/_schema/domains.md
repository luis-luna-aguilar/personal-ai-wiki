# Domains — controlled vocabulary

Valid values for the `domains:` field in frontmatter. A page may have multiple domains.

Domains are high-level areas of use. They correspond to state-of pages in `wiki/state-of/`. Adding a new domain is a significant decision — it usually means a new state-of page will be created.

## Current domains

- **`coding`** — software development, code generation, pair programming, refactoring, testing
- **`agents`** — agentic systems, tool use, multi-step autonomy, orchestration
- **`models`** — foundation models themselves (as distinct from tools built on them)
- **`legal`** — legal practice: law firms, in-house teams, contracts, matters, compliance, governance of AI deployment
- **`computer-use`** — AI agents that operate through application UIs, connect to third-party services, and execute multi-step workflows on behalf of users
- **`finance`** — AI applied to personal and institutional finance: budgeting, investment tracking, financial data analysis, fintech integrations
- **`science`** — AI applied to scientific research: data analysis at scale, experiment automation, accelerating discovery
- **`creative`** — AI tools for image, video, slides, avatar, and UI generation
- **`healthcare`** — AI applied to clinical workflows, medical knowledge, transcription, patient operations, and healthcare delivery
- **`cybersecurity`** — AI applied to security: attack surface analysis, vulnerability detection, supply chain risk, and AI-specific threat vectors

## Conventions

- Domain names are lowercase, single-word or hyphenated. Examples: `coding`, `agents`, `marketing`, `data-analysis`.
- A tool that applies to multiple domains lists them all explicitly. There is no wildcard.
- "misc" is not a valid domain. If something doesn't fit, propose a new domain or leave the domain off.

## Adding a new domain

1. Propose in a proposal file under a "Schema / vocabulary additions" section.
2. Once approved, add the entry here with a one-line description.
3. Create a corresponding `wiki/state-of/<domain>.md` skeleton.
