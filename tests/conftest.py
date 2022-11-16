from typing import Generator

import pytest
from httpx import AsyncClient
from tortoise.contrib.test import initializer, finalizer, _restore_default

from app.app import app


@pytest.fixture()
def database() -> Generator:
    initializer(['app.database'])
    _restore_default()
    try:
        yield
    finally:
        finalizer()


@pytest.fixture()
async def client() -> Generator:
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client
