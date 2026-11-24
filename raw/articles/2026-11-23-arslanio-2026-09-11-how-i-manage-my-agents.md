---
title: How I manage my agents
type: source
source_type: article
url: https://arslan.io/2026/09/11/how-i-manage-my-agents/
fetched: 2026-11-23
---

# How I manage my agents

There are probably hundreds of posts like this. But I wanted to share my workflow about how I create and manage a fleet of agents. I've had huge success with it over the past few months.

![Pixel loop: a closed track with one step lit](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-retro-loop.png)

I rely on some sort of index, where I save every single piece of agent work. Each plan is a single markdown file, which is human readable and can be shared with co-workers or other agents.

These plans live in a dedicated repo, and accessible by all my Cloud Agents (and by my co-workers of course). Initially, random agents would create and manage these plans, but later on I switched to long running agents. These are called coordinators, and they read and write to the repo (more on this later). The nice thing about having them in a git repo is that agents know how to interact and I'm getting history for free.

## Layout

It all starts with the skill `/plan-init`. You call it once (in the repo where you keep your plans) and then never call it again. This skill sets up your directory with the folders required to manage your agents, and a `README.md` that is the index of what is next and what is open. Here is what it would create:

```
plans/
  README.md
  drafts/
  next/
  open/
  done/
  discarded/
```

![Pixel board: drafts, next, open, done and discarded trays with plans in them](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-board.png)

Now, let's start using it. Assuming you're on Slack and someone wrote this message:

`"Hey @fatih, the service foo caused an alert and clients started receiving 500, could you look into this?"`

Note it can also be an automation, but let's assume we're the ones triggering it. We're going to manually write this down:

`@cursor /plan-add investigate why the service is getting 500, also check PR 123, it might be related`

This creates a new plan called `hub-service-500.md` and puts it under the `drafts/` folder. The `hub-` prefix is the area of work; the rest is a short slug:

```
drafts/
  hub-service-500.md
next/
...
```

![Pixel diagram: a message becomes a draft page and lands in the drafts tray](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-capture.png)

It all starts by capturing our ideas and thoughts and saving them as a draft

`/plan-add` is nothing special, just a way to make sure any idea/thought you have is saved somewhere. You see something and don't want to forget it, and in Cursor, you write this down: `/plan-add a way to run service bar concurrently`.

Now our folder becomes this:

```
drafts/
  hub-service-500.md
  hub-concurrent-bar.md
next/
...
```

All we do is move things that we might want to pick up in the future into the `drafts/` folder. You want to free up your thoughts. `/plan-add` is just for that. Get it out before you forget. These don't have any decisions yet, but the agent saves them, and while saving, it also checks prior `done/` plans, any message you sent for that service, and so on. It also takes a snapshot of the surroundings (agents are pretty good at observing and finding things you're not even aware of).

Now comes the important part: when the time comes, you go over a draft and turn it into a plan an agent can implement without asking you design questions. This is where you probably want to use a higher reasoning model:

```
/plan-write investigate the service draft, I remember the service was having issues a few weeks ago. Search Slack for related messages. How did we solve it? Check channel #released, did we release any new service that might cause an increased load?
```

![Pixel diagram: a one-line draft becomes a fully written plan](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-write.png)

From here on, you're actually investigating the problem. You prove the cause, name the change, and write the commands that will prove it worked. If this is a feature, you're designing a spec. An investigation with no change stays in `drafts/`. Open questions stay there too, until you answer them. In our case the cause is last week's deploy, and the change is a tighter timeout in the foo client. That is enough, so the plan gets written to `next/`:

```
drafts/
  hub-concurrent-bar.md
next/
  hub-service-500.md
open/
...
```

Once you have a few of these, or not, you can dispatch the plan with any agent you have. Here I always use something that just rips and is super fast.

Because the plan already has all the decisions, you need a model that is good at coding and following the plan:

```
/plan-dispatch the plan for the service 500s

# or /plan-dispatch
```

