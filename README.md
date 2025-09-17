# FastAPI Template Pro

Un **boilerplate FastAPI** orienté production : structure claire, sécurité, migrations DB, qualité de code et DX rapide.

## Sommaire
- [Caractéristiques](#caractéristiques)
- [Prérequis](#prérequis)
- [Démarrage rapide](#démarrage-rapide)
- [Configuration (.env)](#configuration-env)
- [Architecture & conventions](#architecture--conventions)
- [Qualité & CI locale](#qualité--ci-locale)
- [Base de données & migrations](#base-de-données--migrations)
- [Sécurité](#sécurité)
- [Observabilité](#observabilité)
- [Scripts utiles](#scripts-utiles)

## Caractéristiques
- FastAPI 0.116, SQLAlchemy 2.x (async), Alembic migrations
- Auth JWT (HMAC), hash bcrypt, CORS
- Logs structurés JSON, middleware de latence
- Tests Pytest, typage Mypy, lint Ruff/Flake8, formatage Black
- Dockerfile + docker-compose (PostgreSQL)

## Prérequis
- Python 3.11+
- Docker / Docker Compose

## Démarrage rapide
```bash
python -m venv .venv && source .venv/bin/activate
make install
cp .env.example .env

docker compose up -d db
make migrate
make dev  # http://localhost:8000/docs
