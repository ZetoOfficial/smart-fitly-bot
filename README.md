# Smart Fitly Bot

Бэкенд для Telegram Mini App, который помогает тренерам вести клиентов: дневники питания и активности, еженедельные чекины и ежемесячные замеры.

- **Стек:** Python 3.13, FastAPI, SQLAlchemy 2, Alembic, PostgreSQL, uvicorn.
- **Доменные сущности:** User (Trainer/Student), Group/GroupUser, Daily, Goal, Measurement, Checkin.
- **Структура:** код лежит в `backend/app` (main, config, db, models, api, services, schemas); миграции в `alembic/`; тесты в `backend/tests`.

## Подготовка окружения

1. Установите зависимости: `pip install -r requirements.txt` или `uv sync`.
2. Поднимите БД (локально или через Docker).
3. Создайте `.env` при необходимости, ключевые переменные:
   - `DATABASE_URL` — строка подключения к Postgres (по умолчанию `postgresql+psycopg://smartfitly:smartfitly@localhost:5432/smartfitly`).
   - `TZ` или `APP_ENV` при желании переопределить время или окружение.

## Локальный запуск

- Прямой запуск: `uv run uvicorn app.main:app --reload --app-dir backend`
- Docker Compose: `docker compose up --build` (поднимет Postgres и backend на `:8000`).
- Здоровье сервиса: `GET /api/v1/health/`.

## Миграции

- Создать ревизию: `alembic revision --autogenerate -m "message"`
- Применить: `alembic upgrade head`

## Тесты и качество

- Запуск тестов: `pytest` (конфигурация в `pyproject.toml`, тесты в `backend/tests`).
- Линт/типизация: `uv run ruff check backend` и `uv run mypy backend`.

## Дополнительно

- JSON-ответы придерживаются camelCase, Python-код — snake_case.
- При изменении моделей не забывайте обновлять Alembic миграции.
