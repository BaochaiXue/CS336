import os
import glob
import csv

def main():
    os.makedirs('docs', exist_ok=True)
    
    # Check textbook coverage gap (Word count approximation)
    print("Gathering book chapter statistics...")
    ch_stats = []
    base_book = "book/chapters"
    try:
        files = glob.glob(os.path.join(base_book, "*.tex")) + glob.glob("book/appendices/*.tex")
        files.sort()
        for f in files:
            with open(f, 'r') as fp:
                data = fp.read()
                words = len(data.split())
                todos = data.count("TODO") + data.count("stub")
                ch_stats.append((os.path.basename(f), words, todos))
    except Exception as e:
        print(e)
    
    # Audit coverage
    coverage_md = "# Coverage Gap Audit\n\n## Textbook Chapter Status\n\n| Chapter | Word Count | TODOs | Status |\n|---------|------------|-------|--------|\n"
    for name, words, todos in ch_stats:
        status = "Stub"
        if words > 1000: status = "Mature"
        elif words > 250: status = "Partial"
        coverage_md += f"| `{name}` | {words} | {todos} | {status} |\n"
        
    coverage_md += "\n## CS336 Syllabus Alignment Gaps\n"
    coverage_md += "Currently, Chapters 0-13 cover Probability, PyTorch, Tokenization, Optimization basics, Attention, Block architecture, Position Embeddings, and basic Evaluation well. However, significant gaps exist for **Part III: The Training Pipeline** (Hardware, DP/FSDP parallelism, scaling laws, RLHF/Reasoning RL). These map to CS336 Assignments 3, 4, and 5 and are critical to draft next.\n"
    
    with open("docs/coverage_gap_audit.md", "w") as f:
        f.write(coverage_md)

    # Read papers
    print("Gathering paper statistics...")
    total_manifest = 0
    with open("papers/manifest.csv", 'r') as f:
        reader = csv.DictReader(f)
        total_manifest = sum(1 for row in reader)
        
    extracted_dirs = os.listdir("papers/extracted") if os.path.exists("papers/extracted") else []
    extracted_dirs = [d for d in extracted_dirs if os.path.isdir(os.path.join("papers/extracted", d))]
    
    num_tex = 0
    num_pdf_only = 0
    for d in extracted_dirs:
        files = os.listdir(os.path.join("papers/extracted", d))
        if any(f.endswith('.tex') for f in files):
            num_tex += 1
        elif any(f.endswith('.pdf') for f in files):
            num_pdf_only += 1

    repo_audit = f"""# Repo State Audit

## Overview
- This repository conforms partially to `ARCHITECTURE.md`.
- `book/` exists and contains {len(ch_stats)} chapters/appendices, of which {(sum(1 for s in ch_stats if s[1]>1000))} are considered 'Mature'.
- `scripts/` exists but predominantly relies on a primitive `fetch_papers.py`.

## Directory Deltas
- Missing / Needs Creation: `papers/merged_tex`, `papers/raw_archives`, `docs/chapter_specs`, `docs/exec_plans/active|completed`.
- `papers/extracted` contains {len(extracted_dirs)} entries. Many are currently named using slug identifiers (e.g. `a_neural_probabilistic_language_model`) rather than normalized ASCII strings.
"""
    with open("docs/repo_audit.md", "w") as f:
        f.write(repo_audit)

    pipe_audit = f"""# Paper Pipeline Audit

## Current State
- `manifest.csv` contains {total_manifest} entries.
- Processing currently yields:
  - {len(extracted_dirs)} total extracted directories.
  - {num_tex} have TeX files.
  - {num_pdf_only} are PDF only.
- `fetch_papers.py` currently retrieves from arXiv or URL, but DOES NOT search local archives, DOES NOT normalize names properly, and DOES NOT merge `.tex` sources.

## Action Plan
We must rewrite the pipeline as requested in the implementation plan to encompass steps A-H.
"""
    with open("docs/paper_pipeline_audit.md", "w") as f:
        f.write(pipe_audit)
        
    print("Audits written to docs/")

if __name__ == '__main__':
    main()
