---
title: "🔬Doing Vibe Physics — Alex Lupsasca, OpenAI"
type: newsletter
sender: "Latent.Space <swyx@substack.com>"
received: 2026-05-05
gmail_id: 19df9db0e488d8a2
---

# 🔬Doing Vibe Physics — Alex Lupsasca, OpenAI

**From:** Latent.Space <swyx@substack.com>
**Date:** 2026-05-05

View this post on the web at https://www.latent.space/p/lupsasca

Some people are going crazy over GPT 5.5. Some people. This is the story of the Jagged [ https://substack.com/redirect/17e6486a-c9a0-4249-acf9-3be2f01d8697?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] Frontier [ https://substack.com/redirect/92044f9a-5033-40e2-9ffa-1a6c9a4e26fc?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. People who use AI to write emails or even code implementation work find the lift moderate [ https://substack.com/redirect/82b3d9b6-56ba-47de-abef-d9b4a9b2390c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] whereas people pushing the limits of the model are figuring out that the limits just moved outwards [ https://substack.com/redirect/da33c031-7005-4166-8086-ab140e7ead2e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Alex Lupsaska [ https://substack.com/redirect/0ae627f7-85c1-44c1-beee-d32d4947f787?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] has been tracking this limit for a year and a half now. “When GPT5 came out, it was able to reproduce one of my best papers (that took a very long time to come up with) in 30 minutes.”
But Alex also notes that this shift was mostly invisible.
I remember when GPT-5 came out… on Twitter, the reception was lukewarm. A lot of people were like, well, we expected a lot more, and it’s not better at writing email. And I remember thinking, well, okay, GPT-3 could write email. How much better can it get at writing email? That’s not the point. But at the science frontier, the capabilities were really taking off.
The “Oscar for physics”
Alex made an early splash in his career with breakthroughs in our understanding of black holes. He’s also known for the an iPhone app that makes visualizing black holes fun and interactive to regular audiences [ https://substack.com/redirect/70375f30-2195-4a72-a472-72c9af35ae77?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. Alex won the 2024 New Horizons in Fundamental Physics Breakthrough Prize. Known as the “Oscar for physics” this is arguably the most prestigious prize an early stage theoretical physicist can win.
Alex first saw promise for AI in theoretical physics after he asked o3 for help on his research. In the podcast, Alex recalls asking GPT for help with a calculation that would have taken days, and getting a result in eleven minutes. He immediately recognized how impactful AI would be for his work even as though his physicist colleagues and the larger community gave it a lukewarm or skeptical reception.
The Move 37 Moment for AI x Physics
GPT-5 had just been released, and Alex tried asking it to solve a problem in a just published paper. GPT-5 said no answer. But Mark Chen, CRO of OpenAI [ https://substack.com/redirect/eabe1599-7283-4625-91dc-1ac01dca57b5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], pushed a bit harder, and had Alex prime the model with a textbook warmup problem, which it easily solved. After using this “priming” trick, GPT-5 was able to reproduce his full result in eleven minutes (yes, the paper was released after the model’s training cutoff).
“This changes everything.” Alex notes that we seem to be on the edge of a massive change in theoretical physics reasoning. A year prior LLMs were just starting do correct math. Now ChatGPT could reproduce his hardest paper in the time it takes to get a coffee.
Alex was on sabbatical at Vanderbilt, and he joined OpenAI to start pushing the boundary of AI’s ability to accelerate physics.
“AI solved the problem before the plane landed”
Alex began to put GPT through it’s paces, reaching out to colleagues for problems they were stuck on. His old PhD advisor (Prof. Andrew Storminger at Harvard [ https://substack.com/redirect/1e56ac7e-668b-40d6-9aa4-f1f53e4672b2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]) had an insidght about certain physical quantities known as “single-minus gluon tree amplitudes”. 
In certain cases, these amplitudes may be non-zero [ https://substack.com/redirect/46bcc2dc-4ce6-4c35-b60f-ab0dcb2f4bd3?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] when previously shown to always vanish. The team pushed this intuition forward, and came up with a formula for these quantities that appeared nonzero, but which was otherwise completely intractable. 
Spending over a year on this problem, no real progress was made.
Prof. Storminger planned to visit OpenAI to work on the problem the week after the initial conversation started. In that one week ChatGPT fully solved the problem, as Alex recalled, before Prof. Storminger’s plane even landed.
What was interesting is not only that ChatGPT solved this problem, but how it solved it. The model quickly realized found a limiting case (known as the “half-collinear regime”), that in hindsight has a nice intuitive explanation. Taking this limit, the gnarly results collapsed down to a simple and intuitive formula!
The last step was to prove this intuitive formula. The team started with a fresh session, gave a prompt with the context of what they previously learned, and let the model loose. Not only was ChatGPT able to reproduce the previous result, it was able to prove it using a technique unknown to the authors!
The Vibe Physics moment
With a concrete success in the bag, the team asked if they could generate new physics from scratch using ChatGPT. They took on what they felt to be a harder problem, looking at the graviton, a proposed particle that should appear when one combines gravity and quantum mechanics. They wrote up a simple prompt asking ChatGPT to perform the same research as the gluon paper but instead for gravitons. And then hit go!
What came next was truly “vibe physics”, with ChatGPT pushing out 110 pages of novel physics, new calculations, and novel techniques. This was over the course of a day, with most interactions the familiar following the now familiar pattern for anyone who uses a coding agent:
GPT: Here's your <long, detailed, awesome result>. 
     Would you like me to do <another really cool thing>?
Alex: Yes, please do!
GPT: <does the really cool thing>
And for those who look deeply, this really was not just a direct 1-1 mapping between gluons and gravitons. ChatGPT imported new techniques that were necessary due to the nature of gravitons, and used them flawlessly.
They spent the next three weeks verifying all the results. And voila! A new paper [ https://substack.com/redirect/e8a0e468-6f06-4913-b8a9-9157b1420085?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] featuring novel results in quantum gravity, generated in less than three days total. Truly a “Feel the AGI moment”.
For those interested, there’s a blog post [ https://substack.com/redirect/0de310f2-5bc6-4549-a351-dc9d654cab33?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] with the full transcript [ https://substack.com/redirect/6f1437af-b392-495c-9266-5d4211c17416?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] from initial prompt to final paper. Even if you know no physics, it’s crazy seeing pages of correct calculations fall out of simple prompts such as “Yes calculate outside of SD first. This is the first step.”
Out-of-domain = new knowledge
The thing that is qualitatively different between Vibe Physics and Vibe Coding is that Vibe Physics means actually extending the frontier of human knowledge. Looking at the Gluon and Graviton results, they seem in retrospect, like many results in physics and math, like natural extensions of what we already know. This is in fact part of what makes them beautiful. But this was a problem that stumped experts in the domain for a year. Although it does still have a bit of a recombinant flavor, this thing has never been done before.
It may be that there are still large classes of problems that AI won’t do well on, and approaches that an AI might not think to take. This is the “taste” that everyone has been talking about. Alex told us that these capabilities, however, allow him to explore many possible avenues in order to map out much more ambitious problems to tackle. With AI able to output results basically as fast as we can conceive and validate them, the scope of what one theorist can hope to achieve has just gotten a lot, lot bigger.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakU1TmpJNU1qUXpNaXdpYVdGMElqb3hOemM0TURFek16Y3dMQ0psZUhBaU9qRTRNRGsxTkRrek56QXNJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5vVTlyQzBhWnIwNTdSLXJRLXpSWHp6M0wyQ1MtdmF5NzlTUGVQWlgxbmE0IiwicCI6MTk2MjkyNDMyLCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc3ODAxMzM3MCwiZXhwIjoyMDkzNTg5MzcwLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.7ITi-h_vqzQv7lcAX2JH28pfLzKH3i_DLBnXWQWXd8w?
