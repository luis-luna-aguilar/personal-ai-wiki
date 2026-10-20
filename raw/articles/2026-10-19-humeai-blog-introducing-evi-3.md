---
title: Introducing EVI 3: the world’s most realistic and instructible speech-to-speech foundation model
type: source
source_type: article
url: https://www.hume.ai/blog/introducing-evi-3
fetched: 2026-10-19
---

# Introducing EVI 3: the world’s most realistic and instructible speech-to-speech foundation model

At Hume, we promised ourselves that before the end of 2025, we’d achieve a voice AI experience that can be fully personalized. We believe this is an essential step toward voice being the primary way people want to interact with AI.

Today, we’re excited to introduce Hume’s third-generation speech-language model, EVI 3. As a speech-language model, where the same intelligence handles transcription, language, and speech, EVI 3 brings more expressiveness, realism, and emotional understanding to voice AI. And instead of being limited to a handful of speakers, EVI 3 can speak with any voice and personality you create with a prompt.

EVI 3 streams in user speech and forms natural, expressive speech and language responses. At conversational latency, it produces the same quality of speech as our text-to-speech model, Octave. Simultaneously, it responds with the same intelligence as the most advanced LLMs of similar latency. It also communicates with reasoning models and web search systems as it speaks, “thinking fast and slow” to match the intelligence of any frontier AI system.

In a blind comparison with OpenAI’s GPT-4o, EVI 3 was rated higher, on average, on empathy, expressiveness, naturalness, interruption quality, response speed, and audio quality.

## Research insights

EVI 3 can instantly generate new voices and personalities instead of being limited to a handful of speakers. For instance, users can speak to any of the more than 100,000 custom voices already created on our text-to-speech platform, each with an inferred personality. No matter the voice, it responds with a wide range of emotions or styles, implicitly or on command.

This novel capability is made possible by Hume’s latest research on speech-language models. Rather than relying on fine-tuning for individual speakers' voices and personalities with small, curated datasets, we developed methods to capture the full range of human voices and speaking styles in one model. Then, with a reinforcement learning approach, we trained EVI 3 to identify and hone the preferred qualities of any human voice. Finally, we developed a streaming approach that enables EVI 3 to respond at conversational latency.

![Evi 3 Voice to Voice Tokens](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fxqnc2for%2Fproduction%2F7b537737702bef25e4589283bd3525592f1c02c2-1920x1080.png%3Fw%3D1200&w=3840&q=75)

EVI 3 voice-to-voice token generation mechanics. A single autoregressive model processes both text (T) and voice (V) tokens. The system prompt, comprised of both T and V tokens, not only provides language instructions similar to an LLM prompt but also shapes the assistant's speaking style. Additional context tokens can be injected while the assistant is speaking and seamlessly incorporated into the response, enabling EVI 3 to perform advanced search, reasoning, and tool use via systems that run in parallel.

## Evaluating EVI 3

We performed a suite of evaluations comparing the capabilities of EVI 3 to those of other leading voice-to-voice AI models. Our evaluations addressed key aspects of conversational AI that will shape the future of human-AI interaction: the nuanced modulation of emotion and style, implicit emotion understanding, and overall conversational quality in unstructured, dynamic interactions.

### Overall preference

We first compared the overall conversational experience delivered by EVI 3 and GPT-4o. In a blind comparison on our survey platform, participants engaged each model in unstructured, multi-turn dialogues lasting between one and three minutes. Conversations revolved around a simple directive: “Get the AI to say something interesting.”

Participants provided feedback across seven conversational dimensions: amusement, audio quality, empathy, expressiveness, interruption handling, naturalness, and response speed.

![Group 6](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fxqnc2for%2Fproduction%2F2eac323437395b83c6669194c7f91878748f94c7-4096x2310.png%3Fw%3D1200&w=3840&q=75)

Results favored EVI 3 across all seven dimensions evaluated.

### Emotion/style modulation

Next, we assessed how effectively EVI 3 modulates its emotional tone and speaking style during real-time conversations. Participants interacted with EVI 3, GPT-4o, Gemini, or Sesame, tasked with getting each AI to express 30 distinct emotions and speaking styles. These styles ranged broadly from emotions like "exhilarated" and "sad" to unique vocal tones such as "act like a pirate," “act like you’re admiring a beautiful painting,” "sultry," and "whisper."

Each participant was asked to get each model to speak with a specific emotion or style from the following list: afraid, angry, anxious, bored, cartoony, coy, despondent, determined, embarrassed, exhilarated, fatigued, high-pitch, horrified, in pain, like you see an adorable puppy, like you're a know-it-all, like you're admiring a painting, like you're running a marathon, low-pitch, monotone, out-of-breath, pedantic, pirate, proud, sad, sarcastic, sultry, whisper, yelling

Participants engaged with EVI 3 and GPT-4o directly on our survey platform via each API in a blind comparison. For Gemini and Sesame, participants were directed to their respective apps.

After each interaction, participants rated each models’ performance in expressing the requested emotion or style on a scale from 1 to 5.

![Group 5](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fxqnc2for%2Fproduction%2Fbd67e9f7bac4371bf05638485e620a55784b8d5d-3572x3294.png%3Fw%3D1200&w=3840&q=75)

Our model outperformed GPT-4o, Gemini, and Sesame in ratings of how well it acted out a wide range of target emotions and styles as instructed by participants.

### Emotion understanding

To examine EVI 3's proficiency in understanding the user’s tone of voice, we designed an evaluation that controlled for language and assessed the model’s understanding of the tune, rhythm, and timbre of speech. Participants were asked to express nine distinct emotions while delivering the same query (e.g., “Can you tell what emotion is in my voice?”). EVI 3’s performance was compared to GPT-4o in a blind evaluation on our survey platform.

Participants were each asked to act out one of 9 specific emotions: Afraid, Amused, Angry, Disgusted, Distressed, Excited, Joyful, Sad, or Surprised. After each conversation, participants rated each model's accuracy in recognizing their expressed emotion, as well as the naturalness of its responses, using a 1-5 rating scale.

![Frame 1](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fxqnc2for%2Fproduction%2Fc8954559d29516b20c46b923929d2fc08d9bf159-3834x2111.png%3Fw%3D1200&w=3840&q=75)

EVI 3 outperformed GPT-4o in identifying eight of the nine tested emotions and in the naturalness of its response.

### Latency

EVI 3 is capable of delivering voice responses in under 300ms on state-of-the-art hardware. In practice, however, the latency experienced by an end user depends on a variety of additional factors, including network latency, traffic, and implementation details. While we are still improving our deployment of EVI 3, it is faster than other voice-to-voice models in our initial testing.

From our New York office, we compared the practical latency of EVI 3 to that of Gemini, GPT-4o, and Sesame. (EVI 3 is currently deployed on the U.S. West Coast.)

| Model | Practical latency (interval between end of user speech and beginning of assistant speech) |
| --- | --- |
| Gemini Live API | 1.2s-3.6s, averaging around 1.5s |
| GPT-4o via OpenAI Realtime API | 2.5-3.1s, averaging around 2.6s |
| Sesame via web app | 0.8-1.2s, averaging around 1s |
| EVI 3 via web app | 0.9-1.4s, averaging around 1.2s |

### General access information

You can interact with EVI 3 today through our live demo and our iOS app. We plan to release API access in the coming weeks.

The model is still being trained. When it is released, it will be more proficient in other languages, particularly French, German, Italian, and Spanish. In the meantime, we’re excited to work with developers through our early access program.
