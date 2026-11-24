---
title: State of Finance
type: state-of
domains: [finance]
tags: []
as_of: 2026-11-23
sources: [perplexity-computer-plaid, hebbia-homepage, legacy-ai-tools-roadmap-xlsx, stripe-agent-native-commerce-fraud-2026-04-29, finance-agent-workflows-2026-05-06, chatgpt-personal-finance-2026-05, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, mistral-document-ai, landingai-agentic-document-extraction, latent-space-crossing-the-threshold-2026-10-14, chatgpt-for-accounting-page, openai-chatgpt-financial-services-2026-09-10]
---

# State of Finance

Current state of AI applied to personal and institutional finance — budgeting, investment tracking, financial data analysis, and fintech integrations.

## Subcategories

### Finance AI

AI products specialized for financial analysis, modeling, and document-heavy finance workflows.

- [Hebbia](../tools/hebbia.md) — document-heavy knowledge-work platform with especially strong practical relevance in finance analysis and modeling workflows *(as of 2026-04-22)*
- **Anthropic finance agent templates** — secondary newsletter coverage describes templates for pitch generation, valuation review, KYC, and month-end close with market-data integrations; pending primary Anthropic verification *(as of 2026-05-06)*
- **Bridgewater / Thinking Machines expert-judgment model** — expert-labeled financial information-filtering tasks fine-tuned on Qwen3-235B; trained model reached 84.7% average accuracy and 13.8x lower inference cost per task than frontier baselines in the public Thinking Machines report *(as of 2026-07-02)*
- **ChatGPT for Financial Services** — OpenAI; ChatGPT Work edition for banking and equity research: OpenAI-hosted data (Daloopa, PitchBook, LSEG News, Crunchbase) with figure-level citations, tuned finance connectors, firm templates, information-barrier workspaces; OpenAI's Joseph Kim predicts agent-run idea generation and trading in 2027 *(as of 2026-10-14)*
- **ChatGPT for Accounting** — OpenAI; an Accounting plugin for the ChatGPT desktop app adds guidance for invoice processing, reconciliation and reporting across connected apps (QuickBooks, Xero, BILL, FreshBooks, NetSuite and others), with computer use for apps without a plugin and monthly checks saved as reusable skills; entries are drafted for human approval *(as of 2026-11-23)*
- **Claude for Financial Advisors** — Anthropic; announced September 2026; advisors connect their own systems to Claude plus a set of workflow skills; Anthropic pairs it with an identity, approval, and regression "trust layer" for financial agents *(as of 2026-10-14)*

### Personal finance AI

Consumer-facing AI tools that connect to financial accounts and assist with budgeting, tracking, and everyday money workflows.

- **ChatGPT @Finances** — OpenAI; activated with `@Finances` in any ChatGPT conversation; connects to 12,000+ financial providers; gives personalized money advice grounded in real income and spending data; GPT-5.5 Thinking 79/100 on complex finance tasks; US Pro preview only *(as of 2026-05-18)*
- [Perplexity Computer](../tools/perplexity-computer.md) — connects to 12,000+ financial institutions via Plaid, letting users build custom budgeting/tracking tools inside an AI chat interface; also reportedly moving toward a professional-finance positioning combining licensed finance data with packaged workflows (newsletter coverage, pending primary verification) *(as of 2026-05-06)*

### Document intelligence

AI products specialized for extracting, structuring, querying, or reasoning over documents, PDFs, forms, and tables — as distinct from general-purpose finance assistants.

- [Mistral Document AI](../tools/mistral-document-ai.md) — Mistral; document-intelligence product for extracting and structuring information from PDFs, forms, and enterprise document flows *(as of 2026-04-22)*
- [LandingAI Agentic Document Extraction](../tools/landingai-agentic-document-extraction.md) — LandingAI; agentic extraction for visually complex documents, emphasizing preserved structural context across tables, forms, and segmented layouts *(as of 2026-04-22)*

### Agent-native commerce and fraud

AI is shifting the fraud attack surface and enabling agents as autonomous economic participants:

- **Stolen compute as the new stolen card.** Stripe's view (via Every newsletter): fraud is moving from payment credentials toward stolen API keys, tokens, credits, free-trial abuse, and unpaid compute bills. "Compute is the new cash."
- **Agents as buyers** — wallets, spend growth and merchant responses are tracked on [Agentic commerce](../trends/agentic-commerce.md).
- **Merchant implications.** Free-trial farming by automated agents, credit-consumption abuse, and unauthorized compute use are the emerging fraud patterns at the intersection of AI and commerce.

## Recent changes

- [2026-11-24] Agent-buyer bullets (agents as purchasers, Stripe Link Agent Wallet spend) moved to the new [Agentic commerce](../trends/agentic-commerce.md) trend page; this section keeps the fraud bullets and a pointer.
- [2026-11-23] OpenAI's ChatGPT for Accounting page: Accounting plugin plus app connectors and computer use for invoicing, reconciliation and month-end reporting, with reusable skills and human approval of every entry; added to Finance AI.
- [2026-10-14] AIE NYC finance keynotes: OpenAI (ChatGPT for Financial Services), Anthropic (Claude for Financial Advisors), Two Sigma, and Bloomberg converge on placing controls (classifier routing, propose-not-act, deterministic checks outside the model) rather than stacking approvals; guidance on [Agent autonomy and governance](../training/agent-autonomy-and-governance.md).
- [2026-09-10] ChatGPT for Financial Services launched: OpenAI-hosted premium data (Daloopa, PitchBook, LSEG News, Crunchbase) with figure-level citations, tuned finance MCP connectors plus 50+ others, admin-published Office templates and information-barrier workspaces; shared sign-in to existing data subscriptions in progress.
- [2026-07-02] Bridgewater/Thinking Machines case study: expert prompts plus domain fine-tuning beat larger frontier models on subjective finance information-filtering tasks at lower cost.
- [2026-05-18] ChatGPT @Finances launched: 12,000+ financial providers; personalized money advice grounded in real spending data; GPT-5.5 Thinking 79/100, Pro 82.5/100; US Pro preview; added to Personal finance AI
- [2026-05-06] Added packaged finance-agent workflow signal: Anthropic finance templates and Perplexity Computer professional-finance positioning are secondary-source entries pending primary verification.
- [2026-04-29] Added agent-native commerce and compute-fraud framing from Stripe's perspective (via Every newsletter); stolen compute, agent-as-purchaser, free-trial farming
- [2026-04-22] Added `Finance AI` subcategory with [Hebbia](../tools/hebbia.md) as the first dedicated finance-workflow product in the wiki
- [2026-04-10] Page seeded from Perplexity Computer's Plaid integration signal (Superhuman AI newsletter)

## Sources

- [Stripe agent-native commerce and compute fraud](../sources/newsletters/stripe-agent-native-commerce-fraud-2026-04-29.md)
- [Finance agent workflow packaging - May 2026](../sources/newsletters/finance-agent-workflows-2026-05-06.md)
- [Thinking Machines - Learning to Replicate Expert Judgment in Financial Tasks](../sources/articles/thinking-machines-financial-expert-judgment-2026-07-02.md)
- [Latent Space — Crossing the Threshold: autonomy and safety in financial agents](../sources/newsletters/latent-space-crossing-the-threshold-2026-10-14.md)
- [OpenAI — ChatGPT for Accounting solutions page](../sources/articles/chatgpt-for-accounting-page.md)
- [OpenAI — Introducing ChatGPT for Financial Services](../sources/articles/openai-chatgpt-financial-services-2026-09-10.md)
