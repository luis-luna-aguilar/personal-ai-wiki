---
title: Introducing Gemini 4 Hydrogen
type: source
source_type: article
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
fetched: 2026-11-24
---

# Introducing Gemini 4 Hydrogen

Skip to main content
Innovation & AI
Products & platforms
Company news
Feed
Newsletter
Home
Innovation & AI
Models & research
Gemini Models
Introducing Gemini 4 Hydrogen

Nov 12, 2026

15 min read

Hydrogen brings cutting-edge intelligence to everyone.

Koray Kavukcuoglu

SVP, Google DeepMind and Chief AI Architect, Google

Share
Listen to article
17:50 minutes
In this article
Gemini 4 Hydrogen is available
Unlocking efficiencies in multi-model workloads
Scaling developer and enterprise workflows
Adaptable speed and intelligence across thinking levels
Fast, everyday help in the Gemini app and Search
Designed for safe, dependable execution for scale
Available to everyone today

Last updated November 16, 2026

Today, we’re introducing Gemini 4 Hydrogen, bringing cutting-edge intelligence to everyone — with speed and efficiency for everyday coding and agentic workflows.

While our frontier models, Gemini 4 Carbon and Gemini 4 Argon, excel at deep, long-horizon reasoning on your hardest problems, Hydrogen is built for rapid execution across diverse agentic workflows. With Hydrogen, we’re also bringing Gemini 4 to everyone — for all tiers of Google AI Studio, the Gemini API, Gemini for business, the Gemini app, Google Search, and paid Google AI Pro and Ultra subscribers in Google Antigravity.

Hydrogen surpasses Argon on the Artificial Analysis Intelligence Index at its default high thinking level (51 vs. 50, and reaching 54 at its highest xhigh thinking setting), while often completing tasks faster than models in its class. Gemini 4 Hydrogen is priced flat across its entire 1 million-token context window at $1.50 per million input tokens and $7.50 per million output tokens.

Unlocking efficiencies in multi-model workloads

In real-world software development, while teams rely on frontier models like Carbon and Argon for deep architectural judgment when designing systems or untangling subtle bugs, they still need a fast, disciplined execution model for writing code, running tests, and verifying changes. Hydrogen is built to stand on its own as a model for everyday work — or to pair with Carbon and Argon as the high-efficiency execution engine in multi-model workflows.

To help make this multi-model collaboration automatic, we’re introducing Orchestrator in Google Antigravity. Rather than using a single model from start to finish, Orchestrator dynamically switches between models like Carbon and Hydrogen within the same session. On Terminal-Bench 4.0, Orchestrator reached near-Carbon task success rates while, on average, consuming 24% less quota and completing 19% faster. For workflows that require parallel agents, Carbon can act as the coordinator while Hydrogen can power worker and verifier agents to build and test changes simultaneously across isolated workspaces — helping teams ship complex projects faster without driving up token costs.

Scaling developer and enterprise workflows

Beyond multi-model workflows, Hydrogen is a major standalone upgrade for teams migrating from Gemini 3.8 Flash. It delivers significant leaps in both speed and intelligence — finishing tasks 2.5 times faster at its high default setting while more than tripling Terminal-Bench 4.1 scores (57% vs. 18.2%), cutting fabricated claims by more than 5x, and adapting cleanly when a tool call fails or a search returns empty. It also matches or outperforms competing models in its class across core developer and enterprise workflows:

