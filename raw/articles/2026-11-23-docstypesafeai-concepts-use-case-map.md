---
title: Use cases - TypeSafe
type: source
source_type: article
url: https://docs.typesafe.ai/concepts/use-case-map
fetched: 2026-11-23
---

# Use cases - TypeSafe

Documentation Index

Fetch the complete documentation index at: /llms.txt

Use this file to discover all available pages before exploring further.

Skip to main content
TypeSafe home page
Search...
⌘K
TypeSafe console
Documentation
Build with Jev
Reference
Technical Blog
GET STARTED
Introduction
Quick start
Jev with coding agents
Use cases
CONCEPTS
System One
State
Primitives (Questions)
Choice
Score
Noul
Box
Dreamer-ready
Advanced: structure
Images
Dreamer-ready
Confidence
How to build with TypeSafe
AI primer
PATTERNS
Patterns
Speculative fan-out
Screen with a Noul first
Companion Noul
Routing by confidence
Routing by probability
Composite scoring
GET STARTED
Use cases
Copy page

Build business workflows where Jev makes the judgments and your code acts on them.

Use cases include checking invoices, moderating chat, guarding LLM apps, and searching documents. Pick a category to see its use cases and try the example behind each one, or read on for how they are built.
Use case categories
Business process automation
Check invoices, claims, and documents before money moves, and send the uncertain ones to a person. Code owns the control flow, not markdown files, so it runs a million times in the background without a human co-pilot.
Real-time apps
Frontier intelligence in about 150ms, fast enough for live UIs, voice assistants, games, and live chat moderation.
Search and labeling at scale
About 100x cheaper than a frontier LLM, so you can ask a question of every row, line, or record, then rank, filter, or label the results.
Agents and verification
Catch the jailbreaks, hallucinations, and citation errors other AIs make, at a fraction of the cost of the LLM call, and add routing, safety checks, and new abilities to agents.
Images and video
Find, read, and check what’s in scans, photos, and video frames.
Use cases and examples
Business process automation
For teams that check documents and claims before money moves, copy values out of documents by hand, or work through a queue of alerts.
Use case	What Jev judges	What your code does	Example
Decide whether an invoice can be paid	Questions about the invoice, purchase order, contract, vendor record, prior invoices, correspondence, delivery evidence, and approvals	Stops on fraud or duplicates, then holds, disputes line items, requests a corrected invoice, routes for approval, pays less than the invoiced amount, schedules, or pays	See the workflow ↗
Check OCR values and their bounding boxes on invoices	Where each value an OCR extractor read appears on the page, whether the page supports that value, and whether a crop of its box does too	Accepts the fields and sends low-scoring ones to review	Try it →
Extract pre-parsed values, such as invoice totals	Which of the candidates a regex found is the value you asked for	Copies that text exactly as it appears and converts it to a standard format	Try it →
Extract dates from documents	Which day, month, year, or relative date (such as “next Thursday”) a document names for each date you ask about	Works out the calendar date, checks that it is valid, and sends low-confidence ones to review	Try it →
Recover the structure of plain-text documents	Which lines continue the one before, and whether each block is a heading, list, code, or callout	Rebuilds the document as Markdown	Try it →
Classify SEC filings by industry	Which of 75 industry groups an SEC annual report belongs to	Reports the group, or the broader division above it when the answer’s confidence is low	Try it →
Brief a regulation in one request	Thirteen questions about the GDPR’s Wikipedia article, such as whether a data breach must be reported within 72 hours, whether the law applies outside the EU, and how large its fines can be	Gets all 13 answers from one request, about 12x cheaper and faster than asking them one at a time	Try it →
Triage security alerts	Whether the activity was unauthorized, whether a ticket or schedule explains it, and how strong the evidence is	Closes explained alerts, queues unclear ones, and acts to contain confirmed incidents	See the workflow ↗

Worked example: catch invoice fraud in an accounts-payable inbox

More ideas

Claims triage

Financial crime and know-your-customer (KYC) checks

Risk assessment

Real-time apps
For apps that need an answer in milliseconds, such as smart home assistants, ordering, presentation tools, and live chat moderation.
Use case	What Jev judges	What your code does	Example
Tick off a presenter’s notes as they speak	How well the live transcript covers each note not yet ticked	Ticks a note once its score passes the threshold	Try it →
Turn a cafe order into a shopping cart	Which menu items an order names, and the fields of each item	Builds a structured cart	Try it →
Control a smart home from plain-language requests	What kind of request it is, and which area, device, and action it targets	Runs the command, and passes questions and conversation to an LLM	Try it →
Filter Twitch chat	What kind of message it is (a question, cheering, chat, unasked-for gameplay advice, or spam), whether it insults someone, and whether it spoils the game	Hides insults, spam, and unasked-for advice, blurs spoilers, and highlights questions	Try it →
More ideas

Voice agents

Search and labeling at scale
For teams searching long documents, organizing product catalogs, merging datasets, or building predictive models from text.
Use case	What Jev judges	What your code does	Example
Line-by-line search of a long document	Which line answers a plain-language query, and whether the document answers it at all	Ranks the lines, and labels the document as answered, partly answered, or not answered	Try it →
Re-rank legal search results	Whether each candidate on a keyword-search shortlist could be the precedent a court opinion cites	Puts the most likely candidates first	Try it →
Find a half-remembered film among 5,000	Whether each film matches the person’s description, first from a short plot, then from a long plot for the top 80, then which of the top 20 it is	Shows one film when the top probability is high, or a short list when it isn’t	Try it →
Search Airbnb listings from a Google Sheets formula	Which listings in each group of 100 best match a plain-English request, then how well each shortlisted listing matches it	Keeps the top 5 from each group, turns each score into a mark out of 10, and returns the 10 best	Try it →
Hierarchical classification of patents, products, and medical topics	Which category fits an item at each level of a category tree	Follows the most likely branches down to the most specific category	Try it →
Align entities across knowledge graphs	Whether two records describe the same item, closely related items, or different items, and whether their title, artist, and label match	Recommends a merge for clear matches, sends in-between pairs to a curator, and leaves the rest unlinked	Try it →
Discover features for a predictive model	Questions about each record that an LLM proposes	Turns the answers into numeric input columns for the model, and accepts a change that rewords or drops a question only when it lowers the model’s error	Try it →
More ideas

