---
title: How We Run a 25-person Company on Four AI Agents
type: source
source_type: article
url: https://every.to/source-code/how-we-run-a-25-person-company-on-four-ai-agents
fetched: 2026-04-22
---

# How We Run a 25-person Company on Four AI Agents

*This event was produced in partnership with* *[Notion](https://www.notion.com/). They had no input on the development of this article.*

*Want to learn alongside Every’s team? Check out our upcoming camps and courses at* *[every.to/events](https://every.to/events).*

---

Every runs six products, a media company, and a consultancy with around 25 people. At any given moment, each person has roughly 30 tasks on their to-do list. So how do they figure out which to work on first?

The team used to rely on **[Brandon Gell](https://every.to/@brandon_5263)**, Every’s COO, to run traffic control and coordinate the whole company, which required him to manually cross-reference launch calendars, company strategy documents, and task lists. Now he messages a Notion agent named Anton in Slack and gets a prioritized list for himself and others in seconds.

Anton is one of four custom agents Every has built with help from [Notion AI](https://www.notion.com/en-gb/product/ai) over the past few months. Each one automates a different task that, without the agent, would require tedious logistical work to track and schedule. Each one draws on the same set of interconnected databases that the team already maintains.

At our first [Custom Agents Camp](https://every.to/events), produced in partnership with [Notion](https://www.notion.com/), Brandon and Every head of growth **[Austin Tedesco](https://every.to/@tedescau)**, walked more than 500 subscribers through four agents they’ve built, the databases underneath them, and how to create your own. Notion product designer **Brian Levin** also joined to share best practices from the Notion team.

#### **Key takeaways**

* **Describe the outcome, not the steps.** Tell the AI what you want to accomplish and let it figure out the implementation. Over-prescribing (“Create a database, then add a relation, then filter by...”) tends to confuse the model.
* **Your Notion is your agent’s brain.** Custom agents get powerful when they can query interconnected databases. Every’s agents work because strategy, calendar, tasks, people, and meeting notes all live in Notion and reference each other.
* **Don’t write the agent’s instructions yourself.** Tell Notion AI what you want the agent to accomplish, and it will generate the instructions. Or use Claude Code with Notion’s API to build the whole thing from your terminal.

#### 

Attio is the AI CRM that thinks fast and acts faster.

With Attio, AI isn’t just a feature—it’s the foundation. With powerful AI automations and research agents, Attio transforms your go-to-market motion into a data-driven engine, from intelligent pipeline tracking to product-led growth.

Then ask Attio anything:

1. Prepare you for meetings with automatically compiled context
2. Create tasks and records while you work so you never miss a follow-up
3. Build powerful AI automations for your most complex workflows

Teams at Granola, Lightdash, and Wisper Flow are already experiencing the future of GTM with Attio.

Ready to build without limits?

## **Anton: The prioritization agent**

Every ships something almost every day, whether it’s a product update, an article, an event, a consulting deliverable, or a combination. Each launch gets its own set of tasks inside Notion, automatically populated from a template when the launch is added to the calendar.

The system works beautifully for tracking the full universe of tasks that exists. The problem is prioritization. With multiple launches overlapping each week, figuring out which of your 30 tasks matters this morning requires mentally weighing launch dates against company strategy against what your teammates are blocked on. Brandon used to be the human router for all of that. Now Anton does it.

[![The Anton agent, available through Notion or in Slack, helps Every team members keep track of their priorities. (Image courtesy of Katie Parrott.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_d5de7857-15eb-48ac-94bd-42574bffd9e6.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_d5de7857-15eb-48ac-94bd-42574bffd9e6.png)

The Anton agent, available through Notion or in Slack, helps Every team members keep track of their priorities. (Image courtesy of Katie Parrott.)

Anton also runs a daily broadcast to the whole company in Slack, summarizing what’s happening that week, and people can thread on the message to ask follow-up questions. “Having agents directly in Slack is where most of these conversations happen,” Brandon said.

[![A day in the life at Every, including what’s launching, when, and who owns it. (Image courtesy of Katie Parrott.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_84660cde-7e19-4fca-8566-423d8705aa9f.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_84660cde-7e19-4fca-8566-423d8705aa9f.png)

A day in the life at Every, including what’s launching, when, and who owns it. (Image courtesy of Katie Parrott.)

#### **The details:**

* **Goal:** Answer “What should I work on today?” for any team member, and post a daily company-wide priority summary to Slack.
* **Access:** Company strategy document, [OKRs](https://www.atlassian.com/agile/agile-at-scale/okr) database, unified calendar, tasks database that is linked to calendar entries, and a people database mapping each person to their team and role.
* **Outcome:** A prioritized task list personalized to whoever’s asking. The agent can also answer team-level questions (“What are **[Cora](https://cora.computer/)**‘s priorities this week?”) because it knows the organizational structure.

#### **Here’s a prompt so you can build it yourself in Notion:**

I want a custom agent that helps my team prioritize their work. We have a calendar database where each entry is a launch or project with a date. We have a tasks database where each task is linked to a calendar entry and assigned to a person. We also have a strategy document that outlines our top priorities this quarter. The agent should: (1) Tell any team member their most important tasks today, based on upcoming launches and strategy alignment. (2) Post a daily summary to Slack with the company’s priorities for the week. Build the databases if they don’t exist, and create the agent with instructions.

## **Max: The meetings-to-tasks agent**

Every recently moved all meeting notes into Notion. Meetings get recorded, transcribed, and stored in a database. That’s useful for reference, but meeting notes have a shelf life of about six hours before everyone forgets what they agreed to do. The real value is in the action items—and in saving those in the same system where the meeting was recorded.

This is where Max enters the proverbial chat. When a meeting ends, Max processes the transcript, extracts action items, and posts them to a Slack channel as a numbered list. Anyone can reply with which items should become tasks (“4, 5, and 7”), and Max creates them in the tasks database, linked to the correct launch. Meetings feed directly into the system the team already uses to track work, and nothing gets lost between the Zoom call and the to-do list.

[![Max summarizes action items coming out of Every’s last studio standup. (Image courtesy of Katie Parrott.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_e1db190c-85ba-42b9-a7a8-8a78deae2079.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_e1db190c-85ba-42b9-a7a8-8a78deae2079.png)

Max summarizes action items coming out of Every’s last studio standup. (Image courtesy of Katie Parrott.)

#### **The details:**

* **Goal:** Process meeting recordings, extract action items, and route selected items back into the task system.
* **Access:** Meetings database (with Notion’s built-in transcription), calendar, tasks database, and Slack.
* **Outcome:** A numbered list of action items posted to Slack after every meeting. Reply with which numbers matter (“4, 5, and 7”), and Max creates them as tasks linked to the correct launch.

#### **Here’s a prompt so you can build it yourself in Notion**

I want a custom agent that processes meeting notes. When a meeting is recorded in our meetings database, the agent should: (1) Update the meeting title based on the transcript. (2) Tag attendees. (3) Extract action items. (4) Post them to [Slack channel], numbered. (5) When someone replies with numbers (e.g., “2, 4, 6”), create those as tasks in our tasks database, linked to the relevant project on our calendar. Mark the meeting as “processed” when done.

## **The strategy interviewer**

OKR planning at most companies takes weeks. Someone sends a template, people procrastinate, leadership reviews drafts that don’t align with company goals, and the cycle repeats until everyone is exhausted and Q2 is already six weeks old. Brandon told the team on a Monday that OKRs were due Wednesday—a turnaround that would have been absurd without this agent.

The strategy interviewer works like a good chief of staff. It knows the company’s top-level goals, and it interviews each team member to draw out their plans for the quarter, pushing for specifics and measurable outcomes. Some people, like Austin, pasted in notes they’d already been collecting and got polished OKRs in about 10 minutes. Others used the interview as a thinking tool, talking through their priorities while the agent structured them in real time.

[![Every’s strategy interviewer agent helped the entire team develop 2026 OKRs that were aligned with the whole company’s goals. (Image courtesy of Katie Parrott.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_537848f9-9fe4-44d0-b1e1-9043f48a4d8b.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_537848f9-9fe4-44d0-b1e1-9043f48a4d8b.png)

Every’s strategy interviewer agent helped the entire team develop 2026 OKRs that were aligned with the whole company’s goals. (Image courtesy of Katie Parrott.)

Brian from Notion added a useful refinement: After the interview, ask the agent, “What’s the dumbest, simplest system we could build to accomplish these goals?” Repeating this strips away complexity and gets you to the essence.

#### **The details:**

* **Goal:** Interview each team member about their quarterly goals and produce structured OKRs aligned to company strategy.
* **Access:** Company strategy document and OKRs database.
* **Outcome:** A complete set of OKRs per person, stored in a shared database for leadership review. Every’s team completed theirs in two days.

#### **Here’s a prompt so you can build it yourself in Notion:**

I want a custom agent that helps my team write quarterly OKRs. Here’s our company strategy: [paste or link your strategy document]. The agent should interview each person about their goals, ask follow-up questions to make them specific and measurable, and write OKRs that align to the company strategy. Store results in an OKRs database with fields for objective, key results, owner, team, and quarter.

## **The campaign reporter**

Austin tracks growth across PostHog, Stripe, and several other platforms. Before agents, he [spent his mornings](https://every.to/p/the-agent-that-saved-my-brain) opening dashboards, pulling numbers manually, and compiling a report for his team. Assembling the data into something useful took more effort than analyzing it.

Now a custom Notion agent posts a daily scorecard to the growth team’s Slack channel—key metrics, pace indicators, and a flag for whether the team is ahead or behind its targets. The database underneath pulls from external sources via Notion Workers—custom scripts that connect Notion to outside APIs. You describe what you want to a coding agent (“I need to pull daily traffic numbers from PostHog into a Notion database”), and it writes the script for you using Notion’s [public workers template](https://github.com/makenotion/workers-template). Previously, this kind of connection required the app itself to build an official integration. Workers let you wire up whatever tools you already use.

[![Austin’s campaign reporter agent monitors the progress of Every’s Plus One campaign. (Image courtesy of Austin Tedesco.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_0b9928ed-09b1-4af2-85f5-4faff181972f.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4105/optimized_0b9928ed-09b1-4af2-85f5-4faff181972f.png)

Austin’s campaign reporter agent monitors the progress of Every’s Plus One campaign. (Image courtesy of Austin Tedesco.)

Austin built the whole pipeline from his Claude Code terminal using the Notion API. He brain-dumped the desired outcome using **[Monologue](https://www.monologue.to/)** (Every’s speech-to-text tool), let Claude Code create the database and data pipeline, and pasted the generated instructions into the Notion custom agent setup. When the first output had wrong numbers, he copied the Slack message link back into Claude Code along with the message, “This number looks off,” and iterated from there.

#### **The details:**

* **Goal:** Post a daily growth scorecard to Slack showing whether a campaign is on pace.
* **Access:** A Notion database that pulls data from PostHog and Stripe via Notion Workers (currently in alpha). Brian from Notion demoed the [public workers template repo](https://github.com/makenotion/workers-template) for anyone who wants to connect external data sources.
* **Outcome:** A formatted Slack message each morning with key metrics, pace indicators, and a link to the full report.

#### **Here’s a prompt so you can build it yourself in Notion**

I’m running a campaign for [product]. I need a daily scorecard posted to [Slack channel] showing: [list 3-5 key metrics]. The data lives in PostHog for traffic and Stripe for subscriptions. Set up a Notion database to store this data, create a custom agent that reads from it, and post a daily report showing whether we’re ahead or behind pace. Here are our targets: [list targets].

If you need external data in your Notion databases, ask a coding agent: “I want to create a Notion Worker that pulls [data type] from [service]. Here’s the workers template repo: <https://github.com/makenotion/workers-template>. Walk me through setting it up.”

## **Build your own: The general-purpose template**

The agents above are specific to Every’s workflows, but the pattern underneath them is the same every time. Brian’s advice from the session: Don’t install someone else’s template and hope it fits. Instead, have Notion AI interview you about your problem, then build the agent around your answers. Here’s a starter prompt you can adapt for anything:

Interview me to help me build a custom Notion agent. Here’s what I’m trying to accomplish: [describe the outcome you want in plain language—e.g., “I want to know which client projects are at risk of missing their deadlines” or “I want a weekly summary of what my team shipped”].

Ask me questions about how I currently do this work, what information I’d need the agent to access, where I want the output delivered (Notion, Slack, email), and how often it should run. Then build the databases, write the agent instructions, and set up any recurring schedules. Start simple—I’d rather have something working today that I can improve over time.

Once you have the first agent running, the second one is easier—because the databases it created become the foundation for whatever you build next. That’s how Every ended up with four agents on three databases. Brandon started with the calendar and tasks. The agents came one at a time, each one plugging into what already existed.

Brian’s advice for keeping the scope manageable: after the interview, ask the agent, “What’s the dumbest, simplest system we could build to accomplish this?” Start there. You’ll know what to add once you’ve lived with it for a week.

---

***Katie Parrott*** *is a staff writer and AI editorial lead at Every. You can read more of her work in* *[her newsletter](https://katieparrott.substack.com/). To read more essays like this, subscribe to* *[Every](https://every.to/subscribe), and follow us on X at* *[@every](https://twitter.com/every) and on* *[LinkedIn](https://www.linkedin.com/company/everyinc/).*

*Discover Every’s [upcoming workshops and camps](https://every.to/events), and access recordings from past events, including the Notion agent camp.*

*For sponsorship opportunities, reach out to sponsorships@every.to.*
