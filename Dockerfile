# ---- Build stage: resolve & install dependencies ----
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --user -r requirements.txt

# ---- Runtime stage: minimal image, non-root user ----
FROM python:3.12-slim

RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

COPY --from=builder /root/.local /home/appuser/.local
COPY game.py ./

ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER appuser

LABEL org.opencontainers.image.title="guess-game" \
      org.opencontainers.image.description="CLI number guessing game" \
      org.opencontainers.image.source="https://github.com/unaidabdullah-ui/python-cli-game-ci-cd"

CMD ["python", "game.py"]
