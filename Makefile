PYTHONPATH ?= backend

.PHONY: install run format lint typecheck test migrate revision

install:
	uv sync

run:
	PYTHONPATH=$(PYTHONPATH) uv run uvicorn app.main:app --reload --app-dir backend

format:
	uv run ruff format backend

lint:
	uv run ruff check backend

typecheck:
	uv run mypy backend

test:
	PYTHONPATH=$(PYTHONPATH) uv run pytest

migrate:
	docker compose exec backend env DATABASE_URL=postgresql+psycopg://smartfitly:smartfitly@db:5432/smartfitly uv run alembic upgrade head

# Usage: make revision message="Your migration message"
revision:
	docker compose exec backend env DATABASE_URL=postgresql+psycopg://smartfitly:smartfitly@db:5432/smartfitly uv run alembic revision --autogenerate -m "$(message)"
