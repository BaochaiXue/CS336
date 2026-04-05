# Repo State Audit

> Generated: 2026-04-05. Based on direct filesystem inspection.

## Root Directory Structure

```
CS336/
├── AGENTS.md              (1.4 KB) — project navigator
├── ARCHITECTURE.md        (4.2 KB) — structure description
├── README.md              (1.8 KB) — overview
├── cs336_textbook_blueprint.md (8.8 KB) — master blueprint
├── cs336_core_readings.md     (3.6 KB) — Tier A readings
├── cs336_paper_manifest.csv   (25 KB) — full paper list (root copy)
├── cs336_paper_manifest.json  (54 KB) — JSON mirror (root copy)
├── cs336_codex_master_prompt.txt (12 KB) — legacy codex prompt
├── book/                  — LaTeX source tree
├── docs/                  — system-of-record documents
├── papers/                — paper source management
└── scripts/               — build and validation tools
```

## book/ Structure

```
book/
├── textbook.tex           (9.1 KB) — main document, 337 lines
├── bibliography.bib       (22 KB)
├── frontmatter/           — title, preface, TOC
├── parts/                 — part-level TeX
├── chapters/              — 30 .tex files (including duplicates)
│   ├── ch00–ch10: 11 chapters
│   ├── ch11_norms_position.tex (STUB, 214 words, 22 TODOs)
│   ├── ch11_position.tex (MATURE, 1383 words, 0 TODOs) ⚠️ NOT included in textbook.tex
│   ├── ch12_hyperparameters.tex (STUB, 213 words, 22 TODOs)
│   ├── ch12_initialization.tex (MATURE, 1232 words, 0 TODOs) ⚠️ NOT included in textbook.tex
│   ├── ch13_variants.tex (STUB, 213 words, 22 TODOs)
│   ├── ch13_eval.tex (MATURE, 1074 words, 0 TODOs) ⚠️ NOT included in textbook.tex
│   └── ch14–ch26: 13 chapters (ALL STUBS, ~213 words each, 22 TODOs)
├── appendices/            — 5 appendix stubs (~9 words each)
├── figures/               — (exists, contents TBD)
└── tables/                — (exists, contents TBD)
```

### Critical Bug: textbook.tex includes stubs, not mature files

| Included in textbook.tex | Status | Mature alternative | Status |
|-------------------------|--------|-------------------|--------|
| `ch11_norms_position` | Stub (214w) | `ch11_position` | Mature (1383w) |
| `ch12_hyperparameters` | Stub (213w) | `ch12_initialization` | Mature (1232w) |
| `ch13_variants` | Stub (213w) | `ch13_eval` | Mature (1074w) |

## docs/ Structure

```
docs/
├── vision.md              (2.6 KB) ✅ exists, well-formed
├── scope.md               (2.7 KB) ✅ exists, well-formed
├── style_guide.md         (4.5 KB) ✅ exists, well-formed
├── notation.md            (5.6 KB) ✅ exists, well-formed
├── pedagogy.md            (4.5 KB) ✅ exists, well-formed
├── neuroscience_analogy_policy.md (3.6 KB) ✅ exists, well-formed
├── decision_log.md        (1.8 KB) ✅ exists, 7 decisions logged
├── course_coverage_matrix.md (5.7 KB) ✅ exists, well-formed
├── coverage_gap_audit.md  (2.2 KB) ⚠️ stale (doesn't reflect duplicate chapter issue)
├── repo_audit.md          — this file (being regenerated)
├── paper_pipeline_audit.md (0.5 KB) ⚠️ stale
├── chapter_specs/         ❌ empty
├── exec_plans/
│   ├── active/            ❌ empty
│   └── completed/         ❌ empty
└── evals/
    └── chapter_rubric.md  (2.3 KB) ✅ exists, well-formed
```

### Missing docs (referenced in requirements but not yet created):
- `docs/harness_audit.md`
- `docs/chapter_completion_report.md`
- `docs/course_coverage_audit.md`

## papers/ Structure

```
papers/
├── manifest.csv           (38 KB) — 116 entries
├── manifest.json          (89 KB) — JSON mirror
├── link_index.csv         (30 KB)
├── link_index.md          (12 KB)
├── raw_archives/          ❌ empty
├── extracted/             ❌ empty (papers went directly to normalized/)
├── normalized/            115 directories
├── merged_tex/            94 .tex files
└── metadata/
    ├── fetch_log.txt      (21 KB)
    ├── folder_rename_map.json (8.3 KB)
    ├── local_archives_inventory.json (2 bytes — empty array)
    ├── merge_results.json (19 KB)
    └── source_failures.json (521 bytes — 1 failure)
```

## scripts/ Structure

```
scripts/
├── audit_repo.py          (3.9 KB) ✅ functional
├── build_book.sh          (2.0 KB) ✅ functional
├── build_index.py         (4.7 KB) ✅ functional
├── fetch_papers.py        (7.6 KB) ✅ functional
├── merge_tex.py           (6.2 KB) ✅ functional
├── normalize_papers.py    (3.4 KB) ✅ functional
└── scan_local_archives.py (1.2 KB) ⚠️ typo in shebang: `#!/usr/import/env python3`
```

## Documentation–Reality Gaps

| Document | Claim | Reality |
|----------|-------|---------|
| AGENTS.md | `scripts/check_cs336_coverage.py` | Does not exist |
| ARCHITECTURE.md | `extracted/` contains paper dirs | Empty; papers are in `normalized/` |
| ARCHITECTURE.md | Pipeline: `raw_archives/ → extracted/ → normalized/` | Actually: downloaded → `normalized/` directly |
| repo_audit.md (old) | `papers/merged_tex` needs creation | Already has 94 files |
| paper_pipeline_audit.md (old) | fetch_papers.py doesn't merge | merge_tex.py handles this separately |
| scan_local_archives.py | Shebang: `#!/usr/import/env python3` | Should be `#!/usr/bin/env python3` |
