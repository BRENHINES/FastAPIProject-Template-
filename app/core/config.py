from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    APP_NAME: str = "FastAPI Template"
    APP_VERSION: str = "1.0.0"
    ENV: str = "dev"  # dev|staging|prod
    DEBUG: bool = True

    # API
    API_V1_PREFIX: str = "/api/v1"

    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    # CORS (CSV dans .env)
    BACKEND_CORS_ORIGINS: str = ""

    # DB
    DATABASE_URL: str  # async: postgresql+asyncpg://...
    SYNC_DATABASE_URL: str  # sync: pour Alembic

    # Optionnel: seed superuser
    SUPERUSER_EMAIL: str | None = None
    SUPERUSER_PASSWORD: str | None = None

    # Observabilité
    LOG_LEVEL: str = "INFO"
    SENTRY_DSN: str | None = None

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    @field_validator("ENV")
    @classmethod
    def _normalize_env(cls, v: str) -> str:
        return v.lower()

    @property
    def cors_origins(self) -> list[str]:
        if not self.BACKEND_CORS_ORIGINS:
            return []
        return [o.strip() for o in self.BACKEND_CORS_ORIGINS.split(",") if o.strip()]


settings = Settings()
