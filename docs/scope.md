# Scope

## In Scope

### Full Coverage (Spring 2025)
All topics from the official CS336 Spring 2025 offering:
- Lectures 1–17 (overview through RL systems)
- Assignments 1–5 (Basics, Systems, Scaling, Data, Alignment)
- All papers referenced in `spring2025-lectures/references.py`

### Partial Coverage (Spring 2026)
Topics from the current `lectures/references.py` that are publicly available:
- New papers added to the 2026 reference list
- New architectural developments (Mamba 3, OLMiX, etc.)
- Updated model recipes (Qwen 3.5, GLM 5, DeepSeek V3.2, OLMo 3, etc.)
- Presented as "2026 Update Cards" — boxed notes that supplement the main narrative

### Prerequisites (Part 0)
Self-contained coverage of:
- Probability, entropy, cross-entropy, KL divergence, MLE, perplexity
- Linear algebra, matrix calculus, automatic differentiation
- PyTorch and tensor manipulation
- CUDA / GPU execution model basics
- Minimal linguistics and NLP background

### Appendices
- Proof techniques and derivation details
- CUDA/Triton cookbook
- Linguistics quick reference
- Neuroscience analogy index
- Reproducibility, experiment hygiene, and debugging

## Out of Scope

1. **Multimodal models** — CS336 focuses on text-only language models. Vision-language models, speech, etc. are mentioned only in passing.
2. **Production deployment** — We cover inference serving broadly but not production MLOps (Kubernetes, model registries, A/B testing).
3. **Specific cloud platform tutorials** — We reference GPU/TPU concepts but do not provide AWS/GCP/Azure step-by-step guides.
4. **Historical NLP survey** — We include enough history to motivate the Transformer, but this is not a comprehensive NLP history book.
5. **Non-English NLP** — Multilingual and cross-lingual topics are briefly mentioned in data chapters but not deeply covered.
6. **Reinforcement learning from scratch** — We assume basic RL concepts (reward, policy, gradient) and provide capsule refreshers; we do not teach full RL.

## Version Commitment

| Course Year | Commitment |
|-------------|------------|
| Spring 2025 | 100% coverage of all lectures and assignments |
| Spring 2026 | Best-effort coverage via "2026 Update Cards" for publicly available material |
| Future years | Out of scope for this edition |

## Chapter Numbering

The numbering in the blueprint is the canonical reference:
- Part 0: Chapters 0–5 (prerequisites)
- Part I: Chapters 6–8 (foundations)
- Part II: Chapters 9–13 (Transformer)
- Part III: Chapters 14–18 (systems)
- Part IV: Chapters 19–21 (scaling/eval)
- Part V: Chapters 22–23 (data)
- Part VI: Chapters 24–26 (alignment)
- Appendices: A–E