The plan has everything it needs, so an isolated [Cloud Agent](https://cursor.com/cloud?ref=arslan.io) has all the information. It also knows if it has dependencies, or if it can be called in parallel with other plans, and so on. The plan first gets moved into the `open/` folder, and then the agent starts working on it.

```
drafts/
  hub-concurrent-bar.md
next/
open/
  hub-service-500.md
done/
...
```

After this, the agent works and opens a Pull Request. A plan that reaches `next/` is meant to end as one or more PRs. A demo or a note for another team can come with it, but the PR is the artifact. You decide if it's done. The agent reports back what it did, and that gets written into the markdown file. Once the PR is merged, you sync the plans:

![Pixel diagram: an open plan turns into a pull request that merges](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-artifact.png)

```
/plan-sync
```

What does it do? `/plan-sync` checks the recorded PRs against the plan that was dispatched. If the merge matches, the file moves to `done/`. If something is missing, it asks me. Sometimes we abandon a change. In that case, we put it into `discarded/`. I also have a `/plan-status` which gives me a report: what is waiting on a merge, what is blocked, which draft can be written now, and so on.

## Coordinators

![Pixel org chart: the Hub on top, three area coordinators below it, each with its own three agents](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-coordinators.png)

I've been using the plan system for months at two different companies for But of course it can be better. Why? Because there is a lot of bookkeeping. And there are manual processes that can be automated (like checking upon PR's, or Slack messages, and so on).

