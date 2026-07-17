---
title: "🔬ESMFold2: The Bitter Lesson is Coming for Proteins - Alex Rives, BioHub"
type: newsletter
sender: "Latent.Space <swyx@substack.com>"
received: 2026-05-27
gmail_id: 19e6a8d2e6e01513
---

# 🔬ESMFold2: The Bitter Lesson is Coming for Proteins - Alex Rives, BioHub

**From:** Latent.Space <swyx@substack.com>
**Date:** 2026-05-27

View this post on the web at https://www.latent.space/p/esmfold2

Editor’s note: In our first BioHub pod with Priscilla and Mark [ https://substack.com/redirect/0f90a71e-e3bf-4d0f-9c79-609108be6f20?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] they discussed their acquisition of EvoScale [ https://substack.com/redirect/e8eb6405-5c7f-4464-8898-e47ff45dbb7a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], led by Alex Rives [ https://substack.com/redirect/74719713-0dd2-4cdd-9cc2-1af0bb41c3f6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], who is now Head of Science at BioHub. With ESM-1 they trained language models on millions of protein sequences drawn from across life, with a simple “next token” objective: predict the amino acids that have been randomly masked out, based on the context of the rest of the sequence. But they soon found that these models also learned biological structure and function, including properties the model had never been explicitly shown AND that this ability scales predictably with compute, leading to ESM2 and ESM3 [ https://substack.com/redirect/3bcbb8fd-c800-402b-9495-687c08074800?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Today, Alex announced [ https://substack.com/redirect/b1940670-95cc-45e9-84a5-6e556065dfbd?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] ESMFold 2, an open scientific engine to power prediction, design, and discovery across protein biology.
Building on Cryo-EM data (discussed in the CZI pod), ESMFold2 reports state of the art performance on protein interactions, especially antibodies, a critical modality for therapeutics, and evidence that inference time scaling is also working across five targets in cancer and immunology.
In a nod to that other famous AI x protein folding project, they are also releasing an atlas of 6.8 billion proteins, and 1.1 billion predicted structures, which you can play around with on their website [ https://substack.com/redirect/77ff73a6-583a-4211-9475-d4c91a377dc6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. We are honored to work with them for this huge release!
One of the refrains we’ve heard on the Science pod has been that protein folding, materials design, cellular biology, etc. are very different problems from Language Modeling. They definitely are. Yet Alex Rives and the ESM team at BioHub just released a preprint and model [ https://substack.com/redirect/9ef0fc1d-4512-4af4-9f3a-aaa0993e9ade?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], demonstrating that vanilla BERT-like transformer models trained on sufficiently large and diverse data sets can beat specialized models like AlphaFold3 on some of the hardest protein-related problems. 
Andrew White had a great segment [ https://substack.com/redirect/871379b8-f18b-4b03-8403-7ca446ecd848?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] in our first LS-Science episode that explained how mind blowing AlphaFold2 was when it was released in 2020: it suddenly solved problems on a GPU on your desktop that DESRes [ https://substack.com/redirect/ecff5237-87b5-47ec-b420-11ed154eef67?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] had built custom-ASIC supercomputer clusters to solve. John Jumper and Demmis Hassabis received the Nobel Prize [ https://substack.com/redirect/5df22c1c-e7c2-4e35-8c5f-23008ae88520?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] in Chemistry for this work.
AlphaFold2 took advantage of an very clever observation: if multiple species co-evolve pairs of mutations, this implies that the mutations correspond to parts of the protein that are close in 3d space. This is usually shorthanded as MSAs (multi-sequence alignments), and is the key insight which makes AlphaFold2 so effective.
Like other inductive biases, however, it hurts generalization.
Scale-pilled before it was cool
If you take a look at the timeline for scaling laws for LLMs and release of structure prediction models, the ESM team notably doubled down on their MSAs-be-damned approach after AlphaFold2 released. This obviously requires a great deal of belief in the scale hypothesis.
Why the conviction?
ESM developed at a time when many of the scaling laws and the “Bitter Lesson” were proving increasingly correct. AlphaFold2’s wild success must have been both exciting and bitterly disappointing.  But using MSAs mean that the model is is dependent on training data that contains MSAs in order to be accurate in a given domain.  For things like antibodies that don’t have MSAs to train on, AlphaFold tends to do poorly.
ESM takes a different approach: learn the relationship between different proteins by unsupervised training on as much diversity as you can find (sound familiar?) and then correlate that back to structures know from the Protein Data Bank (PDB) and other sources. 
In other words, a World Model.
World Model for proteins
“World Model” is a hype term that I define like this:
Use unsupervised training to learn abstract patterns from the data:
The abstraction should be semantic - novel constructions represent things that obey the rules of the real world
The abstraction should be compositional - recombining different patterns leads to novel and often valid constructions
The abstraction should support generalization - it predicts things in the real world it wasn’t trained on 
Once you have a world model, you can attach “heads” to it for downstream tasks: predict properties of a protein, decompose its functional features, or search the representation for proteins that meet design criteria. The two big models BioHub just released under MIT license map directly onto this:
World model → ESMC (a model trained on 2.8 billion sequences)
Structure-prediction head → ESMFold2
One of the interesting ways the world model can “predict things” is to generate proteins sequences and then measure the predicted properties, such as binding affinity, in the lab.  Alex talks in the episode about validating some of the harder molecules they predicted in the wet-lab. Very cool!
Another way is to use mech-interp techniques such as Sparse Auto Encoders [ https://substack.com/redirect/ed651a09-2eec-49c0-8006-832749b66888?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] (SAEs) to extract semantic features from your model, and then find novel features that predict unknown biology.  I won’t spoil this part for you: it was one of the highlights of the episode for me!
A cell is a computer
We have all heard that genes are like computer programs, but usually the analogy fizzles after that. Of course genes are transcribed into RNA and RNA is translated into proteins, so genes are programs for building proteins, but that carries the analogy only to “binary digits are programs.”  
Here’s a better analogy: you can think of the cell nucleus as a storage device / storage controller, the ribosome as a JIT-compiler and runtime, and the semantic features that we learn from our world model via SAEs as functions, proteins as processes that interact together in workflows (signalling pathways) to produce behaviors and outputs (phenotypes). 
Like functions, the SAE features have a hierarchical composition from local, secondary and tertiary structures (mimicing protein structure), but also motifs that are conceptual, such as membrane integrations, disordered regions and disulfide bonds. As we learn to compose these features we into novel protein designs, we move further towards programmable biology. 
Alex goes into much more detail about this in the episode, as well as:
Principles for new data collection
BioHub’s vision
Modeling the cell
Enjoy!
Full Video podcast
please like and subscribe!
X: https://x.com/alexrives [ https://substack.com/redirect/36ad2ae9-ac3a-4088-8cce-a6035359cba8?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]
LinkedIn:

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakU1T1RRNE56Z3pOaXdpYVdGMElqb3hOemM1T1RBME1EazFMQ0psZUhBaU9qRTRNVEUwTkRBd09UVXNJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS4wUGdoLUtoZTRYRlIzWjczalRaVzRpZTFXeDBXOFdGeUlGRlk1MXZUY2xRIiwicCI6MTk5NDg3ODM2LCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc3OTkwNDA5NSwiZXhwIjoyMDk1NDgwMDk1LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.ncilCzAtqPFiwnwhnuu4UEwnkRDN9j9UXd6MJS8y7jE?