Iterative repository coding and debugging: Hydrogen handles issue resolution, debugging, rapid iteration, and codebase Q&A with focused, surgical edits — delivering cleaner, production-ready code without rewriting unrelated files. It outperforms similar-tier models on SWE-sweep where it has to discover and repair bugs without breaking existing code. To explore large repositories efficiently, the model excels at natively batching file-read and search calls in parallel rather than inspecting files one by one; in early testing across complex graphs, SQL, and data-heavy enterprise workflows, our partners have seen Hydrogen run 2x to 2.8x faster while reducing token usage by 12% to 23%, compared to 3.8 Flash.
Open-ended agentic execution: On multi-step tasks like deep research, data analysis, and broad codebase navigation, Hydrogen ranks #5 on Agent Arena, arena.ai’s live benchmark. For deep domain reasoning and analysis, it leads its class on HLE-Diamond (58.8%), ranks #1 overall on Vals Tax Agent Bench (52.3%), ties for #1 on the Vals Legal Research Bench (55.8%), and leads its class on AutomationBench-AA.
The new Gemini 4 Hydrogen model is thorough and skeptical in a way I haven't seen from past Gemini models. It is really pleasant and surprising! We have been working on a thorny problem for 10 days with frontier models from competitors and the Hydrogen model was able to catch 2 issues with our approach and proposed a fix. Really amazing and efficient.
By Andrew Carr
Chief Scientist and Co-Founder, Cartwheel
Building with Hydrogen made it very easy to build new tools — it combines the performance of a frontier model with speed that makes iteration on tools feel incredibly lightweight.
By Tris Warkentin
Founding Member of Technical Staff, Discovery Loop
Gemini 4 Hydrogen was the most accurate model on the toxicology and safety section of our Antibody Development benchmark, passing 67% of attempts against 37% for the best non-Gemini model, and the fastest Gemini model at about 13 minutes per task. It reasoned like a cautious safety reviewer, weighing the whole clinical picture rather than single data points and choosing conservative assumptions where patient risk was high.
By Joshua Badshah and Dillon Flood
Biologics Development, LatchBio
Across our reasoning and creative evaluation suite, Gemini 4 Hydrogen matched accuracy with 100% format compliance while slashing end-to-end latency by 28% and cutting total token usage by 23%. From solving complex graph and SQL problems up to 2.8× faster to generating rule-compliant voice ad scripts for StanShop, Hydrogen gives our streaming agents the speed, step-by-step verification, and efficiency we need at scale.
By Rahul Singh
Co-Founder & CTO, STAN
Multimodal knowledge work: Hydrogen pairs native 1 million-token input with up to 1 million output tokens to synthesize dense PDFs, spreadsheets, charts, audio, and recorded video into polished, cited reports and structured deliverables. It outperforms other models on the new Multimodal Knowledge Agent (MKA) benchmark (53.4%) for end-to-end agentic knowledge work over complex visual files, and on Agents’ Last Exam v1.1 (71.6%) for end-to-end professional workflows.
Web development: On tasks where speed matters to developers, like live UI prototyping, design-to-code iteration, and interactive app building, Hydrogen generates more functional, feature-complete layouts in fewer prompts.
Our goal, at Astrocade, is to let anyone’s creativity grow into games that people enjoy playing and sharing. Serving our creators the best frontier models is central to that experience. In early testing, Gemini 4 Hydrogen blew past our expectations in game generation performance. We’re optimistic that Gemini 4 Hydrogen will be key in helping creators take their games to the next level.
By Ali Sadeghian
Co-Founder, Astrocade
In Box’s evaluations, Gemini 4 Hydrogen’s accuracy significantly improved when compared to Gemini 3.8 Flash, while running about twice as fast and using 12% fewer tokens. We saw the strongest gains in data-heavy workflows, where accurately reading tables and performing complex calculations is essential to producing reliable reports. These results demonstrate meaningful progress in the model’s ability to handle complex enterprise content with greater accuracy and efficiency.
By Yashodha Bhavnani
VP of AI Products, Box
We evaluated Gemini 4 Hydrogen over 276 runs. It swept every single design brief, ran 1.8× faster with 30% cleaner code, and eliminated the text clipping and hallucinated claims we saw in previous models.
By Dominique Yahyavi
Co-Founder & CEO, Pixelcut
We tested Gemini 4 Hydrogen across demanding video-comprehension workflows — from tracking characters and physical action to breaking down complex cinematography and directing downstream video models. Hydrogen consistently nailed major scene progressions, camera angles, and visual aesthetics, while anchoring on real visual evidence rather than hallucinating details. It's proving to be an exceptionally capable multimodal foundation for end-to-end cinematic generation.
By Harshit Yadav
Founder & CEO, Zingroll
00:00

Using Hydrogen for on-the-fly 3D coding, Geminisland lets anyone add to a shared voxel island from a single prompt to generate custom structures live on the map that players can walk around and explore in first person. Try the live app.

