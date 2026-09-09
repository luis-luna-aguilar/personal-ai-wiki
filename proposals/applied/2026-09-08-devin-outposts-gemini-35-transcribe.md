---
type: proposal
sources:
  - raw/tweets/2026-09-07-cognition-2079612229318848582.md
  - raw/tweets/2026-09-07-sundarpichai-2092659467284517088.md
status: pending
created: 2026-09-08
---

# Proposal: Devin Outposts and Gemini 3.5 Transcribe

## Summary

### The source

Two smaller, single-source product announcements. Cognition's launch thread introduces **Devin Outposts**: Devin's planning and inference loop continues running in Cognition's cloud, but command execution, file edits, and repository access can now run on infrastructure the customer controls — a Mac mini, a lab GPU box, a VM inside a private network, or a Kubernetes cluster. Cognition shipped launch-partner deployment guides with Cloudflare (isolated sandbox on Cloudflare's edge, with customizable proxies and private connectivity), Daytona (sub-90ms snapshot-started Linux/Windows sandboxes), E2B (fast configurable cloud sandboxes reaching into a private cloud), Modal (same GPU infrastructure used for training/serving, so Devin can reproduce failures and profile fixes on production hardware), and Namespace (an M5-powered Mac with Xcode and computer use, for autonomously building and testing Apple-platform apps). Separately, Google's Sundar Pichai announced **Gemini 3.5 Transcribe**, a new speech-understanding model: multi-speaker intent detection, automatic detection of 85+ languages out of the box, and custom vocabulary adaptation for specialized jargon, available now via the Gemini API in Google AI Studio and Gemini Enterprise.

### What changes

`tools/devin.md` already documents Devin's evolution into persistent operational roles (Auto-Triage, Security Swarm, Devin Fusion); this proposal adds Devin Outposts as a new bullet describing the local/cloud infrastructure split, alongside a Recent-changes entry. `tools/gemini.md` already tracks Gemini's assistant/enterprise/API surfaces in detail; this proposal adds Gemini 3.5 Transcribe as a new bullet and Recent-changes entry.

### What to weigh

Both items come from tweet threads (Cognition's own launch thread, Pichai's own announcement) rather than a blog post or press release with full technical detail — reasonably strong as primary vendor announcements go, but thinner than a dedicated launch article for either product.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/devin.md` — add Devin Outposts bullet, bump `as_of`, add Recent-changes entry
    > See draft below

- [ ] **Update** `wiki/tools/gemini.md` — add Gemini 3.5 Transcribe bullet, bump `as_of`, add Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/tweets/cognition-devin-outposts-2026-07-21.md` — source summary

- [ ] **Create** `wiki/sources/tweets/sundarpichai-gemini-35-transcribe-2026-08-26.md` — source summary

## Page drafts

### wiki/tools/devin.md (updated)

```md
---
as_of: 2026-07-21
sources: [..., cognition-devin-outposts-2026-07-21]
---

## Current status (as of 2026-07-14)

(... existing bullets unchanged ...)

- **Devin Outposts (July 2026):** Devin's planning/inference loop continues running in Cognition's cloud, but command execution, file edits, and repository access can now run on infrastructure the customer controls — a Mac mini, a lab GPU box, a private-network VM, or a Kubernetes cluster. Launch-partner deployment guides ship with Cloudflare (isolated edge sandbox), Daytona (sub-90ms snapshot-started sandboxes), E2B (fast configurable cloud sandboxes reaching into a private cloud), Modal (same GPU infra used for training/serving, so Devin can reproduce failures on production hardware), and Namespace (M5-powered Mac with Xcode/computer use for Apple-platform apps).

## Recent changes

- [2026-07-21] Devin Outposts: command execution/file edits/repo access can run on customer-controlled infrastructure while planning stays in Cognition's cloud; launch-partner guides with Cloudflare, Daytona, E2B, Modal, and Namespace.
- (... existing entries follow ...)
```

### wiki/tools/gemini.md (updated)

```md
---
as_of: 2026-08-26
sources: [..., sundarpichai-gemini-35-transcribe-2026-08-26]
---

## Recent changes

- [2026-08-26] Gemini 3.5 Transcribe launched: multi-speaker intent detection, 85+ languages auto-detected, custom vocabulary adaptation for specialized jargon; available via the Gemini API in Google AI Studio and Gemini Enterprise.
- (... existing entries follow ...)
```

Add to the body under "**Other Gemini surfaces already tracked here:**" (or as a new bullet near the top of Current status):

```md
- **Gemini 3.5 Transcribe (August 2026):** a speech-understanding model with multi-speaker intent detection, automatic 85+ language detection, and custom vocabulary adaptation for specialized jargon; available now via the Gemini API in Google AI Studio and Gemini Enterprise.
```

### wiki/sources/tweets/cognition-devin-outposts-2026-07-21.md (new)

```md
---
title: "Cognition on X: \"Outposts lets you run Devin sessions inside infrastructure you control\""
type: source
source_type: tweet
source_file: raw/tweets/2026-09-07-cognition-2079612229318848582.md
url: https://x.com/cognition/status/2079612229318848582?s=12
published: 2026-07-21
ingested: 2026-09-08
domains: [coding, agents]
---

# Cognition — Introducing Devin Outposts

Launch thread for Devin Outposts: Devin's planning/inference loop stays in Cognition's cloud while execution runs on customer-controlled infrastructure, with launch-partner deployment guides for Cloudflare, Daytona, E2B, Modal, and Namespace.

## Influenced pages

- [Devin](../../tools/devin.md) — Devin Outposts bullet

## Key claims extracted

- Planning/inference stays in Cognition's cloud; execution (commands, file edits, repo access) runs on customer infrastructure
- Launch partners: Cloudflare, Daytona, E2B, Modal, Namespace, NVIDIA Brev
- Each partner gives Devin a different execution environment (edge sandbox, fast snapshot boot, private cloud reach, GPU training infra, Apple-platform Mac)
```

### wiki/sources/tweets/sundarpichai-gemini-35-transcribe-2026-08-26.md (new)

```md
---
title: "Sundar Pichai on X: \"Say hello to Gemini 3.5 Transcribe!\""
type: source
source_type: tweet
source_file: raw/tweets/2026-09-07-sundarpichai-2092659467284517088.md
url: https://x.com/sundarpichai/status/2092659467284517088?s=12
published: 2026-08-26
ingested: 2026-09-08
domains: [voice, models]
---

# Sundar Pichai — Gemini 3.5 Transcribe

Announcement of Gemini 3.5 Transcribe: multi-speaker intent detection, 85+ auto-detected languages, custom vocabulary adaptation; available via the Gemini API in Google AI Studio and Gemini Enterprise.

## Influenced pages

- [Gemini](../../tools/gemini.md) — Gemini 3.5 Transcribe bullet

## Key claims extracted

- Multi-speaker speech/intent understanding
- Auto-detection of 85+ languages out of the box
- Custom vocabulary adaptation for specialized jargon
- Available now via Gemini API, Google AI Studio, and Gemini Enterprise
```
