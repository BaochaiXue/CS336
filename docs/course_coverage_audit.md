# CS336 Course Coverage Audit

> Generated: 2026-04-05. Cross-referenced against CS336 Spring 2025 syllabus and 2026 references.

## Lecture → Chapter Coverage Status

### Spring 2025

| # | Lecture Topic | Chapter(s) | Chapter Status | Coverage |
|---|--------------|-----------|----------------|----------|
| L1 | Overview, tokenization, LM | Ch 0, 6, 7 | Ch0: Partial, Ch6: Mature, Ch7: Mature | ⚠️ Partial |
| L2 | PyTorch, training, resource accounting | Ch 3, 12, 14 | Ch3: Mature, Ch12-init: Mature (not included!), Ch14: Stub | ⚠️ Partial |
| L3 | Architecture (Transformer) | Ch 9, 10, 11 | Ch9: Mature, Ch10: Mature, Ch11-pos: Mature (not included!) | ⚠️ Partial (include bug) |
| L4 | **Mixture of Experts** | **Ch 13** | **Ch13_variants: STUB (pure TODO)** | ❌ **Not covered** |
| L5 | GPUs | Ch 15 | Stub | ❌ Not covered |
| L6 | Kernels, Triton | Ch 16 | Stub | ❌ Not covered |
| L7 | Parallelism basics | Ch 17 | Stub | ❌ Not covered |
| L8 | Parallelism advanced | Ch 17 | Stub | ❌ Not covered |
| L9 | Scaling laws basics | Ch 19 | Stub | ❌ Not covered |
| L10 | Inference, evaluation | Ch 18, 21 | Both Stub | ❌ Not covered |
| L11 | Scaling details | Ch 19, 20 | Both Stub | ❌ Not covered |
| L12 | Data: sources, filtering | Ch 22 | Stub | ❌ Not covered |
| L13 | Data: dedup, mixing | Ch 22, 23 | Both Stub | ❌ Not covered |
| L14 | Data: SFT construction | Ch 23, 24 | Both Stub | ❌ Not covered |
| L15 | RLHF alignment | Ch 25 | Stub | ❌ Not covered |
| L16 | RLVR (reasoning RL) | Ch 25 | Stub | ❌ Not covered |
| L17 | RL systems | Ch 25, 26 | Both Stub | ❌ Not covered |

### Coverage Summary
- **Mature content available**: L1 (partial), L2 (partial), L3 (partial, blocked by include bug)
- **Zero coverage**: L4 (MoE), L5–L17 (all Part III through Part VI)
- **Include bug impact**: Even the mature content for L2 (ch12_initialization) and L3 (ch11_position) is invisible in the compiled PDF because textbook.tex includes the stub versions

## Assignment → Chapter Readiness

| Assignment | Chapters Needed | Mature? | Ready? |
|-----------|----------------|---------|--------|
| A1: Basics | Ch 6,7,9–12 | Ch6,7,9,10: ✅; Ch11,12: ✅ content exists but wrong include | ⚠️ Fixable |
| A2: Systems | Ch 14–17 | None mature | ❌ |
| A3: Scaling | Ch 10,11,19 | Ch10: ✅ | ❌ |
| A4: Data | Ch 22,23 | None mature | ❌ |
| A5: Alignment | Ch 24–26 | None mature | ❌ |

## MoE Coverage Audit (Special Section)

### CS336 Course Requirements
- **L4 (Spring 2025)**: Dedicated lecture on Mixture of Experts
- **2026**: MoE remains on syllabus; DeepSeek V2/V3 are MoE-heavy references

### Current State in Book
- `ch13_variants.tex` is the mapped chapter for L4
- **Content: ZERO**. The file is a 99-line pure TODO template
- Not a single sentence of MoE content exists anywhere in the book
- The chapter title "Architectural Variants and Extensions" is too vague for a topic that gets its own lecture

### Required Content (per specification)
1. Why MoE: decoupling parameters from per-token compute
2. Dense FFN → sparse expert routing derivation
3. Top-k/top-1 routing definitions  
4. Gating/router math
5. Capacity factor
6. Token dropping/overflow
7. Auxiliary load balancing loss
8. Expert/router collapse
9. Dispatch/combine implementation
10. All-to-all communication cost
11. Expert parallelism
12. Training throughput/memory/communication
13. Inference latency/throughput/cache
14. Sparse vs dense tradeoffs
15. Switch Transformer, GShard, Mixtral/DeepSeek landscape
16. Fine-tuning risks
17. MoE + long context + deployment cost

### Related Papers Available in Pipeline
| Paper | TeX Available? |
|-------|---------------|
| Sparsely-Gated MoE (Shazeer 2017) | ✅ |
| Switch Transformers | ✅ |
| Mixtral | ✅ |
| DeepSeek V2 (MLA + MoE) | ✅ |
| DeepSeek V3 | ✅ |
| Aux-Loss-Free MoE | ✅ |
| GShard | ❌ Missing from manifest |

### Decision
**MoE must be written into ch13_variants.tex as a complete, dedicated chapter.** The chapter title should change from "Architectural Variants" to "Mixture of Experts" to match CS336 L4 scope. This is not a subsection treatment — it is a full chapter.

## Spring 2026 Topics

| Topic | Status in Book | Available Papers |
|-------|---------------|-----------------|
| Mamba/SSM (Mamba 2, Mamba 3) | Not covered | ✅ mamba_2, mamba_3 merged |
| OLMiX | Not covered | ✅ olmix merged |
| Multi-Token Prediction | Not covered | ✅ mtp merged |
| MLA (Multi-head Latent Attention) | Not covered | ✅ deepseek_v2 discusses |
| Aux-loss-free MoE | Not covered | ✅ auxfree merged |
| μP | Not covered | ✅ mup merged |
| Muon/SOAP optimizers | Not covered | ✅ soap merged |
| OLMo 3 | Not covered | ✅ olmo_3 merged |
| DeepSeek V3.2 | Not covered | ✅ deepseek_v3_2 merged |
| Qwen 3.5 | Not covered | ⚠️ pdf_only |
| GLM 5 | Not covered | ✅ glm_5 merged |

These should be addressed as "2026 Update Cards" per docs/scope.md.

## Priority Ranking for Chapter Writing

### Immediate (this session)
1. **Fix textbook.tex includes** (ch11, ch12 point to mature files)
2. **Write ch13 MoE chapter** (L4, zero current coverage)

### High Priority (next sessions)
3. Ch14 Resource Accounting (L2 mapping, A2 prep)
4. Ch15 GPUs/TPUs (L5)
5. Ch17 Parallelism (L7–L8, A2)
6. Ch19 Scaling Laws (L9, L11, A3)

### Medium Priority
7. Ch16 Kernels/Triton (L6, A2)
8. Ch18 Inference (L10)
9. Ch20 Model Recipes (L11)
10. Ch21 Evaluation (L10)

### Lower Priority (but still required)
11. Ch22–23 Data (L12–L14, A4)
12. Ch24–26 Alignment (L15–L17, A5)
