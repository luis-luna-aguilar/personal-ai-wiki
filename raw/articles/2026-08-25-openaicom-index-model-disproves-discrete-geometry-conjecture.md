---
title: An OpenAI model has disproved a central conjecture in discrete geometry
type: source
source_type: article
url: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
fetched: 2026-08-25
note: >
  Automated fetch (scripts/fetch_url.py) hit a Cloudflare "Just a moment..."
  bot-check interstitial and could not retrieve the rendered page. Content
  below was captured by opening the live page in a real browser session
  (compound-engineering:agent-browser retry) and transcribing the rendered
  text, including four mathematician testimonial quotes read via the page's
  testimonial carousel. Quotes are verbatim; surrounding structure is
  reconstructed from the accessibility-tree read, not a verbatim full-page
  dump.
---

# An OpenAI model has disproved a central conjecture in discrete geometry

An internal OpenAI model has disproved a longstanding conjecture in discrete geometry: the planar unit-distance problem, first posed by Paul Erdős in 1946.

The problem asks how many pairs of points, among n points placed in the plane, can be exactly distance 1 apart. For nearly 80 years, the prevailing belief was that "square grid" style constructions were essentially optimal, corresponding to an upper bound of roughly n^(1+o(1)).

Our new result disproves this conjecture. More precisely, for infinitely many values of n, the proof constructs configurations of n points with at least n^(1+δ) unit-distance pairs, for some fixed exponent δ > 0. The original proof did not give an explicit value of δ; a forthcoming refinement by Princeton mathematician Will Sawin shows one can take δ = 0.014.

The result is also notable for how it was found. The proof came from a new general-purpose reasoning model, rather than from a system trained specifically for mathematics, scaffolded to search through proof strategies, or targeted at the unit distance problem in particular. As part of a broader effort to test whether advanced models can contribute to frontier research, we evaluated it on a collection of Erdős problems. In this case, it produced a proof resolving the open problem.

After verifying the initial proof, we investigated the success rate of our models on this problem with varying amounts of test-time compute. (The page shows a chart of this relationship; no numeric time or dollar-cost figures are given in the surrounding text.)

The proof has been checked by a group of external mathematicians. They have also written a companion paper explaining the argument and providing further background and context for the significance of the result.

It marks the first time that a prominent open problem, central to a subfield of mathematics, has been solved autonomously by AI. It also offers an early glimpse of a new kind of collaboration between AI and human mathematicians. In this case, the companion work by external mathematicians paints a substantially richer picture than the original solution alone.

That future still depends on human judgment. Expertise becomes more valuable, not less. AI can help search, suggest, and verify. People choose the problems that matter, interpret the results, and decide what questions to pursue next.

The proof is available (linked PDF), a companion paper by leading external mathematicians is available (linked PDF), and an abridged version of the model's chain of thought is linked as well.

## Technical method (as described on the page)

Erdős's original lower bound can be understood through the Gaussian integers. The new argument replaces the Gaussian integers with more complicated generalizations from algebraic number theory with richer symmetries. The precise argument uses tools such as infinite class field towers and Golod–Shafarevich theory to show the number fields required for the argument actually exist.

## Mathematicians on the result (testimonial carousel, 4 quotes, verbatim)

**Noga Alon:**
"This has been one of Erdős' favorite problems, I have heard him myself mentioning the problem multiple times in his lectures. I believe it would be fair to say that every mathematician working in Combinatorial Geometry thought about this problem, and lots of mathematicians working in other areas spent at least some time thinking about it… The solution of the problem by the internal model of Open AI is, in my opinion, an outstanding achievement, settling a long-standing open problem. The fact that the correct answer is not n^(1+o(1)) is surprising, and the construction and its analysis apply fairly sophisticated tools from algebraic number theory in an elegant and clever way."

**Tim Gowers:**
"There is no doubt that the solution to the unit-distance problem is a milestone in AI mathematics: if a human had written the paper and submitted it to the Annals of Mathematics and I had been asked for a quick opinion, I would have recommended acceptance without any hesitation. No previous AI-generated proof has come close to that."

**Arul Shankar:**
"The model's CoT is deeply interesting. It is noteworthy that a significant majority of the thoughts are trying to construct a counterexample to the widely believed upper bound, rather than trying to prove it. This argues that the model has some combination of good intuition, willingness to try approaches considered long-shot by the community, and a predisposition to attempt constructions… In my opinion this paper demonstrates that current AI models go beyond just helpers to human mathematicians – they are capable of having original ingenious ideas, and then carrying them out to fruition."

**Jacob Tsimerman:**
"This is a really impressive piece of work, and I would accept it for any journal without hesitation. I actually briefly worked on this problem and tried to make a counterexample, but failed to make progress… It is definitely an intimidating construction to see through even if you know what is going on, and even harder to go play for yourself."

## Additional named reaction quoted on the page

**Thomas Bloom** (from the companion note):
"When assessing the importance and influence of an AI-generated proof, a question I ask myself is: has this taught us something new about the problem? Do we understand discrete geometry better now? I think the answer is a moderated yes: this shows that there is a lot more that number theoretic constructions have to say about these sorts of questions than we suspected; moreover, that the number theory required can be very deep." … "The frontiers of knowledge are very spiky, and no doubt the coming months and years will see similar successes in many other areas of mathematics, where long-standing open problems are resolved by an AI revealing unexpected connections and pushing the existing technical machinery to its limit."

## What the page does NOT state

No model name/version (e.g. "GPT-5.6"), no run duration, and no dollar cost appear anywhere in the rendered page text. These specific figures (informally: "<32 hours," "<$1,000," speculated "GPT-5.6" lineage) originate only from secondary Twitter/AINews recap and speculation, not from OpenAI's own announcement.
