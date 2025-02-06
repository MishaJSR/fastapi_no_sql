import datetime
import uuid
from http.client import HTTPException

from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_async_session
from database.models import game_repository
from game.schema import ResponseAllGame, ConstructAddGame, ResponsePostGame, ConstructRemoveGame

router = APIRouter(
    prefix="/game",
    tags=["Game"]
)

@router.get("/",
             response_model=list[ResponseAllGame],
             summary="Посмотреть список всех игр",
             description="Позволяет посмотреть список всех игр")
async def check_all_games(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(text('SELECT * FROM game'))
    games = result.scalars()
    print(games)
    return []


@router.post("/",
             response_model=ResponsePostGame,
             summary="Посмотреть список всех игр",
             description="Позволяет посмотреть список всех игр")
async def add_game(data: ConstructAddGame = Depends(ConstructAddGame.as_query),
                   session: AsyncSession = Depends(get_async_session)):
    res = await game_repository.add_object(session=session, data=data.model_dump())
    if res:
        return ResponsePostGame(**res)
    else:
        raise HTTPException(status_code=400, detail="Данный пользователь не найден")


@router.delete("/add_url/{id_dalete}",
             # response_model=ResponseAddUrl,
             summary="Удалить матч по uuid4",
             description="Этот эндпоинт позволяет добавить URL видео YouTube в систему. "
                         "Необходимо предоставить ссылку на видео через query параметр 'url'.")
async def remove_dame(id_delete: ConstructRemoveGame = Depends(ConstructRemoveGame.as_query),
                      session: AsyncSession = Depends(get_async_session),):
    return id_delete
