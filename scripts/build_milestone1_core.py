import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def write_file(rel_path, content):
    full_path = BASE_DIR / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, w, encoding=utf-8) as f:
        f.write(content.strip() + \n)
    print(f [+] Created {rel_path} ({len(content.splitlines())} lines))

print(Building Milestone 1: Core Foundation, Models & Auth...)
