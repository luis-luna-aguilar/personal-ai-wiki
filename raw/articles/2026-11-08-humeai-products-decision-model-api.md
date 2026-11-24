---
title: Decision Model API | Hume AI
type: source
source_type: article
url: https://www.hume.ai/products/decision-model-api
fetched: 2026-11-08
note: letter-by-letter animated heading text removed; FAQ answers expanded in aside-browser and appended below. Page carries no publish date (launch campaign link, 2026-11-08).
---

# Decision Model API | Hume AI

NEW
Introducing the Hume Audio Decisions API
One model, any question, straight from audio
Emotion Science
Products
Solutions
Benchmarks
Resources
Talk to Hume
Decision models for voice AI
The bar is human. Hume diagnoses system breaks and feeds failures into improvement.
See a Demo
API Docs
(opens in a new tab)

A sample telehealth call plays while three questions about it are answered for every five seconds of audio.

Source:
Sample call
Microphone
Upload files
LISTENING..
Stop
Telehealth consultation

0:02 / 0:56

0:00
0:14
0:28
0:42
0:56
CONTEXT

A telehealth consultation between a clinician and a patient.

Yes/No
Does the patient sound anxious?
Pick One
Which best describes the clinician’s tone?
Scale
How reassured does the patient sound by the end?
Add question
You can add or change a question any time.

Yes
No
Not sure
Answered 0 of 12 chunks · every 5 seconds is answered on its own

Why audio needs a decision model

Voice AI considers tone, pauses, and sounds. Developers set Q&A; the audio decision model gives probabilities for quick audio judgments.

Watch Video
Different questions. The same audio.

Ask objective, subjective or perceptual questions about speech and sound. Select a tab to explore examples.

Audio Fact
Listener Judgment
Interaction Decisions
How many speakers are audible?
Are the speakers talking over each other?
What language is being spoken?
Is there background speech?
0%

One speaker

0%

Two speakers

0%

Three or more speakers

Find the audio worth acting on
Ask more of the same audio

Apply several questions to the same recordings, from naturalness and clarity to empathy and timing.

Designed for fast evaluation

Repeat evaluations across your collection as your model or criteria change.

Pinpoint cases for your next step

Find candidate examples for training, isolate evaluation failures, and surface cases for escalation review.

Running
25,642 files scanned 180 ms each
Searching for frustrated customer calls...
Customer sounds frustrated
is
Yes
Issue resolved
is
No
Add Question
Call 56
1:12
Yes
71%
No
63%
Call 908
1:55
Yes
66%
No
48%
Call 122
1:24
Yes
68%
No
50%
Call 87
0:58
Yes
74%
No
38%
Call 341
2:07
Yes
61%
No
57%
More reliable than
a single listener
See a Demo

The Audio Decision Model agrees with the human crowd 70.7% of the time, while a single human rater agrees 56.5% of the time.

Number of client hours processed.
1B hours
Human judgments across Hume’s work.
10M+

Agreement with a panel of human raters: Audio Decision Model 70.7%, Individual Rater 56.5%.

AGREEMENT WITH A PANEL OF HUMAN RATERS

Audio Decision Model

70.7%

Individual Rater

56.5%
100

Accuracy against speed: Hume’s Decision Model averages 0.82 over 10 leading benchmarks at 0.23 seconds median latency per screen, scoring higher and answering faster than Gemini 3.8 Flash, Qwen3.8-Omni-Flash, Inkling-Small, gpt-audio-1.5, Gemini 3.5 Flash Lite and Nemotron 3 Nano Omni.

ACCURACY AGAINST SPEED

0.1 s
0.2 s
1 s
2 s
10 s
0.50
0.60
0.70
0.80
Median latency per screen, seconds (log scale)
Average accuracy across leading benchmarks
HUME’S DECISION MODEL
Gemini 3.8 Flash
Qwen3.8-Omni-Flash
Inkling-Small
gpt-audio-1.5
Gemini 3.5 Flash Lite
Nemotron 3 Nano Omni

The Audio Decision Model answers audio questions faster and more accurately than any other model on the market.

Average score over 10 leading benchmarks: MMAU, ParaPair, EmphAssess, etc.
0.82
Median latency per screen
0.23 s
Compare the judgments that matter

