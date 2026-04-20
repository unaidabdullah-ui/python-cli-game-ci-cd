![CI](https://img.shields.io/badge/CI-Jenkins-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Tests](https://img.shields.io/badge/Tests-Pytest-green)


# 🚀 Python CLI Game with CI/CD & Docker

## 📌 Overview

This project is a simple Python-based CLI game ("Guess the Number") enhanced with **DevOps practices** like containerization, automated testing, and CI/CD pipelines using Jenkins.

The goal of this project is to demonstrate how even a small application can be structured and deployed using real-world engineering workflows.

---

## 🧠 Tech Stack

* Python
* Docker
* Docker Compose
* Jenkins (CI/CD)
* Pytest (Testing)

---

## ⚙️ Features

* 🎮 Interactive CLI number guessing game
* 🧪 Automated testing using Pytest
* 🐳 Dockerized application for consistent environments
* 🔁 CI/CD pipeline using Jenkins
* 📦 Dependency management via requirements.txt

---

## 🏗️ Project Structure

```
.
├── game.py              # Main game logic
├── test_game.py         # Unit tests
├── requirements.txt     # Dependencies
├── Dockerfile           # Container setup
├── docker-compose.yml   # Multi-container setup
├── Jenkinsfile          # CI/CD pipeline
└── README.md
```

---

## 🛠️ Setup & Run

### 🔹 Run Locally

```bash
git clone https://github.com/your-username/python-cli-game-ci-cd.git
cd python-cli-game-ci-cd

pip install -r requirements.txt
python game.py
```

---

### 🔹 Run with Docker

```bash
docker build -t guess-game .
docker run -it guess-game
```

---

### 🔹 Run with Docker Compose

```bash
docker-compose up --build
```

---

## 🔁 CI/CD Pipeline (Jenkins)

Pipeline stages:

1. Clone repository
2. Install dependencies
3. Run tests (pytest)
4. Build Docker image
5. Deploy container

---

## 📈 What This Project Demonstrates

* Writing testable Python code
* Setting up CI/CD pipelines
* Containerizing applications using Docker
* Structuring projects like real-world systems

---

## 🚀 Future Improvements

* Add REST API (Flask/FastAPI)
* Deploy on AWS EC2
* Add GitHub Actions pipeline
* Add frontend UI (React)

---

## 👨‍💻 Author

Unaid Abdullah
