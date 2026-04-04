#!/usr/bin/env python3
import json
import csv
import os

def main():
    print("Building indexes and updating manifest...")
    manifest_path = "papers/manifest.csv"
    manifest_json_path = "papers/manifest.json"
    merge_results_path = "papers/metadata/merge_results.json"
    rename_map_path = "papers/metadata/folder_rename_map.json"
    
    with open(manifest_path, 'r') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        papers = list(reader)
        
    merge_results = {}
    if os.path.exists(merge_results_path):
        with open(merge_results_path, 'r') as f:
            merge_results = json.load(f)
            
    rename_map = {}
    if os.path.exists(rename_map_path):
        with open(rename_map_path, 'r') as f:
            rename_map = json.load(f)
            
    # Add new fields if they don't exist
    new_fields = ['canonical_title', 'legal_folder_name', 'local_folder', 
                  'merged_tex_path', 'source_status', 'source_type', 'used_local_archive']
    for nf in new_fields:
        if nf not in fields:
            fields.append(nf)
            
    # Update data
    link_rows = []
    
    # We need a reverse lookup for rename map to figure out the canonical folder
    # from the original key/slug. But we know normalize_papers used the canonical title directly.
    # We can reconstruct it or match.
    
    import unicodedata
    import re
    def safe_canonical_name(title, pk=""):
        if not title: title = pk
        s = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('ascii')
        s = re.sub(r'[<>:"/\\|?*]', '', s)
        s = re.sub(r'\span+', ' ', s)
        s = re.sub(r'[\s\-]+', '_', s)
        s = re.sub(r'_+', '_', s)
        s = s.strip('_ .').lower()[:120]
        return s
        
    for p in papers:
        title = p.get('display_title', '')
        pk = p.get('primary_key', '')
        canon = safe_canonical_name(title, pk)
        
        # update manifest
        p['canonical_title'] = title
        p['legal_folder_name'] = canon
        p['local_folder'] = f"papers/normalized/{canon}"
        
        status_info = merge_results.get(canon, {})
        status = status_info.get('status', 'source_unavailable')
        p['source_status'] = status
        
        if status == 'success':
            p['merged_tex_path'] = status_info.get('merged_path', '')
            p['source_type'] = 'tex_source'
        elif status == 'pdf_only':
            p['merged_tex_path'] = ''
            p['source_type'] = 'pdf_only'
            # Also mark pdf path locally if wanted
        else:
            p['merged_tex_path'] = ''
            p['source_type'] = 'source_unavailable'
            
        p['used_local_archive'] = 'false'
        if 'arxiv_id' not in p: p['arxiv_id'] = ''
        if 'notes' not in p: p['notes'] = ''
        
        # Index row
        link_rows.append({
            'canonical_title': title,
            'authors': p.get('organization', ''),
            'year': p.get('date', '')[:4] if p.get('date') else '',
            'primary_key': pk,
            'official_course_relevance': "2026 " + p.get('topic_hint', ''),
            'source_url': p.get('url', ''),
            'arxiv_abs_url': f"https://arxiv.org/abs/{p['arxiv_id']}" if p['arxiv_id'] else '',
            'arxiv_eprint_url': f"https://arxiv.org/e-print/{p['arxiv_id']}" if p['arxiv_id'] else '',
            'official_pdf_url': p.get('source_candidate_url', ''),
            'local_folder': p['local_folder'],
            'merged_tex_path': p['merged_tex_path'],
            'status': p['source_type']
        })
        
    # Write updated CSV
    with open(manifest_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(papers)
        
    # Write updated JSON
    with open(manifest_json_path, 'w') as f:
        json.dump(papers, f, indent=2)
        
    # Write Link Index CSV
    link_fields = list(link_rows[0].keys())
    with open("papers/link_index.csv", 'w') as f:
        writer = csv.DictWriter(f, fieldnames=link_fields)
        writer.writeheader()
        writer.writerows(link_rows)
        
    # Write Link Index MD
    md = "# CS336 Paper Source Index\n\n"
    md += "| Title | Year | Folder | TeX Source | Status |\n"
    md += "|---|---|---|---|---|\n"
    for r in link_rows:
        md += f"| {r['canonical_title']} | {r['year']} | `{r['local_folder']}` | `{r['merged_tex_path']}` | {r['status']} |\n"
        
    with open("papers/link_index.md", 'w') as f:
        f.write(md)
        
    print("Finished updating manifest and building link_index.md/csv.")

if __name__ == "__main__":
    main()
