FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=backend

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml ./pyproject.toml
COPY backend ./backend
COPY alembic ./alembic
COPY alembic.ini ./alembic.ini

RUN uv sync --no-dev

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "backend"]
