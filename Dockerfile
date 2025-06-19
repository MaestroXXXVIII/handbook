FROM python:3.12.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/src:$PYTHONPATH

RUN apt-get update && apt-get install -y curl
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
COPY uv.lock pyproject.toml /app/

RUN uv sync --locked

COPY . /app

RUN sed -i '1s|^.*$|#!/app/.venv/bin/python|' /app/.venv/bin/alembic
