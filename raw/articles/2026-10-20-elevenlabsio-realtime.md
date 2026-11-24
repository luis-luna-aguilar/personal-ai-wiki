---
title: Eleven Realtime | Speech to Speech Voice Agents | ElevenLabs
type: source
source_type: article
url: https://elevenlabs.io/realtime
fetched: 2026-10-20
---

# Eleven Realtime | Speech to Speech Voice Agents | ElevenLabs

Meet Eleven v4, our most emotive model yet.

Discover
Skip to content
Products
Solutions
Customers
Resources
Enterprise
Pricing
Log in
Sign up
Max
Mini
Instant conversation
with Eleven Realtime
Build in ElevenAgents
Explore docs

A new class of Speech to Speech models for building voice agents that sound natural. Pick v1 Mini for natural conversations or v1 Max for complex tasks.

Optimized as one system

Speech recognition, turn-taking, LLM, and voice are all tuned end-to-end. Available in ElevenAgents and the Realtime API.

Eleven Realtime v1 Mini
Optimized for natural conversations
Try in ElevenAgents

Best for use cases built around natural, expressive conversation, like AI assistants, educational tutors, and interactive characters.

Built for conversations that flow

Timing and tone stay natural through interruptions and quick back-and-forth.

Assistants
Tutors
Characters
View docs
Benchmark results

The performance figures behind conversations that don’t miss a beat.

Time to first audio
620ms
Full-Duplex-Bench
95.8%
Speech Agent Arena Elo
988
Eleven Realtime v1 Max
Optimized for complex tasks
Try in ElevenAgents

Best for use cases that require precise, thoughtful responses, like customer support and lead qualification.

Benchmark results

The performance figures behind conversations built to reason.

Time to first audio
570ms
Big Bench Audio
98.8%
Task success rate
87.1%
Built for complex business interactions

Reasons through complex questions and calls tools to get things done without slowing the conversation down.

Lead Qualification
Customer Support
Assisted Scheduling
View docs
Build with Eleven Realtime
in ElevenAgents

Select a Realtime model when you create an agent, and start talking to it right away.

Try in ElevenAgents
One dropdown

Set your agent’s model to v1 Mini or v1 Max. Transcription, turn-taking, and voice are already configured.

Deploy to any channel
Built for production
An OpenAI-compatible Realtime API

Eleven Realtime is also available through the Realtime API. It’s compatible with OpenAI’s Realtime API, so you change the endpoint and model name and keep the rest of your code.

npx skills add elevenlabs/skills \
  --skill realtime

Install with one command using our skill

Run the skill and watch as setup is handled for you. Realtime voice lands in your product in minutes.

Same events, same handlers

Every client and server event arrives as it does from OpenAI, so the handlers, logging, and tooling you built keep working.

Auditable conversations

View and audit conversations in a dedicated UI/dashboard. Every conversation is logged and searchable, fully ready for when compliance needs it.

Connect with OpenAI's SDK

Use the Realtime SDK you already have. Point its WebSocket transport at ElevenLabs, choose a Realtime model and a voice, and connect with your client secret.

View docs
import { OpenAIRealtimeWebSocket, RealtimeAgent, RealtimeSession } from "@openai/agents-realtime";

const { value: clientSecret } = await fetch("/api/token").then((res) => res.json());

const agent = new RealtimeAgent({
  name: "ElevenLabs agent",
  instructions: "You are a helpful, friendly voice assistant. Keep replies concise.",
});

const transport = new OpenAIRealtimeWebSocket({
  url: "wss://api.elevenlabs.io/v1/convai/realtime",
});

const session = new RealtimeSession(agent, {
  transport,
  model: "eleven_realtime_v1_mini",
  config: {
    outputModalities: ["audio"],
    audio: { output: { voice: "brian" } },
  },
});

await session.connect({ apiKey: clientSecret });


Cast from 17,500+ voices

Narration
Conversational
Social media
Character
Educational
Advertisement
Entertainment
Multilingual

Narration voices A place for the storytellers. Warm, authoritative, and consistent across every project.

Use voices
View more

Conversational voices For everyday conversations, you need a natural, easygoing voice. Our conversational voices are built for dialogue and podcasts that are made to feel unscripted.

Use voices
View more

Social media voices Voices that come alive in short-form content. Capture the energy and personality needed to make a user stay on your TikTok or Reel from end to end.

Use voices
View more

Character voices A pool of voices for your fictional world. Select from a dynamic cast that brings your game, audiobook, or animation to life.

Use voices
View more

Educational voices Trustworthy, patient voices that guide students through complex topics. These voices excel for courses, tutorials, training simulations, and guides at every level.

Use voices
View more

Advertisement voices Polished voices brimming with confidence to land your next product sale. Perfect for digital ads or TV and radio reads.

Use voices
View more

