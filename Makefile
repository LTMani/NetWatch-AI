.PHONY: install build run test clean lint

install:
	pip install -r requirements.txt

build:
	python -m py_compile run.py app.py main.py

run:
	python run.py

test:
	python -m pytest

lint:
	python scripts/verify_all_subsets.py

clean:
	python -c "import shutil, pathlib; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"