00:00

Paired with our new Gemini front end design skill in Google Antigravity, Hydrogen built an e-commerce storefront in one shot complete with a WebGL2 topographic shader, pinned four-stage scrollytelling, a thermal split-slider, a 3D wireframe spec card, and a live finish configurator. Try the live app and the Gemini front end design skill.

00:00

In Google Antigravity, Hydrogen turned Google Sheets into an animated pixel canvas by shrinking thousands of cells combining Python, native =LET(...) formulas, and conditional formatting to paint and animate full-motion scenes directly inside a live spreadsheet.

00:00

Starting from a YouTube keynote video and a design template in Google Antigravity, Hydrogen generated a multi-slide presentation directly in Google Slides, then ran an autonomous audit-and-fix loop to catch overlapping text and clean up every slide layout.

00:00

With Gemini in Google Sheets, Hydrogen can help teams rapidly turn financial data into interactive models that dynamically adjust based on various forecasting scenarios, generating outputs over 30% faster than previous models in Sheets canvas.

Adaptable speed and intelligence across four thinking levels

We built Gemini 4 Hydrogen for real-world usability. Hydrogen’s four thinking levels — low, medium, high (default), and a new xhigh tier — offer a wide range of options across quality, latency, and cost, scaling in a smooth, predictable progression so you only wait and pay for the reasoning depth a task requires. Across thinking levels, Hydrogen matches or outperforms some of the competing models in its class while often finishing tasks faster and using fewer output tokens.

Fast, everyday help in the Gemini app and Search

For consumers, Gemini 4 Hydrogen makes it easier to get things done, staying on track and following instructions more closely across multi-turn conversations.

In the Gemini app, Hydrogen makes your everyday assistant even more helpful — it’s better at following your guidance, calling the right tools, and getting you to a reliable output with less back-and-forth.

Ready-to-go writing, research, and everyday work: Hydrogen sticks closely to your tone, format, and specific rules, so email drafts, study guides, rewrites, and documents come back ready to use on the first try. When you are comparing products or synthesizing dense material, it pulls together clear tables and visual breakdowns without dropping key details.

Connects the dots and gets more tasks done: Hydrogen breaks down your goal step-by-step, pulling relevant context from your uploads, Google apps like Gmail and Google Drive, and Connected Apps like Airtable and Dropbox. When you start a task in Gemini, it also more frequently calls the right tools and skills for the job, helping save you time as you check things off your to-do list.

Everyday prototyping and iteration: For exploring and testing ideas, Hydrogen generates clean, working layouts in fewer prompts, making it easy to prototype and refine interactive projects quickly, like synthesizing real-time global lightning strike data into an interactive 3D globe.
00:00

Moving fast from idea to working prototype, Hydrogen built an interactive 3D globe and Web Audio music engine driven by real-time lightning strikes and mapped every bolt around the world into visual ripples and live ambient music.

00:00

When tasked to create a WebGL2 water and glass visualizer, Hydrogen built it from pure math and SDF textures — simulating real-time light refraction, reflection, dispersion, and absorption.

00:00

Using a custom skill for video assembly and adhering to a creative brief, Gemini 4 Hydrogen created an archival sizzle reel about the element ‘Hydrogen’, sourcing public-domain footage and cutting it into one continuous edit with clean narration.

Hydrogen is significantly upgrading Search, delivering more helpful, intuitive responses for all users globally.

Better understands your true intent: With Hydrogen, you can ask your question in your natural flow of thought — even if you have multiple parts to your query, hard-to-understand typos, or highly specific requests — and Search will intelligently comprehend what you’re looking for.
More visual responses: You’ll get highly adaptive, visual, and easy-to-scan responses that are uniquely relevant to your needs, at the speed you expect from Search.
Wider range of relevant links: With Hydrogen’s advanced reasoning, we’re also upgrading our query fan-out technique in Search, connecting you to a broader range of helpful links than before, helping you find sites you previously might not have discovered.
Designed for safe, dependable execution at scale

Gemini 4 Hydrogen brings improvements from our latest Gemini 4 safety and security stack to our broadest audience yet, combining built-in training with real-time surface safeguards to help mitigate both misalignment and misuse. Beyond foundational protections, we focused on two areas that matter most for a faster model that’s for everyday work:

