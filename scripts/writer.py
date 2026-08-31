import os
from pathlib import Path

BASE = Path('t:/Git Project/netwatch-ai')

def write(path, content):
    p = BASE / path
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'[+] Wrote {path} ({len(content.splitlines())} lines)')
