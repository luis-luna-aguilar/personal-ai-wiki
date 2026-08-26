---
title: GPT-Live
type: tool
domains: [voice, agents]
subcategory: voice-models
tags: [openai, closed-source, agentic]
as_of: 2026-07-07
sources: [gpt-live-launch-2026-07]
---

# GPT-Live

GPT-Live is OpenAI's full-duplex voice model family for natural human-AI interaction. It powers the new ChatGPT Voice experience and is designed to listen and speak at the same time instead of forcing rigid turn-taking.

## Current status (as of 2026-07-07)

- Rolling out globally to ChatGPT on iOS, Android, and ChatGPT.com.
- **GPT-Live-1** becomes the default ChatGPT Voice model for Go, Plus, and Pro users.
- **GPT-Live-1 mini** becomes the default ChatGPT Voice model for Free users.
- API access is planned but not yet generally available; developers and enterprises can sign up for notification.
- Full-duplex interaction lets the model keep listening while speaking, pause, interrupt, acknowledge with short backchannels, or stay quiet while the user thinks.
- Deeper work is delegated to a frontier model in the background; at launch, GPT-Live uses GPT-5.5 behind the scenes.
- ChatGPT Voice adds reasoning-level choices: Instant for fast responses, Medium and High for more thinking.
- Voice now supports visual response cards for topics such as weather, stocks, and sports, while continuing to support search, memory, images, and file uploads.

## Strengths

- More natural interruption, pause, and backchannel behavior than turn-based voice systems.
- Keeps conversational flow while search, reasoning, or more agentic background work runs separately.
- Human evaluations in the launch source report strong preference over Advanced Voice Mode for 5-10 minute conversations.
- Reported gains over Advanced Voice Mode on GPQA, BrowseComp, and an internal τ³-Voice Telecom variant.

## Weaknesses / caveats

- Launch source is OpenAI's own announcement; independent evals are not yet available.
- API support is planned but not yet live at launch.
- No voice with video or screen sharing in ChatGPT at launch, though OpenAI says those capabilities are planned.
- Some languages may have non-native accent or fluency gaps.

## Safety

OpenAI says GPT-Live adds audio-native safety tests, generated-audio synthetic evals, and voice-specific safeguards for self-harm, psychosis/mania, emotional reliance, violence, sexual content, and teen use. The system can steer output while speaking, surface safety resources, or end a conversation in higher-risk cases.

## Recent changes

- [2026-07-07] GPT-Live-1 and GPT-Live-1 mini launched in ChatGPT Voice globally; API access planned.

## Sources

- [Introducing GPT-Live](../sources/articles/gpt-live-launch-2026-07.md)
