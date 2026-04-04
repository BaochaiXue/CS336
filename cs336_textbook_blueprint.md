# CS336 textbook blueprint

## Goal

Write a self-contained LaTeX textbook for CS undergraduates that fully covers the official Stanford CS336 Spring 2025 course arc and is designed to stay aligned with the Spring 2026 arc as it evolves. The book should follow the spirit of CS336's "from scratch" philosophy while being more detailed, more explicit about prerequisites, and more pedagogically structured.

## Audience

The primary audience is a CS undergraduate who:
- can program in Python,
- has some "AI tool use / vibe coding" experience,
- may have trained or fine-tuned small models,
- does **not** necessarily know NLP, linguistics, CUDA, or distributed systems deeply.

## Non-negotiable writing requirements

1. **Mathematically rigorous but readable**
   - Definitions, assumptions, notation, and derivations must be explicit.
   - Every major equation gets:
     - symbol table,
     - derivation or justification,
     - intuitive interpretation,
     - worked numerical or code-level example.

2. **Self-contained**
   - Do not assume prior NLP, linguistics, CUDA, or systems expertise.
   - Introduce needed prerequisites either inline or in prerequisite capsules.
   - The book must stand alone; students should not need to constantly consult another textbook.

3. **Course-aligned**
   - The narrative spine should follow the official CS336 lecture/assignment arc:
     - tokenization and basics,
     - PyTorch and resource accounting,
     - architectures and hyperparameters,
     - mixture of experts,
     - GPUs / kernels / Triton,
     - parallelism,
     - scaling laws,
     - inference,
     - evaluation,
     - data,
     - alignment and reasoning RL.

4. **Neuroscience-first analogies**
   - Most intuitive analogies and examples should come from neuroscience / brain science.
   - Every analogy box must contain three subsections:
     - **Where the analogy helps**
     - **Where the analogy breaks**
     - **What intuition the student should keep**
   - Never imply that LLMs and brains are literally the same mechanism.

5. **Primary-source grounded**
   - Use primary papers, official technical reports, official course materials, and official repos as the main factual sources.
   - Prefer direct paper citations over secondary summaries.

## Recommended repository structure (harness-oriented)

```text
AGENTS.md
ARCHITECTURE.md
README.md

docs/
  vision.md
  scope.md
  style_guide.md
  notation.md
  pedagogy.md
  neuroscience_analogy_policy.md
  course_coverage_matrix.md
  decision_log.md
  chapter_specs/
    00_overview.md
    01_entropy_tokenization.md
    ...
  exec_plans/
    active/
    completed/
  evals/
    chapter_rubric.md
    notation_consistency.md
    math_rigor.md
    pedagogy_checks.md
    cs336_coverage_checks.md

papers/
  manifest.csv
  manifest.json
  raw_archives/
  extracted/
  normalized/
  merged_tex/
  metadata/

book/
  textbook.tex
  frontmatter/
  parts/
  chapters/
  appendices/
  figures/
  tables/
  bibliography.bib

scripts/
  fetch_papers.py
  normalize_sources.py
  merge_tex.py
  build_book.sh
  lint_tex.py
  check_references.py
  check_notation.py
  check_cs336_coverage.py
```

## Project-management philosophy

Use a harness-engineering style:
- Keep `AGENTS.md` short and high-signal; it should be a **map**, not a giant manual.
- Treat `docs/` as the **system of record**.
- Keep structured execution plans and chapter-state artifacts so long-running work can resume across sessions.
- Separate planning, retrieval/normalization, drafting, and evaluation stages.
- Prefer explicit artifacts over hidden context.

## Book architecture

### Part 0 · Orientation and prerequisite capsules
0. How to use this book, notation, and the "from scratch" philosophy
1. Probability, entropy, cross-entropy, KL, MLE, perplexity
2. Linear algebra, matrix calculus, automatic differentiation refresher
3. PyTorch and tensor manipulation essentials
4. CUDA / GPU execution model essentials
5. Minimal linguistics and NLP background

### Part I · Language modeling foundations
6. The language modeling problem from Shannon to neural LMs
7. Tokenization: bytes, characters, subwords, BPE, unigram, byte-level models
8. From n-grams to neural language models to sequence models

