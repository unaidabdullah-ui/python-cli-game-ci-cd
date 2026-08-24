# ---- Build stage: resolve & install dependencies ----
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt ./

# Install dependencies into a known directory
RUN pip install --no-cache-dir \
    --target=/install \
    -r requirements.txt

# ---- Runtime stage: minimal image, non-root user ----
FROM python:3.12-slim

RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /install /usr/local/lib/python3.12/site-packages

COPY game.py ./

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN chown -R appuser:appuser /app

USER appuser

LABEL org.opencontainers.image.title="guess-game" \
      org.opencontainers.image.description="CLI number guessing game" \
      org.opencontainers.image.source="https://github.com/unaidabdullah-ui/python-cli-game-ci-cd"

CMD ["python", "game.py"]
