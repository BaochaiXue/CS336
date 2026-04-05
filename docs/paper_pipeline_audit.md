# Paper Pipeline Audit

> Generated: 2026-04-05. Based on direct inspection of papers/ directory and scripts/.

## Pipeline Overview

### Actual Pipeline (Current State)
```
arXiv/URL → fetch_papers.py → papers/raw_archives/ (transient) 
         → extract → papers/normalized/<canonical_name>/
         → merge_tex.py → papers/merged_tex/<canonical_name>.tex
         → build_index.py → manifest.csv/json, link_index.csv/md
```

### Scripts and Their Capabilities

| Script | What It Does | Limitations |
|--------|-------------|-------------|
| `scan_local_archives.py` | Walks repo for .zip/.tar/.gz files | Shebang typo (`/usr/import/`); output is empty `[]` (no archives found) |
| `fetch_papers.py` | Downloads from arXiv e-print or URL, extracts | Works well; rate-limits arXiv; no local archive search |
| `normalize_papers.py` | Renames extracted/ dirs to canonical names | Moves from extracted/ to normalized/; extracted/ is now empty |
| `merge_tex.py` | Finds main .tex, expands \\input/\\include, cleans comments | Handles verbatim environments; 5-level recursion; outputs to both local and global |
| `build_index.py` | Updates manifest fields, generates link_index | Adds canonical_title, legal_folder_name, source_status fields |
| `audit_repo.py` | Generates coverage_gap_audit.md and repo_audit.md | Simplistic word-count heuristic (>1000 = Mature) |
| `build_book.sh` | Full LuaLaTeX + biber build pipeline | Clean/quick modes; works correctly |

## Current Data State

### Manifest
- `papers/manifest.csv`: 116 entries (header + 116 data rows)
- `papers/manifest.json`: 116 entries (JSON array)
- Root-level copies (`cs336_paper_manifest.csv/json`): 116 entries — these are the *original* manifests before working copies were created

### Normalized Papers
- **115 directories** in `papers/normalized/`
- Some directory names have bracket artifacts: `[marin_8b_retro]`, `[minimax_m2.5]`, `[xiaomi_mimo_v2]`
- Some names use commas: `nemotron_3_super_open,_efficient_mixture_of_experts...`

### Merged TeX
- **94 files** in `papers/merged_tex/`
- All successfully merged papers have entries in `papers/metadata/merge_results.json`

### Source Status Breakdown

| Status | Count | Examples |
|--------|-------|---------|
| success (TeX merged) | 73 | llama3, chinchilla, transformer, moe, switch_transformers, mixtral |
| pdf_only | 21 | long_short_term_memory, language_models_are_unsupervised_multitask_learners, adagrad |
| download_failed | 1 | bahdanau_training_costs (Medium blog post) |

### MoE-Related Papers in Pipeline

| Paper | Folder | Merged TeX? | Notes |
|-------|--------|------------|-------|
| Sparsely-Gated MoE (Shazeer 2017) | `moe` | ✅ | 65 KB merged |
| Switch Transformers (Fedus 2022) | `switch_transformers` | ✅ | 96 KB merged |
| Mixtral of Experts (Jiang 2024) | `mixtral` | ✅ | 36 KB merged |
| DeepSeek-V2 (MLA + MoE) | `deepseek_v2` | ✅ | 132 KB merged |
| DeepSeek-V3 | `deepseek_v3` | ✅ | 138 KB merged |
| Aux-Loss-Free MoE | `auxfree` | ✅ | 48 KB merged |
| **GShard** | ❌ NOT IN MANIFEST | ❌ | Must be added |

### Metadata Files

| File | Content |
|------|---------|
| `fetch_log.txt` | 21 KB of download logs |
| `folder_rename_map.json` | 8.3 KB, maps old→new directory names |
| `local_archives_inventory.json` | 2 bytes (`[]`) — no archives found |
| `merge_results.json` | 19 KB, 94 entries with status |
| `source_failures.json` | 1 failure (Bahdanau blog post) |

## Pipeline Gaps

1. **GShard not in manifest** — important MoE paper, needs addition
2. **No `archive_cleanup_log.json`** — raw archives are already cleaned (empty dir) but no log exists
3. **Bracket-named directories** — `[marin_8b_retro]` etc. are technically valid but ugly
4. **scan_local_archives.py has typo** in shebang line
5. **extracted/ is empty** — all content moved to normalized/, but ARCHITECTURE.md still references it as an active stage

## Recommended Actions

1. Add GShard to manifest (arxiv: 2006.16668)
2. Fix scan_local_archives.py shebang
3. Create `archive_cleanup_log.json` noting current state
4. Update ARCHITECTURE.md to reflect actual pipeline flow
5. The pipeline is fundamentally working; no major rewrites needed
