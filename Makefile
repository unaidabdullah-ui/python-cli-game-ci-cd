.PHONY: install lint format typecheck test build run clean

install:
	pip install -r requirements-dev.txt

lint:
	flake8 .
	black --check .
	isort --check-only .

format:
	black .
	isort .

typecheck:
	mypy game.py

test:
	pytest

build:
	docker build -t guess-game:latest .

run:
	docker compose up --build

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache htmlcov .coverage coverage.xml test-results.xml
