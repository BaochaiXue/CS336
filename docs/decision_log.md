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
