from multiprocessing.context import assert_spawning

import pytest
from httpx import AsyncClient, ASGITransport

@pytest.mark.asyncio
async def test_post_questions(app_with_overrides):
    async with AsyncClient(transport=ASGITransport(app=app_with_overrides), base_url='http://test') as ac:
        data = {
            "text": "Как задать вопрос?"
        }

        r = await ac.post('/questions/', json=data)

        assert r.status_code == 200
        print(r.json())

@pytest.mark.asyncio
async def test_get_question(app_with_overrides):
    async with AsyncClient(transport=ASGITransport(app=app_with_overrides), base_url='http://test') as ac:
        r = await ac.get("/questions/1")
        assert r.status_code == 200
        print(r.json())


@pytest.mark.asyncio
async def test_delete_question(app_with_overrides):
    async with AsyncClient(transport=ASGITransport(app=app_with_overrides), base_url='http://test') as ac:
        r = await ac.delete("/questions/1")
        assert r.status_code == 200
        print(r.json())

