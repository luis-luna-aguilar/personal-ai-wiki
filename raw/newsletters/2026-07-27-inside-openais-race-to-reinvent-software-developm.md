---
title: "Inside OpenAI’s Race to Reinvent Software Development for the Agent Era"
type: newsletter
sender: "Every <hello@every.to>"
received: 2026-07-27
gmail_id: 19fa53d186649cf2
---

# Inside OpenAI’s Race to Reinvent Software Development for the Agent Era

**From:** Every <hello@every.to>
**Date:** 2026-07-27

An exclusive look at how OpenAI’s infrastructure team is adapting to a flood of AI-generated code  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌
https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvLyIsInBvc2l0aW9uIjowfQ==


INSIDE OPENAI’S RACE TO REINVENT SOFTWARE DEVELOPMENT FOR THE AGENT ERA https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3Avb3BlbmFpLWluZnJhc3RydWN0dXJlIiwicG9zaXRpb24iOjF9


AN EXCLUSIVE LOOK AT HOW OPENAI’S INFRASTRUCTURE TEAM IS ADAPTING TO A FLOOD OF AI-GENERATED CODE https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3Avb3BlbmFpLWluZnJhc3RydWN0dXJlIiwicG9zaXRpb24iOjJ9

by Laura Entis https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL0BsYXVyYV8yN2JiYWZfMSIsInBvc2l0aW9uIjozfQ==

Midjourney/Every illustration.

Was this newsletter forwarded to you? Sign up https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL2FjY291bnQiLCJwb3NpdGlvbiI6NH0= to get it in your inbox.



----------------------------------------



Software development is about to change in ways many teams outside the frontier labs haven’t had to think about yet. Our new interactive piece, “Before the Deluge,” shows what that looks like from the inside.

We spoke with six members of OpenAI’s infrastructure team—including its vice president of applied infrastructure engineering—about three converging pressures: an overwhelming surge of AI-generated code, software-development infrastructure pushed to its limits, and a fundamental redesign of how code gets reviewed and kept reliable.

What they’re working through now is a preview of what’s coming for software development everywhere.

“Before the Deluge” reveals how those pressures interact, what the engineers are doing to hold the system together, and what the broader software community will need to reckon with as AI-generated code becomes routine. It’s a close look at a stress test already underway—at one of the organizations most responsible for accelerating it.

Read it here https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3Avb3BlbmFpLWluZnJhc3RydWN0dXJlP3NvdXJjZT1wb3N0X2J1dHRvbiIsInBvc2l0aW9uIjo1fQ==



----------------------------------------



Laura Entis https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL0BsYXVyYV8yN2JiYWZfMSIsInBvc2l0aW9uIjo2fQ== is a staff writer at Every. You can follow her on LinkedIn https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL3d3dy5saW5rZWRpbi5jb20vaW4vbGF1cmFlbnRpcy8iLCJwb3NpdGlvbiI6N30=.

To read more essays like this, subscribe to Every https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3N1YnNjcmliZSIsInBvc2l0aW9uIjo4fQ==, and follow us on X at @every https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwOi8vdHdpdHRlci5jb20vZXZlcnkiLCJwb3NpdGlvbiI6OX0= and on LinkedIn https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL3d3dy5saW5rZWRpbi5jb20vY29tcGFueS9ldmVyeWluYy8iLCJwb3NpdGlvbiI6MTB9.

Subscribe https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3N1YnNjcmliZT9zb3VyY2U9cG9zdF9idXR0b24iLCJwb3NpdGlvbiI6MTF9

WHAT DID YOU THINK OF THIS POST?

Amazing https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3Avb3BlbmFpLWluZnJhc3RydWN0dXJlL2ZlZWRiYWNrP3JhdGluZz1hbWF6aW5nXHUwMDI2aGFzaD0lcmVjaXBpZW50Lmhhc2glIiwicG9zaXRpb24iOjEyfQ== Good https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3Avb3BlbmFpLWluZnJhc3RydWN0dXJlL2ZlZWRiYWNrP3JhdGluZz1nb29kXHUwMDI2aGFzaD0lcmVjaXBpZW50Lmhhc2glIiwicG9zaXRpb24iOjEzfQ== Meh https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3Avb3BlbmFpLWluZnJhc3RydWN0dXJlL2ZlZWRiYWNrP3JhdGluZz1tZWhcdTAwMjZoYXNoPSVyZWNpcGllbnQuaGFzaCUiLCJwb3NpdGlvbiI6MTR9 Bad https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3Avb3BlbmFpLWluZnJhc3RydWN0dXJlL2ZlZWRiYWNrP3JhdGluZz1iYWRcdTAwMjZoYXNoPSVyZWNpcGllbnQuaGFzaCUiLCJwb3NpdGlvbiI6MTV9


GET MORE OUT OF YOUR SUBSCRIPTION

Try our AI tools for ultimate productivity

https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3Byb2R1Y3RzP3V0bV9zb3VyY2U9ZW1haWxcdTAwMjZ1dG1fbWVkaXVtPXBvc3RfcGF5d2FsbFx1MDAyNnV0bV9jYW1wYWlnbj1wYXl3YWxsX2dpZiIsInBvc2l0aW9uIjoxNn0=
Front-row access to the future of AI
In-depth reviews of new models on release day
Playbooks and guides for putting AI to work
Prompts and use cases for builders

Bundle of AI software
Sparkle: Organize your Mac with AI
Cora: The most human way to do email
Spiral: Repurpose your content endlessly
Monologue: Effortless voice dictation for your Mac

You received this email because you signed up for emails from Every https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvIiwicG9zaXRpb24iOjE3fQ==. Need help? Visit our help center https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2hlbHAuZXZlcnkudG8iLCJwb3NpdGlvbiI6MTh9. No longer interested in receiving emails from us? Click here to unsubscribe https://every.to/emails/click/136f006095268802530f927779a5f4d55a493840c0f1f77c950761a77b64df9e/eyJzdWJqZWN0IjoiSW5zaWRlIE9wZW5BSeKAmXMgUmFjZSB0byBSZWludmVudCBTb2Z0d2FyZSBEZXZlbG9wbWVudCBmb3IgdGhlIEFnZW50IEVyYSIsInBvc3RfaWQiOjQzNTcsInBvc3RfdHlwZSI6InBvc3QiLCJ1cmwiOiJodHRwczovL2V2ZXJ5LnRvL3Vuc3Vic2NyaWJlP3Bvc3Q9b3BlbmFpLWluZnJhc3RydWN0dXJlXHUwMDI2aGFzaD0lcmVjaXBpZW50Lmhhc2glIiwicG9zaXRpb24iOjE5fQ==.

221 Canal St 5th floor, New York, NY 10013