Accuracy across the criteria you care about.

Hume’s Decision Model
Hume
82%
Gemini 3.8 Flash
Google
78%
Qwen3.8-Omni-Flash
Alibaba
76%
Inkling-Small
Thinking Machines
67%
Questions
about the model
What is Hume’s audio decision model?

It’s Hume’s audio-native decision model. Developers submit audio, a question and possible answers; it returns a probability for each answer. It helps teams evaluate speech and sound, assess how a voice comes across to listeners, and inform decisions in voice applications.

What is a decision model for audio or voice?
How is the audio decision model different from speech-to-text or a general-purpose audio LLM?
Can I define my own questions and ask several in one API call?
How can the audio decision model support voice-model evaluation and training?
How do I request Audio Decision Model API access?
Audio decisions that fit your stack.

Send audio, your question and possible answers.
The audio decision model returns a probability for each

curl https://api.hume.ai/v0/decisions/file \
  -H "X-Hume-Api-Key: $HUME_API_KEY" \
  -F file=@support_call.wav \
  -F 'request={
    "questions": {
      "background": {
        "type": "noul",
        "instructions": "Is there background speech?"
      },
      "speakers": {
        "type": "choice",
        "instructions": "How many speakers can you hear?",
        "criteria": [
          { "name": "One" },
          { "name": "Two" },
          { "name": "Three or more" }
        ]
      }
    }
  };type=application/json'

curl https://api.hume.ai/v0/decisions/file \
  -H "X-Hume-Api-Key: $HUME_API_KEY" \
  -F file=@support_call.wav \
  -F 'request={
    "questions": {
      "background": {
        "type": "noul",
        "instructions": "Is there background speech?"
      },
      "speakers": {
        "type": "choice",
        "instructions": "How many speakers can you hear?",
        "criteria": [
          { "name": "One" },
          { "name": "Two" },
          { "name": "Three or more" }
        ]
      }
    }
  };type=application/json'


Klingt der Sprecher gelangweilt?
Is there background speech?
どんな言語が話されているのですか？
Apa kabar anda saat ini?
Có bao nhiêu loa phát ra âm thanh?
¿El cliente suena frustrado?

Use the Decision Model API as a decision layer in a voice-agent system with speech recognition and generation.

Request API Access
Make emotionally
intelligent voice AI measurable
Talk to Hume
View Benchmark

Get new benchmark research and leaderboard updates.

Subscribe
PRODUCTS
Audio Decision API
Expression APIs
Human Feedback API
User Testing API
Speech Data
SOLUTIONS
Develop Voice Models
Deploy Voice Agents
Healthcare
Insurance
Financial Services
Customer Support
Travel & Hospitality
Telecom
BENCHMARK
Real-World VoiceEQ
Methodology
(opens in a new tab)
Emotion Science
RESOURCES
API Docs
(opens in a new tab)
Blog
Research & Insights
Publications
About
Careers
Privacy Policy
Terms of Service
© 2026 Hume AI, Inc.

## FAQ (expanded)

What is Hume's audio decision model?

It's Hume's audio-native decision model. Developers submit audio, a question and possible answers; it returns a probability for each answer.

What is a decision model for audio or voice?

A decision model listens to audio directly and answers a question you define with a probability for each possible answer, instead of transcribing first and guessing from text. That makes it suited to judgments that depend on how something sounds: tone, pacing, interruptions and background sound.

How is the audio decision model different from speech-to-text or a general-purpose audio LLM?

Speech-to-text tells you what was said; the audio decision model answers questions about how it was said and what it means for the conversation. Unlike a general-purpose audio LLM that generates free text, it returns calibrated probabilities over the answers you provide, so results are easy to compare, threshold and act on.

Can I define my own questions and ask several in one API call?

Yes. You write the questions and the possible answers (yes/no, pick one, or a scale) and can send several questions against the same audio in a single request.

How can the audio decision model support voice-model evaluation and training?

Run the same questions across your recordings to score naturalness, clarity, empathy or timing, compare model versions, find candidate examples for training and surface failures for review.

How do I request Audio Decision Model API access?

Use "Request API Access" and tell us about your use case. Our team will follow up with next steps.
