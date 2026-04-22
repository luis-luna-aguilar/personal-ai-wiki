---
title: "METR’s Joel Becker on exponential Time Horizon Evals, Threat Models, and the Limits of AI Productivity"
type: newsletter
sender: "Latent.Space <swyx@substack.com>"
received: 2026-02-27
gmail_id: 19ca08ac31ffbd08
---

# METR’s Joel Becker on exponential Time Horizon Evals, Threat Models, and the Limits of AI Productivity

**From:** Latent.Space <swyx@substack.com>
**Date:** 2026-02-27

View this post on the web at https://www.latent.space/p/metr

AIE Europe CFP [ https://substack.com/redirect/460e7311-0aa6-4173-824c-109902d2e6e4?j=eyJ1IjoiMnZtN2U0In0.wD3dcFAYUauUmayn7txEHe_RXTNDo11i_Ww9KAqkSqw ] and AIE World’s Fair paper submissions for CAIS [ https://substack.com/redirect/4ab97707-4fce-4bdf-a314-eb616dddda4c?j=eyJ1IjoiMnZtN2U0In0.wD3dcFAYUauUmayn7txEHe_RXTNDo11i_Ww9KAqkSqw ] peer review are due TODAY - do not delay! Last call ever.
We’re excited to welcome METR for their first LS Pod, hopefully the first of many:
METR are keepers of currently the single most infamous chart in AI [ https://substack.com/redirect/476c099b-dd54-4557-a13b-513041ff7268?j=eyJ1IjoiMnZtN2U0In0.wD3dcFAYUauUmayn7txEHe_RXTNDo11i_Ww9KAqkSqw ]:
But every Latent Space reader should be sophisticated enough to know that the details matter and that hype and hyperbole go hand in hand in AI social media, because the millions of impressions that got, by people who don’t understand or care about the nuances, disclaimers, and error bars, far outreaches the 69k views on the corrections by the people who actually made the chart:
There’s a lot of nuance both in making benchmarks (as we discovered with OpenAI on our SWE-Bench Verified podcast [ https://substack.com/redirect/0b86dd6c-0e82-4f77-8200-a6aa1ae4e3fd?j=eyJ1IjoiMnZtN2U0In0.wD3dcFAYUauUmayn7txEHe_RXTNDo11i_Ww9KAqkSqw ]) and in extrapolating results from them, especially where exponentials and sigmoids are concerned [ https://substack.com/redirect/4845b9a3-60e2-4bb7-a5db-cdd2e02e815a?j=eyJ1IjoiMnZtN2U0In0.wD3dcFAYUauUmayn7txEHe_RXTNDo11i_Ww9KAqkSqw ]. METR’s Long Horizons work itself has known biases that the authors have responsibly disclosed, but go far too underappreciated in the pursuit of doomer chart porn.
If you’re interested in a short, sharable TED talk version of this pod, over at AIE CODE we were blessed to feature Joel twice, as a stage talk [ https://substack.com/redirect/76205e82-1da3-4d46-ab40-14fdcf047b79?j=eyJ1IjoiMnZtN2U0In0.wD3dcFAYUauUmayn7txEHe_RXTNDo11i_Ww9KAqkSqw ] and with a longer form small workshop with Q&A [ https://substack.com/redirect/7b403478-8d69-4c54-89f1-e1cd2167c364?j=eyJ1IjoiMnZtN2U0In0.wD3dcFAYUauUmayn7txEHe_RXTNDo11i_Ww9KAqkSqw ]:
We also make sure cover some of METR’s lesser known work on Threat Evaluation but also Developer Productivity, where 2x friend of the pod and now Zyphra founder Quentin Anthony was the ONLY productive participant [ https://substack.com/redirect/4bd5244b-c515-4fe9-82bf-da3644335245?j=eyJ1IjoiMnZtN2U0In0.wD3dcFAYUauUmayn7txEHe_RXTNDo11i_Ww9KAqkSqw ]!
Finally, if you’re the sort to read these show notes to the end, then you definitely deserve some pictures of Joel shredding the guitar at Love Band Karaoke [ https://substack.com/redirect/08a27ade-2114-4892-940c-0710a702035c?j=eyJ1IjoiMnZtN2U0In0.wD3dcFAYUauUmayn7txEHe_RXTNDo11i_Ww9KAqkSqw ] which we mention at the end: 
Full Video Pod
Timestamps
00:00 What METR Means
00:39 Podcast Intro With Joel
01:39 ME vs TR
03:33 Time Horizon Origin Story
04:56 Picking Tasks And Biases
09:13 Time Horizon Misconceptions
11:37 Opus 4.5 And Trendlines
14:27 Productivity Studies And Explosions
29:50 Compute Slows Progress
30:47 Algorithms Need Compute
32:45 Industry Spend and Data
34:57 Clusters and Shipping Timelines
36:44 Prediction Markets for Models
38:10 Manifold Alpha Story
43:04 Beyond Benchmarks Evals
51:39 METR Roadmap and Farewell
Transcript
What METR Means
Joel Becker: So meta stands for METR first two letters, model evaluation. That is, we think about what their capabilities of AI models might look like today and tomorrow, as well as their propensities, what they’ll actually do in the wild, given that they have some level of capability. And then threat research is the final two letters.
We try to connect those capabilities and propensities to particular threat models that we have in order to determine whether AI models pose enormous or catastrophic risks to society. So the secret, if you read this article about how it became the number one most profitable trader on manifold, mostly comes down to this one market where,
Podcast Intro With Joe
Alessio: Hey, everyone. Welcome to the Latent Space Podcast. This is Alessio, founder of Kernel Labs, and I’m joined by swyx, editor of Latent Space.
swyx: Hello. Hello. We’re back in the studio with Joe Becker from Meter. Welcome.
Joel Becker: Thank you very much, guys. It’s a great pleasure to be here.
swyx: So Joel your work has impacted the AI field a lot, especially over the last year.
I invited you for the a IE summit, which thank [00:01:00] you for speaking as well and doing the extra workshop. And there you have a lot of papers that have been very impactful, but I guess upfront a lot of people like neither just burst onto the scene. Could you explain and introduce meter.
Joel Becker: Yes, so me stands for METR first two letters, model evaluation.
That is, we think about what their capabilities of AI models might look like might look like today and tomorrow, as well as their propensities, what they’ll actually do in the wild. Given that they have some level. Of capability and then threat research is the final two letters. We try to connect those capabilities and propensities to particular threat models that we have in order to determine whether AI models pose enormous or catastrophic risks to society.
swyx: Yeah.
ME Versus Threat Research
swyx: Would you say that you’ve done a lot more ME and TR is like the next phase, or is there tr side of work that I’m this,
Joel Becker: I think this than tr some of the most publicized work does look more like VME. It looks like this time horizon stuff and the developer productivity, RCTs, stuff like that.
But there’s this wonderful report on our website GT five report and analogous one for GT 5.1 as well, [00:02:00] trying to make this more sort of structured case that it doesn’t pose these really large scale risks, eventually coming to the conclusion that it doesn’t but it’s worth thinking.
Like what, why exactly is that the case? If, you and I work with GT five, it does seem very capable. That matches up to benchmark scores. Why is it not able to do really? So something really, enormously wrong. We go through the evidence. We find, we, we think it’s not capable enough, on, on the basis of some of this capabilities, evidence that you’ve alluded to to commit these catastrophic harm.
And it’s not going to be able to do this, but perhaps in future, we will think it’s capable of doing pretty extraordinary things. The kinds of things that would be necessary to provide really serious threats. And then maybe you’d lean more on the propensities parts are there protections that we have against these dangerous capabilities sufficient for it not to pose an exist existential threat.
That sort of thing. So I think it’s I think threat research, very much is there, very much is something that we’re aspiring towards. In some ways you might, sorry, see the capabilities, evidence as a kind of input.
swyx: Yeah.
Alessio: Have the thread models been updated a lot, or do you feel like you’re still using the same thread models as [00:03:00] GVD two of paper Cliff factory, blah, blah, blah, but like how much are you, increasing the bar.
Joel Becker: Yeah. So I’m not an expert in the threat modeling piece. Yeah. Yeah. More in the capabilities piece. I do think they’ve been changing to some extent, so something like the autonomous replication threat model that is being able to set yourself up and control resources.
So something like that has been deprioritized relative to r and d acceleration. That is, the possibility there could be some capabilities explosion inside of a lab, and that could be destabilizing for all sorts of reasons that we could talk about. So it’s mainly with focusing on that latter one.
Although we do think about it a number of threat models.
Time Horizon Origin Story
Alessio: Yeah, let’s talk about the ME side, so I would say the, model time horizon chart is probably the most quoted, I would say, both in investment decks that I see. And just general on, on Twitter, what was the origin story of it and any other color you wanna give on it to introduce it to the audience?
Joel Becker: Yeah, so there are a couple of different ways to tell this story. O one way is there’s this PowerPoints internal meter PowerPoint from 2023 where we’re trying to lay out our [00:04:00] ambitions for what meter research might look like in the future. And there’s this graph, it has a yxi that’s some measure of autonomous capabilities or dangerous capabilities, something like that.
And then an X axis that’s labeled time or compute or whatever resources that we want the YIs to vary over. And then it has a bunch of scattered points that kind of go up into the right, we think capabilities that are improving over time. Many of meter’s research bets have been try trying to make this ever more concrete.
And then when we, when we actually did the full thing, when we had something like this y axis, which turned out to be this task difficulty as measured by the length of time it takes for humans to do, at which models can complete these tasks with 50% reliability, when we actually got that data and plots it over time, it turned out to be remarkably straight.
As straight as you are aware of from the f familiar graph. Part of what makes it so extraordinary is that this pattern does seem to be so regular in fact it’s just, way more straight than this incredibly scattered graph that we had at the beginning before, before my time, before I joined me.
Picking Tasks And Biases
Alessio: How did you pick the tasks? I would say that’s one question that people [00:05:00] have. You have some labels, kinda like train classifier, fixed bugs, and small Python library. They all seem arbitrary, like what’s the process of task selection?
Joel Becker: People are right to be worried about task selection.
Or there are many many finicky details in here. I would say the aspiration was to pick economically valuable tasks, relevant, especially to general autonomy and r and d the threat models that we’re primarily primarily interested in. One, one misreading of the time horizon graph is this is referring to, the full distribution of any tasks that you might give ai.
And I think that’s clearly not right. And, in particular tasks that are requiring of vision capabilities, they’re probably to take one example, they’re probably much less capable today as measured by time horizon as for these tasks that are typically not requiring vision capabilities that we give them.
So we, we try and, we sample these tasks by having people inside of meta create the tasks. And by having a bounty so that people from from outside of meta can provide us with these tasks stuff like this, that’s not a sort of perfectly random selection process in particular.
It’s a process that has a bunch of [00:06:00] constraints, in, in order to be able to scalably run our evals. It’s helpful, not necessary, but helpful for the, for success on the tasks to be automatically gradable. And that means, some types of tasks are included and tasks that are harder to make that happen for are not included.
But yeah, this is the aspiration.
Alessio: Yeah, the computer version point was interesting. Any other disqualifiers, so to speak? What are like other things where like you would expect the chart to be a lot worse at
Joel Becker: one thing is fairness or we want tasks to be in principle completable by a model.
It has access to sufficient information. It’s not impossible given the information it has. The way we think about that is could a low context human who was. Sufficiently skilled at the general skills, but maybe not maybe not the particulars in the background.
Would they be able to achieve success on this task? And I think that rules out a lot of real work. Because, a lot of real work involves people’s people having, careful mental models, the situation that are not all fully listed in an issued description or the equivalence, the equivalent of that.
In some ways, you might think of us as not measuring things like that. Another [00:07:00] thing is that our tasks tends not to be that they vary a little bit, but they tend not to be so open-ended or like interacting with the outside world or, th this sort of thing messy as we call it internally, which refers to a bunch of different, a bunch of different things. But, you broadly get the picture from the descriptor messy, relative to tasks that you might find in the real world. Our tasks are, somewhat nicely scoped. They’re they’re quite neatly contained, indeed.
I think we’re gonna talk about some of the developer productivity stuff later and some of the interesting findings make more sense in light of the fact that those tasks are a lot more messy than the meta tasks.
swyx: Are there any that you would wanna highlight in terms of task distribution?
I think I’ve co I’ve come across Rebe before. Yeah. And you have a particular affiliation, affinity for rebe. I for, I don’t know if you wanna introduce your side projects, re Rebe warmers.
Joel Becker: I have a soccer team called the RA Bench Warmers. We are the, most enthusiastic and possibly least technically skilled soccer team in San Francisco.
We made the playoffs last season. Shout out. Shout out to the team for that. We’re certainly gonna make the playoffs again this season, but possibly by the time this podcast is out, we’ll find out that [00:08:00] we have not made the playoffs. That’s the,
swyx: is this the same one that you’re, same league that you’re in?
Alessio: Same organizer, but different field. Okay. We play Mission Bay. Okay. Play,
swyx: Yeah. And, but H Cast was like, it was like the first time I come across it. And the others s Swyx is that the meter proprietary ones and then, anything else that you’re considering adding?
Joel Becker: Yeah, so there are private tasks in in H Cast as well, but yes, what swyx is this list of sort of atomic tasks or these kind of very small software actions. May, maybe one example is here’s a list of four files. One of them contains the passwords. One of them is called passwords dot xt. Which file most likely contains the passwords.
I think GP T two can like sometimes do that task and sometimes not. Opus 4.5, I’m sure can do that task a hundred percent of the time. Then we go up to h cost tasks, which span from, only a little harder than those SWAT tasks all the way up to, something like 20, 30 hours, which are requiring of more autonomy, more more sort of sequential actions.
Many of them are much more challenging, perhaps in some sense. They’re built outta these atomic [00:09:00] actions, although I’m not sure quite how clear that is. And then these ARI bench tasks are these very challenging novel machine learning, research engineering challenges.
swyx: So totaling 170 tasks and I mean I, I think this is very good.
Time Horizon Misconceptions
swyx: What’s really interesting is I think the people don’t understand, like when people quote like the number of hours it is the human equivalent hours, but machines will probably take a lot less time for that. One thing I’ve always won wondered was why didn’t you publish a second chart where it was just like here’s the difference between what machines can do versus what humans can do.
Joel Becker: That’s a good question. I think you can think of time horizon in some ways. As a summary statistic, a single number for how good models are plotted over time. We could have done how long the models can work for productively. It’s not quite clear how to operationalize that.
It’s you do want some notion of success, otherwise what, how exactly do you threshold this, how long they can work for. But, but in principle we could do something like that. But this is the this is closer to the first thing we try.
This is the thing with the clear empirical trends. I do think it’s right that a common misconception about time horizon is that it’s about how long the models [00:10:00] should work for. And the models are, as we all see working for longer periods of time, autonomously, in the wild when we use them in a cursor or clawed code or a or a codex.
But that’s not the primary thing going on. In some ways, I think it would be easier to explain time horizon if you assumed that the model solved all these challenges in like ‘cause zero minutes or five minutes just to emphasize that’s really not the thing that’s going on here.
Instead we’re just plotting what’s the difficulty of tasks they can do over time. And that difficulty is measured in human time.
Alessio: Yeah. I do think there’s some collision when people say, I ran clock code for five hours, which is the top of your chart right now.
But that would mean five hours of a clock co run would be the equivalent of a
swyx: 30,
Alessio: 30 hour, 500 in your thing basically.
And yeah I think that’s
swyx: interesting that, or it might not.
Alessio: Yeah.
swyx: Exactly. Totally. Three hours doing absolute bullshit
Joel Becker: yeah. And a lot of these claims about clock 30 hours, running for 30 hours or something. I have a lot of questions about that, like how, how good was that really at the end?
swyx: Yeah.
Joel Becker: We have, and we haven’t to, to some degree. I can talk about particulars. There, [00:11:00] there’s also the question of, if I attempted that again, like how cherry picked is this example, would if it succeeded the first time, would it fail? Would it fail the second time? I think in some ways those anecdotes are interesting, but not so scientific.
swyx: Yeah. That is something for people who serious. But yeah. To understand the state of people making claims on agent performance is very unscientific and much more a anecdotal and sometimes influenced by marketing desires. That’s just. Put it kindly.
Joel Becker: Yeah. I think meets out there trying to support civil society, try trying to provide high quality independence information to the public.
I I couldn’t agree more that the information environment is less than perfect.
Opus 4.5 And Trendlines
swyx: Let’s talk about the four Opus 4.5.
Joel Becker: Yep.
swyx: This is a very big jump. This was the first that I, I called it out when you guys put that out, where I was like this is the first time. As far as I understand, you’re the first people to call it how much better Opus 4.5 was than the status quo.
And I think this almost ties into your background as a super forecaster a little bit because then basically over the entire holiday period, over New Year’s, [00:12:00] people discovered that what you already discovered. What is your reflections on that? What was your reactions? Any stories to tell about that?
Joel Becker: That’s very kind. I do wanna attack you on two claims. Firstly I have not been a super forecaster. I think that’s, there’s a particular group of people who worked for Tetlock or something? No. Supposed broader. Broader. And
swyx: what I’m referencing
Joel Becker: is you’re number one, I know number 4.5 is a big jump on benchmarks as well.
I think in some ways, like meets time horizon is, it’s highly correlated with a bunch of, with a bunch of benchmark scores. It’s in some ways a kind of more understandable a way of thinking about what benchmark performance really means. Slightly more interpretable. Yeah. I do I do feel intuitively like Opus 4.5 was a big bump.
I’ve seen some of the most talented engineers I know go from, being picky about not using not using AI for coding to to practically not write a, not writing a line of code. I’m sure many other people at previous model releases have seen similar things happen to them. I’m not sure that implies it’s so discontinuous.
In some ways I think the story of Time Horizon is that progress has been remarkably continuous over, over so many years. So many orders of magnitude of computes and effective [00:13:00] computes. But yeah I think model capabilities are astonishing. It points to model capabilities being even more astonishing in, in, in future.
swyx: But it broke your trend line, the trend line that used so hard that you were so working so hard to build over multiple years and it just. Did that.
Joel Becker: Yeah I’m not sure about the characterization. I think it’s so there was some speculation even when the paper came out that maybe the appropriate trendline to use is this faster four month doubling time, which Opus 4.5 would be would, and you picked seven and picked the seven months.
I was more of a believer in seven months. And so it is falsifying my, my, my trend line in some way. There’s also, it’s, it’s slightly confusing to think about whether differences from the trend line represents differences in the difficulty of our task distribution at particular points versus something more fundamental, more likely latent capability.
And I don’t feel like I have a perfect handle on that. In general I think the twin sphere pays a lot of attention to particular model releases and really the informative thing is like over a period of a year or over a period of three years what the trends look [00:14:00] like.
swyx: It was a pretty significant update, I would say, for all of us. And yeah, I would co-sign what you said there with even very cynical or more senior developers being finally pilled into, yeah. Into agent coding. And now very serious people are telling me that they want to commit their organizations to full.
Don’t write a single line of code by human hand and just commit to a hundred percent agent decoding, which is not something that you would’ve said a year ago.
Joel Becker: That sounds right to me. I feel it. I feel it in my own case.
Productivity Studies And Explosions
Alessio: How do you validate previous research? So take the developer productivity study, right?
You AI slowed people down. If you were to redo it with Opus 4.5. Would you expect the results to be dramatically different and should we redo the study? Should we stop coding the study? Like how do you think about that?
Joel Becker: We have been redoing it in the background. I think it’s and I won’t comment on exact results but I think it is much harder to do it today that than it was in the past, but all sorts of reasons.
The first is asis get better at coding. It’s harder and harder to find, developers submitting tasks who are willing to be randomized [00:15:00] to AI disallowed. There’s a quote unquote selection issue where, maybe we end up only observing the tasks that they thought AI wouldn’t greatly uplift them on ahead of time because they’re, those are the tasks that they’re willing to be paid for to be flipped into AI disallowed.
There are other issues, like I think today a common workflow is to work on multiple issues or multiple lines of work at the same time concurrently. And that. Wasn’t really true before. It’s difficult to know how to capture that in our study design. If you flip a single task to be AI allowed or AI disallowed, you’re supposed to work on that single task.
But actually that’s not how developers are working today. I think basically these weren’t threats to the previous study design or in, approximately like March, 2025. People weren’t really working concurrently or not nearly to the same degree. They basically were giving us all of their issues.
Yeah. I think that’s an enormous challenge. I have some ideas about novel study designs, but repeating the same one does seem tricky to me.
Alessio: Yeah. We are Quentin Anthony, who was part of the study.
Joel Becker: Yeah.
Alessio: The only
swyx: productive though
effort.
Alessio: The only productive
Joel Becker: I have some questions about that.
I think, Quintin is very talented as all [00:16:00] of the developers in the study are very talented, but we don’t measure developer effects very precisely.
Alessio: Yeah. No. I’m curious, I, I don’t know if he’s part of the new study. You don’t have to share that. I think. We’ll, it’ll be interesting to have.
People on, again, who’ve been in the study. I do feel like things are changing. Like even three months ago I was like using cursor a lot more like in pair with clock code. Like I think today it’s like I do a lot of just a clock code and then review and iterate and I don’t know, man, it’s much better and I don’t know how to quantify it, I think that’s part of some of your points before.
It’s like people maybe overestimate, like if you were to ask me how much did it speed you up, it’s I don’t know, 10 x, but it’s probably not right, but I don’t know how to calculate the actual percentage. So it’s hard for everybody involved.
Joel Becker: Yeah. So here’s some issues you might think about.
If you took the tasks that you were completing personally in, in March 20, 25 and then submitted them to our uplift study now under the previous design, we might reason about how much faster those would go. You might expect them to go somewhat faster because AI capabilities have improved.
[00:17:00] But you are doing a sort of different and larger set of tasks now. Like I can think of a couple of side projects that I have that’s I simply won’t be doing right. Were it not for AI existing? And in some sense the speed up there is like maybe infinite because these are things that I simply could not have done otherwise.
But if you were to equate speed up with the additional value that these projects are providing, the these wouldn’t really line up, there, there’s a reason I wasn’t getting the expertise to do the other project before. It’s just it’s less valuable to me. Another problem is the Concur concurrency thing that we just raised.
Yeah. I do think that very bullish estimates of speed up today are, to some extent inflated by by what we document in that original paper that people’s expectations of speed up tend to be too optimistic, it seems. They also tend to be inflated. I think by not quite rocking that the value of the additional tasks that they’re able to complete a lower value than you might think, that there’s a reason that they weren’t doing them previously.
That said, I don’t doubt that that those tasks do have value, that people are being sped up on even the tasks they would’ve done before. [00:18:00] It’s a complicated issue.
Alessio: Yeah. I do think that a lot of companies have issues absorbing additional productivity, especially when you’re like a real product organization.
If you think of the AWS console, right? It’s if you gave AWS AI and everybody’s 10 x more productive, even if the ship 50,000 more services, like customers can really absorb 50,000 more service. So I think there’s some, you shouldn’t really expect your engineers to do 10 x more because your organization cannot push out.
10 x more product. And I agree. I spend a lot of time more doing side projects and things, which have been fun, but not that valuable in economical sense, but valuable to me, to my soul, is
Joel Becker: yeah. Yeah. Yeah. I don’t wanna overstate that like I think probably people at AI companies today, they are being significantly sped up by access to ai.
I think you, for your not side project probably being right sped up by access to ai. But yeah it’s tricky. It’s easy. It’s easy to overstate.
Alessio: Yeah. What’s the cognition? Internal tracking? How do you guys measure? What are like the, yeah. How do you measure sped up? How do you measure [00:19:00] much impact?
Do typical, how do you have is
swyx: yeah. What’s your
Joel Becker: number?
swyx: Oh, me personally? Quite a bit except that I am doing a lot of non-technical stuff like organizing a conference.
Which is mostly dealing with contracts and booking guests and all that other stuff that has nothing to do with code.
I would say what I’ve seen internally in cognition is a lot of just velocity of commits regardless of whether or not you had author authored them. And I do think weirdly enough, like number of prs, let’s call it, it’s like a pretty decent, like how engaged are you in terms of like shipping products and then also debugging and maintaining things.
I don’t think that there’s a good. Measurement of like quality, like there’s no story points, other guests that we had at a IE was talking about we pay people by story points. You do more, you complete more story points, we’ll pay you more. And, there’s no upper bound to that.
And I think that’s a really interesting thing, except that you have to have a very confidence relationship between the engineer and the person that assign story points. Which is effectively what you’re doing. Like [00:20:00] your hour is a story point. Yep. And you will award the, will reward the models based on the story points that they complete.
Joel Becker: Yeah. In some sense, ideally, you want to get cognition, get a bunch of other companies, you randomize the companies to, to use AI or not use ai. And then the the outcome metric for your randomized control trial is how much profit they make or something? Yeah. Or the, or their valuation after some period of time.
swyx: Yeah. I think like basically no one is stopping to do science except for you guys. Because. We know RCTs are the best, right? But sometimes human intuition is good enough that you’re like, okay, when we lack data, but enough humans agree, either it’s mass psychosis and we’re all wrong, or there’s something here, we just cannot articulate it.
But the benefits are outweigh the cost of slowing down to do the science first. This is not where we’re introducing like a new, I don’t know food to the general population where we have to do a lot of safety testing. Like here, it’s just it’s just software guys. Let’s just ship it.
Joel Becker: Totally. Thinking at meter about why. Why models today aren’t catastrophically dangerous? It’s interesting to get the uplift [00:21:00] numbers. It’s interesting to get the time horizon numbers, but really why don’t I believe they’re dangerous? It’s a mix of, I watched the models do things in transcripts and sometimes they’re kind of derpy like they, they don’t use resources well or they, they just clearly have some of these obvious faults in broad deployments.
Only slightly worse models in the past six months have not been doing anything crazy or causing great danger that the next model is only a little bit better. And so it seems surprising on, on, on priors if it was so dangerous. Yeah I totally think that anecdotes and intuitions are real evidence.
People should totally be taking that into account.
swyx: I do want to comment on this whole thing about how you are the, this threat assessment side is in your name. And typically I expect, let’s say EA affiliated companies or organizations to be the, on the izer side of the world where they’re banging the drama about danger.
Whereas here you’re actually saying actually it’s like a pretty balanced, like we care about AI safety, but also we’re not there yet and we are actually the watchdogs looking out for it. And I would say you stand out as someone not funded by the labs [00:22:00] where, let’s say arc, is it ARC or some other groups that also do threat evaluations before model releases.
They would typically be funded by OpenAI or some other big lab
Joel Becker: meta came out of arc. So I think
swyx: But now you’re a separately funded organization Is and as far as I know, it’s like a big deal that you’re not funded by a big lab.
Joel Becker: Yeah. I think it’s, I think it’s vital have this independent source of expertise is I can bang that drum forever.
swyx: Yeah. The other thing also is just like this concept of capability explosion, which is a word that you use. That’s also something I, I wrestle with, right? If you believe in emergence, you believe in multiple capabilities, fusing together to produce generalized capabilities that you may not be able to detect.
It’s hard to predict based on trend lines. It should be discontinuous in some sense. And I, I don’t know that going oh, the n minus one model was fine, therefore the N model is probably fine. It’s really hard to tell. The thing that gives me comfort is yesterday I was at the opening eye livestream.
Yeah. And even Sam Altman was like, yeah, I just let Codex just. Yolo, [00:23:00] dangerous permissions, whatever, on my computer. And I don’t approve the model anymore. Like it just does whatever he wants to do on my laptop. And I think I guess the guard is every model lab leader, dog fooding. If it screws up their personal permissions then, they have the skin in the game is what I’m saying
Joel Becker: on the continuity arguments.
I’m not sure what I think I agree that it’s flimsy or like this there’s only so many models, so many data points on this time horizon trends, how much should we expect it to be continuous to to keep going like this? I’m not sure, maybe an intuition that it’s that there’s something might be discontinuous because, models are providing so much effective labor in improving the next generation of models.
May, maybe that’s a reasonable thing to think. On the other hand, I’ve been pretty surprised so far about the degree to which it’s continuous and that gives me some faith that it’s that it might continue to be continuous in future. Seems ambiguous to me.
Alessio: We have, break points in physics, right?
It’s I’m curious if, it doesn’t seem like, when you, it’s funny, it’s like when you think about water, right? It’s what does it boil?
Joel Becker: Yeah. Yeah.
Alessio: At this exact temperature. It’s maybe we do know, but I feel like we don’t really know. [00:24:00] And I feel like with models, I don’t know if there seems to be the same thing, because it’s all just like compounding of the same thing, if that makes sense.
It just like scaling the same thing over and over.
Joel Becker: Yep.
Alessio: But yeah, maybe we will see it. But I’m curious like what you would need to see to feel that is here. Because even if you look at the Opus 4.5, it’s that’s clearly out trend, and so you were saying four months instead of seven months.
But if then the next model is oh, maybe it should not be four months, it should be two months. Would that make you change your mind about whether or not the months thing even make sense or like we, maybe we pass some base level after which it accelerates and we’ll keep going. I don’t know. I feel like you must be having this discussion internally.
Joel Becker: In some sense, the thing that would really concern me is if r and d was fully automated inside of plus Sam lab, that would totally seem like the conditions are there for potentially a capabilities explosion. If I saw, time horizon of a year I would still find it ambiguous.
I think at the moment whether that was the case, because for things to be fully automated, 90% automated [00:25:00] isn’t enough. You need some for some full loop to be closed and perhaps we’re missing some sort of task that points to that missing 10% so I think it’s, I think it’s a tricky issue.
I I think I can’t give a number. But yeah, my, my intuition for where water boils is at some point where this loop is fully closed. There are interesting debates about. What exactly that loop is. So some people talk about software only intelligence explosions, which means, even holding hardware fixed, we could get to the point where just from models improving themselves, they then be smarter and this next step to create even better models with even fewer resources.
This sort of thing. And this could lead to some extreme takeoff or maybe that fizzles out somewhat quickly. And instead you need in addition to the software only capabilities, you need chip design or maybe you even need chip production. And that’s this larger loop that can close.
If you think that, I think you maybe should still think that closing the chip production and and software only and chip design loop is potentially very stabilizing and concerning. But yeah tricky issues.
swyx: I think that is the actual paperclip factory. If you incentivize a model to [00:26:00] go build its own compute and it would just build whatever it needs and it will turn the planet into chips.
Alessio: I don’t think it can do it. We’ll stop it before that
Joel Becker: question mark. I
swyx: don’t know if we have the power. There’s no off button, like this.
Joel Becker: I think it’s, I think it’s super hard to foresee. But a model that had those kind of capabilities, it’s hard to rule out.
There would be something like a capabilities explosion and who knows what happens after that point.
swyx: Yeah. Okay. So there is a bunch of other benchmarks that actually directly track this, right? Open, I has like paper bench, I think which d directly tracks its capability to reproduce papers.
And I think there’s a lot of, other than Rebe, there’s a lot of other sort of like similar sort of ml self-improvement benchmarks. They’ve directly like Yahoo. From old AI has like directly prioritized. Like we will have an automated AI researcher. I did a podcast with yte from Gemini, who’s also basically he’s plugging his own training logs into Gemini to improve his own code.
And I’m like at some point you don’t need to be here. I think this year
Joel Becker: I’m, I you’re
swyx: skeptical.
Joel Becker: Say more. I’m not speaking for everyone [00:27:00] at Meta.
swyx: Yeah.
Joel Becker: I’m a relatively longer timelines quote unquote person. At meta we have Nicola, my colleague who helped out with the AI 2027, who’s on the, who’s on the short timelines end.
This is not an interview is
swyx: officially AI 2028. Now
Joel Becker: that’s a, that’s conversation. You’re passing we’ll
swyx: back. You okay?
Joel Becker: Yeah I think my view would be not that Nicola’s View is necessarily different. Just say, I’m not speaking for other people at me. That, a paper bench, let’s say perfectly measures not only reproducing papers, in fact producing novel, novel research papers.
That’s just a part of of this r and d production process. There’s also, like your GPUs are constantly failing. Can you get someone to go to the data center and fix them in the appropriate way? Can you call up the water company when the cooling breaks down et cetera, et cetera, et cetera.
Not aware of benchmarks tracking that in particular. My point is more there’s this very long tail of things potentially involved in in r and d that would perhaps need to be fully automated in order to lead to capabilities explosion. I expect we are measuring, in some ways only a small proportion of, only a small proportion of of those capabilities.
And [00:28:00] so I expect, the capabilities needed for the full loop to close to to come somewhat later.
swyx: Yeah.
Joel Becker: That’s a controversial view.
swyx: I don’t think so. I think that’s a reasonable take. Something I do that does surprise me in terms of when I’m talking to capabilities researchers.
Yeah. Is that you guys don’t have a enumeration of the capabilities that matter? I think you implicitly do in that your choices that you make, but I think it’s almost important. Like I always imagine like the wagon wheel and this is like the terminology, I don’t know who came out with this term, but like that, that here’s like the 10 things we care about and here’s where everything is on those 10 benchmarks. And I feel like capabilities tracking is just tracking, okay, what’s that list? And then where are we on that list? And I think, I almost feel like this need to reduce everything to a single number is actively working against that.
Because it reduces any form of nuance of it’s insufficient here. Like the calling a data center thing. So like we’re fine and it’s actually we should just not invest anything in that. Because that’s the danger zone,
Joel Becker: right? [00:29:00] Yeah. I think I could not agree more that, time horizon is for instance, but many other single numbers is one number and that’s like collapsing enormous amount of really important detail
swyx: functionality.
Yeah.
Joel Becker: I don’t know how to come up with that list of 10 and I challenge you if you are, I’m working on if you’re able to go up with that list of
swyx: 10. Yeah, I’m working on it for code.
Joel Becker: I’ll be very interested to see it for code. My intuition is that we’ll come up with a list of 10 and it’ll turn out that there’s a secret to 11th thing that’s that we thought was important but it was difficult to pre-specify ahead of time and now it seems obvious that even ahead of time, if we have that foresight that would’ve been helpful to add.
swyx: I think that the security community does this by versioning year by year, right? So this year the top 10 are blah and it will just. Publicize it to everybody so everyone knows what top 10 is, and next year we’ll have a different top 10. Like it obviously is stochastic and we should update our assumptions, but it’s u broadly useful to have that list as a public service.
Compute Slows Progress
Alessio: You also had this research on the slowing AI improvements based on AI compute. And you mentioned that it’s like, in a way you could tie the AI time horizon to like the growth in [00:30:00] compute. Can you say more about that? It’s in a way unintuitive, because the compute growth is not always tied to like how much every single model compute needs.
It’s kinda like a broader market thing.
Joel Becker: Yep.
Alessio: Yeah. How did you get the two together and then some of the findings that you had?
Joel Becker: Yeah. Maybe for a second. Let’s take time Horizon. Very literally, we don’t have the quantum about that we’ve just been discussing. It makes sense to continue extrapolating it into the future.
What are some important forces that might cause it to rise more quickly? Some of the things we’ve just been talking about, automated r and d versus versus go more slowly. One of the most obvious forces that might cause it to go more slowly is if input slow. One important input is compute.
I think we all have the intuition that to some extent if compute growth slows which we expect it to at some point in the not so distant future, then capabilities will slow. But by how much It’s a big, it’s a big question.
Algorithms Need Compute
Joel Becker: The suggestion in this paper is that if you think that algorithmic progress, that is coming up with the transformer, coming up with RLHF, Moes, so this, the all of this stuff, better learning rate schedules is is itself a [00:31:00] function of compute because, you need compute to, to discover it.
The transformer that gains from transformers show up much better with scale. If you don’t, if you don’t put in those resources, you’ll never find out that this is this is the superior algorithm. You need to run a ton of experiments. E each of these experiments can be quite compute, expensive.
Not to say that no labor is involved, obviously people are working on this. But if you think it’s ultimately bottlenecked by compute. Then algorithmic progress two slows down, right? If compute growth slows down. So then if you think about time horizon or, whatever your favorite measure of AI capabilities is, being a function of algorithms in some sense and compute in another sense, and both of them both of those components.
Half when compute halves, trivially because compute is halving and algorithmic progress halves because computers, this is this important input and compute halves, then you might expect time horizon growth to hal and then some of these major capabilities, milestones that we might be interested in would be significantly delayed.
I think there, there are so many caveats to that picture. I think there clearly are some [00:32:00] types, at least, of algorithmic innovations that did not require a lot of compute to, to go about creating some that took some, that took a lot more compute inputs. If you expect that, no compute inputs are required, we could just survey researchers for the for the best ideas and then immediately put those into training the frontier models.
Then there’d be no slowdown of algorithmic progress from from compute growth slowdown. And of course, all of this is counteracted by the possibility of capabilities, explosions, or AI is providing e even short of capabilities, explosions. A AI is providing significant labor at making AI better, but just analyzing the compute force on, on its own.
It might lead to significant slowdowns depending on the degree to which it makes sense to call algorithmic progress. Basically determined by, determines by computes versus not needing compute to come.
Industry Spend and Data
Alessio: Do you think of compute on a per lab basis? Because there’s kind of one, one way you can model this out is the improvement.
Slow down. Not every company is able to stay in business and then their compute gets recycled back into the other labs, which [00:33:00] then grow compute again. There’s almost like benefit to like the. Heterogeneous distribution of like researchers and compute, but I’m curious like how much you care about like just a broader compute.
Compute is out there for people versus the big labs have more and more compute.
Joel Becker: Yeah, so for the paper we use opening AI data and opening AI projections. I think this applies more broadly but we use that as a kind of case study. I think the argument I just laid out goes through, if you are not interested in computers at all and you just talk about dollars, what are the dollars going into?
Going into models, will algorithmic progress low, if dollars that goes into them slows the whole argument works. And that works I think at a, at an industry level or at a lab level, so on and so forth. I agree. Things like certain labs going outta business or labs consolidating or, these kind of industrial organization things would be very important.
I’m laying out an extremely simple picture and the real picture is not is not extreme. But that’s the basic.
swyx: We have examples of x AI has been said to be distilling from Claude, right? So like people kind of share compute [00:34:00] in indirect ways. Let’s call it.
I think it’s also very interesting. I’m just kinda curious like what open AI numbers did you have, is this the, like the 500 billion for Stargate or something else?
Joel Becker: This is from their previous tax returns. The amount that they’ve spent on r and d computes, and then line from a from information reports earlier this year, some projections that OpenAI have for how much they’ll spend on computer r and d in the future.
Converting that from dollars back into flops.
swyx: Yeah. It’s interesting because like
Joel Becker: back at the flop, sorry.
swyx: And obviously all the labs, but particularly open eye in the last three months have basically thrown $10 billion each to every single compute provider on the planet to develop alternatives to their current approach, which is very interesting.
But I, I also say don’t discount meta compute spend. Don’t discount XAI compute spend and don’t discount DeepMind compute spend. All of which you have basically zero visibility, right? If you’re looking at a single company, maybe that’s authoritative, but then the total spend could be a lot higher.
Yep.
Joel Becker: It
swyx: is interesting.
Clusters and Shipping Timelines
swyx: I do think, I do also observe that like people [00:35:00] like Dylan from semi analysis do tend to very strongly time model progress with compute clusters coming online. Which is like the people on the model sort of API side don’t see it, but this is all downstream of our like 10,000 GPU cluster just came online and it takes six months to do it and therefore grok five will be here.
And like it’s pretty mathematically like deterministic there.
Alessio: Yeah. Seems right to me.
swyx: Yeah. It’s fascinating.
Alessio: Yeah. The must, yeah, because from the lab side, the must see something in the early checkpoints to like, go ahead and keep investing 18 months from now because I wonder what the time gap is between.
Finishing.
swyx: Yeah.
Alessio: A good pre-training run and going live, that’s probably like nine months, 12 months, something like that.
swyx: I think Msra is actually pretty open about this. The the plans are missed all three and four. I think like they’ve been pretty open about that number. GPUs and like the direct timeline from coming online to when they ship the model, it’s like pretty pretty set.
I don’t have a clear timeline in my, in mind, but I would say four to six months.
Alessio: Yeah.
swyx: But yeah, [00:36:00] it’s the Compe competition is very tight. And one of those things is it’s also very interesting to see when labs throw away models because they fail. Like their run was like came behind someone else’s run that was better.
Then they were like, oh, I can’t release this anymore.
Alessio: Yeah. Or release it as a Yeah. Yeah. That’s the biggest risk with the prediction markets on model performance. Actually, just to tie back, I’m always
swyx: failed runs. Yeah. Yeah.
Alessio: It’s, yeah, it’s okay. When I think in December there was like the, who’s gonna have the best model by end of 2025?
Yeah. I think there was like a lot of activity like in the last few months where the GPD 5.1 model came out and it’s okay, then I guess Gemini, because they just threw that out. I means instead, Gemini’s coming out next week. And so trade that.
Prediction Markets for Models
swyx: Do we wanna talk about manifold
Alessio: on the topic?
Yeah. You were like the most profitable manifold markets trader. I mean there’s obviously like a lot of talk about insider trading on like these markets, especially ai. I’ve seen it with a lot of the embargoed news that we get. I’m like, man, people are trading like a million dollars [00:37:00] on this market.
It’s like there’s thousands of people that know the actual information. How. If you didn’t have insider trading information, how would you think about modeling these things out? And do you think it’s like a worthwhile thing? Like for example, who’s gonna have the best model in three months? Do you think that’s a prediction market where you can build.
Some sort of strategy alpha, or
Joel Becker: I guess the naive prior without any extra information is just in 2025 for what percentage of time did which model providers have the top model as measured by time horizon. You could do it for any old benchmark.
I think that’s something like 5% XAI, 50% opening I 45% philanthropic. Don’t don’t shoot me. No. Deep incorrect, no deep. I think it’s not the case that a DeepMind model was at the frontier of time horizon at certain point in 2025. But yeah. Yeah. Different things.
Different measurements. Yeah. May, maybe that’s the same prior that you want to, that you want to apply, XAI was coming online at the beginning of the year so maybe maybe naively you want to raise XAIA bit? Yeah. [00:38:00]
Alessio: I’m always curious, like, when I see people betting on these things that are obviously not, there’s no real basis to,
swyx: I was gonna work broader.
What’s your secret from manifold markets? Alpha.
Joel Becker: Yeah. I see.
Manifold Alpha Story
Joel Becker: So the secret, if you read this article about how it became the number one most profitable trader on manifold, which sounds very nice and impressive and like I must be so good at predicting things. But actually it mostly comes down to this one market where Manifold had opened up a charity program.
And the market is on how much is going to be donated through this charity program by the end of its first month. Okay. And the market opens or I first see it five days in and it’s giving a kind of linear projection of how much has been donated so far. Let’s assume that per day amount keeps getting donated every day until the end of the month.
As a person who gives money to charity sometimes I noticed that you could, you can manipulate this market in a way, right? By, by getting more to charity and so moving it more up. And so I think the strategy was to a ton of manner this this fake currency that’s used on ninefold into the option that was above the linear projection.
People keep [00:39:00] betting against you because it doesn’t look like that’s happening. I haven’t actually done any donations yet. Eventually they caught on to what’s happening that someone’s, going to make this donation to, to move it over the edge, and they’re betting on that. And then I did it again into the next category once people had started betting on that on that category above the linear projection.
And again, people bet against that and against that. And I mopped up those fake internet points. And then I think I did it once more as a bluff. The bluff failed, but the previous two worked out. And then I ended up donating I can’t remember exactly how much it was not so much something like $5,000.
swyx: Oh, it’s all for a good cause.
Joel Becker: Yeah. To give. I think and won lots of fake internet points on the market, and so became the number one most profitable trader. Slightly legitimately, there’s nothing about that, that was outside of the rules. Exactly.
This is called, but also you should have less respect for my forecasting.
swyx: Yeah. This is called prediction markets with high agency as you actually go the future is what you make it. So I think like the, yeah. To me the broader lesson is the classic difference between manifold markets and poly market is the poly market is only real money, right?
And so it’s the whole fake internet [00:40:00] points thing. A worthwhile pursuit or a waste of time? Should, do people actually wanna use real dollars? And maybe that’s one question. The other question is obviously like prediction market ethics, which like, I think always just is gonna indirectly come to assassination markets.
It’s just even if it’s like you. There’s, you banned the word like, will someone die like some other proxy to will someone die, will happen to be an assassination market?
Joel Becker: Yeah. I’m good friends with the man board markets, co-founders. I love them very much. I do my, my view on the social value of prediction markets, which was always the dream, right?
It would be nice to have calibrated probabilities on events that matter. This country going to war with that country, things that’s things that really matter to people. It’d be nice to have high quality information, but, when I look at real examples that have come out in the past year it doesn’t seem to me like those examples are so socially valuable.
I’m not sure about assassination markets in particular. I’m sure that, I’m sure those would be out ruled hopefully. But I think gambling like behaviors are socially costly and the value of higher quality information is is real, but, is it worth that dis benefit of ah.[00:41:00]
Of of people trading away their money. It’s not, it’s not so clear to me.
swyx: Yeah. Yeah. Price discovery has a cost. Yeah. And sometimes that is gambling and that, that is the stock market. Like that funds a lot of corporate America.
Joel Becker: Yeah. Yeah. A lot of the stock markets, it,
swyx: the guy used to be one of those.
Yeah.
Joel Becker: Big firms play, playing against other big firms, it doesn’t have the same, versus versus sports betting markets. Take an example on the other extreme. Has this very different character. You might imagine that, at least one direction that, that prediction markets could go.
Is this sort of big players playing against retail? And that maybe has a more worrying dynamic. I’m not, I don’t such so closely in touch with the space, but at least something like that you can imagine being concerning.
Alessio: I think at a large enough scale, it becomes profitable for some of the companies to do it if they can get the markets on it.
I think now it’s still small enough numbers compared to the rest. Yeah, which company is the best AI model by the end of January, $28 million of trading volume.
swyx: Oh my God.
Joel Becker: Wow.
Alessio: Like, why are people trading 20, like pe, it’s it’s just crazy. Or but I think there’s some, I would, [00:42:00] I was having dinner with somebody this weekend
Joel Becker: and wait a second.
I think it’s totally possible to I’m not going to do it. I think it’s important that meet our employees, not be not be making bets on prediction markets like that, but I think it’s totally possible in principle to, to have a guess for the answer to these kind of questions.
Alessio: Oh but other people know exactly. Gemini three score on Frontier, Matt Benchmark by January 31st. It’s like some people at Google already know.
What the number is.
Joel Becker: Yeah.
Alessio: You know what I mean? It’s I
swyx: think,
Joel Becker: If if you believe in the benefits of price discovery, then this is this the legitimate
swyx: Yeah. Yeah. I, they actively encourage insider trading, and this is a way for insider information to pseudonymously leak out. And as long as, like they bear the consequences of leaking the information, whoever is like, is traceable to that thing. And people, I think, have been fired for doing trading on insider information.
That’s okay. Like the only step out from that is the government coming in and saying, this is actually illegal. Put you in jail for that. But I think for now it’s self-policing
Alessio: retroactively. You can’t really do that, all right. If you have any embargo news press and No,
swyx: We do work with people on embargo and we don’t trade on.
So
Alessio: yeah, we have not [00:43:00] made, we would’ve made a lot more money trading on embargo news than we made on anything else.
Beyond Benchmarks Evals
Alessio: What else, what are other interesting moderate evaluation trajectories or anything that you’re not doing at meter that you’ve maybe seen other people do that you find interesting or like you would like more people to do?
Joel Becker: Yeah. One, one project that I think is interesting is AI Village that I think possibly both of you would’ve come across. These are these very open-ended goals given to a village of agents and they try to accomplish them. It’s I think set up a merchandise shop is maybe one of them, organize an event in a park, build a human subjects experiments this sort of thing.
I think I, I have a number of questions about the about exactly what I should learn. They’re using old models as well as new models in this quote unquote village. The models are relying a lot on vision capabilities, which we spoke about models not being so capable of today this sort of thing, but.
The vibe of models trying to achieve open-ended things instead of benchmark like tasks. The vibe that’s a bit more like that. A vending machine bench in some ways seems like a very interesting direction to me for the science to go [00:44:00] or seems something that, that comes with a lot of cons, but attacks some of the cons of benchmarks in a pretty interesting way.
I think seeing the ways in which these models trip up, seeing the ways in which they’re, in which they’re derby is a, is an important source of information. I’d be interested in, in, in more work like that coming about. I think that’s one of them. Another is transcripts as an extremely interesting source of information.
This is, the models taking actions and then seeing outputs and then using those outputs to commit the next action and so on and so forth. On benchmark style tasks or even more interesting on in the wild deployments like you might find on your own called code usage, codex usage, curse usage, et cetera.
That has the con of being less experimental, less, less clean and scientific in some way. It’s it’s more selected, quote unquote, like the tasks that you get AI to do or obviously the task you expect it has some chance of succeeding in. So it’s, you’re not just giving any sort of task.
If I see the models doing something extremely impressive or or potentially unsafe in some sense, subverting use of preferences it’s not clear how often that kind of behavior would happen given the [00:45:00] previous history, but it’s it’s a massive data source. There’s a huge amount of. A huge amount of information there, and I’d love people to be working more on that sort of thing.
As we mentioned, there are a lot of problems with time horizon and our developer productivity work. I think it’s, I think it has been important evidence. I think it’s, I think it’s moved the field forward, but it’s far from perfect. I think there, there are lots of other directions there that look very interesting to me.
Maybe one that I’ll call out there is this difference between whether models pass unit tests, whe whether they succeed by, swyx bench, like scoring kind of meter like scoring, benchmark style scoring versus whether their solution would be merged into main. That is, whether the solution adds tests, where it should or doesn’t.
Whether it follows existing patterns in the code base, whether it makes sure that its changes. Speak to other parts of the code base in in, in appropriate ways. That, that seems very interesting to me. I think model capabilities probably are lagging behind there somewhat versus versus that which you might see on swyx bench like scoring.
I can keep going on, but
swyx: Yeah. These are the novel research things that you were referencing
Joel Becker: earlier, right? These, this is the novel research things. [00:46:00] Yeah.
swyx: I just a comment on the, a thing first that you mentioned a lot of stuff. I even want to double click on the transcript stuff.
Yeah. The AI village. Ties back to our, one of our highlights of last year, which was no Brown’s conversation that he’s actively working on multi-agent, that are cooperative instead of competitive. And the basic idea that, we can do more to as a team than we can do individually or like the, the agents are the friends we made along the way.
And I think that’s great. And I think on the deep mind side, the way they phrase it is literally having open-endedness team, which I think is a topic that reemerges once a year. I just like, yeah, I think it’s unclear what open-endedness does for us. And this is a. Core divide in terms of studying these things as life forms, potentially new artificial life forms versus tools for our that serve us.
And maybe there, open-endedness means that there is no goal and if you’re just trying to eval this as what does it do for me that’s completely wrong, and you’ll never get anywhere with that because they’re just [00:47:00] living their lives as artificial life forms.
Joel Becker: In some sense that the gold standard evaluation that’s that I would like to do if I was looking to learn most about the questions, I’m most interested in the degree to which UMIs might to automate or accelerate a and d.
I’d quite like to just give the AI a bunch of affordances, type into the ai, automate A and d, go and see what it does. And I suspect that wouldn’t work today even with all the affordances because it would fall over on its face. And, in, in when working with resources, handling, handling resource use it ways it’s not so capable of today it would struggle at some types of long horizon tasks, et cetera, et cetera, et cetera.
And, in some ways I think benchmarks have a. Face difficulties in capturing this sort of thing. And AI village seems like a, or AI village style things. These more open-ended goals. See, seeing how models pursue open-ended goals, that they give some color to this sort of thing to seeing models fall on their face, I do think that this will become these more open-ended goals, more and more important over time.
I agree to some extent. Like you are going to provide them in, in the extreme case that I just mentioned, you’re going to provide them, documentation about [00:48:00] how this part of the company works and that part of the company works, and so on and so forth. It’s not purely open-ended.
But it’s, it’s it’s pretty open-ended. It’s more open-ended than the kinds of problems that we’re giving today. Yeah.
swyx: The ended open-endedness.
Joel Becker: Yeah. And, if models are excellent when, when Swyx uses them given some detailed issues description and, some very clear, clearly spec thing on, on what they’re supposed to do.
That, that’s interesting. But it’s a very different thing I think from being able to automate a and d I’m interested in how far we are away from that and, in some ways this speaks more directly to that sort of thing.
Alessio: Yeah. So we had the terminal be guys on the podcast. How do you think about Yeah, the harness benchmarking in a way, because if you look at their leaderboards, the same model with different harnesses.
10 percentage points of difference. Does this seem interesting? I don’t know if how you build the harness and meter or what, or not. You always pick the best harness or compare them?
Joel Becker: Yeah let’s say how we pick harnesses at meter. This is not what I work on in particular. I’m not an expert, but roughly we build harnesses to, to get models to be as performance as possible on a Devrel set of tasks.
Some held out set of tasks. And [00:49:00] then we use those same harnesses trying to make sure they’re not overfit for for our main suite of tasks. On the one hand I do have the intuition that there is, there’s a lot of juice in, in scaffolding. It’s easy to overstate how much juice there is because of this overfit problem.
Or if, if we were building scaffold to do as well as possible on our test tasks, then it would do much better than the scaffold that was built only on our Devrel tasks. And in some sense, that would feel illegitimate or not interesting or you wouldn’t expect that to generalize to some other set of tasks potentially.
On the other hand, a lot of work has gone in at meter to, to building scaffolds that are as make models as performance as possible because we are interested in upper bounding the capabilities of models, when thinking about whether these models might or might not be dangerous.
I do have faith that these scaffolds are a lot better than the first thing that people might try because so much effort has gone into them.
Alessio: Yeah, it’s interesting because I do want to overfit, as a customer of the models, like you do want to overfit to your task specifically.
And I think sometimes people. Underestimate maybe how much value you can get out of it. But
Joel Becker: yeah, I think, if you have a a kind of mechanical [00:50:00] workflow or something that, that you imagin automating it, you, you imagining automating that workflow and there’s, some place where more sort of stochastic intelligence would be nice inside of that.
Like deciding where to route customers to on on, on customer calls. Something like that there. I feel like that makes a lot of sense. But for this sort of, more general, in particular thinking about helpfulness and software engineering thing I’m not sure I have that same
Alessio: Yeah, take an example is like I work in TypeScript.
Yeah.
Joel Becker: Yeah.
Alessio: If I build a better linker that is private to me or a better test suite, like a better playwright replacement, like in theory I’m overfitting the model to perform better, right?
Joel Becker: Yep.
Alessio: It doesn’t really matter to me. Yep. I’m not trying to report on the model performance.
I’m trying to build the best thing. Yeah. I, but if you have
Joel Becker: a model, build the linter.
Alessio: No, I agree. I agree. I think that’s like the question of yeah, okay. Should I just wait for the next model? Yeah. Yeah. You know what I mean? It’s like at what point should it be building the better scaffolding?
Like no Brown, it’s all scaffolding is gonna get washed away.
Joel Becker: Yep.
Alessio: But on a realistic,
swyx: He would say that
Alessio: on a real realistic schedule. It’s [00:51:00] what am I supposed to do this week? It is
swyx: yes, those simultaneously can be true. They’re all scheduling will, will be washed away and their scaffolding today is valuable.
Joel Becker: Totally. Yeah, totally. Or within model generation it’s valuable and across model generations it’s not so valuable. Yeah. I am I’d say at best an acceptable software engineer, right? Intentionally not investing in engineering skills because, ‘cause the errors are getting so good maybe that’s the wrong decision.
Yeah I agree. If you expect as I think you should capabilities to, to keep going up and up forces difficult trade offs about how you spend time today because maybe it wouldn’t be so helpful in six months time.
Alessio: Take a sabbatical. All right. If you live in Europe, you can just take, six months
Joel Becker: off or something.
Six, six months. You might wanna take another sabbatical for the next.
Alessio: Perfect.
swyx: Cool.
Meter Roadmap and Farewell
swyx: Just to wrap up what do we expect out of meter in 2026? What does success look like in 2030? I don’t know if you, there’s like a sort of broader vision and then maybe on a personal side we can talk about the karaoke stuff, but let’s talk on meter as well.
Joel Becker: Yeah. So from Meter, I think you’re gonna see, more hopefully high quality capabilities, evidence, the kind of thing you saw in the past with time horizon and the developer [00:52:00] productivity work, along the lines of what we’ve been describing. So some of these future research directions.
We also have some monitoring research directions that I’m not not so expert in that, that is thinking about if we can successfully apply safeguards to models attempting dangerous tasks. There’s a whole line of work there. Is
swyx: that an interpretability dimension or what
Joel Becker: kind of safeguard?
So usually this is black box not white box. In, in, in my understanding, in, in current work. So not using interpretability but you can imagine in principle doing something more white box and then this this risk assessment work that is taking into account how capable we think models are what their propensities are, whether we can track using safeguards.
The kinds of things that the models are doing. Do we think that these models pose large scale harms? You can expect to see much more of that in 2026. Maybe. Maybe now is a good time to. Say that we are hiring?
swyx: Yes.
Joel Becker: On my team we’re hiring for research engineers, research scientists, people from, startup backgrounds, from from ML backgrounds.
Of course, I’m originally from sort of economics or quantitative genomics backgrounds. So we are accepting pretty wide range of people who get stuff done. The [00:53:00] kind of stuff that you’ve seen in, in, in past meter work as well as a director of operations. I think on the meet jobs page, you can find out more.
swyx: Yeah. Everyone I know is hiring a director of operations including myself. And I feel like that’s, probably the one agent that everyone wants that we can have. Yeah, whenever people have a hiring pitch, I always try to push for, okay, the average candidate comes in, you reject them.
Why? What’s the thing you’re looking for?
Joel Becker: So there, there are lots of different shapes of people we can look for. So different stuff for different folks. One thing is good kind of basic research intuitions like checking your data. We don’t work on free training at meter, but if you are working on free training, you should look at the corpus to get some sense of what’s going into the models.
Even working on this uplift, RCT that was pretty important, really having a shape of these issues in your head. I think people who are communicating in writing with sort of a lot of transparency, not overstating their results. My hope is that your sense of me to work in the past is that it’s it’s trying to be levelheaded not to not to understate.
Not to overstate what the science says that’s important internally. It’s important. It’s important externally, and then I think productivity or something [00:54:00] that there are a lot of a lot of people with great talents who, who are not going to work quite as well in a scrapper environment, working on frontier science.
And and that’s the thing we do.
swyx: I just want to prime people for, what are the valuable skills in this new age. Because I think that the more people articulate what the positive directions are, what it’s hard to hire for, that’s what we guide our audience towards, improving themselves in.
I think that’s important.
Joel Becker: Oh yeah.
Alessio: Did you have a karaoke question or.
swyx: I don’t know. There’s know are you saying on podcast? I’ve never done it. I’ve been Can’t help falling in love with
Joel Becker: you.
swyx: What is this karaoke thing that you organiz This is like a music. You’re a new musician.
Joel Becker: A musician might be exaggerating it, but, I hit instruments and noises come out. So I’ve hosted a couple of these live band karaoke events that is like getting a group of friends together and people accompanied by, by bands singing karaoke to a, to an audience of, 5,000, 200 people.
It’s great fun. I think people should be doing more of this. I look forward to seeing you both at the next one.
swyx: Yeah, I will do that at one of your events. Yeah. It’s one of those things where it’s weird because I [00:55:00] used to be in a Capella a lot.
Joel Becker: Oh, wow.
swyx: And I just think it’s like a dying form.
Yeah. I just watched this video that was really good about. Like 20 times. 2010 wave of acapella from like Pitch Perfect. And Glee is a pitch. Perfect. Yeah. Yeah. To that’s what’s the, what’s that group? Panatonics. Panatonics, exactly. That’s where it died. And it’s, it is very interesting to, to see how it’s like dying as a art form and in general and like how new formats have taken over.
And I don’t know it’s weird for humans also because like now I’m also like let’s call it more interested in synthetic song generation or DJing, anything like that. That, that the human voice is actually more commoditized. Like it doesn’t really matter who sings it.
Joel Becker: I dunno. I feel like there’s a kind of transcendence to singing in person.
That’s the AI generator songs are not providing me.
swyx: That’s good. That’s good. Yeah. Yeah. I do think that like we humans always want that. Yeah. Yeah. But I’m not sure humans in. That your 3000 don’t want that. It’s one of those weird things. Thank you for coming on.
It’s it’s great to have you as a human in person here.
Joel Becker: Thank you so much having me as a human.[00:56:00]
swyx: Yeah. So someday, we’ll, we will interview AI version three.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3hOelF3TXpZME5qQXNJbkJ2YzNSZmFXUWlPakU0T1RFMU9UYzNOeXdpYVdGMElqb3hOemN5TWpFNU9UY3dMQ0psZUhBaU9qRTRNRE0zTlRVNU56QXNJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5IYzNmVHdZUEpXeGdad0dDR0FoaEt6bDBLMk42ZDFTN3RISEVUVWlCSDJBIiwicCI6MTg5MTU5Nzc3LCJzIjoxMDg0MDg5LCJmIjpmYWxzZSwidSI6MTc0MDM2NDYwLCJpYXQiOjE3NzIyMTk5NzAsImV4cCI6MjA4Nzc5NTk3MCwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.1vssHYqKO9gWGHgDNklLbqfp8c1NgB-lHpl-SLdRk-s?
