.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os
import re
import sys
import webbrowser
from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


define generate_footer
\n.. toctree::
\n\t:maxdepth: 1
\n\t:caption: Getting Started
\n
\n\tinstallation
\n\texamples
\n
\n.. toctree::
\n\t:maxdepth: 1
\n\t:caption: Help & Reference
\n
\n\thistory
\n\tcontributing
\n\tauthors
\n\tlicense
endef
export INDEX_FOOTER=$(value generate_footer)

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

lint: ## check style with flake8
	pre-commit run --all-files

docs: ## generate Sphinx HTML documentation, including API docs
	sed -n '1,/Installation/{/Installation/!p;}' README.rst > docs/source/index.rst
	echo $$INDEX_FOOTER >> docs/source/index.rst
	sed -i  '' -e 's/\t/    /g' docs/source/index.rst
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/build/html/index.html
