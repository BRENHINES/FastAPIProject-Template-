.PHONY: install dev run lint fmt type test cov migrate revision up down check fix clean

install:
	\tpip install -e .[dev]
	\tpre-commit install                 # installe les hooks git

dev:
	\tuvicorn app.main:app --reload --port 8000

run:
	\tuvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 2

lint:
	\truff check . && flake8 .          # lint (ruff + flake8)

fmt:
	\tblack . && ruff format .          # formatage Black + format Ruff

type:
	\tmypy app                           # vérif. de types stricte

test:
	\tpytest                             # tests unitaires/intégration

cov:
	\tcoverage run -m pytest && coverage html && coverage report

migrate:
	\talembic upgrade head               # applique la dernière migration

revision:
	\talembic revision -m "auto" --autogenerate  # génère une migration

up:
	\tdocker compose up -d

down:
	\tdocker compose down -v

check: fmt lint type test            # pipeline qualité local

fix:
	\truff check . --fix && black .      # auto-fixage général

clean:
	\tfind . -name "*.pyc" -delete -o -name "__pycache__" -exec rm -rf {} +
