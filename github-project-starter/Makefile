.PHONY: help run test lint format docker-build docker-run clean

help:
	@echo "Available commands:"
	@echo "  make run          - Run development server"
	@echo "  make test         - Run test suite with coverage"
	@echo "  make lint         - Check code formatting & linting"
	@echo "  make format       - Auto-format codebase"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-run   - Run Docker container"
	@echo "  make clean        - Remove build artifacts and cache"

run:
	uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest --cov=src --cov-report=term-missing

lint:
	ruff check .
	black --check .

format:
	ruff check --fix .
	black .

docker-build:
	docker build -t fastapi-starter:latest .

docker-run:
	docker run -p 8000:8000 fastapi-starter:latest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf .coverage htmlcov
