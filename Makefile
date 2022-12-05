help:
	@echo "install - install a virtualenv for development and deployment"
	@echo "fmt - format source code with black"
	@echo "test - run unit tests"
	@echo "deploy - deploy all your pipelines"
	@echo "clean - remove build, test, and Python artifacts locally"

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: venv
venv:
	@test -d "venv" || mkdir -p "venv"
	@rm -Rf "venv"
	@python3 -m venv "venv"

install: upgrade-pip install-tests

upgrade-pip:
	$(PIP) install --upgrade pip setuptools

install-tests:
	$(PIP) install -r tests/requirements.txt

fmt:
	$(PIP) install black
	$(PYTHON) -m black .

test:
	export PYTHONPATH=".:./src" && \
	$(PYTHON) -m pytest tests/

clean:
	@rm -fr .tox/
	@rm -fr .venv/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name "*.py[co]" -o -name .pytest_cache -exec rm -rf {} +
	@find . -name '*.egg' -exec rm -f {} +
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
