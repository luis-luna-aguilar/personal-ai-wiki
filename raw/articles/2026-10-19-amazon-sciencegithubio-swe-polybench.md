---
title: SWE-PolyBench
type: source
source_type: article
url: https://amazon-science.github.io/SWE-PolyBench/#full
fetched: 2026-10-19
---

# SWE-PolyBench

SWE-PolyBench
Multi-Language Evaluation of Coding Agents
🚀 We just released SWE-PolyBench verified! 🚀
 Preprint 
 Code 
 Datasets 
 Blog 
 Submit 
About

PolyBench is a multi-language benchmark designed to evaluate AI coding assistants across diverse programming tasks and languages. It contains 2110 instances from 21 repositories, covering Java, JavaScript, TypeScript, and Python. PolyBench includes a variety of task types including bug fixes, feature additions, and code refactoring, reflecting real-world software engineering challenges.

Citation
@misc{rashid2025swepolybenchmultilanguagebenchmarkrepository,
  title={SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents}, 
  author={Muhammad Shihab Rashid and Christian Bock and Yuan Zhuang and Alexander Buchholz and Tim Esler and Simon Valentin and Luca Franceschi and Martin Wistuba and Prabhu Teja Sivaprasad and Woo Jung Kim and Anoop Deoras and Giovanni Zappella and Laurent Callot},
  year={2025},
  eprint={2504.08703},
  archivePrefix={arXiv},
  primaryClass={cs.SE},
  url={https://arxiv.org/abs/2504.08703}, 
  }
}
Leaderboard
Full
PB500
Verified
Resolve Rate by Language
Resolve Rate by Complexity
File Retrieval Metrics
Node Retrieval Metrics
Model
	
Overall
	
Java
	
Python
	
JavaScript
	
TypeScript
	
Org
	
Date
	
Logs
	
Trajs
	
Site



🥇 Amazon Q Developer Agent (v20250402)

	

22.61

	

26.67

	

31.16

	

20.94

	

21.67

	

	

2025-04-11

	

✗

	

✗

	

✗




🥈 Aider-PB (Sonnet 3.5)

	

14.08

	

15.76

	

24.12

	

12.59

	

13.03

	

	

2025-04-02

	

✗

	

✗

	

✗




🥉 Aider-PB (Deepseek R1)

	

11.52

	

12.12

	

18.09

	

10.13

	

11.52

	

	

2025-04-02

	

✗

	

✗

	

✗




SWE-agent-PB (Sonnet 3.5)

	

10.19

	

16.36

	

24.12

	

6.49

	

10.15

	

	

2025-04-08

	

✗

	

✗

	

✗




Aider-PB (Haiku)

	

9.86

	

11.52

	

18.09

	

8.06

	

9.74

	

	

2025-04-02

	

✗

	

✗

	

✗




Agentless-PB (Sonnet 3.5)

	

7.82

	

10.91

	

20.1

	

7.18

	

4.66

	

	

2025-04-02

	

✗

	

✗

	

✗




Aider-PB (Llama3.3 70B)

	

6.02

	

9.09

	

11.06

	

4.23

	

6.45

	

	

2025-04-02

	

✗

	

✗

	

✗




Aider-PB (Mistral-Large)

	

5.88

	

6.67

	

7.04

	

4.82

	

6.86

	

	

2025-04-02

	

✗

	

✗

	

✗




Aider-PB (Deepseek-R1-Distill Llama 70B)

	

5.31

	

5.45

	

12.56

	

3.54

	

5.76

	

	

2025-04-02

	

✗

	

✗

	

✗




iSWE-Agent

	

N/A

	

33.33

	

N/A

	

N/A

	

N/A

	

	

2026-02-06

	

🔗

	

🔗

	

🔗

Complexity Classes: The complexity metrics reflect different types of code modifications:

Single: Refers to tasks where only a single node of the specified type was modified.
Func. Only: Only function nodes were modified, with no changes to class structures.
Class Only: Only class nodes were modified, with no changes to function structures.
None: No class or function nodes were modified. This typically involves changes to configuration files (e.g., .yaml or .json) or other files not parsed for class/function structures.
Mixed: Both class and function nodes were modified in the same task.

Acknowledgements: This leaderboard is a modified version based on the SWE-bench leaderboard, and we are using this template with the explicit permission of the SWE-bench team
