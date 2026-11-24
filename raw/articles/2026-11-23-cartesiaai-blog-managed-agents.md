---
title: Introducing Managed Agents
type: source
source_type: article
url: https://cartesia.ai/blog/managed-agents
fetched: 2026-11-23
---

# Introducing Managed Agents

Today, we’re launching Cartesia Managed Agents, our end-to-end voice agent platform for enterprise conversations. It pushes the frontier of speech-to-speech naturalness and accuracy, and ranks #1 on independent voice agent benchmarks at launch.

We designed the harness and our voice models together, so listening, turn-taking, reasoning, tool-calling, and speech are tuned as one end-to-end system. Everything enterprise teams need to run agents in production comes on one platform: telephony, knowledge bases, tool integrations, and more. And we’ve tested it at scale — Managed Agents has already powered tens of millions of conversations in finance, retail, hospitality, and healthcare.

## Setting a new Pareto frontier

Cascaded pipelines are the dominant paradigm for enterprise tasks, but without careful co-design they can lose out on naturalness and conversational dynamics like turn-taking and interruptions. Today’s speech-to-speech models sound natural, but they’re hard to control and less reliable for enterprise-grade tasks.

With Managed Agents, we co-designed our voice models and the harness to deliver the best conversational experience without sacrificing the intelligence and controllability that complex enterprise tasks require.

On Artificial Analysis’s [Speech Agent Arena](https://artificialanalysis.ai/speech-to-speech/arena), where blind human raters compare agents on tasks like booking appointments and ordering takeout, Managed Agents ranks #1 of 30 agents with a preference Elo of 1115.

Blind human preference across conversational tasks like booking appointments and ordering takeout. Higher is better.

[Artificial AnalysisOctober 2026](https://artificialanalysis.ai/speech-to-speech/arena)

2

Gemini 3.1 Flash
Live Minimal

Google

6

GPT-Live-1
(Sol, low)

OpenAI

7

GPT-Live-1
(Astra, medium)

OpenAI

8

Eleven Realtime
v1 Max

ElevenLabs

11

ElevenLabs Agents
(Default Cascaded)

ElevenLabs

Benchmarks run with GPT-5.5 as the reasoning model.

On [EVA-Bench](https://servicenow.github.io/eva/#results), ServiceNow’s open benchmark for enterprise voice agents in CSM, ITSM, and HR, Managed Agents posts the highest scores for both accuracy (87%) and experience (91%), setting a new Pareto frontier.

First-attempt scores across 200+ enterprise scenarios. Every system in the shaded box scores lower on both. Higher is better.

Speech-to-speechCascadeHybrid

Experience (EVA-X)

020406080100

ElevenLabs Agents (GPT-5.4)

GPT Realtime 2.1

Gemini 3.8 Live

Grok Voice 3.0

020406080100

Accuracy (EVA-A)

See every system's scores

| EVA-Bench: accuracy vs. experience | Accuracy (EVA-A) | Experience (EVA-X) |
| --- | --- | --- |
| Managed Agents (GPT 5.5)Cartesia | 87.4% | 90.7% |
| Grok Voice 3.0xAI | 73.7% | 71.2% |
| Gemini 3.8 LiveGoogle | 45.9% | 88.6% |
| Gemini 3.8 Live Extended Thinking (Minimal)Google | 50.1% | 79.2% |
| Gemini 3.8 Live Extended Thinking (High)Google | 54.8% | 73.7% |
| ElevenLabs Agents (Claude Haiku 4.5)Scribe v2.2 Realtime + Claude Haiku 4.5 + Eleven Flash v2 | 41.0% | 81.7% |
| GPT Realtime 2.1OpenAI | 59.0% | 61.6% |
| Grok Voice 2.0xAI | 51.7% | 64.1% |
| Grok Voice 1.0xAI | 58.8% | 56.9% |
| GPT Realtime 1.5OpenAI | 46.7% | 56.6% |
| GPT Realtime 2OpenAI | 50.4% | 39.0% |
| Gemini 3.1 Flash LiveGoogle | 29.2% | 58.9% |
| ElevenLabs Agents (GPT-5.4)Scribe v2.2 Realtime + GPT-5.4 + Eleven Flash v2 | 67.2% | 13.0% |
| Universal 3.5 Pro + GPT-5.4 + Sonic 3.5Cascade | 53.1% | 24.8% |
| GPT RealtimeOpenAI | 40.7% | 36.5% |
| Parakeet 1.1B CTC en-US + Gemma-4-26B + KokoroCascade | 33.1% | 39.5% |
| Flux General Multi + GPT-5.4 + Sonic 3.5Cascade | 43.1% | 17.6% |
| GPT Realtime MiniOpenAI | 16.3% | 40.6% |
| Gemini 3.6 Flash + Gemini 3.1 Flash TTS PreviewGoogle | 56.2% | 0.0% |
| ElevenLabs Agents (Gemini 3 Flash)Scribe v2.2 Realtime + Gemini 3 Flash + TTS Conversational v3 | 49.0% | 2.4% |
| GPT Realtime 2.1 MiniOpenAI | 21.7% | 29.2% |
| Nova 3 + GPT-5.4-mini + Aura 2Cascade | 39.5% | 9.6% |
| Ink 2 + Haiku 4.5 + Sonic 3.5Cascade | 34.8% | 6.6% |
| UltravoxHybrid | 27.0% | 2.9% |

Benchmarks run with GPT-5.5 as the reasoning model.

“

> On EVA-Bench, ServiceNow’s open-source benchmark for enterprise voice agents,
> Cartesia Managed Agents posted one of the strongest results we’ve seen to
> date. Across 200+ realistic CSM, ITSM and HR scenarios, it stayed accurate on
> the details while keeping conversations natural, which is the balance
> enterprises look for before putting AI on the phone with their customers. It
> also reflects a broader pattern we’re seeing in enterprise voice: harnesses
> and models designed together.

Nitin AggarwalSenior Director of Product Management, Agentic Evals and RAI

When callers interrupt, pause, or change their minds, the agent handles it naturally: in our internal evaluations, callers reported no turn-taking issues in 85% of conversations with Managed Agents, compared with 67% for other agents.

## Designed for complex calls

Cartesia Managed Agents provides all the tools needed to build frontier voice agents in one end-to-end platform. Claims intake, patient scheduling, retail returns, IT helpdesk: enterprise calls rarely stay simple. One conversation can mean verifying a caller, checking three systems, and quoting policy, all without missing a beat.

Keystone Auto InsuranceBrookline Apparel

* Multilingual: Build agents in 44 languages. Agents can switch between English, Spanish, Hindi, French, and Japanese mid-conversation, with all 44 coming soon.
* Tool calls: Integrate your backend APIs, CRMs, and systems of record, so your agent can look up records and take action mid-call.
* Knowledge bases: Get precise answers from hundreds of documents. The agent’s context is prefilled dynamically, so it responds without pausing to search.
* Outbound campaigns: Schedule thousands of calls with outbound batches, each personalized to the person you’re calling.

## Build your first agent

Artificial AnalysisRanked #1 in Speech Agent Arena
