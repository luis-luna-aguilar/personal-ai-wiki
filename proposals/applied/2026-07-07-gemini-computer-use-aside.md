---
type: proposal
sources:
  - raw/newsletters/2026-06-25-chinese-grey-market-sells-claude-api-access.md
  - raw/newsletters/2026-06-25-googles-talent-exodus-continues.md
  - raw/newsletters/2026-06-26-ainews-openai-reports-median-internal-codex-outp.md
  - raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md
status: pending
created: 2026-07-07
---

# Proposal: Gemini computer use and Aside agentic browser

## Summary

Google made computer use a built-in Gemini 3.5 Flash tool for browser, desktop, and mobile agents, with developer API access and safety controls such as sensitive-action confirmation and automated stops on prompt-injection detection. In parallel, Aside launched an agentic browser that uses local browsing history and autofill to act across logged-in websites. Together they push computer use from demos toward mainstream product surfaces.

## Intended changes

- [x] **Update** `wiki/state-of/computer-use.md` — add Gemini 3.5 Flash computer use as a current mainstream computer-use entry.
    > Add Gemini line: built-in computer-use tool for browser/desktop/mobile, Gemini API access, confirmations for sensitive actions, automated stop on prompt-injection detection *(as of 2026-06-25)*.
    >
    > Add caveated Aside note under Computer use: agentic browser using local browsing history and autofill for logged-in sites; benchmark claims secondary until primary source is fetched.

- [x] **Update** `wiki/tools/gemini.md` — add computer-use capability to Gemini page.
    > Add `Computer use (as of 2026-06-25)` section with browser/desktop/mobile action interface, API docs, sensitive-action confirmation, and prompt-injection stop behavior.

- [x] **Create** `wiki/sources/newsletters/gemini-computer-use-aside-2026-06.md` — source summary.
    > See draft below.

## Page drafts

### wiki/state-of/computer-use.md (updated snippets)

```markdown
---
as_of: 2026-06-25
sources: [..., gemini-computer-use-aside-2026-06]
---

### Computer use

- [Gemini](../tools/gemini.md) — Google; Gemini 3.5 Flash adds built-in computer use across browser, desktop, and mobile with API access, sensitive-action confirmation, and prompt-injection-triggered task shutdown *(as of 2026-06-25)*
- **Aside** — agentic browser using local on-device browsing history and autofill to act across logged-in websites; benchmark leadership claims remain secondary until primary source is fetched *(as of 2026-06-25)*

## Recent changes

- [2026-06-25] Gemini 3.5 Flash computer use moves browser/desktop/mobile action into a mainstream Gemini API tool; Aside launches as a browser-native computer-use product.
```

### wiki/tools/gemini.md (updated snippets)

```markdown
---
domains: [models, computer-use]
as_of: 2026-06-25
sources: [..., gemini-computer-use-aside-2026-06]
---

## Computer use (as of 2026-06-25)

Gemini 3.5 Flash now has computer use as a built-in developer capability across browser, desktop, and mobile workflows. Newsletter coverage describes it as a standardized action interface exposed through the Gemini API, with human confirmation for sensitive actions and automatic shutdown when prompt-injection behavior is detected.

The significance is productization: Google is putting computer-use primitives into a mainstream Gemini model/API path rather than leaving them as a separate demo or bespoke agent environment.

## Recent changes

- [2026-06-25] Gemini 3.5 Flash adds built-in computer use for browser, desktop, and mobile with sensitive-action confirmations and prompt-injection shutdown behavior.
```

### wiki/sources/newsletters/gemini-computer-use-aside-2026-06.md (new)

```markdown
---
title: Gemini computer use and Aside agentic browser
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-25-chinese-grey-market-sells-claude-api-access.md
url: https://ai.google.dev/gemini-api/docs/computer-use
published: 2026-06-25
ingested: 2026-07-07
domains: [computer-use, agents]
---

# Gemini computer use and Aside agentic browser

Newsletter coverage reports Google made computer use a built-in Gemini 3.5 Flash capability across browser, desktop, and mobile, exposed through the Gemini API with human confirmation for sensitive actions and automated task stopping on prompt-injection detection. Separate Superhuman coverage describes Aside as an agentic browser using local browsing history and autofill to act across logged-in websites.

## Influenced pages

- [State of Computer Use](../../state-of/computer-use.md) — adds Gemini computer-use entry and caveated Aside note.
- [Gemini](../../tools/gemini.md) — adds computer-use capability.

## Key claims extracted

- Gemini 3.5 Flash computer use supports browser, desktop, and mobile action patterns.
- Developer access is through the Gemini API.
- Safety controls include sensitive-action confirmations and prompt-injection-triggered shutdown.
- Aside claims an agentic browser that uses local on-device browsing history and autofill to access logged-in sites.
- Browser-agent benchmarks such as OSWorld 2.0 and Ecom Bench appear in the same source cluster.
```

## Schema / vocabulary additions

None.
