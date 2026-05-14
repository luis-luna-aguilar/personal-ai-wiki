---
title: Agent-native Product Management - Every
type: source
source_type: article
url: https://every.to/guides/ai-product-management-guide?source=post_button
fetched: 2026-05-13
---

# Agent-native Product Management - Every

#### **Data sources**

A pulse pulls from up to four categories of tools in the product’s stack:

A team that has only one of these can still run a useful pulse. The report skips sections when the requisite data source isn’t available. With the number of data sources, quality beats quantity.

#### **Wiring up MCP connections**

The fastest way to let an agent query these tools on every run is to connect them via MCP. If you’re running Claude Code, `/mcp` lists what’s already connected. Your agent’s MCP registry is an easy way to find connectors, or you can use Google to search for them.

If a tool has no MCP available, the pulse can still work. The agent just needs a credentialed path (like a CLI or API), but agents seem to like MCPs.

#### **Feedback channels**

Pulse covers the quantitative half of feedback—metrics, errors, performance. The qualitative side has to come from users directly. I like emailing with users, so I made the Spiral email address conspicuous in the product, and emails to it land in my work inbox. I also include a 15-minute call booking link in every marketing email that goes out to users. There is no substitute for talking to users. You will never cease to be surprised by what they say.

Platforms like Canny and Featurebase are also good ways to collect and organize feature requests and bug reports. They have MCPs, which can be another good input into Pulse.

#### **Memory: Saved reports**

Every pulse run saves a copy to `~/pulse-reports/` as a Markdown file. A single pulse answers, “What happened today?” A folder of pulses answers, “What happened this month?” “When did this trend start?” “Did that feature change anything?” Over time, the folder becomes the team’s working memory of the product.

#### **Running on a cadence**

Claude Code has a Routines feature, which allows you to schedule frequent tasks, so you can automate recurring pulse runs. I have it run every day at 8 a.m., so I start work with the freshest perspective on how the product is doing. I typically run `/ce:product-pulse` manually a few times over the rest of the day.

#### **Reading it like a founder**

The agent is instructed to assemble the report, read it from the perspective of a founder, annotate anomalies, and run follow-up queries where necessary. For example, if a certain endpoint yielded higher errors, it will dig into those errors: Were they from one user? Did they coincide with a reported third-party outage? On the agent’s second pass, unless everything is completely normal, it will add a section at the end that preemptively answers natural follow-up questions. In this way, the agent works as an analyst, not just by pulling the data but by evaluating and presenting it.

By default, there are no hard-coded thresholds above or below which the agent will flag metrics. The agent evaluates the report using common sense and by comparison to previous pulse numbers. For example, if response times are suddenly three times higher on average, it will flag that and likely investigate further. If you do have specific performance goals—say, average system response time—you can ask your agent to reference those in the relevant section.