Safe, aligned, and secure agentic workflows: While 3.8 Flash has strong alignment and safeguards, Hydrogen is a leap ahead. It reduces overreach in agentic tasks by up to 81% and under-service by up to 79%, and cuts misaligned actions and task shortcutting across tool-use and coding evaluations by 12x. When faced with impossible or blocked tasks, it is up to 2x less likely to bypass permission boundaries and achieves a 94% honesty rate on our internal agent honesty evaluation.

Building on our commitment to reasoning transparency, Hydrogen also preserves 99.9% chain-of-thought legibility with zero deceptive reasoning edits across more than 200,000 audited turns. Against indirect prompt injection attacks, Hydrogen is more than 2.3x more resilient on the Gray Swan IPI benchmark, while significantly improving robustness across tool use, computer use, and coding agents.


Helpful, reliable everyday interactions: Across our product surfaces, we tuned Hydrogen to make everyday conversations more reliable and safe. Our updated safeguards are also much more precise at distinguishing between real biosecurity risks and legitimate medical or scientific questions — keeping false refusals on HealthBench Pro under 0.4%.

For more details see the Gemini 4 Hydrogen model card and the Safety and Security Report.

Gemini 4 Hydrogen, available to everyone today

Starting today, Hydrogen is rolling out globally across our developer, enterprise, and consumer surfaces:

For developers: Build with the Gemini API in AI Studio and Android Studio, try it in AI Studio and if you’re a paid Google AI Pro or Ultra subscriber, you can try it in Google Antigravity.
For enterprises: Deploy it in Gemini for business via the API or model drop down, Google Antigravity, and in Gemini in Google Sheets for eligible business subscriptions.
For everyone: Start using it in the Gemini app model drop down 
1
 and in Google Search for all users, and in Gemini in Google Sheets starting with Google AI Pro and Ultra subscribers.
Posted in:
Gemini models

More Information

About the Author
Koray Kavukcuoglu
SVP, Google DeepMind and Chief AI Architect, Google

Koray is one of the world's foremost experts in artificial intelligence. As the SVP of Google DeepMind, he leads the development of Google DeepMind’s state-of-the art generative AI models and their integration into Google’s products at scale. Prior to his current role, he was VP of Research at Google DeepMind, where he founded the deep learning team and his team pioneered major research breakthroughs such as DQN (Deep Q-Network) and WaveNet.

Read more from Koray Kavukcuoglu
Related stories
Gemini models
See what 6 builders are making with Gemini 4 Hydrogen
By Molly McHugh-Johnson
Gemini models
Introducing Gemini 4 Neon
By Koray Kavukcuoglu
Google DeepMind
Genie 4 is now available
By Diego Rivas & Pavan Kumar
Search
Google Search gets a major upgrade with Gemini 4 Hydrogen
By Robby Stein
Developer tools
Gemini 4 Hydrogen: everyday coding and agentic workflows for developers
Gemini models
Introducing the Multimodal Knowledge Agent benchmark
By Rohan Doshi & Ben Caine
Get the latest news from Google in your inbox

Sign up for our newsletters with product updates, event information, special offers, and more.

Subscribe

Your information will be used in accordance with Google's privacy policy. You may opt out at any time.

Privacy
Terms
Help
More of Google
Google Products
About the Blog
Global (English)
Africa (English)
Australia (English)
Brasil (Português)
Canada (English)
Canada (Français)
Česko (Čeština)
Deutschland (Deutsch)
España (Español)
France (Français)
Greece (Ελληνικά)
India (English)
Indonesia (Bahasa Indonesia)
Ireland (English)
Italia (Italiano)
日本 (日本語)
대한민국 (한국어)
Latinoamérica (Español)
Malaysia (English)
الشرق الأوسط وشمال أفريقيا (اللغة العربية)
MENA (English)
Nederlands (Nederland)
New Zealand (English)
Polska (Polski)
Portugal (Português)
România (Română)
Sverige (Svenska)
ประเทศไทย (ไทย)
Türkiye (Türkçe)
台灣 (中文)
