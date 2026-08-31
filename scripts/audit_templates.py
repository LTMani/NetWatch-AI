import os
import re

template_dir = "app/templates"
issues = []

for root, _, files in os.walk(template_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Check for missing backticks in map callbacks inside <script>
            script_blocks = re.findall(r'<script.*?>([\s\S]*?)</script>', content)
            for s in script_blocks:
                # Look for unquoted HTML table row lines like 'items.map(d => \n <tr>'
                if re.search(r'\.map\s*\(\s*\w+\s*=>\s*\n\s*<', s):
                    issues.append((path, "Unquoted HTML inside .map() callback"))

print("=== TEMPLATE SCRIPT AUDIT RESULTS ===")
if not issues:
    print("[PASS] All templates have clean JavaScript syntax!")
else:
    for path, issue in issues:
        print(f"[ISSUE] {path}: {issue}")
