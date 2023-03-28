import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from api.app import app


@pytest.mark.anyio
async def test_post_post():
    async with LifespanManager(app) as manager:
        async with AsyncClient(app=manager.app, base_url="http://test") as client:
            response = await client.get("/")
            assert response.status_code == 200
            response_json = response.json()
            assert response_json["greeting"] == "Hello world!"
