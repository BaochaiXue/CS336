# AGENTS.md — CS336 Textbook Project Navigator

## Project
LaTeX textbook covering Stanford CS336: Language Modeling from Scratch (2025 + 2026).

## System of Record
- **Blueprint**: `cs336_textbook_blueprint.md` — master spec
- **Docs**: `docs/` — vision, scope, style, notation, coverage matrix, chapter specs, eval rubrics
- **Decision log**: `docs/decision_log.md`
- **Paper manifest**: `papers/manifest.csv` / `.json`
- **Source readings**: `cs336_core_readings.md` (Tier A), `cs336_paper_manifest.csv` (Tier B)

## Key Paths
| What | Where |
|------|-------|
| Book source | `book/textbook.tex` → `book/chapters/` |
| Build | `scripts/build_book.sh` |
| Coverage check | `scripts/check_cs336_coverage.py` |
| Paper sources | `papers/normalized/` → `papers/merged_tex/` |
| Master Index | `papers/link_index.md` |
| Chapter specs | `docs/chapter_specs/` |
| Eval rubrics | `docs/evals/` |

## Workflow
1. **Plan**: chapter spec in `docs/chapter_specs/`
2. **Retrieve**: paper sources via `scripts/fetch_papers.py`
3. **Draft**: LaTeX in `book/chapters/`
4. **Evaluate**: rubrics in `docs/evals/`, scripts in `scripts/`
5. **Log**: decisions in `docs/decision_log.md`, exec plans in `docs/exec_plans/`

## Conventions
- LaTeX engine: LuaLaTeX
- Citation: biblatex + biber
- Notation: see `docs/notation.md`
- Style: see `docs/style_guide.md`
