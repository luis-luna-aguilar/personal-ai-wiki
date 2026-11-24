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
