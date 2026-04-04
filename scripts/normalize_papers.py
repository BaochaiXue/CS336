#!/usr/bin/env python3
import os
import re
import csv
import json
import shutil
import unicodedata

def safe_canonical_name(title, primary_key=""):
    """
    Generate normalized folder name from paper title:
    - ASCII transliteration
    - Fold space to _
    - Limit 120
    - Remove <>:"/\|?*
    - Strip trailing dots/spaces
    """
    if not title:
        title = primary_key
        
    s = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('ascii')
    
    # Remove bad chars
    s = re.sub(r'[<>:"/\\|?*]', '', s)
    # Fold whitespaces/newlines/tabs to single space
    s = re.sub(r'\span+', ' ', s)
    # Replace spaces and common boundary chars with underscore
    s = re.sub(r'[\s\-]+', '_', s)
    # General clean multiple underscores
    s = re.sub(r'_+', '_', s)
    
    s = s.strip('_ .').lower()
    
    # Truncate
    s = s[:120]
    return s

def main():
    print("Normalizing paper directories...")
    
    manifest_path = "papers/manifest.csv"
    extracted_dir = "papers/extracted"
    normalized_dir = "papers/normalized"
    
    if not os.path.exists(extracted_dir):
        print("No extracted directory found. Exiting.")
        return
        
    os.makedirs(normalized_dir, exist_ok=True)
    os.makedirs("papers/metadata", exist_ok=True)
    
    # Load manifest
    papers = []
    with open(manifest_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            papers.append(row)
            
    # Key mapping
    rename_map = {}
    
    # Existing unnormalized directories
    existing_dirs = [d for d in os.listdir(extracted_dir) if os.path.isdir(os.path.join(extracted_dir, d))]
    
    for p in papers:
        title = p.get('display_title', '')
        pk = p.get('primary_key', '')
        
        canonical = safe_canonical_name(title, pk)
        
        # We need to find if this paper was already extracted under previous slug
        # Legacy script used: `safe = re.sub(r'[^\w\s-]', '', title.lower()); safe = re.sub(r'[\s]+', '_', safe.strip())[:80]` or pk
        old_safe = re.sub(r'[^\w\s-]', '', title.lower())
        old_safe = re.sub(r'[\s]+', '_', old_safe.strip())[:80]
        if not old_safe:
            old_safe = re.sub(r'[^\w\s-]', '', pk.lower())
            old_safe = re.sub(r'[\s]+', '_', old_safe.strip())[:80]
            
        old_path_candidate_1 = os.path.join(extracted_dir, old_safe)
        old_path_candidate_2 = os.path.join(extracted_dir, pk)
        
        source_path = None
        if os.path.exists(old_path_candidate_1):
            source_path = old_path_candidate_1
        elif os.path.exists(old_path_candidate_2):
            source_path = old_path_candidate_2
            
        if source_path:
            dest_path = os.path.join(normalized_dir, canonical)
            
            if os.path.exists(dest_path):
                # Avoid moving if already there
                pass
            else:
                shutil.move(source_path, dest_path)
                rename_map[source_path] = dest_path
                print(f"Moved: {os.path.basename(source_path)} -> {canonical}")
        
    map_p = "papers/metadata/folder_rename_map.json"
    with open(map_p, 'w') as f:
        json.dump(rename_map, f, indent=2)
        
    print(f"Renamed {len(rename_map)} folders. Map written to {map_p}.")

if __name__ == "__main__":
    main()
