---
title: The Multiplayer AI Manifesto
type: source
source_type: article
url: https://multiplayer-ai.com/
fetched: 2026-09-14
---

# The Multiplayer AI Manifesto

The Multiplayer AI Manifesto
What is multiplayer AI?
Why we need this manifesto
1. We went from collaborative work to siloed AI chats
2. Siloed chats come with a context tax
3. AI agents require org-wide security
4. Multiplayer AI improves outcomes
Common misconceptions
Isn’t my AI enterprise plan already multiplayer?
Can’t I just add an agent to Slack?
The Multiplayer AI Manifesto
Never copy-and-paste
Work with the door open
Continuously improve
People are not routers
Nothing starts from scratch
Important considerations
Agents don’t belong on laptops
Firewall every agent
Privacy pitfalls
Stay provider-agnostic
Governance is non-negotiable
Build, buy, or open source
Watch the walkthrough
Compare solutions
Get the platform comparison report
The Multiplayer
AI Manifesto

What we think AI at work should look like. Written for anyone with a say in how their company adopts AI.

1
Why we need this manifesto
2
Common misconceptions
3
The five principles
4
Important considerations
5
Compare solutions

Or watch the fourteen-minute walkthrough.

SCROLL
What is multiplayer AI?

Multiplayer AI means people on the same team working with the same AI agents, in shared sessions and with shared learnings, instead of each person alone in a private chat.

I
Why we need this manifesto

REASON

1 We went from collaborative work to siloed AI chats

Collaborative features are a given in today’s apps. We went from email to Slack. From Word to Google Docs. But recently, we have drifted apart into individual AI chats.

Each of those chats is a closed room: whatever gets figured out in there stays with just one teammate by default.

Q3 plan
Alice
Bob
Claire
OUR DOCUMENTS
OUR AI CHATS
vs
Alice
Bob
Claire

REASON

2 Siloed chats come with a context tax

Today, Alice might work with Claude on a report, then send it to Bob via Slack, only for him to put the report into ChatGPT and email the answer back.

With each handoff, the company pays a context tax that they wouldn’t have to pay if teammates could collaborate in the same agent session.

Alice’s screen
GitHub
Claude
ChatGPT
Alice
Bob
CONTEXT TAX
0 handoffs

REASON

3 AI agents require org-wide security

AI has gone from answering questions to taking actions on your systems.

An AI agent running on an employee’s machine might inadvertently move sensitive data from one system it’s connected to into another — or worse, onto the public Internet.

Gmail
a private email
Agent
on Alice’s laptop
#general
anyone can read it
LEAKED
private

REASON

4 Multiplayer AI improves outcomes

When employees of a large enterprise were allowed to collaborate both with each other and with AI, they achieved the highest proportion of top-quality outcomes in a Harvard Business School study.

And companies like Shopify found that allowing all employees to chat with AI agents in public was a boon to productivity. Within a month, 1 in 8 pull requests was already co-authored by their AI agent River.

Share of top-10% quality solutions

Harvard Business School field experiment with 776 professionals at Procter & Gamble

0%
5%
10%
15%
5.1%
Individual
no AI
8.7%
Team
no AI
7.7%
Individual
+ AI
15.1%
Team
+ AI

Source: Dell’Acqua, Ayoubi, Lifshitz, Sadun, Mollick et al., The Cybernetic Teammate (HBS working paper, 2025).

II
Common misconceptions

MISCONCEPTION

Isn’t my AI enterprise plan already multiplayer?

No, ChatGPT and Claude team/enterprise plans only let you share a few settings: prompts, skills, and integrations. They do not allow true multiplayer in the sense that Slack, Google Docs, Figma, and other modern tools do.

There is no chatting with a teammate’s agent. There is no learning from each other. Context is trapped in individual sessions, unindexed and short-lived.

Right now, working with AI is largely single-player. You open a chat, type a prompt, and get an answer, in a box only you can see. When you want to collaborate with your teammates and agents, the best you can do is send a link to a read-only transcript they can’t touch.

