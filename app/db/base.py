from __future__ import annotations
from typing import Any

from sqlalchemy import MetaData, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Convention de nommage pour Alembic (contraintes stables)
naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=naming_convention)

class TimestampMixin:
    created_at: Mapped[Any] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[Any] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

class ReprMixin:
    def __repr__(self) -> str:  # pragma: no cover
        attrs = [f"{k}={getattr(self, k)!r}" for k in self.__mapper__.c.keys()]  # type: ignore[attr-defined]
        return f"<{self.__class__.__name__} {' '.join(attrs)}>"
