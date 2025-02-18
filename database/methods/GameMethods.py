import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.dao import GameDao
from database.database import connection
from database.models.Game import Game


@connection
async def select_all_games(session):
    return await GameDao.get_all(session)

@connection
async def add_game(game_data: dict, session):
    res = await GameDao.add(session, **game_data)
    return res.id


@connection
async def get_games_by_stadium(stadium_id: uuid.UUID, session: AsyncSession):
    query = select(Game).where(Game.stadium_id == stadium_id)
    result = await session.execute(query)
    records = result.scalars().all()
    return records