Relationships and contradictions in records

Demand forecasting

Agents and verification
For teams whose agents or LLM features in production need checks, routing, or review.
Use case	What Jev judges	What your code does	Example
Guardrails for LLM inputs and outputs	Whether a message tries to override the app’s instructions, asks for help to cause harm or for medical advice, or hints at self-harm, and how much harm answering would do	Lets each message through, sends it for review, blocks it, or routes it to a crisis-support path, using thresholds you set	Try it →
Double-check citations	Whether the section a quote comes from supports the claim, contradicts it, or says nothing about it	Marks quotes missing from the source as fabricated, labels the rest verified, contradicted, or unsupported, and sends low-confidence labels to a person	Try it →
Check an LLM’s answer against the paragraphs it was given	Whether the paragraphs state every fact the question needs, whether the answer declines, and whether following the paragraphs step by step leads to the answer	Turns the three probabilities into a risk and sends answers above your threshold to review	Try it →
Review finished agent runs	Whether the agent was allowed to take its irreversible actions, whether the task got done, and how satisfied the user seemed	Alerts whoever is on call about actions that weren’t permitted, closes runs with no problems, and files issues for failures	See the workflow ↗
Classify RAG passages	Whether each retrieved passage is relevant to the question, contains an answer, contradicts what the question assumes, or tries to give the model instructions	Drops irrelevant passages and ones with injected instructions, and gives the answering model the rest, with contradicting passages marked as conflicting	Try it →
Model cascade: cheap first, escalate on failure	Whether each field a cheap model pulled out of the source is wrong, for example because the value doesn’t fit the field’s name, has the wrong type, or is empty when the source has that information	Accepts the cheap model’s answer, and pays for a reasoning model only when a check fails	Try it →
Suggest a skill for an agent	Whether the request needs a skill at all, which of 194 skills fit it, then which of the top 3 fits best and whether each one does what was asked	Asks about the top 3 again with their full descriptions, and suggests at most one skill, or none when the probabilities fall below your thresholds	Try it →
Choose a support assistant’s next actions	What the customer wants, how frustrated they are, and whether they report charges they don’t recognize or ask for a person	Applies safety rules first, then hands off to a person, refunds, freezes a card, or asks the customer to clarify	See the workflow ↗
Give an assistant a simple memory	Whether a request states a lasting fact about the customer, such as their plan or product edition	Saves those requests with Jev’s answers, and adds them to that customer’s later requests to Jev	Try it →
Function calling from plain-language requests	Which function the request needs, and, for each argument limited to a fixed list of values, which value it takes	Calls the matching function in your code with those values, and leaves out arguments the request doesn’t mention	Try it →
More ideas

Tool-call and data-leak checks

Scoring LLM answers

Model router: match each prompt to a model

Semantic code linting

Images and video
For teams reading scans, photos, or video frames by eye.
Use case	What Jev judges	What your code does	Example
Read a scanned vaccination record	Whether each vaccine is on the scan and where, which year each dose was given (or that it is unreadable), and whether each dose still protects on the departure date	Works out how long before the trip each dose was given, flags doubtful readings and out-of-date doses for a nurse, and crops the flagged rows	Try it →
Log bird visits from a feeder camera	Whether a frame shows a bird, where it is, and which species it is	Turns the answers into a visit log for each species	Try it →
More industries
Ideas for industries beyond the categories above.

Content moderation

Gaming

Customer support

Legal and compliance

Recruiting

Lead generation

E-commerce marketplaces

Advertising

Scientific discovery

Signs that you need Jev in your code workflow
You ask an LLM to return JSON, then parse, validate, and retry it. Jev answers each question as a typed primitive with its probability, so there’s no text to parse.
You have too much data to feed through a frontier LLM at a practical cost. In the customer service evaluation, a Jev workflow costs much less than the frontier models.
Your LLM workflow gives different answers to the same input. Ask narrow questions, and the probabilities show your code which answers are unsure. Self-consistency: choices and Self-consistency: nouls show how to measure how often answers change. Across the four evaluations, every model was more accurate as a structured workflow than with the same rules in one prompt.
Your LLM workflow is too slow. In the security incidents evaluation, a Jev workflow takes 0.3 seconds a case, against 3.4 to 66 seconds for the frontier models.
Someone on your team reads each item to decide what happens to it, and the decision depends on details an informed person would notice at a glance.
Mistakes are costly, so uncertain cases need to reach a person.
Designing your own workflow
Start from the action your system takes, and list the judgments it depends on. Turn each judgment into a question for Jev. Keep the rules that combine the answers into a decision in your code. Patterns by goal shows what each pattern is for, and How to build with TypeSafe covers how to design the questions and rules. If you build with a coding agent, install the TypeSafe agent skill so it can help you write the code.

Decision shapes

Was this page helpful?

Yes
No
Jev with coding agents
Previous
System One
Next
github
discord
x
Powered by
This documentation is built and hosted on Mintlify, a developer documentation platform
On this page
Use case categories
Use cases and examples
Business process automation
Real-time apps
Search and labeling at scale
Agents and verification
Images and video
More industries
Signs that you need Jev in your code workflow
Designing your own workflow
