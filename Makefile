PYTHON ?= python3
VENV := .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

.PHONY: venv install run test lint format docker-up docker-down clean

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	$(VENV)/bin/uvicorn app.main:app --app-dir backend --reload --host 0.0.0.0

test:
	$(PY) -m pytest

lint:
	$(PY) -m ruff check .

format:
	$(PY) -m ruff format .

docker-up:
	docker compose -f infrastructure/docker/docker-compose.yml up -d

docker-down:
	docker compose -f infrastructure/docker/docker-compose.yml down

clean:
	rm -rf $(VENV) .pytest_cache .ruff_cache
