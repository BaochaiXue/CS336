# Pedagogy

## Chapter Template

Every chapter must follow this structure:

### 1. Learning Goals
- 3–5 specific, measurable learning objectives
- Written as "After reading this chapter, you will be able to..."
- Cover both conceptual understanding and practical skills

### 2. Big Picture
- 1–2 pages situating this chapter in the overall arc
- Why does this topic matter? What problem does it solve?
- Preview of key ideas (no formal notation yet)
- Connection to previous and upcoming chapters

### 3. Formal Setup and Notation
- Define all new notation needed for this chapter
- Reference `docs/notation.md` for consistency
- State assumptions explicitly
- Provide a "notation recap" box if the chapter draws on many previous symbols

### 4. Main Ideas
- The core technical content
- Each major idea gets its own section
- Build incrementally: simpler cases first, then generalize
- Every equation gets the full treatment: intro → equation → symbol table → interpretation

### 5. Worked Example
- At least one complete, non-trivial worked example per chapter
- Show intermediate steps (do not skip algebra)
- Use realistic numbers (not just $n=2$ toy cases)
- Include a "sanity check" step (does the answer make sense?)

### 6. Systems / Implementation Consequences
- How does the math translate to code?
- What are the memory, compute, and latency implications?
- Common implementation pitfalls
- Reference CS336 assignment connections where applicable

### 7. Neuroscience Analogy Box
- See `docs/neuroscience_analogy_policy.md` for the three-section format
- At least one analogy box per chapter
- Additional analogy boxes for major subsections where helpful

### 8. Common Misconceptions
- 3–5 misconceptions a student might have
- For each: state the misconception, then correct it with a clear explanation

### 9. Exercises
Four tiers:
- **Warmup** (2–3 exercises): Check basic understanding. Can be done mentally or with pen and paper.
- **Derivation** (2–3 exercises): Work through a proof, derivation, or analysis. Requires math.
- **Implementation** (1–2 exercises): Write code (Python/PyTorch). Connected to CS336 assignments where possible.
- **Open-ended** (1 exercise): Discussion question, design choice analysis, or paper-reading prompt.

### 10. Further Reading
- 3–5 annotated references
- Brief description of what each reference contributes beyond this chapter
- Priority: primary papers first, then surveys, then blog posts/tutorials

## Exercise Design Principles

1. **Progressive difficulty**: Each exercise builds on the previous one within a tier
2. **Self-checkable**: Provide sufficient information for students to verify their answers
3. **Connected to assignments**: Label exercises that directly prepare for CS336 assignments
4. **Time estimates**: Warmup (5–15 min), Derivation (20–45 min), Implementation (1–3 hours), Open-ended (30–60 min)

## Prerequisite Dependency Graph

```
Ch0 (Orientation) ──→ Ch1 (Probability/Entropy)
                  ──→ Ch2 (Linear Algebra)
                  ──→ Ch3 (PyTorch)

Ch1 ──→ Ch6 (LM Problem) ──→ Ch7 (Tokenization) ──→ Ch8 (n-gram to Neural)

Ch2 + Ch3 ──→ Ch9 (Attention) ──→ Ch10 (Transformer Blocks) ──→ Ch11 (Norms/Pos)
                                                              ──→ Ch12 (Hyperparams)
                                                              ──→ Ch13 (Variants)

Ch4 (CUDA/GPU) ──→ Ch14 (Resource Accounting) ──→ Ch15 (GPUs/TPUs)
                                               ──→ Ch16 (Kernels/Triton)
                                               ──→ Ch17 (Parallelism)

Ch10 + Ch14 ──→ Ch18 (Inference)

Ch10 + Ch12 ──→ Ch19 (Scaling Laws) ──→ Ch20 (Recipes) ──→ Ch21 (Evaluation)

Ch21 ──→ Ch22 (Data Sources) ──→ Ch23 (Filtering/Dedup)

Ch21 + Ch23 ──→ Ch24 (Instruction Tuning) ──→ Ch25 (RLHF/DPO/GRPO)
                                            ──→ Ch26 (Safety)
```

## Reading Paths

### Full Sequential
Ch 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → ... → 26

### "I Know ML, Teach Me LLMs"
Ch 0 → 6 → 7 → 9 → 10 → 11 → 12 → 19 → 20

### "I Want to Understand Systems"
Ch 4 → 14 → 15 → 16 → 17 → 18

### "I Want to Understand Alignment"
Ch 24 → 25 → 26 (with prereq capsules for RL concepts)

### CS336 Assignment Companion
A1: Ch 6–12 | A2: Ch 14–17 | A3: Ch 19–21 | A4: Ch 22–23 | A5: Ch 24–26
