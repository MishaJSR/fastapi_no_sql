import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.dao import StadiumDao
from database.database import connection
from database.models.Game import Game


@connection
async def add_stadium(stadium_data: dict, session: AsyncSession):
    new_stadium = await StadiumDao.add(session=session, **stadium_data)
    return new_stadium.id

