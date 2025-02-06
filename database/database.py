from typing import AsyncGenerator

from sqlalchemy import MetaData, NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from base_setting import base_settings

metadata = MetaData()

DATABASE_URL = base_settings.get_sql_url()

engine = create_async_engine(DATABASE_URL, echo=False, poolclass=NullPool)
async_session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
