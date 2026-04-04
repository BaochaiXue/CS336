#!/usr/bin/env python3
"""
fetch_papers.py — Download paper sources from arXiv and other URLs.

Usage:
    python scripts/fetch_papers.py [--tier-a-only] [--dry-run]

Reads papers/manifest.csv and downloads:
  - arXiv e-print sources (tar/gz) for arxiv papers
  - PDFs for non-arxiv papers
  - Records failures in papers/metadata/source_failures.json
"""

import csv
import json
import os
import re
import sys
import time
import tarfile
import gzip
import shutil
import zipfile
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime

# Configuration
MANIFEST_PATH = "papers/manifest.csv"
RAW_DIR = "papers/raw_archives"
EXTRACTED_DIR = "papers/extracted"
FAILURES_PATH = "papers/metadata/source_failures.json"

# Rate limiting: be kind to arxiv
ARXIV_DELAY = 4  # seconds between requests


def safe_filename(title):
    """Convert a paper title to a filesystem-safe directory name."""
    # Remove special characters, replace spaces with underscores
    safe = re.sub(r'[^\w\s-]', '', title.lower())
    safe = re.sub(r'[\s]+', '_', safe.strip())
    safe = safe[:80]  # Truncate
    return safe


def download_file(url, dest_path, timeout=60):
    """Download a file from URL to dest_path."""
    req = urllib.request.Request(url, headers={
        'User-Agent': 'CS336-Textbook-Project/1.0 (educational; research)'
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            with open(dest_path, 'wb') as f:
                shutil.copyfileobj(response, f)
        return True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        print(f"  ❌ Download failed: {e}")
        return False


def extract_archive(archive_path, dest_dir):
    """Extract a tar/gz/zip archive to dest_dir."""
    os.makedirs(dest_dir, exist_ok=True)
    
    try:
        if tarfile.is_tarfile(archive_path):
            with tarfile.open(archive_path, 'r:*') as tar:
                tar.extractall(path=dest_dir, filter='data')
            return True
        elif zipfile.is_zipfile(archive_path):
            with zipfile.ZipFile(archive_path, 'r') as z:
                z.extractall(path=dest_dir)
            return True
        else:
            # Try gzip (single file)
            try:
                with gzip.open(archive_path, 'rb') as gz:
                    content = gz.read()
                # It might be a single tex file
                out_path = os.path.join(dest_dir, 'paper.tex')
                with open(out_path, 'wb') as f:
                    f.write(content)
                return True
            except Exception:
                return False
    except Exception as e:
        print(f"  ❌ Extraction failed: {e}")
        return False


def process_paper(row, dry_run=False):
    """Process a single paper entry from the manifest."""
    title = row['display_title']
    primary_key = row['primary_key']
    arxiv_id = row.get('arxiv_id', '').strip()
    source_url = row.get('source_candidate_url', '').strip()
    url = row.get('url', '').strip()
    
    safe_name = safe_filename(title)
    if not safe_name:
        safe_name = safe_filename(primary_key)
    
    dest_dir = os.path.join(EXTRACTED_DIR, safe_name)
    
    # Skip if already extracted
    if os.path.isdir(dest_dir) and any(
        f.endswith('.tex') for f in os.listdir(dest_dir) if os.path.isfile(os.path.join(dest_dir, f))
    ):
        print(f"  ⏭️  Already extracted: {safe_name}")
        return {"status": "already_exists", "path": dest_dir}
    
    if dry_run:
        print(f"  🔍 Would download: {title}")
        if arxiv_id:
            print(f"      Source: https://arxiv.org/e-print/{arxiv_id}")
        return {"status": "dry_run"}
    
    # Determine download URL
    download_url = None
    source_type = "unknown"
    
    if arxiv_id:
        download_url = f"https://arxiv.org/e-print/{arxiv_id}"
        source_type = "arxiv_eprint"
    elif source_url:
        download_url = source_url
        source_type = "direct_source"
    elif url:
        download_url = url
        source_type = "primary_url"
    
    if not download_url:
        return {"status": "no_url", "title": title}
    
    # Download
    os.makedirs(RAW_DIR, exist_ok=True)
    archive_ext = ".tar.gz" if source_type == "arxiv_eprint" else ".pdf"
    archive_path = os.path.join(RAW_DIR, f"{safe_name}{archive_ext}")
    
    print(f"  ⬇️  Downloading: {download_url}")
    success = download_file(download_url, archive_path)
    
    if not success:
        return {"status": "download_failed", "url": download_url, "title": title}
    
    # For arXiv sources, try to extract
    if source_type == "arxiv_eprint":
        print(f"  📦 Extracting: {archive_path}")
        if extract_archive(archive_path, dest_dir):
            # Delete archive after successful extraction
            os.remove(archive_path)
            print(f"  ✅ Extracted to: {dest_dir}")
            return {"status": "extracted", "path": dest_dir}
        else:
            return {"status": "extraction_failed", "archive": archive_path, "title": title}
    else:
        # For PDFs, just move to extracted dir
        os.makedirs(dest_dir, exist_ok=True)
        pdf_dest = os.path.join(dest_dir, f"{safe_name}.pdf")
        shutil.move(archive_path, pdf_dest)
        return {"status": "pdf_only", "path": pdf_dest}
    
    # Rate limit for arxiv
    if arxiv_id:
        time.sleep(ARXIV_DELAY)


def main():
    dry_run = '--dry-run' in sys.argv
    tier_a_only = '--tier-a-only' in sys.argv
    
    print("=" * 60)
    print("CS336 Paper Fetch Pipeline")
    print(f"  Manifest: {MANIFEST_PATH}")
    print(f"  Mode: {'DRY RUN' if dry_run else 'DOWNLOAD'}")
    print(f"  Scope: {'Tier A only' if tier_a_only else 'All papers'}")
    print("=" * 60)
    
    # Load manifest
    with open(MANIFEST_PATH, 'r') as f:
        reader = csv.DictReader(f)
        papers = list(reader)
    
    # Filter if tier A only
    if tier_a_only:
        papers = [p for p in papers if p.get('in_cs336_2025', '').lower() == 'true']
    
    print(f"\nProcessing {len(papers)} papers...\n")
    
    failures = []
    stats = {"extracted": 0, "pdf_only": 0, "already_exists": 0, 
             "download_failed": 0, "extraction_failed": 0, "no_url": 0, "dry_run": 0}
    
    for i, paper in enumerate(papers, 1):
        title = paper['display_title']
        print(f"[{i}/{len(papers)}] {title}")
        
        result = process_paper(paper, dry_run=dry_run)
        status = result.get("status", "unknown")
        stats[status] = stats.get(status, 0) + 1
        
        if status in ("download_failed", "extraction_failed", "no_url"):
            failures.append({
                "title": title,
                "primary_key": paper['primary_key'],
                "status": status,
                "details": result,
                "timestamp": datetime.now().isoformat(),
            })
        
        # Rate limit for arxiv
        if paper.get('arxiv_id', '').strip() and not dry_run:
            time.sleep(ARXIV_DELAY)
    
    # Write failures
    with open(FAILURES_PATH, 'w') as f:
        json.dump({"failures": failures, "last_updated": datetime.now().isoformat()}, 
                  f, indent=2)
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary:")
    for k, v in stats.items():
        if v > 0:
            print(f"  {k}: {v}")
    print(f"  failures logged: {len(failures)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
