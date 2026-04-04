# CS336: Language Modeling from Scratch — Textbook

A self-contained LaTeX textbook covering Stanford CS336 (Spring 2025, with 2026 extensions).

## About

This textbook follows the CS336 "from scratch" philosophy: building a complete understanding of language models from tokenization through alignment. It is designed for CS undergraduates who can program in Python but do not assume prior knowledge of NLP, linguistics, CUDA, or distributed systems.

**Key features:**
- Mathematically rigorous but accessible to undergraduates
- Self-contained prerequisite coverage (probability, linear algebra, PyTorch, GPU basics)
- Neuroscience-first analogies with explicit similarity/difference analysis
- Primary-source grounded (papers, official course materials, official repos)
- Full coverage of CS336 assignments A1–A5

## Building the Book

### Prerequisites
- LuaLaTeX (via TeX Live or MacTeX)
- Biber (for bibliography processing)

### Build
```bash
./scripts/build_book.sh
```

### Partial Build (single chapter)
```bash
# Edit \includeonly in textbook.tex, then:
./scripts/build_book.sh
```

## Structure

| Part | Topic | Chapters |
|------|-------|----------|
| 0 | Prerequisites | 0–5 |
| I | LM Foundations | 6–8 |
| II | Transformer Internals | 9–13 |
| III | Systems & Implementation | 14–18 |
| IV | Scaling, Evaluation, Recipes | 19–21 |
| V | Data | 22–23 |
| VI | Alignment & Reasoning | 24–26 |
| App | Appendices | A–E |

## Course Alignment

Maps to Stanford CS336 assignments:
- **A1 (Basics)**: Chapters 6–12
- **A2 (Systems)**: Chapters 14–17
- **A3 (Scaling)**: Chapters 19–21
- **A4 (Data)**: Chapters 22–23
- **A5 (Alignment)**: Chapters 24–26

## License

Educational use. Paper citations follow original authors' licensing.
