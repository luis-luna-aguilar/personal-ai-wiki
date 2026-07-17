#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

def verify_links(wiki_dir):
    broken_links = []
    wiki_path = Path(wiki_dir).resolve()
    
    if not wiki_path.exists():
        print(f"Error: Wiki directory not found at {wiki_path}")
        sys.exit(1)
        
    # Regex to find markdown links: [text](link)
    # This specifically ignores image links ![alt](url) by checking for an optional leading ! but we actually
    # want to verify image links too.
    # We will match both [text](url) and ![alt](url)
    link_pattern = re.compile(r'\[(?:[^\]]*)\]\(([^)]+)\)')
    
    files_scanned = 0
    links_scanned = 0

    for md_file in wiki_path.rglob('*.md'):
        files_scanned += 1
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for line_num, line in enumerate(lines, 1):
            for match in link_pattern.finditer(line):
                url = match.group(1).strip()
                
                # Ignore external URLs
                if url.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                    continue
                # Ignore pure intra-page anchors
                if url.startswith('#'):
                    continue
                    
                links_scanned += 1
                    
                # Remove anchor from url for file existence check (e.g., file.md#section)
                file_path_part = url.split('#')[0]
                
                if not file_path_part:
                    continue
                
                # Resolve relative path
                # The link is relative to the directory of the current md_file
                target_path = (md_file.parent / file_path_part).resolve()
                
                if not target_path.exists():
                    broken_links.append({
                        'source_file': str(md_file.relative_to(wiki_path.parent)),
                        'line': line_num,
                        'broken_target': url,
                        'resolved_path': str(target_path)
                    })
                    
    return broken_links, files_scanned, links_scanned

if __name__ == '__main__':
    # Default to the 'wiki' and 'indexes' directories 
    # Since our root has /wiki, /indexes (wait, we moved indexes into wiki! Let's check.)
    # In the README, indexes are in /wiki/indexes.
    project_root = Path(__file__).resolve().parent.parent.parent
    wiki_dir = project_root / 'wiki'
    
    print(f"🔍 Scanning wiki directory: {wiki_dir.relative_to(project_root)}")
    broken, files_count, links_count = verify_links(wiki_dir)
    
    print(f"Scanned {files_count} files and {links_count} internal links.")
    
    if broken:
        print(f"\n❌ Found {len(broken)} broken link(s):\n")
        for b in broken:
            print(f"File: {b['source_file']}:{b['line']}")
            print(f"  Broken Link: {b['broken_target']}")
            print("-" * 40)
        sys.exit(1)
    else:
        print("\n✅ All links are valid! The graph is fully connected.")
        sys.exit(0)
