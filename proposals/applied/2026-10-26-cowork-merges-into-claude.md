---
type: proposal
source: raw/articles/2026-10-26-claudecom-blog-cowork-is-now-claude.md
sources:
  - raw/articles/2026-10-26-claudecom-blog-cowork-is-now-claude.md
  - raw/tweets/2026-10-26-claudeai-2100258490740539730.md
status: pending
created: 2026-10-26
---

# Proposal: Claude Cowork and chat merge into one Claude; Claude Docs and Slides launch

## Summary

### In short

Anthropic has stopped asking users to choose a surface. Cowork's hand-it-off, keep-working-after-you-leave agent is now part of every Claude conversation. Claude Docs and Claude Slides launched with the merge, and Claude Design moved into the chat. The merge reached Pro and Max from 16 September and became generally available for Enterprise on 23 October. The proposal keeps the Cowork page but rewrites it as merged into Claude. It updates Claude Design, Claude Tag, State of Agents and State of Creative, and adds two source pages. Reason to hesitate: keeping the Cowork name is a judgment call against archiving the page.

[[#Open questions|Open questions: 2 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

On 16 September Anthropic announced that Claude Cowork and chat are becoming "one Claude". Cowork launched as a separate place for bigger delegated work, and Claude Design as a separate place for visual work. Anthropic says the frustrating part for users was deciding where a task belonged, and that work started in one place did not carry into the other. Now Claude decides what a task needs, and everything Cowork and Design could do is available in any conversation, with the context, skills and connectors already there.

The worked example is a weekly report due at noon. Before leaving home you ask what moved in the pipeline, ask for it written "the way we always do", and ask for five slides. You check progress from your phone. At your desk the report is waiting as a doc and the slides match it, because both came out of the same conversation. The task can then be scheduled for every Monday. By default Claude asks before it takes an action. Users can switch that off and have it check in only when something needs a closer look.

Two new products shipped with the merge. Claude Docs is a document you and Claude write together, and Claude Slides is a deck Claude drafts. Both can be edited directly, presented from Claude, or downloaded as PowerPoint or PDF, and everything sits at one shareable link. Claude Docs, Slides and Design are in beta on paid plans, Enterprise admins choose when to turn them on, and standalone Claude Design keeps working. Existing Cowork chats, projects, artifacts, connectors and skills carry over. A 23 October update to the post says the unified app is now generally available for Claude Enterprise.

### What changes

The wiki tracks Cowork as Anthropic's separate cross-device agent, last updated in July.

- **Claude Cowork** keeps its address but gets a retitled page, a new lead, and a rewritten Current status covering the merge, the rollout, check-in control, Docs/Slides/Design and the carried-over work. Stale July notes are dropped. It gains two Recent-changes entries, and its page date moves to 23 October.
- **State of Agents** rewrites the Cowork leader line around the merged app and adds a Recent-changes entry. The oldest entry moves to history, and the page date moves to 23 October.
- **Claude Design** and its **State of Creative** line note that Design now also works inside conversations, beside Docs and Slides. The Creative line also drops its outdated "powered by Opus 4.7" wording and spills its oldest entry. Both page dates move to 16 September.
- **Claude Tag** corrects a sentence that calls Cowork a desktop product.
- The index updates four lines, and two new source pages are added.

### What to weigh

The blog post has no date line. The 16 September date comes from Anthropic's same-day thread, and the Enterprise claim carries the post's own 23 October update date. The real choice is structure. This proposal keeps `tools/claude-cowork.md` because Anthropic still says "Cowork" for the capability, the wiki has no Claude app page to hand it to, and a history file already sits at Cowork's archive path. Docs and Slides go on that page, not on pages of their own.

## Intended changes

- [ ] **Update** `wiki/tools/claude-cowork.md` — retitle, new lead paragraph, rewritten `## Current status (as of 2026-10-23)`, one added paragraph in `## Why it matters`; add two Recent-changes entries (2026-10-23, 2026-09-16) at the top; append two source ids and two Sources links; `as_of` 2026-07-08 → 2026-10-23
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — rewrite the Claude Cowork leader line; add one Recent-changes entry dated 2026-10-23 at the top; append two source ids; `as_of` 2026-10-19 → 2026-10-23
    > See draft below

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — the list is at its cap of 10, so the oldest entry (2026-07-08, Cowork web/mobile beta) moves to history
    > See draft below

- [ ] **Update** `wiki/tools/claude-design.md` — add one Current-status bullet and move the status heading to 2026-09-16; add one Recent-changes entry dated 2026-09-16; append two source ids and two Sources links; `as_of` 2026-07-08 → 2026-09-16
    > See draft below

- [ ] **Update** `wiki/state-of/creative.md` — extend the Claude Design leader line; add one Recent-changes entry dated 2026-09-16 at the top; append one source id and one Sources link; `as_of` 2026-09-01 → 2026-09-16
    > See draft below

- [ ] **Spill** `wiki/state-of/creative.md` → `wiki/history/state-of/creative.md` — the list is at its cap of 10, so the oldest entry (2026-05-22, Figma agent and Runway Aleph 2.0) moves to history
    > See draft below

- [ ] **Update** `wiki/tools/claude-tag.md` — correct the Cowork description in `## Positioning`; append one source id and one Sources link; `as_of` unchanged (2026-10-10)
    > See draft below

- [ ] **Update** `wiki/index.md` — update the `tools/claude-cowork`, `tools/claude-design`, `state-of/agents` and `state-of/creative` lines
    > See draft below

- [ ] **Create** `wiki/sources/articles/claude-cowork-is-now-claude-2026-09-16.md` — source summary for the blog post

- [ ] **Create** `wiki/sources/tweets/claudeai-cowork-chat-merge-2026-09-16.md` — source summary for the @claudeai launch thread

## Page drafts

### wiki/tools/claude-cowork.md (updated)

Frontmatter changes:

```
title: Claude Cowork (merged into Claude)
as_of: 2026-10-23
sources: [<existing ids>, claude-cowork-is-now-claude-2026-09-16, claudeai-cowork-chat-merge-2026-09-16]
```

Replace the H1 and lead paragraph with:

```
# Claude Cowork (merged into Claude)

Anthropic's delegated knowledge-work agent. Since 2026-09-16 it is no longer a separate place: Cowork and chat merged into one Claude app, so handing over a long-running task (a report, a deck, a recurring job) works from any conversation. This page keeps the Cowork name because Anthropic still uses it for this capability and existing Cowork work carries over unchanged.
```

Replace `## Current status (as of 2026-07-08)` and its bullets with:

```
## Current status (as of 2026-10-23)

- **One Claude.** Cowork and chat merged on 2026-09-16. Anthropic says users struggled to decide where a task belonged and lost context moving between surfaces; Claude now works out what a task needs and uses the context, skills, and connectors already in the conversation.
- **Rollout.** Pro and Max first, on web, desktop, and mobile, with nothing to turn on; Team and Free to follow. Generally available for Claude Enterprise since 2026-10-23.
- **Background work.** Tasks keep running after the laptop closes, progress can be checked from a phone, and a task can be scheduled to recur ("every Monday"). By default Claude asks before taking an action; users can let it keep working and check in only when something needs a closer look.
- **Docs, Slides, and Design in the conversation.** Claude Docs (co-written documents) and Claude Slides (Claude-drafted decks) launched with the merge, and [Claude Design](claude-design.md) now works inside conversations. Users edit directly, present from Claude, or download PowerPoint/PDF; each output lives at one shareable link. All three are in beta on paid plans, and Enterprise admins choose when to enable them.
- **Carry-over.** Existing Cowork chats, projects, artifacts, connectors, and skills stay where users left them.
- Earlier Cowork capabilities still apply: work across local files and desktop apps, Live Artifacts (connector-wired dashboards and trackers that refresh on open, April 2026), and scheduled tasks that run while the computer is closed (July 2026).
```

In `## Why it matters`, insert as the new first paragraph:

```
The merge turns Cowork from a destination into a capability of the main app: the user no longer picks "chat" or "agent", and outputs (docs, decks, designs) live next to the conversation that made them. It is the same direction as OpenAI's plan to fold ChatGPT Work into regular Chat (see [Codex](codex.md)).
```

In `## Recent changes`, insert at the top:

```
- [2026-10-23] Unified Claude (chat plus Cowork) generally available for Claude Enterprise.
- [2026-09-16] Cowork and chat merged into one Claude app (Pro/Max rollout over several weeks); Claude Docs and Claude Slides launched and Claude Design moved into conversations, all three in beta on paid plans; existing Cowork work carried over.
```

Append to `## Sources`:

```
- [Claude Cowork and chat are now one Claude](../sources/articles/claude-cowork-is-now-claude-2026-09-16.md)
- [Claude (@claudeai) — Claude Cowork and chat are merging into one Claude](../sources/tweets/claudeai-cowork-chat-merge-2026-09-16.md)
```

The `## Vertical workflow bundles (as of 2026-05-14)` and `## AWS Bedrock deployment (as of 2026-04-23)` sections are unchanged.

### wiki/state-of/agents.md (updated)

Frontmatter: `as_of: 2026-10-23`; `sources:` append `claude-cowork-is-now-claude-2026-09-16, claudeai-cowork-chat-merge-2026-09-16`.

Under `### Agent orchestration`, replace the Claude Cowork line:

> **Before:** `- [Claude Cowork](../tools/claude-cowork.md) — Anthropic; cross-device background agent for delegated knowledge work, now available on web/mobile beta with scheduled tasks that can run while the user's computer is closed *(as of 2026-07-08)*`

```
- [Claude Cowork](../tools/claude-cowork.md) — Anthropic; delegated knowledge-work agent, merged with chat into one Claude app (Pro/Max rollout from 2026-09-16, Enterprise GA 2026-10-23): long-running and scheduled work from any conversation, with Claude Docs, Slides, and Design in the same thread *(as of 2026-10-23)*
```

In `## Recent changes`, insert at the top:

```
- [2026-10-23] Claude Cowork merged with chat into one Claude app (Pro/Max from 2026-09-16, Enterprise GA 2026-10-23); its leader line now describes the unified app.
```

Remove from `## Recent changes` (spilled, see next draft):

```
- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

### wiki/history/state-of/agents.md (updated)

Append at the end of the file:

```
## Archived from current page on <apply date>

- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

### wiki/tools/claude-design.md (updated)

Frontmatter: `as_of: 2026-09-16`; `sources:` append `claude-cowork-is-now-claude-2026-09-16, claudeai-cowork-chat-merge-2026-09-16`.

Rename the heading `## Current status (as of 2026-07-08)` to `## Current status (as of 2026-09-16)` and add as its last bullet:

```
- Works inside Claude conversations since 2026-09-16, beside the new Claude Docs and Claude Slides, as part of the chat and [Cowork](claude-cowork.md) merge: draft a one-pager in Docs, turn it into a deck in Slides, and mock up a matching visual in Design from one thread. Users can select an element and move it or tell Claude what to change; outputs live at one shareable link. In beta on paid plans, Enterprise admins choose when to enable it, and standalone Claude Design keeps working as before.
```

In `## Recent changes`, insert at the top:

```
- [2026-09-16] Claude Design now works inside Claude conversations, launched alongside Claude Docs and Claude Slides (beta, paid plans); standalone Design unchanged.
```

Append to `## Sources`:

```
- [Claude Cowork and chat are now one Claude](../sources/articles/claude-cowork-is-now-claude-2026-09-16.md)
- [Claude (@claudeai) — Claude Cowork and chat are merging into one Claude](../sources/tweets/claudeai-cowork-chat-merge-2026-09-16.md)
```

### wiki/state-of/creative.md (updated)

Frontmatter: `as_of: 2026-09-16`; `sources:` append `claude-cowork-is-now-claude-2026-09-16`.

Under `### Visual design & prototyping`, replace the Claude Design line:

> **Before:** `- [Claude Design](../tools/claude-design.md) — Anthropic; collaborative prototype, slide, and marketing-asset tool powered by Opus 4.7, with creative-suite connectors and bidirectional Claude Code sync via `/design-sync` *(as of 2026-07-08)*`

```
- [Claude Design](../tools/claude-design.md) — Anthropic; collaborative prototype, slide, and marketing-asset tool with creative-suite connectors and `/design-sync` to Claude Code; since 2026-09-16 also works inside Claude conversations beside the new Claude Docs and Slides (beta) *(as of 2026-09-16)*
```

In `## Recent changes`, insert at the top:

```
- [2026-09-16] Claude Design moved into Claude conversations as Anthropic merged chat and Cowork, launching Claude Docs and Claude Slides beside it (all beta on paid plans).
```

Remove from `## Recent changes` (spilled, see next draft):

```
- [2026-05-22] Figma released a native in-canvas design agent (Gemini Flash + Claude Sonnet + Figma fine-tuned models; Every hands-on: good for first drafts, weak on detail fidelity) and Runway launched Aleph 2.0/Edit Studio for single-frame-edit propagation across video (AINews recap); both newsletter-sourced, no primary announcement fetched, no dedicated pages yet.
```

Append to `## Sources`:

```
- [Claude Cowork and chat are now one Claude](../sources/articles/claude-cowork-is-now-claude-2026-09-16.md)
```

### wiki/history/state-of/creative.md (updated)

Append at the end of the file:

```
## Archived from current page on <apply date>

- [2026-05-22] Figma released a native in-canvas design agent (Gemini Flash + Claude Sonnet + Figma fine-tuned models; Every hands-on: good for first drafts, weak on detail fidelity) and Runway launched Aleph 2.0/Edit Studio for single-frame-edit propagation across video (AINews recap); both newsletter-sourced, no primary announcement fetched, no dedicated pages yet.
```

### wiki/tools/claude-tag.md (updated)

Frontmatter: `sources:` append `claude-cowork-is-now-claude-2026-09-16`. `as_of` unchanged.

In `## Positioning`, replace the second sentence:

> **Before:** `Cowork is Anthropic's desktop / delegated computer-work product; Claude Tag is the shared Slack-channel agent surface.`

```
Cowork, merged into the main Claude app since 2026-09-16, is Anthropic's single-user delegated-work capability; Claude Tag is the shared Slack-channel agent surface.
```

Append to `## Sources`:

```
- [Claude Cowork and chat are now one Claude](../sources/articles/claude-cowork-is-now-claude-2026-09-16.md)
```

### wiki/index.md (updated)

```
- [state-of/agents](state-of/agents.md) — current state of agentic systems and tool use *(as_of: 2026-10-23)*
- [state-of/creative](state-of/creative.md) — current state of AI creative tools across video, image, avatar, slides, UI generation, open models, AI music, and creative-agent caveats *(as_of: 2026-09-16)*
- [tools/claude-cowork](tools/claude-cowork.md) — Anthropic's delegated knowledge-work agent, merged with chat into one Claude app (2026-09-16; Enterprise GA 2026-10-23); Claude Docs and Slides launched with it *(as_of: 2026-10-23)*
- [tools/claude-design](tools/claude-design.md) — Anthropic's artifact-generation surface for prototypes, slides, and one-pagers; also works inside Claude conversations since 2026-09-16 (beta) *(as_of: 2026-09-16)*
```

### wiki/sources/articles/claude-cowork-is-now-claude-2026-09-16.md (new)

```
---
title: Claude Cowork and chat are now one Claude
type: source
source_type: article
source_file: raw/articles/2026-10-26-claudecom-blog-cowork-is-now-claude.md
url: https://claude.com/blog/cowork-is-now-claude
published: 2026-09-16
ingested: 2026-10-26
domains: [agents, creative]
---

# Claude Cowork and chat are now one Claude

Anthropic's post announcing that Cowork and chat merge into one Claude app, with Claude Docs and Claude Slides launching and Claude Design moving into conversations. The post has no date line; it says "starting today", and the same-day @claudeai thread is dated 2026-09-16. An in-post update dated 2026-10-23 adds Enterprise general availability.

## Influenced pages

- [Claude Cowork](../../tools/claude-cowork.md) — merge, rollout, check-in control, carry-over
- [State of Agents](../../state-of/agents.md) — Cowork leader line
- [Claude Design](../../tools/claude-design.md) — Design inside conversations
- [State of Creative](../../state-of/creative.md) — Claude Design leader line
- [Claude Tag](../../tools/claude-tag.md) — corrected Cowork description

## Key claims extracted

- Cowork and chat merge into one Claude; rolling out on Pro and Max over the following weeks, web/desktop/mobile, nothing to turn on; Team and Free follow; Enterprise admins get at least 30 days' notice
- Rationale: users found it frustrating to decide where a task belonged, and work did not carry between Cowork and Design; Claude now works out what a task needs, with existing context, skills, and connectors
- Claude Docs and Claude Slides are new; Claude Design works inside conversations; edit directly, present from Claude, download as PowerPoint or PDF; one shareable link per output; all three in beta on paid plans, Enterprise admins choose when to enable; standalone Claude Design keeps working
- Worked example: weekly report plus five slides from one conversation, checked from a phone, scheduled for every Monday
- Default: Claude asks before taking an action; users can opt into it working on and checking in only when something needs a closer look
- Existing Cowork chats, projects, artifacts, connectors, and skills carry over
- Update, 2026-10-23: the unified experience is generally available for Claude Enterprise
```

### wiki/sources/tweets/claudeai-cowork-chat-merge-2026-09-16.md (new)

```
---
title: 'Claude (@claudeai) — Claude Cowork and chat are merging into one Claude'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-claudeai-2100258490740539730.md
url: https://x.com/claudeai/status/2100258490740539730
published: 2026-09-16
ingested: 2026-10-26
domains: [agents, creative]
---

# Claude (@claudeai) — Claude Cowork and chat are merging into one Claude

Anthropic's launch thread for the chat and Cowork merge, which dates the blog post. It frames Docs, Slides, and Design as one pipeline inside a conversation.

## Influenced pages

- [Claude Cowork](../../tools/claude-cowork.md) — launch date
- [Claude Design](../../tools/claude-design.md) — Docs to Slides to Design in one place

## Key claims extracted

- Cowork and chat are merging into one Claude; rolling out to Pro and Max over the next few weeks
- Claude keeps working after the laptop closes; if something is unclear Claude asks, and the user keeps the final say
- Decks, docs, and designs can be made in the conversation: draft a one-pager in Claude Docs, turn it into a deck with Claude Slides, mock up a matching visual in Claude Design
- Fix a line yourself, comment for Claude on a slide, or select and move an element; present from Claude, export, or share everything at one link
- Claude Design, Claude Slides, and Claude Docs are in beta on all paid plans; Cowork work carries over
```

## Schema / vocabulary additions

None.

## Open questions

- Structure: this proposal keeps `tools/claude-cowork.md` with a status change. The alternative is principle 12 applied to products: create `tools/claude-app.md` ("Claude app") as the current page for the unified app, Docs, and Slides; fold the Cowork page into `wiki/history/tools/claude-cowork.md`, which already exists as its Recent-changes archive; and re-point about a dozen inbound links (index, State of Agents, Claude Tag, the subcategory example, eight source pages). Keep the status-change approach (assumed), or switch?
	- Yeah, but this is not an archive, all those features about cowork still exist in Claude, and we need to keep that knowledge, its alive, not archived. The name is whats being archived.
- Claude Docs and Claude Slides get bullets on the Cowork and Design pages but no pages of their own. Should Claude Slides also get a line under State of Creative's slides coverage, next to Genspark Slides (assumed: not until a source evaluates it)?
	- They can be bullets, but if Cowork is getting deprecated, probably not there...
