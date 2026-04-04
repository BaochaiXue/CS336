# Architecture — CS336 Textbook Project

## Repository Structure

```
CS336/
├── AGENTS.md                    # Project navigator (short, high-signal)
├── ARCHITECTURE.md              # This file
├── README.md                    # Project overview and build instructions
├── cs336_textbook_blueprint.md  # Master blueprint (pre-existing)
├── cs336_core_readings.md       # Tier A reading bundles (pre-existing)
├── cs336_paper_manifest.csv     # Full paper manifest (pre-existing)
├── cs336_paper_manifest.json    # JSON mirror of manifest (pre-existing)
│
├── docs/                        # System of record
│   ├── vision.md                # Project mission and principles
│   ├── scope.md                 # In/out scope, 2025 vs 2026 commitment
│   ├── style_guide.md           # LaTeX conventions, prose rules
│   ├── notation.md              # Master symbol table
│   ├── pedagogy.md              # Chapter template, exercise taxonomy
│   ├── neuroscience_analogy_policy.md
│   ├── decision_log.md          # All major decisions with rationale
│   ├── course_coverage_matrix.md
│   ├── chapter_specs/           # Per-chapter design documents
│   ├── exec_plans/              # Active and completed execution plans
│   │   ├── active/
│   │   └── completed/
│   └── evals/                   # Evaluation rubrics and checklists
│
├── papers/                      # Paper source management
│   ├── manifest.csv             # Working copy of paper manifest
│   ├── manifest.json            # JSON mirror
│   ├── raw_archives/            # Downloaded archives (transient)
│   ├── extracted/               # Extracted paper directories
│   ├── normalized/              # Cleaned/renamed paper directories
│   ├── merged_tex/              # Single-file merged TeX per paper
│   └── metadata/                # Processing metadata and failure logs
│
├── book/                        # LaTeX source
│   ├── textbook.tex             # Main document
│   ├── frontmatter/             # Title page, preface, TOC
│   ├── parts/                   # Part-level TeX files
│   ├── chapters/                # One .tex per chapter
│   ├── appendices/              # Appendix .tex files
│   ├── figures/                 # All figures
│   ├── tables/                  # Standalone table files
│   └── bibliography.bib         # BibTeX database
│
└── scripts/                     # Build and validation tools
    ├── fetch_papers.py           # Download paper sources (legacy/primitive)
    ├── scan_local_archives.py    # Locates raw .tar.gz and .zip in repo
    ├── normalize_papers.py       # Normalizes paper extraction folders
    ├── merge_tex.py              # Merges and cleans TeX sources recursively
    ├── build_index.py            # Generates link_index and updates manifest
    ├── audit_repo.py             # Generates completion tracking metrics
    └── build_book.sh             # Full build pipeline
    [TODO: lint_tex.py, check_references.py, etc are planned but not yet implemented]
```

## Design Decisions

### LaTeX Engine: LuaLaTeX
- Full Unicode support for author names, math symbols
- Modern font handling (fontspec)
- Better memory management for large documents

### Document Class: book
- Standard `book` class with custom preamble
- Parts → Chapters → Sections hierarchy
- `\include` for chapters (enables `\includeonly` for fast partial builds)

### Bibliography: biblatex + biber
- Better Unicode handling than BibTeX
- Flexible citation styles
- Per-chapter bibliographies possible if needed

### Paper Processing Pipeline
```
arxiv e-print → raw_archives/ → extracted/ → normalized/ → merged_tex/
                                                          ↓
                                                    manifest.csv updated
```

### Chapter Lifecycle
```
spec (docs/chapter_specs/) → draft (book/chapters/) → eval (docs/evals/) → done
```