Entertainment voices From booming movie trailers to comic voices made for performance, these voices scream personality. Built for content where delivery matters as much as material.

Use voices
View more

Multilingual voices Voices built for global content. Natural pacing, idiomatic expressions, and accents that connect with audiences in every market.

Use voices
View more
90+ languages and a wide range of accents

Realtime conversation in over 90 languages. Adapt your product to serve customers across the globe.

Languages

English
Spanish
German
Japanese
Korean
Chinese
Polish
French
+94 languages and accents

Accents

American
Australian
Canadian
Cockney
German
German Bavarian
Texas
English
Enterprise-grade security and infrastructure at scale

Data is encrypted in transit and at rest, with support for SOC 2, HIPAA, and GDPR compliance. EU Data Residency and Zero Retention modes are available for stricter data control.

Agents for Enterprise
SOC 2 Type II
ISO 27001
Regional Data Residency
Zero Retention Mode
On-prem options
ISO 42001
AIUC-1
HIPAA compliant
PCI DSS Level 1
See all certifications
Frequently asked questions
What is Eleven Realtime?
What’s the difference between v1 Mini and v1 Max?
How do I use a Realtime model in ElevenAgents?
How do I use the Realtime API?
Does the Realtime API support WebRTC?
Can I use ElevenAgents features with the Realtime API?
How is Eleven Realtime priced?
How were the benchmark results measured?

AI Communication Platform

Talk to sales
Create an AI agent
English
English
Svenska
Polski
Português
日本語
한국어
हिन्दी
Español
Français
Deutsch
Italiano
简体中文
Nederlands

ElevenCreative

Text to Speech
Speech to Text
Voice Changer
Text to Sound Effects
Voice Cloning
Voice Isolator
AI Music Generator
Studio
Voice Design
AI Voice Generator
AI Image Generator
AI Video Generator
Ads Engine

ElevenAgents

Voice Agents
Conversational AI
Integrations
Telecommunications
Financial Services
Healthcare
Government
Technology
Retail & E-commerce
Travel & Hospitality
Customer Support
Chatbots

ElevenAPI

API Reference
Agents API
Speech Engine
Dubbing API
Text to Speech API
Speech to Text API
Sound Effects API
Music API
API Key

Resources

Blog
Iconic Marketplace
Impact Program
Startup Grants
Help Center
Webinars
Docs
Enterprise
Trust Center
India

Socials

X
LinkedIn
GitHub
YouTube
Discord
TikTok
Instagram
Facebook
Reddit

Company

About
Careers
Safety
Brand & Press Kit
ElevenLabs Summit
Policies
Cookie Settings
Voice chat

## FAQ (expanded in the aside browser, fetched 2026-10-20)

What is Eleven Realtime?

Eleven Realtime is a new class of Speech to Speech models for building natural voice agents. Each model combines speech recognition, turn-taking, LLM, and text to speech tuned together as one system, so you get a well-performing agent from a single model choice. It’s available in ElevenAgents and the Realtime API.

What’s the difference between v1 Mini and v1 Max?

V1 Mini is the lower cost choice for simpler use cases like AI assistants, tutors, and interactive characters. V1 Max adds reasoning capability for more complex tasks like customer support, lead qualification, and multi-step workflows with tool calls. 


How do I use a Realtime model in ElevenAgents?

Create an agent, or open an existing one, and choose v1 Mini or v1 Max from the model dropdown. Your prompt, tools, knowledge base, channels, and settings work as before. Nothing changes for existing agents unless you update them.

How do I use the Realtime API?

It’s OpenAI-compatible. If you’re already on OpenAI’s Realtime API, change the endpoint and model name in the code you have, or run npx skills add elevenlabs/skills --skill openai-realtime-migration and the skill handles setup. OpenAI’s SDK works as is. The migration guide covers the differences. If you’re starting from scratch, we recommend ElevenAgents.


Does the Realtime API support WebRTC?

Not at launch. It connects over WebSocket, so a WebRTC integration needs to move to WebSocket first.

Can I use ElevenAgents features with the Realtime API?

No. The Realtime API and ElevenAgents run separately and use different connection protocols. If you need phone, WhatsApp, or contact center channels, a knowledge base, guardrails, testing, or monitoring, build on ElevenAgents.

How is Eleven Realtime priced?

In ElevenAgents, Realtime models use standard ElevenAgents per-minute pricing plus the LLM cost per token. The model selector in the app shows an estimated cost per minute. Through the Realtime API, you pay per minute of connected audio plus tokens, with the same token prices on every plan. See the pricing page for current rates.

How were the benchmark results measured?

Artificial Analysis evaluated both models independently on Big Bench Audio for speech reasoning, Full-Duplex-Bench for conversational dynamics, and the Speech Agent Arena for human preference and task success. Time to first audio is the average measured on Big Bench Audio.

