from database.dao.dao import GameDao
from database.database import connection


@connection
async def select_all_games(session):
    return await GameDao.get_all(session)
