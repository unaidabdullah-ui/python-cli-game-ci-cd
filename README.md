![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Tests](https://img.shields.io/badge/Tests-Pytest-green)
![Lint](https://img.shields.io/badge/Lint-flake8%20%7C%20black%20%7C%20isort-yellow)
![CI](https://img.shields.io/badge/CI%2FCD-Jenkins-red)

# 🚀 Python CLI Game with CI/CD & Docker

## 📌 Overview

A simple Python CLI ("Guess the Number") game, structured and deployed the way a
real service would be: testable code, a linted and type-checked codebase,
a multi-stage Docker build, and a Jenkins pipeline that gates every merge.

---

## 🧠 Tech Stack

* Python 3.12
* Docker / Docker Compose (multi-stage, non-root runtime image)
* Jenkins (CI/CD)
* Pytest + coverage
* flake8, black, isort, mypy

---

## ⚙️ Features

* 🎮 Interactive CLI number guessing game (configurable range and attempt limit)
* 🧪 Unit-tested game logic, decoupled from I/O for fast, deterministic tests
* 🐳 Multi-stage Docker build running as a non-root user
* 🔁 Jenkins pipeline: lint → type-check → test (with coverage) → build → push → deploy
* 🧹 Enforced style via flake8 / black / isort, static typing via mypy
* 📦 Separate runtime (`requirements.txt`) and dev/CI (`requirements-dev.txt`) dependencies

---

## 🏗️ Project Structure

```
.
├── game.py                 # Game logic (testable pure functions) + CLI entrypoint
├── test_game.py             # Unit tests (pytest, mocked I/O)
├── requirements.txt          # Runtime dependencies
├── requirements-dev.txt      # Dev/CI tooling (pytest, flake8, black, isort, mypy)
├── Dockerfile                # Multi-stage, non-root runtime image
├── docker-compose.yml        # Local run configuration
├── .dockerignore
├── .gitignore
├── pyproject.toml            # black / isort / pytest / mypy config
├── setup.cfg                 # flake8 config
├── Jenkinsfile                # CI/CD pipeline
└── README.md
```

---

## 🛠️ Setup & Run

### 🔹 Run locally

```bash
git clone https://github.com/unaidabdullah-ui/python-cli-game-ci-cd.git
cd python-cli-game-ci-cd

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
python game.py

```

Optional flags:

```bash
python game.py --low 1 --high 100 --max-attempts 10
```

### 🔹 Run with Docker

```bash
docker build -t guess-game .
docker run -it guess-game
```

### 🔹 Run with Docker Compose

```bash
docker compose up --build
```

---

## 🧪 Development

```bash
# Lint
flake8 .

# Check formatting
black --check .

# Check import sorting
isort --check-only .

# Auto-format code
black .
isort .

# Type checking
mypy game.py

# Run tests
pytest
```

---

## 🔁 CI/CD Pipeline (Jenkins)

Stages, run on every build:

1. **Checkout** — pull source
2. **Setup Environment** — create a venv, install `requirements-dev.txt`
3. **Lint** — flake8, black, isort (fails the build on violations)
4. **Type Check** — mypy
5. **Test** — pytest with coverage, JUnit results published to Jenkins
6. **Build** — Docker image tagged with the build number and `latest`
7. **Push** *(main branch only)* — push image to the registry
8. **Deploy** *(main branch only)* — `docker compose up -d --build`

---

## 📈 What This Project Demonstrates

* Separating pure logic from I/O for real unit testability
* A CI pipeline that actually gates on lint/type/test failures, not just echoes
* A production-style multi-stage, non-root Docker image
* Reproducible tooling via pinned dev dependencies and shared config files

---

## 🚀 Future Improvements

* Add REST API (Flask/FastAPI)
* Deploy on AWS EC2 / ECS
* Add a GitHub Actions mirror of the Jenkins pipeline for open-source contributors

---

## 👨‍💻 Author

Unaid Abdullah
