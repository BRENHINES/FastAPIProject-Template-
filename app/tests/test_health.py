import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.anyio
async def test_health_root() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"
