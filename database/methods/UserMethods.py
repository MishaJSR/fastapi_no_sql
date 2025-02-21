import uuid

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.dao import UserDao
from database.database import connection


@connection
async def registrate_user(user_data: dict, session: AsyncSession) -> uuid.UUID:
    res = await UserDao.add(session, **user_data)
    return res.id


@connection
async def check_is_auth_user(user_data: dict, session: AsyncSession) -> bool:
    is_bysy = await check_bysy(email=user_data["email"], login=user_data["login"], session=session)
    return True if is_bysy else False


async def check_bysy(session: AsyncSession, email: str, login: str):
    query = select(UserDao.model).filter(or_(UserDao.model.email == email, UserDao.model.login == login))
    result = await session.execute(query)
    record = result.scalar_one_or_none()
    return record
