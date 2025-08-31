from db.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr
from datetime import datetime
from sqlalchemy import func, Integer


engine = create_async_engine(url=settings.DATABASE_URL_asyncpg)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=True)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(server_default=func.now())

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"



async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session




