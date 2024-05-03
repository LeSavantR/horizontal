.ONESHELL:

.DEFAULT_GOAL := run

VENV := .venv
PYTHON := $(VENV)/bin/python3
ENV := $(VENV)/bin/activate
PIP := $(VENV)/bin/pip
POETRY_ENV := POETRY_VIRTUALENVS_IN_PROJECT
PGM = $(PIP)

DEBUG := ${DEBUG}

all: clean run

build: requirements.txt
	@echo "Creating Virtual Environment..."
	@python3 -m venv $(VENV)
	@echo "Environment Created!..."
	@if [ $(PGM) = "poetry" ]; then \
		echo "Using $(PGM)\n"; \
		export $(POETRY_ENV)=true; \
		$(PGM) install; \
	else \
		echo "Using $(PGM)\n"; \
		$(PGM) install -r requirements.txt; \
	fi

run: build
	@export PYTHONDONTWRITEBYTECODE=true
	@$(PYTHON) init.py

clean:
	@echo "Cleaning..."
	@rm -rf __pycache__ */__pycache__
	@rm -rf $(VENV)
	@echo "Cleaned!..."

.PHONY: build run clean
