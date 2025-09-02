
import subprocess

import pytest_asyncio
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from alembic import command
from alembic.config import Config
from api.answer.views import api_router as answer_router
from api.questions.views import api_router as question_router
from db.database import get_async_session
import asyncio
from dotenv import load_dotenv
import os
from db.database import Base
load_dotenv()

TEST_DB_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_TEST_NAME')}"



@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="session")
async def engine():
    eng = create_async_engine(TEST_DB_URL, echo=False, future=True)
    try:
        yield eng
    finally:
        await eng.dispose()



@pytest_asyncio.fixture(scope="session", autouse=True)
async def _db_schema(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture(scope="session")
def session_factory(engine):
    return async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)



@pytest_asyncio.fixture
async def app_with_overrides(session_factory):
    app = FastAPI()

    app.include_router(
        router=answer_router
    )

    app.include_router(
        router=question_router
    )

    async def override_get_async_session():

        async with session_factory() as session:
            yield session

    app.dependency_overrides[get_async_session] = override_get_async_session

    yield app
