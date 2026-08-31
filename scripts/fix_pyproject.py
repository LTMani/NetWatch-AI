content = """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "netwatch-ai"
version = "1.0.0"
description = "AI-powered enterprise network usage, discovery, and intelligence platform"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "Flask>=3.0.0",
    "SQLAlchemy>=2.0.0",
    "PyJWT>=2.8.0",
    "reportlab>=4.0.0",
    "cryptography>=42.0.0",
    "pytest>=8.0.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
"""

with open("pyproject.toml", "w", encoding="utf-8") as f:
    f.write(content)

print("[+] pyproject.toml fixed without BOM!")
