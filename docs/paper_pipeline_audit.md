# Paper Pipeline Audit

## Current State
- `manifest.csv` contains 116 entries.
- Processing currently yields:
  - 115 total extracted directories.
  - 94 have TeX files.
  - 21 are PDF only.
- `fetch_papers.py` currently retrieves from arXiv or URL, but DOES NOT search local archives, DOES NOT normalize names properly, and DOES NOT merge `.tex` sources.

## Action Plan
We must rewrite the pipeline as requested in the implementation plan to encompass steps A-H.
