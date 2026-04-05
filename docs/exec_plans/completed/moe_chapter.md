# MoE Chapter Execution Plan

> Status: ACTIVE  
> Created: 2026-04-05  
> Author: Agent session 64570a68

## Objective

Write a complete, production-quality chapter on Mixture of Experts (MoE) for the CS336 textbook. This chapter maps to CS336 Lecture 4 (Spring 2025) and must be written into `book/chapters/ch13_variants.tex`.

## Decision: Chapter Placement

MoE content will be written into `ch13_variants.tex`, replacing the current pure-stub template. The chapter title changes from "Architectural Variants and Extensions" to "Mixture of Experts".

**Rationale:**
- CS336 L4 maps to Ch13 in the coverage matrix
- ch13_variants.tex is a pure empty stub (213 words, all TODO)
- MoE deserves a full chapter, not a subsection
- No renumbering required
- The previous stub title "Architectural Variants" was too vague

**Trade-off:** The book loses a generic "variants" chapter. Other architectural variants (linear attention, Mamba/SSM, MLA) can be covered in 2026 Update Cards within the relevant chapters, or in a future ch13b if needed.

## Content Requirements

### Must-Cover Topics
1. Why MoE: decoupling parameters from per-token compute
2. Dense FFN → sparse expert routing derivation
3. Top-k routing / top-1 routing definitions
4. Gating / router math
5. Capacity factor
6. Token dropping / overflow
7. Auxiliary load balancing loss
8. Importance / load imbalance
9. Expert collapse / router collapse / instability
10. Dispatch / combine implementation logic
11. All-to-all communication cost
12. Expert parallelism vs data/model/pipeline parallelism
13. Training throughput, memory, communication bottlenecks
14. Inference latency / throughput / cache
15. Sparse vs dense tradeoffs
16. Switch Transformer, GShard, Mixtral/DeepSeek landscape
17. Fine-tuning risks
18. MoE + long context + deployment cost

### Pedagogical Requirements
- Learning goals (4–5 measurable objectives)
- Big picture (motivation, where MoE fits in the Transformer story)
- Formal setup (notation for experts, gating, capacity)
- Worked example (token routing through an 8-expert MoE layer)
- Systems consequences (all-to-all, expert parallelism, memory)
- Neuroscience analogy box (sparse coding / functional specialization)
- Misconceptions (3–5 items)
- Exercises (warmup + derivation + implementation + open-ended)
- Further reading (annotated references)

### Neuroscience Analogy Constraints
- Must use three-section format (helps / breaks / keep)
- Approved domain: "Sparse coding in visual cortex → MoE routing"
- Must explicitly state:
  - Biological sparse coding is NOT an explicit router
  - No token-wise dispatch table in brains
  - Different timescales, plasticity, metabolic constraints
  - Keep: "not all subnetworks are equally active for all inputs"

## Source Papers

| Paper | Local Path | Status |
|-------|-----------|--------|
| Sparsely-Gated MoE | papers/merged_tex/moe.tex | ✅ |
| Switch Transformers | papers/merged_tex/switch_transformers.tex | ✅ |
| Mixtral | papers/merged_tex/mixtral.tex | ✅ |
| DeepSeek V2 | papers/merged_tex/deepseek_v2.tex | ✅ |
| DeepSeek V3 | papers/merged_tex/deepseek_v3.tex | ✅ |
| Aux-Loss-Free MoE | papers/merged_tex/auxfree.tex | ✅ |
| GShard | NOT YET IN MANIFEST | ❌ Add |

## Deliverables

- [ ] `book/chapters/ch13_variants.tex` — complete MoE chapter (~3000+ words)
- [ ] `book/bibliography.bib` — MoE-related BibTeX entries
- [ ] `docs/decision_log.md` — MoE placement decision logged
- [ ] `papers/manifest.csv` — GShard entry added
- [ ] Verify: chapter compiles with lualatex

## Completion Criteria

The chapter is "done" when:
1. All 18 content topics are addressed
2. Neuroscience analogy follows three-section format
3. At least 4 exercises across all tiers
4. Chapter compiles without errors
5. At least 3 citations present
