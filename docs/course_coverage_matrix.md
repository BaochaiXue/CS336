# CS336 Course Coverage Matrix

## Lecture → Chapter Mapping (Spring 2025)

| # | Lecture Topic | Format | Assignment | Textbook Chapter(s) | Status |
|---|--------------|--------|-----------|---------------------|--------|
| L1 | Overview, tokenization, language modeling | `lecture_01.py` | A1 | Ch 0, 6, 7 | ☐ |
| L2 | PyTorch, training, resource accounting | `lecture_02.py` | A1 | Ch 3, 12, 14 | ☐ |
| L3 | Architecture (Transformer design) | `lecture_3.pdf` | A1 | Ch 9, 10, 11 | ☐ |
| L4 | Mixture of Experts | `lecture_4.pdf` | — | Ch 13 | ☐ |
| L5 | GPUs | `lecture_5.pdf` | A2 | Ch 15 | ☐ |
| L6 | Kernels, Triton, compilation | `lecture_06.py` | A2 | Ch 16 | ☐ |
| L7 | Parallelism basics | `lecture_7.pdf` | A2 | Ch 17 | ☐ |
| L8 | Parallelism advanced | `lecture_08.py` | A2 | Ch 17 | ☐ |
| L9 | Scaling laws basics | `lecture_9.pdf` | A3 | Ch 19 | ☐ |
| L10 | Inference, evaluation | `lecture_10.py` | A3 | Ch 18, 21 | ☐ |
| L11 | Scaling details | `lecture_11.pdf` | A3 | Ch 19, 20 | ☐ |
| L12 | Data: sources, filtering | `lecture_12.py` | A4 | Ch 22 | ☐ |
| L13 | Data: dedup, mixing, rewriting | `lecture_13.py` | A4 | Ch 22, 23 | ☐ |
| L14 | Data: SFT data construction | `lecture_14.py` | A4/A5 | Ch 23, 24 | ☐ |
| L15 | RLHF alignment | `lecture_15.pdf` | A5 | Ch 25 | ☐ |
| L16 | RLVR (reasoning RL) | `lecture_16.pdf` | A5 | Ch 25 | ☐ |
| L17 | RL systems / guest lectures | `lecture_17.py` | — | Ch 25, 26 | ☐ |

## Assignment → Chapter Mapping

### Assignment 1: Basics
| A1 Task | Chapter | Section |
|---------|---------|---------|
| Implement BPE tokenizer | Ch 7 | §7.3 BPE algorithm |
| Implement Transformer model | Ch 9–11 | §9 Attention, §10 Blocks, §11 Norms/Position |
| Implement AdamW optimizer | Ch 12 | §12.3 Optimization |
| Train minimal language model | Ch 12 | §12.4 Training loop |
| Learning rate scheduling | Ch 12 | §12.2 Learning rate |

### Assignment 2: Systems
| A2 Task | Chapter | Section |
|---------|---------|---------|
| Profile model with tools | Ch 14 | §14.1–14.3 Resource accounting |
| Benchmark attention layers | Ch 14–15 | §14.4 Arithmetic intensity, §15 GPUs |
| Implement FlashAttention2 in Triton | Ch 16 | §16.4 FlashAttention |
| Distributed training (FSDP) | Ch 17 | §17.4 ZeRO/FSDP |
| Gradient checkpointing | Ch 17 | §17.5 Checkpointing |

### Assignment 3: Scaling
| A3 Task | Chapter | Section |
|---------|---------|---------|
| Understand Transformer components | Ch 10–11 | §10–11 (component ablation) |
| Fit scaling laws via training API | Ch 19 | §19.1–19.3 Kaplan, Chinchilla |
| Project model scaling | Ch 19 | §19.4 Compute-optimal prediction |

### Assignment 4: Data
| A4 Task | Chapter | Section |
|---------|---------|---------|
| Process Common Crawl WARC files | Ch 22 | §22.1 Data sources, §22.2 Crawling |
| Text extraction and cleaning | Ch 22 | §22.3 Cleaning/transformation |
| Quality filtering | Ch 23 | §23.1 Filtering |
| Deduplication (MinHash/exact) | Ch 23 | §23.2 Deduplication |
| Data mixing | Ch 23 | §23.3 Mixing |

### Assignment 5: Alignment and Reasoning RL
| A5 Task | Chapter | Section |
|---------|---------|---------|
| Supervised fine-tuning (SFT) | Ch 24 | §24.1–24.2 Instruction tuning |
| REINFORCE / GRPO for math reasoning | Ch 25 | §25.3 GRPO, §25.4 Reasoning RL |
| (Optional) DPO implementation | Ch 25 | §25.2 DPO |
| (Optional) Safety alignment | Ch 26 | §26.1 Safety alignment |

## Topic Coverage Checklist

### Core Topics (Must Cover)
- [☐] Overview / motivation for language modeling
- [☐] Tokenization (BPE, byte-level, unigram)
- [☐] PyTorch / training mechanics
- [☐] Resource accounting (FLOPs, memory, arithmetic intensity)
- [☐] Transformer architecture (attention, blocks, norms, FFN)
- [☐] Hyperparameters and initialization
- [☐] Mixture of Experts
- [☐] GPUs / TPUs / memory hierarchy
- [☐] Kernels / Triton / FlashAttention
- [☐] Parallelism (data, tensor, pipeline, ZeRO/FSDP)
- [☐] Scaling laws (Kaplan, Chinchilla, overtrained)
- [☐] Inference (KV cache, batching, throughput)
- [☐] Evaluation (MMLU, benchmarks, contamination)
- [☐] Data sources / filtering / deduplication / mixing
- [☐] SFT / instruction tuning
- [☐] RLHF / PPO / DPO
- [☐] GRPO / reasoning RL
- [☐] Safety alignment

### Extended Topics (2026 / Best-Effort)
- [☐] LSTM (historical context)
- [☐] Linear attention
- [☐] QK normalization
- [☐] Auxiliary-loss-free MoE
- [☐] Multi-token prediction
- [☐] Mamba / SSM architectures
- [☐] MLA (Multi-head Latent Attention)
- [☐] μP (maximal update parameterization)
- [☐] Muon / SOAP optimizers
- [☐] WSD learning rate schedule
- [☐] Data: Nemotron-CC, RegMix
- [☐] Models: OLMo 3, DeepSeek V3.2, Qwen 3.5, GLM 5, Marin

### Prerequisite Topics
- [☐] Probability, entropy, cross-entropy, KL divergence
- [☐] MLE, perplexity
- [☐] Linear algebra, matrix calculus
- [☐] Automatic differentiation
- [☐] PyTorch tensors and autograd
- [☐] CUDA / GPU execution model
- [☐] Minimal linguistics background

## Paper Coverage Summary

| Category | Total Papers | In 2025 | In 2026 | Status |
|----------|-------------|---------|---------|--------|
| Alignment/Reasoning RL | 18 | 9 | 18 | ☐ |
| Architectures/Attention | 21 | 16 | 21 | ☐ |
| Evaluation | 4 | 4 | 4 | ☐ |
| General/Foundations | 11 | 9 | 11 | ☐ |
| Model Recipes | 23 | 18 | 23 | ☐ |
| Optimization/Scaling | 13 | 10 | 13 | ☐ |
| Systems/Parallelism | 16 | 13 | 16 | ☐ |
| Tokenization/Data | 12 | 11 | 12 | ☐ |
| **Total** | **118** | **90** | **118** | ☐ |
