import time
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.dao import GameDao, CountryDao
from database.database import connection
from database.models.Country import Country
from database.models.Game import Game
from database.models.Stadium import Stadium


@connection
async def add_country(country_data: dict, session):
    res = await CountryDao.add(session, **country_data)
    return res.id


@connection
async def get_games_by_country_id(country_id: uuid.UUID, offset: int, limit: int,session: AsyncSession):
    st_time = time.time()
    stmt = (
        select(Game)
        .join(Game.stadium)
        .join(Stadium.country)
        .where(Country.id == country_id).offset(offset).limit(limit)
    )
    result = await session.execute(stmt)
    end_time = time.time() - st_time
    print(end_time)
    records = result.scalars().all()
    return records