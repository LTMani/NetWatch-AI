import os
import sys

EXTENSIONS = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.css': 'CSS',
    '.html': 'HTML/Jinja2',
    '.sql': 'SQL',
    '.json': 'JSON',
    '.md': 'Markdown',
    '.ini': 'Config'
}

EXCLUDED_DIRS = {'.git', '__pycache__', '.pytest_cache', 'venv', '.venv', 'node_modules', 'storage'}

def count_lines_in_repo(root_dir='.'):
    stats = {lang: {'files': 0, 'lines': 0, 'code': 0, 'comments': 0, 'blank': 0} for lang in set(EXTENSIONS.values())}
    total_files = 0
    total_lines = 0

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTENSIONS:
                lang = EXTENSIONS[ext]
                filepath = os.path.join(root, f)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                        lines = fp.readlines()
                        num_lines = len(lines)
                        blank = sum(1 for line in lines if not line.strip())
                        code = num_lines - blank

                        stats[lang]['files'] += 1
                        stats[lang]['lines'] += num_lines
                        stats[lang]['code'] += code
                        stats[lang]['blank'] += blank
                        total_files += 1
                        total_lines += num_lines
                except Exception as e:
                    pass

    print('='*72)
    print(f'{"NetWatch AI -- Codebase Metrics & Line of Code (LOC)":^72}')
    print('='*72)
    print(f'{"Language":<18} | {"Files":<8} | {"Total Lines":<12} | {"Code Lines":<12} | {"Blank":<8}')
    print('-'*72)
    for lang, data in sorted(stats.items(), key=lambda x: x[1]['lines'], reverse=True):
        if data['files'] > 0:
            print(f'{lang:<18} | {data["files"]:<8} | {data["lines"]:<12,d} | {data["code"]:<12,d} | {data["blank"]:<8,d}')
    print('='*72)
    print(f'{"TOTAL":<18} | {total_files:<8} | {total_lines:<12,d} | {sum(d["code"] for d in stats.values()):<12,d} | {sum(d["blank"] for d in stats.values()):<8,d}')
    print('='*72)

if __name__ == '__main__':
    count_lines_in_repo('.')