### Part II · Transformer internals
9. Attention from seq2seq to Transformer
10. Transformer blocks from scratch
11. Norms, residual pathways, activations, and positional encodings
12. Hyperparameters, initialization, and optimization basics
13. Variants: sparse attention, long context, GQA, MoE, byte/patch models, Mamba-family extensions

### Part III · Systems and implementation
14. Resource accounting: FLOPs, memory, arithmetic intensity, MFU
15. GPUs, TPUs, memory hierarchy, occupancy, and performance models
16. Kernels, CUDA, Triton, fusion, tiling, and FlashAttention
17. Parallelism: data, tensor, pipeline, ZeRO/FSDP, checkpointing
18. Inference and serving: KV cache, batching, latency, throughput, memory tradeoffs

### Part IV · Scaling, evaluation, and recipes
19. Scaling laws: Kaplan, Chinchilla, compute-optimality, and caveats
20. Model recipes and open-model case studies: GPT-2/3, OPT, BLOOM, LLaMA, OLMo, DeepSeek
21. Evaluation: intrinsic metrics, downstream tasks, harnesses, benchmark design, contamination

### Part V · Data
22. Data sources, licensing, crawling, cleaning, transformation
23. Filtering, deduplication, mixing, rewriting, and SFT data construction

### Part VI · Alignment and reasoning
24. Instruction tuning and preference tuning
25. RLHF, PPO, DPO, GRPO, reasoning RL, and math-reasoning case studies
26. Safety alignment, reward hacking, specification gaps, and deployment caveats

### Appendices
A. Proof techniques and derivation details  
B. CUDA/Triton cookbook  
C. Linguistics quick reference  
D. Neuroscience analogy index  
E. Reproducibility, experiment hygiene, and debugging

## Course-coverage mapping

- Assignment 1 (Basics) maps primarily to Chapters 6-12.
- Assignment 2 (Systems) maps primarily to Chapters 14-17.
- Assignment 3 (Scaling) maps primarily to Chapters 19-20.
- Assignment 4 (Data) maps primarily to Chapters 22-23.
- Assignment 5 (Alignment and Reasoning RL) maps primarily to Chapters 24-26.

## Reading strategy

Use three tiers:

### Tier A: deeply integrated canonical papers
Use `cs336_core_readings.md`.

### Tier B: official-reference manifest
Use `cs336_paper_manifest.csv` / `.json`. This is the broad coverage layer drawn from the official CS336 lecture reference files for Spring 2025 and the current lecture repo.

### Tier C: rolling 2026 frontier appendix
For papers that are too new or too specialized for the main pedagogical spine, summarize them in boxed "2026 update cards" or appendix notes instead of letting them destabilize the core narrative.

## Chapter template

Every chapter should follow this shape:

1. Learning goals  
2. Big picture  
3. Formal setup and notation  
4. Main ideas  
5. Worked example  
6. Systems / implementation consequences  
7. Neuroscience analogy box
   - where it helps
   - where it breaks
   - keep-this-intuition
8. Common misconceptions  
9. Exercises
   - warmup
   - derivation
   - implementation
   - open-ended discussion
10. Further reading  

## Evaluation rubric for Codex-generated chapters

A chapter is not "done" unless:
- it compiles in LaTeX,
- notation is consistent with the global notation file,
- all nontrivial claims have citations,
- every major equation has explanatory prose,
- every analogy has both **similarity** and **difference** sections,
- the chapter is understandable by the target undergraduate reader,
- the chapter passes the CS336 coverage matrix checks.

## Paper-source normalization policy

For local paper sources:
1. Prefer public LaTeX / arXiv source when available.
2. Store downloaded archives in `papers/raw_archives/`.
3. Extract each archive into a temporary folder.
4. After successful extraction, delete the original archive.
5. Rename the extracted folder to a filesystem-safe paper title.
6. If the paper uses multiple TeX files, create `merged_paper.tex` by recursively resolving `\input{}` and `\include{}`.
7. In `merged_paper.tex`, strip comments and collapse extra blank lines.
8. Record failures in `papers/metadata/source_failures.json` rather than silently skipping them.

## Immediate implementation order

1. Build repository scaffold and docs system of record.
2. Create the official-course coverage matrix.
3. Build / validate the paper manifest.
4. Download and normalize paper sources.
5. Draft Part 0 and Part I first.
6. Draft systems and scaling parts next.
7. Draft data and alignment last, while maintaining a stable notation and bibliography.
8. Run evaluator passes after every chapter batch.
