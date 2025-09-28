"""Initialisation applicative (seed)

- En dev, on peut s'assurer que le schéma existe.
- Création optionnelle d'un superutilisateur si variables .env fournies.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.security import hash_password
from app.db.base import Base
from app.db.session import engine
from app.repositories.user_repository import UserRepository


def ensure_schema_if_dev() -> None:
    """Crée les tables si nécessaire en ENV=dev (préférence Alembic en prod)."""
    if settings.ENV != "dev":
        return
    with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all)


def seed_superuser(session: AsyncSession) -> int | None:
    """Crée un superutilisateur si SUPERUSER_EMAIL/PASSWORD sont définis."""
    if not settings.SUPERUSER_EMAIL or not settings.SUPERUSER_PASSWORD:
        return None

    repo = UserRepository(session)
    existing = repo.get_by_email(settings.SUPERUSER_EMAIL)
    if existing:
        return existing.id  # type: ignore[return-value]

    user = repo.create(
        email=settings.SUPERUSER_EMAIL,
        hashed_password=hash_password(settings.SUPERUSER_PASSWORD),
        full_name="Administrator",
    )
    return user.id


def init_db(session: AsyncSession) -> None:
    ensure_schema_if_dev()
    seed_superuser(session)
    return None
