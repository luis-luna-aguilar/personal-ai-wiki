---
type: proposal
source: raw/articles/2026-10-26-elevenlabsio-blog-reception.md
sources:
  - raw/articles/2026-10-26-elevenlabsio-blog-reception.md
  - raw/tweets/2026-10-26-elevenlabs-2100262886916358361.md
status: pending
created: 2026-10-26
---

# Proposal: ElevenLabs Reception, an AI receptionist for small businesses

## Summary

### In short

The AI receptionist has become a packaged product that a small business can switch on in minutes, not a custom voice-agent build. ElevenLabs' Reception, built on its ElevenAgents platform, answers every call, handles routine questions in the caller's language, books the appointment into the calendar and texts a confirmation. It sets up from the business's website. The proposal creates a use-case page for AI receptionists and adds a Reception bullet to the Voice becomes an agent interface trend. Reason to hesitate: filing Reception under use cases instead of giving it a tool page is a scope call.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

On 16 September ElevenLabs introduced Reception, an AI receptionist for small businesses that runs on ElevenAgents, its voice-agent platform. The pitch is the plumber on a job or the salon owner with a client, who has to choose between the work in front of them and a ringing phone. Reception answers around the clock. Callers can ask about services, hours and location in their own words and their own language, in ElevenLabs voices. The owner chooses when it answers: as overflow when nobody on the team picks up, or after closing. It works on a forwarded existing line or a new dedicated number. On the call it works out what the caller needs, checks staff availability and books the appointment. Built-in calendar integrations and a public booking page keep bookings in one place. After each call the team gets a summary, a transcript and a recording. The target trades are home services, professional services, real estate and property management, and salons and studios.

ElevenLabs' launch thread adds two details: Reception texts a confirmation after booking, and setup "just by adding your website". In early replies, an e-commerce marketing operator said the call logs, showing what callers actually ask, were the most useful part. Another tester said he tried three times to bait it into making something up, and it kept saying someone would follow up.

### What changes

The wiki tracks voice as an emerging agent interface, mostly through general assistants such as GPT-Live, and has no page for single-job business voice agents. Its only receptionist evidence is a pilot caveat on AI adoption evidence.

- New page `use-cases/ai-receptionist.md` covers the pattern: coverage choices, grounding and booking setup, where it fits, and failure modes. It links the existing receptionist-pilot finding that customers churned more under AI even at equal error rates.
- **Voice becomes an agent interface** gains a Current-status bullet on Reception and one Recent-changes entry. Its page date moves to 16 September.
- The **index** gains the use-case line, and the trend's date moves. Two new source pages are added.

### What to weigh

The blog post has no date line, so 16 September comes from ElevenLabs' same-day launch thread. Reception is filed as a use case, not a tool. A `tools/` page would need a subcategory, and `voice-models` is defined around the voice model layer rather than finished applications. The tester replies are single users' anecdotes and appear on the use-case page only as illustrations.

## Intended changes

- [ ] **Create** `wiki/use-cases/ai-receptionist.md` — no existing page for the AI-receptionist pattern
    > See draft below

- [ ] **Update** `wiki/trends/voice-becomes-agent-interface.md` — add one Current-status bullet; add one Recent-changes entry dated 2026-09-16 at the top; append two source ids and two Sources links; `as_of` 2026-08-05 → 2026-09-16
    > See draft below

- [ ] **Update** `wiki/index.md` — add the `use-cases/ai-receptionist` line; update the `trends/voice-becomes-agent-interface` date; use-cases count +1, total +1
    > See draft below

- [ ] **Create** `wiki/sources/articles/elevenlabs-reception-2026-09-16.md` — source summary for the blog post

- [ ] **Create** `wiki/sources/tweets/elevenlabs-reception-launch-2026-09-16.md` — source summary for the launch thread

## Page drafts

### wiki/use-cases/ai-receptionist.md (new)

```
---
title: AI receptionist for small businesses
type: use-case
domains: [voice, agents]
tags: [voice, agentic, elevenlabs]
as_of: 2026-09-16
sources: [elevenlabs-reception-2026-09-16, elevenlabs-reception-launch-2026-09-16]
---

# AI receptionist for small businesses

A voice agent that answers a small business's phone when nobody can (during a job, with a client, or after hours), handles routine questions, and books the appointment while the caller is still on the line. The pattern now ships as a packaged product rather than a custom build: ElevenLabs' Reception (2026-09-16), built on its ElevenAgents platform, is set up from the business's website in minutes.

## Current guidance

- **Choose the coverage.** Overflow (staff pick up first and the agent takes the calls nobody reaches) or after-hours only; forward the existing business line or start with a dedicated number.
- **Ground it in the business's own facts.** Services, hours, and location; Reception builds this from the website, and callers can ask in their own words and their own language.
- **Make the call end in a booking.** Connect the calendar and staff availability so the agent books, then texts a confirmation; a public booking page covers callers who prefer to book online.
- **Read the logs.** Summaries, transcripts, and recordings after each call prepare the team for the visit, and one early user found the record of what callers actually ask as valuable as the answering itself.
- **Prefer "someone will follow up" over a guess.** One early tester reports Reception declined three attempts to bait it into inventing an answer; test this before going live.

## Where it fits

- Home services (plumbing, electrical, HVAC): book visits while the team is in the field
- Professional services: capture inquiries and schedule consultations while staff are with clients
- Real estate and property management: answer listing questions and arrange viewings
- Salons and studios: book and reschedule without interrupting a service

## Failure modes

- **Trust, not accuracy, decides adoption.** In Boulton and Watt's receptionist pilot, customers churned more under AI even when error rates matched humans (see [AI adoption: evidence from practice](../training/ai-adoption-evidence.md)).
- **No calendar access, no booking.** Without availability data the agent becomes a message-taker and loses the booking the pattern exists for.
- **Unmeasured baseline.** Few businesses count callers who hang up, so the value of answering every call is hard to see before deployment.

## Related

- [Voice becomes an agent interface](../trends/voice-becomes-agent-interface.md) — the broader shift this use case belongs to
- [AI adoption: evidence from practice](../training/ai-adoption-evidence.md) — the receptionist-pilot trust finding

## Sources

- [Introducing Reception, an AI Receptionist by ElevenAgents](../sources/articles/elevenlabs-reception-2026-09-16.md)
- [ElevenLabs (@ElevenLabs) — Introducing Reception, an AI receptionist](../sources/tweets/elevenlabs-reception-launch-2026-09-16.md)
```

