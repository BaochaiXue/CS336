# Decision Log

All major decisions with rationale. Chronological order.

---

## 2026-04-03: Project initialization

### Decision: LaTeX engine → LuaLaTeX
**Rationale**: Full Unicode support for international author names, modern font handling via fontspec, better memory management for large documents. Compatible with all major TeX distributions.

### Decision: Bibliography → biblatex + biber
**Rationale**: Better Unicode support than BibTeX, flexible citation formatting, supports per-chapter bibliographies if needed.

### Decision: Paper tiering system (A/B/C)
**Rationale**: Not all papers deserve equal depth of integration. Tier A (core readings) are deeply woven into the narrative. Tier B (official references) are cited and discussed. Tier C (2026 frontier) appear in boxed update cards to avoid destabilizing the main narrative.

### Decision: Chapter numbering starts at 0
**Rationale**: Part 0 (prerequisites) uses Chapters 0–5, matching the blueprint. This avoids renumbering when chapters are added or removed.

### Decision: Neuroscience-first analogy policy
**Rationale**: Most CS students have informal intuitions about brains that can be leveraged, but these intuitions are often wrong. The three-section analogy box (helps / breaks / keep) is designed to build useful intuition while preventing misconceptions.

### Decision: 2026 coverage as "Update Cards"
**Rationale**: The 2026 course site is not yet public. Rather than speculate about syllabus changes, we integrate confirmed 2026 papers from `references.py` as boxed update cards that supplement the main narrative.

### Decision: Full paper source download
**Rationale**: Having local LaTeX sources allows direct quotation verification, notation comparison, and precise citation. The disk cost (~2-5 GB) is acceptable.

---

## 2026-04-05: Harness engineering overhaul

### Decision: Fix textbook.tex includes (ch11, ch12)
**Rationale**: Discovered that `textbook.tex` was including stub files (`ch11_norms_position.tex`, `ch12_hyperparameters.tex`) instead of the mature content files (`ch11_position.tex`, `ch12_initialization.tex`). The compiled PDF showed TODO placeholders for chapters that had complete content. Fixed by pointing includes to the mature files.

### Decision: MoE goes into ch13_variants.tex as full chapter
**Rationale**: CS336 Lecture 4 is entirely dedicated to MoE. The current `ch13_variants.tex` is a pure stub (213 words, all TODO). Rather than creating a new chapter and renumbering everything, we repurpose this stub as a dedicated MoE chapter. The previous title "Architectural Variants and Extensions" was too vague. Other architectural variants (linear attention, Mamba/SSM, MLA) can be handled via 2026 Update Cards or appendices. Exec plan: `docs/exec_plans/active/moe_chapter.md`.

### Decision: GShard to be added to paper manifest
**Rationale**: GShard (Lepikhin et al. 2020, arXiv: 2006.16668) is a key MoE paper that describes the foundational concepts of expert parallelism and capacity factor. It was missing from the manifest despite being directly relevant to the Ch13 MoE content.