Multiplayer AI, Y Combinator Requests for Startups, Fall 2026

MISCONCEPTION

Can’t I just add an agent to Slack?

The simplest solution that allows your team to work with agents together is adding them to Slack. And indeed, Claude Tag and other solutions are great starts.

But a lot of work happens off Slack: in emails, Google Docs, GitHub, Salesforce, ServiceNow, etc. Truly multiplayer AI must enable reaching the same agent session from every work surface and every device.

One agent session
Slack
Email
Google Docs
GitHub
Salesforce
now
ServiceNow
The Multiplayer AI Manifesto

We posit the following five principles for a true Multiplayer AI experience. This is a North Star to build toward. No vendor or internal platform that we are aware of currently satisfies all of them.

1
Never copy-and-paste
2
Work with the door open
3
Continuously improve
4
People are not routers
5
Nothing starts from scratch
The Multiplayer
AI Manifesto
FIVE PRINCIPLES

PRINCIPLE

1 Never copy-and-paste
Agents must live next to the work, instead of in their own chat or in Slack.
Every person who is involved in the work must be able to chat directly with the same agent.
Agents must be able to use every tool that a human on the team uses to do the work.
CHAT
Alice is looking at this
Alice
Marketing
via Slack
What changed in the pricing PR, and does it match the spec?
ChatGPT
Read PR #482
Three files. New tier table, copy changes, and the annual discount set to 15%. The spec says 20%.
Bob
Engineering
via Email
Fix it and let marketing know.
ChatGPT
Pushed a commit
Posted in #pricing-launch
Set the discount to 20% and pushed to the PR. Posted the summary in #pricing-launch.
Claire
Customer success
via Slack
Thanks. Ship it Thursday, I’ll tell the customer list.
Follow up with ChatGPT…

The same work as the context tax relay above, in one session.

PRINCIPLE

2 Work with the door open
When chat sessions stay private, best practices spread slowly. When chat sessions are shared, everyone gets better quickly.
Tobi Lütke, Shopify CEO, called this “learning on the shop floor”. Shopify’s internal AI system (River) is only accessible via public Slack channels.

…if you have the door to your office closed, you get more work done today and tomorrow, and you are more productive than most. But 10 years later somehow you don’t quite know what problems are worth working on; all the hard work you do is sort of tangential in importance.

Richard Hamming, You and Your Research
vs

PRINCIPLE

3 Continuously improve
When a teammate writes a great prompt and the agent gets it right on the first try, other teammates should learn how to write good prompts.
When an agent needs correcting, a reusable skill should be created automatically, a saved recipe for that task that future agents use.
When the same workflow is performed repeatedly, a benchmark should be automatically created and its score tracked.
Week 1
Week 5
Week 9
Team performance
Software team
Finance team
Code review skill
Contract review skill
Browser testing skill
Month-end close skill

PRINCIPLE

4 People are not routers
A human must never be asked a question that an agent already has the answer to.
Chasing project updates and relaying answers is work for an agent, not a human.
Humans must focus only on the highest value activities. The bureaucracy must be digitized.
When does the Acme pilot end?
Is the SOC 2 report current?
Take the $2M deal at these terms?
Who owns the Q4 events budget?
Can the pricing page ship Thursday?
Did legal sign off on the vendor?
Chief
of Staff
Alice
Bob
Research Agent

PRINCIPLE

5 Nothing starts from scratch
When agent sessions live in the cloud, you can pick up every project exactly where you left off, with no context lost.
Every artifact, whether a design doc, financial plan, or pull request, must have an agent session that can be resumed even months later.
A new person joining a multiplayer AI team is productive on day 1.
Maya joined · day 1
Onboarding design doc
last active 4 months ago
Resume
PR #482 · Pricing page refresh
last active 6 weeks ago
Resume
Q3 financial plan
last active 2 months ago
Resume
Welcome, Maya. Here’s where each of these left off, and what’s still open.
III
Important considerations

