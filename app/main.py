from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.loggings import setup_logging

setup_logging()


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
)

app = FastAPI(
    title="TP",
    version="1.0.0",
    description=(
        "Producer API exposant des données nettoyées d'une bibliothèque"
        "et des statistiques enrichies stockées"
    ),
    openapi_tags=[
        {"name": "Health", "description": "Endpoints de santé"},
    ],
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
)


# CORS
origins = [o.strip() for o in settings.BACKEND_CORS_ORIGINS.split(",") if o]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*" if settings.ENV == "dev" else ""],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers versionnés
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


# Gestion d'erreurs (exemple simple)
@app.exception_handler(Exception)
async def unhandled_exc(_: FastAPI, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})


# Santé (root)
@app.get("/health", tags=["Health"])
async def health_root() -> dict[str, str]:
    return {"status": "ok"}
