#!/usr/bin/env python3
import os
import re
import json

VERBATIM_ENVS = ['verbatim', 'lstlisting', 'minted', 'algorithm', 'algorithmic']

def find_main_tex(folder):
    tex_files = []
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith('.tex'):
                tex_files.append(os.path.join(root, f))
    
    candidates = []
    for f in tex_files:
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                content = fp.read()
                if '\\documentclass' in content:
                    # Ignore supplementaries usually marked by 'supp', 'appendix' in name
                    if 'supp' in f.lower() or 'app' in f.lower():
                        continue
                    candidates.append((f, len(content)))
        except:
            pass
            
    if not candidates:
        if tex_files:
            # Fallback to largest file
            tex_files.sort(key=lambda x: os.path.getsize(x), reverse=True)
            return tex_files[0]
        return None
        
    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[0][0]

def resolve_include(line, current_dir):
    match = re.search(r'\\(?:input|include)\{([^}]+)\}', line)
    if match:
        target = match.group(1)
        if not target.endswith('.tex'):
            target += '.tex'
        target_path = os.path.join(current_dir, target)
        if os.path.exists(target_path):
            with open(target_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
    return None

def merge_and_clean_tex(main_tex_path):
    basedir = os.path.dirname(main_tex_path)
    
    with open(main_tex_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # MAX 5 depth recursion for includes
    for _ in range(5):
        lines = content.split('\n')
        new_lines = []
        changed = False
        for line in lines:
            if '\\input{' in line or '\\include{' in line:
                # ignore commented includes
                if line.lstrip().startswith('%'):
                    new_lines.append(line)
                    continue
                included = resolve_include(line, basedir)
                if included is not None:
                    new_lines.extend(included.split('\n'))
                    changed = True
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        content = '\n'.join(new_lines)
        if not changed:
            break

    # Clean comments safely
    lines = content.split('\n')
    cleaned_lines = []
    in_verbatim = False
    
    for line in lines:
        env_match = re.search(r'\\(?:begin|end)\{([^}]+)\}', line)
        if env_match:
            env = env_match.group(1)
            if env in VERBATIM_ENVS:
                if '\\begin' in line:
                    in_verbatim = True
                else:
                    in_verbatim = False
        
        if in_verbatim:
            cleaned_lines.append(line)
            continue
            
        # Strip trailing comments if not escaped \%
        # Simplified logic: remove whole line comments
        stripped = line.strip()
        if stripped.startswith('%'):
            continue
            
        # Try to strip inline trailing comments: somewhat dangerous, let's keep it mostly to full line
        if '%' in line:
            # find first % that is not preceded by \
            # If valid, cut it there
            idx = line.find('%')
            while idx != -1:
                if idx == 0 or line[idx-1] != '\\':
                    line = line[:idx]
                    break
                idx = line.find('%', idx+1)
                
        if line.strip() == '':
            # Manage excessive blank lines
            if len(cleaned_lines) > 0 and cleaned_lines[-1].strip() == '':
                continue
                
        cleaned_lines.append(line)
        
    return '\n'.join(cleaned_lines)

def main():
    print("Merging TeX files...")
    normalized_dir = "papers/normalized"
    merged_dir = "papers/merged_tex"
    os.makedirs(merged_dir, exist_ok=True)
    os.makedirs("papers/metadata", exist_ok=True)
    
    if not os.path.exists(normalized_dir):
        print("No papers found in normalized directory.")
        return

    results = {}
    
    for folder in os.listdir(normalized_dir):
        p = os.path.join(normalized_dir, folder)
        if not os.path.isdir(p): continue
        
        main_tex = find_main_tex(p)
        if main_tex:
            try:
                merged_txt = merge_and_clean_tex(main_tex)
                out_local = os.path.join(p, "merged_paper.tex")
                out_global = os.path.join(merged_dir, f"{folder}.tex")
                
                with open(out_local, 'w', encoding='utf-8') as f:
                    f.write(merged_txt)
                with open(out_global, 'w', encoding='utf-8') as f:
                    f.write(merged_txt)
                    
                results[folder] = {
                    "status": "success",
                    "main_tex": main_tex,
                    "merged_path": out_global
                }
                print(f"Merged: {folder}")
            except Exception as e:
                results[folder] = {
                    "status": "error",
                    "error": str(e)
                }
                print(f"Failed to merge {folder}: {e}")
        else:
            # Check if PDF only
            pdf_files = [f for f in os.listdir(p) if f.endswith('.pdf')]
            if pdf_files:
                results[folder] = {
                    "status": "pdf_only",
                    "pdf_file": os.path.join(p, pdf_files[0])
                }
            else:
                results[folder] = {
                    "status": "no_source"
                }
                
    with open("papers/metadata/merge_results.json", 'w') as f:
        json.dump(results, f, indent=2)
        
    print(f"Done merging. Processed {len(results)} directories.")

if __name__ == "__main__":
    main()
