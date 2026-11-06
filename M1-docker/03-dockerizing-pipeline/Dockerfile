FROM python:3.13.11-slim

COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock .python-version README.md ./
COPY src/ ./src/

RUN uv sync --locked

COPY pipeline/pipeline.py pipeline.py

ENTRYPOINT ["uv", "run", "python", "pipeline.py"]
