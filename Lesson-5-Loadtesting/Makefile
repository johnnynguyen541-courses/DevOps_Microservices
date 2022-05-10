setup:
	python3 -m virtualenv venv

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
    #python -m pytest -vv --cov=myrepolib tests/*.py
    #python -m pytest --nbval notebook.ipynb


lint:
	hadolint Dockerfile
	pylint --disable=R,C,W1203 *.py

all: install lint test