### wiki/trends/voice-becomes-agent-interface.md (updated)

Frontmatter: `as_of: 2026-09-16`; `sources:` append `elevenlabs-reception-2026-09-16, elevenlabs-reception-launch-2026-09-16`.

In `## Current status`, add as the last bullet:

```
- Voice agents are also being packaged for one narrow business job. ElevenLabs' Reception (2026-09-16), built on ElevenAgents, answers a small business's calls around the clock, answers questions in the caller's language, books appointments into the calendar, and texts a confirmation, set up from the business's website in minutes (see [AI receptionist for small businesses](../use-cases/ai-receptionist.md)).
```

In `## Recent changes`, insert at the top:

```
- [2026-09-16] ElevenLabs launched Reception, a packaged AI receptionist for small businesses on ElevenAgents (answer, book, confirm by text).
```

Append to `## Sources`:

```
- [Introducing Reception, an AI Receptionist by ElevenAgents](../sources/articles/elevenlabs-reception-2026-09-16.md)
- [ElevenLabs (@ElevenLabs) — Introducing Reception, an AI receptionist](../sources/tweets/elevenlabs-reception-launch-2026-09-16.md)
```

### wiki/index.md (updated)

Under `## Trends`, update the date on the `trends/voice-becomes-agent-interface` line:

```
- [trends/voice-becomes-agent-interface](trends/voice-becomes-agent-interface.md) — voice, texting, and real-time audio are becoming agent surfaces rather than side features *(as_of: 2026-09-16)*
```

Under `## Use Cases`, add:

```
- [use-cases/ai-receptionist](use-cases/ai-receptionist.md) — voice agent that answers a small business's calls, handles routine questions, and books appointments; ElevenLabs Reception as the packaged example *(as_of: 2026-09-16)*
```

Under `## Page count`: `use-cases` +1 and `Total content pages` +1 (from the live values at apply time).

### wiki/sources/articles/elevenlabs-reception-2026-09-16.md (new)

```
---
title: Introducing Reception, an AI Receptionist by ElevenAgents
type: source
source_type: article
source_file: raw/articles/2026-10-26-elevenlabsio-blog-reception.md
url: https://elevenlabs.io/blog/reception
published: 2026-09-16
ingested: 2026-10-26
domains: [voice, agents]
---

# Introducing Reception, an AI Receptionist by ElevenAgents

ElevenLabs' launch post for Reception, an AI receptionist for small businesses built on ElevenAgents. The post has no date line; it says "today", and ElevenLabs' same-day launch thread is dated 2026-09-16.

## Influenced pages

- [AI receptionist for small businesses](../../use-cases/ai-receptionist.md) — new page
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — Reception bullet

## Key claims extracted

- Reception answers calls around the clock, responds to questions about the business, and books appointments in the calendar
- ElevenAgents voices and orchestration are built in; setup takes minutes and requires no technical experience
- Callers ask about services, hours, and location in their own words and their own language
- Owner chooses coverage: team picks up first with Reception covering missed calls, or Reception takes over after closing; forward the existing line or use a dedicated number
- Works out what the caller needs, answers follow-ups, checks staff availability, books the appointment; built-in calendar integrations and a public booking page
- Summaries, transcripts, and recordings after each call
- Target segments: home services, professional services, real estate and property management, salons and studios
- Available at reception.ai with published plans and pricing
```

### wiki/sources/tweets/elevenlabs-reception-launch-2026-09-16.md (new)

```
---
title: 'ElevenLabs (@ElevenLabs) — Introducing Reception, an AI receptionist'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-elevenlabs-2100262886916358361.md
url: https://x.com/ElevenLabs/status/2100262886916358361
published: 2026-09-16
ingested: 2026-10-26
domains: [voice, agents]
---

# ElevenLabs (@ElevenLabs) — Introducing Reception, an AI receptionist

ElevenLabs' launch thread for Reception, which dates the blog post and adds text confirmations and website-based setup. A few early-user replies are recorded as anecdotes.

## Influenced pages

- [AI receptionist for small businesses](../../use-cases/ai-receptionist.md) — setup, confirmation texts, early-user anecdotes
- [Voice becomes an agent interface](../../trends/voice-becomes-agent-interface.md) — launch date

## Key claims extracted

- Reception is "an AI receptionist platform for small businesses, built on ElevenAgents"
- It answers every call, answers questions, books the job, and texts confirmation
- Setup "in minutes just by adding your website"
- Early replies: Chase Dimond's team found the logs of what callers ask "super helpful"; Eli Weiss tried three ways to bait it into making something up and it kept saying someone would follow up; Nick Shackelford notes brands rarely measure how many callers hang up
```

## Schema / vocabulary additions

None.

## Open questions

- Reception is filed under `use-cases/` with no product page. The alternative is `tools/reception.md` under the existing `voice-models` subcategory, or a new `voice-agent-platform` subcategory that could also hold ElevenAgents. Keep the use-case filing (assumed), or add a tool page?
	- Use case please
