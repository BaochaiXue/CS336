#!/usr/bin/env python3
import os
import glob
import json
from pathlib import Path

def scan_archives(base_dir):
    print(f"Scanning for local archives in {base_dir}...")
    extensions = ['.zip', '.tar', '.tar.gz', '.tgz', '.gz']
    
    found_archives = []
    
    for root, dirs, files in os.walk(base_dir):
        # Skip directories
        if '.git' in root or 'venv' in root or 'book/' in root or '.gemini' in root:
            continue
            
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                path = os.path.join(root, file)
                found_archives.append({
                    "filename": file,
                    "path": path,
                    "size": os.path.getsize(path)
                })
                
    return found_archives

def main():
    root_dir = "."
    archives = scan_archives(root_dir)
    
    os.makedirs("papers/metadata", exist_ok=True)
    out_path = "papers/metadata/local_archives_inventory.json"
    
    with open(out_path, "w") as f:
        json.dump(archives, f, indent=2)
        
    print(f"Found {len(archives)} potential archives.")
    print(f"Inventory written to {out_path}")

if __name__ == "__main__":
    main()
