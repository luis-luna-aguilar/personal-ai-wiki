---
title: Voxtral 3: Speech-to-Text, TTS & Voice Agents
type: source
source_type: article
url: https://mistral.ai/news/voxtral-3
fetched: 2026-11-24
---

# Voxtral 3: Speech-to-Text, TTS & Voice Agents

Speech transcription and voice generation have come a long way, but building end-to-end voice agents that can listen, reason, interact, and handle complex workflows remains difficult.

A reliable voice agent needs to do four things very well (and simultaneously):

1. **Listen accurately** across languages, accents, speakers, and interruptions,
2. **Reason** **deeply** about what users mean in specific contexts,
3. **Speak naturally** with emotion and expression, and
4. **Take action** over multiple steps through connected systems.

Getting all four to work together reliably in real time remains a challenge.

To address this, we introduce Voxtral 3: a new family of state-of-the-art [speech-to-text](https://docs.mistral.ai/studio/audio/speech-to-text/overview) and [text-to-speech](https://docs.mistral.ai/studio/audio/text-to-speech/overview) models, alongside a voice agent SDK that brings listening, thinking, tool calling, and speaking into a single real-time streaming pipeline.

Voxtral 3 is built to create natural conversational experiences, from contact-center agents and service desks to virtual assistants and hands-free copilots. With support for dozens of languages, expressive speech, complex reasoning, and deep integration with your own tools and data, agents built with Voxtral can interpret nuanced intent, reason through sophisticated requests, and execute multi-step actions across connected systems.

As with other Mistral models, the Voxtral 3 family is designed for sovereign deployment. Available today through Mistral's EU-hosted API or for self-deployment on your own infrastructure, it gives organizations control over where audio is processed, how data is handled, and whether conversations are retained.

## Highlights

1. **Accurate transcription across 50+ languages**. The speech-to-text model, *Voxtral Small Transcribe 3*, is state-of-the-art in multilingual transcription, identifying who said what (diarization), using keyphrases to improve its accuracy (context-biasing). It detects when someone has finished speaking so agents can respond without delay (end-of-turn detection).
2. **Natural speech that adapts to the conversation**. The text-to-speech model, *Voxtral Mini TTS 3*, introduces new voices that adjust their emotion, pace, and emphasis based on conversational context, with support for 35+ languages and 50+ dialects.
3. **Human-like intelligence at your (spoken) command**. The new voice agent SDK combines listening, reasoning, tool calling, and speaking into a real-time experience. Agents can retrieve information, interact with business systems, and complete tasks during live conversations over phone or web.
4. **Pro Voice for distinctly accurate voice adaptation**. For professional use cases where basic voice cloning does not suffice, Voxtral’s *Pro Voice* adaptation is able to reproduce a speaker’s distinctive character, emotional range, and speaking style across languages, using just 30 minutes of audio.
5. **Your voice AI, on your infrastructure**. Use Mistral's EU-hosted API or deploy Voxtral 3 on your own infrastructure. Keep sensitive conversations within your environment and control whether any audio is retained.

[Try Voxtral now](https://console.mistral.ai/api-keys)  | [Learn more](https://docs.mistral.ai/studio/audio/overview)

## It hears 50+ languages, with state-of-the-art accuracy.

[Voxtral Transcribe 3](http://docs.mistral.ai/models/voxtral-small-transcribe-3-0) represents a significant milestone across transcription, diarization (who spoke when) and context biasing capabilities. The supported list of languages is expanded to 50, including 24 official EU languages and many low-resource Asian and Indic languages.

The Small version achieves state-of-the-art results across diarization and multilingual transcription, including in English, French and Spanish. It outperforms Whisper, Scribe v2 and Gemini 3.5 Transcribe. The [Mini variant](https://docs.mistral.ai/models/voxtral-mini-transcribe-3-0) is 4B parameters, enabling fast and accurate transcriptions at a price of $0.0035/min.

Both models support context biasing, where key terms and free-form text can be given to bias the transcription and improve recall on technical terms. This enables them to be used in production settings with domain-specific vocabulary without the need for fine-tuning.

* Multilingual Transcription
* Diarization
* Context Bias
* Artificial Analysis

### FLEURS 45 Forced vs Inferred

Word Error Rate — lower is better

4.1%4.0%4.1%4.0%4.6%4.5%6.1%4.5%4.9%4.9%6.3%5.6%16.0%14.9%Voxtral Small Transcribe 3Microsoft AI Transcribe 2Voxtral Mini Transcribe 3Gemini 3.5 TranscribeScribe v2GPT TranscribeWhisper large-v32.0%4.0%6.0%8.0%10.0%12.0%14.0%16.0%Word Error Rate

Macro-average WER over the intersection of 45 languages in the FLEURS benchmark supported by all seven models. WER is used for all languages except Japanese, Korean, Thai, and Chinese, which use CER. Lower is better.

Forced = language specified; Inferred = language auto-detected. Languages: AR, BN, BG, CA, ZH, CS, DA, NL, EN, ET, FI, FR, DE, EL, GU, HI, HU, IS, ID, IT, JA, KN, KO, LV, LT, MK, MS, ML, MR, NO, FA, PL, PT, RO, RU, SK, SL, ES, SV, FIL, TE, TH, TR, UK, VI

### Diarization

Concatenated Minimum Permutation WER — lower is better

18.4%18.6%19.0%20.3%23.0%30.9%38.4%Voxtral Small Transcribe 3Voxtral Mini Transcribe 3Pyannote Orchestrator (Precision 3)Microsoft AI Transcribe 2Scribe v2Voxtral Mini Transcribe 2Gemini 3.5 Transcribe15.0%20.0%25.0%30.0%35.0%40.0%Concatenated Minimum Permutation WER

Macro-average concatenated minimum permutation WER (cpWER) over public diarization benchmarks: AMI-IHM, AMI-SDM, Switchboard, Switchboard CallHome, AISHELL-4. For maximum compatibility of API baselines, we use 30 minute versions of AMI and AISHELL. Lower is better.

Diarization benchmark, Concatenated Minimum Permutation Word Error Rate (cpWER).

### Keyphrase Recall

With and without contextual prompting — higher is better

* Without Context
* With Context

94.6%81.4%94.3%84.0%87.3%80.9%Voxtral Small Transcribe 3Scribe v2Gemini 3.5 Transcribe75.0%80.0%85.0%90.0%95.0%100.0%Keyphrase Recall

Voxtral Small Transcribe 3 is highlighted in brand colours. Keyphrase recall on the Earnings 22 benchmarks. The context bias contains keyterms and a randomly sampled number of distractors, ranging from 0 to 100. Bars are superposed absolute values — the outer bar is recall with context, the inner bar is recall without context; the visible band is the uplift from contextual prompting. Higher is better.

Keyphrase recall benchmark. Context = domain-specific vocabulary and speaker names supplied to the model.

### Artificial Analysis Benchmark

Word Error Rate — lower is better

Fun-Realtime-ASR-previewMicrosoft AI Transcribe 2Voxtral Small Transcribe 3Scribe v2Voxtral Mini Transcribe 3Grok Voice Transcribe 2.0Microsoft AI Transcribe 1.5StepAudio 3 ASRGemini 3.5 TranscribeVoxtral SmallGemini 3.1 Pro Preview (High)Universal-3.5 ProSolaria-3, GladiaGPT TranscribeSmallest AI PulseResonant-1Smallest AI Pulse ProInkling, Thinking MachinesQwen3.5 Omni Plus RealtimeGemini 3.1 Pro Preview (Low)Voxtral Mini Transcribe 2Soniox v5 AsyncInworld STT 1GPT-4o TranscribeEnhancedWhisper large-v3Qwen3 ASR FlashAmazon TranscribeModulate STT Batch English VFastCanary Qwen 2.5BChirp 3GPT-4o Mini Transcribecohere-transcribe-03-2026Nova 2 Pro, AmazonMeliaNova-3, DeepgramRev AI1.0%2.0%3.0%4.0%5.0%6.0%AA WER

Artificial Analysis WER Index, a weighted average over VoxPopuli, Earnings-22 and AgentTalk.

Lower is better.

[Voxtral Realtime Transcribe 3](http://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-3-0) is a realtime transcription model built for agentic use-cases. It achieves high-quality transcriptions at sub-500ms latency in over 35 languages, including with diarization and context biasing.

### FLEURS 35

Realtime transcription Word Error Rate — lower is better

4.0%4.2%5.7%5.8%6.0%6.4%7.4%8.4%8.7%Voxtral Mini Transcribe 3\*Gemini 3.5 Realtime TranscribeVoxtral Mini Realtime 3 · 2400 msMicrosoft AI Transcribe 2 StreamingVoxtral Mini Realtime 3 · 960 msVoxtral Mini Realtime 3 · 480 msVoxtral Mini Realtime 3 · 240 msGPT Live TranscribeScribe v2 Realtime3.0%4.0%5.0%6.0%7.0%8.0%9.0%10.0%Word Error Rate

Macro-average WER over 35 languages from the FLEURS benchmark. WER is used for all languages except Japanese, Korean, and Chinese, which use CER. Lower is better. \*Voxtral Mini Transcribe 3 is an offline baseline. The remaining models are realtime.

Languages: AR, BN, BG, CA, CS, NL, EN, ET, FI, FR, DE, EL, GU, HI, ID, IT, JA, KN, KO, LV, MK, MS, ML, MR, NO, FA, PL, PT, RO, RU, SK, ES, FIL, TE, TR

End-of-turn prediction is natively supported, incorporating both acoustic and semantic information to accurately predict when a user is finished speaking. This allows for low-latency voice agent applications, while minimizing false cut-off rates when the user is prematurely interrupted.

## It answers with the right emotion, in your or your customer’s brand's own voice and local dialect.

[Voxtral Mini TTS 3.0](http://docs.mistral.ai/models/voxtral-mini-tts-3-0), available in batch and realtime, achieves state-of-the-art expressiveness and instruction following for 35+ languages and 50+ dialects. At $13 per 1M characters, Voxtral TTS costs less to run than comparable models from OpenAI TTS-1, Deepgram, ElevenLabs Flash and Gemini Flash.

The speech model implicitly interprets the semantic meaning of context better, producing natural speech across a diverse range of emotions and languages. New and improved features include voice cloning from 30+ minutes of sampled audio, custom prompt instruction following (IF), contextual TTS, and a vocabulary library, all of which serve the goal of speech reliability in deployment. Variables for Explicit IF include `emotion`, `pacing`, and `emphasis`.

EnglishFrenchItalianGerman

Prompt

Let's end the debate here: it's GIF.

Let's end the debate here. It's GIF.

Let's end the debate here. It's GIF.

Non-standard phoneme hint: dʒ ɪ f

Prompt

Attends… Ce n’est pas possible. Ce tableau vient de Reims ? Mais alors… C’est celui que ma grand-mère cherchait depuis cinquante ans !

Attends, ce n'est pas possible? Ce tableau vient de Reims? Mais alors, c'est celui que ma grand-mère cherchait depuis 50 ans?

Attends, ce n'est pas possible? Ce tableau viend de Reims? Mais alors? C'est celui que ma grand-mère cherchait depuis 50 ans.

Non-standard phoneme hint: ʁ e i m s

Prompt

Il nostro nuovo assistente si chiama Quivello.

Il nostro nuovo assistente si chiama Quivello.

Il nostro nuovo assistente si chiama Quivello.

Non-standard phoneme hint: tʃ i v ɛ l l o

Prompt

Hallo! Ich bin Xyra, deine persönliche Assistentin.

Hallo, ich bin Xyra, deine persönliche Assistentin.

Hallo, ich bin Xyra, deine persönliche Assistentin.

Non-standard phoneme hint: z aɪ ɹ ə

All natural-sounding speech relies on emotion, which determines its prosody, rhythm, pacing, emphasis, and transitions. Voxtral TTS natively interprets a prompt’s text context to determine the emotion and voice style, making the model inherently better at natural speech without requiring additional instructions or voice prompts.

* Voice Code Bench
* Pronunciation control
* Multilingual
* Expressiveness

### Voice Code Bench: quality per dollar

Voice Code Bench made by BeSimple AI is focused on enterprise customer support failure states related to numbers and unique names.

20%40%60%80%100%$0$10$20$30$40$50$60$70$80$90Faithful clipsPrice (USD per 1M characters)Eleven v4Eleven v4 TurboInworld TTS-2Inworld TTS-2 FlashFish Drama 3Gemini 3.8 Flash TTSQwen-Audio 3.1 FlashQwen-Audio 3.0 PlusCartesia Sonic 3.6Gemini 3.8 Flash Lite TTSDeepgram Flux TTSSpeechify Simba 3.2OpenAI gpt-4o-mini-ttsBreeze TTS 2StepFun StepAudio 2.5Voxtral TTS

Up and to the left is better.

Voice Code Bench (BeSimple AI): 300 English prompts, 2 voices per system (female and male); judge gemini-3.8-flash; prices from vendor pricing pages; generated 2026-10-20.

### Pronunciation control: quality per dollar

Share of clips where the target word is pronounced as intended, with its phonemes

50%60%70%80%90%$0$10$20$30$40$50$60$70$80$90Accurate pronunciationsPrice (USD per 1M characters)Voxtral TTSInworld TTS-2Cartesia Sonic 3.6Inworld TTS-2 FlashFish Drama 3Qwen-Audio 3.1 FlashEleven v4 TurboEleven v4Deepgram Flux TTSQwen-Audio 3.0 Plus

Internal eval. Up and to the left is better. Systems without a documented pronunciation control are listed in the data, not plotted.

300 English sentences, each with one rare or made-up word (150 easy, 150 hard), 2 voices per system; judge gemini-3.8-flash hears the clip with the word's intended IPA; prices from vendor pricing pages; generated 2026-10-20.

### Multilingual: quality per dollar

Mean judge score across 11 languages, 1 native voice per language and system

2.503.003.504.00$0$10$20$30$40$50$60$70$80$90Mean judge score (11 languages)Price (USD per 1M characters)Eleven v4Eleven v4 TurboCartesia Sonic 3.6Fish Drama 3Gemini 3.8 Flash Lite TTSGemini 3.8 Flash TTSInworld TTS-2Inworld TTS-2 FlashOpenAI gpt-4o-mini-ttsVoxtral TTS

Internal eval. Up and to the left is better. Systems covering fewer than 11 languages are listed in the data, not plotted.

377 prompts selected for release, 11 languages, unweighted mean of per-language mean judge scores, 1 to 5 scale; judge gemini-3.8-flash; prices from vendor pricing pages; generated 2026-10-20.

### Expressive English: quality per dollar

Mean judge score on one\_eval, 237 prompts selected for release

2.602.803.003.20$0$10$20$30$40$50$60$70$80$90Mean judge scorePrice (USD per 1M characters)Eleven v4Cartesia Sonic 3.6Eleven v4 TurboInworld TTS-2Gemini 3.8 Flash Lite TTSGemini 3.8 Flash TTSInworld TTS-2 FlashFish Drama 3Speechify Simba 3.2Qwen-Audio 3.1 FlashBreeze TTS 2OpenAI gpt-4o-mini-ttsStepFun StepAudio 2.5Deepgram Flux TTSQwen-Audio 3.0 PlusVoxtral TTS

Internal eval. Up and to the left is better.

Expressive English (one\_eval): 237 prompts selected for release, 2 voices per system (Voxtral TTS: Sarah and James), 1 to 5 scale; judge gemini-3.8-flash; prices from vendor pricing pages; generated 2026-10-20.

### Illustrating Voxtral hill-climbing in expressiveness, numbers and unique names.

### 

Customer SupportPersonal agentExcitedAngry

Prompt

Thank you for calling Mistral! I understand you're having difficulty logging into AI Studio. Can I confirm your email address? I have here elena.vance82@yahoo.com, is that correct?

Thank you for calling Mistral I understand you're having difficulty logging into AI Studio. Can I confirm your email address? I have here elena.vance82 @ yahoo.com. Is that correct?

Thank you for calling Mistral. I understand you're having difficulty logging into AI Studio. Can I confirm your email address? I have here elena.vance82 @ yahoo.com. Is that correct?

Prompt

Gosh that was quick, I've found a flight for your upcoming travel. How about the Emirates flight at 21:00pm on 10/10 returning 10/25 at 22:00pm for £1881? Say the word, and I'll book a window seat now.

Gosh, that was quick. I've found a flight for your upcoming travel. How about the Emirates flight at 21,000pm on 10 over 10, returning 10 over 25 at 22,000pm for £1,881? Say the word and I'll book a window seat now.

Gosh, that was quick. I found a flight for your upcoming travel. How about the Emirates flight at 21pm on October 10th, returning October 25th at 22pm for £1,881? Say the word and I'll book a window seat now.

Prompt

Wow I can't believe you're pregnant! This is so exciting, congratulations Corina, I'm so happy for you!

Wow, I can't believe you're pregnant. This is so exciting. Congratulations, Karina. I'm so happy for you.

Wow, I can't believe you're pregnant. This is so exciting. Congratulations, Karina. I'm so happy for you.

Prompt

What do you mean my passport won't be finished this week -- I've told you several times how I need to go to Paris for work. This is ridiculous. I can't even begin to describe how infuriating this has been.

What do you mean my passport won't be finished this week? I've told you several times how I need to go to Paris for work. This is ridiculous. I can't even begin to describe how infuriating this has been.

What do you mean my passport won't be finished this week? I've told you several times how I need to go to Paris for work. This is ridiculous. I can't even begin to describe how infuriating this has been.

### Speech sounds local in 35 languages and over 50 dialects.

Voxtral TTS supports over **35 languages** and regional dialects. Our multilingual evals adhere to dialect differences in pronunciation, formal vs. informal register, spelling, verbosity, and locale conventions (time, dates, temperatures, addresses, currencies).

Voxtral 3 multilingual library

Europe

Americas

Middle East and Africa

Asia-Pacific

English

French

Spanish

Catalan

Your browser does not support the audio element.

Dutch

Your browser does not support the audio element.

German

Your browser does not support the audio element.

Hungarian

Your browser does not support the audio element.

Italian

Your browser does not support the audio element.

Norwegian

Your browser does not support the audio element.

Polish

Your browser does not support the audio element.

Romanian

Your browser does not support the audio element.

Russian

Your browser does not support the audio element.

Turkish

Your browser does not support the audio element.

Ukrainian

Your browser does not support the audio element.

English

Portuguese

Arabic

Your browser does not support the audio element.

Chinese

Hindi

Your browser does not support the audio element.

Japanese

Your browser does not support the audio element.

Korean

Your browser does not support the audio element.

Vietnamese

Your browser does not support the audio element.

British

Your browser does not support the audio element.

France

Your browser does not support the audio element.

Spain

Your browser does not support the audio element.

American

Your browser does not support the audio element.

Brazilian

Your browser does not support the audio element.

Beijing

Your browser does not support the audio element.

Sichuan

Your browser does not support the audio element.

Voice Presets are available in 18 languages: Arabic (Emirati, Modern Standard), Brazilian (Portuguese), Catalan, Chinese (Mandarin), Dutch, English (American, British), French (France), German, Greek, Hindi, Italian, Korean, Norwegian, Russian, Spanish (Spain), and Vietnamese.

## The voice agent is in control of the whole conversation.

Voxtral 3 introduces a voice agent SDK, built on LiveKit, that runs speech in, reasoning, and speech out as one streaming pipeline. Voxtral Mini Transcribe Realtime 3 listens and detects when the caller has finished speaking, a general model—like [Mistral Small](https://docs.mistral.ai/models/mistral-small-4-0-26-03)—reasons and calls tools, and Voxtral TTS replies in the tone of the conversation so far. No stage waits for the one before it, so each turn completes in under one second, and the agent stops talking when the caller cuts in.

During a call, the agent can verify a caller's identity, check a bill, or book an appointment, using function calling, web search, and retrieval over your own systems. It answers and places calls over SIP, runs in browsers and apps over WebRTC, and connects to the telephony, IVR, and contact-center software you already use.

![](/_astro/diagram-voxtral-alt_25EnEW.webp?dpl=6b044261a8ba1bf79a6faf36)

Each stage is a separate model, so you can change the LLM, the voice, or the language without rewriting the agent, and run the whole stack on Mistral's API in Europe or on your own infrastructure.

## Get started.

Voxtral 3 is available today through the Mistral API, hosted through our European, US, and global endpoints.

You can test out voice agents, audio transcription, speech generation, and voice cloning in the Studio playgrounds.

[Try Voxtral now](https://console.mistral.ai/api-keys)  | [Learn more](https://docs.mistral.ai/studio/audio/overview)

| **Model** | **Price** |
| --- | --- |
| Voxtral Mini Transcribe 3 (batch) | $0.0035/min |
| Voxtral Mini Transcribe Realtime 3 | $0.008/min |
| Voxtral Small Transcribe 3 | $0.0040/min |
| Voxtral Mini TTS 3 | $13/1M chars |
| Voice agent API with Mistral Small 4 for reasoning | 0.04$/min |
| Voice agent API with larger model | 0.08$/min |

To run the full stack on-premises or in a private cloud, [talk to our team](https://mistral.ai/contact/).
