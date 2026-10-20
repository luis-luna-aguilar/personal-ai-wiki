---
title: 'ScaleDown website crawl (homepage, docs, API reference, research, examples, pricing)'
type: source
source_type: article
url: https://scaledown.ai/
fetched: 2026-10-19
fetched_via: aside-browser
note: '83 pages captured in one file; each section starts with its URL'
---

# ScaleDown website crawl


---8<--- page: docs-scaledown-ai-api-reference-batch-overview ---8<---

Page URL: https://docs.scaledown.ai/api-reference/batch-overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Compress
Overview
POST
Compress
On this page
What it does
When to use it
Common use cases
How it works
Supported models
Output format
Mixing types in one batch
Overview
Copy page

Process large volumes of extract, summarize, and classify requests asynchronously.

​
What it does
The Batch API lets you submit hundreds or thousands of extract, summarize, or classify requests in a single call and retrieve results when processing is complete. Instead of waiting for each request to return synchronously, you submit a JSONL body, get back a batch ID, and poll for output when ready.
The request format mirrors the realtime endpoints exactly — you use the same fields you already know, with "model" set to "extract", "summarize", or "classify" as the discriminator.
​
When to use it
You have a large backlog to process. If you need to run extraction, summarization, or classification across thousands of documents, submitting them as a batch is far more efficient than issuing individual synchronous requests.
Latency is not critical. Batch jobs complete asynchronously. If your pipeline can tolerate a delay — overnight document processing, weekly report generation, bulk data enrichment — Batch is the right tool.
You want to reduce complexity at scale. Batch processing avoids managing concurrency, retries, and rate limits on your side. Submit once, retrieve once.
​
Common use cases
Use case	Example
Bulk document extraction	Extract named entities from thousands of contracts overnight
Large-scale summarization	Summarize a backlog of articles, reports, or transcripts in one job
Batch content classification	Classify thousands of support tickets or emails by category
Data enrichment pipelines	Enrich a dataset with structured fields from unstructured text
Offline report generation	Process documents on a schedule without managing concurrency
​
How it works
[POST /v1/batches]  →  batch_id  →  [poll GET /v1/batches/{id}]  →  completed
                                               ↓
                                  [GET /v1/batches/{id}/output]  →  JSONL results

Submit — POST newline-delimited JSON (JSONL) with one request per line, or a single JSON object for one item. Each line has a custom_id you assign and a body with the same fields as the realtime endpoint.
Poll status — GET /v1/batches/{id} until status is "completed" or "failed".
Retrieve output — GET /v1/batches/{id}/output returns a JSONL file with one result per line, matched to your custom_id.
​
Supported models
model value	Equivalent realtime endpoint	Key fields
"extract"	POST /extract	text, entities, instruction
"summarize"	POST /summarization/abstractive	text, instructions, max_tokens
"classify"	POST /classify	text, labels, system_prompt
Any other value for model returns a 400 error immediately — no items are forwarded.
​
Output format
Each output line wraps the domain response in an OpenAI-compatible ChatCompletion shape. The domain result is JSON-serialized and placed in choices[0].message.content:
{
  "custom_id": "your-custom-id",
  "response": {
    "status_code": 200,
    "body": {
      "id": "chatcmpl-...",
      "object": "chat.completion",
      "model": "summarize",
      "choices": [{
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "{\"summary\": \"...\", \"input_chars\": 1200, \"output_chars\": 180}"
        },
        "finish_reason": "stop"
      }]
    }
  },
  "error": null
}

Parse choices[0].message.content as JSON to get the domain response fields.
​
Mixing types in one batch
A single batch can contain items of different types. The model field on each line is the discriminator — each line is processed independently.
{"custom_id": "s-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "summarize", "text": "..."}}
{"custom_id": "e-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "extract", "text": "...", "entities": {...}}}
{"custom_id": "c-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "classify", "text": "...", "labels": [...]}}

Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-api-reference-classify-overview ---8<---

Page URL: https://docs.scaledown.ai/api-reference/classify-overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Compress
Overview
POST
Compress
On this page
Two ways to classify
What it does
When to use it
Common use cases
How it fits into your workflow
Writing good rubrics
Classify
Classify overview
Copy page

Score text against labels you define. Use the custom /classify API for labels with rubrics, or the Jev-compatible Decisions API for typed questions.

​
Two ways to classify
Classify is one model (classify, or classify-1 to pin version 1) with two APIs. Pick based on the request shape you want to send.
	Custom ScaleDown API	Decisions API (Jev-compatible)
Endpoint	POST /classify	POST /v1/scaledown
You send	Text plus a list of labels, each with a rubric	A state plus named questions of type choice, noul or score
You get	A probability per label and a top_label	One typed answer per question
Best for	Routing, tagging and moderation where you write the rubrics	Porting an existing Jev integration, or asking several different questions about one item at once
Extras	Batching (chunks), multi-label, image input, reasoning	Same request and response shape as Jev
If you are not migrating from Jev, start with /classify. The Decisions API runs on the same scoring model, as a thinner layer over /classify.
​
What it does
The /classify endpoint takes a piece of text and a set of labels you define, then returns a probability score for each label indicating how well the text fits. Scores are softmax-normalised across all labels so they sum to 1.0, and the highest-scoring label is returned as top_label.
Each label is scored by running the text against a rubric - a yes/no question you write that describes what the label means. The model judges how strongly the text “answers yes” to each question, then normalises the results into a probability distribution.
​
When to use it
You need to route incoming content. Support tickets, user messages, or documents need to reach the right handler. Classify lets you define your own categories without training a model - just write rubrics that describe each category.
You’re building a moderation layer. A two-label setup (spam / not spam, safe / unsafe) gives you a confidence score you can threshold however your policy requires.
You need intent detection. Identify whether an incoming message is a question, complaint, feedback, or cancellation request - and act on it accordingly.
You want domain tagging at scale. Tag documents as medical, legal, financial, or any domain relevant to your pipeline, without fine-tuning or labelling training data.
​
Common use cases
Use case	How classify helps
Support ticket triage	Route tickets to billing, technical, or account teams automatically
Content moderation	Score content against a rubric for spam, toxicity, or policy violations
Intent detection	Identify question / complaint / feedback / cancellation intent
Domain tagging	Label documents by topic for downstream routing or filtering
Lead qualification	Score inbound inquiries against criteria like urgency or deal size
Email categorisation	Sort inbound email into categories without a rules engine
​
How it fits into your workflow
Classify sits between your input source and your routing or handling logic. You pass in the raw text - a ticket, a message, a document - and use the scores to decide what to do next.
[Incoming text] → [POST /classify] → [Route based on top_label or scores]

The response gives you both a top_label for simple routing and the full scores map if you need finer-grained control (e.g. only act if the top score exceeds a threshold).
​
Writing good rubrics
The rubric is the most important part of a classify request. Poor rubrics produce noisy, unreliable scores; well-written rubrics are specific, direct, and independent.
Rules of thumb:
Be specific. Vague rubrics produce low-confidence scores.
Frame as a yes/no question. “Does this text describe X?” outperforms “X content”.
Avoid negations. “Is this NOT about finance?” will confuse the model. Use a positive label instead.
Keep rubrics independent. Overlapping rubrics (e.g. “Is this medical?” and “Is this about health?”) split probability mass unpredictably.
Examples:
Label	Poor rubric	Good rubric
medical	medical content	Does this text describe a medical condition, symptom, treatment, or health topic?
urgent	urgent or important	Does this text indicate that the sender needs an immediate response or is describing a time-sensitive situation?
complaint	negative feedback	Is this text expressing dissatisfaction, frustration, or a formal complaint about a product or service?
Extract
Classify API
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-api-reference-classify ---8<---

Page URL: https://docs.scaledown.ai/api-reference/classify
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
POST
Classify API
Decisions API (Jev-compatible)
Compress
Overview
POST
Compress
Classify

cURL

curl --request POST \
  --url https://api.scaledown.xyz/classify \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "text": "<string>",
  "labels": [
    {
      "name": "<string>",
      "rubric": "<string>"
    }
  ]
}
'
200
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}
Custom ScaleDown API
Classify API
Copy page

POST /classify - score text against your own labels and rubrics and get a probability for each label.

POST
/
classify
Try it
​
Overview
The /classify endpoint scores a piece of text against a set of labels you define and returns a softmax-normalised probability distribution. Each label is scored using a rubric - a yes/no question that describes what the label means. The label with the highest score is returned as top_label.
​
Request
​
text
string
The text to classify. Provide exactly one of text, chunks, or document. If both text and document are given, the document text is appended after text.
​
chunks
array
A batch of inputs to classify against the same labels and system_prompt. Each item is { "id": string, "text": string }; the id is echoed back on the matching result so you can correlate them. Use this instead of sending one request per chunk: the shared profile (labels + system prompt) is billed once for the whole request instead of once per chunk. Cannot be combined with text or document. Capped at 50 chunks per request.
​
document
string
A base64-encoded file to classify. Supported formats: JPEG, PNG, TIFF, single-page PDF, multi-page PDF. The text is read from the file and used as input. Either text or document must be provided.
​
document_mime_type
string
MIME type of the document (e.g. "image/jpeg", "application/pdf"). Required when document is provided.
​
labels
arrayrequired
One or more label definitions. Must contain at least one item - sending an empty array returns 422.

Show Label fields

​
multi_label
booleandefault:"false"
When false (default), the labels are treated as mutually exclusive options: scores are a softmax distribution that sums to 1.0 and exactly one top_label is returned. When true, each label is scored independently (its own yes/no decision), so several labels can apply to the same input at once. Scores are independent probabilities that do not sum to 1, and every label whose score meets threshold is returned in matched_labels. Use this to attach multiple tags to a single input. Capped at 16 labels in multi-label mode.
​
threshold
numberdefault:"0.5"
Only used when multi_label is true. A label is included in matched_labels when its independent score is greater than or equal to this value. All scores are still returned, so you can also re-threshold client-side.
​
reasoning
booleandefault:"true"
When true (default), a second model call writes a one-sentence reasoning explaining the label chosen by the first call. Set false to skip it: faster, and the extra reasoning input tokens (billed at 2x) are not charged. Only applies to single-label requests with a single text/document; multi-label and batch (chunks) requests never return reasoning.
​
Response
​
top_label
string
Name of the highest-scoring label.
​
reasoning
string
One-sentence explanation of the decision (empty string when reasoning is false, or for multi-label and batch requests). It is generated after top_label is chosen, with the chosen label passed in, so it explains that decision. It is free-form text and is not a second opinion: if none of your labels fits the text well, it may say so (e.g. note that the text is about something else) while top_label still returns the best of the labels you gave. Add a catch-all label such as other to give those texts somewhere to go.
​
scores
object
Map of label name → probability score. All values sum to 1.0.
​
labels
array
Full label list with name, score, and rubric, in the same order as the request.

Show Label fields

​
results
array
Per-input results. Always present: for a single text/document request it has one element (with id "0") and the top-level top_label/scores/labels mirror it. For a chunks request there is one element per chunk, each carrying its own calibrated scores.

Show Result fields

​
chunk_count
integer
Number of inputs classified (1 for single-input requests).
​
ocr_text
string | null
The raw text extracted from the document. null if no document was provided.
Score semantics: In single-label mode, scores are relative probabilities that sum to 1 — a score of 0.85 means 85% of the probability mass relative to the other labels. In multi-label mode, each label’s score is an independent probability that it applies, so scores do not sum to 1 and should be compared against threshold individually.
​
Error responses
Status	Meaning
422 Unprocessable Entity	Malformed request body, empty labels array, none of text/chunks/document provided, more than 50 chunks, more than 20 labels (16 in multi-label mode), or the document could not be read.
502 Bad Gateway	Model service unavailable or returned an error.
​
Authentication
Include your API key in every request using the x-api-key header.
-H "x-api-key: <your-api-key>"

​
Examples
​
Basic topic classification
cURL
Python
TypeScript
const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();

Response:
{
  "top_label": "medical",
  "scores": {
    "medical": 0.887,
    "legal": 0.071,
    "financial": 0.042
  },
  "labels": [
    {
      "label": "medical",
      "score": 0.887,
      "rubric": "Does this text describe a medical condition, symptom, or health topic?"
    },
    {
      "label": "legal",
      "score": 0.071,
      "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
    },
    {
      "label": "financial",
      "score": 0.042,
      "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
    }
  ]
}

​
Support ticket triage
cURL
Python
TypeScript
const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();

Response:
{
  "top_label": "billing",
  "scores": {
    "billing": 0.921,
    "technical": 0.034,
    "account": 0.029,
    "general": 0.016
  },
  "labels": [
    { "label": "billing",   "score": 0.921, "rubric": "Is this text about a billing issue, charge, refund, or payment problem?" },
    { "label": "technical", "score": 0.034, "rubric": "Is this text about a technical problem, bug, or product not working correctly?" },
    { "label": "account",   "score": 0.029, "rubric": "Is this text about account access, login, password, or account settings?" },
    { "label": "general",   "score": 0.016, "rubric": "Is this a general question or inquiry that does not fit a specific support category?" }
  ]
}

​
Classifying a document
Pass a base64-encoded image or PDF in the document field. The text is extracted automatically and classified against your labels. The raw extracted text is returned as ocr_text.
cURL
Python
TypeScript
import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();

Response:
{
  "top_label": "invoice",
  "scores": {
    "invoice": 0.941,
    "contract": 0.037,
    "report": 0.022
  },
  "labels": [
    { "label": "invoice", "score": 0.941, "rubric": "Is this document an invoice or bill requesting payment?" },
    { "label": "contract", "score": 0.037, "rubric": "Is this document a legal contract or agreement between parties?" },
    { "label": "report", "score": 0.022, "rubric": "Is this document a business or financial report?" }
  ],
  "ocr_text": "INVOICE\nBill To: Acme Corp\nAmount Due: $4,200.00\nDue Date: June 1, 2025\n..."
}

​
Multi-label: attaching several tags to one input
Set multi_label: true to score each label independently, so more than one can apply to the same input. Every label whose score meets threshold is returned in matched_labels. This avoids sending the same input once per tag.
cURL
Python
TypeScript
const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();

Response: billing and churn_risk both cleared the threshold; scores are independent and do not sum to 1.
{
  "top_label": "churn_risk",
  "scores": { "billing": 0.88, "churn_risk": 0.79, "legal": 0.31 },
  "labels": [
    { "label": "billing",    "score": 0.88, "rubric": "Does this text describe a billing, invoice, or payment matter?" },
    { "label": "churn_risk", "score": 0.79, "rubric": "Does this text signal the customer may cancel or leave?" },
    { "label": "legal",      "score": 0.31, "rubric": "Does this text describe a legal or contractual dispute?" }
  ],
  "results": [
    {
      "id": "0",
      "top_label": "churn_risk",
      "matched_labels": ["billing", "churn_risk"],
      "scores": { "billing": 0.88, "churn_risk": 0.79, "legal": 0.31 },
      "labels": [
        { "label": "billing",    "score": 0.88, "rubric": "Does this text describe a billing, invoice, or payment matter?" },
        { "label": "churn_risk", "score": 0.79, "rubric": "Does this text signal the customer may cancel or leave?" },
        { "label": "legal",      "score": 0.31, "rubric": "Does this text describe a legal or contractual dispute?" }
      ]
    }
  ],
  "chunk_count": 1
}

​
Batch: classifying many chunks against one profile
Send a chunks array to classify many inputs against the same labels in one request. Each chunk still gets its own calibrated scores, but the shared profile (labels + system_prompt) is billed once for the whole request instead of once per chunk. Results are returned in results, correlated by id.
cURL
Python
TypeScript
const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();

Response: one entry per chunk, correlated by id. Top-level fields mirror the first result.
{
  "top_label": "praise",
  "scores": { "praise": 0.96, "bug_report": 0.04 },
  "labels": [
    { "label": "praise",     "score": 0.96, "rubric": "Is this text expressing satisfaction or positive feedback?" },
    { "label": "bug_report", "score": 0.04, "rubric": "Is this text reporting a bug or something not working?" }
  ],
  "results": [
    {
      "id": "msg-1",
      "top_label": "praise",
      "matched_labels": null,
      "scores": { "praise": 0.96, "bug_report": 0.04 },
      "labels": [
        { "label": "praise",     "score": 0.96, "rubric": "Is this text expressing satisfaction or positive feedback?" },
        { "label": "bug_report", "score": 0.04, "rubric": "Is this text reporting a bug or something not working?" }
      ]
    },
    {
      "id": "msg-2",
      "top_label": "bug_report",
      "matched_labels": null,
      "scores": { "praise": 0.02, "bug_report": 0.98 },
      "labels": [
        { "label": "praise",     "score": 0.02, "rubric": "Is this text expressing satisfaction or positive feedback?" },
        { "label": "bug_report", "score": 0.98, "rubric": "Is this text reporting a bug or something not working?" }
      ]
    }
  ],
  "chunk_count": 2
}

chunks and multi_label can be combined: every chunk is scored independently against every label.
​
Writing good rubrics
The rubric is the most important part of a classify request. It is phrased as a yes/no question the model uses to score each label. The model scores how strongly the text “answers yes” to the question.
Rules of thumb:
Be specific. Vague rubrics produce low-confidence, noisy scores.
Frame as a direct yes/no question. “Does this text describe X?” works better than “X content”.
Avoid negations. “Is this text NOT about finance?” will confuse the model. Use a positive label instead.
Keep rubrics independent. Overlapping rubrics (e.g. “Is this medical?” and “Is this about health?”) will split probability mass unpredictably.
Label	Poor rubric	Good rubric
medical	medical content	Does this text describe a medical condition, symptom, treatment, or health topic?
urgent	urgent or important	Does this text indicate that the sender needs an immediate response or is describing a time-sensitive situation?
complaint	negative feedback	Is this text expressing dissatisfaction, frustration, or a formal complaint about a product or service?
​
How it works
For each label, the model scores the text against the label’s rubric.
Raw scores are real-valued numbers (not probabilities).
Softmax normalisation is applied across all label scores so they sum to 1.0.
The label with the highest normalised score is returned as top_label.
The endpoint always returns a winner - even if the model is uncertain. If you need a confidence threshold, apply it yourself on the scores field.
​
Notes
A request supports up to 20 labels in either mode; multi-label mode is further capped at 16. Batch requests are capped at 50 chunks. Larger sets cost more: in single-label mode all labels and rubrics go into one model call, so every extra label adds its rubric to the billed input tokens (and to the reasoning call, which re-sends them at 2x); in multi-label mode each label is a separate model call, and each chunk is scored separately, run with bounded concurrency.
In single-label mode, scores are relative, not absolute. A top score of 0.4 in a 10-label request can still be the correct answer - it just means probability mass was spread across many labels.
Batch (chunks) exists to reduce cost: the shared profile is billed once per request instead of once per chunk. Calibration is identical to sending each chunk separately.
Multi-label and batch requests do not return a reasoning field; single-label requests return it by default (see the reasoning parameter).
Authorizations
​
x-api-key
stringheaderrequired
Body
application/json
​
text
stringrequired

The text to classify.

​
labels
object[]required

One or more label definitions. Must contain at least one item.

Show child attributes

Response
200
application/json

Successful classification

​
top_label
string

Name of the highest-scoring label.

​
scores
object

Map of label name to probability score. All values sum to 1.0.

Show child attributes

​
labels
object[]

Full label list with name, score, and rubric, in the same order as the request.

Show child attributes

Overview
Overview
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

ADDITIONAL VISIBLE STATES / CHART VALUES
INTERACTIVE TAB PANEL TEXT
--- cURL [tab 2] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();


--- Python [tab 3] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();


--- cURL [tab 5] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();


--- Python [tab 6] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();


--- cURL [tab 8] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();


--- Python [tab 9] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();


--- cURL [tab 11] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();


--- Python [tab 12] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();


--- cURL [tab 14] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();


--- Python [tab 15] ---
{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

{
  "top_label": "<string>",
  "scores": {},
  "labels": [
    {
      "label": "<string>",
      "score": 123,
      "rubric": "<string>"
    }
  ]
}

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The patient presents with a high fever and difficulty breathing.",
    "labels": [
      {
        "name": "medical",
        "rubric": "Does this text describe a medical condition, symptom, or health topic?"
      },
      {
        "name": "legal",
        "rubric": "Does this text describe a legal matter, contract, or regulatory issue?"
      },
      {
        "name": "financial",
        "rubric": "Does this text describe a financial transaction, investment, or monetary matter?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The patient presents with a high fever and difficulty breathing.",
        "labels": [
            {
                "name": "medical",
                "rubric": "Does this text describe a medical condition, symptom, or health topic?",
            },
            {
                "name": "legal",
                "rubric": "Does this text describe a legal matter, contract, or regulatory issue?",
            },
            {
                "name": "financial",
                "rubric": "Does this text describe a financial transaction, investment, or monetary matter?",
            },
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The patient presents with a high fever and difficulty breathing.",
    labels: [
      {
        name: "medical",
        rubric: "Does this text describe a medical condition, symptom, or health topic?",
      },
      {
        name: "legal",
        rubric: "Does this text describe a legal matter, contract, or regulatory issue?",
      },
      {
        name: "financial",
        rubric: "Does this text describe a financial transaction, investment, or monetary matter?",
      },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "I was charged twice for my subscription this month and need a refund immediately.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this text about a technical problem, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this text about account access, login, password, or account settings?"
      },
      {
        "name": "general",
        "rubric": "Is this a general question or inquiry that does not fit a specific support category?"
      }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "I was charged twice for my subscription this month and need a refund immediately.",
        "labels": [
            {"name": "billing",   "rubric": "Is this text about a billing issue, charge, refund, or payment problem?"},
            {"name": "technical", "rubric": "Is this text about a technical problem, bug, or product not working correctly?"},
            {"name": "account",   "rubric": "Is this text about account access, login, password, or account settings?"},
            {"name": "general",   "rubric": "Is this a general question or inquiry that does not fit a specific support category?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "I was charged twice for my subscription this month and need a refund immediately.",
    labels: [
      { name: "billing",   rubric: "Is this text about a billing issue, charge, refund, or payment problem?" },
      { name: "technical", rubric: "Is this text about a technical problem, bug, or product not working correctly?" },
      { name: "account",   rubric: "Is this text about account access, login, password, or account settings?" },
      { name: "general",   rubric: "Is this a general question or inquiry that does not fit a specific support category?" },
    ],
  }),
});
const data = await response.json();


# Encode a file and classify it
DOCUMENT=$(base64 -b 0 -i invoice.pdf)

curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf",
    "labels": [
      {
        "name": "invoice",
        "rubric": "Is this document an invoice or bill requesting payment?"
      },
      {
        "name": "contract",
        "rubric": "Is this document a legal contract or agreement between parties?"
      },
      {
        "name": "report",
        "rubric": "Is this document a business or financial report?"
      }
    ]
  }'


import base64
import requests

with open("invoice.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "labels": [
            {"name": "invoice", "rubric": "Is this document an invoice or bill requesting payment?"},
            {"name": "contract", "rubric": "Is this document a legal contract or agreement between parties?"},
            {"name": "report", "rubric": "Is this document a business or financial report?"},
        ],
    },
)
print(response.json())


import fs from "fs";

const document = fs.readFileSync("invoice.pdf").toString("base64");

const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    document,
    document_mime_type: "application/pdf",
    labels: [
      { name: "invoice", rubric: "Is this document an invoice or bill requesting payment?" },
      { name: "contract", rubric: "Is this document a legal contract or agreement between parties?" },
      { name: "report", rubric: "Is this document a business or financial report?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
    "multi_label": true,
    "threshold": 0.5,
    "labels": [
      { "name": "billing",     "rubric": "Does this text describe a billing, invoice, or payment matter?" },
      { "name": "churn_risk",  "rubric": "Does this text signal the customer may cancel or leave?" },
      { "name": "legal",       "rubric": "Does this text describe a legal or contractual dispute?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "text": "The invoice is overdue and the customer is threatening to cancel their contract.",
        "multi_label": True,
        "threshold": 0.5,
        "labels": [
            {"name": "billing",    "rubric": "Does this text describe a billing, invoice, or payment matter?"},
            {"name": "churn_risk", "rubric": "Does this text signal the customer may cancel or leave?"},
            {"name": "legal",      "rubric": "Does this text describe a legal or contractual dispute?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    text: "The invoice is overdue and the customer is threatening to cancel their contract.",
    multi_label: true,
    threshold: 0.5,
    labels: [
      { name: "billing",    rubric: "Does this text describe a billing, invoice, or payment matter?" },
      { name: "churn_risk", rubric: "Does this text signal the customer may cancel or leave?" },
      { name: "legal",      rubric: "Does this text describe a legal or contractual dispute?" },
    ],
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/classify \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "chunks": [
      { "id": "msg-1", "text": "I love the new dashboard, it saves me so much time." },
      { "id": "msg-2", "text": "The export button has been broken for a week." }
    ],
    "labels": [
      { "name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?" },
      { "name": "bug_report", "rubric": "Is this text reporting a bug or something not working?" }
    ]
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "chunks": [
            {"id": "msg-1", "text": "I love the new dashboard, it saves me so much time."},
            {"id": "msg-2", "text": "The export button has been broken for a week."},
        ],
        "labels": [
            {"name": "praise",     "rubric": "Is this text expressing satisfaction or positive feedback?"},
            {"name": "bug_report", "rubric": "Is this text reporting a bug or something not working?"},
        ],
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/classify", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    chunks: [
      { id: "msg-1", text: "I love the new dashboard, it saves me so much time." },
      { id: "msg-2", text: "The export button has been broken for a week." },
    ],
    labels: [
      { name: "praise",     rubric: "Is this text expressing satisfaction or positive feedback?" },
      { name: "bug_report", rubric: "Is this text reporting a bug or something not working?" },
    ],
  }),
});
const data = await response.json();

---8<--- page: docs-scaledown-ai-api-reference-compress-overview ---8<---

Page URL: https://docs.scaledown.ai/api-reference/compress-overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Compress
Overview
POST
Compress
On this page
What it does
When to use it
Common use cases
How it fits into your workflow
Pricing impact
Compress
Overview
Copy page

Reduce token usage across any AI workflow without changing your prompts or models.

​
What it does
The /compress/raw/ endpoint takes a prompt and its supporting context, then returns a semantically equivalent version that uses significantly fewer tokens. The compression is lossless in intent - the downstream model receives the same information, just expressed more efficiently.
Compression is applied primarily to the context field, where redundancy tends to be highest. The prompt (your actual question or instruction) is kept intact wherever possible to preserve precise intent.
​
When to use it
You’re spending too much on tokens. If your AI calls include long system prompts, retrieved documents, or conversation history, a large share of your token bill is coming from context - not the actual question. Compressing that context by 50–70% directly reduces cost with no changes to your model or application logic.
You’re hitting context window limits. Long documents, multi-turn conversations, and RAG pipelines frequently run into model context limits. Compression lets you fit more into a single call without truncating content or splitting requests.
You’re running latency-sensitive workloads. Fewer input tokens means faster time-to-first-token from the model. For real-time or user-facing applications, this can make a meaningful difference.
You want to use a smaller, cheaper model. Smaller models have tighter context windows. Compression makes it practical to run workloads on smaller models that would otherwise require a larger one.
​
Common use cases
Use case	How compression helps
RAG pipelines	Compress retrieved chunks before they’re included in the prompt
Long document Q&A	Fit full documents into context without truncation
Multi-turn chat	Compress conversation history to maintain context across long sessions
Code review / analysis	Compress large codebases or diffs passed as context
Batch processing	Reduce cost at scale when running the same pipeline across many documents
Reasoning model calls	Reduce the token overhead of chain-of-thought and reasoning traces
​
How it fits into your workflow
Compress sits between your data retrieval step and your model call. Your application logic doesn’t change - you just route the context through ScaleDown before sending it to the model.
[Your app] → [Retrieve context] → [POST /compress/raw/] → [Call your AI model]

The response nests the result under results. results.compressed_prompt is a drop-in replacement for the context you sent; your prompt is returned unchanged in results.original_prompt.
​
Pricing impact
Token savings translate directly to cost savings. At a 60% compression ratio, a workflow that previously cost 
10
/
𝑑
𝑎
𝑦
𝑖
𝑛
𝑡
𝑜
𝑘
𝑒
𝑛
𝑠
𝑝
𝑒
𝑛
𝑑
𝑑
𝑟
𝑜
𝑝
𝑠
𝑡
𝑜
10/dayintokenspenddropsto4/day - with no changes to the model, the output quality, or the application.
Decisions API
Compress
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-api-reference-compress ---8<---

Page URL: https://docs.scaledown.ai/api-reference/compress
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Compress
Overview
POST
Compress
Compress

cURL

curl --request POST \
  --url https://api.scaledown.xyz/compress/raw/ \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "context": "<string>",
  "prompt": "<string>",
  "scaledown": {
    "rate": "<string>"
  }
}
'
200
{
  "results": {
    "success": true,
    "compressed_prompt": "<string>",
    "original_prompt": "<string>",
    "original_prompt_tokens": 123,
    "compressed_prompt_tokens": 123,
    "compression_ratio": 123
  },
  "model_used": "<string>",
  "input_tokens": 123,
  "total_original_tokens": 123,
  "total_compressed_tokens": 123,
  "num_pairs_processed": 123,
  "num_successful": 123,
  "num_failed": 123,
  "successful": true,
  "partially_successful": true,
  "latency_ms": 123,
  "request_metadata": {
    "compression_time_ms": 123,
    "compression_rate": "<string>",
    "average_compression_ratio": 123
  }
}
Compress
Compress
Copy page

Compress a prompt and context to reduce token usage while preserving semantic meaning.

POST
/
compress
/
raw
/
Try it
​
Overview
The /compress/raw/ endpoint compresses your prompt and context, reducing token count while maintaining the semantic integrity needed for high-quality AI responses. Compression ratios of 50–70% are typical, with no meaningful degradation in downstream model output quality.
​
Request
​
context
stringrequired
Background information, instructions, or supporting text that provides context for the prompt. This is the content most aggressively compressed - structure and meaning are preserved, but redundancy is removed.
​
prompt
stringrequired
The main query or question to send to your AI model. Kept intact where possible to preserve intent.
​
scaledown
objectrequired
Compression configuration.

Show scaledown fields

​
Response
The compression result is nested under results; request-level totals and status are at the top level.
​
results
object

Show results fields

​
model_used
string
Tokenizer/model name used to count tokens.
​
input_tokens
number
Input tokens billed for the request.
​
total_original_tokens
number
Sum of original tokens across all pairs processed.
​
total_compressed_tokens
number
Sum of compressed tokens across all pairs processed.
​
num_pairs_processed
number
Number of context/prompt pairs in the request. num_successful and num_failed break this down.
​
successful
boolean
Whether every pair was compressed successfully. partially_successful is true if only some were.
​
latency_ms
number
End-to-end request latency in milliseconds.
​
request_metadata
object

Show Metadata fields

​
Error responses
Status	Meaning
400 Bad Request	Malformed request body or missing required fields.
401 Unauthorized	Missing or invalid x-api-key.
429 Too Many Requests	Rate limit exceeded. Back off and retry.
500 Internal Server Error	Compression service unavailable.
​
Authentication
Include your API key in every request using the x-api-key header.
-H "x-api-key: <your-api-key>"

​
Examples
​
Auto compression
cURL
Python
TypeScript
curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
    "prompt": "Summarize what ScaleDown does in one sentence.",
    "scaledown": {
      "rate": "auto"
    }
  }'

Response:
{
  "results": {
    "success": true,
    "compressed_prompt": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity.",
    "original_prompt": "Summarize what ScaleDown does in one sentence.",
    "original_prompt_tokens": 150,
    "compressed_prompt_tokens": 65,
    "compression_ratio": 0.43
  },
  "model_used": "gpt-4o",
  "input_tokens": 150,
  "total_original_tokens": 150,
  "total_compressed_tokens": 65,
  "num_pairs_processed": 1,
  "num_successful": 1,
  "num_failed": 0,
  "successful": true,
  "partially_successful": false,
  "latency_ms": 2341,
  "request_metadata": {
    "compression_time_ms": 2341,
    "compression_rate": "auto",
    "average_compression_ratio": 0.43
  }
}

​
Fixed compression rate
Pass a number for rate when you want a fixed level of compression. rate is the fraction of tokens to remove, so higher values compress more: 0.4 removes about 40% and keeps about 60%. The result is approximate, not an exact token budget.
cURL
Python
TypeScript
curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "...",
    "prompt": "What are the key points?",
    "scaledown": {
      "rate": 0.4
    }
  }'

​
Notes
"auto" rate is recommended for most use cases. Fixed rates below 0.3 may noticeably affect output quality on dense technical content.
The compressed_prompt field is a single string - pass it as the full prompt to your downstream model, replacing both context and prompt.
Authorizations
​
x-api-key
stringheaderrequired
Body
application/json
​
context
stringrequired

Background information, instructions, or supporting text that provides context for the prompt.

​
prompt
stringrequired

The main query or question to send to your AI model.

​
scaledown
objectrequired

Show child attributes

Response
200
application/json

Successful compression

​
results
object

Show child attributes

​
model_used
string
​
input_tokens
number
​
total_original_tokens
number
​
total_compressed_tokens
number
​
num_pairs_processed
number
​
num_successful
number
​
num_failed
number
​
successful
boolean
​
partially_successful
boolean
​
latency_ms
number
​
request_metadata
object

Show child attributes

Overview
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

ADDITIONAL VISIBLE STATES / CHART VALUES
INTERACTIVE TAB PANEL TEXT
--- Python [tab 3] ---
{
  "results": {
    "success": true,
    "compressed_prompt": "<string>",
    "original_prompt": "<string>",
    "original_prompt_tokens": 123,
    "compressed_prompt_tokens": 123,
    "compression_ratio": 123
  },
  "model_used": "<string>",
  "input_tokens": 123,
  "total_original_tokens": 123,
  "total_compressed_tokens": 123,
  "num_pairs_processed": 123,
  "num_successful": 123,
  "num_failed": 123,
  "successful": true,
  "partially_successful": true,
  "latency_ms": 123,
  "request_metadata": {
    "compression_time_ms": 123,
    "compression_rate": "<string>",
    "average_compression_ratio": 123
  }
}

{
  "results": {
    "success": true,
    "compressed_prompt": "<string>",
    "original_prompt": "<string>",
    "original_prompt_tokens": 123,
    "compressed_prompt_tokens": 123,
    "compression_ratio": 123
  },
  "model_used": "<string>",
  "input_tokens": 123,
  "total_original_tokens": 123,
  "total_compressed_tokens": 123,
  "num_pairs_processed": 123,
  "num_successful": 123,
  "num_failed": 123,
  "successful": true,
  "partially_successful": true,
  "latency_ms": 123,
  "request_metadata": {
    "compression_time_ms": 123,
    "compression_rate": "<string>",
    "average_compression_ratio": 123
  }
}

curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
    "prompt": "Summarize what ScaleDown does in one sentence.",
    "scaledown": {
      "rate": "auto"
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "context": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
        "prompt": "Summarize what ScaleDown does in one sentence.",
        "scaledown": {"rate": "auto"},
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/compress/raw/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    context: "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
    prompt: "Summarize what ScaleDown does in one sentence.",
    scaledown: { rate: "auto" },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "...",
    "prompt": "What are the key points?",
    "scaledown": {
      "rate": 0.4
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "context": "...",
        "prompt": "What are the key points?",
        "scaledown": {"rate": 0.4},
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/compress/raw/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    context: "...",
    prompt: "What are the key points?",
    scaledown: { rate: 0.4 },
  }),
});
const data = await response.json();


--- TypeScript [tab 4] ---
{
  "results": {
    "success": true,
    "compressed_prompt": "<string>",
    "original_prompt": "<string>",
    "original_prompt_tokens": 123,
    "compressed_prompt_tokens": 123,
    "compression_ratio": 123
  },
  "model_used": "<string>",
  "input_tokens": 123,
  "total_original_tokens": 123,
  "total_compressed_tokens": 123,
  "num_pairs_processed": 123,
  "num_successful": 123,
  "num_failed": 123,
  "successful": true,
  "partially_successful": true,
  "latency_ms": 123,
  "request_metadata": {
    "compression_time_ms": 123,
    "compression_rate": "<string>",
    "average_compression_ratio": 123
  }
}

{
  "results": {
    "success": true,
    "compressed_prompt": "<string>",
    "original_prompt": "<string>",
    "original_prompt_tokens": 123,
    "compressed_prompt_tokens": 123,
    "compression_ratio": 123
  },
  "model_used": "<string>",
  "input_tokens": 123,
  "total_original_tokens": 123,
  "total_compressed_tokens": 123,
  "num_pairs_processed": 123,
  "num_successful": 123,
  "num_failed": 123,
  "successful": true,
  "partially_successful": true,
  "latency_ms": 123,
  "request_metadata": {
    "compression_time_ms": 123,
    "compression_rate": "<string>",
    "average_compression_ratio": 123
  }
}

curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
    "prompt": "Summarize what ScaleDown does in one sentence.",
    "scaledown": {
      "rate": "auto"
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "context": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
        "prompt": "Summarize what ScaleDown does in one sentence.",
        "scaledown": {"rate": "auto"},
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/compress/raw/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    context: "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
    prompt: "Summarize what ScaleDown does in one sentence.",
    scaledown: { rate: "auto" },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "...",
    "prompt": "What are the key points?",
    "scaledown": {
      "rate": 0.4
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "context": "...",
        "prompt": "What are the key points?",
        "scaledown": {"rate": 0.4},
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/compress/raw/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    context: "...",
    prompt: "What are the key points?",
    scaledown: { rate: 0.4 },
  }),
});
const data = await response.json();


--- Python [tab 6] ---
{
  "results": {
    "success": true,
    "compressed_prompt": "<string>",
    "original_prompt": "<string>",
    "original_prompt_tokens": 123,
    "compressed_prompt_tokens": 123,
    "compression_ratio": 123
  },
  "model_used": "<string>",
  "input_tokens": 123,
  "total_original_tokens": 123,
  "total_compressed_tokens": 123,
  "num_pairs_processed": 123,
  "num_successful": 123,
  "num_failed": 123,
  "successful": true,
  "partially_successful": true,
  "latency_ms": 123,
  "request_metadata": {
    "compression_time_ms": 123,
    "compression_rate": "<string>",
    "average_compression_ratio": 123
  }
}

{
  "results": {
    "success": true,
    "compressed_prompt": "<string>",
    "original_prompt": "<string>",
    "original_prompt_tokens": 123,
    "compressed_prompt_tokens": 123,
    "compression_ratio": 123
  },
  "model_used": "<string>",
  "input_tokens": 123,
  "total_original_tokens": 123,
  "total_compressed_tokens": 123,
  "num_pairs_processed": 123,
  "num_successful": 123,
  "num_failed": 123,
  "successful": true,
  "partially_successful": true,
  "latency_ms": 123,
  "request_metadata": {
    "compression_time_ms": 123,
    "compression_rate": "<string>",
    "average_compression_ratio": 123
  }
}

curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
    "prompt": "Summarize what ScaleDown does in one sentence.",
    "scaledown": {
      "rate": "auto"
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "context": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
        "prompt": "Summarize what ScaleDown does in one sentence.",
        "scaledown": {"rate": "auto"},
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/compress/raw/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    context: "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
    prompt: "Summarize what ScaleDown does in one sentence.",
    scaledown: { rate: "auto" },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "...",
    "prompt": "What are the key points?",
    "scaledown": {
      "rate": 0.4
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "context": "...",
        "prompt": "What are the key points?",
        "scaledown": {"rate": 0.4},
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/compress/raw/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    context: "...",
    prompt: "What are the key points?",
    scaledown: { rate: 0.4 },
  }),
});
const data = await response.json();


--- TypeScript [tab 7] ---
{
  "results": {
    "success": true,
    "compressed_prompt": "<string>",
    "original_prompt": "<string>",
    "original_prompt_tokens": 123,
    "compressed_prompt_tokens": 123,
    "compression_ratio": 123
  },
  "model_used": "<string>",
  "input_tokens": 123,
  "total_original_tokens": 123,
  "total_compressed_tokens": 123,
  "num_pairs_processed": 123,
  "num_successful": 123,
  "num_failed": 123,
  "successful": true,
  "partially_successful": true,
  "latency_ms": 123,
  "request_metadata": {
    "compression_time_ms": 123,
    "compression_rate": "<string>",
    "average_compression_ratio": 123
  }
}

{
  "results": {
    "success": true,
    "compressed_prompt": "<string>",
    "original_prompt": "<string>",
    "original_prompt_tokens": 123,
    "compressed_prompt_tokens": 123,
    "compression_ratio": 123
  },
  "model_used": "<string>",
  "input_tokens": 123,
  "total_original_tokens": 123,
  "total_compressed_tokens": 123,
  "num_pairs_processed": 123,
  "num_successful": 123,
  "num_failed": 123,
  "successful": true,
  "partially_successful": true,
  "latency_ms": 123,
  "request_metadata": {
    "compression_time_ms": 123,
    "compression_rate": "<string>",
    "average_compression_ratio": 123
  }
}

curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
    "prompt": "Summarize what ScaleDown does in one sentence.",
    "scaledown": {
      "rate": "auto"
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "context": "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
        "prompt": "Summarize what ScaleDown does in one sentence.",
        "scaledown": {"rate": "auto"},
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/compress/raw/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    context: "ScaleDown is a context engineering platform. It compresses AI prompts while preserving semantic integrity...",
    prompt: "Summarize what ScaleDown does in one sentence.",
    scaledown: { rate: "auto" },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "context": "...",
    "prompt": "What are the key points?",
    "scaledown": {
      "rate": 0.4
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "context": "...",
        "prompt": "What are the key points?",
        "scaledown": {"rate": 0.4},
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/compress/raw/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    context: "...",
    prompt: "What are the key points?",
    scaledown: { rate: 0.4 },
  }),
});
const data = await response.json();

---8<--- page: docs-scaledown-ai-api-reference-decisions-overview ---8<---

Page URL: https://docs.scaledown.ai/api-reference/decisions-overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Overview
POST
Decisions API
Compress
Overview
POST
Compress
On this page
What it does
When to use it
How it fits into your workflow
Model
Differences from Jev
Decisions API (Jev-compatible)
Decisions overview
Copy page

A drop-in replacement for the Jev Decisions API: answer typed choice, yes/no and scale questions about a piece of text.

​
What it does
The /v1/scaledown endpoint answers typed questions about a piece of text or a document, in the same request/response shape as TypeSafe’s Jev Decisions API (POST /api/alpha/decisions on OpenRouter). If you already have integration code written against Jev, it should work against /v1/scaledown with only the base URL changed.
You send a state object (the item being decided on) and a questions map, where each question is one of three typed primitives:
choice - pick exactly one option from a set of criteria. Backed by the same calibrated single-label decode as /classify.
noul - an independent yes/no question, answered as a probability. Backed by the same calibrated binary decode /classify uses in multi-label mode.
score - an ordered-scale question, e.g. rating severity or quality. Answered with the same calibrated decode as choice, over an ordered list of levels, then reduced to a probability-weighted expected value - see How score is calculated.
Every question in a request is answered against the same shared state, concurrently.
​
When to use it
You’re porting an existing Jev integration. /v1/scaledown accepts the same request shape and returns the same response shape, so a Jev-based routing or tagging layer can point at api.scaledown.xyz instead with minimal changes.
You want several classification decisions from one request. Mix choice, noul, and score questions in a single call - e.g. pick a category, check an independent tag, and rate severity - instead of making separate /classify calls.
You don’t need our classify-specific features. /v1/scaledown is a thin, standard-shaped layer over /classify. If you need batching (chunks), image-direct multimodal input, or the free-form reasoning explanation (returned by default, controlled by the reasoning parameter), use /classify directly - /v1/scaledown intentionally doesn’t expose those.
​
How it fits into your workflow
[Jev-shaped request] → [POST /v1/scaledown] → [choice/noul/score answered via /classify's scoring] → [answers + usage]

Internally, each choice question becomes one single-label classify call (its criteria become labels), each noul question becomes one binary yes/no classify call, and each score question becomes one single-label classify call over its ordered levels (reduced afterward to an expected value). All run concurrently against the shared state, and the response’s usage is the sum of every internal call’s tokens.
​
Model
The supported model values are "classify" (always the latest version) and "classify-1" (pinned to version 1), which are currently identical. "classify-1" is the default when the field is omitted. Sending any other value returns 422. There’s currently no way to select a different backend model through this endpoint.
​
Differences from Jev
	Jev	/v1/scaledown
choice / noul / score	✅	✅
Mixed question types per request	✅	✅ - routed internally, answered concurrently
Arbitrary multi-field state object	✅	Only state.text / state.document are read
Model selection	Multiple models	Only "classify" / "classify-1"
Batch input (many items per request)	❌	Not on /v1/scaledown - use /classify’s chunks
Document / image classification	❌	state.document + state.document_mime_type (non-standard extension)
Free-form reasoning explanation	❌	Not available on this endpoint (see /classify’s reasoning field)
Classify API
Decisions API
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-api-reference-decisions ---8<---

Page URL: https://docs.scaledown.ai/api-reference/decisions
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Overview
POST
Decisions API
Compress
Overview
POST
Compress
Decisions

cURL

curl --request POST \
  --url https://api.scaledown.xyz/v1/scaledown \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '
{
  "state": "<string>",
  "questions": {},
  "model": "classify-1"
}
'
200
{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}
Decisions API (Jev-compatible)
Decisions API
Copy page

POST /v1/scaledown - Jev-compatible request and response. Send a state and a set of typed questions, get one answer per question.

POST
/
v1
/
scaledown
Try it
​
Overview
The /v1/scaledown endpoint mirrors TypeSafe’s Jev Decisions API request/response shape. You send a state object plus a questions map, and get back one typed answer per question. choice, noul, and score questions are all answered using the same calibrated scoring /classify uses.
​
Request
​
model
stringdefault:"classify-1"
Optional. "classify" (always the latest version) or "classify-1" (pinned to version 1). Defaults to "classify-1" when omitted. Any other value is rejected with 422.
​
state
object | stringrequired
The item being decided on. Pass a plain string as shorthand for { "text": "..." }, matching TypeSafe’s API, or an object to use the fields below.

Show State fields

​
questions
objectrequired
A map of question name → question definition. Must contain at least one entry. Every question is answered against the same state, concurrently.

Show choice question

Show noul question

Show score question

​
Response
​
model
string
Echoes the model you sent ("classify" or "classify-1"; "classify-1" if omitted).
​
answers
object
Map of question name → typed answer, matching the questions keys from the request.

Show choice answer

Show noul answer

Show score answer

​
usage
object
Token usage and cost, summed across every internal call the request fanned out to (one per question, regardless of type).

Show Usage fields

​
How score is calculated
A score question is answered with the same constrained, calibrated decode choice uses - one model call scores every level in criteria, producing a probability distribution over them (probabilities). That distribution is then reduced to a single continuous score value: the probability-weighted expected value across level indices.
For example, given criteria with 3 levels (indices 0, 1, 2) and probabilities: {"0": 0.0, "1": 0.57, "2": 0.43}:
score = 0×0.0 + 1×0.57 + 2×0.43 = 1.43

score is therefore a continuous position on the scale, not necessarily a whole level - a value near 1.43 says the model leans toward level 2 but isn’t fully decided between levels 1 and 2. Use probabilities (or confidence, the top level’s own probability) if you need the calibration behind that number instead of just the point estimate.
​
Error responses
Status	Meaning
422 Unprocessable Entity	Malformed request body, empty questions map, empty criteria on a choice question, criteria outside the 2-10 range on a score question, neither state.text nor state.document provided, an unsupported model value, or the document could not be read.
402 Payment Required	Insufficient credits.
502 Bad Gateway	Model service unavailable or returned an error.
504 Gateway Timeout	Request timed out.
​
Authentication
Include your API key in every request using the x-api-key header.
-H "x-api-key: <your-api-key>"

​
Examples
​
Single choice question
cURL
Python
TypeScript
import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "model": "classify-1",
        "state": {"text": "I was charged twice for my subscription this month."},
        "questions": {
            "category": {
                "type": "choice",
                "instructions": "Which single category best describes the post?",
                "criteria": {
                    "billing": "About a charge, invoice, refund, or payment problem.",
                    "technical": "About a bug or something not working.",
                    "account": "About login, access, or account settings.",
                },
            }
        },
    },
)
print(response.json())

Response:
{
  "model": "classify-1",
  "answers": {
    "category": {
      "type": "choice",
      "choice": "billing",
      "probabilities": { "billing": 0.93, "technical": 0.04, "account": 0.03 },
      "confidence": 0.93
    }
  },
  "usage": { "input_tokens": 62, "output_tokens": 1, "cost": 0.0000026 }
}

​
Mixed choice + noul questions
choice and noul questions can be combined in one request. Both are answered concurrently against the same state.
cURL
Python
TypeScript
import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {"text": "The invoice is overdue and the customer is threatening to cancel."},
        "questions": {
            "category": {
                "type": "choice",
                "criteria": {
                    "billing": "About a charge, invoice, or payment matter.",
                    "legal": "About a legal or contractual dispute.",
                },
            },
            "is_churn_risk": {
                "type": "noul",
                "instructions": "Does this text signal the customer may cancel or leave?",
            },
        },
    },
)
print(response.json())

Response:
{
  "model": "classify-1",
  "answers": {
    "category": {
      "type": "choice",
      "choice": "billing",
      "probabilities": { "billing": 0.88, "legal": 0.12 },
      "confidence": 0.88
    },
    "is_churn_risk": { "type": "noul", "noul": 0.79 }
  },
  "usage": { "input_tokens": 94, "output_tokens": 2, "cost": 0.0000039 }
}

​
A score question
Use score for an ordered-scale rating, like severity or quality. criteria is an ordered array, not a map - level 0 is the first item, level 1 the second, and so on.
cURL
Python
TypeScript
import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {
            "text": "The export button crashes the settings page in Safari. "
            "It works in Chrome, but a few of our customers only use Safari."
        },
        "questions": {
            "bug_severity": {
                "type": "score",
                "instructions": "How severe is the reported issue?",
                "criteria": [
                    "Cosmetic; no impact to functionality",
                    "Broken or degraded feature, but workaround exists",
                    "Blocking issue; no workaround exists",
                ],
            }
        },
    },
)
print(response.json())

Response:
{
  "model": "classify-1",
  "answers": {
    "bug_severity": {
      "type": "score",
      "score": 1.43,
      "confidence": 0.57,
      "legend": {
        "0": "Cosmetic; no impact to functionality",
        "1": "Broken or degraded feature, but workaround exists",
        "2": "Blocking issue; no workaround exists"
      },
      "probabilities": { "0": 0.0, "1": 0.57, "2": 0.43 }
    }
  },
  "usage": { "input_tokens": 68, "output_tokens": 1, "cost": 0.0000029 }
}

score: 1.43 (0×0.0 + 1×0.57 + 2×0.43) says the model leans toward “blocking issue” (level 2) but isn’t fully decided between that and “broken or degraded” (level 1).
​
Mixing all three question types
choice, noul, and score questions can all appear in the same request. Every question is answered concurrently against the same state, and usage sums across all of them.
cURL
curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "Great product, but the onboarding was confusing." },
    "questions": {
      "sentiment": {
        "type": "choice",
        "criteria": { "positive": "Overall positive tone.", "negative": "Overall negative tone." }
      },
      "is_actionable": {
        "type": "noul",
        "instructions": "Does this feedback suggest a specific, actionable improvement?"
      },
      "quality_score": {
        "type": "score",
        "instructions": "Rate overall product quality.",
        "criteria": ["poor", "average", "excellent"]
      }
    }
  }'

Response:
{
  "model": "classify-1",
  "answers": {
    "sentiment": {
      "type": "choice",
      "choice": "positive",
      "probabilities": { "positive": 0.81, "negative": 0.19 },
      "confidence": 0.81
    },
    "is_actionable": { "type": "noul", "noul": 0.72 },
    "quality_score": {
      "type": "score",
      "score": 1.65,
      "confidence": 0.51,
      "legend": { "0": "poor", "1": "average", "2": "excellent" },
      "probabilities": { "0": 0.03, "1": 0.46, "2": 0.51 }
    }
  },
  "usage": { "input_tokens": 103, "output_tokens": 3, "cost": 0.0000044 }
}

​
Notes
"classify" and "classify-1" are the only supported model values. Omit it (defaults to "classify-1") or pass either explicitly - any other value is rejected with 422.
Every question in a request - choice, noul, or score - is one separate calibrated model call, run concurrently. usage is the sum across all of them - a request with a choice, a noul, and a score question makes 3 calls and bills for all 3.
score’s criteria is an ordered array (2-10 levels), unlike choice’s unordered {key: description} map - the array position is the level index.
No reasoning field exists on this endpoint - it never generates a free-form explanation, unlike /classify, which returns one by default (the reasoning parameter).
No batching - each request evaluates one state. To classify many items, use /classify’s chunks array instead.
See Differences from Jev for the full compatibility matrix.
Authorizations
​
x-api-key
stringheaderrequired
Body
application/json
​
state
string
object
string
required

The item being decided on. A plain string is shorthand for {"text": "..."}.

​
questions
objectrequired

Map of question name to question definition. Must contain at least one entry.

Show child attributes

​
model
enum<string>default:classify-1

Optional. "classify-1" is the only supported value and also the default when omitted. Any other value returns 422.

Available options: classify-1 
Response
200
application/json

Successful decision

​
model
string

Always "classify-1".

​
answers
object

Map of question name to typed answer, matching the questions keys from the request.

Show child attributes

​
usage
object

Token usage and cost, summed across every internal call the request fanned out to.

Show child attributes

Overview
Overview
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

ADDITIONAL VISIBLE STATES / CHART VALUES
INTERACTIVE TAB PANEL TEXT
--- cURL [tab 2] ---
{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "classify-1",
    "state": "I was charged twice for my subscription this month.",
    "questions": {
      "category": {
        "type": "choice",
        "instructions": "Which single category best describes the post?",
        "criteria": {
          "billing": "About a charge, invoice, refund, or payment problem.",
          "technical": "About a bug or something not working.",
          "account": "About login, access, or account settings."
        }
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "model": "classify-1",
        "state": {"text": "I was charged twice for my subscription this month."},
        "questions": {
            "category": {
                "type": "choice",
                "instructions": "Which single category best describes the post?",
                "criteria": {
                    "billing": "About a charge, invoice, refund, or payment problem.",
                    "technical": "About a bug or something not working.",
                    "account": "About login, access, or account settings.",
                },
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    model: "classify-1",
    state: { text: "I was charged twice for my subscription this month." },
    questions: {
      category: {
        type: "choice",
        instructions: "Which single category best describes the post?",
        criteria: {
          billing: "About a charge, invoice, refund, or payment problem.",
          technical: "About a bug or something not working.",
          account: "About login, access, or account settings.",
        },
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The invoice is overdue and the customer is threatening to cancel." },
    "questions": {
      "category": {
        "type": "choice",
        "criteria": {
          "billing": "About a charge, invoice, or payment matter.",
          "legal": "About a legal or contractual dispute."
        }
      },
      "is_churn_risk": {
        "type": "noul",
        "instructions": "Does this text signal the customer may cancel or leave?"
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {"text": "The invoice is overdue and the customer is threatening to cancel."},
        "questions": {
            "category": {
                "type": "choice",
                "criteria": {
                    "billing": "About a charge, invoice, or payment matter.",
                    "legal": "About a legal or contractual dispute.",
                },
            },
            "is_churn_risk": {
                "type": "noul",
                "instructions": "Does this text signal the customer may cancel or leave?",
            },
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: { text: "The invoice is overdue and the customer is threatening to cancel." },
    questions: {
      category: {
        type: "choice",
        criteria: {
          billing: "About a charge, invoice, or payment matter.",
          legal: "About a legal or contractual dispute.",
        },
      },
      is_churn_risk: {
        type: "noul",
        instructions: "Does this text signal the customer may cancel or leave?",
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari." },
    "questions": {
      "bug_severity": {
        "type": "score",
        "instructions": "How severe is the reported issue?",
        "criteria": [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists"
        ]
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {
            "text": "The export button crashes the settings page in Safari. "
            "It works in Chrome, but a few of our customers only use Safari."
        },
        "questions": {
            "bug_severity": {
                "type": "score",
                "instructions": "How severe is the reported issue?",
                "criteria": [
                    "Cosmetic; no impact to functionality",
                    "Broken or degraded feature, but workaround exists",
                    "Blocking issue; no workaround exists",
                ],
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: {
      text: "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari.",
    },
    questions: {
      bug_severity: {
        type: "score",
        instructions: "How severe is the reported issue?",
        criteria: [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists",
        ],
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "Great product, but the onboarding was confusing." },
    "questions": {
      "sentiment": {
        "type": "choice",
        "criteria": { "positive": "Overall positive tone.", "negative": "Overall negative tone." }
      },
      "is_actionable": {
        "type": "noul",
        "instructions": "Does this feedback suggest a specific, actionable improvement?"
      },
      "quality_score": {
        "type": "score",
        "instructions": "Rate overall product quality.",
        "criteria": ["poor", "average", "excellent"]
      }
    }
  }'


--- TypeScript [tab 4] ---
{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "classify-1",
    "state": "I was charged twice for my subscription this month.",
    "questions": {
      "category": {
        "type": "choice",
        "instructions": "Which single category best describes the post?",
        "criteria": {
          "billing": "About a charge, invoice, refund, or payment problem.",
          "technical": "About a bug or something not working.",
          "account": "About login, access, or account settings."
        }
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "model": "classify-1",
        "state": {"text": "I was charged twice for my subscription this month."},
        "questions": {
            "category": {
                "type": "choice",
                "instructions": "Which single category best describes the post?",
                "criteria": {
                    "billing": "About a charge, invoice, refund, or payment problem.",
                    "technical": "About a bug or something not working.",
                    "account": "About login, access, or account settings.",
                },
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    model: "classify-1",
    state: { text: "I was charged twice for my subscription this month." },
    questions: {
      category: {
        type: "choice",
        instructions: "Which single category best describes the post?",
        criteria: {
          billing: "About a charge, invoice, refund, or payment problem.",
          technical: "About a bug or something not working.",
          account: "About login, access, or account settings.",
        },
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The invoice is overdue and the customer is threatening to cancel." },
    "questions": {
      "category": {
        "type": "choice",
        "criteria": {
          "billing": "About a charge, invoice, or payment matter.",
          "legal": "About a legal or contractual dispute."
        }
      },
      "is_churn_risk": {
        "type": "noul",
        "instructions": "Does this text signal the customer may cancel or leave?"
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {"text": "The invoice is overdue and the customer is threatening to cancel."},
        "questions": {
            "category": {
                "type": "choice",
                "criteria": {
                    "billing": "About a charge, invoice, or payment matter.",
                    "legal": "About a legal or contractual dispute.",
                },
            },
            "is_churn_risk": {
                "type": "noul",
                "instructions": "Does this text signal the customer may cancel or leave?",
            },
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: { text: "The invoice is overdue and the customer is threatening to cancel." },
    questions: {
      category: {
        type: "choice",
        criteria: {
          billing: "About a charge, invoice, or payment matter.",
          legal: "About a legal or contractual dispute.",
        },
      },
      is_churn_risk: {
        type: "noul",
        instructions: "Does this text signal the customer may cancel or leave?",
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari." },
    "questions": {
      "bug_severity": {
        "type": "score",
        "instructions": "How severe is the reported issue?",
        "criteria": [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists"
        ]
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {
            "text": "The export button crashes the settings page in Safari. "
            "It works in Chrome, but a few of our customers only use Safari."
        },
        "questions": {
            "bug_severity": {
                "type": "score",
                "instructions": "How severe is the reported issue?",
                "criteria": [
                    "Cosmetic; no impact to functionality",
                    "Broken or degraded feature, but workaround exists",
                    "Blocking issue; no workaround exists",
                ],
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: {
      text: "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari.",
    },
    questions: {
      bug_severity: {
        type: "score",
        instructions: "How severe is the reported issue?",
        criteria: [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists",
        ],
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "Great product, but the onboarding was confusing." },
    "questions": {
      "sentiment": {
        "type": "choice",
        "criteria": { "positive": "Overall positive tone.", "negative": "Overall negative tone." }
      },
      "is_actionable": {
        "type": "noul",
        "instructions": "Does this feedback suggest a specific, actionable improvement?"
      },
      "quality_score": {
        "type": "score",
        "instructions": "Rate overall product quality.",
        "criteria": ["poor", "average", "excellent"]
      }
    }
  }'


--- cURL [tab 5] ---
{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "classify-1",
    "state": "I was charged twice for my subscription this month.",
    "questions": {
      "category": {
        "type": "choice",
        "instructions": "Which single category best describes the post?",
        "criteria": {
          "billing": "About a charge, invoice, refund, or payment problem.",
          "technical": "About a bug or something not working.",
          "account": "About login, access, or account settings."
        }
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "model": "classify-1",
        "state": {"text": "I was charged twice for my subscription this month."},
        "questions": {
            "category": {
                "type": "choice",
                "instructions": "Which single category best describes the post?",
                "criteria": {
                    "billing": "About a charge, invoice, refund, or payment problem.",
                    "technical": "About a bug or something not working.",
                    "account": "About login, access, or account settings.",
                },
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    model: "classify-1",
    state: { text: "I was charged twice for my subscription this month." },
    questions: {
      category: {
        type: "choice",
        instructions: "Which single category best describes the post?",
        criteria: {
          billing: "About a charge, invoice, refund, or payment problem.",
          technical: "About a bug or something not working.",
          account: "About login, access, or account settings.",
        },
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The invoice is overdue and the customer is threatening to cancel." },
    "questions": {
      "category": {
        "type": "choice",
        "criteria": {
          "billing": "About a charge, invoice, or payment matter.",
          "legal": "About a legal or contractual dispute."
        }
      },
      "is_churn_risk": {
        "type": "noul",
        "instructions": "Does this text signal the customer may cancel or leave?"
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {"text": "The invoice is overdue and the customer is threatening to cancel."},
        "questions": {
            "category": {
                "type": "choice",
                "criteria": {
                    "billing": "About a charge, invoice, or payment matter.",
                    "legal": "About a legal or contractual dispute.",
                },
            },
            "is_churn_risk": {
                "type": "noul",
                "instructions": "Does this text signal the customer may cancel or leave?",
            },
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: { text: "The invoice is overdue and the customer is threatening to cancel." },
    questions: {
      category: {
        type: "choice",
        criteria: {
          billing: "About a charge, invoice, or payment matter.",
          legal: "About a legal or contractual dispute.",
        },
      },
      is_churn_risk: {
        type: "noul",
        instructions: "Does this text signal the customer may cancel or leave?",
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari." },
    "questions": {
      "bug_severity": {
        "type": "score",
        "instructions": "How severe is the reported issue?",
        "criteria": [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists"
        ]
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {
            "text": "The export button crashes the settings page in Safari. "
            "It works in Chrome, but a few of our customers only use Safari."
        },
        "questions": {
            "bug_severity": {
                "type": "score",
                "instructions": "How severe is the reported issue?",
                "criteria": [
                    "Cosmetic; no impact to functionality",
                    "Broken or degraded feature, but workaround exists",
                    "Blocking issue; no workaround exists",
                ],
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: {
      text: "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari.",
    },
    questions: {
      bug_severity: {
        type: "score",
        instructions: "How severe is the reported issue?",
        criteria: [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists",
        ],
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "Great product, but the onboarding was confusing." },
    "questions": {
      "sentiment": {
        "type": "choice",
        "criteria": { "positive": "Overall positive tone.", "negative": "Overall negative tone." }
      },
      "is_actionable": {
        "type": "noul",
        "instructions": "Does this feedback suggest a specific, actionable improvement?"
      },
      "quality_score": {
        "type": "score",
        "instructions": "Rate overall product quality.",
        "criteria": ["poor", "average", "excellent"]
      }
    }
  }'


--- TypeScript [tab 7] ---
{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "classify-1",
    "state": "I was charged twice for my subscription this month.",
    "questions": {
      "category": {
        "type": "choice",
        "instructions": "Which single category best describes the post?",
        "criteria": {
          "billing": "About a charge, invoice, refund, or payment problem.",
          "technical": "About a bug or something not working.",
          "account": "About login, access, or account settings."
        }
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "model": "classify-1",
        "state": {"text": "I was charged twice for my subscription this month."},
        "questions": {
            "category": {
                "type": "choice",
                "instructions": "Which single category best describes the post?",
                "criteria": {
                    "billing": "About a charge, invoice, refund, or payment problem.",
                    "technical": "About a bug or something not working.",
                    "account": "About login, access, or account settings.",
                },
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    model: "classify-1",
    state: { text: "I was charged twice for my subscription this month." },
    questions: {
      category: {
        type: "choice",
        instructions: "Which single category best describes the post?",
        criteria: {
          billing: "About a charge, invoice, refund, or payment problem.",
          technical: "About a bug or something not working.",
          account: "About login, access, or account settings.",
        },
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The invoice is overdue and the customer is threatening to cancel." },
    "questions": {
      "category": {
        "type": "choice",
        "criteria": {
          "billing": "About a charge, invoice, or payment matter.",
          "legal": "About a legal or contractual dispute."
        }
      },
      "is_churn_risk": {
        "type": "noul",
        "instructions": "Does this text signal the customer may cancel or leave?"
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {"text": "The invoice is overdue and the customer is threatening to cancel."},
        "questions": {
            "category": {
                "type": "choice",
                "criteria": {
                    "billing": "About a charge, invoice, or payment matter.",
                    "legal": "About a legal or contractual dispute.",
                },
            },
            "is_churn_risk": {
                "type": "noul",
                "instructions": "Does this text signal the customer may cancel or leave?",
            },
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: { text: "The invoice is overdue and the customer is threatening to cancel." },
    questions: {
      category: {
        type: "choice",
        criteria: {
          billing: "About a charge, invoice, or payment matter.",
          legal: "About a legal or contractual dispute.",
        },
      },
      is_churn_risk: {
        type: "noul",
        instructions: "Does this text signal the customer may cancel or leave?",
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari." },
    "questions": {
      "bug_severity": {
        "type": "score",
        "instructions": "How severe is the reported issue?",
        "criteria": [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists"
        ]
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {
            "text": "The export button crashes the settings page in Safari. "
            "It works in Chrome, but a few of our customers only use Safari."
        },
        "questions": {
            "bug_severity": {
                "type": "score",
                "instructions": "How severe is the reported issue?",
                "criteria": [
                    "Cosmetic; no impact to functionality",
                    "Broken or degraded feature, but workaround exists",
                    "Blocking issue; no workaround exists",
                ],
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: {
      text: "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari.",
    },
    questions: {
      bug_severity: {
        type: "score",
        instructions: "How severe is the reported issue?",
        criteria: [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists",
        ],
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "Great product, but the onboarding was confusing." },
    "questions": {
      "sentiment": {
        "type": "choice",
        "criteria": { "positive": "Overall positive tone.", "negative": "Overall negative tone." }
      },
      "is_actionable": {
        "type": "noul",
        "instructions": "Does this feedback suggest a specific, actionable improvement?"
      },
      "quality_score": {
        "type": "score",
        "instructions": "Rate overall product quality.",
        "criteria": ["poor", "average", "excellent"]
      }
    }
  }'


--- cURL [tab 8] ---
{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "classify-1",
    "state": "I was charged twice for my subscription this month.",
    "questions": {
      "category": {
        "type": "choice",
        "instructions": "Which single category best describes the post?",
        "criteria": {
          "billing": "About a charge, invoice, refund, or payment problem.",
          "technical": "About a bug or something not working.",
          "account": "About login, access, or account settings."
        }
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "model": "classify-1",
        "state": {"text": "I was charged twice for my subscription this month."},
        "questions": {
            "category": {
                "type": "choice",
                "instructions": "Which single category best describes the post?",
                "criteria": {
                    "billing": "About a charge, invoice, refund, or payment problem.",
                    "technical": "About a bug or something not working.",
                    "account": "About login, access, or account settings.",
                },
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    model: "classify-1",
    state: { text: "I was charged twice for my subscription this month." },
    questions: {
      category: {
        type: "choice",
        instructions: "Which single category best describes the post?",
        criteria: {
          billing: "About a charge, invoice, refund, or payment problem.",
          technical: "About a bug or something not working.",
          account: "About login, access, or account settings.",
        },
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The invoice is overdue and the customer is threatening to cancel." },
    "questions": {
      "category": {
        "type": "choice",
        "criteria": {
          "billing": "About a charge, invoice, or payment matter.",
          "legal": "About a legal or contractual dispute."
        }
      },
      "is_churn_risk": {
        "type": "noul",
        "instructions": "Does this text signal the customer may cancel or leave?"
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {"text": "The invoice is overdue and the customer is threatening to cancel."},
        "questions": {
            "category": {
                "type": "choice",
                "criteria": {
                    "billing": "About a charge, invoice, or payment matter.",
                    "legal": "About a legal or contractual dispute.",
                },
            },
            "is_churn_risk": {
                "type": "noul",
                "instructions": "Does this text signal the customer may cancel or leave?",
            },
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: { text: "The invoice is overdue and the customer is threatening to cancel." },
    questions: {
      category: {
        type: "choice",
        criteria: {
          billing: "About a charge, invoice, or payment matter.",
          legal: "About a legal or contractual dispute.",
        },
      },
      is_churn_risk: {
        type: "noul",
        instructions: "Does this text signal the customer may cancel or leave?",
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari." },
    "questions": {
      "bug_severity": {
        "type": "score",
        "instructions": "How severe is the reported issue?",
        "criteria": [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists"
        ]
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {
            "text": "The export button crashes the settings page in Safari. "
            "It works in Chrome, but a few of our customers only use Safari."
        },
        "questions": {
            "bug_severity": {
                "type": "score",
                "instructions": "How severe is the reported issue?",
                "criteria": [
                    "Cosmetic; no impact to functionality",
                    "Broken or degraded feature, but workaround exists",
                    "Blocking issue; no workaround exists",
                ],
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: {
      text: "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari.",
    },
    questions: {
      bug_severity: {
        type: "score",
        instructions: "How severe is the reported issue?",
        criteria: [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists",
        ],
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "Great product, but the onboarding was confusing." },
    "questions": {
      "sentiment": {
        "type": "choice",
        "criteria": { "positive": "Overall positive tone.", "negative": "Overall negative tone." }
      },
      "is_actionable": {
        "type": "noul",
        "instructions": "Does this feedback suggest a specific, actionable improvement?"
      },
      "quality_score": {
        "type": "score",
        "instructions": "Rate overall product quality.",
        "criteria": ["poor", "average", "excellent"]
      }
    }
  }'


--- TypeScript [tab 10] ---
{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

{
  "model": "<string>",
  "answers": {},
  "usage": {
    "input_tokens": 123,
    "output_tokens": 123,
    "cost": 123
  }
}

curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "classify-1",
    "state": "I was charged twice for my subscription this month.",
    "questions": {
      "category": {
        "type": "choice",
        "instructions": "Which single category best describes the post?",
        "criteria": {
          "billing": "About a charge, invoice, refund, or payment problem.",
          "technical": "About a bug or something not working.",
          "account": "About login, access, or account settings."
        }
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "model": "classify-1",
        "state": {"text": "I was charged twice for my subscription this month."},
        "questions": {
            "category": {
                "type": "choice",
                "instructions": "Which single category best describes the post?",
                "criteria": {
                    "billing": "About a charge, invoice, refund, or payment problem.",
                    "technical": "About a bug or something not working.",
                    "account": "About login, access, or account settings.",
                },
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    model: "classify-1",
    state: { text: "I was charged twice for my subscription this month." },
    questions: {
      category: {
        type: "choice",
        instructions: "Which single category best describes the post?",
        criteria: {
          billing: "About a charge, invoice, refund, or payment problem.",
          technical: "About a bug or something not working.",
          account: "About login, access, or account settings.",
        },
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The invoice is overdue and the customer is threatening to cancel." },
    "questions": {
      "category": {
        "type": "choice",
        "criteria": {
          "billing": "About a charge, invoice, or payment matter.",
          "legal": "About a legal or contractual dispute."
        }
      },
      "is_churn_risk": {
        "type": "noul",
        "instructions": "Does this text signal the customer may cancel or leave?"
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {"text": "The invoice is overdue and the customer is threatening to cancel."},
        "questions": {
            "category": {
                "type": "choice",
                "criteria": {
                    "billing": "About a charge, invoice, or payment matter.",
                    "legal": "About a legal or contractual dispute.",
                },
            },
            "is_churn_risk": {
                "type": "noul",
                "instructions": "Does this text signal the customer may cancel or leave?",
            },
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: { text: "The invoice is overdue and the customer is threatening to cancel." },
    questions: {
      category: {
        type: "choice",
        criteria: {
          billing: "About a charge, invoice, or payment matter.",
          legal: "About a legal or contractual dispute.",
        },
      },
      is_churn_risk: {
        type: "noul",
        instructions: "Does this text signal the customer may cancel or leave?",
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari." },
    "questions": {
      "bug_severity": {
        "type": "score",
        "instructions": "How severe is the reported issue?",
        "criteria": [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists"
        ]
      }
    }
  }'


import requests

response = requests.post(
    "https://api.scaledown.xyz/v1/scaledown",
    headers={"x-api-key": "<your-api-key>"},
    json={
        "state": {
            "text": "The export button crashes the settings page in Safari. "
            "It works in Chrome, but a few of our customers only use Safari."
        },
        "questions": {
            "bug_severity": {
                "type": "score",
                "instructions": "How severe is the reported issue?",
                "criteria": [
                    "Cosmetic; no impact to functionality",
                    "Broken or degraded feature, but workaround exists",
                    "Blocking issue; no workaround exists",
                ],
            }
        },
    },
)
print(response.json())


const response = await fetch("https://api.scaledown.xyz/v1/scaledown", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "<your-api-key>",
  },
  body: JSON.stringify({
    state: {
      text: "The export button crashes the settings page in Safari. It works in Chrome, but a few of our customers only use Safari.",
    },
    questions: {
      bug_severity: {
        type: "score",
        instructions: "How severe is the reported issue?",
        criteria: [
          "Cosmetic; no impact to functionality",
          "Broken or degraded feature, but workaround exists",
          "Blocking issue; no workaround exists",
        ],
      },
    },
  }),
});
const data = await response.json();


curl -X POST https://api.scaledown.xyz/v1/scaledown \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "state": { "text": "Great product, but the onboarding was confusing." },
    "questions": {
      "sentiment": {
        "type": "choice",
        "criteria": { "positive": "Overall positive tone.", "negative": "Overall negative tone." }
      },
      "is_actionable": {
        "type": "noul",
        "instructions": "Does this feedback suggest a specific, actionable improvement?"
      },
      "quality_score": {
        "type": "score",
        "instructions": "Rate overall product quality.",
        "criteria": ["poor", "average", "excellent"]
      }
    }
  }'

---8<--- page: docs-scaledown-ai-api-reference-extract-overview ---8<---

Page URL: https://docs.scaledown.ai/api-reference/extract-overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Compress
Overview
POST
Compress
On this page
What it does
When to use it
Common use cases
How it fits into your workflow
Tips for better results
Compared to traditional NER
Extract
Overview
Copy page

Pull structured data from unstructured text using a schema you define in plain English.

​
What it does
The extract model, called through the OpenAI-compatible POST /v1/chat/completions endpoint, runs Named Entity Recognition (NER) over arbitrary text - but instead of a fixed set of entity types (person, place, organization), you define exactly what you’re looking for in plain English. The model interprets your descriptions and finds matching spans in the text, returning each one with a confidence score, character offsets, and surrounding context.
This makes it practical to extract domain-specific entities that generic NER models don’t support: contract parties, product SKUs, medical terms, financial figures, custom identifiers, or anything else you can describe.
​
When to use it
You need structured data from unstructured text. If your pipeline involves parsing documents, emails, web pages, or transcripts to pull out specific values, Extract replaces brittle regex patterns and rigid NLP pipelines with a flexible, description-driven approach.
Your entity types don’t fit standard NER. Off-the-shelf NER handles names, locations, and organizations. Extract handles whatever you define - lease terms, part numbers, clinical findings, competitor mentions, or any other domain-specific concept.
You need confidence scores. Extract returns a confidence score for every result. Set a threshold (globally or per entity type) to drop low-confidence hits, or use the scores to route extractions to a human review queue.
You want context alongside every result. Every extracted span comes with 500 characters of surrounding text on each side, so you can verify the extraction in context without going back to the source document.
Your source is an image or scan, not text. Send a base64-encoded photo, scan, or PDF in the document field (via extra_body) and Extract reads the text before extraction - so receipts, invoices, IDs, business cards, and scanned forms work without a separate preprocessing step. See Extracting from an image or PDF.
Some of your fields are decisions, not spans. Booleans and small categories - “is this account past due?”, “electric or gas?” - have no verbatim span to pull. Constrain those keys to a fixed set of choices (an enum, or a oneOf of const branches) and Extract routes them to the classification model, which is a Constrained Decoding Model (CDM) purpose-built for categorical decisions, while extracting the rest as normal. Per-label rubrics (via oneOf) describe when each label applies and meaningfully improve accuracy. See Classification keys.
​
Common use cases
Use case	Example entities
Contract analysis	Parties, effective dates, termination clauses, governing law
Resume parsing	Name, email, skills, companies, job titles, education
Medical records	Diagnoses, medications, dosages, lab values, dates of service
Financial documents	Revenue figures, dates, entities, regulatory references
Customer support tickets	Product names, error codes, account identifiers
News / media monitoring	People, organizations, locations, quoted statements
E-commerce	Product names, prices, SKUs, brands, specifications
Scanned images & receipts	Merchant, total, date, line items, tax from a photo or scan
​
How it fits into your workflow
Extract sits between your document ingestion step and whatever system consumes structured data - a database, a downstream process, or a human review interface.
[Ingest document] → [POST /v1/chat/completions, model "extract"] → [Structured entity list] → [Database / downstream system]

Each entity in the response includes character offsets (start, end), so you can highlight or link back to the exact location in the source document.
​
Tips for better results
The entity name and description are treated as part of the model’s prompt - how you phrase them directly affects extraction quality.
Use lowercase or Title Case labels. The model was trained with lowercase entity names. person, company, and date work better than PERSON or DATE.
Be specific, and test synonyms. person and full name find slightly different things. If results are missing or noisy, try rephrasing the label name.
Labels can be descriptive phrases. "capital city and population center" is a perfectly valid label name and will outperform a bare "city" when you need that distinction.
Descriptions can be instructions. Write "Find the first and last name of the person in the text" rather than just "Name". Full instructions consistently outperform short noun phrases.
Don’t mix overlapping granularities. Including both "location" and "city" in the same call forces the model to split results between them unpredictably. Pick one level of granularity per concept.
​
Compared to traditional NER
	Traditional NER	ScaleDown Extract
Entity types	Fixed (person, place, org, …)	You define them in plain English
Domain specificity	General-purpose	Works for any domain
Confidence scores	Varies by model	Always included
Per-entity thresholds	Not typically supported	Supported
Context window	Usually sentence-level	Full document
Structured / nested output	Not supported	Supported via nested object and array schemas
Categorical / boolean fields	Extracted as text (lower accuracy)	Routed to a purpose-built classifier via enum / oneOf
Document / image input	Not supported	Supported via base64
Summarize
Extract
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-api-reference-extract ---8<---

Page URL: https://docs.scaledown.ai/api-reference/extract
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Compress
Overview
POST
Compress
On this page
Overview
Request
Response
Error responses
Authentication
Examples
Basic extraction
Extracting from an image or PDF
Structured (nested) extraction
Classification keys
Multiple matches, with limits
Writing good entity labels
Notes
Extract
Extract
Copy page

Extract named entities from text using a custom-defined schema through the OpenAI-compatible chat completions API.

​
Overview
Extract is called through the OpenAI-compatible POST /v1/chat/completions endpoint. Set model to extract (latest) or extract-1 (pinned version), put the text in the last user message, and describe the fields you want with the standard response_format JSON schema. The model runs Named Entity Recognition over the text. Unlike standard NER, you define the entity types in plain English - each property name becomes an entity type and its description is the search criteria - and each match comes back with a confidence score and surrounding context.
Because the endpoint is OpenAI-compatible, you can point an unmodified OpenAI or OpenRouter SDK at ScaleDown by changing only the base URL and API key.
POST https://api.scaledown.xyz/v1/chat/completions

​
Request
​
model
stringrequired
"extract" (always the latest version) or "extract-1" (pinned to version 1). Both currently behave identically.
​
messages
arrayrequired
Standard OpenAI chat messages. The last user message is the text to extract from. Any system messages are joined and used as a global instruction - rules that apply across all entity types, such as deduplication logic or ranking constraints.
​
response_format
objectrequired
Defines what to extract. Must be { "type": "json_schema", "json_schema": { "name": "...", "schema": {...} } }. Each property of schema.properties is an entity type:
A scalar property (string, number, integer, boolean) - its description says what to look for. Each distinct value found in the text is returned as its own entity (up to 30 per type)
A nested object (type: "object" with properties) - a structured sub-schema
An array of objects (type: "array" with object items) - a repeated structure, such as line items
A classification key - a property with an enum, or a oneOf of const branches, routed to the classifier (see Classification keys)
Per-property threshold (0-1) and top_n annotations override the global values for that entity type only. $ref and $defs are not supported; inline your schema. Alternatively, send a flat top-level entities object instead of response_format (see below).
​
threshold
numberdefault:0
Non-standard extension, passed with the SDK’s extra_body. Global confidence threshold (0-1). Extracted entities whose confidence is below it are dropped. 0 (default) keeps everything. Can be overridden per entity type. Does not apply to nested/array schemas or classification keys.
​
top_n
numberdefault:0
Non-standard extension, passed with extra_body. Global limit on how many entities to return per entity type, keeping the most confident. 0 (default) returns all matches. Results are still returned in order of appearance in the text. Can be overridden per entity type.
​
context_chars
numberdefault:500
Non-standard extension, passed with extra_body. Number of characters of surrounding text to include on each side of a matched span in the context response field. Set to 0 to omit context entirely.
​
document
string
Non-standard extension, passed with extra_body. A base64-encoded file to extract from. Supported formats: JPEG, PNG, TIFF, single-page PDF, multi-page PDF. The text is read from the file and used as input; if the user message also has text, the document text is appended after it.
​
document_mime_type
string
Non-standard extension, passed with extra_body. MIME type of the document (e.g. "image/jpeg", "application/pdf"). Required when document is provided.
​
entities
object
Optional flat alternative to response_format, matching a batch item body. A mapping of entity type name to a description string, or to an object with description, threshold and top_n, a nested object, an array of objects, or a classification config {"labels": [{"name": ..., "rubric": ...}]}. When present it takes precedence over response_format. Top-level text and instruction likewise take precedence over the user and system messages.
​
Response
A standard chat.completion. The extraction result is a JSON string in choices[0].message.content - parse it to read the fields below.
​
model
string
Echoes the model you sent (extract or extract-1).
​
usage
object
prompt_tokens is the input tokens billed for the request, completion_tokens the model’s output tokens, and total_tokens their sum.
​
choices[0].message.content
string
A JSON string with these fields:

Show Parsed content

​
Error responses
Status	Meaning
400 Bad Request	No input text, response_format missing or not json_schema, a schema with no properties, or a $ref/$defs in the schema.
402 Payment Required	Insufficient credits.
422 Unprocessable Entity	Malformed request body, a classification key with fewer than 2 or more than 20 labels, or the document could not be read.
500 Internal Server Error	Inference service unavailable.
504 Gateway Timeout	Extraction request timed out.
​
Authentication
Include your API key in every request using the x-api-key header. Authorization: Bearer <your-api-key> is also accepted, so an OpenAI SDK only needs its api_key set.
-H "x-api-key: <your-api-key>"

​
Examples
The Python and TypeScript examples assume this client:
import json
from openai import OpenAI

client = OpenAI(base_url="https://api.scaledown.xyz/v1", api_key="<your-api-key>")

​
Basic extraction
cURL
Python
TypeScript
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'

The parsed content is:
{
  "entities": [
    {"text": "Acme Corp", "type": "vendor", "confidence": 0.97, "start": 0, "end": 9, "context": "Acme Corp invoiced $500 on 2024-01-05."},
    {"text": "$500", "type": "amount", "confidence": 0.95, "start": 19, "end": 23, "context": "Acme Corp invoiced $500 on 2024-01-05."},
    {"text": "2024-01-05", "type": "date", "confidence": 0.96, "start": 27, "end": 37, "context": "Acme Corp invoiced $500 on 2024-01-05."}
  ],
  "structured_result": null,
  "input_tokens": 142,
  "ocr_text": null
}

​
Extracting from an image or PDF
Pass a base64-encoded photo, scan, or PDF through extra_body and the text is read before extraction, so receipts, invoices, IDs, and scanned forms work without a separate preprocessing step. A message is still required; use a short placeholder user message. The raw extracted text is returned as ocr_text.
cURL
Python
DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'

For a PDF, set document_mime_type to "application/pdf"; single-page and multi-page PDFs are both supported.
​
Structured (nested) extraction
Use a nested object, or an array of objects for repeated structures such as line items. The full result is returned in structured_result, keyed by property name.
Python
cURL
r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])

​
Classification keys
Some of the fields you want are not really extraction targets - they are decisions. “Is this account past due?” or “Is this an electric or gas meter?” have no verbatim span to pull; they require judging the text against a fixed set of options. The extraction model is tuned to copy spans out of the source, so it is a poor fit for these, and mixing them into an extraction call drags down accuracy for every key.
To handle these, mark the key as a classification key by constraining it to a fixed list of labels. Any key constrained this way is split out of the extraction call and routed to our classification model instead - a Constrained Decoding Model (CDM) purpose-built for categorical and boolean decisions, using constrained decoding over your labels with calibrated confidence scores. The rest of the request extracts as normal, and classified values are merged back into the same response so nothing changes on your side.
Each label has a name and, optionally, a rubric describing when that label applies. Rubrics meaningfully improve accuracy - prefer them over bare strings for anything non-obvious. An optional per-key description adds context about the decision.
To mark a key as a classification key in a response_format schema, constrain the property to a fixed set of choices in one of two ways:
enum - the values are the labels; an optional description becomes the shared rubric.
oneOf of const branches - each branch’s description is that label’s rubric (per-label rubrics).
Python
cURL
r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])

Alternatively, with the flat entities body, send {"is_delinquent": {"labels": [{"name": "yes", "rubric": "balance is overdue"}, ...]}}.
The classified value is returned as the entity text, and confidence is the calibrated probability of the chosen label. The label itself is usually not a verbatim span in the source (it was inferred), so start/end and context instead point at the evidence the model used for the decision - here, "90 days past due" for is_delinquent, not the word “delinquent”. If no relevant evidence is found, start/end fall back to 0 and context is empty. In a structured (nested) request, classified values also appear in structured_result under their key.
A classification key still counts as part of your single extract call - one request in, one response out, billed as one extract call. Each classification key needs at least 2 and at most 20 labels; outside that range the request returns 422.
To locate the evidence span, each classification key runs a brief follow-up pass that pulls the verbatim phrase backing the decision. This is transparent - the span and context are populated for you - but it does add to the token usage reported for the call. If you don’t need spans for a boolean/categorical field, you can ignore start/end/context on those entities.
​
Multiple matches, with limits
A scalar property returns each distinct value found in the text, one entity per value, in order of first appearance, up to 30 per entity type. A value that occurs several times is returned once (at its first occurrence). You do not need to ask for a list.
Python
r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Alice Johnson, Bob Martinez and Carol Nguyen flew from Paris to London."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "trip",
            "schema": {
                "type": "object",
                "properties": {
                    "person": {"type": "string", "description": "Full name of a person"},
                    "city": {"type": "string", "description": "Name of a city"},
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])

This returns three person entities (Alice Johnson, Bob Martinez, Carol Nguyen) and two city entities (Paris, London). Every entity has a confidence. Use threshold and top_n to filter on it. Set them for the whole request through extra_body, and override them per property with extra keywords on that property:
Python
r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Alice Johnson, Bob Martinez and Carol Nguyen flew from Paris to London."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "trip",
            "schema": {
                "type": "object",
                "properties": {
                    "person": {"type": "string", "description": "Full name of a person", "top_n": 1},
                    "city": {"type": "string", "description": "Name of a city"},
                },
            },
        },
    },
    extra_body={"threshold": 0.5},
)

Here person returns only its single most confident match, and every entity below 0.5 confidence is dropped. Per-property values override the request-level ones.
​
Writing good entity labels
The entity name and description are both used as part of the model’s search criteria - wording them well is the biggest lever you have on extraction quality.
Use lowercase or Title Case. The model was trained with lowercase labels. Keeping your entity names lowercase (e.g. person, company) or Title Case (e.g. Person, Company) produces better results than ALL_CAPS or other conventions.
Be specific with names, and test synonyms. The entity name itself influences what the model looks for. person and full name will find slightly different things. If results are missing or noisy, try rephrasing the name - person name, individual, or full name may all behave differently on your data.
Labels can be descriptive phrases, not just single words. Instead of city, use capital city and population center. The extra context helps the model distinguish between entity types that might otherwise overlap.
Descriptions can be full instructions. Rather than "Name of the person", write "Find the first and last name of the person mentioned in the text". Instruction-style descriptions consistently outperform short noun phrases on complex or ambiguous entities.
Avoid mixing overlapping granularities in the same call. If you include both location and city, the model has to decide which label to assign to a city - and will often split results unpredictably between them. Pick one level of granularity per concept.
Examples:
Instead of	Use
CITY	city or City
city + location in the same call	just city or just location
"Name"	"Find the first and last name of the person in the text"
"city" (when you want capitals specifically)	"capital city and population center"
​
Notes
GET /v1/models lists extract and extract-1. The bare name always points at the latest version; use extract-1 to pin.
Streaming is not supported; the full result is returned in one response.
Scalar properties return at most 30 distinct values each. Nested and array definitions are bounded at 200 items.
Results are grouped by entity type and returned in order of appearance in the text. top_n selects the most confident entities but does not reorder them.
Array properties are returned in structured_result as a plain list (strings or objects), not a list of lists. If a request contains any array or nested-object property, its scalar properties return a single value each; send them in a separate request (or declare them as arrays) to get every match.
threshold and top_n apply to extracted scalar entities only. A classification key always returns a single chosen label.
The context field is always derived from the original text input - it is not generated by the model.
Character offsets (start, end) refer to byte positions in the original text string.
There is no fixed limit on the number of entity types you can define in a single request.
Classification keys (any property constrained to a fixed set of choices) are routed to the classification model rather than extracted. Use them for boolean or categorical fields - keeping them out of the extraction path improves accuracy for both.
Overview
Overview
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

ADDITIONAL VISIBLE STATES / CHART VALUES
INTERACTIVE TAB PANEL TEXT
--- cURL [tab 0] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "company name"},
                    "amount": {"type": "string", "description": "dollar amount"},
                    "date": {"type": "string", "description": "invoice date"},
                },
            },
        },
    },
)
result = json.loads(r.choices[0].message.content)
print(result["entities"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "extract",
  messages: [{ role: "user", content: "Acme Corp invoiced $500 on 2024-01-05." }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "invoice",
      schema: {
        type: "object",
        properties: {
          vendor: { type: "string", description: "company name" },
          amount: { type: "string", description: "dollar amount" },
          date: { type: "string", description: "invoice date" },
        },
      },
    },
  },
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.entities);


DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'


import base64

with open("receipt.jpg", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Extract the receipt fields."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "schema": {
                "type": "object",
                "properties": {
                    "merchant": {"type": "string", "description": "store or merchant name"},
                    "total": {"type": "string", "description": "total amount paid"},
                },
            },
        },
    },
    extra_body={"document": document, "document_mime_type": "image/jpeg"},
)
print(json.loads(r.choices[0].message.content)["entities"])


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": {"type": "string", "description": "invoice number"},
            "line_items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "product": {"type": "string", "description": "product name"},
                  "quantity": {"type": "string", "description": "number of units"},
                  "unit_price": {"type": "string", "description": "price per unit"}
                }
              }
            }
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "account",
        "schema": {
          "type": "object",
          "properties": {
            "customer": {"type": "string", "description": "customer name"},
            "is_delinquent": {
              "oneOf": [
                {"const": "yes", "description": "balance is overdue"},
                {"const": "no", "description": "account is current"}
              ]
            },
            "meter_type": {
              "enum": ["electric", "gas", "water"],
              "description": "type of utility service"
            }
          }
        }
      }
    }
  }'


--- Python [tab 1] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "company name"},
                    "amount": {"type": "string", "description": "dollar amount"},
                    "date": {"type": "string", "description": "invoice date"},
                },
            },
        },
    },
)
result = json.loads(r.choices[0].message.content)
print(result["entities"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "extract",
  messages: [{ role: "user", content: "Acme Corp invoiced $500 on 2024-01-05." }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "invoice",
      schema: {
        type: "object",
        properties: {
          vendor: { type: "string", description: "company name" },
          amount: { type: "string", description: "dollar amount" },
          date: { type: "string", description: "invoice date" },
        },
      },
    },
  },
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.entities);


DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'


import base64

with open("receipt.jpg", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Extract the receipt fields."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "schema": {
                "type": "object",
                "properties": {
                    "merchant": {"type": "string", "description": "store or merchant name"},
                    "total": {"type": "string", "description": "total amount paid"},
                },
            },
        },
    },
    extra_body={"document": document, "document_mime_type": "image/jpeg"},
)
print(json.loads(r.choices[0].message.content)["entities"])


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": {"type": "string", "description": "invoice number"},
            "line_items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "product": {"type": "string", "description": "product name"},
                  "quantity": {"type": "string", "description": "number of units"},
                  "unit_price": {"type": "string", "description": "price per unit"}
                }
              }
            }
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "account",
        "schema": {
          "type": "object",
          "properties": {
            "customer": {"type": "string", "description": "customer name"},
            "is_delinquent": {
              "oneOf": [
                {"const": "yes", "description": "balance is overdue"},
                {"const": "no", "description": "account is current"}
              ]
            },
            "meter_type": {
              "enum": ["electric", "gas", "water"],
              "description": "type of utility service"
            }
          }
        }
      }
    }
  }'


--- TypeScript [tab 2] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "company name"},
                    "amount": {"type": "string", "description": "dollar amount"},
                    "date": {"type": "string", "description": "invoice date"},
                },
            },
        },
    },
)
result = json.loads(r.choices[0].message.content)
print(result["entities"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "extract",
  messages: [{ role: "user", content: "Acme Corp invoiced $500 on 2024-01-05." }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "invoice",
      schema: {
        type: "object",
        properties: {
          vendor: { type: "string", description: "company name" },
          amount: { type: "string", description: "dollar amount" },
          date: { type: "string", description: "invoice date" },
        },
      },
    },
  },
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.entities);


DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'


import base64

with open("receipt.jpg", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Extract the receipt fields."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "schema": {
                "type": "object",
                "properties": {
                    "merchant": {"type": "string", "description": "store or merchant name"},
                    "total": {"type": "string", "description": "total amount paid"},
                },
            },
        },
    },
    extra_body={"document": document, "document_mime_type": "image/jpeg"},
)
print(json.loads(r.choices[0].message.content)["entities"])


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": {"type": "string", "description": "invoice number"},
            "line_items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "product": {"type": "string", "description": "product name"},
                  "quantity": {"type": "string", "description": "number of units"},
                  "unit_price": {"type": "string", "description": "price per unit"}
                }
              }
            }
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "account",
        "schema": {
          "type": "object",
          "properties": {
            "customer": {"type": "string", "description": "customer name"},
            "is_delinquent": {
              "oneOf": [
                {"const": "yes", "description": "balance is overdue"},
                {"const": "no", "description": "account is current"}
              ]
            },
            "meter_type": {
              "enum": ["electric", "gas", "water"],
              "description": "type of utility service"
            }
          }
        }
      }
    }
  }'


--- cURL [tab 3] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "company name"},
                    "amount": {"type": "string", "description": "dollar amount"},
                    "date": {"type": "string", "description": "invoice date"},
                },
            },
        },
    },
)
result = json.loads(r.choices[0].message.content)
print(result["entities"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "extract",
  messages: [{ role: "user", content: "Acme Corp invoiced $500 on 2024-01-05." }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "invoice",
      schema: {
        type: "object",
        properties: {
          vendor: { type: "string", description: "company name" },
          amount: { type: "string", description: "dollar amount" },
          date: { type: "string", description: "invoice date" },
        },
      },
    },
  },
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.entities);


DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'


import base64

with open("receipt.jpg", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Extract the receipt fields."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "schema": {
                "type": "object",
                "properties": {
                    "merchant": {"type": "string", "description": "store or merchant name"},
                    "total": {"type": "string", "description": "total amount paid"},
                },
            },
        },
    },
    extra_body={"document": document, "document_mime_type": "image/jpeg"},
)
print(json.loads(r.choices[0].message.content)["entities"])


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": {"type": "string", "description": "invoice number"},
            "line_items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "product": {"type": "string", "description": "product name"},
                  "quantity": {"type": "string", "description": "number of units"},
                  "unit_price": {"type": "string", "description": "price per unit"}
                }
              }
            }
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "account",
        "schema": {
          "type": "object",
          "properties": {
            "customer": {"type": "string", "description": "customer name"},
            "is_delinquent": {
              "oneOf": [
                {"const": "yes", "description": "balance is overdue"},
                {"const": "no", "description": "account is current"}
              ]
            },
            "meter_type": {
              "enum": ["electric", "gas", "water"],
              "description": "type of utility service"
            }
          }
        }
      }
    }
  }'


--- Python [tab 4] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "company name"},
                    "amount": {"type": "string", "description": "dollar amount"},
                    "date": {"type": "string", "description": "invoice date"},
                },
            },
        },
    },
)
result = json.loads(r.choices[0].message.content)
print(result["entities"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "extract",
  messages: [{ role: "user", content: "Acme Corp invoiced $500 on 2024-01-05." }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "invoice",
      schema: {
        type: "object",
        properties: {
          vendor: { type: "string", description: "company name" },
          amount: { type: "string", description: "dollar amount" },
          date: { type: "string", description: "invoice date" },
        },
      },
    },
  },
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.entities);


DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'


import base64

with open("receipt.jpg", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Extract the receipt fields."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "schema": {
                "type": "object",
                "properties": {
                    "merchant": {"type": "string", "description": "store or merchant name"},
                    "total": {"type": "string", "description": "total amount paid"},
                },
            },
        },
    },
    extra_body={"document": document, "document_mime_type": "image/jpeg"},
)
print(json.loads(r.choices[0].message.content)["entities"])


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": {"type": "string", "description": "invoice number"},
            "line_items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "product": {"type": "string", "description": "product name"},
                  "quantity": {"type": "string", "description": "number of units"},
                  "unit_price": {"type": "string", "description": "price per unit"}
                }
              }
            }
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "account",
        "schema": {
          "type": "object",
          "properties": {
            "customer": {"type": "string", "description": "customer name"},
            "is_delinquent": {
              "oneOf": [
                {"const": "yes", "description": "balance is overdue"},
                {"const": "no", "description": "account is current"}
              ]
            },
            "meter_type": {
              "enum": ["electric", "gas", "water"],
              "description": "type of utility service"
            }
          }
        }
      }
    }
  }'


--- Python [tab 5] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "company name"},
                    "amount": {"type": "string", "description": "dollar amount"},
                    "date": {"type": "string", "description": "invoice date"},
                },
            },
        },
    },
)
result = json.loads(r.choices[0].message.content)
print(result["entities"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "extract",
  messages: [{ role: "user", content: "Acme Corp invoiced $500 on 2024-01-05." }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "invoice",
      schema: {
        type: "object",
        properties: {
          vendor: { type: "string", description: "company name" },
          amount: { type: "string", description: "dollar amount" },
          date: { type: "string", description: "invoice date" },
        },
      },
    },
  },
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.entities);


DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'


import base64

with open("receipt.jpg", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Extract the receipt fields."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "schema": {
                "type": "object",
                "properties": {
                    "merchant": {"type": "string", "description": "store or merchant name"},
                    "total": {"type": "string", "description": "total amount paid"},
                },
            },
        },
    },
    extra_body={"document": document, "document_mime_type": "image/jpeg"},
)
print(json.loads(r.choices[0].message.content)["entities"])


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": {"type": "string", "description": "invoice number"},
            "line_items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "product": {"type": "string", "description": "product name"},
                  "quantity": {"type": "string", "description": "number of units"},
                  "unit_price": {"type": "string", "description": "price per unit"}
                }
              }
            }
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "account",
        "schema": {
          "type": "object",
          "properties": {
            "customer": {"type": "string", "description": "customer name"},
            "is_delinquent": {
              "oneOf": [
                {"const": "yes", "description": "balance is overdue"},
                {"const": "no", "description": "account is current"}
              ]
            },
            "meter_type": {
              "enum": ["electric", "gas", "water"],
              "description": "type of utility service"
            }
          }
        }
      }
    }
  }'


--- cURL [tab 6] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "company name"},
                    "amount": {"type": "string", "description": "dollar amount"},
                    "date": {"type": "string", "description": "invoice date"},
                },
            },
        },
    },
)
result = json.loads(r.choices[0].message.content)
print(result["entities"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "extract",
  messages: [{ role: "user", content: "Acme Corp invoiced $500 on 2024-01-05." }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "invoice",
      schema: {
        type: "object",
        properties: {
          vendor: { type: "string", description: "company name" },
          amount: { type: "string", description: "dollar amount" },
          date: { type: "string", description: "invoice date" },
        },
      },
    },
  },
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.entities);


DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'


import base64

with open("receipt.jpg", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Extract the receipt fields."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "schema": {
                "type": "object",
                "properties": {
                    "merchant": {"type": "string", "description": "store or merchant name"},
                    "total": {"type": "string", "description": "total amount paid"},
                },
            },
        },
    },
    extra_body={"document": document, "document_mime_type": "image/jpeg"},
)
print(json.loads(r.choices[0].message.content)["entities"])


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": {"type": "string", "description": "invoice number"},
            "line_items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "product": {"type": "string", "description": "product name"},
                  "quantity": {"type": "string", "description": "number of units"},
                  "unit_price": {"type": "string", "description": "price per unit"}
                }
              }
            }
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "account",
        "schema": {
          "type": "object",
          "properties": {
            "customer": {"type": "string", "description": "customer name"},
            "is_delinquent": {
              "oneOf": [
                {"const": "yes", "description": "balance is overdue"},
                {"const": "no", "description": "account is current"}
              ]
            },
            "meter_type": {
              "enum": ["electric", "gas", "water"],
              "description": "type of utility service"
            }
          }
        }
      }
    }
  }'


--- Python [tab 7] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "company name"},
                    "amount": {"type": "string", "description": "dollar amount"},
                    "date": {"type": "string", "description": "invoice date"},
                },
            },
        },
    },
)
result = json.loads(r.choices[0].message.content)
print(result["entities"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "extract",
  messages: [{ role: "user", content: "Acme Corp invoiced $500 on 2024-01-05." }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "invoice",
      schema: {
        type: "object",
        properties: {
          vendor: { type: "string", description: "company name" },
          amount: { type: "string", description: "dollar amount" },
          date: { type: "string", description: "invoice date" },
        },
      },
    },
  },
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.entities);


DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'


import base64

with open("receipt.jpg", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Extract the receipt fields."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "schema": {
                "type": "object",
                "properties": {
                    "merchant": {"type": "string", "description": "store or merchant name"},
                    "total": {"type": "string", "description": "total amount paid"},
                },
            },
        },
    },
    extra_body={"document": document, "document_mime_type": "image/jpeg"},
)
print(json.loads(r.choices[0].message.content)["entities"])


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": {"type": "string", "description": "invoice number"},
            "line_items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "product": {"type": "string", "description": "product name"},
                  "quantity": {"type": "string", "description": "number of units"},
                  "unit_price": {"type": "string", "description": "price per unit"}
                }
              }
            }
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "account",
        "schema": {
          "type": "object",
          "properties": {
            "customer": {"type": "string", "description": "customer name"},
            "is_delinquent": {
              "oneOf": [
                {"const": "yes", "description": "balance is overdue"},
                {"const": "no", "description": "account is current"}
              ]
            },
            "meter_type": {
              "enum": ["electric", "gas", "water"],
              "description": "type of utility service"
            }
          }
        }
      }
    }
  }'


--- cURL [tab 8] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [
      {"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "vendor": {"type": "string", "description": "company name"},
            "amount": {"type": "string", "description": "dollar amount"},
            "date":   {"type": "string", "description": "invoice date"}
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Acme Corp invoiced $500 on 2024-01-05."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "company name"},
                    "amount": {"type": "string", "description": "dollar amount"},
                    "date": {"type": "string", "description": "invoice date"},
                },
            },
        },
    },
)
result = json.loads(r.choices[0].message.content)
print(result["entities"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "extract",
  messages: [{ role: "user", content: "Acme Corp invoiced $500 on 2024-01-05." }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "invoice",
      schema: {
        type: "object",
        properties: {
          vendor: { type: "string", description: "company name" },
          amount: { type: "string", description: "dollar amount" },
          date: { type: "string", description: "invoice date" },
        },
      },
    },
  },
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.entities);


DOCUMENT=$(base64 -b 0 -i receipt.jpg)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Extract the receipt fields."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "receipt",
        "schema": {
          "type": "object",
          "properties": {
            "merchant": {"type": "string", "description": "store or merchant name"},
            "total": {"type": "string", "description": "total amount paid"}
          }
        }
      }
    },
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "image/jpeg"
  }'


import base64

with open("receipt.jpg", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Extract the receipt fields."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "schema": {
                "type": "object",
                "properties": {
                    "merchant": {"type": "string", "description": "store or merchant name"},
                    "total": {"type": "string", "description": "total amount paid"},
                },
            },
        },
    },
    extra_body={"document": document, "document_mime_type": "image/jpeg"},
)
print(json.loads(r.choices[0].message.content)["entities"])


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "invoice",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_number": {"type": "string", "description": "invoice number"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product": {"type": "string", "description": "product name"},
                                "quantity": {"type": "string", "description": "number of units"},
                                "unit_price": {"type": "string", "description": "price per unit"},
                            },
                        },
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["structured_result"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Invoice 1042 from Acme Corp. 2 x Widget at $10.00, 1 x Gadget at $25.00."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": {"type": "string", "description": "invoice number"},
            "line_items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "product": {"type": "string", "description": "product name"},
                  "quantity": {"type": "string", "description": "number of units"},
                  "unit_price": {"type": "string", "description": "price per unit"}
                }
              }
            }
          }
        }
      }
    }
  }'


r = client.chat.completions.create(
    model="extract",
    messages=[{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "account",
            "schema": {
                "type": "object",
                "properties": {
                    "customer": {"type": "string", "description": "customer name"},
                    "is_delinquent": {
                        "oneOf": [
                            {"const": "yes", "description": "balance is overdue"},
                            {"const": "no", "description": "account is current"},
                        ]
                    },
                    "meter_type": {
                        "enum": ["electric", "gas", "water"],
                        "description": "type of utility service",
                    },
                },
            },
        },
    },
)
print(json.loads(r.choices[0].message.content)["entities"])


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "extract",
    "messages": [{"role": "user", "content": "Account for Jane Doe. Balance is 90 days past due. Service: natural gas line."}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "account",
        "schema": {
          "type": "object",
          "properties": {
            "customer": {"type": "string", "description": "customer name"},
            "is_delinquent": {
              "oneOf": [
                {"const": "yes", "description": "balance is overdue"},
                {"const": "no", "description": "account is current"}
              ]
            },
            "meter_type": {
              "enum": ["electric", "gas", "water"],
              "description": "type of utility service"
            }
          }
        }
      }
    }
  }'

---8<--- page: docs-scaledown-ai-api-reference-openapi-json ---8<---

Page URL: https://docs.scaledown.ai/api-reference/openapi.json
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
{
  "openapi": "3.1.0",
  "info": {
    "title": "ScaleDown API",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://api.scaledown.xyz"
    }
  ],
  "security": [
    {
      "apiKey": []
    }
  ],
  "components": {
    "securitySchemes": {
      "apiKey": {
        "type": "apiKey",
        "in": "header",
        "name": "x-api-key"
      }
    }
  },
  "paths": {
    "/compress/raw/": {
      "post": {
        "summary": "Compress",
        "description": "Compress a prompt and context to reduce token usage while preserving semantic meaning.",
        "operationId": "compress",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": ["context", "prompt", "scaledown"],
                "properties": {
                  "context": {
                    "type": "string",
                    "description": "Background information, instructions, or supporting text that provides context for the prompt."
                  },
                  "prompt": {
                    "type": "string",
                    "description": "The main query or question to send to your AI model."
                  },
                  "scaledown": {
                    "type": "object",
                    "required": ["rate"],
                    "properties": {
                      "rate": {
                        "type": "string",
                        "description": "Compression aggressiveness. Use 'auto' or a number between 0 and 1 for the fraction of tokens to remove (e.g. 0.8 removes about 80% and keeps about 20%)."
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful compression",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "results": {
                      "type": "object",
                      "properties": {
                        "success": { "type": "boolean" },
                        "compressed_prompt": { "type": "string", "description": "The compressed context." },
                        "original_prompt": { "type": "string", "description": "The prompt, unchanged." },
                        "original_prompt_tokens": { "type": "number" },
                        "compressed_prompt_tokens": { "type": "number" },
                        "compression_ratio": { "type": "number" }
                      }
                    },
                    "model_used": { "type": "string" },
                    "input_tokens": { "type": "number" },
                    "total_original_tokens": { "type": "number" },
                    "total_compressed_tokens": { "type": "number" },
                    "num_pairs_processed": { "type": "number" },
                    "num_successful": { "type": "number" },
                    "num_failed": { "type": "number" },
                    "successful": { "type": "boolean" },
                    "partially_successful": { "type": "boolean" },
                    "latency_ms": { "type": "number" },
                    "request_metadata": {
                      "type": "object",
                      "properties": {
                        "compression_time_ms": { "type": "number" },
                        "compression_rate": {
                          "oneOf": [
                            { "type": "string" },
                            { "type": "number" }
                          ]
                        },
                        "average_compression_ratio": { "type": "number" }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": { "description": "Malformed request body or missing required fields." },
          "401": { "description": "Missing or invalid x-api-key." },
          "429": { "description": "Rate limit exceeded." },
          "500": { "description": "Compression service unavailable." }
        }
      }
    },
    "/classify": {
      "post": {
        "summary": "Classify",
        "description": "Score text against a set of user-defined labels and return a softmax-normalised probability distribution.",
        "operationId": "classify",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": ["text", "labels"],
                "properties": {
                  "text": {
                    "type": "string",
                    "description": "The text to classify."
                  },
                  "labels": {
                    "type": "array",
                    "description": "One or more label definitions. Must contain at least one item.",
                    "items": {
                      "type": "object",
                      "required": ["name", "rubric"],
                      "properties": {
                        "name": {
                          "type": "string",
                          "description": "Short identifier for the label (e.g. \"medical\", \"billing\"). Used as the key in the scores response object."
                        },
                        "rubric": {
                          "type": "string",
                          "description": "A yes/no question the model uses to score the label. Phrased so that a \"yes\" answer means the label applies."
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful classification",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "top_label": {
                      "type": "string",
                      "description": "Name of the highest-scoring label."
                    },
                    "scores": {
                      "type": "object",
                      "description": "Map of label name to probability score. All values sum to 1.0.",
                      "additionalProperties": { "type": "number" }
                    },
                    "labels": {
                      "type": "array",
                      "description": "Full label list with name, score, and rubric, in the same order as the request.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "label": { "type": "string" },
                          "score": { "type": "number" },
                          "rubric": { "type": "string" }
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "422": { "description": "Malformed request body or empty labels array." },
          "502": { "description": "Model service unavailable or returned an error." }
        }
      }
    },
    "/v1/scaledown": {
      "post": {
        "summary": "Decisions",
        "description": "Jev (TypeSafe)-compatible endpoint: answer typed choice/noul/score questions about a shared state object.",
        "operationId": "decisions",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": ["state", "questions"],
                "properties": {
                  "model": {
                    "type": "string",
                    "enum": ["classify-1"],
                    "default": "classify-1",
                    "description": "Optional. \"classify-1\" is the only supported value and also the default when omitted. Any other value returns 422."
                  },
                  "state": {
                    "description": "The item being decided on. A plain string is shorthand for {\"text\": \"...\"}.",
                    "oneOf": [
                      { "type": "string" },
                      {
                        "type": "object",
                        "description": "The item being decided on. Provide text, document, or both.",
                        "properties": {
                          "text": {
                            "type": "string",
                            "description": "The text to evaluate every question against."
                          },
                          "document": {
                            "type": "string",
                            "description": "A base64-encoded file to evaluate (image or PDF). Non-standard extension, not part of the Jev API."
                          },
                          "document_mime_type": {
                            "type": "string",
                            "description": "MIME type of document. Required when document is provided."
                          }
                        }
                      }
                    ]
                  },
                  "questions": {
                    "type": "object",
                    "description": "Map of question name to question definition. Must contain at least one entry.",
                    "additionalProperties": {
                      "type": "object",
                      "required": ["type"],
                      "properties": {
                        "type": {
                          "type": "string",
                          "enum": ["choice", "noul", "score"],
                          "description": "choice: pick one mutually-exclusive option from criteria. noul: independent yes/no question. score: an ordered-scale question, answered as a position on the scale."
                        },
                        "instructions": {
                          "type": "string",
                          "description": "Optional guidance for how to answer the question."
                        },
                        "criteria": {
                          "description": "Required for choice questions: object mapping option key to description (at least one entry). Required for score questions: ORDERED array of 2-10 level descriptions, lowest to highest (level index = array position). Ignored for noul questions.",
                          "oneOf": [
                            {
                              "type": "object",
                              "additionalProperties": { "type": "string" }
                            },
                            {
                              "type": "array",
                              "items": { "type": "string" },
                              "minItems": 2,
                              "maxItems": 10
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful decision",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "model": {
                      "type": "string",
                      "description": "Always \"classify-1\"."
                    },
                    "answers": {
                      "type": "object",
                      "description": "Map of question name to typed answer, matching the questions keys from the request.",
                      "additionalProperties": {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "enum": ["choice", "noul", "score"]
                          },
                          "choice": {
                            "type": "string",
                            "description": "choice answers only: the chosen option key."
                          },
                          "probabilities": {
                            "type": "object",
                            "description": "choice/score answers only: map of option key (choice) or level index as a string (score) to probability. Sums to 1.0.",
                            "additionalProperties": { "type": "number" }
                          },
                          "confidence": {
                            "type": "number",
                            "description": "choice/score answers only: the chosen option's, or top level's, probability."
                          },
                          "noul": {
                            "type": "number",
                            "description": "noul answers only: P(yes), 0 to 1."
                          },
                          "score": {
                            "type": "number",
                            "description": "score answers only: probability-weighted expected value across level indices (sum of level_index * probability). A continuous position on the scale, not necessarily a whole level."
                          },
                          "legend": {
                            "type": "object",
                            "description": "score answers only: map of level index (as a string) to its criteria description, echoing the request's criteria back for display.",
                            "additionalProperties": { "type": "string" }
                          }
                        }
                      }
                    },
                    "usage": {
                      "type": "object",
                      "description": "Token usage and cost, summed across every internal call the request fanned out to.",
                      "properties": {
                        "input_tokens": { "type": "integer" },
                        "output_tokens": { "type": "integer" },
                        "cost": { "type": "number" }
                      }
                    }
                  }
                }
              }
            }
          },
          "402": { "description": "Insufficient credits." },
          "422": { "description": "Malformed request body, empty questions map, empty criteria on a choice question, a score question's criteria outside the 2-10 item range, neither state.text nor state.document provided, an unsupported model value, or the document could not be read." },
          "502": { "description": "Model service unavailable or returned an error." },
          "504": { "description": "Request timed out." }
        }
      }
    }
  }
}

---8<--- page: docs-scaledown-ai-api-reference-summarize-overview ---8<---

Page URL: https://docs.scaledown.ai/api-reference/summarize-overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Compress
Overview
POST
Compress
On this page
What it does
When to use it
Common use cases
How it fits into your workflow
Abstractive vs. extractive summarization
Summarize
Overview
Copy page

Generate fluent, faithful summaries of long text.

​
What it does
The summarize model, called through the OpenAI-compatible POST /v1/chat/completions endpoint, condenses text into a shorter, fluent rewrite in the model’s own words. Unlike extractive summarization - which lifts sentences directly from the source - abstractive summarization produces a coherent output that captures the key information without being constrained to the original phrasing.
​
When to use it
You need to condense long documents for humans or downstream models. Summaries reduce reading time for human reviewers and reduce token costs when passing document content to another model.
You need format or focus control. A system message lets you specify bullet points, a particular language, a word limit, or a topical focus - without overriding the core faithful-summary behaviour.
You want consistent, low-noise outputs. Sampling parameters (temperature, top-p) are fixed to a configuration tuned for faithful summarization. You get stable, predictable outputs rather than creative or hallucinated ones.
​
Common use cases
Use case	Example
Document review	Summarize legal contracts, research papers, or policy documents
News digests	Condense articles to one-paragraph or bullet-point briefs
Customer feedback	Summarize support tickets, reviews, or survey responses at scale
Meeting transcripts	Generate action-item-focused summaries from call recordings
Financial reporting	Extract key figures and decisions from earnings calls or filings
Content pipelines	Pre-process long articles before passing them to downstream models
RAG pre-processing	Summarize retrieved chunks to reduce token overhead before model calls
​
How it fits into your workflow
Summarize works as a standalone step that can sit anywhere documents are consumed - before storing, before displaying, or before passing to another model.
[Ingest document] → [POST /v1/chat/completions, model "summarize"] → [Summary] → [Store / display / pass to model]

The response includes input_chars and output_chars so you can track compression ratios across your pipeline, and latency_ms for performance monitoring.
​
Abstractive vs. extractive summarization
	Extractive	Abstractive (this endpoint)
How it works	Selects and stitches existing sentences	Rewrites content in the model’s own words
Output quality	Can feel disjointed	Fluent and coherent
Faithfulness	Directly tied to source	Validated - rejects off-task outputs
Flexibility	Limited	Controllable via a system message
Summarize
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-api-reference-summarize ---8<---

Page URL: https://docs.scaledown.ai/api-reference/summarize
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Summarize
Overview
Summarize
Extract
Overview
Extract
Classify
Overview
Custom ScaleDown API
Decisions API (Jev-compatible)
Compress
Overview
POST
Compress
On this page
Overview
Request
Response
Error responses
Authentication
Examples
Basic summary
With instructions
Summarizing a document
Notes
Summarize
Summarize
Copy page

Produce an abstractive summary of a block of text through the OpenAI-compatible chat completions API.

​
Overview
Summarize is called through the OpenAI-compatible POST /v1/chat/completions endpoint. Set model to summarize (latest) or summarize-1 (pinned version) and send the text as the last user message. The model condenses it in its own words without adding new information or commentary. Unlike extractive summarization, the output is a fluent rewrite - not a selection of lifted sentences.
Because the endpoint is OpenAI-compatible, you can point an unmodified OpenAI or OpenRouter SDK at ScaleDown by changing only the base URL and API key.
POST https://api.scaledown.xyz/v1/chat/completions

​
Request
​
model
stringrequired
"summarize" (always the latest version) or "summarize-1" (pinned to version 1). Both currently behave identically.
​
messages
arrayrequired
Standard OpenAI chat messages. The last user message is the text to summarize. Any system messages are joined and used as the summary instructions.
​
max_tokens
numberdefault:1000
Standard OpenAI field. Maximum number of tokens in the generated summary. Defaults to 1000, which is also the maximum: larger values are capped at 1000, and the model is instructed to finish within the limit. If a summary still hits the limit it is cut off and the parsed result sets finish_reason to "length" with a notice. For a higher output limit, email neal@scaledown.ai.
​
document
string
Non-standard extension, passed with the SDK’s extra_body. A base64-encoded file to summarize. Supported formats: JPEG, PNG, TIFF, single-page PDF, multi-page PDF. The text is read from the file and used as input.
​
document_mime_type
string
Non-standard extension, passed with extra_body. MIME type of the document (e.g. "image/jpeg", "application/pdf"). Required when document is provided.
​
text
string
Optional top-level override for the input text. When present it takes precedence over the last user message - this lets a batch item body be reused verbatim. Likewise a top-level instructions string takes precedence over system messages.
Temperature, top-p, and other sampling parameters are fixed and not configurable.
​
Response
A standard chat.completion. The summary result is a JSON string in choices[0].message.content - parse it to read the fields below.
​
model
string
Echoes the model you sent (summarize or summarize-1).
​
usage
object
prompt_tokens is the input tokens billed for the request, completion_tokens the model’s output tokens, and total_tokens their sum.
​
choices[0].message.content
string
A JSON string with these fields:

Show Parsed content

​
Error responses
Status	Meaning
400 Bad Request	No input text (no user message, text, or document).
402 Payment Required	Insufficient credits.
422 Unprocessable Entity	Malformed request body or the document could not be read.
500 Internal Server Error	Inference service unavailable.
504 Gateway Timeout	Summarization request timed out.
​
Authentication
Include your API key in every request using the x-api-key header. Authorization: Bearer <your-api-key> is also accepted, so an OpenAI SDK only needs its api_key set.
-H "x-api-key: <your-api-key>"

​
Examples
​
Basic summary
cURL
Python
TypeScript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [{ role: "user", content: "Your long text here..." }],
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.summary);

Response:
{
  "id": "chatcmpl-9f2c1e0a7b3d4c5e8a6b1d2f3e4a5b6c",
  "object": "chat.completion",
  "created": 1760000000,
  "model": "summarize",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "{\"summary\":\"The company reported strong Q3 results, approved a share buyback program, and announced plans for Southeast Asian expansion.\",\"input_chars\":8340,\"output_chars\":142,\"latency_ms\":3241,\"input_tokens\":2105,\"finish_reason\":\"stop\",\"notice\":null}"
    },
    "finish_reason": "stop"
  }],
  "usage": { "prompt_tokens": 2105, "completion_tokens": 38, "total_tokens": 2143 }
}

​
With instructions
Put format, language, focus area, or length guidance in a system message. It extends, and does not replace, the default behaviour (no new information, no commentary).
cURL
Python
TypeScript
const r = await client.chat.completions.create({
  model: "summarize-1",
  max_tokens: 150,
  messages: [
    { role: "system", content: "Use bullet points. Focus on dates and key decisions only." },
    { role: "user", content: "Your long text here..." },
  ],
});
console.log(JSON.parse(r.choices[0].message.content!).summary);

The parsed content is:
{
  "summary": "- The company reported Q3 revenue of $4.2B, up 12% year-over-year.\n- The board approved a $500M share buyback program on October 14.\n- CEO announced plans to expand into Southeast Asia by mid-2027.",
  "input_chars": 8340,
  "output_chars": 198,
  "latency_ms": 3241,
  "input_tokens": 2105,
  "finish_reason": "stop",
  "notice": null
}

​
Summarizing a document
Pass a base64-encoded image or PDF through extra_body (extra_body fields are merged into the top level of the request). The text is extracted automatically and summarized, and the raw extracted text is returned as ocr_text. A message is still required; use a short placeholder user message.
cURL
Python
TypeScript
import fs from "fs";

const document = fs.readFileSync("report.pdf").toString("base64");

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [
    { role: "system", content: "Use bullet points. Focus on key figures and decisions only." },
    { role: "user", content: "Summarize the attached document." },
  ],
  // @ts-expect-error ScaleDown extension fields
  document,
  document_mime_type: "application/pdf",
});
console.log(JSON.parse(r.choices[0].message.content!).summary);

​
Notes
The base instructions (no new information, no commentary) are always applied. System messages add on top of them - they do not replace them.
GET /v1/models lists summarize and summarize-1. The bare name always points at the latest version; use summarize-1 to pin.
Streaming is not supported; the full result is returned in one response.
Overview
Overview
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

ADDITIONAL VISIBLE STATES / CHART VALUES
INTERACTIVE TAB PANEL TEXT
--- cURL [tab 0] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


import json
from openai import OpenAI

client = OpenAI(
    base_url="https://api.scaledown.xyz/v1",
    api_key="<your-api-key>",
)

r = client.chat.completions.create(
    model="summarize",
    messages=[{"role": "user", "content": "Your long text here..."}],
)
print(json.loads(r.choices[0].message.content)["summary"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [{ role: "user", content: "Your long text here..." }],
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.summary);


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize-1",
    "max_tokens": 150,
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


r = client.chat.completions.create(
    model="summarize-1",
    max_tokens=150,
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
        {"role": "user", "content": "Your long text here..."},
    ],
)
print(json.loads(r.choices[0].message.content)["summary"])


const r = await client.chat.completions.create({
  model: "summarize-1",
  max_tokens: 150,
  messages: [
    { role: "system", content: "Use bullet points. Focus on dates and key decisions only." },
    { role: "user", content: "Your long text here..." },
  ],
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


DOCUMENT=$(base64 -b 0 -i report.pdf)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
      {"role": "user", "content": "Summarize the attached document."}
    ],
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf"
  }'


import base64

with open("report.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="summarize",
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
        {"role": "user", "content": "Summarize the attached document."},
    ],
    extra_body={"document": document, "document_mime_type": "application/pdf"},
)
print(json.loads(r.choices[0].message.content)["summary"])


import fs from "fs";

const document = fs.readFileSync("report.pdf").toString("base64");

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [
    { role: "system", content: "Use bullet points. Focus on key figures and decisions only." },
    { role: "user", content: "Summarize the attached document." },
  ],
  // @ts-expect-error ScaleDown extension fields
  document,
  document_mime_type: "application/pdf",
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


--- Python [tab 1] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


import json
from openai import OpenAI

client = OpenAI(
    base_url="https://api.scaledown.xyz/v1",
    api_key="<your-api-key>",
)

r = client.chat.completions.create(
    model="summarize",
    messages=[{"role": "user", "content": "Your long text here..."}],
)
print(json.loads(r.choices[0].message.content)["summary"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [{ role: "user", content: "Your long text here..." }],
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.summary);


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize-1",
    "max_tokens": 150,
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


r = client.chat.completions.create(
    model="summarize-1",
    max_tokens=150,
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
        {"role": "user", "content": "Your long text here..."},
    ],
)
print(json.loads(r.choices[0].message.content)["summary"])


const r = await client.chat.completions.create({
  model: "summarize-1",
  max_tokens: 150,
  messages: [
    { role: "system", content: "Use bullet points. Focus on dates and key decisions only." },
    { role: "user", content: "Your long text here..." },
  ],
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


DOCUMENT=$(base64 -b 0 -i report.pdf)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
      {"role": "user", "content": "Summarize the attached document."}
    ],
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf"
  }'


import base64

with open("report.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="summarize",
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
        {"role": "user", "content": "Summarize the attached document."},
    ],
    extra_body={"document": document, "document_mime_type": "application/pdf"},
)
print(json.loads(r.choices[0].message.content)["summary"])


import fs from "fs";

const document = fs.readFileSync("report.pdf").toString("base64");

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [
    { role: "system", content: "Use bullet points. Focus on key figures and decisions only." },
    { role: "user", content: "Summarize the attached document." },
  ],
  // @ts-expect-error ScaleDown extension fields
  document,
  document_mime_type: "application/pdf",
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


--- cURL [tab 3] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


import json
from openai import OpenAI

client = OpenAI(
    base_url="https://api.scaledown.xyz/v1",
    api_key="<your-api-key>",
)

r = client.chat.completions.create(
    model="summarize",
    messages=[{"role": "user", "content": "Your long text here..."}],
)
print(json.loads(r.choices[0].message.content)["summary"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [{ role: "user", content: "Your long text here..." }],
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.summary);


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize-1",
    "max_tokens": 150,
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


r = client.chat.completions.create(
    model="summarize-1",
    max_tokens=150,
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
        {"role": "user", "content": "Your long text here..."},
    ],
)
print(json.loads(r.choices[0].message.content)["summary"])


const r = await client.chat.completions.create({
  model: "summarize-1",
  max_tokens: 150,
  messages: [
    { role: "system", content: "Use bullet points. Focus on dates and key decisions only." },
    { role: "user", content: "Your long text here..." },
  ],
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


DOCUMENT=$(base64 -b 0 -i report.pdf)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
      {"role": "user", "content": "Summarize the attached document."}
    ],
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf"
  }'


import base64

with open("report.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="summarize",
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
        {"role": "user", "content": "Summarize the attached document."},
    ],
    extra_body={"document": document, "document_mime_type": "application/pdf"},
)
print(json.loads(r.choices[0].message.content)["summary"])


import fs from "fs";

const document = fs.readFileSync("report.pdf").toString("base64");

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [
    { role: "system", content: "Use bullet points. Focus on key figures and decisions only." },
    { role: "user", content: "Summarize the attached document." },
  ],
  // @ts-expect-error ScaleDown extension fields
  document,
  document_mime_type: "application/pdf",
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


--- Python [tab 4] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


import json
from openai import OpenAI

client = OpenAI(
    base_url="https://api.scaledown.xyz/v1",
    api_key="<your-api-key>",
)

r = client.chat.completions.create(
    model="summarize",
    messages=[{"role": "user", "content": "Your long text here..."}],
)
print(json.loads(r.choices[0].message.content)["summary"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [{ role: "user", content: "Your long text here..." }],
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.summary);


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize-1",
    "max_tokens": 150,
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


r = client.chat.completions.create(
    model="summarize-1",
    max_tokens=150,
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
        {"role": "user", "content": "Your long text here..."},
    ],
)
print(json.loads(r.choices[0].message.content)["summary"])


const r = await client.chat.completions.create({
  model: "summarize-1",
  max_tokens: 150,
  messages: [
    { role: "system", content: "Use bullet points. Focus on dates and key decisions only." },
    { role: "user", content: "Your long text here..." },
  ],
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


DOCUMENT=$(base64 -b 0 -i report.pdf)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
      {"role": "user", "content": "Summarize the attached document."}
    ],
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf"
  }'


import base64

with open("report.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="summarize",
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
        {"role": "user", "content": "Summarize the attached document."},
    ],
    extra_body={"document": document, "document_mime_type": "application/pdf"},
)
print(json.loads(r.choices[0].message.content)["summary"])


import fs from "fs";

const document = fs.readFileSync("report.pdf").toString("base64");

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [
    { role: "system", content: "Use bullet points. Focus on key figures and decisions only." },
    { role: "user", content: "Summarize the attached document." },
  ],
  // @ts-expect-error ScaleDown extension fields
  document,
  document_mime_type: "application/pdf",
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


--- cURL [tab 6] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


import json
from openai import OpenAI

client = OpenAI(
    base_url="https://api.scaledown.xyz/v1",
    api_key="<your-api-key>",
)

r = client.chat.completions.create(
    model="summarize",
    messages=[{"role": "user", "content": "Your long text here..."}],
)
print(json.loads(r.choices[0].message.content)["summary"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [{ role: "user", content: "Your long text here..." }],
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.summary);


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize-1",
    "max_tokens": 150,
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


r = client.chat.completions.create(
    model="summarize-1",
    max_tokens=150,
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
        {"role": "user", "content": "Your long text here..."},
    ],
)
print(json.loads(r.choices[0].message.content)["summary"])


const r = await client.chat.completions.create({
  model: "summarize-1",
  max_tokens: 150,
  messages: [
    { role: "system", content: "Use bullet points. Focus on dates and key decisions only." },
    { role: "user", content: "Your long text here..." },
  ],
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


DOCUMENT=$(base64 -b 0 -i report.pdf)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
      {"role": "user", "content": "Summarize the attached document."}
    ],
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf"
  }'


import base64

with open("report.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="summarize",
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
        {"role": "user", "content": "Summarize the attached document."},
    ],
    extra_body={"document": document, "document_mime_type": "application/pdf"},
)
print(json.loads(r.choices[0].message.content)["summary"])


import fs from "fs";

const document = fs.readFileSync("report.pdf").toString("base64");

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [
    { role: "system", content: "Use bullet points. Focus on key figures and decisions only." },
    { role: "user", content: "Summarize the attached document." },
  ],
  // @ts-expect-error ScaleDown extension fields
  document,
  document_mime_type: "application/pdf",
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


--- Python [tab 7] ---
curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


import json
from openai import OpenAI

client = OpenAI(
    base_url="https://api.scaledown.xyz/v1",
    api_key="<your-api-key>",
)

r = client.chat.completions.create(
    model="summarize",
    messages=[{"role": "user", "content": "Your long text here..."}],
)
print(json.loads(r.choices[0].message.content)["summary"])


import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.scaledown.xyz/v1",
  apiKey: "<your-api-key>",
});

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [{ role: "user", content: "Your long text here..." }],
});
const result = JSON.parse(r.choices[0].message.content!);
console.log(result.summary);


curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize-1",
    "max_tokens": 150,
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
      {"role": "user", "content": "Your long text here..."}
    ]
  }'


r = client.chat.completions.create(
    model="summarize-1",
    max_tokens=150,
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on dates and key decisions only."},
        {"role": "user", "content": "Your long text here..."},
    ],
)
print(json.loads(r.choices[0].message.content)["summary"])


const r = await client.chat.completions.create({
  model: "summarize-1",
  max_tokens: 150,
  messages: [
    { role: "system", content: "Use bullet points. Focus on dates and key decisions only." },
    { role: "user", content: "Your long text here..." },
  ],
});
console.log(JSON.parse(r.choices[0].message.content!).summary);


DOCUMENT=$(base64 -b 0 -i report.pdf)

curl -X POST https://api.scaledown.xyz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: <your-api-key>" \
  -d '{
    "model": "summarize",
    "messages": [
      {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
      {"role": "user", "content": "Summarize the attached document."}
    ],
    "document": "'"$DOCUMENT"'",
    "document_mime_type": "application/pdf"
  }'


import base64

with open("report.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

r = client.chat.completions.create(
    model="summarize",
    messages=[
        {"role": "system", "content": "Use bullet points. Focus on key figures and decisions only."},
        {"role": "user", "content": "Summarize the attached document."},
    ],
    extra_body={"document": document, "document_mime_type": "application/pdf"},
)
print(json.loads(r.choices[0].message.content)["summary"])


import fs from "fs";

const document = fs.readFileSync("report.pdf").toString("base64");

const r = await client.chat.completions.create({
  model: "summarize",
  messages: [
    { role: "system", content: "Use bullet points. Focus on key figures and decisions only." },
    { role: "user", content: "Summarize the attached document." },
  ],
  // @ts-expect-error ScaleDown extension fields
  document,
  document_mime_type: "application/pdf",
});
console.log(JSON.parse(r.choices[0].message.content!).summary);

---8<--- page: docs-scaledown-ai-benchmarks-methodology ---8<---

Page URL: https://docs.scaledown.ai/benchmarks/methodology
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Benchmarks
Overview
Head-to-head
On this page
How to read the results
Methodology
Copy page

The datasets and metrics behind every ScaleDown benchmark.

Each ScaleDown model is scored on one public dataset with one standard metric, so results are comparable across providers.
Task	Dataset	Metric	What is tested
Classify	CLINC OOS	Accuracy	Picking the right intent label, including out-of-scope queries
Extract	CUAD	F1	Pulling contract clauses and fields out of legal agreements
Summarize	QMSum	ROUGE-L	Summarizing multi-speaker meeting transcripts
Compress	FinanceBench	F1	Answering finance questions from long filings after the context is compressed
​
How to read the results
Accuracy is shown per task and as an average. Cross-task scores use standardized F1, ROUGE-L and accuracy.
Cost is price per 1K requests, so cheap models and large models are compared on the same unit.
Latency is response time per task. Lower is better.
Every provider page compares ScaleDown against each model in that provider’s lineup, not just the flagship.
Compress is evaluated end to end: the compressed context is passed to a downstream LLM and the answer is scored, so the metric reflects whether the right information survived.
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-benchmarks-openai ---8<---

Page URL: https://docs.scaledown.ai/benchmarks/openai
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Benchmarks
Overview
Head-to-head
On this page
Accuracy
Latency
ScaleDown vs OpenAI
Copy page

ScaleDown against GPT-5.5, GPT-5.4 Mini and GPT-5.4 Nano.

Compared against GPT-5.5, GPT-5.4 Mini and GPT-5.4 Nano on the four benchmark tasks.
​
Accuracy
ScaleDown averages 8.72% higher accuracy than the OpenAI average.
Task	Dataset	ScaleDown vs OpenAI avg
Classify	CLINC OOS	+5.40%
Extract	CUAD	+14.40%
Summarize	QMSum	+8.83%
Compress	FinanceBench	+6.23%
​
Latency
ScaleDown is about 2.4x faster than the OpenAI average. Response time in milliseconds:
Task	ScaleDown	GPT-5.5	Mini	Nano	OpenAI avg
Classify	647	3,592	694	697	1,661
Extract	918	6,083	1,042	1,860	2,995
Summarize	1,426	7,805	1,856	1,759	3,807
Compress	2,658	8,217	3,087	3,426	4,910
Cost and full charts: Per-1K-request cost, accuracy charts and the cost-vs-accuracy plot on scaledown.ai.
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-benchmarks-overview ---8<---

Page URL: https://docs.scaledown.ai/benchmarks/overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Benchmarks
Overview
Head-to-head
On this page
Each comparison reports
Head-to-head
Benchmarks
Overview
Copy page

How ScaleDown’s task-specific models compare to frontier LLMs on accuracy, cost and latency.

ScaleDown models are small and built for one job each: Classify, Extract, Summarize and Compress. We benchmark each against leading general-purpose models on public datasets and compare accuracy, cost and latency side by side.
Methodology
The four tasks, their datasets and metrics.
ScaleDown vs OpenAI
Accuracy and latency against GPT-5.5, Mini and Nano.
​
Each comparison reports
Accuracy: ScaleDown versus every model in a provider’s lineup.
Cost: price per 1K requests for each model.
Latency: response time per task.
​
Head-to-head
OpenAI
GPT-5.5, GPT-5.4 Mini, GPT-5.4 Nano
8.72% higher accuracy, 2.4× faster.
Anthropic
Fable 5, Opus 4.8, Sonnet 4.6, Haiku 4.5
8.0% higher accuracy, 3.8× faster.
Gemini
3.1 Pro, 3.5 Flash, 3.1 Flash-Lite
9.0% higher accuracy, 8.3× faster.
Grok
Grok 4.3, Grok 4.2
7.93% higher accuracy, 2.2× faster.
DeepSeek
V4 Pro, V4 Flash
19.5% higher accuracy, 4.1× faster.
Qwen
Qwen3.8 Max, 27B, Qwen3.5 4B
16.71% higher accuracy, 13.9× faster.
All benchmarks: Full charts, cost tables and latency on scaledown.ai.
Head-to-head
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-benchmarks-providers ---8<---

Page URL: https://docs.scaledown.ai/benchmarks/providers
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Benchmarks
Overview
Head-to-head
On this page
OpenAI
Anthropic
Gemini
Grok
DeepSeek
Qwen
GLiNER
Benchmarks
Head-to-head
Copy page

ScaleDown versus each provider’s lineup on accuracy, cost and latency.

Every figure is ScaleDown measured against that provider’s average across its models on the same task. Accuracy is the gain in score; cost and latency are how many times cheaper or faster ScaleDown is. Datasets and metrics are in Methodology.
​
OpenAI
Models compared: GPT-5.5, GPT-5.4 Mini, GPT-5.4 Nano
8.72% higher accuracy
than the OpenAI avg
89× cheaper
than the OpenAI avg
2.4× faster
than the OpenAI avg
Task	Accuracy	Cost	Latency
Classify	+5.40%	1,810× cheaper	2.6× faster
Extract	+14.40%	35× cheaper	3.3× faster
Summarize	+8.83%	41× cheaper	2.7× faster
Compress	+6.23%	138× cheaper	1.8× faster
Full ScaleDown vs OpenAI charts and cost tables
​
Anthropic
Models compared: Fable 5, Opus 4.8, Sonnet 4.6, Haiku 4.5
8.0% higher accuracy
than the Anthropic avg
161× cheaper
than the Anthropic avg
3.8× faster
than the Anthropic avg
Task	Accuracy	Cost	Latency
Classify	+2.29%	5,250× cheaper	3.6× faster
Extract	+13.33%	91× cheaper	3.2× faster
Summarize	+8.22%	217× cheaper	4.4× faster
Full ScaleDown vs Anthropic charts and cost tables
​
Gemini
Models compared: 3.1 Pro, 3.5 Flash, 3.1 Flash-Lite
9.0% higher accuracy
than the Gemini avg
29× cheaper
than the Gemini avg
8.3× faster
than the Gemini avg
Task	Accuracy	Cost	Latency
Classify	+2.10%	2,437× cheaper	13.8× faster
Extract	+10.34%	26× cheaper	13.4× faster
Summarize	+14.70%	28× cheaper	2.6× faster
Full ScaleDown vs Gemini charts and cost tables
​
Grok
Models compared: Grok 4.3, Grok 4.2
7.93% higher accuracy
than the Grok avg
24× cheaper
than the Grok avg
2.2× faster
than the Grok avg
Task	Accuracy	Cost	Latency
Classify	+1.45%	1,161× cheaper	2.3× faster
Extract	+12.30%	22× cheaper	2.3× faster
Summarize	+10.05%	25× cheaper	2.1× faster
Full ScaleDown vs Grok charts and cost tables
​
DeepSeek
Models compared: DeepSeek V4 Pro, DeepSeek V4 Flash
19.5% higher accuracy
than the DeepSeek avg
9× cheaper
than the DeepSeek avg
4.1× faster
than the DeepSeek avg
Task	Accuracy	Cost	Latency
Classify	+20.75%	113× cheaper	3.7× faster
Extract	+31.03%	9× cheaper	3.9× faster
Summarize	+6.73%	10× cheaper	4.4× faster
Full ScaleDown vs DeepSeek charts and cost tables
​
Qwen
Models compared: Qwen3.8 Max, Qwen3.8 27B, Qwen3.5 4B
16.71% higher accuracy
than the Qwen avg
24× cheaper
than the Qwen avg
13.9× faster
than the Qwen avg
Task	Accuracy	Cost	Latency
Classify	+9.12%	761× cheaper	7.2× faster
Extract	+31.98%	18× cheaper	26.1× faster
Summarize	+9.04%	28× cheaper	9.2× faster
Full ScaleDown vs Qwen charts and cost tables
​
GLiNER
Model compared: GLiNER2.5-multi-v1, a local open-source model for classification and extraction.
GLiNER is the one comparison where ScaleDown is not the faster or cheaper option. GLiNER runs locally, so inference is free, and it is faster, while ScaleDown is more accurate.
Task	Accuracy (ScaleDown vs GLiNER)	GLiNER latency	Cost
Classify	+15.5 pp for ScaleDown	22 ms	GLiNER free (local inference)
Extract	+0.2 pp for ScaleDown	480 ms	GLiNER free (local inference)
Averaged across both tasks, ScaleDown’s accuracy advantage is +10.5%.
Full ScaleDown vs GLiNER charts
Overview
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-cookbooks-documents ---8<---

Page URL: https://docs.scaledown.ai/cookbooks/documents
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Cookbooks
Overview
Browse by data type
Voice & Calls
Chats & Tickets
Files & Docs
Web Pages
On this page
Compress
Summarize
Extract
Classify
Browse by data type
Files & Docs
Copy page

Filings, contracts, reports and case files, including scanned documents.

Filings, contracts, reports and case files, including scanned documents. Four recipes, one per ScaleDown model.
​
Compress
Strip redundant, low-signal text out of a long document before it hits your LLM.
Sits in front of your LLM. Open the full Python recipe.
	
Why it fits	Filings, contracts, and reports are long and repetitive across versions; you are paying to process restatement.
How it goes	Document or extracted text in → Compress trims to what the task needs → the LLM runs on the trimmed context.
Payoff	On FinanceBench, Compress with GPT-5.4 delivered +8% accuracy with 97% fewer tokens vs. GPT-5.4 alone.
​
Summarize
Digest a long filing, contract, or case file into a short brief.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	The reader needs the gist of a dense document, not the whole thing.
How it goes	Document in → Summarize produces the brief → surface it to the user or downstream step.
Payoff	Document briefs without a frontier call per doc.
​
Extract
Pull structured facts: parties, dates, amounts, clauses, citations.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	In regulated work a wrong field is a real problem; Extract returns the values as written.
How it goes	Document in → tell Extract the fields → it returns them structured → into the system of record.
Payoff	Clean structured data off unstructured docs.
​
Classify
Triage and tag documents by type, relevance, and routing.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	At high document volume you want a cheap first pass that decides what each doc is before deeper work.
How it goes	Document in → Classify assigns the label → route to the right pipeline or reviewer.
Payoff	Fast triage at page-volume scale.
Chats & Tickets
Web Pages
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-cookbooks-messages ---8<---

Page URL: https://docs.scaledown.ai/cookbooks/messages
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Cookbooks
Overview
Browse by data type
Voice & Calls
Chats & Tickets
Files & Docs
Web Pages
On this page
Compress
Summarize
Extract
Classify
Browse by data type
Chats & Tickets
Copy page

Email threads, Slack channels and support tickets.

Email threads, Slack channels and support tickets. Four recipes, one per ScaleDown model.
​
Compress
Shrink a long thread down to what matters before an LLM drafts a reply or runs an action.
Sits in front of your LLM. Open the full Python recipe.
	
Why it fits	Long email and Slack threads carry a lot of greetings, sign-offs, and quoted history; most of it is dead weight on the next call.
How it goes	Thread in → Compress strips the boilerplate, keeps the ask → the LLM works on the trimmed context.
Payoff	Fewer tokens into the drafting or answering call.
​
Summarize
Catch me up on this thread in one or two lines.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	People do not want to read a long thread top to bottom; they want the state of it.
How it goes	Thread in → Summarize produces the digest → surface it in the inbox, channel, or handoff.
Payoff	Thread digests without a frontier call each time.
​
Extract
Pull the action items, dates, and owners out of a message or thread.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	The asks are buried in prose; Extract turns them into fields a system can act on.
How it goes	Message in → tell Extract what to look for → it returns tasks, dates, owners → push to the tracker.
Payoff	Structured to-dos straight from the thread.
​
Classify
Sort and route each message by topic, priority, or sentiment.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	Triage runs on every support message; volume makes per-message frontier cost add up fast.
How it goes	Message in → Classify assigns the label → route to the right queue, owner, or alert.
Payoff	Cheap, fast labeling at inbox volume.
Voice & Calls
Files & Docs
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-cookbooks-overview ---8<---

Page URL: https://docs.scaledown.ai/cookbooks/overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Cookbooks
Overview
Browse by data type
On this page
The four models
Every recipe has the same five parts
Browse by data type
Cookbooks
Overview
Copy page

16 recipes for using ScaleDown’s four models on voice, messages, documents and web pages.

Cookbooks are end-to-end recipes: real input, a ScaleDown call, and the response you get back, in Python. There are 16, one for each pairing of data type and model. Run them from scaledown.ai/cookbooks; you need an API key (see the quickstart).
​
The four models
Each model has its own job. Compress runs before your LLM; the other three each stand in for an LLM call.
Compress
Runs in front of your LLM. Trims retrieved or pasted context down to what the question needs, so the LLM call uses fewer tokens and returns faster. Endpoint: POST /compress/raw/.
Summarize
Replaces an LLM call. Turns long, messy text such as transcripts, threads and filings into a short abstractive summary. Model: summarize on POST /v1/chat/completions.
Extract
Replaces an LLM call. Pulls the fields you define out of unstructured text and returns them as structured data, exactly as written in the source. Model: extract on POST /v1/chat/completions.
Classify
Replaces an LLM call. Scores text against labels you define with a yes/no rubric and returns a probability for each, plus a top_label for routing. Endpoints: POST /v1/scaledown (Decisions) and POST /classify.
​
Every recipe has the same five parts
Part	What it tells you
The move	What the model does here, in one line
Model role	Whether it sits in front of your LLM or replaces a call
Why it fits	The constraint that makes this the right model
How it goes	The pipeline, step by step
Payoff	The result. Only two recipes quote measured benchmarks: Voice Summarize (QMSum) and Documents Compress (FinanceBench). The rest are described qualitatively.
​
Browse by data type
Voice & Calls
Call recaps, caller routing, CRM fields from sales calls.
Chats & Tickets
Thread digests, triage and action items.
Files & Docs
Briefs, document tagging and clause extraction.
Web Pages
Boilerplate stripping, relevance filtering and enrichment.
Browse all cookbooks: Filter by data type or model on scaledown.ai.
Voice & Calls
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-cookbooks-voice ---8<---

Page URL: https://docs.scaledown.ai/cookbooks/voice
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Cookbooks
Overview
Browse by data type
Voice & Calls
Chats & Tickets
Files & Docs
Web Pages
On this page
Compress
Summarize
Extract
Classify
Browse by data type
Voice & Calls
Copy page

Calls, voice agents and meeting recordings, after transcription.

Calls, voice agents and meeting recordings, after transcription. Four recipes, one per ScaleDown model.
​
Compress
Trim the backend docs down to what the question needs, so the agent can answer a live caller fast.
Sits in front of your answering LLM. Open the full Python recipe.
	
Why it fits	The caller is not left waiting while a big chunk of retrieved text gets processed.
How it goes	Caller asks → speech transcribed → backend pulls docs → Compress trims them → LLM writes a short answer → agent says it.
Payoff	Lower latency on the retrieval step, less token spend per answered call.
​
Summarize
Turn a call or meeting transcript into a short recap with the decisions and action items.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	Transcripts are long, conversational, and multi-speaker, exactly the workload Summarize is built for.
How it goes	Call ends → transcript in → Summarize produces the recap → push to the notetaker, CRM, or follow-up draft.
Payoff	State-of-the-art on QMSum, the meeting-summarization benchmark.
​
Extract
Pull the CRM fields out of a sales call, deal size, economic buyer, next meeting, into clean fields.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	A deal cannot move on a guess; Extract returns the numbers and names exactly as they were said on the call.
How it goes	Call ends → transcript in → you tell Extract what to look for → it returns the fields → push into HubSpot.
Payoff	Structured CRM fields straight off the transcript, no rep data entry.
​
Classify
Send the caller to the right place based on what they say, instead of press 1 for billing.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	Routing is the busiest step in the call; Classify handles a simple choice fast without paying a frontier model to overthink it.
How it goes	Caller says what they need → speech transcribed → Classify picks the label → agent routes them into that flow.
Payoff	Faster routing at lower cost per call.
Overview
Chats & Tickets
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-cookbooks-web ---8<---

Page URL: https://docs.scaledown.ai/cookbooks/web
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Cookbooks
Overview
Browse by data type
Voice & Calls
Chats & Tickets
Files & Docs
Web Pages
On this page
Compress
Summarize
Extract
Classify
Browse by data type
Web Pages
Copy page

Scraped pages and enriched records for GTM and signal products.

Scraped pages and enriched records for GTM and signal products. Four recipes, one per ScaleDown model.
​
Compress
Strip HTML boilerplate and repetition out of a scraped page before any downstream call.
Sits in front of your LLM. Open the full Python recipe.
	
Why it fits	Raw web content is mostly navigation, markup, and restatement across sources: high redundancy, high Compress leverage.
How it goes	Scraped page in → Compress strips boilerplate → the downstream model works on the signal.
Payoff	Large token reduction on noisy pages before the expensive step.
​
Summarize
Turn an enriched record or scraped page into a short, human-readable summary.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	The output a user reads should be a tight profile, not a wall of scraped text.
How it goes	Page or record in → Summarize produces the profile → surface it in the product.
Payoff	Readable summaries at crawl volume.
​
Extract
Pull structured facts off a page: company, role, signal, contact details.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	Enrichment is continuous extraction over raw web content; this is the core loop for GTM and signal products.
How it goes	Page in → tell Extract the fields → it returns structured facts → into the record.
Payoff	Structured enrichment off unstructured pages.
​
Classify
Relevance-score and tag scraped records, so only the useful ones move on.
Replaces an LLM call. Open the full Python recipe.
	
Why it fits	Most scraped records are junk; you want a cheap, fast filter before spending on extraction.
How it goes	Record in → Classify scores relevance and assigns tags → route or drop.
Payoff	Fast filtering keeps junk out of the expensive pipeline.
Files & Docs
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-dietcode-clients ---8<---

Page URL: https://docs.scaledown.ai/dietcode/clients
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
DietCode
Overview
Install
Proxy mode
Supported clients
On this page
The sd_retrieve tool
Notes per client
DietCode
Supported clients
Copy page

What DietCode does in Claude Code, Codex CLI and Cursor.

Client	Hooks (auto compression, intent)	Proxy mode	Status line
Claude Code	Yes	Yes	Yes
Codex CLI	Yes	No	No
Cursor	No (no hook system)	No	No
​
The sd_retrieve tool
Compression, summarization, classification and extraction run automatically through hooks and the proxy, so their schemas never add to your tool list. The one tool exposed to the agent, in all three clients, is sd_retrieve, which restores the original text behind a proxy summary marker. It only has something to retrieve in a Claude Code proxy session.
​
Notes per client
Claude Code: full feature set, including the live savings display. This is an npm CLI plugin; there is no IDE extension, and the status line is Claude Code’s terminal status line.
Codex CLI: the same hooks as Claude Code. Token savings happen, but nothing is displayed.
Cursor: has no hook system, so it gets no automatic optimization today. Install it there only for sd_retrieve.
Proxy mode
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-dietcode-install ---8<---

Page URL: https://docs.scaledown.ai/dietcode/install
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
DietCode
Overview
Install
Proxy mode
Supported clients
On this page
Claude Code (recommended)
Codex CLI
Cursor
DietCode
Install
Copy page

Install DietCode and run the setup wizard.

You need Node.js 18+ and a ScaleDown API key from scaledown.ai/dashboard.
​
Claude Code (recommended)
npm install -g dietcode
dietcode setup

The wizard:
Opens your browser to get an API key.
Validates the key you paste against the API.
Saves it to your shell config and ~/.scaledown/config.json.
Registers the MCP server with Claude Code.
Writes the UserPromptSubmit, PostToolUse and PreCompact hooks, the status line and the auto-compact threshold to ~/.claude/settings.json.
Offers to alias claude to dietcode claude, which turns on proxy mode.
Optionally configures Codex CLI and Cursor.
Restart Claude Code and you’re done.
​
Codex CLI
npm install -g dietcode
codex mcp add dietcode --env SCALEDOWN_API_KEY=your-key-here -- npx -y dietcode

Run dietcode setup and answer y for Codex CLI to register the same hooks Claude Code uses in ~/.codex/config.toml.
​
Cursor
npm install -g dietcode

Add to .cursor/mcp.json (or ~/.cursor/mcp.json for global use):
{
  "mcpServers": {
    "dietcode": {
      "command": "npx",
      "args": ["-y", "dietcode"],
      "env": { "SCALEDOWN_API_KEY": "your-key-here" }
    }
  }
}

Restart Cursor. sd_retrieve appears in Agent mode.
Cursor has no hook system, so it currently gets none of the automatic optimization. See Supported clients.
Overview
Proxy mode
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-dietcode-overview ---8<---

Page URL: https://docs.scaledown.ai/dietcode/overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
DietCode
Overview
Install
Proxy mode
Supported clients
On this page
What it does
DietCode
Overview
Copy page

Cut token usage in Claude Code, Codex CLI and Cursor with automatic compression, summarization and intent routing.

DietCode is an npm plugin that optimizes coding-agent sessions using ScaleDown. It runs automatically through hooks (Claude Code and Codex CLI) and an optional local proxy.
scaledown-team/DietCode
Source, issues and the full README.
​
What it does
On every prompt, DietCode:
Classifies intent and prepends a one-line hint such as [DietCode intent: file_read (87%)], so the agent picks the right tool.
Compresses large contexts when you paste a big codebase and ask a retrieval-style question, cutting 50-70% of tokens before the prompt reaches the model.
Compresses large tool outputs. ls, grep and git diff/log/status are compacted with no latency; anything still large goes through ScaleDown.
Tracks savings live in the Claude Code status line, for example ↓ 125.4K saved · 747 reqs.
Compression only fires on prompts that are both large and retrieval-style. Conversational prompts and code you ask it to write are left alone.
your prompt ──▶ [intent classify] ──▶ [needle-in-haystack?] ──▶ compress ──▶ agent
                     │                        │
                 one-line hint          /compress/raw/  (50-70% smaller)

Install
Set up in about a minute.
Proxy mode
Real per-turn token savings.
Supported clients
Claude Code, Codex CLI, Cursor.
Install
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-dietcode-proxy-mode ---8<---

Page URL: https://docs.scaledown.ai/dietcode/proxy-mode
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
DietCode
Overview
Install
Proxy mode
Supported clients
On this page
What the proxy sends
Why it works
Run the proxy yourself
DietCode
Proxy mode
Copy page

Route Claude Code through a local proxy that shrinks the context every turn.

Hooks can only add context to the window; they can never rewrite the history Claude re-sends every turn. To genuinely reduce tokens, DietCode sits in the request path.
dietcode claude   # claude, routed through a local DietCode proxy

This starts a small proxy on 127.0.0.1 (ephemeral port, torn down when you quit), points Claude Code at it via ANTHROPIC_BASE_URL, and launches claude normally.
​
What the proxy sends
[ system + tools ]            untouched, keeps Anthropic's prompt cache warm
[ running ScaleDown summary ] stands in for older turns
[ last N turns verbatim ]     the live working set

​
Why it works
Progressive
Most turns make zero ScaleDown calls. One call folds the oldest turns into the summary only when summary plus recent turns passes SCALEDOWN_PROXY_COMPACT_THRESHOLD.
Replaces native compaction
The forwarded payload stays small, so Claude’s own auto-compaction effectively never fires. ScaleDown owns compaction instead.
Reversible
Compacted turns are stored locally. The summary tells Claude to call sd_retrieve("<id>") when it needs an exact detail.
Cache-safe
System prompt and tools are untouched, so Anthropic’s prompt cache stays warm.
​
Run the proxy yourself
dietcode proxy --port 8788
export ANTHROPIC_BASE_URL=http://127.0.0.1:8788
claude

Why not a PreCompact hook? It can only append to the window, so injecting a summary there costs tokens instead of saving them. The real work happens in the proxy, where DietCode controls the request payload.
Install
Supported clients
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-introduction ---8<---

Page URL: https://docs.scaledown.ai/introduction
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Getting Started
Introduction
Quickstart
Understanding the response
On this page
What is ScaleDown?
Before You Start
Explore the models
Getting Started
Introduction
Copy page

What ScaleDown is, what you need, and where to go next.

​
What is ScaleDown?
ScaleDown is a suite of task-specific models, including Constrained Decoding Models (CDMs) for classification and structured decisions, that reduce your AI token usage through context extraction - identifying and retaining only the information that matters for your task. You get the same quality responses while paying significantly less.
​
Before You Start
To use ScaleDown, you’ll need:
An API key
Basic knowledge of making API calls
Your existing AI prompts that you want to optimize
The API base URL is https://api.scaledown.xyz. (api.scaledown.ai is not an API host.)
Ready to get your API key? Contact our sales team.
​
Explore the models
Compress
Trim context before your LLM call.
Summarize
Short abstractive summaries of long text.
Extract
Structured fields from unstructured text.
Classify
Label text with your own rubrics.
Quickstart
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

ADDITIONAL VISIBLE STATES / CHART VALUES
Docs root request redirected to /introduction; captured rendered Introduction page.

---8<--- page: docs-scaledown-ai-llms-txt ---8<---

Page URL: https://docs.scaledown.ai/llms.txt
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
# ScaleDown

- [Introduction](https://docs.scaledown.ai/introduction.md): What ScaleDown is, what you need, and where to go next.
- [Quickstart](https://docs.scaledown.ai/quickstart.md): Make your first ScaleDown request in three steps.
- [Understanding the response](https://docs.scaledown.ai/response.md): What the Compress API returns and how to read it.
- [Overview](https://docs.scaledown.ai/api-reference/summarize-overview.md): Generate fluent, faithful summaries of long text.
- [Summarize](https://docs.scaledown.ai/api-reference/summarize.md): Produce an abstractive summary of a block of text through the OpenAI-compatible chat completions API.
- [Overview](https://docs.scaledown.ai/api-reference/extract-overview.md): Pull structured data from unstructured text using a schema you define in plain English.
- [Extract](https://docs.scaledown.ai/api-reference/extract.md): Extract named entities from text using a custom-defined schema through the OpenAI-compatible chat completions API.
- [Classify overview](https://docs.scaledown.ai/api-reference/classify-overview.md): Score text against labels you define. Use the custom /classify API for labels with rubrics, or the Jev-compatible Decisions API for typed questions.
- [Classify API](https://docs.scaledown.ai/api-reference/classify.md): POST /classify - score text against your own labels and rubrics and get a probability for each label.
- [Decisions overview](https://docs.scaledown.ai/api-reference/decisions-overview.md): A drop-in replacement for the Jev Decisions API: answer typed choice, yes/no and scale questions about a piece of text.
- [Decisions API](https://docs.scaledown.ai/api-reference/decisions.md): POST /v1/scaledown - Jev-compatible request and response. Send a state and a set of typed questions, get one answer per question.
- [Overview](https://docs.scaledown.ai/api-reference/compress-overview.md): Reduce token usage across any AI workflow without changing your prompts or models.
- [Compress](https://docs.scaledown.ai/api-reference/compress.md): Compress a prompt and context to reduce token usage while preserving semantic meaning.
- [Overview](https://docs.scaledown.ai/benchmarks/overview.md): How ScaleDown's task-specific models compare to frontier LLMs on accuracy, cost and latency.
- [Head-to-head](https://docs.scaledown.ai/benchmarks/providers.md): ScaleDown versus each provider's lineup on accuracy, cost and latency.
- [Overview](https://docs.scaledown.ai/cookbooks/overview.md): 16 recipes for using ScaleDown's four models on voice, messages, documents and web pages.
- [Voice & Calls](https://docs.scaledown.ai/cookbooks/voice.md): Calls, voice agents and meeting recordings, after transcription.
- [Chats & Tickets](https://docs.scaledown.ai/cookbooks/messages.md): Email threads, Slack channels and support tickets.
- [Files & Docs](https://docs.scaledown.ai/cookbooks/documents.md): Filings, contracts, reports and case files, including scanned documents.
- [Web Pages](https://docs.scaledown.ai/cookbooks/web.md): Scraped pages and enriched records for GTM and signal products.
- [Overview](https://docs.scaledown.ai/dietcode/overview.md): Cut token usage in Claude Code, Codex CLI and Cursor with automatic compression, summarization and intent routing.
- [Install](https://docs.scaledown.ai/dietcode/install.md): Install DietCode and run the setup wizard.
- [Proxy mode](https://docs.scaledown.ai/dietcode/proxy-mode.md): Route Claude Code through a local proxy that shrinks the context every turn.
- [Supported clients](https://docs.scaledown.ai/dietcode/clients.md): What DietCode does in Claude Code, Codex CLI and Cursor.
- [Overview](https://docs.scaledown.ai/slm-agent/overview.md): Scan your codebase for LLM calls and migrate them to ScaleDown models, then tune the prompts against your own data.
- [Install](https://docs.scaledown.ai/slm-agent/install.md): Add ScaleDown Agent to Claude Code, Cursor, VS Code or any MCP client.
- [Evaluate](https://docs.scaledown.ai/slm-agent/evaluate.md): Scan a project, get a migration plan, and apply it.
- [Optimize](https://docs.scaledown.ai/slm-agent/optimize.md): Tune a ScaleDown prompt until it matches or beats the frontier model it replaced.

## OpenAPI Specs

- [openapi](/api-reference/openapi.json)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.

ADDITIONAL VISIBLE STATES / CHART VALUES
Documentation page index captured to enumerate current docs.

---8<--- page: docs-scaledown-ai-quickstart ---8<---

Page URL: https://docs.scaledown.ai/quickstart
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Getting Started
Introduction
Quickstart
Understanding the response
On this page
Your First ScaleDown Request
Step 1: Set Up Your Request
Step 2: Configure Your Compression
Step 3: Make the Request
Getting Started
Quickstart
Copy page

Make your first ScaleDown request in three steps.

​
Your First ScaleDown Request
​
Step 1: Set Up Your Request
Here’s how to make your first API call to compress a prompt.
Python
TypeScript
JavaScript
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}

​
Step 2: Configure Your Compression
Separate your context from your main prompt and set the compression rate to "auto" for the best results.
Python
TypeScript
JavaScript
payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}

​
Step 3: Make the Request
With your request set up and configured, you can now execute the API call.
Python
TypeScript
JavaScript
response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)

That’s it! Your prompt is now compressed and ready to be used with your AI model.
Next: understand the response.
Introduction
Understanding the response
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

ADDITIONAL VISIBLE STATES / CHART VALUES
INTERACTIVE TAB PANEL TEXT
--- Python [tab 0] ---
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}


interface CompressRequest {
    context: string;
    prompt: string;
    scaledown: {
        rate: string;
    };
}

const payload: CompressRequest = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


const payload = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)


// Assuming you're using a fetch-like library (e.g., node-fetch)
const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
});
const result = await response.json();

console.log(result);


// Using Fetch API in a browser or Node.js environment
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(result => {
    console.log(result);
})
.catch(error => console.error('Error:', error));


--- TypeScript [tab 1] ---
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}


interface CompressRequest {
    context: string;
    prompt: string;
    scaledown: {
        rate: string;
    };
}

const payload: CompressRequest = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


const payload = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)


// Assuming you're using a fetch-like library (e.g., node-fetch)
const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
});
const result = await response.json();

console.log(result);


// Using Fetch API in a browser or Node.js environment
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(result => {
    console.log(result);
})
.catch(error => console.error('Error:', error));


--- JavaScript [tab 2] ---
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}


interface CompressRequest {
    context: string;
    prompt: string;
    scaledown: {
        rate: string;
    };
}

const payload: CompressRequest = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


const payload = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)


// Assuming you're using a fetch-like library (e.g., node-fetch)
const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
});
const result = await response.json();

console.log(result);


// Using Fetch API in a browser or Node.js environment
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(result => {
    console.log(result);
})
.catch(error => console.error('Error:', error));


--- Python [tab 3] ---
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}


interface CompressRequest {
    context: string;
    prompt: string;
    scaledown: {
        rate: string;
    };
}

const payload: CompressRequest = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


const payload = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)


// Assuming you're using a fetch-like library (e.g., node-fetch)
const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
});
const result = await response.json();

console.log(result);


// Using Fetch API in a browser or Node.js environment
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(result => {
    console.log(result);
})
.catch(error => console.error('Error:', error));


--- TypeScript [tab 4] ---
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}


interface CompressRequest {
    context: string;
    prompt: string;
    scaledown: {
        rate: string;
    };
}

const payload: CompressRequest = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


const payload = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)


// Assuming you're using a fetch-like library (e.g., node-fetch)
const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
});
const result = await response.json();

console.log(result);


// Using Fetch API in a browser or Node.js environment
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(result => {
    console.log(result);
})
.catch(error => console.error('Error:', error));


--- JavaScript [tab 5] ---
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}


interface CompressRequest {
    context: string;
    prompt: string;
    scaledown: {
        rate: string;
    };
}

const payload: CompressRequest = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


const payload = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)


// Assuming you're using a fetch-like library (e.g., node-fetch)
const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
});
const result = await response.json();

console.log(result);


// Using Fetch API in a browser or Node.js environment
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(result => {
    console.log(result);
})
.catch(error => console.error('Error:', error));


--- Python [tab 6] ---
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}


interface CompressRequest {
    context: string;
    prompt: string;
    scaledown: {
        rate: string;
    };
}

const payload: CompressRequest = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


const payload = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)


// Assuming you're using a fetch-like library (e.g., node-fetch)
const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
});
const result = await response.json();

console.log(result);


// Using Fetch API in a browser or Node.js environment
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(result => {
    console.log(result);
})
.catch(error => console.error('Error:', error));


--- TypeScript [tab 7] ---
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}


interface CompressRequest {
    context: string;
    prompt: string;
    scaledown: {
        rate: string;
    };
}

const payload: CompressRequest = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


const payload = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)


// Assuming you're using a fetch-like library (e.g., node-fetch)
const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
});
const result = await response.json();

console.log(result);


// Using Fetch API in a browser or Node.js environment
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(result => {
    console.log(result);
})
.catch(error => console.error('Error:', error));


--- JavaScript [tab 8] ---
import requests
import json

# ScaleDown API endpoint
url = "https://api.scaledown.xyz/compress/raw/"

# Your headers (replace YOUR_API_KEY with your actual key)
headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


// ScaleDown API endpoint
const url = "[https://api.scaledown.xyz/compress/raw/](https://api.scaledown.xyz/compress/raw/)";

// Your headers (replace YOUR_API_KEY with your actual key)
const headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
};


payload = {
    "context": "Context about your specific topic or instructions here",
    "prompt": "Your actual query or question here",
    "scaledown": {
        "rate": "auto" # Automatic compression rate optimization
    }
}


interface CompressRequest {
    context: string;
    prompt: string;
    scaledown: {
        rate: string;
    };
}

const payload: CompressRequest = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


const payload = {
    context: "Context about your specific topic or instructions here",
    prompt: "Your actual query or question here",
    scaledown: {
        rate: "auto" // Automatic compression rate optimization
    }
};


response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result)


// Assuming you're using a fetch-like library (e.g., node-fetch)
const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
});
const result = await response.json();

console.log(result);


// Using Fetch API in a browser or Node.js environment
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(result => {
    console.log(result);
})
.catch(error => console.error('Error:', error));

---8<--- page: docs-scaledown-ai-response ---8<---

Page URL: https://docs.scaledown.ai/response
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
Getting Started
Introduction
Quickstart
Understanding the response
Getting Started
Understanding the response
Copy page

What the Compress API returns and how to read it.

The API response provides the compressed prompt along with useful metadata about the operation.
{
  "results": {
    "success": true,
    "compressed_prompt": "Your optimized context here...",
    "original_prompt": "Summarize the key facts.",
    "original_prompt_tokens": 150,
    "compressed_prompt_tokens": 65,
    "compression_ratio": 0.43
  },
  "model_used": "gpt-4o",
  "input_tokens": 150,
  "total_original_tokens": 150,
  "total_compressed_tokens": 65,
  "num_pairs_processed": 1,
  "num_successful": 1,
  "num_failed": 0,
  "successful": true,
  "partially_successful": false,
  "latency_ms": 2341,
  "request_metadata": {
    "compression_time_ms": 2341,
    "compression_rate": "auto",
    "average_compression_ratio": 0.43
  }
}

Quickstart
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-slm-agent-evaluate ---8<---

Page URL: https://docs.scaledown.ai/slm-agent/evaluate
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
ScaleDown Agent
Overview
Install
Evaluate
Optimize
On this page
The migration report
MCP tools
ScaleDown Agent
Evaluate
Copy page

Scan a project, get a migration plan, and apply it.

/slm-agent:evaluate scans your project, writes a migration plan, and applies the changes to your code with your approval.
​
The migration report
Evaluation saves scaledown-report.md in your project root, following a fixed schema (version "1"):
Section	Content
Summary table	Files scanned, files with AI calls, total opportunities, providers detected
Complexity breakdown	Calls at each level, trivial to highly complex
Per-opportunity sections	Files, line numbers, complexity score, confidence and action for each of sd_classify, sd_extract, sd_summarize, sd_compress
Complex call decompositions	For calls scoring 3+/5, which sub-tasks can move to a ScaleDown model and which still need a frontier LLM
HTTP API reference	Request and response shapes for /classify, /v1/scaledown, /v1/chat/completions (extract, summarize) and /compress/raw/
## Summary
| Metric | Value |
|---|---|
| Files scanned | 42 |
| Files with AI API calls | 7 |
| Total integration opportunities | 11 |
| Providers detected | openai, langchain |

​
MCP tools
Tool	Description
get_ai_detection_patterns	Regex patterns for all supported AI providers
get_integration_template	Before/after code showing how to integrate ScaleDown
generate_migration_plan	Structured markdown plan from a list of findings
save_migration_report	Writes the plan to scaledown-report.md
Analysis runs locally. The only network calls are your application’s runtime calls to ScaleDown, using the SCALEDOWN_API_KEY you provide.
Install
Optimize
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-slm-agent-install ---8<---

Page URL: https://docs.scaledown.ai/slm-agent/install
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
ScaleDown Agent
Overview
Install
Evaluate
Optimize
On this page
Claude Code
ScaleDown Agent
Install
Copy page

Add ScaleDown Agent to Claude Code, Cursor, VS Code or any MCP client.

​
Claude Code
/plugin marketplace add scaledown-team/SLM_Agent
/plugin install slm-agent@scaledown
/reload-plugins

Then, inside any project:
/slm-agent:evaluate    # find and migrate AI calls to ScaleDown models
/slm-agent:optimize    # tune a ScaleDown prompt against your own data

The plugin configures the MCP server and registers both skills. No further setup needed.
Cursor
VS Code
Any MCP client
Add to .cursor/mcp.json (or ~/.cursor/mcp.json for global):
{
  "mcpServers": {
    "scaledown-slm-agent": {
      "command": "npx",
      "args": ["-y", "@scaledown/migration-agent"]
    }
  }
}

Then ask Cursor: “Use the scaledown-slm-agent tools to evaluate this codebase for ScaleDown integration opportunities.”
optimize in Cursor: Cursor loads Agent Skills from .agents/skills/. Copy optimize/ from the package (or the cloned repo) into your project’s .agents/skills/, restart Cursor, and ask it to “optimize my ScaleDown prompt”. optimize needs no MCP setup; evaluate does.
Overview
Evaluate
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-slm-agent-optimize ---8<---

Page URL: https://docs.scaledown.ai/slm-agent/optimize
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
ScaleDown Agent
Overview
Install
Evaluate
Optimize
On this page
The loop
Metric per task
Output
ScaleDown Agent
Optimize
Copy page

Tune a ScaleDown prompt until it matches or beats the frontier model it replaced.

Migrating a call is step one. /slm-agent:optimize is step two: making the ScaleDown model’s output match or beat the frontier model on your data.
export SCALEDOWN_API_KEY=...
/slm-agent:optimize

​
The loop
Collect your API key (read from the environment, never written to disk) and a small set of labeled samples.
Create samples if you have none. It finds representative inputs in your project, agrees a label schema with you, records a baseline answer per sample, and validates the set.
Run a reproducible eval (scaledown-eval/run_eval.py) with a metric that can’t be gamed.
Iterate the prompt one scoped change at a time. It re-runs the current best twice in the same batch to separate real gains from API noise, and scores the whole task so a win on one class that regresses another is caught.
​
Metric per task
Task	Metric
Classify	Macro-F1 plus a confusion matrix, so a rare class can’t be ignored
Extract	Per-field precision and recall, split by real vs empty so a field can’t look accurate by returning nothing
Summarize	ROUGE and faithfulness
Compress	Compression ratio plus downstream correctness
​
Output
Everything lives under scaledown-eval/: the samples, each prompt version, per-round metrics, and an optimization-report.md with the winning prompt and the exact command to reproduce it. Sample data is only sent to the ScaleDown endpoint you provided a key for.
Evaluate
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: docs-scaledown-ai-slm-agent-overview ---8<---

Page URL: https://docs.scaledown.ai/slm-agent/overview
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
ScaleDown home page
Search...
⌘K
Docs
API Reference
Benchmarks
Cookbooks
DietCode
ScaleDown Agent
ScaleDown Agent
Overview
Install
Evaluate
Optimize
On this page
What it does
Supported providers
ScaleDown Agent
Overview
Copy page

Scan your codebase for LLM calls and migrate them to ScaleDown models, then tune the prompts against your own data.

ScaleDown Agent is an MCP server and Claude Code plugin that finds AI API calls in your project and shows where ScaleDown models can replace or shrink them. It analyzes code locally; no source code is sent to ScaleDown.
scaledown-team/SLM_Agent
Source, issues and the full README.
​
What it does
Evaluates. Scans for OpenAI, Anthropic, LangChain, LlamaIndex, Cohere and other AI calls.
Plans. Maps each call site to the model that fits:
Model	Use it to	Savings
sd_compress	Cut context tokens 50-70% before your LLM call (RAG, long docs)	Fewer tokens
sd_classify	Replace LLM classification calls	~95% cheaper
sd_extract	Replace LLM entity extraction calls	~95% cheaper
sd_summarize	Replace LLM summarization calls	~90% cheaper
Migrates. Applies the changes to your code, with your approval.
Optimizes. Tunes the prompt you pass to a ScaleDown model on your own data and benchmarks it against the frontier-model output it replaced.
​
Supported providers
OpenAI, Anthropic and LangChain (Python and TypeScript/JS); LlamaIndex, Cohere and Google Generative AI (Python); Vercel AI SDK (TypeScript/JS).
Install
Claude Code, Cursor, VS Code.
Evaluate
Migration report and MCP tools.
Optimize
Tune prompts on your data.
Install
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform

---8<--- page: scaledown-ai-benchmarks-scaledown-vs-anthropic ---8<---

Page URL: https://scaledown.ai/benchmarks/scaledown-vs-anthropic/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
ScaleDown vs Anthropic

We benchmarked three ScaleDown models (Classify, Extract, Summarize) against Claude Fable 5, Opus 4.8, Sonnet 4.6, and Haiku 4.5 across three public benchmarks.

Benchmarks: QMSum, CUAD, and CLINC OOS.

ACCURACY

8.0%

better than Anthropic avg

CLASSIFY

+2.29%

EXTRACT

+13.33%

SUMMARIZE

+8.22%

COST

161×

cheaper than Anthropic avg

CLASSIFY

5,250×

EXTRACT

91×

SUMMARIZE

217×

LATENCY

3.8×

faster than Anthropic avg

CLASSIFY

3.6×

EXTRACT

3.2×

SUMMARIZE

4.4×

Accuracy

Each ScaleDown model is purpose-built for one task. Summarize is compared on QMSum, Extract on CUAD, and Classify on CLINC OOS. All Anthropic models are run on the same benchmark and scored with the same metric.

Classify

CLINC OOS · Accuracy · higher is better

SD
Classify
Anthropic
Avg
Fable
Opus
Sonnet
Haiku
0.84
0.88
0.92
0.96
1.00
0.950
0.930
0.979
0.989
0.871
0.869
MODEL	ACCURACY
ScaleDown Classify	0.9500
Anthropic Avg	
0.9300
(-2.29%)

└Fable 5	
0.9794
(+2.94%)

└Opus 4.8	
0.9893
(+3.93%)

└Sonnet 4.6	
0.8707
(-7.93%)

└Haiku 4.5	
0.8689
(-8.11%)

Extract

CUAD · F1 · higher is better

SD
Extract
Anthropic
Avg
Fable
Opus
Sonnet
Haiku
0.40
0.46
0.52
0.58
0.64
0.612
0.480
0.450
0.504
0.496
0.465
MODEL	F1
ScaleDown Extract	0.6120
Anthropic Avg	
0.4800
(-13.33%)

└Fable 5	
0.4499
(-16.21%)

└Opus 4.8	
0.5045
(-10.75%)

└Sonnet 4.6	
0.4959
(-11.61%)

└Haiku 4.5	
0.4646
(-14.74%)

Summarize

QMSum · ROUGE-L · higher is better

SD
Summarize
Anthropic
Avg
Fable
Opus
Sonnet
Haiku
0.16
0.19
0.22
0.25
0.28
0.267
0.180
0.179
0.189
0.188
0.184
MODEL	ROUGE-L
ScaleDown Summarize	0.2670
Anthropic Avg	
0.1800
(-8.22%)

└Fable 5	
0.1788
(-8.82%)

└Opus 4.8	
0.1894
(-7.76%)

└Sonnet 4.6	
0.1875
(-7.95%)

└Haiku 4.5	
0.1836
(-8.34%)

ScaleDown's task-specific models average 8% higher accuracy than Anthropic's general-purpose lineup across all three benchmarks. The gap is widest on Extract (+13.3%), where CUAD's dense contract language favors a model built specifically for extraction. Classify is closer: Opus 4.8 and Fable 5 edge slightly ahead on raw accuracy, but ScaleDown still beats the blended Anthropic average at a fraction of the cost and latency.

Cost

All costs are calculated per 1,000 calls using list pricing at the time of measurement.

MOST ATTRACTIVE QUADRANT
ScaleDown
Fable 5
Opus 4.8
Sonnet 4.6
Haiku 4.5
$0.01
$0.1
$1
$10
$100
Cost per 1K calls
65%
70%
75%
80%
85%
90%
95%
100%
Accuracy score
(standardized F1, ROUGE-L & accuracy metrics)
SD Classify
SD Summarize
SD Extract
ScaleDown Avg
Anthropic Avg
Fable Classify
Fable Extract
Fable Summarize
Opus Classify
Opus Extract
Opus Summarize
Sonnet Classify
Sonnet Extract
Sonnet Summarize
Haiku Classify
Haiku Extract
Haiku Summarize
TASK	SCALEDOWN	FABLE 5	OPUS 4.8	SONNET 4.6	HAIKU 4.5	ANTHROPIC AVG
Classify	$0.0014	
$16.50
(11,786×)
	
$11.20
(8,000×)
	
$1.28
(914×)
	
$0.42
(300×)
	
$7.35
(5,250×)

Extract	$0.66	
$84.00
(127×)
	
$106.80
(162×)
	
$37.04
(56×)
	
$12.48
(19×)
	
$60.08
(91×)

Summarize	$0.70	
$120.00
(171×)
	
$426.00
(609×)
	
$46.80
(67×)
	
$15.40
(22×)
	
$152.05
(217×)

Average	$0.45	
$73.50
(163×)
	
$181.33
(400×)
	
$28.37
(63×)
	
$9.43
(21×)
	
$73.16
(161×)

ScaleDown costs 161× less than the Anthropic average per 1,000 calls. The widest gap is on Classify (5,250×), where a lightweight classifier stands in for a full-size language model on a task that doesn't need one. Even against Haiku 4.5, Anthropic's smallest and cheapest model, ScaleDown still runs at roughly a twentieth of the cost.

Latency

Mean response time per call, measured in milliseconds. Lower is better.

ScaleDown
Fable 5
Opus 4.8
Sonnet 4.6
Haiku 4.5
Anthropic Avg
0
2,000
4,000
6,000
8,000
10,000
Classify
Extract
Summarize
TASK	SCALEDOWN	FABLE 5	OPUS 4.8	SONNET 4.6	HAIKU 4.5	ANTHROPIC AVG
Classify	647ms	
4,712ms
(7.3×)
	
1,571ms
(2.4×)
	
1,839ms
(2.8×)
	
1,316ms
(2.0×)
	
2,360ms
(3.6×)

Extract	918ms	
5,522ms
(6.0×)
	
2,201ms
(2.4×)
	
2,447ms
(2.7×)
	
1,610ms
(1.8×)
	
2,945ms
(3.2×)

Summarize	1,426ms	
9,517ms
(6.7×)
	
3,900ms
(2.7×)
	
7,299ms
(5.1×)
	
4,102ms
(2.9×)
	
6,205ms
(4.4×)

Average	997ms	
6,584ms
(6.6×)
	
2,557ms
(2.6×)
	
3,862ms
(3.9×)
	
2,343ms
(2.4×)
	
3,836ms
(3.9×)

Latency follows the same shape: ScaleDown averages 997ms per call against 3,836ms for the Anthropic average, a 3.8× speedup that holds against every individual Claude model, not just the blended average.

Takeaway

ACCURACY

–
ScaleDown Summarize outperforms the Anthropic average by 8.22%.
–
ScaleDown Extract outperforms the Anthropic average by 13.33%.
–
ScaleDown Classify outperforms the Anthropic average by 2.29%.

COST

–
ScaleDown Summarize is 217× cheaper than the Anthropic average.
–
ScaleDown Extract is 91× cheaper than the Anthropic average.
–
ScaleDown Classify is 5,250× cheaper than the Anthropic average.

LATENCY

–
ScaleDown Summarize is 4.4× faster than the Anthropic average.
–
ScaleDown Extract is 3.2× faster than the Anthropic average.
–
ScaleDown Classify is 3.6× faster than the Anthropic average.
0.16

ADDITIONAL VISIBLE STATES / CHART VALUES
Chart-read values: Numeric values and scales shown in the visible benchmark charts are transcribed in the full visible text above; associated comparison tables are also included. Values were taken from displayed labels/axes, not estimated from bar lengths.

---8<--- page: scaledown-ai-benchmarks-scaledown-vs-deepseek ---8<---

Page URL: https://scaledown.ai/benchmarks/scaledown-vs-deepseek/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
ScaleDown vs DeepSeek

We benchmarked three ScaleDown models (Classify, Extract, Summarize) against DeepSeek V4 Pro and DeepSeek V4 Flash across three public benchmarks.

Benchmarks: QMSum, CUAD, and CLINC OOS.

ACCURACY

19.5%

better than DeepSeek avg

CLASSIFY

+20.75%

EXTRACT

+31.03%

SUMMARIZE

+6.73%

COST

9×

cheaper than DeepSeek avg

CLASSIFY

113×

EXTRACT

9×

SUMMARIZE

10×

LATENCY

4.1×

faster than DeepSeek avg

CLASSIFY

3.7×

EXTRACT

3.9×

SUMMARIZE

4.4×

Accuracy

Each ScaleDown model is purpose-built for one task. Summarize is compared on QMSum, Extract on CUAD, and Classify on CLINC OOS. DeepSeek V4 Pro and DeepSeek V4 Flash are run on the same benchmark and scored with the same metric.

Classify

CLINC OOS · Accuracy · higher is better

SD
Classify
DeepSeek
Avg
V4
Pro
V4
Flash
0.70
0.80
0.90
1.00
0.950
0.743
0.735
0.750
MODEL	ACCURACY
ScaleDown Classify	0.9500
DeepSeek Avg	
0.7425
(-20.75%)

└DeepSeek V4 Pro	
0.7350
(-21.50%)

└DeepSeek V4 Flash	
0.7500
(-20.00%)

Extract

CUAD · F1 · higher is better

SD
Extract
DeepSeek
Avg
V4
Pro
V4
Flash
0.25
0.35
0.45
0.55
0.65
0.612
0.302
0.307
0.296
MODEL	F1
ScaleDown Extract	0.6120
DeepSeek Avg	
0.3017
(-31.03%)

└DeepSeek V4 Pro	
0.3070
(-30.50%)

└DeepSeek V4 Flash	
0.2963
(-31.57%)

Summarize

QMSum · ROUGE-L · higher is better

SD
Summarize
DeepSeek
Avg
V4
Pro
V4
Flash
0.15
0.20
0.25
0.30
0.267
0.200
0.194
0.205
MODEL	ROUGE-L
ScaleDown Summarize	0.2670
DeepSeek Avg	
0.1997
(-6.73%)

└DeepSeek V4 Pro	
0.1939
(-7.31%)

└DeepSeek V4 Flash	
0.2054
(-6.16%)

Across the three measured tasks, ScaleDown's task-specific models average 19.5% higher accuracy than the DeepSeek lineup. The gap is widest on Extract (+31.0% on CUAD's legal-clause spans) and narrowest on Summarize (+6.7% on QMSum), where DeepSeek's general-purpose summaries are closer to ScaleDown's purpose-built output.

Cost

All costs are calculated per 1,000 calls from real per-call usage data returned by the API.

MOST ATTRACTIVE QUADRANT
ScaleDown
DeepSeek V4 Pro
DeepSeek V4 Flash
$0.01
$0.1
$1
$10
Cost per 1K calls
40
50
60
70
80
90
100
Accuracy score
(normalized vs. ScaleDown = 100 on each task)
SD Summarize
SD Extract
SD Classify
ScaleDown Avg
Pro Summarize
Pro Extract
Pro Classify
Flash Summarize
Flash Extract
Flash Classify
TASK	SCALEDOWN	DEEPSEEK V4 PRO	DEEPSEEK V4 FLASH	DEEPSEEK AVG
Classify	$0.0014	
$0.28
(200×)
	
$0.04
(26×)
	
$0.16
(113×)

Extract	$0.66	
$10.32
(16×)
	
$1.44
(2×)
	
$5.88
(9×)

Summarize	$0.70	
$12.11
(17×)
	
$1.55
(2×)
	
$6.83
(10×)

Average	$0.45	
$7.57
(17×)
	
$1.01
(2×)
	
$4.29
(9×)

ScaleDown costs 9× less than the DeepSeek average per 1,000 calls across the three measured tasks. The gap is largest on Classify (113×), where a small classifier stands in for a general-purpose chat model, and narrowest on Extract (9×).

Latency

Mean response time per call, measured in milliseconds. Lower is better.

ScaleDown
DeepSeek V4 Pro
DeepSeek V4 Flash
DeepSeek Avg
0
2,000
4,000
6,000
8,000
Classify
Extract
Summarize
TASK	SCALEDOWN	DEEPSEEK V4 PRO	DEEPSEEK V4 FLASH	DEEPSEEK AVG
Classify	647ms	
2,975ms
(4.6×)
	
1,801ms
(2.8×)
	
2,388ms
(3.7×)

Extract	918ms	
3,508ms
(3.8×)
	
3,692ms
(4.0×)
	
3,600ms
(3.9×)

Summarize	1,426ms	
7,747ms
(5.4×)
	
4,885ms
(3.4×)
	
6,316ms
(4.4×)

Average	997ms	
4,743ms
(4.8×)
	
3,459ms
(3.5×)
	
4,101ms
(4.1×)

ScaleDown is 4.1× faster than the DeepSeek average across the three measured tasks, holding a consistent edge over both individual models - DeepSeek V4 Pro runs 3.7–5.4× slower and V4 Flash 2.8–4.4× slower than ScaleDown depending on the task.

Takeaway

ACCURACY

–
ScaleDown Summarize outperforms the DeepSeek average by 6.73%.
–
ScaleDown Extract outperforms the DeepSeek average by 31.03%.
–
ScaleDown Classify outperforms the DeepSeek average by 20.75%.

COST

–
ScaleDown Summarize is 10× cheaper than the DeepSeek average.
–
ScaleDown Extract is 9× cheaper than the DeepSeek average.
–
ScaleDown Classify is 113× cheaper than the DeepSeek average.

LATENCY

–
ScaleDown Summarize is 4.4× faster than the DeepSeek average.
–
ScaleDown Extract is 3.9× faster than the DeepSeek average.
–
ScaleDown Classify is 3.7× faster than the DeepSeek average.
0.15

ADDITIONAL VISIBLE STATES / CHART VALUES
Chart-read values: Numeric values and scales shown in the visible benchmark charts are transcribed in the full visible text above; associated comparison tables are also included. Values were taken from displayed labels/axes, not estimated from bar lengths.

---8<--- page: scaledown-ai-benchmarks-scaledown-vs-gemini ---8<---

Page URL: https://scaledown.ai/benchmarks/scaledown-vs-gemini/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
ScaleDown vs Gemini

We benchmarked three ScaleDown models (Classify, Extract, Summarize) against Gemini 3.1 Pro, Gemini 3.5 Flash, and Gemini 3.1 Flash-Lite across three public benchmarks.

Benchmarks: QMSum, CUAD, and CLINC OOS.

ACCURACY

9.0%

better than Gemini avg

CLASSIFY

+2.10%

EXTRACT

+10.34%

SUMMARIZE

+14.70%

COST

29×

cheaper than Gemini avg

CLASSIFY

2,437×

EXTRACT

26×

SUMMARIZE

28×

LATENCY

8.3×

faster than Gemini avg

CLASSIFY

13.8×

EXTRACT

13.4×

SUMMARIZE

2.6×

Accuracy

Each ScaleDown model is purpose-built for one task. Summarize is compared on QMSum, Extract on CUAD, and Classify on CLINC OOS. All Gemini models are run on the same benchmark and scored with the same metric.

Classify

CLINC OOS · Accuracy · higher is better

SD
Classify
Gemini
Avg
3.1 Pro
3.5 Flash
3.1
Flash-Lite
0.84
0.88
0.92
0.96
1.00
0.950
0.929
0.949
0.897
0.941
MODEL	ACCURACY
ScaleDown Classify	0.9500
Gemini Avg	
0.9290
(-2.10%)

└Gemini 3.1 Pro	
0.9490
(-0.10%)

└Gemini 3.5 Flash	
0.8970
(-5.30%)

└Gemini 3.1 Flash-Lite	
0.9410
(-0.90%)

Extract

CUAD · F1 · higher is better

SD
Extract
Gemini
Avg
3.1 Pro
3.5 Flash
3.1
Flash-Lite
0.40
0.46
0.52
0.58
0.64
0.612
0.509
0.517
0.507
0.502
MODEL	F1
ScaleDown Extract	0.6120
Gemini Avg	
0.5090
(-10.34%)

└Gemini 3.1 Pro	
0.5166
(-9.54%)

└Gemini 3.5 Flash	
0.5068
(-10.52%)

└Gemini 3.1 Flash-Lite	
0.5025
(-10.95%)

Summarize

QMSum · ROUGE-L · higher is better

SD
Summarize
Gemini
Avg
3.1 Pro
3.5 Flash
3.1
Flash-Lite
0.04
0.10
0.16
0.22
0.28
0.267
0.120
0.097
0.081
0.182
MODEL	ROUGE-L
ScaleDown Summarize	0.2670
Gemini Avg	
0.1200
(-14.70%)

└Gemini 3.1 Pro	
0.0973
(-16.97%)

└Gemini 3.5 Flash	
0.0809
(-18.61%)

└Gemini 3.1 Flash-Lite	
0.1819
(-8.51%)

ScaleDown's task-specific models average 9% higher accuracy than Gemini's lineup, with the widest gap on Summarize (+14.7%) against QMSum. Extract follows a similar pattern (+10.3%), while Classify is the tightest race on the page: Gemini 3.1 Pro comes within a tenth of a percentage point of ScaleDown, which still edges ahead by the smallest margin on this page.

Cost

All costs are calculated per 1,000 calls using list pricing at the time of measurement.

MOST ATTRACTIVE QUADRANT
ScaleDown
Gemini 3.1 Pro
Gemini 3.5 Flash
Gemini 3.1 Flash-Lite
$0.01
$0.1
$1
$10
$100
Cost per 1K calls
30%
40%
50%
60%
70%
80%
90%
100%
Accuracy score
(standardized F1, ROUGE-L & accuracy metrics)
SD Classify
SD Summarize
SD Extract
ScaleDown Avg
Gemini Avg
Pro Classify
Pro Extract
Pro Summarize
Flash Classify
Flash Extract
Flash Summarize
Lite Classify
Lite Extract
Lite Summarize
TASK	SCALEDOWN	GEMINI 3.1 PRO	GEMINI 3.5 FLASH	GEMINI 3.1 FLASH-LITE	GEMINI AVG
Classify	$0.0014	
$5.89
(4,207×)
	
$4.16
(2,971×)
	
$0.19
(133×)
	
$3.41
(2,436×)

Extract	$0.66	
$28.01
(42×)
	
$21.24
(32×)
	
$2.86
(4×)
	
$17.37
(26×)

Summarize	$0.70	
$31.01
(44×)
	
$23.26
(33×)
	
$3.65
(5×)
	
$19.30
(28×)

Average	$0.45	
$21.64
(48×)
	
$16.22
(36×)
	
$2.23
(5×)
	
$13.36
(29×)

ScaleDown costs 29× less than the Gemini average per 1,000 calls. Summarize and Extract track close to that average (28× and 26×), but Classify pulls the number up sharply to 2,437×, since even Gemini's cheapest model isn't priced for a task this small.

Latency

Mean response time per call, measured in milliseconds. Lower is better.

ScaleDown
Gemini 3.1 Pro
Gemini 3.5 Flash
Gemini 3.1 Flash-Lite
Gemini Avg
0
4,000
8,000
12,000
16,000
20,000
Classify
Extract
Summarize
TASK	SCALEDOWN	GEMINI 3.1 PRO	GEMINI 3.5 FLASH	GEMINI 3.1 FLASH-LITE	GEMINI AVG
Classify	647ms	
9,427ms
(14.6×)
	
8,918ms
(13.8×)
	
8,351ms
(12.9×)
	
8,899ms
(13.8×)

Extract	918ms	
15,755ms
(17.2×)
	
19,603ms
(21.4×)
	
1,422ms
(1.5×)
	
12,260ms
(13.4×)

Summarize	1,426ms	
5,554ms
(3.9×)
	
2,775ms
(1.9×)
	
2,640ms
(1.9×)
	
3,656ms
(2.6×)

Average	997ms	
10,245ms
(10.3×)
	
10,432ms
(10.5×)
	
4,138ms
(4.2×)
	
8,272ms
(8.3×)

Latency is where the Gemini comparison is most dramatic, especially on Classify, where all three Gemini models run 13× to 14.6× slower than ScaleDown regardless of size. Extract shows a similar gap against Gemini 3.1 Pro and 3.5 Flash (17× and 21× slower), though Gemini 3.1 Flash-Lite stays much closer at 1.6×. Averaged across tasks, ScaleDown is 8.3× faster overall.

Takeaway

ACCURACY

–
ScaleDown Summarize outperforms the Gemini average by 14.70%.
–
ScaleDown Extract outperforms the Gemini average by 10.34%.
–
ScaleDown Classify outperforms the Gemini average by 2.10%.

COST

–
ScaleDown Summarize is 28× cheaper than the Gemini average.
–
ScaleDown Extract is 26× cheaper than the Gemini average.
–
ScaleDown Classify is 2,437× cheaper than the Gemini average.

LATENCY

–
ScaleDown Summarize is 2.6× faster than the Gemini average.
–
ScaleDown Extract is 13.4× faster than the Gemini average.
–
ScaleDown Classify is 13.8× faster than the Gemini average.
0.04

ADDITIONAL VISIBLE STATES / CHART VALUES
Chart-read values: Numeric values and scales shown in the visible benchmark charts are transcribed in the full visible text above; associated comparison tables are also included. Values were taken from displayed labels/axes, not estimated from bar lengths.

---8<--- page: scaledown-ai-benchmarks-scaledown-vs-gliner ---8<---

Page URL: https://scaledown.ai/benchmarks/scaledown-vs-gliner/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
404

Oops! Page not found

Return to Home

---8<--- page: scaledown-ai-benchmarks-scaledown-vs-grok ---8<---

Page URL: https://scaledown.ai/benchmarks/scaledown-vs-grok/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
ScaleDown vs Grok

We benchmarked three ScaleDown models (Classify, Extract, Summarize) against Grok 4.3 and Grok 4.2 across three public benchmarks.

Benchmarks: QMSum, CUAD, and CLINC OOS.

ACCURACY

7.93%

better than Grok avg

CLASSIFY

+1.45%

EXTRACT

+12.30%

SUMMARIZE

+10.05%

COST

24×

cheaper than Grok avg

CLASSIFY

1,161×

EXTRACT

22×

SUMMARIZE

25×

LATENCY

2.2×

faster than Grok avg

CLASSIFY

2.3×

EXTRACT

2.3×

SUMMARIZE

2.1×

Accuracy

Each ScaleDown model is purpose-built for one task. Summarize is compared on QMSum, Extract on CUAD, and Classify on CLINC OOS. All Grok models are run on the same benchmark and scored with the same metric.

Classify

CLINC OOS · Accuracy · higher is better

SD
Classify
Grok
Avg
Grok 4.3
Grok 4.2
0.84
0.88
0.92
0.96
1.00
0.950
0.936
0.939
0.932
MODEL	ACCURACY
ScaleDown Classify	0.9500
Grok Avg	
0.9360
(-1.45%)

└Grok 4.3	
0.9390
(-1.10%)

└Grok 4.2	
0.9320
(-1.80%)

Extract

CUAD · F1 · higher is better

SD
Extract
Grok
Avg
Grok 4.3
Grok 4.2
0.40
0.46
0.52
0.58
0.64
0.612
0.489
0.484
0.494
MODEL	F1
ScaleDown Extract	0.6120
Grok Avg	
0.4890
(-12.30%)

└Grok 4.3	
0.4840
(-12.80%)

└Grok 4.2	
0.4940
(-11.80%)

Summarize

QMSum · ROUGE-L · higher is better

SD
Summarize
Grok
Avg
Grok 4.3
Grok 4.2
0.04
0.10
0.16
0.22
0.28
0.267
0.167
0.168
0.165
MODEL	ROUGE-L
ScaleDown Summarize	0.2670
Grok Avg	
0.1670
(-10.05%)

└Grok 4.3	
0.1680
(-9.90%)

└Grok 4.2	
0.1650
(-10.20%)

ScaleDown's task-specific models average 7.9% higher accuracy than Grok's lineup, with the widest gap on Extract (+12.3%) and a similarly strong lead on Summarize (+10.1%). Classify is the closest race on the page: Grok 4.3 trails by about a point and 4.2 by under two, with ScaleDown holding a narrow but consistent lead.

Cost

All costs are calculated per 1,000 calls using list pricing at the time of measurement.

MOST ATTRACTIVE QUADRANT
ScaleDown
Grok 4.3
Grok 4.2
$0.01
$0.1
$1
$10
$100
Cost per 1K calls
30%
40%
50%
60%
70%
80%
90%
100%
Accuracy score
(standardized F1, ROUGE-L & accuracy metrics)
SD Classify
ScaleDown Avg
SD Extract
SD Summarize
Grok Avg
4.3 Classify
4.3 Extract
4.3 Summarize
4.2 Classify
4.2 Extract
4.2 Summarize
TASK	SCALEDOWN	GROK 4.3	GROK 4.2	GROK AVG
Classify	$0.0014	
$2.13
(1,521×)
	
$1.12
(800×)
	
$1.63
(1,161×)

Extract	$0.66	
$14.76
(22×)
	
$13.78
(21×)
	
$14.27
(22×)

Summarize	$0.70	
$17.60
(25×)
	
$16.80
(24×)
	
$17.20
(25×)

Average	$0.45	
$11.50
(25×)
	
$10.57
(23×)
	
$11.03
(24×)

ScaleDown costs 24× less than the Grok average per 1,000 calls, ranging from 22× on Extract to over 1,161× on Classify, where a small classifier stands in for a general-purpose chat model.

Latency

Mean response time per call, measured in milliseconds. Lower is better.

ScaleDown
Grok 4.3
Grok 4.2
Grok Avg
0
1,000
2,000
3,000
4,000
5,000
Classify
Extract
Summarize
TASK	SCALEDOWN	GROK 4.3	GROK 4.2	GROK AVG
Classify	647ms	
2,331ms
(3.6×)
	
694ms
(1.1×)
	
1,513ms
(2.3×)

Extract	918ms	
3,302ms
(3.6×)
	
861ms
(0.9×)
	
2,082ms
(2.3×)

Summarize	1,426ms	
4,410ms
(3.1×)
	
1,681ms
(1.2×)
	
3,046ms
(2.1×)

Average	997ms	
3,348ms
(3.4×)
	
1,079ms
(1.1×)
	
2,213ms
(2.2×)

Latency is the closest metric on this page. Against the blended average, ScaleDown is 2.2× faster, and it holds a narrow edge even against Grok 4.2 alone, though 4.2 nudges ahead by under 60ms on Extract specifically. Grok 4.3 is where the real latency gap shows up, running 3 to 3.6× slower than ScaleDown across every task.

Takeaway

ACCURACY

–
ScaleDown Summarize outperforms the Grok average by 10.05%.
–
ScaleDown Extract outperforms the Grok average by 12.30%.
–
ScaleDown Classify outperforms the Grok average by 1.45%.

COST

–
ScaleDown Summarize is 25× cheaper than the Grok average.
–
ScaleDown Extract is 22× cheaper than the Grok average.
–
ScaleDown Classify is 1,161× cheaper than the Grok average.

LATENCY

–
ScaleDown Summarize is 2.1× faster than the Grok average.
–
ScaleDown Extract is 2.3× faster than the Grok average.
–
ScaleDown Classify is 2.3× faster than the Grok average.
0.04

ADDITIONAL VISIBLE STATES / CHART VALUES
Chart-read values: Numeric values and scales shown in the visible benchmark charts are transcribed in the full visible text above; associated comparison tables are also included. Values were taken from displayed labels/axes, not estimated from bar lengths.

---8<--- page: scaledown-ai-benchmarks-scaledown-vs-kimi ---8<---

Page URL: https://scaledown.ai/benchmarks/scaledown-vs-kimi/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
ScaleDown vs Kimi

We benchmarked ScaleDown against Moonshot AI's Kimi K3, Kimi K2.6, and Kimi K2 on three public benchmarks.

Benchmarks: QMSum, CUAD, and CLINC OOS.

ACCURACY

13.2%

better than Kimi avg

CLASSIFY

+0.50%

EXTRACT

+27.83%

SUMMARIZE

+11.44%

COST

30×

cheaper than Kimi avg

CLASSIFY

626×

EXTRACT

23×

SUMMARIZE

36×

LATENCY

7.3×

faster than Kimi avg

CLASSIFY

2.7×

EXTRACT

4.3×

SUMMARIZE

11.4×

Accuracy

Summarize is compared on QMSum (ROUGE-L), Classify on CLINC OOS (accuracy), and Extract on CUAD (F1). Kimi K3, Kimi K2.6, and Kimi K2 are run on the same benchmark and scored with the same metric as ScaleDown.

Classify

CLINC OOS · Accuracy · higher is better

SD
Classify
Kimi
Avg
Kimi
K3
Kimi
K2.6
Kimi
K2
0.00
0.25
0.50
0.75
1.00
0.950
0.945
0.895
0.955
0.985
MODEL	ACCURACY
ScaleDown Classify	0.9500
Kimi Avg	
0.9450
(-0.50%)

└Kimi K3	
0.8950
(-5.50%)

└Kimi K2.6	
0.9550
(+0.50%)

└Kimi K2	
0.9850
(+3.50%)

Summarize

QMSum · ROUGE-L · higher is better

SD
Summarize
Kimi
Avg
Kimi
K3
Kimi
K2.6
Kimi
K2
0.00
0.10
0.20
0.30
0.267
0.153
0.164
0.127
0.167
MODEL	ROUGE-L
ScaleDown Summarize	0.2670
Kimi Avg	
0.1526
(-11.44%)

└Kimi K3	
0.1640
(-10.30%)

└Kimi K2.6	
0.1265
(-14.05%)

└Kimi K2	
0.1673
(-9.97%)

Extract

CUAD · F1 · higher is better

SD
Extract
Kimi
Avg
Kimi
K3
Kimi
K2.6
Kimi
K2
0.00
0.15
0.30
0.45
0.60
0.612
0.334
0.330
0.346
0.325
MODEL	F1
ScaleDown Extract	0.6120
Kimi Avg	
0.3337
(-27.83%)

└Kimi K3	
0.3300
(-28.20%)

└Kimi K2.6	
0.3460
(-26.60%)

└Kimi K2	
0.3250
(-28.70%)

On Summarize, ScaleDown leads all three Kimi models by a wide margin (0.267 ROUGE-L vs. 0.126-0.167). On Classify, the result flips: both Kimi K2.6 (0.955) and Kimi K2 (0.985) actually beat ScaleDown's 0.950, and Kimi K3 lands close behind at 0.895 once reasoning is disabled so the label survives. Kimi's general-purpose intent classification is strong across the board here. On Extract, ScaleDown leads all three Kimi models by a wide margin too (0.612 F1 vs. 0.325-0.346), though the gap is narrower than on Summarize - all three Kimi models land within a few points of each other on CUAD's contract-clause spans, with Kimi K2.6 scoring marginally highest.

Cost

All costs are calculated per 1,000 calls from real per-call usage data returned by the OpenRouter API.

MOST ATTRACTIVE QUADRANT
ScaleDown
Kimi K3
Kimi K2.6
Kimi K2
$0.01
$0.1
$1
$10
$100
Cost per 1K calls
0
25
50
75
100
Accuracy score
(normalized vs. ScaleDown = 100 on each task)
SD Classify
SD Summarize
SD Extract
K3 Classify
K3 Summarize
K3 Extract
K2.6 Classify
K2.6 Summarize
K2.6 Extract
K2 Classify
K2 Summarize
K2 Extract
TASK	SCALEDOWN	KIMI K3	KIMI K2.6	KIMI K2	KIMI AVG
Classify	$0.0014	
$1.80
(1284×)
	
$0.52
(374×)
	
$0.31
(223×)
	
$0.88
(627×)

Extract	$0.66	
$29.69
(45×)
	
$7.31
(11×)
	
$8.12
(12×)
	
$15.04
(23×)

Summarize	$0.70	
$51.42
(73×)
	
$16.63
(24×)
	
$8.24
(12×)
	
$25.43
(36×)

Average	$0.45	
$27.64
(61×)
	
$8.15
(18×)
	
$5.56
(12×)
	
$13.78
(30×)

On Summarize, ScaleDown is far cheaper than every Kimi model ($0.70 vs. $8.24-$51.42 per 1,000 calls), and Kimi K3 in particular is expensive here since its long context and reasoning overhead push up completion tokens. On Classify, ScaleDown's $0.0014 is cheaper than all three Kimi models ($0.312-$1.80), though the gap is far smaller than on Summarize. On Extract, ScaleDown's $0.66 is again cheaper than every Kimi model ($7.31-$29.69 per 1,000 calls), with Kimi K3 costing roughly 4x Kimi K2.6 and Kimi K2 on the same CUAD contracts, largely due to its higher per-token pricing rather than longer completions.

Latency

Mean response time per call, measured in milliseconds. Lower is better.

ScaleDown
Kimi K3
Kimi K2.6
Kimi K2
0
6,000
12,000
18,000
24,000
Classify
Extract
Summarize
TASK	SCALEDOWN	KIMI K3	KIMI K2.6	KIMI K2	KIMI AVG
Classify	647ms	
2,582ms
(4.0×)
	
1,292ms
(2.0×)
	
1,443ms
(2.2×)
	
1,772ms
(2.7×)

Extract	918ms	
5,369ms
(5.8×)
	
3,516ms
(3.8×)
	
2,879ms
(3.1×)
	
3,921ms
(4.3×)

Summarize	1,426ms	
13,121ms
(9.2×)
	
27,248ms
(19.1×)
	
8,487ms
(6.0×)
	
16,285ms
(11.4×)

Average	997ms	
7,024ms
(7.0×)
	
10,685ms
(10.7×)
	
4,270ms
(4.3×)
	
7,326ms
(7.3×)

ScaleDown is faster than every Kimi model on all three measured tasks, at 1,426ms vs. 8,487-27,248ms on Summarize, 647ms vs. 1,292-2,582ms on Classify, and 918ms vs. 2,879-5,369ms on Extract, where Kimi K3's reasoning overhead makes it the slowest of the three even on CUAD's short contract excerpts.

Takeaway

ACCURACY

–
ScaleDown Summarize outperforms the Kimi average by 11.44 percentage points.
–
ScaleDown Extract outperforms the Kimi average by 27.83 percentage points.
–
ScaleDown Classify outperforms the Kimi average by 0.50 percentage points.

COST

–
ScaleDown Summarize is 36× cheaper than the Kimi average.
–
ScaleDown Extract is 23× cheaper than the Kimi average.
–
ScaleDown Classify is 626× cheaper than the Kimi average.

LATENCY

–
ScaleDown Summarize is 11.4× faster than the Kimi average.
–
ScaleDown Extract is 4.3× faster than the Kimi average.
–
ScaleDown Classify is 2.7× faster than the Kimi average.
0.15

ADDITIONAL VISIBLE STATES / CHART VALUES
Chart-read values: Numeric values and scales shown in the visible benchmark charts are transcribed in the full visible text above; associated comparison tables are also included. Values were taken from displayed labels/axes, not estimated from bar lengths.

---8<--- page: scaledown-ai-benchmarks-scaledown-vs-openai ---8<---

Page URL: https://scaledown.ai/benchmarks/scaledown-vs-openai/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
ScaleDown vs OpenAI

We benchmarked all four ScaleDown models (Classify, Extract, Summarize, Compress) against GPT-5.5, GPT-5.4 Mini, and GPT-5.4 Nano across four public benchmarks.

Benchmarks: FinanceBench, QMSum, CUAD and CLINC OOS.

ACCURACY

8.72%

better than OpenAI avg

CLASSIFY

+5.40%

EXTRACT

+14.40%

SUMMARIZE

+8.83%

COMPRESS

+6.23%

COST

89×

cheaper than OpenAI avg

CLASSIFY

1,810×

EXTRACT

35×

SUMMARIZE

41×

COMPRESS

138×

LATENCY

2.4×

faster than OpenAI avg

CLASSIFY

2.6×

EXTRACT

3.3×

SUMMARIZE

2.7×

COMPRESS

1.8×

Accuracy

Each ScaleDown model is purpose-built for one task. Compress is compared on FinanceBench, Summarize on QMSum, Classify on CLINC OOS, and Extract on CUAD. OpenAI models are run on the same benchmark and scored with the same metric.

Classify

CLINC OOS · Accuracy · higher is better

ScaleDown Classify
OpenAI Avg
GPT-5.5
GPT-5.4 Mini
GPT-5.4 Nano
0.84
0.87
0.90
0.93
0.96
0.950
0.896
0.898
0.915
0.875
MODEL	ACCURACY
ScaleDown Classify	0.950
OpenAI Avg	
0.896
(-5.40%)

└GPT-5.5	
0.898
(-5.20%)

└GPT-5.4 Mini	
0.915
(-3.50%)

└GPT-5.4 Nano	
0.875
(-7.50%)

Extract

CUAD · F1 · higher is better

ScaleDown Extract
OpenAI Avg
GPT-5.5
GPT-5.4 Mini
GPT-5.4 Nano
0.40
0.46
0.52
0.58
0.64
0.612
0.468
0.504
0.468
0.432
MODEL	F1
ScaleDown Extract	0.612
OpenAI Avg	
0.468
(-14.40%)

└GPT-5.5	
0.504
(-10.80%)

└GPT-5.4 Mini	
0.468
(-14.40%)

└GPT-5.4 Nano	
0.432
(-18.00%)

Summarize

QMSum · ROUGE-L · higher is better

ScaleDown Summarize
OpenAI Avg
GPT-5.5
GPT-5.4 Mini
GPT-5.4 Nano
0.16
0.19
0.22
0.25
0.28
0.267
0.179
0.179
0.186
0.171
MODEL	ROUGE-L
ScaleDown Summarize	0.267
OpenAI Avg	
0.179
(-8.83%)

└GPT-5.5	
0.179
(-8.80%)

└GPT-5.4 Mini	
0.186
(-8.10%)

└GPT-5.4 Nano	
0.171
(-9.60%)

Compress

FinanceBench · F1 · higher is better

ScaleDown Compress
OpenAI Avg
GPT-5.5
GPT-5.4 Mini
GPT-5.4 Nano
0.15
0.20
0.25
0.30
0.35
0.311
0.249
0.307
0.239
0.200
MODEL	F1
ScaleDown Compress	0.311
OpenAI Avg	
0.249
(-6.23%)

└GPT-5.5	
0.307
(-0.40%)

└GPT-5.4 Mini	
0.239
(-7.20%)

└GPT-5.4 Nano	
0.200
(-11.10%)

ScaleDown's four task-specific models average 8.7% higher accuracy than the OpenAI lineup. Extract shows the widest gap (+14.4%) on CUAD's contract-heavy benchmark, while Compress is the closest matchup on the page: GPT-5.5 comes within half a point of ScaleDown on FinanceBench, though OpenAI's smaller models trail well behind. Classify is a clean sweep, ScaleDown outscores every individual GPT model, not just the blended average.

Cost

All costs are calculated per 1,000 calls using list pricing at the time of measurement.

MOST ATTRACTIVE QUADRANT
ScaleDown
GPT-5.5
GPT-5.4 Mini
GPT-5.4 Nano
$0.1
$0.3
$1
$3
$10
$30
$100
$300
Cost per 1K calls
65%
70%
75%
80%
85%
90%
95%
100%
Accuracy score
(standardized F1, ROUGE-L & accuracy metrics)
SD Classify
SD Summarize
SD Extract
SD Compress
ScaleDown Avg
OpenAI Avg
GPT-5.5 Compress
GPT-5.5 Classify
GPT-5.5 Extract
GPT-5.5 Summarize
Mini Classify
Mini Summarize
Mini Extract
Mini Compress
Nano Classify
Nano Summarize
Nano Extract
Nano Compress
TASK	SCALEDOWN	GPT-5.5	GPT-5.4 MINI	GPT-5.4 NANO	OPENAI AVG
Classify	$0.0014	
$7.20
(5,143×)
	
$0.32
(229×)
	
$0.08
(57×)
	
$2.53
(1,810×)

Extract	$0.66	
$58.86
(89×)
	
$8.40
(13×)
	
$2.22
(3×)
	
$23.16
(35×)

Summarize	$0.70	
$72.34
(103×)
	
$10.34
(15×)
	
$2.80
(4×)
	
$28.49
(41×)

Compress	$1.37	
$466.00
(340×)
	
$81.00
(59×)
	
$21.20
(15×)
	
$189.40
(138×)

Average	$0.68	
$151.10
(221×)
	
$25.02
(37×)
	
$6.58
(10×)
	
$60.90
(89×)

ScaleDown runs 89× cheaper than OpenAI on average per 1,000 calls. The gap is largest on Classify (1,810×), where a small classifier replaces a general-purpose chat model, and narrowest on Extract (35×), where GPT-5.4 Nano's lower list price closes some of the distance.

Latency

Mean response time per call, measured in milliseconds. Lower is better.

ScaleDown
GPT-5.5
GPT-5.4 Mini
GPT-5.4 Nano
OpenAI Avg
0
2,000
4,000
6,000
8,000
Classify
Extract
Summarize
Compress
TASK	SCALEDOWN	GPT-5.5	GPT-5.4 MINI	GPT-5.4 NANO	OPENAI AVG
Classify	647ms	
3,592ms
(5.6×)
	
694ms
(1.1×)
	
697ms
(1.1×)
	
1,661ms
(2.6×)

Extract	918ms	
6,083ms
(6.6×)
	
1,042ms
(1.1×)
	
1,860ms
(2.0×)
	
2,995ms
(3.3×)

Summarize	1,426ms	
7,805ms
(5.5×)
	
1,856ms
(1.3×)
	
1,759ms
(1.2×)
	
3,807ms
(2.7×)

Compress	2,658ms	
8,217ms
(3.1×)
	
3,087ms
(1.2×)
	
3,426ms
(1.3×)
	
4,910ms
(1.8×)

Average	1,412ms	
6,424ms
(4.5×)
	
1,670ms
(1.2×)
	
1,936ms
(1.4×)
	
3,343ms
(2.4×)

Latency tells a more nuanced story. Against GPT-5.5, ScaleDown is dramatically faster, from 3.1× on Compress up to 6.6× on Extract. GPT-5.4 Mini stays close throughout, landing within roughly 1.1× to 1.3× of ScaleDown on every task, and Nano is usually just as close, though it spikes to 2× slower specifically on Extract. The 2.4× average is driven mostly by GPT-5.5 running slow across the board.

Takeaway

ACCURACY

–
ScaleDown Compress outperforms the OpenAI average by 6.23%.
–
ScaleDown Summarize outperforms the OpenAI average by 8.83%.
–
ScaleDown Extract outperforms the OpenAI average by 14.40%.
–
ScaleDown Classify outperforms the OpenAI average by 5.40%.

COST

–
ScaleDown Compress is 138× cheaper than the OpenAI average.
–
ScaleDown Summarize is 41× cheaper than the OpenAI average.
–
ScaleDown Extract is 35× cheaper than the OpenAI average.
–
ScaleDown Classify is 1,810× cheaper than the OpenAI average.

LATENCY

–
ScaleDown Compress is 1.8× faster than the OpenAI average.
–
ScaleDown Summarize is 2.7× faster than the OpenAI average.
–
ScaleDown Extract is 3.3× faster than the OpenAI average.
–
ScaleDown Classify is 2.6× faster than the OpenAI average.
0.15

ADDITIONAL VISIBLE STATES / CHART VALUES
Visible chart values and accompanying table values are transcribed in the page text above; no chart value had to be estimated from bar height.

Chart-read values: Numeric values and scales shown in the visible benchmark charts are transcribed in the full visible text above; associated comparison tables are also included. Values were taken from displayed labels/axes, not estimated from bar lengths.

---8<--- page: scaledown-ai-benchmarks-scaledown-vs-qwen ---8<---

Page URL: https://scaledown.ai/benchmarks/scaledown-vs-qwen/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
ScaleDown vs Qwen

We benchmarked three ScaleDown models (Classify, Extract, Summarize) against Qwen3.8 Max, Qwen3.8 27B, and Qwen3.5 4B across three public benchmarks.

Benchmarks: QMSum, CUAD, and CLINC OOS.

ACCURACY

16.71%

better than Qwen avg

CLASSIFY

+9.12%

EXTRACT

+31.98%

SUMMARIZE

+9.04%

COST

24×

cheaper than Qwen avg

CLASSIFY

761×

EXTRACT

18×

SUMMARIZE

28×

LATENCY

13.9×

faster than Qwen avg

CLASSIFY

7.2×

EXTRACT

26.1×

SUMMARIZE

9.2×

Accuracy

Each ScaleDown model is purpose-built for one task. Summarize is compared on QMSum, Extract on CUAD, and Classify on CLINC OOS. Qwen3.8 Max, Qwen3.8 27B, and Qwen3.5 4B are run on the same benchmark and scored with the same metric.

Classify

CLINC OOS · Accuracy · higher is better

SD
Classify
Qwen
Avg
3.8
Max
3.8
27B
3.5
4B
0.45
0.60
0.75
0.90
1.00
0.950
0.859
0.850
0.868
0.892
MODEL	ACCURACY
ScaleDown Classify	0.9500
Qwen Avg	
0.8590
(-9.12%)

└Qwen3.8 Max	
0.8500
(-10.00%)

└Qwen3.8 27B	
0.8675
(-8.25%)

└Qwen3.5 4B	
0.8925
(-5.75%)

Extract

CUAD · F1 · higher is better

SD
Extract
Qwen
Avg
3.8
Max
3.8
27B
3.5
4B
0.25
0.35
0.45
0.55
0.65
0.612
0.292
0.282
0.302
0.295
MODEL	F1
ScaleDown Extract	0.6120
Qwen Avg	
0.2920
(-31.98%)

└Qwen3.8 Max	
0.2820
(-33.00%)

└Qwen3.8 27B	
0.3024
(-30.96%)

└Qwen3.5 4B	
0.2951
(-31.69%)

Summarize

QMSum · ROUGE-L · higher is better

SD
Summarize
Qwen
Avg
3.8
Max
3.8
27B
3.5
4B
0.15
0.20
0.25
0.30
0.267
0.177
0.167
0.186
0.154
MODEL	ROUGE-L
ScaleDown Summarize	0.2670
Qwen Avg	
0.1770
(-9.04%)

└Qwen3.8 Max	
0.1674
(-9.96%)

└Qwen3.8 27B	
0.1859
(-8.11%)

└Qwen3.5 4B	
0.1541
(-11.29%)

Across the three measured tasks, ScaleDown's task-specific models average 16.71% higher accuracy than the Qwen lineup. The gap is widest on Extract (+31.98% on CUAD's legal-clause spans), followed by Summarize (+9.04%) and Classify (+9.12%). Qwen3.5 4B is the least accurate of the three Qwen models on Summarize, but the most accurate of the three on Classify once it's run without forced reasoning, since a short one-sentence justification per call outperforms a long thinking trace that too often got cut off before naming a label. Qwen3.8 27B still edges out Qwen3.8 Max on raw accuracy despite being the smaller, cheaper model, since Max's mandatory reasoning overhead doesn't translate into better answers on these tasks.

Cost

All costs are calculated per 1,000 calls. Max and 27B use real per-call usage data returned by the OpenRouter API; Qwen3.5 4B is estimated from measured GPU wall-clock time on a Modal A100 at Modal's published per-second rate, since it is self-hosted rather than billed per call.

MOST ATTRACTIVE QUADRANT
ScaleDown
Qwen3.8 Max
Qwen3.8 27B
Qwen3.5 4B
$0.01
$0.1
$1
$10
Cost per 1K calls
40
50
60
70
80
90
100
Accuracy score
(normalized vs. ScaleDown = 100 on each task)
SD Summarize
SD Extract
SD Classify
ScaleDown Avg
Max Summarize
Max Extract
Max Classify
27B Summarize
27B Extract
27B Classify
4B Summarize
4B Extract
4B Classify
TASK	SCALEDOWN	QWEN3.8 MAX	QWEN3.8 27B	QWEN3.5 4B	QWEN AVG
Classify	$0.0014	
$1.94
(1386×)
	
$0.19
(136×)
	
$0.59
(421×)
	
$0.91
(648×)

Extract	$0.66	
$17.76
(27×)
	
$5.52
(8×)
	
$0.79
(1×)
	
$8.02
(12×)

Summarize	$0.70	
$32.83
(47×)
	
$6.56
(9×)
	
$1.09
(2×)
	
$13.49
(19×)

Average	$0.45	
$17.51
(39×)
	
$4.09
(9×)
	
$0.82
(2×)
	
$10.80
(24×)

ScaleDown costs 24× less than the Qwen average per 1,000 calls across the three measured tasks. The gap is largest on Classify (761×), where Max and 27B's mandatory reasoning still burns hundreds of tokens on a one-word intent label, and narrowest on Extract (18×). Qwen3.5 4B is the cheapest Qwen model on Summarize and Extract, since it runs on a single self-hosted GPU instead of paying per-token through an API; on Classify, Qwen3.8 27B is cheapest, as its short completions undercut even 4B's now-brief wall-clock time. On Extract, ScaleDown remains cheaper than 4B despite 4B's self-hosted pricing, and wins by a wide margin on accuracy and latency there too.

Latency

Mean response time per call, measured in milliseconds. Lower is better.

ScaleDown
Qwen3.8 Max
Qwen3.8 27B
Qwen3.5 4B
Qwen Avg
0
7,000
14,000
21,000
28,000
35,000
Classify
Extract
Summarize
TASK	SCALEDOWN	QWEN3.8 MAX	QWEN3.8 27B	QWEN3.5 4B	QWEN AVG
Classify	647ms	
4,468ms
(6.9×)
	
4,825ms
(7.5×)
	
1,016ms
(1.6×)
	
3,436ms
(5.3×)

Extract	918ms	
13,747ms
(15.0×)
	
34,181ms
(37.2×)
	
3,393ms
(3.7×)
	
17,107ms
(18.6×)

Summarize	1,426ms	
16,420ms
(11.5×)
	
9,726ms
(6.8×)
	
4,985ms
(3.5×)
	
10,377ms
(7.3×)

Average	997ms	
11,545ms
(11.6×)
	
16,244ms
(16.3×)
	
3,131ms
(3.1×)
	
13,895ms
(13.9×)

ScaleDown is 13.9× faster than the Qwen average across the three measured tasks. The gap is largest on Extract (26.1×), where Qwen3.8 27B in particular has a long, noisy latency tail, and narrowest on Classify (7.2×): Max and 27B's mandatory reasoning still slows every call, though Qwen3.5 4B, now run without forced reasoning, closes most of that gap on its own. Qwen3.5 4B is the fastest of the three Qwen models on every task, both because it is a smaller model and because it runs locally rather than through an extra network hop to OpenRouter. On Classify, disabling forced reasoning cut its latency from over 10 seconds down to roughly 1 second, though it is still slower than ScaleDown's 647ms there.

Takeaway

ACCURACY

–
ScaleDown Summarize outperforms the Qwen average by 9.04%.
–
ScaleDown Extract outperforms the Qwen average by 31.98%.
–
ScaleDown Classify outperforms the Qwen average by 9.12%.

COST

–
ScaleDown Summarize is 28× cheaper than the Qwen average.
–
ScaleDown Extract is 18× cheaper than the Qwen average.
–
ScaleDown Classify is 761× cheaper than the Qwen average.

LATENCY

–
ScaleDown Summarize is 9.2× faster than the Qwen average.
–
ScaleDown Extract is 26.1× faster than the Qwen average.
–
ScaleDown Classify is 7.2× faster than the Qwen average.
0.15

ADDITIONAL VISIBLE STATES / CHART VALUES
Chart-read values: Numeric values and scales shown in the visible benchmark charts are transcribed in the full visible text above; associated comparison tables are also included. Values were taken from displayed labels/axes, not estimated from bar lengths.

---8<--- page: scaledown-ai-benchmarks ---8<---

Page URL: https://scaledown.ai/benchmarks/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
ScaleDown Benchmarks

Task-specific models benchmarked against leading models across accuracy, cost and latency.

ScaleDown vs OpenAI
GPT-5.5 · GPT-5.4 Mini · GPT-5.4 Nano
→
ScaleDown vs Anthropic
Fable 5 · Opus 4.8 · Sonnet 4.6 · Haiku 4.5
→
ScaleDown vs Gemini
3.1 Pro · 3.5 Flash · 3.1 Flash-Lite
→
ScaleDown vs Grok
Grok 4.3 · Grok 4.2
→
ScaleDown vs DeepSeek
DeepSeek V4 Pro · DeepSeek V4 Flash
→
ScaleDown vs Qwen
Qwen3.8 Max · Qwen3.8 27B
→
ScaleDown vs Kimi
Kimi K3 · Kimi K2.6 · Kimi K2
→

---8<--- page: scaledown-ai-blog-benchmarking-scaledowns-classification ---8<---

Page URL: https://scaledown.ai/blog/benchmarking-scaledowns-classification/
Dates shown (publication/updated/changelog): May 13, 2026

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
How We Benchmark Classify for Model Routing
Soham Chatterje
·
May 13, 2026

Model routing is becoming a standard pattern in production LLM systems. Instead of sending every query to a single frontier model, a router classifies the incoming request and directs it to the most appropriate model or pipeline. The routing decision might be based on task complexity, domain, required capabilities, or cost constraints.

The router sits upstream of everything else. It’s the highest-volume, most latency-sensitive component in the pipeline, and most teams are still using a frontier LLM for it, burning tokens on a classification task that doesn’t need generative capabilities at all.

The Benchmark

The task is multi-class intent classification: given an input query, classify it into the correct routing category. This mirrors the real-world pattern where an orchestration layer decides which downstream model, tool, or pipeline should handle a given request.

We evaluate on accuracy (percentage of queries correctly classified) and total cost for the benchmark run. Both matter for production use cases: a cheaper model that misroutes 20% of queries creates downstream costs far exceeding any token savings.

Results
ScaleDown is the most accurate

At 90.53%, it outperforms both GPT-5.4 Mini (+3.46 points) and GPT-5.4 Nano (+10.86 points). This isn’t surprising if you’ve worked with task-specific models before: a small model trained specifically for classification on a well-defined taxonomy will typically beat a generalist model that has to infer the classification schema from a prompt.

The cost difference

ScaleDown’s total benchmark cost was $0.0008, roughly 50x cheaper than GPT-5.4 Nano and 200x cheaper than Mini. At production volumes, this difference compounds fast. A system processing 1M classification calls per day would spend roughly $1,000/day with Mini, $250/day with Nano, and $0.50/day with ScaleDown.

No accuracy-cost tradeoff

Typically, when you move from a larger model to a smaller one, you accept lower accuracy for lower cost. Here, the smallest and cheapest model is also the most accurate. This is the core argument for task-specific SLMs: when the task is well-defined and doesn’t require generation, a purpose-built classifier dominates on both axes.

Why LLMs Underperform on Classification

It’s worth understanding why GPT-5.4 Nano and Mini score lower on what seems like a straightforward task. There are a few factors at play.

First, LLMs solve classification indirectly. They generate a text response that happens to contain a class label. The model has to parse the prompt, understand the taxonomy, reason about the mapping, and produce the right token. A classifier scores each class directly and picks the highest one.

Second, LLMs are sensitive to prompt engineering. The classification accuracy of a frontier model depends heavily on how the taxonomy is described, how examples are formatted, and how the output format is specified. Small changes in the system prompt can swing accuracy by several points.

Third, generalist models over-interpret. When a user query contains domain-specific language, a frontier model’s broad knowledge can cause it to infer more nuance than the routing taxonomy requires. A query about “Roth conversions” might get classified into a tax optimization category when the routing schema just needs “retirement planning.”

Where This Matters

Model routing is the most obvious use case, but the same classification SLM applies anywhere you’re using an LLM for what is fundamentally a categorization task:

Intent classification in conversational AI. When a financial planning assistant needs to determine whether a user is asking about retirement, tax optimization, or insurance, that’s a routing decision, not a generation task. We covered this use case in depth in our previous post on intent classification for financial planners.

Content moderation and filtering. Classifying user inputs as safe/unsafe, on-topic/off-topic, or into content categories before they reach downstream processing.

Document triage. Routing incoming documents to the correct processing pipeline based on document type, urgency, or department.

In all of these, the classification call is high-volume, latency-sensitive, and doesn’t require text generation. Replacing the LLM with a task-specific classifier improves all three dimensions simultaneously: accuracy goes up, cost goes down, latency drops.

Key Takeaways

Classification is the wrong task for a generalist LLM. When the job is mapping inputs to a fixed rubric, a task-specific SLM is faster, cheaper, and more accurate.

The benchmark numbers tell a clear story: 90.53% accuracy at $0.0008, versus 87.07% at $0.16 for the next best option. That’s better accuracy at 0.5% of the cost. At scale, this is the difference between classification being a rounding error in your infrastructure budget and being a meaningful line item.

We offer 50M free tokens for every agent. Try the classification endpoint at scaledown.ai.

Try ScaleDown
GET API KEY
BOOK A CALL
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER

MODELS

Classify
Extract
Summarize
Compress

RESOURCES

Cookbooks
Docs
Blog
Listicles

COMMUNITY

GitHub
Discord
LinkedIn
X

BENCHMARKS

ScaleDown vs OpenAI
ScaleDown vs Anthropic
ScaleDown vs Gemini
ScaleDown vs Grok
ScaleDown vs DeepSeek
ScaleDown vs Qwen
ScaleDown vs Kimi

ASK YOUR AI ASSISTANT ABOUT SCALEDOWN

SCALEDOWN · APPLIED RESEARCH LAB
Terms of Service
Privacy Policy
DPA
Cookie Policy
© 2026 · All Rights Reserved

---8<--- page: scaledown-ai-blog-no-model-training-on-your-data-at ---8<---

Page URL: https://scaledown.ai/blog/no-model-training-on-your-data-at/
Dates shown (publication/updated/changelog): June 3, 2026

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
No Model Training on Your Data at ScaleDown
Soham Chatterje
·
June 3, 2026

Your data is never used to train ScaleDown’s models. Not during inference. Not after inference. Not in aggregate, anonymized, de-identified, or any other form. The models you call today were not trained on any customer’s production data, and the models you call tomorrow won’t be either

Why This Matters

Most AI providers have a training clause somewhere in their terms. The language varies: “we may use inputs to improve our services,” “aggregated and de-identified data may be used for model development,” “you can opt out of training by contacting support.” The default is usually that your data trains their models. You have to actively opt out of it.

At ScaleDown, there is no opt-out. The training pipeline and the inference pipeline are architecturally separate systems. Customer request data does not flow into the training pipeline. There is no flag to toggle, no setting to configure, no enterprise tier required to unlock this. It is the default and only behavior.

How Our Models Are Trained

ScaleDown’s task-specific SLMs are trained on public datasets and synthetically generated data. The training corpus includes MS-MARCO, Natural Questions, S2ORC, EDGAR filings, CUAD, and synthetic QA pairs generated over public-domain documents. This is documented in detail in our finetuning methodology post.

No customer data enters this pipeline at any stage. Not as training examples. Not as evaluation data. Not as seed data for synthetic generation. The boundary is absolute.

What This Means in Practice

When you send a financial document through our compression endpoint, the model processes it and returns the compressed output. The document is not added to a training queue. It is not written to a dataset. It is not sampled for future fine-tuning runs. Combined with our zero data retention policy, the document exists only in memory for the duration of the request and is discarded when the response is returned.

This matters most for customers in regulated industries. If you are processing legal contracts, medical records, financial filings, or internal communications through ScaleDown, your data cannot appear in a future model checkpoint. It cannot leak into another customer’s inference results through memorization. It cannot surface in a training data audit because it was never in the training data.

No Exceptions

The guarantee applies uniformly across all endpoints (compression, summarization, extraction, classification), all deployment configurations, and all customer tiers. There is no “research usage” carve-out, no “aggregate insights” exception, no clause that activates under specific conditions.

If ScaleDown ever changes its training data policy, which would require a fundamental architectural change, customers will be notified in advance with explicit consent required. This is not a footnote in a terms-of-service update. It is a commitment.

Key Takeaways

Your data trains your competitors’ models. At ScaleDown, it doesn’t. The inference pipeline has no connection to the training pipeline. Customer data is never used for model improvement in any form.

We offer 50M free tokens for every agent. Try it at scaledown.ai.

Try ScaleDown
GET API KEY
BOOK A CALL
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER

MODELS

Classify
Extract
Summarize
Compress

RESOURCES

Cookbooks
Docs
Blog
Listicles

COMMUNITY

GitHub
Discord
LinkedIn
X

BENCHMARKS

ScaleDown vs OpenAI
ScaleDown vs Anthropic
ScaleDown vs Gemini
ScaleDown vs Grok
ScaleDown vs DeepSeek
ScaleDown vs Qwen
ScaleDown vs Kimi

ASK YOUR AI ASSISTANT ABOUT SCALEDOWN

SCALEDOWN · APPLIED RESEARCH LAB
Terms of Service
Privacy Policy
DPA
Cookie Policy
© 2026 · All Rights Reserved

---8<--- page: scaledown-ai-blog-self-hosted-deployment-of-scaledown ---8<---

Page URL: https://scaledown.ai/blog/self-hosted-deployment-of-scaledown/
Dates shown (publication/updated/changelog): June 3, 2026

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
Self-Hosted Deployment of ScaleDown
Soham Chatterje
·
June 3, 2026
Why Self-Host

The managed ScaleDown API handles most use cases. But some organizations have requirements that no external API can satisfy regardless of its security posture: data that cannot leave the network boundary, air-gapped environments, regulatory regimes that mandate on-premise processing, or latency constraints that require co-location with the application layer.

Self-hosted ScaleDown exists for these cases. The models run on your GPUs, the API runs on your servers, and no data leaves your environment. There is no callback to ScaleDown’s infrastructure, no telemetry sent externally, no license server that requires an outbound connection.

What You Get

A self-hosted deployment includes the full ScaleDown model suite packaged as container images. The deployment is a standard containerized service: pull the image, configure the runtime, expose the API. The interface is identical to the managed API, so existing client code works without modification.

The models are optimized for inference on commodity GPU hardware. Minimum requirements depend on which models you deploy and your throughput targets, but a L40 GPU node can serve all four model types for moderate workloads. Horizontal scaling follows the same patterns as any stateless inference service: add nodes behind a load balancer.

Deployment Model

ScaleDown provides the container images and deployment manifests. Your team handles the infrastructure: compute provisioning, networking, monitoring, and scaling. We provide reference architectures for common setups (Kubernetes with GPU node pools, standalone Docker on bare metal, ECS/EKS on AWS) and engineering support during initial deployment.

Updates are delivered as new container image versions. You control the rollout schedule, and if a specific model version is validated against your compliance requirements, you can pin it indefinitely.

What Stays the Same

The API contract is identical between managed and self-hosted. Endpoints, request formats, response formats, and model behavior are the same. If you build against the managed API and later migrate to self-hosted (or vice versa), the only change is the base URL.

Model quality is identical because the models are identical. The self-hosted images contain the same weights, the same tokenizers, and the same inference logic as the managed service.

What Changes

You take on operational responsibility: uptime, scaling, GPU utilization, model updates. ScaleDown provides the models and support. For organizations with existing ML infrastructure teams, this is a natural fit. For organizations without GPU operations experience, the managed API is typically the better starting point.

Licensing is per-deployment rather than per-token. Contact us for pricing based on your scale and deployment configuration.

Key Takeaways

Self-hosted ScaleDown gives you the same models and API with full data sovereignty. Nothing leaves your network. No external dependencies at runtime. You control the hardware, the update schedule, and the network boundary.

We offer 50M free tokens for every agent on the managed API. For self-hosted deployments, reach out at scaledown.ai.

Try ScaleDown
GET API KEY
BOOK A CALL
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER

MODELS

Classify
Extract
Summarize
Compress

RESOURCES

Cookbooks
Docs
Blog
Listicles

COMMUNITY

GitHub
Discord
LinkedIn
X

BENCHMARKS

ScaleDown vs OpenAI
ScaleDown vs Anthropic
ScaleDown vs Gemini
ScaleDown vs Grok
ScaleDown vs DeepSeek
ScaleDown vs Qwen
ScaleDown vs Kimi

ASK YOUR AI ASSISTANT ABOUT SCALEDOWN

SCALEDOWN · APPLIED RESEARCH LAB
Terms of Service
Privacy Policy
DPA
Cookie Policy
© 2026 · All Rights Reserved

---8<--- page: scaledown-ai-blog-zero-data-retention-at-scaledown ---8<---

Page URL: https://scaledown.ai/blog/zero-data-retention-at-scaledown/
Dates shown (publication/updated/changelog): May 15, 2026

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back
Zero Data Retention at ScaleDown
Soham Chatterje
·
May 15, 2026

At ScaleDown, ZDR means one specific thing “your prompt data is never written to disk.” It exists in memory for the duration of the request and nowhere else. When the response is returned, the prompt is gone. There is no retention period because there is no retention.

The Request Lifecycle

Understanding the guarantee requires understanding exactly what happens to your data from the moment a request enters ScaleDown to the moment it leaves.

A request arrives at the ScaleDown API. The input is tokenized in memory. The tokenized representation is passed to the model for processing. While the model runs, system-level metrics are collected from the tokenized data and infrastructure telemetry data such as latency, throughput, compression ratio. The model produces a response. The response is returned to the caller. The prompt data is discarded.

Nothing in that sequence involves writing the prompt to a database, a log file, a message queue, or any persistent store. The telemetry collected during processing is derived from structural properties of the request, not from the contents.

What We Retain vs. What We Never Retain

What we retain is request latency, throughput, token counts, compression ratios, model version, error codes.

The data ScaleDown keeps is limited to what is needed to operate and improve the infrastructure.

What we never retain is prompt contents, tool call inputs and outputs, user-supplied context, conversation history, request bodies in any form.

The data we keep has no semantic content. Token count tells us a request was 2,400 tokens. It does not tell us what those tokens said. Compression ratio tells us how efficiently the input was encoded. It does not tell us what was encoded. There is no path from retained telemetry back to the original prompt.

No Exceptions

The behavior is uniform across all request types and environments. Production requests, staging requests, and debug requests go through the same pipeline with the same data handling.

A request that fails partway through (model timeout, upstream error, rate limit) logs error metadata such as the error type, the point of failure, the relevant system metrics. It does not log the request contents that were in flight when the failure occurred.

This matters because exceptions are where guarantees break down. A system that handles nominal requests correctly but logs full request bodies on errors is not a ZDR system. The failure path is often the highest-risk path: failures happen under load, during debugging, in environments with reduced observability controls. ScaleDown applies the same handling regardless.

Key Takeaways

Prompt data exists only for the duration of processing. It is never persisted beyond the request lifecycle, not for debugging, not for model improvement, not in any form that survives the request boundary.

If you’re building on ScaleDown with sensitive inputs (legal documents, financial records, healthcare data, internal communications), the guarantee is structural, not contractual. The data is not retained because the system has no mechanism to retain.

We offer 50M free tokens for every agent. Try it at scaledown.ai.

Try ScaleDown
GET API KEY
BOOK A CALL
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER

MODELS

Classify
Extract
Summarize
Compress

RESOURCES

Cookbooks
Docs
Blog
Listicles

COMMUNITY

GitHub
Discord
LinkedIn
X

BENCHMARKS

ScaleDown vs OpenAI
ScaleDown vs Anthropic
ScaleDown vs Gemini
ScaleDown vs Grok
ScaleDown vs DeepSeek
ScaleDown vs Qwen
ScaleDown vs Kimi

ASK YOUR AI ASSISTANT ABOUT SCALEDOWN

SCALEDOWN · APPLIED RESEARCH LAB
Terms of Service
Privacy Policy
DPA
Cookie Policy
© 2026 · All Rights Reserved

---8<--- page: scaledown-ai-blog ---8<---

Page URL: https://scaledown.ai/blog/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Blog

Technical insights on SLMs, MLOps, and applied AI research.

Try ScaleDown
GET API KEY
BOOK A CALL
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER

MODELS

Classify
Extract
Summarize
Compress

RESOURCES

Cookbooks
Docs
Blog
Listicles

COMMUNITY

GitHub
Discord
LinkedIn
X

BENCHMARKS

ScaleDown vs OpenAI
ScaleDown vs Anthropic
ScaleDown vs Gemini
ScaleDown vs Grok
ScaleDown vs DeepSeek
ScaleDown vs Qwen
ScaleDown vs Kimi

ASK YOUR AI ASSISTANT ABOUT SCALEDOWN

SCALEDOWN · APPLIED RESEARCH LAB
Terms of Service
Privacy Policy
DPA
Cookie Policy
© 2026 · All Rights Reserved

ADDITIONAL VISIBLE STATES / CHART VALUES
Blog index was visually present but contained no article cards or changelog entries.

---8<--- page: scaledown-ai-cookbooks ---8<---

Page URL: https://scaledown.ai/cookbooks/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
ScaleDown Cookbooks

See how to use ScaleDown models to classify, extract, summarize, and compress across different types of data.

What kind of data does your AI agent handle?
Voice & Calls

Live voice agents, meeting transcripts, call recordings, support calls.

Chats & Tickets

Emails, Slack channels, support tickets, chat threads.

Files & Docs

PDFs, contracts, filings, reports, post-OCR scans.

Web Pages

Scraped pages, news articles, social posts, raw HTML.

Voice & Calls
CLASSIFICATION
Route a caller to the right flow or agent from one sentence

Classifies what the caller says and routes them to the right flow or agent.

Voice & Calls
EXTRACTION
Pull deal size, economic buyer, and next steps into HubSpot

Pulls the CRM fields a sales call produces straight off the transcript.

Voice & Calls
SUMMARIZATION
Turn a call transcript into a recap of decisions and action items

Folds a multi-speaker transcript into the decision made and who owes the next step.

Voice & Calls
COMPRESSION
Answer a question buried in a big knowledge base

Trims internal docs down to what the caller actually asked.

Chats & Tickets
CLASSIFICATION
Triage every support message by topic and priority

Labels and routes each message by topic and priority, at inbox volume.

Chats & Tickets
EXTRACTION
Pull the action items, dates, and owners out of a thread

Pulls action items, dates, and owners out of a thread.

Chats & Tickets
SUMMARIZATION
Catch me up on this thread in two lines

Turns a long thread into a two-line digest.

Chats & Tickets
COMPRESSION
Trim a long thread before an LLM drafts the reply

Strips quoted history and filler out of a long thread.

Files & Docs
CLASSIFICATION
Sort and tag documents by type, relevance, and routing

A cheap first pass on what each doc is, at page-volume scale.

Files & Docs
EXTRACTION
Pull parties, dates, amounts, and clauses as written

Returns structured facts off unstructured docs, exactly as written.

Files & Docs
SUMMARIZATION
Brief a long filing or contract down to the gist

Gives the gist of a dense document, no frontier call per doc.

Files & Docs
COMPRESSION
Shrink a long document before it hits your LLM

On FinanceBench: +8% accuracy with 97% fewer tokens. Cuts restatement out of filings and reports.

Web Pages
CLASSIFICATION
Relevance-score and tag scraped records

A cheap, fast filter for what's worth a deeper pipeline.

Web Pages
EXTRACTION
Enrich a page with company, role, signal, and contacts

Pulls company, role, signal, and contacts off raw web content.

Web Pages
SUMMARIZATION
Turn a scraped page or record into a readable profile

Turns a scraped page into a tight, readable profile.

Web Pages
COMPRESSION
Strip HTML boilerplate before any downstream call

Cuts navigation and markup out of a scraped page.

Try ScaleDown
GET API KEY
BOOK A CALL
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER

MODELS

Classify
Extract
Summarize
Compress

RESOURCES

Cookbooks
Docs
Blog
Listicles

COMMUNITY

GitHub
Discord
LinkedIn
X

BENCHMARKS

ScaleDown vs OpenAI
ScaleDown vs Anthropic
ScaleDown vs Gemini
ScaleDown vs Grok
ScaleDown vs DeepSeek
ScaleDown vs Qwen
ScaleDown vs Kimi

ASK YOUR AI ASSISTANT ABOUT SCALEDOWN

SCALEDOWN · APPLIED RESEARCH LAB
Terms of Service
Privacy Policy
DPA
Cookie Policy
© 2026 · All Rights Reserved

---8<--- page: scaledown-ai-dietcode ---8<---

Page URL: https://scaledown.ai/dietcode/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
The optimization layer every coding agent needs.

The only plugin you need to start token minimizing in Claude Code.

INSTALL DIETCODE
Claude Code
DietCode
Headroom
RTK

ACCURACY

Claude Code
DietCode
Headroom
RTK
0%
25%
50%
75%
100%
53%
60%
40%
53%

COST

Claude Code
DietCode
Headroom
RTK
0%
25%
50%
75%
100%
100%
20%
30%
40%

LATENCY

Claude Code
DietCode
Headroom
RTK
0s
2000s
4000s
6000s
8000s
2319s
2123s
6559s
5103s
Try ScaleDown
GET API KEY
BOOK A CALL
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER

MODELS

Classify
Extract
Summarize
Compress

RESOURCES

Cookbooks
Docs
Blog
Listicles

COMMUNITY

GitHub
Discord
LinkedIn
X

BENCHMARKS

ScaleDown vs OpenAI
ScaleDown vs Anthropic
ScaleDown vs Gemini
ScaleDown vs Grok
ScaleDown vs DeepSeek
ScaleDown vs Qwen
ScaleDown vs Kimi

ASK YOUR AI ASSISTANT ABOUT SCALEDOWN

SCALEDOWN · APPLIED RESEARCH LAB
Terms of Service
Privacy Policy
DPA
Cookie Policy
© 2026 · All Rights Reserved
0s

ADDITIONAL VISIBLE STATES / CHART VALUES
Chart values read from the visible chart labels: Accuracy: Claude Code 53%, DietCode 60%, Headroom 40%, RTK 53%. Cost: Claude Code 100%, DietCode 20%, Headroom 30%, RTK 40%. Latency: Claude Code 2,319s, DietCode 2,123s, Headroom 6,559s, RTK 5,103s. (The page displays the latency axis in seconds.)

---8<--- page: scaledown-ai-docs-api-reference-classify-api ---8<---

Page URL: https://scaledown.ai/docs/api-reference/classify-api/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE · CLASSIFY

POST /classify

Classify text against user-defined labels with softmax-normalized probability scores.

ℹ
All requests require an x-api-key header. Get your API key →
Request
PARAM	TYPE	DESCRIPTION
text	string	The text to classify. Either text or document must be provided.
document	string	A base64-encoded image or PDF. Supported formats: JPEG, PNG, TIFF, single-page PDF, multi-page PDF. OCR is performed automatically.
document_mime_type	string	Required when document is provided. E.g. "image/jpeg", "application/pdf".
labels*	array	Array of label objects. Each must have a name and rubric.
labels[].name*	string	The label identifier returned in the response.
labels[].rubric*	string	A yes/no question describing what this label represents. This is the most important field - write specific, actionable questions.
cURL
Python
TypeScript
Copy
curl -X POST https://api.scaledown.xyz/classify \
  -H "x-api-key: YOUR_SCALEDOWN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "I was charged twice for my subscription last month and need a refund.",
    "labels": [
      {
        "name": "billing",
        "rubric": "Is this about a billing issue, charge, refund, or payment problem?"
      },
      {
        "name": "technical",
        "rubric": "Is this about a technical issue, bug, or product not working correctly?"
      },
      {
        "name": "account",
        "rubric": "Is this about account access, login, password, or profile settings?"
      }
    ]
  }'
Response
JSON
Copy
{
  "top_label": "billing",
  "scores": {
    "billing": 0.88,
    "technical": 0.07,
    "account": 0.05
  },
  "labels": [
    { "name": "billing",   "score": 0.88, "rubric": "Is this about a billing issue..." },
    { "name": "technical", "score": 0.07, "rubric": "Is this about a technical issue..." },
    { "name": "account",   "score": 0.05, "rubric": "Is this about account access..." }
  ],
  "ocr_text": null
}
PARAM	TYPE	DESCRIPTION
top_label	string	The name of the highest-scoring label.
scores	object	A map of label name → probability score. All scores sum to 1.0.
labels	array	Full result array with name, score, and rubric for each label, in request order.
ocr_text	string | null	The raw text extracted from a document via OCR. null if no document was provided.
⚠
Scores are relative probabilities, not absolute confidence values. Always apply your own threshold before acting on a classification (e.g. require score > 0.6 before routing).
Error responses
STATUS	MEANING
422	Malformed request body or empty labels array.
502	Model service unavailable.
← Classify Overview
Integrate Classify →

---8<--- page: scaledown-ai-docs-api-reference-classify ---8<---

Page URL: https://scaledown.ai/docs/api-reference/classify/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE

Classify

Score text against your own labels - no training data required.

Overview

The /classify endpoint takes a piece of text and a set of labels you define, then returns a probability score for each label indicating how well the text matches. Scores are normalized via softmax and sum to 1.0, with the strongest match returned as top_label.

Each label is defined with a rubric - a yes/no question that describes what the label represents. The model judges how strongly the text "answers yes" to each question, then normalizes the results into a probability distribution.

When to use Classify
Support ticket triage - automatically route tickets to billing, technical, or account teams based on content
Content moderation - score content against spam, toxicity, or policy violation rubrics with confidence thresholds
Intent detection - distinguish between questions, complaints, feedback, and cancellation requests
Domain tagging - label documents by topic (medical, legal, financial) for downstream processing
Lead qualification - evaluate inbound messages against qualification criteria
Email categorization - sort incoming messages without rules engines or training data
Writing good rubrics

The rubric is the most important part of a classify request. Effective rubrics are:

Specific and framed as yes/no questions - "Does this text describe X?" outperforms "X content"
Positive rather than negative - avoid negations that confuse the model
Independent - overlapping rubrics split probability mass unpredictably
INSTEAD OF	USE
medical content	Does this text describe a medical condition, symptom, treatment, or health topic?
billing	Is this about a billing issue, charge, refund, or payment problem?
urgent	Does this message indicate the user is blocked, losing data, or needs an immediate response?
ℹ
Scores are relative probabilities, not absolute confidence. A score of 0.85 means the model assigned 85% of the probability mass to that label - not that it is 85% confident in an absolute sense. Apply your own thresholds when routing or filtering.
✦
See the API Reference for full request/response parameters, or explore the Model Routing and Support Ticket Classification examples.
← Integrate Compress
Classify API Reference →

---8<--- page: scaledown-ai-docs-api-reference-compress-api ---8<---

Page URL: https://scaledown.ai/docs/api-reference/compress-api/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE · COMPRESS

POST /compress/raw/

Compress a context and prompt into a semantically equivalent, token-efficient version.

ℹ
All requests require an x-api-key header. Get your API key →
Request
PARAM	TYPE	DESCRIPTION
context*	string	The background text to compress - documents, retrieved chunks, conversation history, or system prompt context.
prompt*	string	The user's query or instruction. Used to guide query-aware compression. Kept largely intact.
scaledown.rate*	string | number	"auto" for automatic compression (recommended), or a fixed float between 0–1 giving the fraction of tokens to remove (e.g. 0.5 removes about 50%; 0.8 keeps about 20%). Fixed rates below 0.3 may degrade quality on dense technical content.
cURL
Python
TypeScript
Copy
curl -X POST https://api.scaledown.xyz/compress/raw/ \
  -H "x-api-key: YOUR_SCALEDOWN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "context": "Your long document, conversation history, or retrieved chunks go here...",
    "prompt": "What are the key obligations in this contract?",
    "scaledown": {"rate": "auto"}
  }'
Response
JSON
Copy
{
  "compressed_prompt": "Key obligations include: delivery by Q3, payment net-30...",
  "original_prompt_tokens": 1842,
  "compressed_prompt_tokens": 614,
  "compression_rate": 0.33,
  "original_chars": 9210,
  "compressed_chars": 3070,
  "successful": true,
  "latency_ms": 118
}
PARAM	TYPE	DESCRIPTION
compressed_prompt	string	The compressed output - context and prompt combined into a single string, ready to pass directly to your LLM.
original_prompt_tokens	number	Token count of the original input.
compressed_prompt_tokens	number	Token count of the compressed output.
compression_rate	number	Fraction of original tokens retained (e.g. 0.33 = 67% compression).
original_chars	number	Character count of the original input.
compressed_chars	number	Character count of the compressed output.
successful	boolean	Whether the compression succeeded.
latency_ms	number	Server-side processing time in milliseconds.
Error responses
STATUS	MEANING
400	Malformed request body or missing required fields.
401	Missing or invalid x-api-key.
429	Rate limit exceeded.
500	Inference service unavailable.
ℹ
Use "auto" mode unless you have a strict token budget. Fixed rates below 0.3 may degrade quality on dense technical content.
← Compress Overview
Integrate Compress →

---8<--- page: scaledown-ai-docs-api-reference-compress ---8<---

Page URL: https://scaledown.ai/docs/api-reference/compress/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE

Compress

Reduce token usage by 50–70% while preserving semantic integrity.

Overview

The /compress/raw/ endpoint takes your context and prompt and returns a semantically equivalent version that uses significantly fewer tokens. The service prioritizes compressing context - the background information, retrieved documents, conversation history - while preserving the prompt itself as much as possible.

Compression ratios of 50–70% are typical, with no meaningful degradation in downstream model output quality.

When to use Compress
Cost reduction - If you're spending heavily on tokens from long system prompts, retrieved documents, or conversation history, compression cuts that cost by 50–70%.
Context window constraints - Compress large retrieval sets or long conversations to fit within your model's context window without truncation.
Latency optimization - Fewer input tokens means faster time-to-first-token from your LLM, which matters for real-time applications.
Model downsizing - Compressed contexts allow smaller, cheaper models to handle tasks that previously required larger alternatives.
How it fits in your workflow

Compress sits between your retrieval step and your LLM call. Your application logic doesn't change - you just route the context through ScaleDown before sending it to the model.

Retrieve context
→
ScaleDown /compress
→
LLM
→
Answer

The returned compressed_prompt field is a single string combining compressed context and prompt, ready to use directly. A workflow that previously cost $10/day in token spend drops to $4/day - with no changes to the model, the output quality, or the application.

Use cases
RAG pipelines - compress retrieved chunks before passing them to your LLM
Document analysis - process long PDFs and contracts without hitting context limits
Multi-turn conversations - compress conversation history as it grows
Batch processing - reduce costs when running the same prompt against many documents
✦
See the API Reference for request/response parameters, or jump to the RAG Example to see Compress in action.
← Quickstart
Compress API Reference →

---8<--- page: scaledown-ai-docs-api-reference-extract-api ---8<---

Page URL: https://scaledown.ai/docs/api-reference/extract-api/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE · EXTRACT

POST /extract

Extract named entities from text using a custom-defined schema.

ℹ
All requests require an x-api-key header. Get your API key →
Request
PARAM	TYPE	DESCRIPTION
text	string	The input text to extract entities from. Either text or document must be provided. If both are given, the OCR text is appended after text.
document	string	A base64-encoded file. Supported: JPEG, PNG, TIFF, single-page PDF, multi-page PDF. OCR via AWS Textract.
document_mime_type	string	Required when document is provided. E.g. "image/jpeg", "application/pdf".
instruction	string	Optional global instruction prepended before extraction. Use for deduplication rules, ranking constraints, or output format requirements across all entity types.
entities*	object	A mapping of entity type names to their definition. Values can be: a plain string description (each distinct value in the text is returned as its own entity, up to 10 per type), an object with description/threshold/top_n, a nested object schema, or an array of objects.
threshold	number	Global confidence threshold (0–1). Default 0 (keep all). Extracted entities below this confidence are dropped. Can be overridden per entity type.
top_n	number	Global limit on results per entity type; the most confident are kept. 0 returns all (default). Can be overridden per entity type.
Examples
Basic extraction
cURL
Python
TypeScript
Copy
curl -X POST https://api.scaledown.xyz/extract \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_SCALEDOWN_API_KEY" \
  -d '{
    "text": "Henry Wang is a CS student from the SF Bay Area. You can find him on Twitter at @henryw and Instagram at @b0i.",
    "entities": {
      "Name": "Full name of the person",
      "Twitter": "Twitter or X handle",
      "Instagram": "Instagram username"
    }
  }'
Response
Copy
{
  "entities": [
    {
      "text": "Henry Wang",
      "type": "Name",
      "confidence": 0.994,
      "start": 0,
      "end": 10,
      "context": "Henry Wang is a CS student from the SF Bay Area. You can find him on Twitter at @henryw and Instagram at @b0i."
    },
    {
      "text": "@henryw",
      "type": "Twitter",
      "confidence": 0.976,
      "start": 79,
      "end": 86,
      "context": "Henry Wang is a CS student from the SF Bay Area. You can find him on Twitter at @henryw and Instagram at @b0i."
    },
    {
      "text": "@b0i",
      "type": "Instagram",
      "confidence": 0.978,
      "start": 104,
      "end": 108,
      "context": "Henry Wang is a CS student from the SF Bay Area. You can find him on Twitter at @henryw and Instagram at @b0i."
    }
  ],
  "structured_result": null,
  "ocr_text": null
}
Structured (nested) extraction

For more complex documents, define nested schemas to extract structured objects or arrays. Use a nested object to extract a single structured group of fields, or an array of objects to extract a repeated structure such as invoice line items.

The full structured output is returned in the structured_result field.

cURL - nested object
cURL - array schema
Python
Copy
curl -X POST https://api.scaledown.xyz/extract \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_SCALEDOWN_API_KEY" \
  -d '{
    "text": "Ship to: Jane Smith, 42 Maple Street, Springfield, IL 62701.",
    "entities": {
      "recipient": "The full name of the recipient",
      "address": {
        "street": "Street address including number",
        "city": "City name",
        "state": "Two-letter state code",
        "zip": "ZIP or postal code"
      }
    }
  }'
Response - nested object
Copy
{
  "entities": [
    {
      "text": "Jane Smith",
      "type": "recipient",
      "confidence": 1.0,
      "start": 9,
      "end": 19,
      "context": "Ship to: Jane Smith, 42 Maple Street, Springfield, IL 62701."
    }
  ],
  "structured_result": {
    "recipient": "Jane Smith",
    "address": {
      "street": "42 Maple Street",
      "city": "Springfield",
      "state": "IL",
      "zip": "62701"
    }
  },
  "ocr_text": null
}
Response - array schema
Copy
{
  "entities": [],
  "structured_result": {
    "vendor": null,
    "line_items": [
      { "description": "Widget A", "quantity": "1", "unit_price": "$10.00" },
      { "description": "Widget B", "quantity": "3", "unit_price": "$5.00" },
      { "description": "Shipping", "quantity": "1", "unit_price": "$8.50" }
    ]
  },
  "ocr_text": null
}
Response fields
PARAM	TYPE	DESCRIPTION
entities	array	List of extracted scalar entities, sorted by confidence descending within each type. Nested/array types appear in structured_result instead.
entities[].text	string	The exact text span extracted from the input.
entities[].type	string	The entity type name, matching a key from your entities request field.
entities[].confidence	number	Model confidence score between 0 and 1.
entities[].start	number	Character offset of the start of the entity in the input text.
entities[].end	number	Character offset of the end of the entity.
entities[].context	string	Up to 500 characters of surrounding text on each side. Prefixed/suffixed with ... when clipped.
structured_result	object | null	Present when any entity uses a nested object or array schema. null for flat extraction requests.
ocr_text	string | null	Raw text extracted from the document via OCR. null if no document was provided.
Error responses
STATUS	MEANING
422	Malformed request body, neither text nor document provided, or OCR failed.
500	Inference service unavailable.
504	Extraction request timed out.
Writing good entity labels
INSTEAD OF	USE
CITY	city or City
city + location in the same call	just city or just location
"Name"	"Find the first and last name of the person in the text"
"city" (when you want capitals specifically)	"capital city and population center"
← Extract Overview
Integrate Extract →

---8<--- page: scaledown-ai-docs-api-reference-extract ---8<---

Page URL: https://scaledown.ai/docs/api-reference/extract/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE

Extract

Named entity recognition with custom schemas defined in plain English.

Overview

The /extract endpoint performs Named Entity Recognition (NER) on unstructured text. Unlike standard NER with fixed categories, you define the entity types you want in plain English - the model uses your descriptions to find matching spans, returning each one with a confidence score and surrounding context.

Every result includes up to 500 characters of surrounding text on each side, so you can validate or use the extracted value without going back to the source document.

Key capabilities
Flexible entity definition - describe what you're searching for in plain English: "contract parties," "medical diagnoses," or "product SKUs"
Context preservation - results include 500 characters of surrounding text for verification
Structured output - supports nested objects and arrays for complex schema definitions beyond simple entity extraction
Document support - accepts base64-encoded images and PDFs with automatic OCR via AWS Textract
Primary use cases
Contract analysis - extract parties, dates, liability caps, governing law clauses
Resume parsing - pull names, skills, education, work history
Medical records - identify diagnoses, medications, dosages, dates
Financial documents - extract amounts, dates, account numbers, counterparties
Support ticket triage - identify products, error codes, account identifiers
E-commerce - extract product names, SKUs, prices, specifications
Writing good entity labels

The entity name and description are treated as part of the model's prompt - how you phrase them directly affects extraction quality.

Use lowercase or Title Case - the model performs better with person or Person than PERSON
Descriptions can be full instructions - "Find the first and last name of the person mentioned in the text" outperforms "Name of the person"
Avoid overlapping granularities - don't include both location and city in the same request
Test synonym variations - person and full name find slightly different things
✦
See the API Reference for the full parameter spec including structured (nested) extraction, per-entity thresholds, and document support.
← Integrate Classify
Extract API Reference →

---8<--- page: scaledown-ai-docs-api-reference-integrate-classify ---8<---

Page URL: https://scaledown.ai/docs/api-reference/integrate-classify/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE · CLASSIFY

Integrate Classify

Copy-paste AI prompts to generate integration code for the /classify endpoint.

Copy one of these prompts into Claude, ChatGPT, or any AI assistant to generate integration code for the /classify endpoint. Start with the quick integration prompt to get something working fast, or use the production-ready prompt if you're building for a live environment.

Prompts
Quick integration

Paste this prompt to generate a minimal Python function - useful for prototyping or one-off scripts.

Quick integration prompt
Copy
Write a Python function `classify_text(text: str, labels: list[dict], api_key: str) -> dict`
that calls the ScaleDown classification API and returns the parsed response.

API details:
- Endpoint: POST https://api.scaledown.xyz/classify
- Auth: HTTP header `x-api-key: <your key>`
- Request body (JSON):
    {
      "text": "<text to classify>",
      "labels": [
        {"name": "<label name>", "rubric": "<yes/no question describing this label>"}
      ]
    }
- Success response (JSON):
    {
      "top_label": "<highest scoring label name>",
      "scores": {"<name>": <0.0-1.0>, ...},
      "labels": [{"name": str, "score": float, "rubric": str}],
      "ocr_text": null
    }
- Error responses: 422 (malformed body or empty labels), 502 (service unavailable)

Requirements:
- Use the requests library.
- Raise a ValueError with the status code and body on any non-2xx response.
- Return the full parsed JSON response on success.
Production-ready

Paste this prompt to generate a fully typed Python service class with error handling, retries, and environment-variable-based configuration.

Production-ready prompt
Copy
Write a production-quality Python module for integrating the ScaleDown classification API.

API details:
- Endpoint: POST https://api.scaledown.xyz/classify
- Auth: HTTP header `x-api-key: <your key>`
- Request body (JSON):
    {
      "text": "<text to classify>",       // optional if document provided
      "document": "<base64 file>",        // optional; image or PDF
      "document_mime_type": "image/jpeg", // required when document is set
      "labels": [
        {"name": "<name>", "rubric": "<yes/no question>"}
      ]
    }
- Success response (JSON):
    {
      "top_label": str,
      "scores": {str: float},
      "labels": [{"name": str, "score": float, "rubric": str}],
      "ocr_text": str | None
    }
- Error responses: 422 (bad body), 502 (service unavailable)

Apply these principles:
1. Environment config - load SCALEDOWN_API_KEY from env; raise ValueError if missing.
2. Typed result - ClassifyResult dataclass: top_label (str), scores (dict[str, float]),
   labels (list[dict]), ocr_text (str | None)
3. Custom exception - ScaleDownError with status_code and message.
4. Single-responsibility client - ScaleDownClassifyClient with one public method:
     classify(text: str | None = None, labels: list[dict] = [],
              document: str | None = None,
              document_mime_type: str | None = None) -> ClassifyResult
5. Retry with exponential backoff - 2s, 4s, 8s on 5xx/504. Raise immediately on 422.
6. Full type annotations.
FastAPI route classifier

Paste this prompt to generate a FastAPI endpoint that classifies incoming content and routes to label-specific handlers.

FastAPI route classifier prompt
Copy
Write a FastAPI application that receives text content, classifies it using the
ScaleDown classify API, and routes to different handler functions based on the
top label. Apply a 0.5 confidence threshold - requests below this score return
a low-confidence response rather than routing.

ScaleDown API:
- Endpoint: POST https://api.scaledown.xyz/classify
- Auth: x-api-key header
- Request: {"text": str, "labels": [{"name": str, "rubric": str}]}
- Response: {"top_label": str, "scores": {str: float}, "labels": [...], "ocr_text": null}

Use case: support ticket routing
Labels: billing, technical, account, general

Requirements:
1. POST /route endpoint accepting {"content": str}
2. Call ScaleDown classify with the four labels above
3. If top score >= 0.5, route to the matching handler
4. If top score < 0.5, return {"status": "low_confidence", "scores": ...}
5. Each handler returns a dict with {"team": str, "priority": str, "message": str}
6. Load SCALEDOWN_API_KEY from environment.
What the production prompt generates
✦
Principles encoded in the production-ready prompt: environment-variable config, typed dataclasses, custom exception class, single-responsibility service client, retry with exponential backoff, full type annotations.
Example output from the production-ready prompt
▼
← Classify API Reference
Extract Overview →

---8<--- page: scaledown-ai-docs-api-reference-integrate-compress ---8<---

Page URL: https://scaledown.ai/docs/api-reference/integrate-compress/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE · COMPRESS

Integrate Compress

Copy-paste AI prompts to generate integration code for the /compress/raw/ endpoint.

Copy one of these prompts into Claude, ChatGPT, or any AI assistant to generate integration code for the /compress/raw/ endpoint. Start with the quick integration prompt to get something working fast, or use the production-ready prompt if you're building for a live environment.

Prompts
Quick integration

Paste this prompt to generate a minimal Python function - useful for prototyping or one-off scripts.

Quick integration prompt
Copy
Write a Python function `compress_context(context: str, prompt: str, api_key: str) -> str`
that calls the ScaleDown compression API and returns the compressed prompt string.

API details:
- Endpoint: POST https://api.scaledown.xyz/compress/raw/
- Auth: HTTP header `x-api-key: <your key>`
- Request body (JSON):
    {
      "context": "<the text to compress>",
      "prompt": "<the user query>",
      "scaledown": {"rate": "auto"}
    }
- Success response (JSON):
    {
      "compressed_prompt": "<the compressed text>",
      "original_prompt_tokens": 150,
      "compressed_prompt_tokens": 65,
      "compression_rate": 0.43,
      "original_chars": 750,
      "compressed_chars": 325,
      "successful": true,
      "latency_ms": 118
    }
- Error responses: 400 (malformed), 401 (invalid key), 429 (rate limit), 500 (server error)

Requirements:
- Use the requests library.
- Raise a ValueError with a descriptive message on any non-2xx HTTP response.
- Return the `compressed_prompt` string on success.
Production-ready

Paste this prompt to generate a fully typed Python service class with error handling, retries, and environment-variable-based configuration.

Production-ready prompt
Copy
Write a production-quality Python module for integrating the ScaleDown compression API.

API details:
- Endpoint: POST https://api.scaledown.xyz/compress/raw/
- Auth: HTTP header `x-api-key: <your key>`
- Request body (JSON):
    {
      "context": "<text to compress>",
      "prompt": "<user query>",
      "scaledown": {"rate": "auto" | 0.0–1.0}
    }
- Success response (JSON):
    {
      "compressed_prompt": "<compressed text>",
      "original_prompt_tokens": int,
      "compressed_prompt_tokens": int,
      "compression_rate": float,
      "original_chars": int,
      "compressed_chars": int,
      "successful": bool,
      "latency_ms": int
    }
- Error responses: 400 (malformed), 401 (invalid key), 429 (rate limit), 500 (server error)

Apply these programming principles:

1. Environment configuration - Load the API key from SCALEDOWN_API_KEY env var.
   Raise a clear ValueError at construction time if it is missing or empty.

2. Typed result - Define a CompressResult dataclass with fields:
     compressed_prompt (str), original_tokens (int), compressed_tokens (int),
     compression_rate (float), savings_percent (float), latency_ms (int)

3. Custom exception - Define ScaleDownError(Exception) with status_code (int)
   and message (str).

4. Single-responsibility client - Implement ScaleDownCompressClient with one
   public method:
     compress(context: str, prompt: str, rate: str | float = "auto") -> CompressResult

5. Retry with exponential backoff - On HTTP 5xx or 429, wait 2s, 4s, 8s before
   retries 1, 2, 3. Raise ScaleDownError after all retries exhausted.
   Raise immediately on 400, 401 (not retriable).

6. Type annotations - Full type annotations on all methods.
FastAPI middleware

Paste this prompt to generate middleware that automatically compresses request context fields before route handlers process them.

FastAPI middleware prompt
Copy
Write a FastAPI middleware class ScaleDownCompressMiddleware that automatically
compresses a "context" field in incoming JSON request bodies before route handlers
process them.

ScaleDown API:
- Endpoint: POST https://api.scaledown.xyz/compress/raw/
- Auth: x-api-key header
- Request: {"context": str, "prompt": str, "scaledown": {"rate": "auto"}}
- Response: {"compressed_prompt": str, ...}

Requirements:
1. Read the request body, parse as JSON.
2. If the body has a "context" key, compress it using ScaleDown.
3. Replace the "context" field with the compressed value before forwarding.
4. If the body has no "context" key or compression fails, pass the original
   request through unchanged (log a warning on failure, do not block the request).
5. Load SCALEDOWN_API_KEY from environment; skip compression if the key is absent.
6. Add "x-scaledown-original-tokens" and "x-scaledown-compressed-tokens" response
   headers when compression succeeds.
What the production prompt generates
✦
Principles encoded in the production-ready prompt: environment-variable config, typed result dataclass, custom exception class, single-responsibility service client, retry with exponential backoff, full type annotations.
Example output from the production-ready prompt
▼
← Compress API Reference
Classify Overview →

---8<--- page: scaledown-ai-docs-api-reference-integrate-extract ---8<---

Page URL: https://scaledown.ai/docs/api-reference/integrate-extract/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE · EXTRACT

Integrate Extract

Copy-paste AI prompts to generate integration code for the /extract endpoint.

Copy one of these prompts into Claude, ChatGPT, or any AI assistant to generate integration code for the /extract endpoint. Start with the quick integration prompt to get something working fast, or use the production-ready prompt if you're building for a live environment.

Prompts
Quick integration

Paste this prompt to generate a minimal TypeScript function - useful for prototyping or one-off scripts.

Quick integration prompt
Copy
Write a TypeScript async function `extractEntities` that calls the ScaleDown entity
extraction API and returns the parsed response.

API details:
- Endpoint: POST https://api.scaledown.xyz/extract
- Auth: HTTP header `x-api-key: <your key>`
- Request body (JSON):
    {
      "text": "<the document or passage to search>",       // optional if document is provided
      "document": "<base64-encoded file>",                 // optional; image or PDF
      "document_mime_type": "image/jpeg",                  // required when document is set
      "instruction": "<optional global instruction>",      // optional
      "entities": {
        "<EntityTypeName>": "<plain English description of what to look for>"
      }
    }
  Either "text" or "document" must be provided.
- Success response (JSON):
    {
      "entities": [
        {
          "text": "<the exact matched span>",
          "type": "<EntityTypeName>",
          "confidence": 1.0,
          "start": 0,
          "end": 10,
          "context": "<up to 500 characters of surrounding text on each side>"
        }
      ],
      "structured_result": null,
      "ocr_text": null
    }
- Error responses: 422 (bad body, OCR failure), 500 (server error), 504 (timeout)

Function signature:
  extractEntities(
    payload: { text?: string; document?: string; document_mime_type?: string;
               entities: Record<string, unknown> },
    apiKey: string
  ): Promise<{ entities: Array<{ text: string; type: string; confidence: number;
                                 start: number; end: number; context: string }>;
               structured_result: Record<string, unknown> | null;
               ocr_text: string | null }>

Requirements:
- Use the native fetch API (Node 18+).
- Throw an Error with the HTTP status code and response body on any non-2xx response.
- Return the full parsed response on success.
Production-ready

Paste this prompt to generate a fully typed TypeScript service class with error handling, retries, and environment-variable-based configuration.

Production-ready prompt
Copy
Write a production-quality TypeScript module for integrating the ScaleDown entity
extraction API.

API details:
- Endpoint: POST https://api.scaledown.xyz/extract
- Auth: HTTP header `x-api-key: <your key>`
- Request body (JSON):
    {
      "text": "<document or passage to search>",          // optional if document is provided
      "document": "<base64-encoded file>",                // optional; image or PDF
      "document_mime_type": "application/pdf",            // required when document is set
      "instruction": "<optional global instruction>",
      "entities": {
        "<TypeName>": "<description string>"
          | { "description": "<what to look for>", "threshold": 0.0–1.0, "top_n": number }
          | { "<field>": "<description>", ... }           // nested object schema
          | [{ "<field>": "<description>", ... }]         // array-of-objects schema
      },
      "threshold": 0.5,
      "top_n": 0
    }
- Success response (JSON):
    {
      "entities": [{ "text": str, "type": str, "confidence": float,
                     "start": int, "end": int, "context": str }],
      "structured_result": { "<TypeName>": value | { ... } | [ ... ] | null } | null,
      "ocr_text": str | null
    }
- Error responses: 422, 500, 504

Apply these principles:
1. Environment config - load SCALEDOWN_API_KEY from process.env; throw at construction if missing.
2. TypeScript interfaces - EntityDefinition, ExtractOptions, ExtractedEntity, ExtractResult.
3. Custom error class - ScaleDownError extends Error with status: number and body: string.
4. Single-responsibility client - ScaleDownExtractClient with one public async method:
     extract(payload: {...}, options?: ExtractOptions): Promise<ExtractResult>
5. Retry with exponential backoff - 2s, 4s, 8s on 5xx/504. Throw immediately on 422.
6. Use fetch (Node 18+). No external HTTP dependencies. Full type annotations.
LangChain tool

Paste this prompt to generate a LangChain Tool that makes the Extract endpoint available to an AI agent.

LangChain tool prompt
Copy
Write a Python LangChain Tool subclass called ScaleDownExtractTool that wraps the
ScaleDown entity extraction API so it can be used as a tool inside a LangChain agent.

ScaleDown API details:
- Endpoint: POST https://api.scaledown.xyz/extract
- Auth: HTTP header `x-api-key: <your key>`
- Request body (JSON):
    {
      "text": "<document or passage to search>",
      "entities": { "<TypeName>": "<description string>" | { "description": str, "threshold": float, "top_n": int } },
      "threshold": 0.5,
      "top_n": 0
    }
- Success response: { "entities": [...], "structured_result": dict | None, "ocr_text": str | None }
- Error responses: 422, 500, 504

Requirements:
1. Load SCALEDOWN_API_KEY from os.environ in __init__. Raise ValueError if absent.
2. name = "extract_entities"; description = clear sentence about the tool's purpose.
3. _run accepts a single JSON string: { "text": str, "entities": {...}, "threshold": float, "top_n": int }
4. Return JSON-encoded response on success. On error return { "error": "<message>" }.
5. Implement _arun as async version using aiohttp.
6. Include a short usage example showing how to add this tool to a LangChain agent.
What the production prompt generates
✦
Principles encoded in the production-ready prompt: environment-variable config, full TypeScript interfaces, custom error class, single-responsibility service client, retry with exponential backoff, no external HTTP dependencies.
Example output from the production-ready prompt
▼
← Extract API Reference
Summarize Overview →

---8<--- page: scaledown-ai-docs-api-reference-integrate-summarize ---8<---

Page URL: https://scaledown.ai/docs/api-reference/integrate-summarize/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE · SUMMARIZE

Integrate Summarize

Copy-paste AI prompts to generate integration code for the /summarization/abstractive endpoint.

Copy one of these prompts into Claude, ChatGPT, or any AI assistant to generate integration code for the /summarization/abstractive endpoint. Start with the quick integration prompt to get something working fast, or use the production-ready prompt if you're building for a live environment.

Prompts
Quick integration

Paste this prompt to generate a minimal Python function - useful for prototyping or one-off scripts.

Quick integration prompt
Copy
Write a Python function `summarize_text(payload: dict, api_key: str,
instructions: str = None) -> str` that calls the ScaleDown abstractive
summarization API and returns the summary string.

API details:
- Endpoint: POST https://api.scaledown.xyz/summarization/abstractive
- Auth: HTTP header `x-api-key: <your key>`
- Request body (JSON):
    {
      "text": "<the document or passage to summarize>",  // optional if document is provided
      "document": "<base64-encoded file>",               // optional; image or PDF
      "document_mime_type": "image/jpeg",                // required when document is set
      "instructions": "<optional extra rules>",          // optional
      "max_tokens": 200                                // optional
    }
  Either "text" or "document" must be provided.
  The "instructions" field extends, not replaces, the default faithful-summary behaviour.
- Success response (JSON):
    {
      "summary": "<the generated summary>",
      "input_chars": 8340,
      "output_chars": 142,
      "latency_ms": 3241,
      "ocr_text": null
    }
- Error responses: 422, 500, 504

Requirements:
- The payload parameter is a dict that may contain "text", "document", and
  "document_mime_type" keys. Pass it through to the request body.
- Accept the API key as the second parameter.
- Add "instructions" to the request body only if it is not None.
- Raise a ValueError with status code and response body on any non-2xx HTTP response.
- Return the `summary` string on success.
Production-ready

Paste this prompt to generate a fully typed Python service class with error handling, retries, and environment-variable-based configuration.

Production-ready prompt
Copy
Write a production-quality Python module for integrating the ScaleDown abstractive
summarization API.

API details:
- Endpoint: POST https://api.scaledown.xyz/summarization/abstractive
- Auth: HTTP header `x-api-key: <your key>`
- Request body (JSON):
    {
      "text": "<document or passage>",        // optional if document provided
      "document": "<base64-encoded file>",    // optional; image or PDF
      "document_mime_type": "application/pdf",// required when document is set
      "instructions": "<optional rules>",     // optional
      "max_tokens": 200                     // optional
    }
- Success response:
    { "summary": str, "input_chars": int, "output_chars": int,
      "latency_ms": int, "ocr_text": str | None }
- Error responses: 422, 500, 504

Apply these principles:
1. Environment config - load SCALEDOWN_API_KEY from env; raise ValueError if missing.
2. Typed result - SummaryResult dataclass: summary, input_chars, output_chars,
   latency_ms (int), ocr_text (str | None)
3. Custom exception - ScaleDownError(Exception) with status_code and message.
4. Single-responsibility client - ScaleDownSummarizer with one public method:
     summarize(text=None, document=None, document_mime_type=None,
               instructions=None, max_tokens=None) -> SummaryResult
5. Retry with exponential backoff - 2s, 4s, 8s on 5xx/504. Raise immediately on 422.
6. Full type annotations.
Async batch pipeline

Paste this prompt to generate an async batch summarizer that processes many documents concurrently with controlled parallelism.

Async batch pipeline prompt
Copy
Write a Python async module that batch-summarizes a list of texts or documents using
the ScaleDown abstractive summarization API with controlled concurrency.

ScaleDown API:
- Endpoint: POST https://api.scaledown.xyz/summarization/abstractive
- Auth: x-api-key header
- Request: { "text": str, "instructions": str, "max_tokens": int }
- Success response: { "summary": str, "input_chars": int, "output_chars": int,
                      "latency_ms": int, "ocr_text": str | None }
- Error responses: 422, 500, 504

Requirements:
1. Load SCALEDOWN_API_KEY from os.environ; raise ValueError if absent.
2. SummarizeItem dataclass: text (str | None), document (str | None),
   document_mime_type (str | None)
3. Public async function:
     batch_summarize(items: list[SummarizeItem], instructions=None,
                     max_tokens=None, concurrency=5) -> list[str | None]
   Returns summaries in the same order as input. Returns None for failed items.
4. Concurrency control - asyncio + aiohttp with asyncio.Semaphore(concurrency).
5. Per-request retry - 2s, 4s, 8s on 5xx/504; None stored after 3 failures.
6. Log WARNING for permanently failed documents including index and error.
7. Omit optional fields when None.
8. Include __main__ block with 3-item sample run.
What the production prompt generates
✦
Principles encoded in the production-ready prompt: environment-variable config, typed result dataclass, custom exception class, single-responsibility service client, retry with exponential backoff, full type annotations.
Example output from the production-ready prompt
▼
← Summarize API Reference
RAG Example →

---8<--- page: scaledown-ai-docs-api-reference-summarize-api ---8<---

Page URL: https://scaledown.ai/docs/api-reference/summarize-api/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE · SUMMARIZE

POST /summarization/abstractive

Condense text into a faithful, coherent summary using abstractive summarization.

ℹ
All requests require an x-api-key header. Get your API key →
Request
PARAM	TYPE	DESCRIPTION
text	string	The document or passage to summarize. Either text or document must be provided. If both are given, OCR text is appended after text.
document	string	A base64-encoded image or PDF. OCR is performed automatically via AWS Textract.
document_mime_type	string	Required when document is provided. E.g. "image/jpeg", "application/pdf".
instructions	string	Optional rules appended to the base faithful-summary behaviour. Examples: "Use bullet points.", "Focus on financial figures only.", "Write in Spanish."
max_tokens	number	Maximum output token count. Defaults to 200, which is also the maximum; larger values are capped. For a higher limit, email neal@scaledown.ai.
cURL
Python
TypeScript
Copy
curl -X POST https://api.scaledown.xyz/summarization/abstractive \
  -H "x-api-key: YOUR_SCALEDOWN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The company reported Q3 revenue of $4.2B, up 12% year-over-year, driven by strong cloud growth. Operating expenses rose 8% to $3.1B. Net income increased to $1.1B...",
    "instructions": "Use bullet points. Focus on financial figures only."
  }'
Summarizing a document
Python - PDF
Copy
import base64
import requests

with open("report.pdf", "rb") as f:
    document = base64.b64encode(f.read()).decode()

response = requests.post(
    "https://api.scaledown.xyz/summarization/abstractive",
    headers={"x-api-key": "YOUR_SCALEDOWN_API_KEY"},
    json={
        "document": document,
        "document_mime_type": "application/pdf",
        "instructions": "Focus on key decisions and action items.",
    },
)
result = response.json()
print(result["summary"])
print(result["ocr_text"])  # raw OCR output
Response
JSON
Copy
{
  "summary": "• Q3 revenue: $4.2B (+12% YoY)\n• Operating expenses: $3.1B (+8%)\n• Net income: $1.1B",
  "input_chars": 8340,
  "output_chars": 142,
  "latency_ms": 3241,
  "finish_reason": "stop",
  "notice": null,
  "ocr_text": null
}
PARAM	TYPE	DESCRIPTION
summary	string	The generated summary text.
input_chars	number	Character count of the input text.
output_chars	number	Character count of the generated summary.
latency_ms	number	End-to-end processing time in milliseconds.
finish_reason	string	"stop" if the summary finished on its own, "length" if it was cut off at the output limit.
notice	string | null	Set when finish_reason is "length"; explains the output limit and that a higher limit is available via neal@scaledown.ai.
ocr_text	string | null	Raw text extracted from the document via OCR. null if no document was provided.
Error responses
STATUS	MEANING
422	Malformed request body, neither text nor document provided, or OCR failed.
500	Inference service unavailable.
504	Request timed out.
ℹ
The base instructions (no new information, no commentary) are always applied. The instructions field adds on top of them - it does not replace them.
← Summarize Overview
Integrate Summarize →

---8<--- page: scaledown-ai-docs-api-reference-summarize ---8<---

Page URL: https://scaledown.ai/docs/api-reference/summarize/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

API REFERENCE

Summarize

Condense documents into faithful, coherent summaries without adding new information.

Overview

The /summarization/abstractive endpoint uses abstractive summarization to condense text in the model's own words - not by extracting existing sentences. The output captures key information while remaining coherent and faithful to the source.

The model is tuned for stable, low-hallucination outputs. The base instructions (no new information, no commentary) are always applied. The optional instructions field adds on top of them - it does not replace them.

When to use Summarize
Legal and research documents - condense lengthy contracts or papers into key points
News and content pipelines - generate briefs from long articles
Customer feedback - summarize reviews or support threads
Meeting notes - turn transcripts into actionable summaries
Financial reports - extract key figures and decisions
RAG preprocessing - reduce token overhead before storing or indexing documents
Using the instructions field

The instructions parameter lets you direct the output format without overriding the faithfulness constraint. Examples:

"Use bullet points."
"Focus on financial figures only."
"Write in Spanish."
"Limit to 3 sentences."
ℹ
The instructions field extends the default behavior - it cannot instruct the model to add new information or make up content not present in the source.
✦
See the API Reference for the full parameter spec including document support and code examples.
← Integrate Extract
Summarize API Reference →

---8<--- page: scaledown-ai-docs-examples-model-routing ---8<---

Page URL: https://scaledown.ai/docs/examples/model-routing/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

EXAMPLES

LLM Model Routing

Use the /classify endpoint to intelligently route requests to the right model - reducing costs by up to 68% without sacrificing quality.

Overview

Rather than sending every request to your most expensive model, route incoming prompts to appropriately-sized models based on task complexity and type. A simple factual lookup doesn't need GPT-4o. A one-line code fix doesn't need Claude Opus.

ScaleDown's /classify endpoint classifies incoming prompts and dispatches them to the right model. Routing 40% of requests to cheaper models can reduce daily costs from ~$15,000 to ~$4,800 - a 68% reduction.

Four routing labels
LABEL	USE CASE	TARGET MODEL
simple	Factual lookups, yes/no questions, basic definitions	gpt-4o-mini
coding	Code generation, debugging, refactoring	claude-3-5-haiku
reasoning	Multi-step analysis, comparison, planning	gpt-4o
creative	Writing, brainstorming, open-ended generation	claude-3-5-sonnet
Implementation
Python
Copy
import requests
from anthropic import Anthropic
from openai import OpenAI

CLASSIFY_URL = "https://api.scaledown.xyz/classify"
SCALEDOWN_HEADERS = {
    "x-api-key": "YOUR_SCALEDOWN_API_KEY",
    "Content-Type": "application/json"
}

openai_client = OpenAI()
anthropic_client = Anthropic()

ROUTING_LABELS = [
    {
        "name": "simple",
        "rubric": "Is this a simple factual question, yes/no question, or basic definition lookup that requires minimal reasoning?"
    },
    {
        "name": "coding",
        "rubric": "Is this request about writing, debugging, reviewing, or explaining code or technical implementation?"
    },
    {
        "name": "reasoning",
        "rubric": "Does this require multi-step reasoning, analysis, comparison, planning, or synthesis of complex information?"
    },
    {
        "name": "creative",
        "rubric": "Is this a creative writing, brainstorming, open-ended generation, or imaginative task?"
    }
]

CONFIDENCE_THRESHOLD = 0.55  # Fallback to GPT-4o if uncertain
FALLBACK_MODEL = "gpt-4o"


def classify_prompt(prompt: str) -> tuple[str, float]:
    """Classify a prompt and return (label, confidence)."""
    response = requests.post(
        CLASSIFY_URL,
        headers=SCALEDOWN_HEADERS,
        json={"text": prompt, "labels": ROUTING_LABELS}
    )
    result = response.json()
    top_label = result["top_label"]
    confidence = result["scores"][top_label]
    return top_label, confidence


def call_openai(prompt: str, model: str) -> str:
    response = openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def call_claude(prompt: str, model: str) -> str:
    response = anthropic_client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


def route_and_generate(prompt: str) -> dict:
    """Classify the prompt, pick the right model, and generate a response."""

    # Step 1: Classify
    label, confidence = classify_prompt(prompt)
    print(f"Label: {label} (confidence: {confidence:.2f})")

    # Step 2: Apply confidence threshold
    if confidence < CONFIDENCE_THRESHOLD:
        print(f"Low confidence - falling back to {FALLBACK_MODEL}")
        label = "reasoning"  # use capable fallback

    # Step 3: Route to appropriate model
    model_map = {
        "simple":    ("openai",    "gpt-4o-mini"),
        "coding":    ("anthropic", "claude-haiku-4-5-20251001"),
        "reasoning": ("openai",    "gpt-4o"),
        "creative":  ("anthropic", "claude-sonnet-4-6"),
    }

    provider, model = model_map[label]

    if provider == "openai":
        answer = call_openai(prompt, model)
    else:
        answer = call_claude(prompt, model)

    return {
        "label": label,
        "confidence": confidence,
        "model_used": model,
        "answer": answer,
    }


# Test routing
examples = [
    "What is the capital of France?",                     # simple
    "Write a Python function to flatten a nested list",   # coding
    "Compare the trade-offs between REST and GraphQL",    # reasoning
    "Write a short story about a robot learning to paint",# creative
]

for prompt in examples:
    result = route_and_generate(prompt)
    print(f"Q: {prompt[:50]}...")
    print(f"→ {result['label']} → {result['model_used']}\n")
Cost analysis

At a traffic split of 50% simple, 30% coding, 20% reasoning - routing reduces cost significantly:

SCENARIO	DAILY COST
All requests to GPT-4o (baseline)	~$15,000
Routed (50% simple, 30% coding, 20% reasoning)	~$4,800
Savings	~68%
Production recommendations
Start with simpler two-tier splits - cheap vs. expensive, before adding more labels
Log all routing decisions - track label distributions to tune rubrics over time
Set sensible fallback thresholds - treat low-confidence scores as ambiguous, not wrong
Overlapping scores are data - if two labels consistently split 50/50, your rubrics may need refinement
✦
The /classify call itself costs far less than the LLM savings it unlocks. For high-volume applications, the classification overhead is negligible compared to routing 50% of traffic to a 10× cheaper model.
← Legal Contract Analyzer
Support Ticket Classification →

---8<--- page: scaledown-ai-docs-examples-rag-basic ---8<---

Page URL: https://scaledown.ai/docs/examples/rag-basic/
Dates shown (publication/updated/changelog): February 2025

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

EXAMPLES

Build RAG Without a Vector Database

ScaleDown Team · February 2025 · 12 min read

Use ScaleDown's query-aware compression to build retrieval-augmented generation without embeddings, vector stores, or infra.

Most RAG tutorials make you spin up Pinecone, Weaviate, or Chroma before you can ask a single question. What if you could skip the vector database entirely and still get accurate, grounded answers from your documents?

ScaleDown's compression API is query-aware. It takes both your document context and the user's question, then keeps only the parts that actually matter. Retrieval and compression in a single API call. No embeddings, no vector store, no infra.

✦
This guide walks you through building a customer support bot that answers questions from a product knowledge base. All you need is ScaleDown and an LLM.
How it works

A typical RAG pipeline has you embed documents, store them in a vector database, retrieve relevant chunks, and then send them to an LLM. That's a lot of moving parts.

ScaleDown replaces the embed, store, retrieve steps with a single compression call. The API accepts both context and prompt, so it knows what the user is asking and throws away everything else.

TRADITIONAL RAG

Documents
↓
Chunk & Embed
↓
Vector DB
↓
Retrieve
↓
LLM

SCALEDOWN RAG

Documents
↓
ScaleDown Compress
↓
LLM
ℹ
ScaleDown's context + prompt design means compression is query-aware. It doesn't just shrink text - it keeps what's relevant to the question and removes what isn't.
Build it step by step
Step 1 - Set up your API keys

You need a ScaleDown API key and an OpenAI key (or any LLM provider).

Python
TypeScript
Copy
import requests
import json
from openai import OpenAI

SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"
SCALEDOWN_HEADERS = {
    "x-api-key": "YOUR_SCALEDOWN_API_KEY",
    "Content-Type": "application/json"
}

openai_client = OpenAI()  # Uses OPENAI_API_KEY env var
Step 2 - Load your knowledge base

In production, this comes from your docs, CMS, or help center. Here's a sample with 6 support articles - roughly 350 tokens across 6 topics. In production your knowledge base could be thousands of articles. ScaleDown handles compression the same way.

Python
Copy
knowledge_base = """
## Password Reset
To reset your password, go to Settings > Security > Reset Password.
Click "Send Reset Link" and check your email. The link expires in 24 hours.
If you don't receive the email, check your spam folder or contact support@example.com.
Two-factor authentication users must verify via their authenticator app after resetting.

## Pricing Plans
We offer three plans:
- Starter ($9/mo): 1 user, 5GB storage, email support, basic analytics.
- Pro ($29/mo): 5 users, 50GB storage, priority support, advanced analytics,
  API access, and custom integrations.
- Enterprise ($99/mo): Unlimited users, 500GB storage, dedicated account manager,
  SSO, audit logs, SLA guarantee, and custom onboarding.
All plans include a 14-day free trial. Annual billing saves 20%.

## Data Export
You can export your data in CSV, JSON, or PDF format.
Go to Settings > Data > Export. Select the date range and format.
Exports under 10,000 rows are instant. Larger exports are queued and
you'll receive an email when the file is ready for download.
Export history is retained for 30 days.

## API Rate Limits
The API allows 100 requests per minute on Starter, 500 on Pro,
and 2000 on Enterprise. Rate limit headers are included in every response.
If you exceed the limit, you'll receive a 429 status code.
Implement exponential backoff for best results.

## Account Deletion
To delete your account, go to Settings > Account > Delete Account.
This action is irreversible. All data will be permanently removed within 72 hours.
You must cancel any active subscription before deleting your account.
An email confirmation is required to proceed with deletion.

## Integrations
We support integrations with Slack, Jira, GitHub, Zapier, and Salesforce.
Go to Settings > Integrations to connect your tools.
Pro and Enterprise plans support custom webhooks and OAuth2 applications.
Starter plans are limited to 2 active integrations.
"""
Step 3 - Compress the context with ScaleDown

Send your entire knowledge base as context and the user's question as prompt. ScaleDown compresses the context while keeping what's relevant to the question.

Python
TypeScript
Copy
user_question = "What's included in the Pro plan and how much does it cost?"

response = requests.post(
    SCALEDOWN_URL,
    headers=SCALEDOWN_HEADERS,
    json={
        "context": knowledge_base,
        "prompt": user_question,
        "model": "gpt-4o",
        "scaledown": {"rate": "auto"}
    }
)

result = response.json()
compressed_context = result["compressed_prompt"]

print(f"Original tokens:   {result['original_prompt_tokens']}")
print(f"Compressed tokens: {result['compressed_prompt_tokens']}")
# Original tokens:   350
# Compressed tokens:  85
ℹ
The knowledge base has 6 articles. The user asked about the Pro plan. ScaleDown looked at both the context and the prompt, figured out that only the pricing section is relevant, and compressed everything else away. Result: ~75% fewer tokens, with the pricing details fully intact.
Step 4 - Send the compressed context to your LLM
Python
TypeScript
Copy
response = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful customer support assistant. "
                "Answer using ONLY the provided context. "
                "If the context doesn't contain the answer, say so."
            )
        },
        {
            "role": "user",
            "content": f"Context:\n{compressed_context}\n\nQuestion: {user_question}"
        }
    ],
    temperature=0.2
)

print(response.choices[0].message.content)

Example output:

The Pro plan costs $29/month and includes 5 users, 50GB storage, priority support, advanced analytics, API access, and custom integrations. A 14-day free trial is available, and annual billing saves 20%.
Putting it all together
Python
TypeScript
Copy
import requests
from openai import OpenAI

SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"
SCALEDOWN_HEADERS = {
    "x-api-key": "YOUR_SCALEDOWN_API_KEY",
    "Content-Type": "application/json"
}
openai_client = OpenAI()


def ask(knowledge_base: str, question: str) -> str:
    """Answer a question using a knowledge base, powered by ScaleDown."""

    # Step 1: Compress. ScaleDown keeps what's relevant to the question.
    compress_response = requests.post(
        SCALEDOWN_URL,
        headers=SCALEDOWN_HEADERS,
        json={
            "context": knowledge_base,
            "prompt": question,
            "model": "gpt-4o",
            "scaledown": {"rate": "auto"}
        }
    )
    result = compress_response.json()
    compressed_context = result["compressed_prompt"]

    print(f"Tokens: {result['original_prompt_tokens']} -> {result['compressed_prompt_tokens']}")

    # Step 2: Generate. Send compressed context to your LLM.
    ai_response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful customer support assistant. "
                    "Answer using ONLY the provided context. "
                    "If the answer isn't in the context, say you don't know."
                )
            },
            {
                "role": "user",
                "content": f"Context:\n{compressed_context}\n\nQuestion: {question}"
            }
        ],
        temperature=0.2
    )

    return ai_response.choices[0].message.content


# Try it
print(ask(knowledge_base, "How do I export my data as CSV?"))
print(ask(knowledge_base, "What happens if I delete my account?"))
print(ask(knowledge_base, "How many API requests can I make on the Pro plan?"))
How this compares
	TRADITIONAL RAG	SCALEDOWN RAG
Retrieval	Vector DB (Pinecone, Weaviate, etc.)	ScaleDown's query-aware compression
Embeddings	Required (OpenAI, Cohere, etc.)	Not needed
Infrastructure	DB hosting, index management	Single API call
Context sent to LLM	Full retrieved chunks	Compressed, 40–70% fewer tokens
Hallucination risk	Depends on chunk quality	Lower - less noise in context
Setup time	Hours (provisioning, indexing)	Minutes (one API key)
Best for	Millions of documents	Knowledge bases, support docs, internal tools
⚠
For very large corpora (millions of documents), a dedicated vector database gives you better indexing and query performance at scale. ScaleDown RAG works best for knowledge bases where simplicity and cost savings are the priority.
← Integrate Summarize
E-commerce Assistant →

---8<--- page: scaledown-ai-docs-examples-rag-ecommerce ---8<---

Page URL: https://scaledown.ai/docs/examples/rag-ecommerce/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

EXAMPLES

E-commerce Product Assistant

Build a product Q&A system using ScaleDown's compression to filter catalogs before passing to an LLM - no vector database required.

Overview

This example demonstrates building a product Q&A system using ScaleDown's compression combined with an LLM. The approach enables efficient catalog searching without vector databases.

ScaleDown compresses the product catalog down to only the relevant product details before the LLM generates an answer. When a shopper asks "Which laptops have USB-C ports and how many?", ScaleDown filters six products down to just the two laptops, eliminating irrelevant items like headphones and TVs.

Why this approach
Broad catalog search - handles cross-product questions like comparing options under a budget
Specification accuracy - preserves exact prices, specs, and product details while removing noise
No infrastructure - one API call replaces embed + store + retrieve
Implementation
Step 1 - Sample product catalog
Python
Copy
import requests
from openai import OpenAI

SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"
SCALEDOWN_HEADERS = {
    "x-api-key": "YOUR_SCALEDOWN_API_KEY",
    "Content-Type": "application/json"
}
openai_client = OpenAI()

product_catalog = """
## MacBook Pro 14"
Price: $1,999 | Category: Laptop
Specs: M3 Pro chip, 18GB RAM, 512GB SSD, 14.2" Liquid Retina display
Ports: 3x Thunderbolt 4 (USB-C), HDMI, SD card, MagSafe
Battery: 18 hours | Weight: 3.5 lbs
Best for: Professional video editing, software development

## Dell XPS 15
Price: $1,599 | Category: Laptop
Specs: Intel Core i7-13700H, 16GB RAM, 512GB NVMe SSD, 15.6" OLED display
Ports: 2x Thunderbolt 4 (USB-C), USB-A, SD card reader
Battery: 13 hours | Weight: 4.2 lbs
Best for: Creative professionals, multimedia work

## Sony WH-1000XM5 Headphones
Price: $349 | Category: Audio
Specs: Industry-leading noise cancellation, 30-hour battery
Connectivity: Bluetooth 5.2, USB-C charging, 3.5mm jack
Best for: Travel, open offices, music listening

## Samsung 65" QLED TV
Price: $1,199 | Category: Television
Specs: 4K 120Hz, Quantum HDR, Neo QLED backlighting
Connectivity: 4x HDMI 2.1, 2x USB, Wi-Fi 6, Bluetooth 5.2
Best for: Home theater, gaming

## Apple AirPods Pro (2nd Gen)
Price: $249 | Category: Audio
Specs: Active Noise Cancellation, Transparency mode, 6-hour battery (30 with case)
Connectivity: Bluetooth 5.3, USB-C, H2 chip
Best for: iPhone users, gym, commuting

## iPad Pro 12.9"
Price: $1,099 | Category: Tablet
Specs: M2 chip, 8GB RAM, 256GB storage, 12.9" Liquid Retina XDR
Ports: Thunderbolt 4 (USB-C), Smart Connector
Best for: Digital artists, note-taking, video streaming
"""
Step 2 - Query function
Python
Copy
def answer_product_question(catalog: str, question: str) -> str:
    """Answer a shopper's question using the product catalog."""

    # Step 1: ScaleDown compresses the catalog to only relevant products
    compress_response = requests.post(
        SCALEDOWN_URL,
        headers=SCALEDOWN_HEADERS,
        json={
            "context": catalog,
            "prompt": question,
            "model": "gpt-4o",
            "scaledown": {"rate": "auto"}
        }
    )
    result = compress_response.json()
    compressed_catalog = result["compressed_prompt"]

    print(f"Tokens: {result['original_prompt_tokens']} -> {result['compressed_prompt_tokens']}")

    # Step 2: LLM answers using only relevant product data
    ai_response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful product assistant. Answer the customer's question "
                    "using ONLY the product information provided. Include specific prices, "
                    "specs, and model names. If the answer isn't in the catalog, say so."
                )
            },
            {
                "role": "user",
                "content": f"Product catalog:\n{compressed_catalog}\n\nQuestion: {question}"
            }
        ],
        temperature=0.1
    )

    return ai_response.choices[0].message.content
Step 3 - Try it
Python
Copy
# Question 1: USB-C ports on laptops
answer = answer_product_question(
    product_catalog,
    "Which laptops have USB-C ports and how many does each have?"
)
print(answer)
# ScaleDown keeps only the two laptop entries, dropping audio/TV/tablet
# Tokens: ~320 -> ~90

# Question 2: Budget noise-canceling headphones
answer = answer_product_question(
    product_catalog,
    "I have a $300 budget. Do you have noise-canceling headphones?"
)
print(answer)

# Question 3: Comparison under $1,500
answer = answer_product_question(
    product_catalog,
    "What laptops do you have under $1,700? Compare their battery life."
)
print(answer)
Example output

Question: "Which laptops have USB-C ports and how many does each have?"

Both laptops have USB-C ports. The MacBook Pro 14" has 3 Thunderbolt 4 (USB-C) ports plus MagSafe, while the Dell XPS 15 has 2 Thunderbolt 4 (USB-C) ports. Both also include additional connectivity options like HDMI and SD card readers.
ℹ
ScaleDown saw "laptops" and "USB-C" in the question, kept only the MacBook Pro and Dell XPS entries, and dropped the headphones, TV, AirPods, and iPad - resulting in ~72% token reduction while preserving all relevant specs.
← RAG Example
HR Policy Bot →

---8<--- page: scaledown-ai-docs-examples-rag-hr ---8<---

Page URL: https://scaledown.ai/docs/examples/rag-hr/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

EXAMPLES

HR Policy Bot

Build an internal HR assistant that answers policy questions by compressing your employee handbook with ScaleDown.

Overview

This example shows how to build an internal HR assistant using ScaleDown's compression paired with an LLM. When an employee asks about remote work policies, ScaleDown automatically filters the handbook down to only relevant content, then passes the compressed result to Claude or GPT-4 for answering.

Key implementation steps
Compress - send the full handbook and employee question to ScaleDown's API, which intelligently identifies and preserves only pertinent policy sections
Generate - feed the compressed context into an LLM with a system prompt instructing it to answer "using ONLY the provided handbook"
Respond - the model delivers specific, accurate answers citing actual policy figures
⚠
Sensitive matters - disciplinary actions, terminations, accommodations - should always be escalated to human HR representatives rather than handled by the bot.
Implementation
Python
Copy
import requests
from openai import OpenAI

SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"
SCALEDOWN_HEADERS = {
    "x-api-key": "YOUR_SCALEDOWN_API_KEY",
    "Content-Type": "application/json"
}
openai_client = OpenAI()

# Sample HR handbook (in production: load from your HRIS, Notion, Confluence, etc.)
hr_handbook = """
## Vacation Policy
Full-time employees accrue 15 days of paid vacation per year in their first 3 years,
20 days from year 4 onwards. Vacation days must be approved by your manager at least
2 weeks in advance. Up to 5 unused vacation days can be carried over to the next year.
Vacation is paid out upon termination.

## Remote Work Policy
Employees may work remotely up to 3 days per week after completing their 90-day
onboarding period. Remote work arrangements must be agreed upon with your manager.
Core hours are 10am–3pm in your local timezone. Fully remote roles are approved
on a case-by-case basis by the HR director and department head.

## Parental Leave
Primary caregivers receive 16 weeks of fully paid parental leave.
Secondary caregivers receive 4 weeks of fully paid parental leave.
Leave can begin up to 4 weeks before the expected due date.
Additional unpaid leave of up to 12 weeks is available under FMLA.

## Health Benefits
The company covers 90% of health insurance premiums for employees and 70%
for dependents. Dental and vision are included. Open enrollment is in November.
FSA and HSA accounts are available. Mental health coverage includes 20 therapy
sessions per year at no cost.

## Professional Development
Each employee receives $2,000 per year for professional development (courses,
conferences, certifications). Requests must be submitted to your manager and
approved by HR. Reimbursement requires receipts and proof of completion.
The company also offers a tuition reimbursement program of up to $5,250/year
for job-related degree programs, subject to a 2-year employment commitment.

## Performance Reviews
Performance reviews are conducted twice per year: in June and December.
Compensation adjustments are made annually in January based on performance ratings.
Employees rated "Exceeds Expectations" are eligible for a bonus of 10–20% of
base salary. Promotion decisions are made in December alongside year-end reviews.
"""


def answer_hr_question(handbook: str, question: str) -> str:
    """Answer an HR policy question using the employee handbook."""

    # Step 1: Compress handbook to relevant sections
    compress_response = requests.post(
        SCALEDOWN_URL,
        headers=SCALEDOWN_HEADERS,
        json={
            "context": handbook,
            "prompt": question,
            "model": "gpt-4o",
            "scaledown": {"rate": "auto"}
        }
    )
    result = compress_response.json()
    compressed_handbook = result["compressed_prompt"]

    print(f"Handbook tokens: {result['original_prompt_tokens']} -> {result['compressed_prompt_tokens']}")

    # Step 2: Generate answer from compressed context
    ai_response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an HR assistant. Answer the employee's question using ONLY "
                    "the information in the provided handbook. Be specific - cite exact "
                    "numbers, timelines, and policy details. If the handbook doesn't cover "
                    "the question, say so and recommend they contact HR directly."
                )
            },
            {
                "role": "user",
                "content": f"Employee Handbook:\n{compressed_handbook}\n\nQuestion: {question}"
            }
        ],
        temperature=0.1
    )

    return ai_response.choices[0].message.content


# Example questions
print(answer_hr_question(hr_handbook, "How many vacation days do I get after 5 years?"))
print(answer_hr_question(hr_handbook, "Can I work from home every day?"))
print(answer_hr_question(hr_handbook, "How much parental leave does the company offer?"))
print(answer_hr_question(hr_handbook, "What's my professional development budget?"))
Example outputs

Q: "How many vacation days do I get after 5 years?"

After completing 4 or more years of employment, you accrue 20 days of paid vacation per year. You can also carry over up to 5 unused days to the following year, giving you a potential maximum of 25 days available in a given year.

Q: "How much parental leave does the company offer?"

Primary caregivers receive 16 weeks of fully paid parental leave, which can begin up to 4 weeks before the expected due date. Secondary caregivers receive 4 weeks of fully paid leave. Additional unpaid leave of up to 12 weeks is available under FMLA.
✦
ScaleDown compresses the handbook to only the sections relevant to each question. A question about vacation days doesn't include parental leave or professional development policy - keeping the LLM focused and reducing hallucination surface area.
← E-commerce Assistant
Legal Contract Analyzer →

---8<--- page: scaledown-ai-docs-examples-rag-legal ---8<---

Page URL: https://scaledown.ai/docs/examples/rag-legal/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

EXAMPLES

Legal Contract Analyzer

Analyze contracts using query-aware compression to focus the LLM on relevant clauses - reducing costs by 70–85% per query.

Overview

ScaleDown's RAG approach streamlines contract analysis by compressing irrelevant sections before sending text to an LLM. Rather than maintaining vector databases, the system identifies clauses matching a query and removes boilerplate.

When a user asks "What is the liability cap?", ScaleDown reduces ~620 tokens to ~95 tokens by retaining Section 5 (liability terms) while dropping definitions, payment schedules, and confidentiality clauses unrelated to the question - a 70–85% token reduction per query.

Why compression matters for legal analysis
Citation accuracy - legal answers require precision; compression helps the LLM focus on the correct clauses
Cost efficiency - enterprise contracts spanning 10–30 pages benefit from large per-query token reduction
No hallucination - grounding answers in compressed, relevant text reduces fabricated clause references
Implementation
Python
Copy
import requests
from openai import OpenAI

SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"
SCALEDOWN_HEADERS = {
    "x-api-key": "YOUR_SCALEDOWN_API_KEY",
    "Content-Type": "application/json"
}
openai_client = OpenAI()

# Sample software license agreement
contract = """
SOFTWARE LICENSE AGREEMENT

This Software License Agreement ("Agreement") is entered into as of January 1, 2024,
between TechCorp Inc. ("Licensor") and ClientCo LLC ("Licensee").

SECTION 1. DEFINITIONS
"Software" means the TechCorp Platform, including all updates and documentation.
"Authorized Users" means employees and contractors of Licensee.
"Confidential Information" means any non-public business information.

SECTION 2. LICENSE GRANT
Licensor grants Licensee a non-exclusive, non-transferable license to use the
Software for internal business purposes only. Sublicensing is expressly prohibited.
The license covers up to 50 Authorized Users.

SECTION 3. PAYMENT TERMS
Licensee shall pay $50,000 annually, due within 30 days of invoice.
Late payments incur a 1.5% monthly interest charge. Licensor may suspend access
after 15 days of non-payment with 5 days written notice.

SECTION 4. CONFIDENTIALITY
Each party agrees to maintain the confidentiality of the other party's Confidential
Information for 3 years following disclosure. This obligation survives termination.

SECTION 5. LIMITATION OF LIABILITY
In no event shall either party's liability exceed the fees paid in the 12 months
preceding the claim. Neither party is liable for indirect, consequential, or
punitive damages. This limitation does not apply to breaches of confidentiality
or intellectual property infringement.

SECTION 6. TERM AND TERMINATION
This Agreement is effective for 2 years and auto-renews annually unless either
party provides 90 days written notice of non-renewal. Either party may terminate
for material breach with 30 days notice and opportunity to cure.

SECTION 7. SECURITY AND COMPLIANCE
Licensor maintains SOC 2 Type II certification and ISO 27001 compliance.
Annual penetration testing reports are available upon request under NDA.
Data is encrypted in transit (TLS 1.3) and at rest (AES-256).

SECTION 8. GOVERNING LAW
This Agreement is governed by the laws of Delaware. Disputes are resolved through
binding arbitration in San Francisco, California.
"""


def analyze_contract(contract_text: str, question: str) -> str:
    """Answer a legal question about a contract using ScaleDown + LLM."""

    # Step 1: Compress to relevant clauses only
    compress_response = requests.post(
        SCALEDOWN_URL,
        headers=SCALEDOWN_HEADERS,
        json={
            "context": contract_text,
            "prompt": question,
            "model": "gpt-4o",
            "scaledown": {"rate": "auto"}
        }
    )
    result = compress_response.json()
    compressed_contract = result["compressed_prompt"]

    print(f"Contract tokens: {result['original_prompt_tokens']} -> {result['compressed_prompt_tokens']}")

    # Step 2: Generate precise legal answer
    ai_response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a legal analyst. Answer questions about the contract using "
                    "ONLY the provided text. Be precise - cite specific section numbers, "
                    "dollar amounts, timeframes, and exact language. If the contract "
                    "doesn't address the question, say so explicitly."
                )
            },
            {
                "role": "user",
                "content": f"Contract:\n{compressed_contract}\n\nQuestion: {question}"
            }
        ],
        temperature=0.1
    )

    return ai_response.choices[0].message.content


# Query multiple aspects of the contract
print(analyze_contract(contract, "What is the liability cap?"))
print(analyze_contract(contract, "Can the licensee sublicense the software?"))
print(analyze_contract(contract, "What are the payment terms and penalties for late payment?"))
print(analyze_contract(contract, "How long does the confidentiality obligation last?"))
print(analyze_contract(contract, "What security certifications does the vendor maintain?"))
Example outputs

Q: "What is the liability cap?"

Per Section 5 (Limitation of Liability), neither party's total liability can exceed the fees paid in the 12 months preceding the claim. The agreement also excludes liability for indirect, consequential, or punitive damages. Important exceptions: this limitation does not apply to breaches of confidentiality or intellectual property infringement.

Q: "What are the payment terms and penalties for late payment?"

Per Section 3, the annual fee is $50,000, due within 30 days of invoice. Late payments accrue interest at 1.5% per month. After 15 days of non-payment, the Licensor may suspend access with 5 days prior written notice.
✦
For each query, ScaleDown compresses the 620-token contract to ~90–120 tokens of relevant clauses. Across 100 queries per day on a 10-page contract, this translates to roughly 85% token savings on the context portion of each LLM call.
← HR Policy Bot
LLM Model Routing →

---8<--- page: scaledown-ai-docs-examples-support-tickets ---8<---

Page URL: https://scaledown.ai/docs/examples/support-tickets/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

EXAMPLES

Support Ticket Classification

Route support tickets to the right team automatically - no training data or fine-tuning required.

Overview

Instead of hardcoded rules, you define rubrics - yes/no questions describing each category. The API returns probability scores for each label, letting you route based on the top match.

The guide recommends starting with 4–6 well-designed labels rather than numerous overlapping ones, and always maintaining a fallback handler for ambiguous inputs.

Implementation
Step 1 - Define labels with rubrics

Create clear, independent questions like "Is this about a billing issue, charge, refund, or payment problem?" Each rubric should be specific to avoid overlapping categories.

Python
Copy
import requests

CLASSIFY_URL = "https://api.scaledown.xyz/classify"
SCALEDOWN_HEADERS = {
    "x-api-key": "YOUR_SCALEDOWN_API_KEY",
    "Content-Type": "application/json"
}

SUPPORT_LABELS = [
    {
        "name": "billing",
        "rubric": "Is this about a billing issue, incorrect charge, refund request, or payment problem?"
    },
    {
        "name": "technical",
        "rubric": "Is this about a software bug, error message, feature not working, or technical troubleshooting?"
    },
    {
        "name": "account",
        "rubric": "Is this about account access, login issues, password reset, or profile management?"
    },
    {
        "name": "feature_request",
        "rubric": "Is this a suggestion for a new feature, product improvement, or enhancement request?"
    },
    {
        "name": "general",
        "rubric": "Is this a general question about how to use the product, documentation request, or how-to inquiry?"
    }
]

CONFIDENCE_THRESHOLD = 0.6  # Require this confidence before routing


def classify_ticket(ticket_text: str) -> dict:
    """Classify a support ticket and return routing decision."""
    response = requests.post(
        CLASSIFY_URL,
        headers=SCALEDOWN_HEADERS,
        json={"text": ticket_text, "labels": SUPPORT_LABELS}
    )
    result = response.json()
    top_label = result["top_label"]
    top_score = result["scores"][top_label]

    return {
        "top_label": top_label,
        "confidence": top_score,
        "scores": result["scores"],
        "requires_review": top_score < CONFIDENCE_THRESHOLD,
    }
Step 2 - Route with confidence thresholds

Check the top score before routing. Treat low-confidence results (below 0.6) as candidates for manual review rather than forcing an incorrect categorization.

Python
Copy
TEAM_ROUTING = {
    "billing":         {"team": "Billing Support",    "sla_hours": 4,  "priority": "high"},
    "technical":       {"team": "Technical Support",  "sla_hours": 8,  "priority": "medium"},
    "account":         {"team": "Account Support",    "sla_hours": 2,  "priority": "high"},
    "feature_request": {"team": "Product Team",       "sla_hours": 72, "priority": "low"},
    "general":         {"team": "General Support",    "sla_hours": 24, "priority": "low"},
}


def route_ticket(ticket_text: str, ticket_id: str) -> dict:
    """Classify and route a support ticket."""

    classification = classify_ticket(ticket_text)
    top_label = classification["top_label"]
    confidence = classification["confidence"]

    # Handle hybrid / ambiguous cases
    scores = classification["scores"]
    sorted_labels = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_two = sorted_labels[:2]

    is_hybrid = (
        len(top_two) >= 2 and
        top_two[0][1] > 0.4 and
        top_two[1][1] > 0.3
    )

    if classification["requires_review"] or is_hybrid:
        return {
            "ticket_id": ticket_id,
            "status": "manual_review",
            "reason": "low_confidence" if classification["requires_review"] else "hybrid_classification",
            "top_label": top_label,
            "confidence": confidence,
            "scores": scores,
        }

    routing = TEAM_ROUTING[top_label]
    return {
        "ticket_id": ticket_id,
        "status": "routed",
        "team": routing["team"],
        "priority": routing["priority"],
        "sla_hours": routing["sla_hours"],
        "label": top_label,
        "confidence": confidence,
    }


# Test with sample tickets
tickets = [
    ("TKT-001", "I was charged $99 twice this month and need a refund immediately."),
    ("TKT-002", "The export button doesn't work in Chrome. I get a 500 error."),
    ("TKT-003", "I can't log in. The page just spins and nothing happens."),
    ("TKT-004", "Would love a dark mode option - would really help at night."),
    ("TKT-005", "How do I add a new team member to my account?"),
]

for ticket_id, text in tickets:
    result = route_ticket(text, ticket_id)
    print(f"{ticket_id}: {result['status']} → {result.get('team', 'Manual Review')} ({result['label'] if 'label' in result else result['top_label']}: {result['confidence']:.0%})")
Example output
Output
Copy
TKT-001: routed → Billing Support       (billing: 92%)
TKT-002: routed → Technical Support    (technical: 88%)
TKT-003: routed → Account Support      (account: 79%)
TKT-004: routed → Product Team         (feature_request: 85%)
TKT-005: routed → General Support      (general: 71%)
Advanced patterns
Dynamic system prompt selection

Beyond routing, use the classification label to select a specialized system prompt for each team:

Python
Copy
SYSTEM_PROMPTS = {
    "billing": (
        "You are a billing specialist. Help the customer resolve payment issues, "
        "process refunds according to policy, and escalate disputes when needed."
    ),
    "technical": (
        "You are a technical support engineer. Diagnose bugs systematically, "
        "ask for reproduction steps, and provide clear troubleshooting guidance."
    ),
    "account": (
        "You are an account specialist. Verify identity before making changes, "
        "follow security protocols, and escalate suspicious requests."
    ),
}

def get_system_prompt(label: str) -> str:
    return SYSTEM_PROMPTS.get(label, "You are a helpful support agent.")
✦
Monitor rubric quality through confidence patterns over time. If billing tickets consistently score 0.55–0.65, your billing rubric may be too similar to the account rubric - tighten the wording to differentiate them.
← LLM Model Routing
Workflow Example →

---8<--- page: scaledown-ai-docs-examples-workflow ---8<---

Page URL: https://scaledown.ai/docs/examples/workflow/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

EXAMPLES

Workflow Example

A complete end-to-end workflow showing how to integrate ScaleDown compression into an AI pipeline.

Complete workflow

Here's how to use the compressed context in your AI workflow. The service operates in three steps: compress context via the ScaleDown API, construct a prompt with the compressed output, then send to your AI provider.

Python
Copy
import requests
import openai

SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"
headers = {
    "x-api-key": "YOUR_SCALEDOWN_API_KEY",
    "Content-Type": "application/json"
}

# Step 1: Compress your context with ScaleDown
compressed_response = requests.post(
    SCALEDOWN_URL,
    headers=headers,
    json={
        "context": "Long context about your topic...",
        "prompt": "What specific question you want answered",
        "model": "gpt-4o",
        "scaledown": {"rate": "auto"}
    }
)

compressed_context = compressed_response.json()["compressed_prompt"]

# Step 2: Use compressed context with your AI provider
your_actual_question = "What specific question you want answered"

final_prompt = f"""
System: You are a helpful assistant that answers questions using the provided context
Context: {compressed_context}
User: {your_actual_question}
"""

# Step 3: Send to your AI provider (OpenAI, etc.)
ai_response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": final_prompt}]
)
Real example - Messi biography
Python
Copy
# Example: Compress context about Messi
payload = {
    "context": "Lionel Messi is an Argentine professional footballer who plays as a forward for and captains both Major League Soccer club Inter Miami and the Argentina national team. Often considered the best player in the world and regarded by many as the greatest of all time, Messi has won a record eight Ballon d'Or awards, a record six European Golden Shoes, and in 2020 was named to the Ballon d'Or Dream Team. Until 2021, he had spent his entire professional career with FC Barcelona, with whom he won a club-record 35 trophies, including ten La Liga titles, seven Copa del Rey titles, and the UEFA Champions League four times.",
    "prompt": "How many Ballon d'Or awards does Messi have?",
    "model": "gpt-4o",
    "scaledown": {
        "rate": "auto"
    }
}

response = requests.post(SCALEDOWN_URL, headers=headers, json=payload)
result = response.json()

print(f"Original tokens:   {result['original_prompt_tokens']}")
print(f"Compressed tokens: {result['compressed_prompt_tokens']}")
print(f"Compressed context: {result['compressed_prompt']}")

# Use the compressed context in your final prompt
compressed_context = result["compressed_prompt"]
question = "How many Ballon d'Or awards does Messi have?"

# Pass to your LLM
final_response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": f"Context: {compressed_context}\n\nQuestion: {question}"
        }
    ]
)
print(final_response.choices[0].message.content)
# → Messi has won a record eight Ballon d'Or awards.
Advanced configuration options

Once you're comfortable with basic compression, you can fine-tune your requests:

OPTION	DESCRIPTION	DEFAULT
rate	"auto" or a float 0–1. Lower = more compression. Rates below 0.3 may degrade quality on dense content.	"auto"
model	The target model's tokenizer. ScaleDown optimizes token counts for this model.	"gpt-4o"
✦
The compressed context functions as a condensed version of lengthy source material. Developers can maintain relevance while reducing token usage - particularly valuable when working with budget-conscious AI API calls.
← Support Ticket Classification
Python Package →

---8<--- page: scaledown-ai-docs-guides-classify ---8<---

Page URL: https://scaledown.ai/docs/guides/classify/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

GUIDES

Classification Patterns

Route, triage, and tag content at scale. No training data, no fine-tuning - define your labels in plain English.

How it works

ScaleDown's Classify model scores a piece of text against a set of labels you define. Each label has a name and a rubric - a yes/no question that determines whether the label applies.

The model returns a probability distribution across all labels, plus a top_label field for easy routing. No training data, no fine-tuning, no labeling pipelines - you describe the categories and the model handles the rest.

Basic example
Python
TypeScript
Copy
import requests

response = requests.post(
    "https://api.scaledown.xyz/classify",
    headers={"x-api-key": "YOUR_SCALEDOWN_KEY"},
    json={
        "text": "Hi, I was charged twice for my last order and need a refund.",
        "labels": [
            {
                "name": "billing",
                "rubric": "Is this about a billing issue, payment problem, or refund request?"
            },
            {
                "name": "technical",
                "rubric": "Is this about a bug, error, or technical problem with the product?"
            },
            {
                "name": "account",
                "rubric": "Is this about account access, login, or account settings?"
            },
            {
                "name": "general",
                "rubric": "Is this a general inquiry that doesn't fit the other categories?"
            },
        ],
    },
)

result = response.json()
print(result["top_label"])   # "billing"
print(result["scores"])      # {"billing": 0.89, "technical": 0.04, ...}
Request parameters
PARAM	TYPE	DESCRIPTION
text*	string	The content to classify - ticket, email, document, or any plain text.
labels*	Label[]	Array of label objects. Must have at least one label.
labels[].name*	string	Short identifier for the category. Used as the key in the scores object.
labels[].rubric*	string	A yes/no question that determines if this label applies. More specific rubrics yield more accurate scores.
Response
JSON
Copy
{
  "top_label": "billing",
  "scores": {
    "billing": 0.891,
    "technical": 0.041,
    "account": 0.038,
    "general": 0.030
  },
  "labels": [
    { "name": "billing", "score": 0.891, "applies": true },
    { "name": "technical", "score": 0.041, "applies": false },
    { "name": "account", "score": 0.038, "applies": false },
    { "name": "general", "score": 0.030, "applies": false }
  ]
}
ℹ
Scores are relative probabilities that sum to 1.0, not absolute confidence values. If you need a confidence threshold (e.g. "only route if score > 0.7"), apply it against scores[top_label].
Common patterns
Support ticket routing
Python
Copy
ROUTING_LABELS = [
    {"name": "billing", "rubric": "Is this about payment, invoices, or charges?"},
    {"name": "technical", "rubric": "Is this a bug report or technical issue?"},
    {"name": "onboarding", "rubric": "Is this about setup or getting started?"},
    {"name": "feature_request", "rubric": "Is this requesting a new feature or improvement?"},
    {"name": "cancellation", "rubric": "Is this about cancelling or downgrading?"},
]

ROUTING_TABLE = {
    "billing": "billing-queue@company.com",
    "technical": "eng-support@company.com",
    "onboarding": "success@company.com",
    "feature_request": "product@company.com",
    "cancellation": "retention@company.com",
}

def route_ticket(ticket_text: str) -> str:
    result = requests.post(
        "https://api.scaledown.xyz/classify",
        headers={"x-api-key": "YOUR_SCALEDOWN_KEY"},
        json={"text": ticket_text, "labels": ROUTING_LABELS},
    ).json()
    return ROUTING_TABLE.get(result["top_label"], "general-queue@company.com")
Content moderation

Use a confidence threshold to flag borderline content for human review:

Python
Copy
def moderate(text: str) -> dict:
    result = requests.post(
        "https://api.scaledown.xyz/classify",
        headers={"x-api-key": "YOUR_SCALEDOWN_KEY"},
        json={
            "text": text,
            "labels": [
                {"name": "safe", "rubric": "Is this content safe and appropriate?"},
                {"name": "spam", "rubric": "Is this spam, promotional, or low-quality content?"},
                {"name": "harmful", "rubric": "Does this contain harmful, abusive, or dangerous content?"},
            ],
        },
    ).json()

    top = result["top_label"]
    confidence = result["scores"][top]

    if top == "safe":
        return {"action": "allow"}
    elif confidence > 0.85:
        return {"action": "block", "reason": top}
    else:
        return {"action": "review", "reason": top, "confidence": confidence}
Intent detection
Python
Copy
# Detect user intent from a chat message
def detect_intent(message: str) -> str:
    result = requests.post(
        "https://api.scaledown.xyz/classify",
        headers={"x-api-key": "YOUR_SCALEDOWN_KEY"},
        json={
            "text": message,
            "labels": [
                {"name": "question", "rubric": "Is the user asking a question?"},
                {"name": "complaint", "rubric": "Is the user expressing a complaint or frustration?"},
                {"name": "purchase", "rubric": "Is the user trying to buy something or asking about pricing?"},
                {"name": "cancel", "rubric": "Is the user trying to cancel or leave?"},
                {"name": "other", "rubric": "Is this a message that doesn't fit the above?"},
            ],
        },
    ).json()
    return result["top_label"]
Writing good rubrics

The rubric is the most important input. A few principles:

Make it a yes/no question. "Does this contain X?" works better than "What is this about?"
Be specific. "Is this about a payment failure or overcharge?" outperforms "Is this a billing issue?"
Avoid overlap. If two rubrics could both answer "yes" to the same input, add exclusion language: "Is this about X and not about Y?"
Test with edge cases. The model performs best with up to ~20 labels. Beyond that, split into hierarchical classification steps.
← RAG
Next: Integration Prompts →

---8<--- page: scaledown-ai-docs-guides-integration-prompts ---8<---

Page URL: https://scaledown.ai/docs/guides/integration-prompts/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

GUIDES

Integration Prompts

Drop-in system prompts for agent pipelines. Copy one into your agent's system prompt and it immediately knows how to call the ScaleDown API.

✦
These prompts are designed for Claude, GPT-4o, and similar instruction-following models. Paste the relevant prompt into the system message of any agent - no code changes required.
How to use
Pick the prompt for the ScaleDown model your agent needs
Copy it and paste into your agent's system prompt (or prepend to an existing one)
Replace <SCALEDOWN_API_KEY> with your actual key, or set it via your environment and tell the agent where to find it
The agent will now call the ScaleDown API automatically when it encounters relevant tasks
CompressPaste into any agent that handles large context windows or RAG retrieval.
Copy prompt
You have access to the ScaleDown Compress API to reduce token count before sending context to a frontier LLM.

Endpoint: POST https://api.scaledown.xyz/compress/raw/
Headers: {"x-api-key": "<SCALEDOWN_API_KEY>", "Content-Type": "application/json"}
Request body fields:
- "context" (string, required): the background text, document, or conversation history to compress
- "prompt" (string, required): the user's main query or question
- "scaledown" (object, required): compression settings - use {"rate": "auto"} for automatic compression, or {"rate": 0.5} to remove about that fraction of tokens (0–1; 0.8 keeps about 20%)

When the user provides a long document, conversation history, or large context window:
1. POST the content using the above format
2. Read "compressed_prompt" from the response - this is the ready-to-use compressed output
3. Pass "compressed_prompt" as the context when calling your primary LLM instead of the original text

Response fields: compressed_prompt (string), original_prompt_tokens (number), compressed_prompt_tokens (number), successful (boolean), latency_ms (number).

Typical compression achieves 50–70% token reduction with maintained output quality. Use "auto" mode unless you need a guaranteed token budget. Rates below 0.3 may degrade dense technical content.
SummarizePaste into agents that summarize documents, threads, or transcripts.
Copy prompt
You have access to the ScaleDown Summarize API for generating high-quality abstractive summaries.

Endpoint: POST https://api.scaledown.xyz/summarization/abstractive
Headers: {"x-api-key": "<SCALEDOWN_API_KEY>", "Content-Type": "application/json"}
Request body fields:
- "text" (string, required): the input text to summarize - can be an article, document, transcript, or any plain text
- "instructions" (string, optional): directives to shape output, e.g. "Use bullet points. Focus on dates and key decisions only."
- "max_tokens" (number, optional): token ceiling for the output summary; defaults to and is capped at 200

When the user asks you to summarize a document, transcript, article, or thread:
1. POST the content using the above format
2. Return the "summary" field from the response directly to the user
3. If the user wants a specific format or focus, pass that as "instructions"

Response fields: summary (string), input_chars (number), output_chars (number), latency_ms (number).

The model never adds new information or commentary beyond what is in the source text.
ExtractPaste into agents that pull structured data from unstructured documents.
Copy prompt
You have access to the ScaleDown Extract API for pulling structured entities out of unstructured text.

Endpoint: POST https://api.scaledown.xyz/extract
Headers: {"x-api-key": "<SCALEDOWN_API_KEY>", "Content-Type": "application/json"}
Request body fields:
- "text" (string, required): the source document, article, web page, or any plain text to extract from
- "entities" (object, required): a mapping of entity type names to plain-English definitions, e.g. {"Name": "Full name of a person", "Email": "Email address"}
- "threshold" (number, optional): global confidence threshold 0–1; entities below this confidence are dropped (default 0, keep all)
- "top_n" (number, optional): max results to return per entity type, keeping the most confident; 0 returns all (default 0)

When the user wants to extract specific fields, entities, or data from unstructured text:
1. Build the "entities" map using plain English descriptions for each type
2. POST to the endpoint and read the "entities" array from the response
3. Each result includes: text (string), type (string), confidence (number 0–1), start/end (character offsets), context (surrounding text)

No JSON schema definition required - describe entity types in plain English.
ClassifyPaste into agents that route, triage, or tag content.
Copy prompt
You have access to the ScaleDown Classify API for routing, triaging, and labeling content at scale.

Endpoint: POST https://api.scaledown.xyz/classify
Headers: {"x-api-key": "<SCALEDOWN_API_KEY>", "Content-Type": "application/json"}
Request body fields:
- "text" (string, required): the content to classify
- "labels" (array, required): at least one label object; an empty array returns a 422 error. Each label object has:
  - "name" (string, required): short identifier for the category, e.g. "billing"
  - "rubric" (string, required): a yes/no question that determines if the label applies, e.g. "Is this about a billing issue or payment problem?"

When the user wants to categorize, tag, route, or triage text:
1. Define each category as a label with a name and a rubric question
2. POST to the endpoint
3. Read "top_label" from the response for the winning category, and "scores" for relative probabilities across all labels

Response fields: top_label (string), scores (object mapping label name → probability, all sum to 1.0).

Scores are relative probabilities, not absolute confidence values. Performance is best with up to ~20 labels.
Combining prompts

You can include multiple ScaleDown prompts in a single system message to give your agent access to all four models. Simply concatenate the prompts with a blank line between each one.

For agents that handle diverse tasks (e.g. a general-purpose assistant that both summarizes documents and routes support tickets), include both the Summarize and Classify prompts.

⚠
Make sure your agent has network access to api.scaledown.xyz and can make outbound HTTP requests. For Claude Code and similar tool-use agents, no special configuration is needed.
← Classify
Next: Python Package →

---8<--- page: scaledown-ai-docs-guides-rag ---8<---

Page URL: https://scaledown.ai/docs/guides/rag/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

GUIDES

RAG with Compression

Reduce retrieval costs by compressing chunks before they hit your LLM - without changing your retrieval logic.

Overview

In a standard RAG pipeline, retrieved chunks are concatenated and passed directly to a frontier LLM. The problem: retrieved text is often noisy, redundant, and much longer than what the LLM actually needs.

Inserting ScaleDown's Compress model between retrieval and generation strips that noise before it hits your token budget. The compressed output is query-aware - only the content relevant to the user's question is retained.

Query
→
Retrieve chunks
→
ScaleDown Compress
→
LLM
→
Answer
Why compress before the LLM?
Cost - 50–70% fewer tokens passed to your LLM means 50–70% lower generation costs
Speed - shorter contexts = faster first token from your LLM
Quality - removing irrelevant noise can improve answer accuracy by reducing hallucination surface area
Context limits - compress large retrieval sets that would otherwise overflow the context window
Basic implementation
Python
TypeScript
Copy
import requests

def rag_with_compression(query: str, retrieved_chunks: list[str], llm_client) -> str:
    # 1. Join retrieved chunks into a single context
    raw_context = "\n\n".join(retrieved_chunks)

    # 2. Compress with ScaleDown
    compress_resp = requests.post(
        "https://api.scaledown.xyz/compress/raw/",
        headers={"x-api-key": "YOUR_SCALEDOWN_KEY"},
        json={
            "context": raw_context,
            "prompt": query,
            "scaledown": {"rate": "auto"},
        },
    )
    compressed = compress_resp.json()["compressed_prompt"]

    # 3. Pass compressed context to your LLM
    answer = llm_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer based on the context provided."},
            {"role": "user", "content": f"Context:\n{compressed}\n\nQuestion: {query}"},
        ],
    )
    return answer.choices[0].message.content
Chunk-level vs. batch compression

You can compress all retrieved chunks together (recommended) or individually:

Together (recommended)

Pass all chunks as a single context string. ScaleDown preserves cross-chunk context and removes cross-chunk redundancy. Best for coherent documents or closely related chunks.

Individually

Call compress once per chunk, then concatenate. Useful when chunks are from unrelated sources and you want per-chunk budget control. Use a fixed rate (e.g. 0.5) to predictably cap each chunk.

Python - per-chunk
Copy
def compress_chunks_individually(query: str, chunks: list[str]) -> list[str]:
    compressed = []
    for chunk in chunks:
        r = requests.post(
            "https://api.scaledown.xyz/compress/raw/",
            headers={"x-api-key": "YOUR_SCALEDOWN_KEY"},
            json={
                "context": chunk,
                "prompt": query,
                "scaledown": {"rate": 0.5},  # fixed 50% compression per chunk
            },
        )
        compressed.append(r.json()["compressed_prompt"])
    return compressed
Tips for production
Use "auto" rate for general-purpose RAG. The model selects the ideal compression based on content density and query relevance.
For strict latency budgets, compress at indexing time (pre-compress your chunks when ingesting documents) rather than at query time.
Monitor compression_rate in production - if it consistently returns above 0.85, your chunks may already be highly dense and compression is adding overhead without much gain.
Compression works best on prose-heavy content (documents, transcripts, articles). For already-structured data like tables or JSON, consider using the Extract endpoint instead.
ℹ
Typical RAG pipelines see 55–65% cost reduction on the LLM generation step after inserting compression. At $15/M tokens for GPT-4o, that's roughly $8–9 saved per million input tokens.
← Quickstart
Next: Classify →

---8<--- page: scaledown-ai-docs-research-generic-prompt-reduction ---8<---

Page URL: https://scaledown.ai/docs/research/generic-prompt-reduction/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

RESEARCH

Generic Prompt Reduction

How ScaleDown's compression model works, and when to use it across different prompt structures.

The problem with long prompts

LLM costs scale linearly with input tokens. For many production workloads - document Q&A, RAG pipelines, long-context summarization, agentic tool traces - the majority of spend is in the input, not the output. Yet most of that input is noise: repeated instructions, boilerplate, retrieved text that's only tangentially relevant to the query.

Generic prompt reduction addresses this by asking: what is the minimum token representation of this prompt that preserves the information needed to answer the query?

Query-aware compression

ScaleDown's compression is not generic text summarization. It is query-aware: the model reads both the context and the query, and preserves only the facts, entities, and relationships that are relevant to answering that specific query.

This is a key distinction from simple text truncation or extractive summarization. Consider a 2,000-token contract asked the question "What are the payment terms?" - a query-aware compressor can discard the 1,600 tokens covering IP ownership, governing law, and termination clauses, and retain only the 400 tokens that describe payment schedules and invoicing obligations.

COMPRESSION INTERNALS (SIMPLIFIED)
1.
Encode context and query jointly → token-level relevance scores
2.
Select tokens above relevance threshold (Pareto-optimal subset)
3.
Reconstruct coherent text from selected tokens (fluency pass)
4.
Return compressed_prompt - ready for direct LLM input
When to use compression
High-value use cases
RAG retrieval context - retrieved chunks before passing to a frontier LLM
Long document Q&A - contracts, filings, research papers
Conversation history - condense prior turns before a new query
Agent tool traces - compress prior observations in agentic loops
Batch processing - reduce cost on high-volume document pipelines
Low-value use cases
Short prompts (< 200 tokens) - overhead exceeds savings
Structured data (JSON, tables) - use Extract instead
Code generation contexts - code tokens are information-dense; compression rates are typically low
ℹ
Run a quick audit: if your average prompt is under 500 tokens, compression ROI is marginal. Above 1,000 tokens, it almost always pays off.
Auto vs. fixed rate

The rate: "auto" setting instructs the model to select the Pareto-optimal compression rate for the given context-query pair. This typically achieves 50–70% compression on prose-heavy content.

Fixed rates (e.g. rate: 0.4) are useful when you have a hard token budget - for example, when fitting into a 4K context window. The model will compress to exactly that fraction of the original token count, redistributing its relevance budget to fit.

Python - rate comparison
Copy
import requests

def compare_rates(context, prompt):
    for rate in ["auto", 0.7, 0.5, 0.3]:
        r = requests.post(
            "https://api.scaledown.xyz/compress/raw/",
            headers={"x-api-key": "YOUR_KEY"},
            json={"context": context, "prompt": prompt, "scaledown": {"rate": rate}},
        ).json()
        print(
            f"rate={rate:>5}: "
            f"{r['original_prompt_tokens']} → {r['compressed_prompt_tokens']} tokens "
            f"({r['compression_rate']:.0%} retained)"
        )
Pareto merging for multi-document inputs

When compressing multiple documents for a single query, passing them together (rather than individually) allows the model to perform cross-document deduplication. Repeated facts, overlapping definitions, and redundant boilerplate are merged across sources rather than preserved once per document.

This is especially effective for RAG pipelines retrieving from large knowledge bases where the same fact may appear in multiple chunks.

Python - multi-doc compression
Copy
# Pass all docs together for cross-document deduplication
all_docs = "\n\n---\n\n".join(documents)

result = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={"x-api-key": "YOUR_KEY"},
    json={
        "context": all_docs,
        "prompt": query,
        "scaledown": {"rate": "auto"},
    },
).json()

# Typically achieves higher compression than sum of individual calls
print(f"Combined compression: {result['compression_rate']:.0%} retained")
Quality vs. compression tradeoff

Compression rate and output quality trade off non-linearly. In most cases:

0.7–0.9 retained - minimal quality impact, moderate cost savings
0.4–0.7 retained - the sweet spot for most production workloads
0.2–0.4 retained - aggressive compression; suitable for simple factual queries, not complex reasoning
< 0.2 retained - not recommended except for extremely simple extraction tasks
⚠
Rates below 0.3 on dense technical content (code, legal text, financial filings) may cause fact loss. Test your specific content type before deploying aggressive compression in production.
← Python Package
Next: Compression for Reasoning Models →

---8<--- page: scaledown-ai-docs-research-modular-prompt-optimization ---8<---

Page URL: https://scaledown.ai/docs/research/modular-prompt-optimization/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

RESEARCH

Modular Prompt Optimization

A composable framework for reducing hallucinations in large language models through systematic prompt-optimization techniques.

Overview

This research presents a system for composing prompt-optimization techniques to reduce hallucinations in large language models. The framework treats prompt methods as modular, interchangeable components that can be combined and evaluated across different models and datasets.

We built a modular framework to compose prompt-optimization primitives - including Chain-of-Thought, Chain-of-Verification, Expert Persona, and uncertainty prompts - and evaluate hallucinations with precise metrics.

Key capabilities
Composable prompt primitives - Chain-of-Thought, Chain-of-Verification, Expert Persona, and uncertainty prompts can be freely combined
Cross-model evaluation - run combinatorial experiments across multiple LLMs simultaneously
Precise metrics - measure hallucination reduction using precision, recall, F1, and hallucination rate
Technical architecture

The framework separates concerns into four layers:

Model backends - pluggable LLM providers
Task definitions - datasets and evaluation criteria
Prompt optimizers - individual technique implementations
Evaluation - hallucination-centric metrics

This separation enables researchers to independently extend each component - adding new models, tasks, or optimization techniques requires minimal code changes.

Evaluation approach

Rather than optimizing solely for accuracy, the system prioritizes hallucination-centric metrics. Responses receive three-way labeling (correct / incorrect / abstention), generating metrics that balance answer quality against coverage.

This addresses a fundamental tension: abstention mechanisms often reduce hallucinations while decreasing answer coverage. The framework makes this trade-off explicit and measurable.

METRIC	DESCRIPTION
Precision	Fraction of answered questions that are correct
Recall	Fraction of all questions the model answers correctly (including abstentions)
F1	Harmonic mean of precision and recall
Hallucination rate	Fraction of answers that are factually incorrect
Pipeline overview

The pipeline orchestrates a multi-stage workflow. A question enters at Stage 1 (Baseline), where the target model generates an initial response. If confidence gates determine the answer is insufficient, processing advances to Stage 2 (APO) for prompt refinement, then potentially Stage 3 (CoVe) for verification-based fact-checking.

Three specialized model roles
Target Model - the primary, powerful model generating main answers
Helper Model - a smaller, cost-effective model handling auxiliary tasks like prompt rewriting or verification question generation
Judge Model - evaluates answer confidence to determine pipeline progression
Efficiency through gating

Gates serve as decision checkpoints. The JudgeGate employs a separate judge LLM to programmatically assess the quality of answers against confidence thresholds, preventing unnecessary computation costs. Only answers that fail the gate advance to more expensive stages.

Reproducibility

The framework includes ready-to-run CLI scripts, automatic checkpointing, and analysis notebooks. Code is available on GitHub for replication and extension.

bash
Copy
# Install with optional extras
pip install "scaledown[haste,semantic]"

# Run a baseline evaluation
python -m scaledown.eval --task qa --model gpt-4o --optimizer chain-of-thought

# Compose multiple optimizers
python -m scaledown.eval \
  --task qa \
  --model gpt-4o \
  --optimizers chain-of-thought,chain-of-verification \
  --judge gpt-4o-mini \
  --output results/cot_cov_gpt4o.json
ℹ
This research is integrated into ScaleDown's hallucination reduction pipeline. The pipeline works seamlessly with ScaleDown's core compression technology, allowing individual model roles to leverage token compression simultaneously.
← Generic Prompt Reduction
Prompt Compression for Reasoning →

---8<--- page: scaledown-ai-docs-research-pareto-merging ---8<---

Page URL: https://scaledown.ai/docs/research/pareto-merging/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

RESEARCH

Pareto Merging
Overview

Created as part of Eleuther SOAR by Nadya Devani, Pouya Sadeghi, Purva Kandalgaonkar, Suparnojit Sarkar

The Pareto Merging method is an advanced technique for combining multiple specialized AI models into a single, highly efficient model. Unlike traditional methods that create one static merged model, Pareto Merging produces a flexible framework that can generate an infinite number of model variations tailored to specific needs without retraining. This method merges two types of models: a concise, non-reasoning Large Language Model (LLM) and a powerful Large Reasoning Model (LRM). The key innovation is a two-part architecture:

Preference-Independent Base Model: A single, fixed base model combines the general knowledge of the LLM with the reasoning capabilities of the LRM.
Preference-Dependent Tensor: A small, trainable "control knob" that is adjusted on-the-fly based on a predicted question difficulty score.

This allows the system to be dynamic: for easy questions, it leans towards the concise base model to save costs, and for difficult questions, it engages more reasoning power to ensure high accuracy.

Architecture
[ Architecture diagram ]
Pareto Merging API
Overview

The ScaleDown Pareto Merging API provides dynamic, cost-effective reasoning. It merges a concise LLM with a powerful LRM, allowing you to balance response accuracy and token cost on a per-query basis. Instead of using a static model, our system adjusts its reasoning depth based on the predicted difficulty of your prompt, reducing costs by up to 30% while maintaining high accuracy.

Quick Start

Get started in minutes by using our hosted API endpoint or by running the model locally with our Python package.

Installation
bash
Copy
# Placeholder for package installation
pip install scaledown-paretomerge
ℹ
The Pareto Merging technique is applied automatically in ScaleDown's API based on detected prompt difficulty. No additional configuration is required to benefit from adaptive reasoning depth.
← Python Package
Generic Prompt Reduction →

---8<--- page: scaledown-ai-docs-research-prompt-compression-reasoning ---8<---

Page URL: https://scaledown.ai/docs/research/prompt-compression-reasoning/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

RESEARCH

Prompt Compression for Reasoning Models

Why reasoning models have a unique compression opportunity - and how to capture it.

The reasoning model cost problem

Reasoning models like OpenAI's o3, o4-mini, and Anthropic's Claude 3.7 Sonnet (extended thinking) generate large internal chain-of-thought (CoT) traces before producing a final answer. These traces can be 5–20× longer than the visible output, and they're billed at full token rates.

The typical cost structure for a reasoning model call:

COMPONENT	TYPICAL TOKEN COUNT	% OF TOTAL COST
User input (context)	1,000–10,000	10–25%
CoT reasoning trace	5,000–50,000	50–80%
Final answer	100–500	5–10%

Compressing the input context doesn't affect the CoT length directly, but it has two compounding effects: shorter context = less reasoning surface area = fewer CoT tokens generated. In practice, a 60% input compression yields approximately 30–45% reduction in CoT length on factual retrieval tasks.

When compression helps reasoning models most
Document-grounded tasks

When the reasoning model is answering questions over retrieved documents (e.g. "What does section 4.2 of this contract require?"), the CoT length scales with the amount of irrelevant context it has to reason through. Compressing to only the relevant sections dramatically reduces the reasoning trace.

Multi-step agentic loops

In agentic settings, prior observations (tool outputs, intermediate results) accumulate in the context window. Each turn, the reasoning model re-reads and reasons over the entire history. Compressing prior turns before each new step prevents exponential cost growth.

Batch evaluation

Evaluating reasoning model responses over large datasets (e.g. running a benchmark, grading outputs) is expensive because each evaluation call generates its own CoT. Compressing the evaluation context before each grading call can cut batch costs by 40–60%.

ℹ
Reasoning models are particularly sensitive to input quality. Because ScaleDown's compression is query-aware (not generic summarization), it preserves the precise facts the model needs to reason correctly - reducing CoT length without degrading answer accuracy.
Implementation patterns
Single-turn document Q&A
Python
Copy
import requests
from openai import OpenAI

openai = OpenAI()

def reason_over_document(document: str, question: str) -> str:
    # Step 1: compress with ScaleDown
    compress_result = requests.post(
        "https://api.scaledown.xyz/compress/raw/",
        headers={"x-api-key": "YOUR_SCALEDOWN_KEY"},
        json={
            "context": document,
            "prompt": question,
            "scaledown": {"rate": "auto"},
        },
    ).json()

    compressed = compress_result["compressed_prompt"]
    savings_pct = (1 - compress_result["compression_rate"]) * 100
    print(f"Compressed input by {savings_pct:.0f}% before reasoning call")

    # Step 2: send compressed context to reasoning model
    response = openai.chat.completions.create(
        model="o4-mini",
        messages=[
            {
                "role": "user",
                "content": f"Context:\n{compressed}\n\nQuestion: {question}"
            }
        ],
    )
    return response.choices[0].message.content
Agentic loop with history compression
Python
Copy
def run_agent_loop(task: str, tools: list, max_steps: int = 10):
    history = []
    current_query = task

    for step in range(max_steps):
        # Compress accumulated history before each reasoning call
        if history:
            history_text = "\n".join([
                f"[{h['role']}]: {h['content']}" for h in history
            ])
            compressed_history = requests.post(
                "https://api.scaledown.xyz/compress/raw/",
                headers={"x-api-key": "YOUR_SCALEDOWN_KEY"},
                json={
                    "context": history_text,
                    "prompt": current_query,
                    "scaledown": {"rate": 0.5},  # keep 50% of history
                },
            ).json()["compressed_prompt"]

            messages = [
                {"role": "system", "content": f"Prior steps (compressed):\n{compressed_history}"},
                {"role": "user", "content": current_query},
            ]
        else:
            messages = [{"role": "user", "content": current_query}]

        # Call reasoning model
        response = openai.chat.completions.create(
            model="o4-mini",
            messages=messages,
            tools=tools,
        )

        # Process response, update history...
        # (tool calls, observations, etc.)
        msg = response.choices[0].message
        history.append({"role": "assistant", "content": msg.content or ""})

        if not msg.tool_calls:
            return msg.content  # done

    return "Max steps reached"
Benchmark results

Internal testing on FinanceBench (financial document Q&A) with o4-mini:

SETUP	AVG INPUT TOKENS	AVG COT TOKENS	COST / 1K CALLS	F1 SCORE
o4-mini (no compression)	8,420	12,840	$18.50	0.199
ScaleDown + o4-mini	2,780	7,210	$7.20	0.255

The ScaleDown + o4-mini setup achieved higher F1 than uncompressed o4-mini at 61% lower cost. The improvement in accuracy is likely due to the compressed context surfacing the relevant financial figures more cleanly, reducing the model's tendency to hallucinate from noisy input.

✦
The combination of ScaleDown compression + a smaller reasoning model (o4-mini) frequently outperforms an uncompressed larger reasoning model (o3) at significantly lower cost. Test this pattern before defaulting to the largest model in your pipeline.
← Generic Prompt Reduction

---8<--- page: scaledown-ai-docs-research-python-package ---8<---

Page URL: https://scaledown.ai/docs/research/python-package/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Generic Prompt Reduction
Pareto Merging
Get API key →
← scaledown.ai

RESEARCH

Python Package

The official ScaleDown Python SDK - a thin, typed wrapper around the REST API.

Installation
pip
uv
poetry
Copy
pip install scaledown
Authentication

Set your API key as an environment variable or pass it directly:

Environment variable (recommended)
Python
Copy
# .env or shell
export SCALEDOWN_API_KEY="sk-..."
Compress
Python
Copy
from scaledown import ScaleDown

client = ScaleDown()

result = client.compress(
    context="Your long document or conversation history here...",
    prompt="What are the key points?",
    rate="auto",  # or a float like 0.5
)

print(result.compressed_prompt)
print(f"{result.compression_rate:.0%} compression")
print(f"{result.original_prompt_tokens} → {result.compressed_prompt_tokens} tokens")
PARAM	TYPE	DESCRIPTION
context*	str	The text to compress.
prompt*	str	The query used to guide compression.
rate*	str | float	"auto" or a float 0–1 specifying the target token fraction.
Summarize
Python
Copy
result = client.summarize(
    text="Full article, transcript, or document text...",
    instructions="Bullet points only. Focus on decisions and action items.",
    max_tokens=512,
)

print(result.summary)
Extract
Python
Copy
result = client.extract(
    text="John Smith signed the NDA on January 15, 2024. Contact: john@acme.com",
    entities={
        "Person": "Full name of a person",
        "Date": "A date or deadline",
        "Email": "An email address",
    },
    threshold=0.6,  # filter out low-confidence results
)

for entity in result.entities:
    print(f"{entity.type}: {entity.text} ({entity.confidence:.0%})")
Classify
Python
Copy
result = client.classify(
    text="My subscription was charged twice this month.",
    labels=[
        {"name": "billing", "rubric": "Is this about a payment or billing issue?"},
        {"name": "technical", "rubric": "Is this about a technical bug?"},
        {"name": "account", "rubric": "Is this about account access?"},
    ],
)

print(result.top_label)   # "billing"
print(result.scores)      # {"billing": 0.91, "technical": 0.05, "account": 0.04}
Async support
Python (async)
Copy
from scaledown import AsyncScaleDown

client = AsyncScaleDown()

async def process(text: str, query: str) -> str:
    result = await client.compress(context=text, prompt=query, rate="auto")
    return result.compressed_prompt
Error handling
Python
Copy
from scaledown import ScaleDown
from scaledown.exceptions import (
    AuthenticationError,
    RateLimitError,
    APIError,
)

client = ScaleDown()

try:
    result = client.compress(context="...", prompt="...", rate="auto")
except AuthenticationError:
    print("Invalid API key")
except RateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after}s")
except APIError as e:
    print(f"API error {e.status_code}: {e.message}")
ℹ
The Python package is a thin wrapper - all requests go directly to api.scaledown.xyz. There is no local inference. Response objects mirror the REST API response fields as typed dataclasses.
← Integration Prompts
Next: Generic Prompt Reduction →

---8<--- page: scaledown-ai-docs ---8<---

Page URL: https://scaledown.ai/docs/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
GETTING STARTED

Quickstart

CLASSIFY

Overview
API Reference
Integrate

EXTRACT

Overview
API Reference
Integrate

SUMMARIZE

Overview
API Reference
Integrate

COMPRESS

Overview
API Reference
Integrate

RESEARCH

Python Package
Documentation
Generic Prompt Reduction
Overview
Modular Prompt Optimization
Pareto Merging
Get API key →
← scaledown.ai

GETTING STARTED

Quickstart

Make your first ScaleDown API call in under five minutes.

✦
New accounts get 1M free tokens - no credit card required. Get your API key →
What is ScaleDown?

ScaleDown is an applied AI research lab building task-specific small language models (SLMs) for classification, extraction, summarization, and compression. Each model is purpose-trained for a single task - delivering frontier-quality results at 10× lower cost and 2× lower latency than general-purpose alternatives like GPT-4o or Claude.

Instead of routing every AI call through a large general-purpose model, ScaleDown lets you offload the repetitive, well-defined tasks to models built exactly for those jobs.

Before you start

You'll need:

A ScaleDown API key - sign up here to get 1M free tokens
Basic familiarity with HTTP / REST APIs
Your first request

The example below calls the Compress endpoint - ScaleDown's most popular model. It takes a long context and a query, and returns a semantically compressed version with 50–70% fewer tokens.

Python
TypeScript
cURL
Copy
import requests

response = requests.post(
    "https://api.scaledown.xyz/compress/raw/",
    headers={
        "x-api-key": "YOUR_SCALEDOWN_API_KEY",
        "Content-Type": "application/json",
    },
    json={
        "context": "Your long document, conversation history, or retrieved chunks go here...",
        "prompt": "What are the key obligations in this contract?",
        "scaledown": {"rate": "auto"},
    },
)

result = response.json()
compressed = result["compressed_prompt"]

print(f"Original tokens:   {result['original_prompt_tokens']}")
print(f"Compressed tokens: {result['compressed_prompt_tokens']}")
print(f"Compression rate:  {result['compression_rate']:.0%}")
Request parameters
PARAM	TYPE	DESCRIPTION
context*	string	The background text, document, or conversation history to compress.
prompt*	string	The user's main query or question. Used to guide query-aware compression.
scaledown.rate*	string | number	Use "auto" for automatic compression, or a fixed number between 0–1 (e.g. 0.5 = 50% of original tokens).
ℹ
Use "auto" mode unless you have a strict token budget. Rates below 0.3 may degrade quality on dense technical content.
Response structure
JSON
Copy
{
  "compressed_prompt": "Key obligations include: delivery by Q3, payment net-30...",
  "original_prompt_tokens": 1842,
  "compressed_prompt_tokens": 614,
  "compression_rate": 0.67,
  "original_chars": 9210,
  "compressed_chars": 3070,
  "successful": true,
  "latency_ms": 118
}
PARAM	TYPE	DESCRIPTION
compressed_prompt	string	The compressed output, ready to pass directly to your LLM as context.
original_prompt_tokens	number	Token count of the original input.
compressed_prompt_tokens	number	Token count of the compressed output.
compression_rate	number	Fraction of original tokens retained (e.g. 0.33 = 67% compression).
successful	boolean	Whether the compression succeeded.
latency_ms	number	Server-side processing time in milliseconds.
Next steps

Now that you've made your first call, explore the other models:

Summarize - Generate abstractive summaries of long documents and transcripts
Extract - Pull structured entities from unstructured text using plain-English schemas
Classify - Route, triage, and label content at scale with zero training
Next: RAG Guide
→

ADDITIONAL VISIBLE STATES / CHART VALUES
Expanded the Research sidebar groups to reveal linked Python Package and Generic Prompt Reduction pages.

---8<--- page: scaledown-ai-models-classify ---8<---

Page URL: https://scaledown.ai/models/classify/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back

SCALEDOWN CLASSIFY

Deterministic
Classification

ScaleDown Classify delivers deterministic, encoder-only classification at 2.5× lower latency, achieving 90.53% accuracy with no sampling variability. Handles up to 1M tokens per request.

DOCS
GET YOUR API KEY
Watch Classification in Action
SD CLASSIFY
INPUT STREAM

Refund not processed after 2 weeks, very disappointed.

Billing Issue

Love the new dashboard update, so much faster now!

Positive Feedback

How do I export my data to CSV?

Support Request

App keeps crashing on iOS 17.4 after latest update.

Bug Report
12k tokens/sec

---8<--- page: scaledown-ai-models-compress ---8<---

Page URL: https://scaledown.ai/models/compress/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back

SCALEDOWN COMPRESS

Query-Aware
Compression

ScaleDown Compress reduces downstream LLM token usage by 70%, and improved F1 by 22% by intelligently compressing any volume of context before it reaches the model.

DOCS
GET YOUR API KEY
Watch Compression in Action
Real World Case Study
SD COMPRESS
INPUT DOCUMENT

The quarterly earnings report for FY2024 shows revenue of $4.2B.

We also saw strong performance across all regional segments globally.

Weather conditions in Q3 were noted as a minor operational factor.

The board met twice to review internal governance documentation.

Net income increased 18% year-over-year driven by margin expansion.

Office supply procurement was streamlined across all twelve locations.

Customer retention rate reached an all-time high of 94.7% this year.

The core finding: revenue up 18%, retention up, margins expanding.

20k tokens/sec
CASE STUDY
Nummo's workloads pull large token volumes from email and Slack into GPT-5.4.
ScaleDown compresses that context by 90% before the call while keeping accuracy consistent.
100%
ACCURACY RETAINED
90%
COST REDUCTION
50%
LATENCY SAVINGS
"For us it was the difference between a business that works and one that doesn't."
Matt Lee, CEO @ Nummo

---8<--- page: scaledown-ai-models-extract ---8<---

Page URL: https://scaledown.ai/models/extract/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back

SCALEDOWN EXTRACT

High-Fidelity
Extraction

ScaleDown Extract cuts extraction costs by over 98%, returning structured entities in under 50ms. Handles up to 1M tokens per request.

DOCS
GET YOUR API KEY
Watch Extraction in Action
Real World Case Study
SD EXTRACT
INPUT TEXT

On March 14, 2025, Sarah Chen signed a contract worth $2.4M with Acme Corp for cloud infrastructure services.

EXTRACTED JSON
{
"date": "March 14, 2025",
"signatory": "Sarah Chen",
"contract_value": "$2.4M",
"counterparty": "Acme Corp"
}
12k tokens/sec
CASE STUDY
Grotto runs 100,000s of real estate listing calls, previously served by Gemini 2.5 Flash.
ScaleDown Extract now helps pull keywords and mentions from call transcripts, improving accuracy, cutting cost, and reducing latency.
3.2%
ACCURACY INCREASE
47%
COST REDUCTION
15%
LATENCY SAVINGS
"I've always believed experts would serve small, specialized models at scale. ScaleDown is the team to do this, clearly proven by our exemplary results and their incredible continued support as we grow."
Ben Epstein, Chief Technology Officer @ Grotto

---8<--- page: scaledown-ai-models-summarize ---8<---

Page URL: https://scaledown.ai/models/summarize/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
Back

SCALEDOWN SUMMARIZE

State of the Art
Summarization

ScaleDown Summarize delivers concise, information-dense summaries while reducing costs by up to 98%. Handles up to 1M tokens per request.

DOCS
GET YOUR API KEY
Watch Summarization in Action
Real World Case Study
SD SUMMARIZE
INPUT

Q3 saw record-breaking engagement across all product lines, with mobile DAU surpassing 12M for the first time.

The infrastructure team completed a major migration to distributed compute, reducing p99 latency by 34%.

Several enterprise contracts were renewed at higher tiers, contributing to a 22% jump in ARR.

SUMMARY

5k tokens/sec
CASE STUDY
AnyTeam's Deep Research feature conducts extensive web scraping to prepare sellers for upcoming prospect calls.
ScaleDown Summarize distills that context into highly relevant summaries, improving accuracy while reducing cost and latency.
65%
MORE ACCURATE
92%
CHEAPER
22%
FASTER
"ScaleDown helps scale our agentic research workflows while also reducing costs and improving the accuracy of the outputs we deliver to our end users."
Jeff Yoshimura, Co-Founder @ AnyTeam

---8<--- page: scaledown-ai-pricing ---8<---

Page URL: https://scaledown.ai/#pricing
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
[NEW]
diet_code · save tokens in Claude Code without changing how you work
Constrained decoding models

ScaleDown is an applied research lab building task specific models for classification, extraction, summarization and compression.

GET STARTED
Or get 20% off on OpenRouter
BOOK A DEMO
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER
COMPRESSION
SUMMARIZATION
EXTRACTION
CLASSIFICATION

OUR PARTNERS & CUSTOMERS

1 model, 1 architecture, 1 task
CLASSIFY
EXTRACT
SUMMARIZE
COMPRESS
[01]
Classify

Sort text and images fast. Built for high-throughput tagging, triage, and filtering.

Define your label taxonomy in plain text. Classify millions of items per hour, from short messages and images to documents up to 1M tokens, with consistent, calibrated outputs. No fine-tuning required.

LEARN MORE
DOCS
EXAMPLE · LABELS: BILLING | BUG | FEATURE REQUEST
"I was charged twice this month"
billing
"Export crashes on Safari"
bug
"Can you add SSO?"
feature request
"Refund still hasn’t arrived"
billing
Live in under a minute

01Create account

Get started in under a minute.

1M free tokens included.

CONTINUE
OR
Continue with Google

02Generate API key

Generate a key from your dashboard.

Access all four models.

SCALEDOWN_API_KEY
sk-••••••••••••

WORKS WITH ALL FOUR

CLASSIFY
EXTRACT
SUMMARIZE
COMPRESS

03Make first request

Compatible with any HTTP client or SDK.

payload = {
"context": "...",
"prompt": "...",
"scaledown": { "rate": "auto" }
}
requests.post(url, json=payload)
State of the art on the benchmarks that matter
CLASSIFY
EXTRACT
SUMMARIZE
COMPRESS
Classification
CLINC OOS

ACCURACY (%)

DS Flash
Claude Haiku
Qwen 27B
GPT-5.4 Mini
Grok 4.2
Gemini Lite
ScaleDown
68%
75%
82%
95%

COST PER 1K CALLS

Grok 4.2
Claude Haiku
Qwen 27B
Gemini Lite
GPT-5.4 Mini
DS Flash
ScaleDown
$0
$0.3
$0.6
$0.9
$1.2

SPEED (TOKENS/SEC)

GPT-5.5
GPT-5.4 Mini
GPT-5.4 Nano
ScaleDown
100
500
2k
12k
Security & Compliance

Built to SOC 2, HIPAA, GDPR and ISO 27001 standards
Zero data retention · Self-hosted · Enterprise access controls · No training on your data

Zero Data Retention

Self-Hosted Deployment

Enterprise Access Controls

No Model Training on Your Data

Pricing
MODEL	TEXT INPUT	IMAGE INPUT	OUTPUT	CONTEXT
Classify

Calibrated label probabilities

	$0.05 / 1M tokens	$0.15 / 1M tokens	Free	1M tokens
Extract

Structured fields from text

	$0.05 / 1M tokens	$0.15 / 1M tokens	Free	1M tokens
Summarize

Faithful, length-controlled summaries

	$0.05 / 1M tokens	$0.15 / 1M tokens	Free	1M tokens
Compress

Shorten prompts and chat context

	$0.05 / 1M tokens	-	Free	1M tokens
2 ways to use ScaleDown

$0.05

/ 1M TOKENS

New accounts get 1M tokens free
All four models included
1M context window, unlimited compression
Flat pricing, no tiers
GET API KEY

Enterprise

/ DEDICATED OR LICENSED

Dedicated instance
License to run it on your own hardware
Dedicated support and SLAs
REQUEST QUOTE
Frequently Asked Questions
How much work is it to integrate ScaleDown?
Do you charge for output tokens?
Is there a limit on how much I can compress?
How fast are the models?
How much context can the models handle?
Can I self-host ScaleDown at my company?
Is my data used to train ScaleDown models?
Try ScaleDown
GET API KEY
BOOK A CALL
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER

MODELS

Classify
Extract
Summarize
Compress

RESOURCES

Cookbooks
Docs
Blog
Listicles

COMMUNITY

GitHub
Discord
LinkedIn
X

BENCHMARKS

ScaleDown vs OpenAI
ScaleDown vs Anthropic
ScaleDown vs Gemini
ScaleDown vs Grok
ScaleDown vs DeepSeek
ScaleDown vs Qwen
ScaleDown vs Kimi

ASK YOUR AI ASSISTANT ABOUT SCALEDOWN

SCALEDOWN · APPLIED RESEARCH LAB
Terms of Service
Privacy Policy
DPA
Cookie Policy
© 2026 · All Rights Reserved
MANIFESTO
100

---8<--- page: scaledown-ai ---8<---

Page URL: https://scaledown.ai/
Dates shown (publication/updated/changelog): None shown

FULL VISIBLE TEXT
scaledown
MODELS
Classify
Extract
Summarize
Compress
BENCHMARKS
COOKBOOKS
BLOG
PRICING
DOCS
BOOK A CALL
LOGIN / SIGN UP
[NEW]
diet_code · save tokens in Claude Code without changing how you work
Constrained decoding models

ScaleDown is an applied research lab building task specific models for classification, extraction, summarization and compression.

GET STARTED
Or get 20% off on OpenRouter
BOOK A DEMO
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER
COMPRESSION
SUMMARIZATION
EXTRACTION
CLASSIFICATION

OUR PARTNERS & CUSTOMERS

1 model, 1 architecture, 1 task
CLASSIFY
EXTRACT
SUMMARIZE
COMPRESS
[04]
Compress

Lossless, query-aware compression. Strip the noise out of long context without losing the signal.

Send in a prompt or document up to 1M tokens. Get back a semantically compressed version that preserves every fact relevant to your query, at a fraction of the token count. Unlimited volume.

LEARN MORE
DOCS
EXAMPLE · QUERY: "WHAT WAS Q3 REVENUE?"
[48,000] tokens
OUTPUT
[6,200] tokens · every relevant fact kept
Live in under a minute

01Create account

Get started in under a minute.

1M free tokens included.

CONTINUE
OR
Continue with Google

02Generate API key

Generate a key from your dashboard.

Access all four models.

SCALEDOWN_API_KEY
sk-••••••••••••

WORKS WITH ALL FOUR

CLASSIFY
EXTRACT
SUMMARIZE
COMPRESS

03Make first request

Compatible with any HTTP client or SDK.

payload = {
"context": "...",
"prompt": "...",
"scaledown": { "rate": "auto" }
}
requests.post(url, json=payload)
State of the art on the benchmarks that matter
CLASSIFY
EXTRACT
SUMMARIZE
COMPRESS
Compression
FINANCEBENCH

F1 SCORE

GPT-5.2
ScaleDown
0.15
0.18
0.21
0.24
0.28

COST PER 1K CALLS

GPT-5.2
ScaleDown
$0
$5
$10
$15
$20

SPEED (TOKENS/SEC)

GPT-5.5
GPT-5.4 Mini
GPT-5.4 Nano
ScaleDown
100
500
2k
20k
Security & Compliance

Built to SOC 2, HIPAA, GDPR and ISO 27001 standards
Zero data retention · Self-hosted · Enterprise access controls · No training on your data

Zero Data Retention

Self-Hosted Deployment

Enterprise Access Controls

No Model Training on Your Data

Pricing
MODEL	TEXT INPUT	IMAGE INPUT	OUTPUT	CONTEXT
Classify

Calibrated label probabilities

	$0.05 / 1M tokens	$0.15 / 1M tokens	Free	1M tokens
Extract

Structured fields from text

	$0.05 / 1M tokens	$0.15 / 1M tokens	Free	1M tokens
Summarize

Faithful, length-controlled summaries

	$0.05 / 1M tokens	$0.15 / 1M tokens	Free	1M tokens
Compress

Shorten prompts and chat context

	$0.05 / 1M tokens	-	Free	1M tokens
2 ways to use ScaleDown

$0.05

/ 1M TOKENS

New accounts get 1M tokens free
All four models included
1M context window, unlimited compression
Flat pricing, no tiers
GET API KEY

Enterprise

/ DEDICATED OR LICENSED

Dedicated instance
License to run it on your own hardware
Dedicated support and SLAs
REQUEST QUOTE
Frequently Asked Questions
How much work is it to integrate ScaleDown?

One API call. ScaleDown is a drop-in REST API compatible with any HTTP client or SDK. Most teams are in production within a day.

Do you charge for output tokens?

No. ScaleDown does not charge for output tokens. We exclusively charge for input tokens because most of our models (Compress, Extract, and Classify) are encoder-only architectures. Summarize has a decoder/generative step, but for our customers we will eat that cost.

Is there a limit on how much I can compress?

No. Compression is unlimited. There are no caps on request volume, document count, or total tokens compressed. Pricing stays flat at $0.05 per 1M tokens no matter how much you send.

How fast are the models?

ScaleDown models are 20x faster than frontier models on equivalent tasks. Latency is measured in milliseconds, not seconds, making them suitable for real-time pipelines and high-throughput batch workloads.

How much context can the models handle?

Summarize, Extract, and Classify each ship with a 1M-token context window whereas Compress is unlimited.

Can I self-host ScaleDown at my company?

Yes. ScaleDown supports fully self-hosted deployments inside your VPC with no outbound calls, as well as air-gapped deployments for environments that cannot reach the public internet.

Is my data used to train ScaleDown models?

No. Your inputs, outputs, and API keys are never logged, stored, or used to train or improve ScaleDown models.

Try ScaleDown
GET API KEY
BOOK A CALL
SOTA
ACCURACY
467x
CHEAPER
200x
FASTER

MODELS

Classify
Extract
Summarize
Compress

RESOURCES

Cookbooks
Docs
Blog
Listicles

COMMUNITY

GitHub
Discord
LinkedIn
X

BENCHMARKS

ScaleDown vs OpenAI
ScaleDown vs Anthropic
ScaleDown vs Gemini
ScaleDown vs Grok
ScaleDown vs DeepSeek
ScaleDown vs Qwen
ScaleDown vs Kimi

ASK YOUR AI ASSISTANT ABOUT SCALEDOWN

SCALEDOWN · APPLIED RESEARCH LAB
Terms of Service
Privacy Policy
DPA
Cookie Policy
© 2026 · All Rights Reserved
MANIFESTO
0.28
Every AI query you send runs on metal, power, and water. We've just gotten really good at forgetting that.

We talk about AI like it lives in an actual cloud somewhere far away. Unfortunately it doesn't. It lives in buildings the size of airports, full of copper and cooling pipes, pulling power from the grid 24/7 and sucking up 5 Olympic pools worth of water every day. The race to superintelligence is being built out of Earth's finite resources.

Most people don't know this, but ScaleDown started as Carbon ScaleDown, and it started in those buildings. I used to spend my days inside some of the biggest data centers in the world. Server racks and blinking lights as far as I could see, powering something like 20% of the internet. It felt like taking the red pill in the Matrix and finally being unplugged, seeing the world for what it truly was. Once you've stood in that room, you can't unsee it.

And here's the thing: most of what we ask LLMs to do is simple. Summarize this ticket. Pull a date out of a PDF. Tag this email. We're using an 18-wheeler to drive to work, and paying for it in money, in time, and in energy we could've spent on the thing we actually wanted to build. Death by a thousand paper cuts.

It's not just an AI problem either. Same fat shows up in the food we eat, the clothes we buy, the way we build software. We reach for whatever's easiest, not what is actually best for the outcomes we want. Choosing the path of least resistance is not the way.

So we built ScaleDown: constrained decoding models that each do one job (classification, extraction, and summarization). 20x faster, 100x cheaper, and more accurate and consistent than a giant model trying to do everything. Scalpel, not sledgehammer. Save the big reasoning models for the tasks that actually need them.

The bigger goal is below the API. Every task we pull off an oversized model means more out of every GPU, fewer square feet of data center, less power and water. We can't make more of any of that overnight. We can waste less of it.

And you shouldn't have to care about any of this to make the right call. If it's cheaper, faster, and better, you just pick it. That's the whole idea.

Maybe you don't care about trees or carbon or any of that bullshit. Totally fine. But there's a better way to do most things, and I think we owe it to the people who come after us to find it. We got handed a pretty messy situation, but we also have the tools to do something about it.

So make the 1% shift wherever you can. We're trying to make it stupid easy on the AI side.

ScaleDown Team

Close

ADDITIONAL VISIBLE STATES / CHART VALUES
HOMEPAGE MODEL TAB CONTENT
=== EXTRACT ===
1 model, 1 architecture, 1 task
CLASSIFY
EXTRACT
SUMMARIZE
COMPRESS
[02]
Extract

Semantic NER using natural language. Define what you want in plain English and pull it out of text or images as structured data.

Describe your entities in plain English: names, dates, product SKUs, any schema you define. Send text, images, or scanned documents up to 1M tokens and get clean JSON every time.

LEARN MORE
DOCS
EXAMPLE · INPUT

“Acme Corp renews on March 3, 2027 for $48,000 under SKU AC-220.”

SCHEMA · company, renewal_date, amount, sku
OUTPUT
{
"company": "Acme Corp",
"renewal_date": "2027-03-03",
"amount": 48000,
"sku": "AC-220"
}


=== SUMMARIZE ===
1 model, 1 architecture, 1 task
CLASSIFY
EXTRACT
SUMMARIZE
COMPRESS
[03]
Summarize

Summarization better than frontier model quality, 10x lower price, 20x lower latency.

Built for pipelines that need human-quality summaries at scale. Summarize text, images, and documents up to 1M tokens in a single call, with no chunking and no truncation.

LEARN MORE
DOCS
EXAMPLE · INPUT
[Meeting transcript · 30,000 tokens]
OUTPUT

• Key decision from the meeting

• Owner and next step

• Open question or risk



=== COMPRESS ===
1 model, 1 architecture, 1 task
CLASSIFY
EXTRACT
SUMMARIZE
COMPRESS
[04]
Compress

Lossless, query-aware compression. Strip the noise out of long context without losing the signal.

Send in a prompt or document up to 1M tokens. Get back a semantically compressed version that preserves every fact relevant to your query, at a fraction of the token count. Unlimited volume.

LEARN MORE
DOCS
EXAMPLE · QUERY: "WHAT WAS Q3 REVENUE?"
[48,000] tokens
OUTPUT
[6,200] tokens · every relevant fact kept


FAQ ANSWERS
Q: How much work is it to integrate ScaleDown?
One API call. ScaleDown is a drop-in REST API compatible with any HTTP client or SDK. Most teams are in production within a day.

Q: Do you charge for output tokens?
One API call. ScaleDown is a drop-in REST API compatible with any HTTP client or SDK. Most teams are in production within a day.
No. ScaleDown does not charge for output tokens. We exclusively charge for input tokens because most of our models (Compress, Extract, and Classify) are encoder-only architectures. Summarize has a decoder/generative step, but for our customers we will eat that cost.

Q: Is there a limit on how much I can compress?
One API call. ScaleDown is a drop-in REST API compatible with any HTTP client or SDK. Most teams are in production within a day.
No. ScaleDown does not charge for output tokens. We exclusively charge for input tokens because most of our models (Compress, Extract, and Classify) are encoder-only architectures. Summarize has a decoder/generative step, but for our customers we will eat that cost.
No. Compression is unlimited. There are no caps on request volume, document count, or total tokens compressed. Pricing stays flat at $0.05 per 1M tokens no matter how much you send.

Q: How fast are the models?
One API call. ScaleDown is a drop-in REST API compatible with any HTTP client or SDK. Most teams are in production within a day.
No. ScaleDown does not charge for output tokens. We exclusively charge for input tokens because most of our models (Compress, Extract, and Classify) are encoder-only architectures. Summarize has a decoder/generative step, but for our customers we will eat that cost.
No. Compression is unlimited. There are no caps on request volume, document count, or total tokens compressed. Pricing stays flat at $0.05 per 1M tokens no matter how much you send.
ScaleDown models are 20x faster than frontier models on equivalent tasks. Latency is measured in milliseconds, not seconds, making them suitable for real-time pipelines and high-throughput batch workloads.

Q: How much context can the models handle?
One API call. ScaleDown is a drop-in REST API compatible with any HTTP client or SDK. Most teams are in production within a day.
No. ScaleDown does not charge for output tokens. We exclusively charge for input tokens because most of our models (Compress, Extract, and Classify) are encoder-only architectures. Summarize has a decoder/generative step, but for our customers we will eat that cost.
No. Compression is unlimited. There are no caps on request volume, document count, or total tokens compressed. Pricing stays flat at $0.05 per 1M tokens no matter how much you send.
ScaleDown models are 20x faster than frontier models on equivalent tasks. Latency is measured in milliseconds, not seconds, making them suitable for real-time pipelines and high-throughput batch workloads.
Summarize, Extract, and Classify each ship with a 1M-token context window whereas Compress is unlimited.

Q: Can I self-host ScaleDown at my company?
One API call. ScaleDown is a drop-in REST API compatible with any HTTP client or SDK. Most teams are in production within a day.
No. ScaleDown does not charge for output tokens. We exclusively charge for input tokens because most of our models (Compress, Extract, and Classify) are encoder-only architectures. Summarize has a decoder/generative step, but for our customers we will eat that cost.
No. Compression is unlimited. There are no caps on request volume, document count, or total tokens compressed. Pricing stays flat at $0.05 per 1M tokens no matter how much you send.
ScaleDown models are 20x faster than frontier models on equivalent tasks. Latency is measured in milliseconds, not seconds, making them suitable for real-time pipelines and high-throughput batch workloads.
Summarize, Extract, and Classify each ship with a 1M-token context window whereas Compress is unlimited.
Yes. ScaleDown supports fully self-hosted deployments inside your VPC with no outbound calls, as well as air-gapped deployments for environments that cannot reach the public internet.

Q: Is my data used to train ScaleDown models?
One API call. ScaleDown is a drop-in REST API compatible with any HTTP client or SDK. Most teams are in production within a day.
No. ScaleDown does not charge for output tokens. We exclusively charge for input tokens because most of our models (Compress, Extract, and Classify) are encoder-only architectures. Summarize has a decoder/generative step, but for our customers we will eat that cost.
No. Compression is unlimited. There are no caps on request volume, document count, or total tokens compressed. Pricing stays flat at $0.05 per 1M tokens no matter how much you send.
ScaleDown models are 20x faster than frontier models on equivalent tasks. Latency is measured in milliseconds, not seconds, making them suitable for real-time pipelines and high-throughput batch workloads.
Summarize, Extract, and Classify each ship with a 1M-token context window whereas Compress is unlimited.
Yes. ScaleDown supports fully self-hosted deployments inside your VPC with no outbound calls, as well as air-gapped deployments for environments that cannot reach the public internet.
No. Your inputs, outputs, and API keys are never logged, stored, or used to train or improve ScaleDown models.

MANIFESTO DIALOG
- title: "ScaleDown AI | Task-specific SLMs" [url=https://scaledown.ai/]
- dialog "Every AI query you send runs on metal, power, and water. We've just gotten really good at forgetting" [ref=e110] [scrollable]:
  - heading "Every AI query you send runs on metal, power, and water. We've just gotten really good at forgetting" [level=2]: "Every AI query you send runs on metal, power, and water. We've just gotten really good at forgetting that."
  - text: "We talk about AI like it lives in an actual cloud somewhere far away. Unfortunately it doesn't. It lives in buildings the size of airports, full of copper and cooling pipes, pulling power from the grid 24/7 and sucking up 5 Olympic pools worth of water every day. The race to superintelligence is being built out of Earth's finite resources.Most people don't know this, but ScaleDown started as Carbon ScaleDown, and it started in those buildings. I used to spend my days inside some of the biggest data centers in the world. Server racks and blinking lights as far as I could see, powering something like 20% of the internet. It felt like taking the red pill in the Matrix and finally being unplugged, seeing the world for what it truly was. Once you've stood in that room, you can't unsee it.And here's the thing: most of what we ask LLMs to do is simple. Summarize this ticket. Pull a date out of a PDF. Tag this email. We're using an 18-wheeler to drive to work, and paying for it in money, in time, and in energy we could've spent on the thing we actually wanted to build. Death by a thousand paper cuts.It's not just an AI problem either. Same fat shows up in the food we eat, the clothes we buy, the way we build software. We reach for whatever's easiest, not what is actually best for the outcomes we want. Choosing the path of least resistance is not the way.So we built ScaleDown: constrained decoding models that each do one job (classification, extraction, and summarization). 20x faster, 100x cheaper, and more accurate and consistent than a giant model trying to do everything. Scalpel, not sledgehammer. Save the big reasoning models for the tasks that actually need them.The bigger goal is below the API. Every task we pull off an oversized model means more out of every GPU, fewer square feet of data center, less power and water. We can't make more of any of that overnight. We can waste less of it.And you shouldn't have to care about any of this to make the right call. If it's cheaper, faster, and better, you just pick it. That's the whole idea.Maybe you don't care about trees or carbon or any of that bullshit. Totally fine. But there's a better way to do most things, and I think we owe it to the people who come after us to find it. We got handed a pretty messy situation, but we also have the tools to do something about it.So make the 1% shift wherever you can. We're trying to make it stupid easy on the AI side.ScaleDown Team"
  - button "Close" [ref=e111] [focused]
- iframe:
  - iframe [ref=f3e1]

BENCHMARK CHART VALUES READ FROM HOVER TOOLTIPS (not just axis labels)
Classify / CLINC OOS accuracy: DS Flash 71.5%; Claude Haiku 79.5%; Qwen 27B 82.6%; GPT-5.4 Mini 87.07%; Grok 4.2 88.8%; Gemini Lite 89.7%; ScaleDown 90.53%.
Classify cost per 1K calls: Grok 4.2 $1.12; Claude Haiku $0.42; Qwen 27B $0.19; Gemini Lite $0.1862; GPT-5.4 Mini $0.16; DS Flash $0.037; ScaleDown $0.0008.
Classify speed tokens/sec: GPT-5.5 65.7; GPT-5.4 Mini 152.9; GPT-5.4 Nano 165.9; ScaleDown 12k (tooltip).
Extract / CUAD F1: DS Flash 0.227; Qwen 27B 0.231; GPT-5.4 Mini 0.3542; Grok 4.2 0.378; Gemini Lite 0.384; Claude Haiku 0.431; ScaleDown 0.4685.
Extract cost per 1K calls: Grok 4.2 $13.78; Claude Haiku $12.48; Qwen 27B $5.52; Gemini Lite $2.86; DS Flash $1.44; GPT-5.4 Mini $0.83; ScaleDown $0.33.
Extract speed tokens/sec: GPT-5.5 65.7; GPT-5.4 Mini 152.9; GPT-5.4 Nano 165.9; ScaleDown 12k (tooltip).
Summarize / QMSum ROUGE-L: Grok 4.2 0.137; Gemini Lite 0.151; Claude Haiku 0.152; Qwen 27B 0.154; DS Flash 0.17; GPT-5.4 Mini 0.195; ScaleDown 0.221.
Summarize cost per 1K calls: Grok 4.2 $16.8; Claude Haiku $15.4; GPT-5.4 Mini $10.8; Qwen 27B $6.56; Gemini Lite $3.65; DS Flash $1.55; ScaleDown $0.7.
Summarize speed tokens/sec: GPT-5.5 65.7; GPT-5.4 Mini 152.9; GPT-5.4 Nano 165.9; ScaleDown 5k (tooltip).
Compress / FinanceBench F1: GPT-5.2 0.1989; ScaleDown 0.2548.
Compress cost per 1K calls: GPT-5.2 $18.5; ScaleDown $7.2.
Compress speed tokens/sec: GPT-5.5 65.7; GPT-5.4 Mini 152.9; GPT-5.4 Nano 165.9; ScaleDown 20k (tooltip).
