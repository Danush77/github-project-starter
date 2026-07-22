# Production-Ready FastAPI Microservice Starter

[![CI Pipeline](https://github.com/your-username/fastapi-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/fastapi-starter/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A production-grade, enterprise-ready Python microservice boilerplate built with **FastAPI**, **Pydantic v2**, **Docker**, **Pytest**, and **GitHub Actions**.

---

## ✨ Features

- **⚡ FastAPI Framework**: Modern, fast (high-performance) web framework for building APIs with Python.
- **🛡️ Pydantic V2**: Strict data validation, settings management, and automated OpenAPI documentation.
- **🐳 Containerized Deployment**: Production-optimized `Dockerfile` and `docker-compose.yml`.
- **🧪 Automated Testing**: Comprehensive unit & integration testing suite powered by `pytest` and `httpx`.
- **🔄 CI/CD Pipelines**: Pre-configured GitHub Actions workflows for continuous integration, code linting, and automated testing.
- **📦 Clean Architecture**: Modular structure designed for scalability, maintainability, and clean separation of concerns.
- **📋 Standard GitHub Templates**: Bug reports, feature request templates, and issue management setup.

---

## 📁 Repository Structure

```
├── .github/
│   ├── ISSUE_TEMPLATE/       # GitHub issue templates
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/            # GitHub Actions CI/CD pipelines
│       ├── ci.yml
│       └── release.yml
├── docs/                     # Project architecture & detailed documentation
│   └── ARCHITECTURE.md
├── src/                      # Source code
│   └── app/
│       ├── api/              # API endpoints and routing
│       │   ├── endpoints/
│       │   └── router.py
│       ├── core/             # Core configurations & logging setup
│       ├── models/           # Data models & Pydantic schemas
│       ├── config.py         # Environment variables & configuration management
│       └── main.py           # Application entrypoint
├── tests/                    # Automated test suites
│   ├── conftest.py
│   ├── test_health.py
│   └── test_items.py
├── .env.example              # Sample environment variables
├── .gitignore                # Standard git ignore rules
├── Dockerfile                # Multi-stage production Docker image definition
├── docker-compose.yml        # Multi-container orchestration
├── LICENSE                   # MIT License
├── Makefile                  # Helper commands for local dev
├── pyproject.toml            # Project dependencies & tool configs
└── requirements.txt          # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- **Python**: 3.11 or higher
- **Docker & Docker Compose**: (Optional, for containerized execution)
- **Make**: (Optional, for utility commands)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-starter.git
cd fastapi-starter
```

### 2. Environment Configuration

Copy the example environment file and configure variables:

```bash
cp .env.example .env
```

### 3. Local Setup with Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Running the Application

```bash
# Using uvicorn directly
uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000

# Or using Makefile
make run
```

Access interactive API documentation:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🐳 Running with Docker

```bash
# Build and run containers
docker-compose up --build

# Run in detached mode
docker-compose up -d
```

---

## 🧪 Testing & Code Quality

Run tests and coverage reports using pytest:

```bash
# Run pytest
pytest

# Run tests with coverage report
make test
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