Whether you build or buy, multiplayer AI is tricky to get right.

CONSIDERATION

Agents don’t belong on laptops
Laptop agents can’t be accessed by the rest of the team.
Laptop agents stop working when the lid gets closed.
Laptop agents can gain access to everything that an employee has access to.

CONSIDERATION

Firewall every agent
An agent tricked by a malicious email or document can send sensitive data to an outsider. Security people call this prompt injection.
Every agent must be limited to the services you approve. That is only practical in locked-down cloud environments.
Gmail
a private email
Agent
in a cloud sandbox
✕
#general
not on the allow-list
private

CONSIDERATION

Privacy pitfalls
Agents are at their most useful when they have access to sensitive data such as emails, Slack messages, financial records, etc.
When adding another teammate to a session that has exposure to sensitive data, it is important to handle permissions correctly.
For example, the agent should only have access to integrations that every member of a shared session has access to.
CHAT
Claire and Claude are here
Claire
Customer success
via Email
Pull up the last email from Acme’s CFO about the renewal.
Claude
Here it is, from Tuesday: “We can sign at $410k if the SLA moves to 99.95%.” Want a summary of the whole thread?
Bob joined the chat
Bob
Engineering
What did the CFO say about price?
Claude
ACCESS RESTRICTED
That came from Claire’s inbox, which isn’t shared with you, so I can’t repeat it here. Claire can share the thread, or I can ask her for you.
Follow up with Claude…

CONSIDERATION

Stay provider-agnostic
Some teammates prefer Claude, some prefer ChatGPT, and your CFO prefers open source.
The most powerful model changes week by week, and most tasks do not require the most powerful model in the first place.
When you bet your company on one model provider, you align yourself with their incentive structure, which is to bill you for as much usage as possible.
VOL. 7 · ANY GIVEN WEEK
The Daily Token
1¢ / 1K
US government suspends all access to Claude Fable 5

Anthropic statement, June 2026: every customer cut off overnight to comply with an export control directive

Uber burns its 2026 AI budget in four months on Claude Code

Forbes, May 2026

Anthropic cuts off OpenAI’s access to Claude

A terms-of-service dispute days before a major launch

ChatGPT goes down for ten hours

Elevated error rates across ChatGPT, Sora and the API

OpenAI retires GPT-4o, then brings it back after backlash

Users revolt when a beloved model disappears overnight

CONSIDERATION

Governance is non-negotiable
Governance means being able to answer four questions about any session a year later: which agent ran, who asked it to, what data it touched, and what it changed. Regulated industries and anyone subject to GDPR cannot skip this.
Auditors need a “black box” for agents, just as they have for every system of record: enough to check what happened without redoing the work by hand.
SESSION #4128 · AUDIT RECORD
a year later
Agent
Claude · sandbox eu-1
Requested by
Bob
Data accessed
Acme contract, 3 decks, 4 tickets
Changes made
None. A draft was saved.

CONSIDERATION

Build, buy, or open source
There are compelling reasons for each one of building internally, running an open-source solution, or using a hosted platform.
Most organizations find that while a basic version can be built quickly, getting to a fully-featured, seamless experience is a significant effort that detracts from their main goals.
Whichever way you go, one thing is not up for negotiation: you must own your data — the learnings, skills, and evals your team creates by using the platform.
Watch the walkthrough

Prefer to watch? Here is the whole manifesto in fourteen minutes, read by the person who wrote it.

Compare solutions

No platform satisfies all of these principles at this time. But some are closer than others. We are building a detailed comparison, featuring leading platforms such as Buzz, Claude Tag, QM, Superconductor, Viktor, and more.

Get the comparison
Send

Questions? Comments? Please reach out.

Share the manifesto

The Multiplayer AI Manifesto · September 2026 · By Sergey Karayev
and the team behind Superconductor
Back to top ↑
