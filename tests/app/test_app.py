import pytest
from httpx import AsyncClient

from app.app import app


class TestApp:

    @pytest.mark.asyncio
    async def test_ping(self):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/ping")
        assert response.status_code == 200
        assert response.json() == {'message': 'OK'}
