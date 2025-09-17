# Dossier `app/`


Contient le **code applicatif**.
- `main.py`: point d'entrée FastAPI, routes, middlewares, CORS, docs.
- `api/`: routeurs versionnés et endpoints.
- `core/`: configuration, sécurité, logging.
- `db/`: session SQLAlchemy, base déclarative, init et migrations.
- `models/`: modèles ORM (SQLAlchemy).
- `schemas/`: schémas Pydantic pour I/O (validation).
- `repositories/`: couche d'accès aux données.
- `services/`: logique métier (use-cases).
- `auth/`: dépendances OAuth2/JWT.
- `dependencies/`: dépendances réutilisables FastAPI.
- `middlewares/`: middlewares custom.
- `tests/`: tests unitaires/integration.