So, once you have a dozens of plans, you want the agents running them for you. Luckily, when [I joined Cursor](https://arslan.io/2026/08/10/joining-cursor/), I discovered that we were working on a new project. And we just announced it [yesterday](https://x.com/cursor_ai/status/2098162488013455784?ref=arslan.io). It's called [Projects](https://cursor.com/blog/projects?ref=arslan.io).

I no longer manage my plans with individual agents anymore, instead I run the plans through coordinators. These are the long-running agents Cursor introduced with [Projects](https://cursor.com/blog/projects?ref=arslan.io). A coordinator doesn't write code itself. It directs the agents that do. It's like an orchestra conductor for agents. What's nice is, a **Project** also comes with a few features a typical agent doesn't have.

![Pixel diagram: one plan fanning out to three agents](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-dispatch.png)

First, it can start new chat sessions in the cloud, on your local machine, or on a remote machine you own. The default is a fresh Cloud Agent with its own clone of the repo; the agent gets the plan and the Project's Context. Sometimes, some work needs my local machine. The great thing is, even from my iPhone, or online from Cursor.com, the Project can dispatch agents to my MacBook (assuming you enabled `remote workers`). Finally, I also keep a large Linux EC2 box running. I use it for work-related work.

Second, it has a `Project Context` tab, a folder of files that belongs only to the Project:

* A `notes.md` file. This is your **README.md** of your Project. But it's dynamic. You can edit it as well if you like, but I let only the coordinator write to it.
* a `docs/` and `/media` folder that you as a Human open.
* an `internal/` folder for Agent's scratch files. You do not open it.

And then there is also a `User Context` tab, this is global that all Project coordinators can read from. It includes things like:

* `preferences.md` Whenever you create a new Project, the coordinator reads this. It's like AGENTS.md, but it's not passed down to agents. The coordinator reads it at the start of every turn, and agents do not get it.
* `skills/` folder. You can sync your skills here, so all agents have access to them.

![Pixel field of blocks: the index of every plan](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-index.png)

Third, a Project has `subscriptions`. A coordinator can follow a pull request, watch a Slack channel, or wake up on a schedule. Mine subscribe to every PR their workers open. When CI finishes or a reviewer leaves a comment, the coordinator wakes up, reads it, and sends the worker back if there is something to fix. When the PR merges, it unsubscribes and updates the plan. Sometimes I setup a metrics, and then make sure the coordinator checks the metrics every 6 hours.

Remember the Slack message at the beginning? I said it could also be an automation. This is how: the coordinator watches the channel, and when an alert comes in, it runs `/plan-add` itself. Whether it also dispatches on its own is a mix. Some of my coordinators dispatch a ready plan right away, some still wait for my go. Both work, and I haven't settled on one yet.

The nice thing is `notes.md` of a Project. You can ask your agent to update it on its own, or tell it how to do it. In my case, it holds the information about my plans. So each coordinator has these in their `notes.md`: Goal, PRs, Open, Next, Drafts, Done, Links, Research.

Each of my projects has the same layout, so I immediately know what's going on. I also make sure the Project's state is saved, so every change to the notes is also committed to the same repo as the plans, in the same turn:

```
docs/
  billing/coordinator-notes.md
  storage/coordinator-notes.md
  fleet/coordinator-notes.md
  hub/coordinator-notes.md
```

This turned out to matter a lot. Because I was beta testing Projects, in week one I hit a platform bug and got stuck in an error loop after 460 messages or so. I asked it to write a handoff, started a fresh Project, and told the new one to rebuild its notes from the repo. It was working again in one turn.

![Pixel diagram: the Hub hands off to a new coordinator, which builds up in three steps](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-spawn.png)

Coordinators cannot message each other and cannot read each other's Context (besides the global User Context). So they leave things for each other in git:

```
docs/coordinator/
  preferences.md
  handoff-billing-2026-09-04.md
  plan-retro-2026-09-03-report.md
  inbox/hub.md
  inbox/billing.md
```

Every file there starts with four lines: `From`, `To`, `Date`, and `Why`. The inbox files hold the messages, one file per coordinator. A message is one checkbox line with the date, the sender, and one or two sentences. The `Hub` writes into a Project's file; a Project writes into `hub.md`; Projects do not write into each other's files, they ask the Hub. Every coordinator pulls and reads its own file at the start of each turn, and then commits its reply.

![Pixel diagram: the Hub leaves a letter for a coordinator](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-inbox.png)

## Retro

It could look like it's a lot. And it is! I constantly revise it though. And there are a few things that nicely tie everything together. I have a skill called `/plan-retro`. Once called, it reads the finished plans in `done/` and `discarded/` and the transcripts behind them. How do I write? Do we have the same misunderstanding over and over again? It then proposes a concrete edit to a skill. It also might suggest removing certain skills, or propose a new rule.

You don't have to do it, but it's extremely helpful. It's there to close the loop (remember [feedback loops](https://arslan.io/2026/06/16/kubernetes-runs-on-feedback-loops/)?). Agents are so powerful that we should let them improve our skills and systems constantly.

![Pixel loop: drafts to next to open to done and back, with an exit to discarded](https://storage.ghost.io/c/ce/27/ce27a3ef-1519-4f17-a161-c8cdf7793306/content/images/2026/09/pattern-lifecycle.png)

The nice thing about this is, it isn't just about the plans you add. The retro step looks at how my work actually landed. Then it proposes a change to the skill that let that through.

Cursor's [Projects post](https://cursor.com/blog/projects?ref=arslan.io) has the same idea under the name gardening: a coordinator that adds a lint rule whenever it sees the same mistake twice. Retro is that, applied to the skills instead of the codebase.

## Recap

If you've read this far, you might ask: How can I download these skills? There are none! And I deliberately didn't publish them. This works best for *me*. But it might not work for you at all. So do this instead: paste the following prompt into your agent and let it create the skill files. They will be truly shaped to your habits:

```
Read https://arslan.io/2026/09/11/how-i-manage-my-agents/ in full. Then look at how I actually work before you write anything: go through my last three months of commits and pull requests, the issues or tickets I opened and closed, and, if you can reach them, the chat channels where I ask for work and report on it. 

Write down what repeats: how I phrase a task, what I check before I call something done, which mistakes I correct more than once, and where my work waits on other people. From that, create the plan skills from the post (plan-init, plan-add, plan-write, plan-dispatch, plan-status, plan-sync, plan-retro), plus a plan-spec skill that holds the folder layout and the plan file format the others read first, as skill files in my Cursor skills folder, written for my habits and not for the author's: my folder names, my commit and PR format, the checks I run, the people and systems my plans depend on. 

Keep each skill under two pages, in plain English, and name the exact commands it runs. Where my history shows I do something differently from the post, follow my history. When you are done, walk one made-up plan through the whole loop so I can see them work together, then stop. Commit nothing until I have read it.
```

That is the loop to manage your agents. To recap:

* Plans hold the work
* Coordinators run it
* Notes and handoffs make any of them replaceable
* The retro rewrites the rules from our conversations and past actions

Thanks for reading, and let me know if you have any questions.
