# Architecture — CS336 Textbook Project

## Repository Structure (Current State — 2026-04-05)

```
CS336/
├── AGENTS.md                    # Project navigator (short, high-signal)
├── ARCHITECTURE.md              # This file
├── README.md                    # Project overview and build instructions
├── cs336_textbook_blueprint.md  # Master blueprint (pre-existing)
├── cs336_core_readings.md       # Tier A reading bundles (pre-existing)
├── cs336_paper_manifest.csv     # Full paper manifest (pre-existing, root copy)
├── cs336_paper_manifest.json    # JSON mirror (pre-existing, root copy)
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
│   ├── course_coverage_audit.md # Detailed 2025/2026 alignment analysis
│   ├── repo_audit.md            # Filesystem state audit
│   ├── harness_audit.md         # Harness readiness assessment
│   ├── paper_pipeline_audit.md  # Paper processing state
│   ├── coverage_gap_audit.md    # Per-chapter metrics (auto-generated)
│   ├── chapter_completion_report.md  # Quantitative chapter maturity
│   ├── chapter_specs/           # Per-chapter design documents
│   ├── exec_plans/              # Execution plans
│   │   ├── active/              # In-progress plans
│   │   └── completed/           # Finished plans with results
│   └── evals/                   # Evaluation rubrics and checklists
│       └── chapter_rubric.md    # Standard chapter evaluation template
│
├── papers/                      # Paper source management
│   ├── manifest.csv             # Working copy of paper manifest (116 entries)
│   ├── manifest.json            # JSON mirror
│   ├── link_index.csv           # Paper link index
│   ├── link_index.md            # Markdown version
│   ├── raw_archives/            # Downloaded archives (transient, currently empty)
│   ├── extracted/               # Intermediate extraction (currently empty)
│   ├── normalized/              # Final paper directories (115 dirs)
│   ├── merged_tex/              # Single-file merged TeX per paper (94 files)
│   └── metadata/                # Processing metadata and logs
│       ├── merge_results.json
│       ├── folder_rename_map.json
│       ├── source_failures.json
│       ├── local_archives_inventory.json
│       └── fetch_log.txt
│
├── book/                        # LaTeX source
│   ├── textbook.tex             # Main document
│   ├── frontmatter/             # Title page, preface, TOC
│   ├── parts/                   # Part-level TeX files
│   ├── chapters/                # One .tex per chapter (27 chapters + 3 legacy files)
│   ├── appendices/              # 5 appendix stubs
│   ├── figures/
│   ├── tables/
│   └── bibliography.bib         # BibTeX database
│
└── scripts/                     # Build and validation tools
    ├── fetch_papers.py           # Download paper sources from arXiv/URLs
    ├── scan_local_archives.py    # Locate local archive files
    ├── normalize_papers.py       # Rename paper directories to canonical names
    ├── merge_tex.py              # Merge and clean TeX sources
    ├── build_index.py            # Generate link_index, update manifest
    ├── audit_repo.py             # Generate per-chapter coverage metrics
    └── build_book.sh             # Full LuaLaTeX + biber build pipeline
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

**Current actual flow:**
```
arXiv e-print / URL → fetch_papers.py → raw_archives/ (transient)
                    → extract/decompress → normalized/<canonical_name>/
                    → merge_tex.py → normalized/<name>/merged_paper.tex
                                   → merged_tex/<name>.tex
                    → build_index.py → manifest.csv/json updated
                                     → link_index.csv/md regenerated
```

**Note:** The `extracted/` directory was an intermediate stage that has been superseded.
Papers now go directly from download to `normalized/`.

### Chapter Lifecycle
```
spec (docs/chapter_specs/) → draft (book/chapters/) → eval (docs/evals/) → done
```

### Known Issues

1. Three legacy stub files exist alongside mature versions:
   - `ch11_norms_position.tex` (stub) vs `ch11_position.tex` (mature)
   - `ch12_hyperparameters.tex` (stub) vs `ch12_initialization.tex` (mature)
   - `ch13_eval.tex` (mature, evaluation content) — not currently included
2. `textbook.tex` now includes the mature versions (fixed 2026-04-05)
3. Chapters 14–26 and all appendices remain as stubs
