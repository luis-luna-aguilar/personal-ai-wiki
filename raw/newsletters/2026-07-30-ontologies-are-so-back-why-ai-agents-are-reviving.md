---
title: "Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web"
type: newsletter
sender: "Latent.Space <swyx@substack.com>"
received: 2026-07-30
gmail_id: 19fb2c07ac1759c1
---

# Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web

**From:** Latent.Space <swyx@substack.com>
**Date:** 2026-07-30

View this post on the web at https://www.latent.space/p/ontologies-agentic-systems

One of the most watched videos from the recent AI Engineer World’s Fair is a 20-minute talk by  [ https://substack.com/redirect/cd99cdd9-5afb-4725-a84d-d673f8f96992?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]Frank Coyle [ https://substack.com/redirect/cd99cdd9-5afb-4725-a84d-d673f8f96992?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], a professor of computer science who currently teaches generative AI and LLMs at UC Berkeley. Drawing on his decades of experience, Coyle re-introduced the concept and practice of ontologies to today’s AI engineers.
Coyle argued that while LLMs are very effective at providing probabilistic reasoning, for agentic systems to be truly effective they need “logical guardrails” — by which he means ontologies.
In computer science, an ontology is “a description of data structure – of classes, properties, and relationships in a domain of knowledge” (as nicely defined by Oxford Semantic Technologies [ https://substack.com/redirect/aa95193f-5baf-41d2-895b-6bbf2f7647ec?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]). Coyle himself defined an ontology as simply “data as graphs.” He added that ontologies as a concept go right back to Aristotle, and have been used throughout the history of Artificial Intelligence.
The company Neo4j, known for its graph database systems, is also using ontologies in its agentic products.
In a keynote session at AIEWF [ https://substack.com/redirect/07e37e17-69cc-4c37-b22a-e2d1eccd8a54?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Neo4j CEO Emil Eifrem talked about three different types of ontologies to enable a “smarter shared substrate” to run agents at scale. The first is a business-facing ontology, describing the key concepts in an organization; next is a technical ontology, which Eifrem described as “all the metadata of all the data sources and data assets in your enterprise ecosystem”; and finally execution traces, which are “the runtime signals out of your agent.”
What’s Old is New Again: the Semantic Web
Frank Coyle thinks web ontologies are especially useful in building agentic systems. He mentioned Schema.org, FOAF, Dublin Core and other ontologies familiar to web developers — or at least, those of a certain vintage. He also mentioned “augmenting technologies” like RDFS (Resource Description Framework Schema) and OWL (Web Ontology Language).
One benefit of using these established ontologies is that they’re already in the training data of LLMs, so developers can just prompt for them — much better than reinventing ontologies from first principles.
“This stuff has been out there underlying a lot of what we already do,” Coyle said. “So take advantage of these things that already exist.”
As an example, he showed a Claude agent loop which used an ontology to help validate the LLM’s reasoning after the tool had run.
Coyle calls the convergence of probabilistic agents with ontologies “neurosymbolic AI.”
“Sounds pretty fancy,” he said, “but it’s really neural networks tied into symbolic AI — rule-based systems come under that category, as do the knowledge graphs that we’re assembling.”
He reiterated that neurosymbolic AI represents “a way to keep the LLM on its guardrails.”
The Pros and Cons of Ontologies
Someone who has been steeped in ontologies for many years and is now combining that with AI engineering is Kingsley Idehen, who runs a company called OpenLink Software [ https://substack.com/redirect/f6682b00-66de-4ae9-8e82-54735b3dff43?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. He’s been building an “agent engineering stack” that uses Semantic Web technologies — including [ https://substack.com/redirect/6b05b33d-449c-44a0-9b2e-09ddb8cda1fd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] an “agent with RDF memory.” 
I asked Idehen to explain to me the benefits of ontologies.
“The beauty of LLMs is that they are powerful processors of language,” he replied. “The beauty of an ontology is that it defines the types of entities and relationships through which language acquires computable context. Together, they bring the expressive power of language to computing’s UI/UX stack.”
That makes a lot of sense, but if you’ve been a web developer for a while you’ll know the challenges of ontologies: maintenance and keeping them up-to-date. It’s why the 1990s and 2000s vision for a “Semantic Web” — which was based on ontologies — never took off.
Current AI developer Prasenjit Sarkar offered a potential solution for the maintenance problem on X, arguing that [ https://substack.com/redirect/5f248b03-cf38-49a2-b3b3-62da280fb4a1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] “when an agent maintains the ontology as part of its own operation, updating definitions when it encounters edge cases, the maintenance problem changes character.” It’s still a hard problem though, he added.
Despite these issues, the structured nature of ontologies does appear to be a good match with the occasionally wayward tendencies of probabilistic LLMs. You get the power of LLMs, but ontologies will keep them in check.
Plus, as Neo4j’s Eifrem explained, ontologies allow us to move from “a world of thick agents with manually wired data sources” to a new world of “thin agents on a smarter shared ontology-based semantic layer.”
Loops and Guardrails
Back to Coyle’s presentation. He also had a great point about loop engineering, which he noted “has been around forever” in computer science. The problem, of course, is that loops can break or otherwise “go off the rails.”
Again, this is where an ontology system can act as a guardrail to a probabilistic LLM. One of Coyle’s slides referred to it as “a bounded set of rules around an unbounded loop.”
Near the end of his presentation, Coyle demonstrated how to use OWL as a check on agents. One slide showed that while language can be slippery, “an OWL axiom is a rule a machine enforces.”
He also showed how “you can have a reasoner built on ontology, to check [and] keep the LLM on track — have guardrails to keep it honest.”
Semantic Vibes
Perhaps ontologies are starting to resonate with AI engineers because a central concern at this time is quality control for loop engineering. We saw this debate play out at AIEWF [ https://substack.com/redirect/c4fe0eb4-781d-4838-aa45-6c8657016a3e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], with many conference speakers not willing to go all-in on fully automated “software factories [ https://substack.com/redirect/ceedfd98-25c6-463d-ad3a-cb5e8029dc30?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]” just yet. One of the key learnings from the event [ https://substack.com/redirect/f8351df7-26c2-4be7-ba3d-e7303f413fce?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] was that there need to be guardrails and humans in the loop.
Also it’s fascinating to see traditional web technologies make a resurgence in the field of AI engineering, especially after the 2025 trend of “vibe coding” made it seem like anyone could create software. Of course, since then the penny has dropped: we need to maintain that software and make sure it doesn’t break! So in 2026, we’re seeing a return to software engineering discipline — including now a revival of web ontologies as a way to keep probabilistic LLMs honest.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakl3T0RnME5qRXdNQ3dpYVdGMElqb3hOemcxTkRFd016Z3pMQ0psZUhBaU9qRTRNVFk1TkRZek9ETXNJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5oZVFJa2xWanZySTZmR2QxazFJcmtlSjBCSDVudnhDYlhNdEhFRGV3SERFIiwicCI6MjA4ODQ2MTAwLCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc4NTQxMDM4MywiZXhwIjoyMTAwOTg2MzgzLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.LRh0TrWKlTWFX1LE5QmGafDJETpamo8ELQbTbWSFCmA?
