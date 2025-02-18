import datetime
import uuid

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.dao import GameDao
from database.methods.GameMethods import select_all_games
from game.schema import ResponseAllGame, ConstructAddGame, ResponsePostGame, ConstructRemoveGame, ResponseRemoveGame

router = APIRouter(
    prefix="/game",
    tags=["Game"]
)

@router.get("/",
             #response_model=list[ResponseAllGame],
             summary="Посмотреть список всех игр",
             description="Позволяет посмотреть список всех игр")
async def check_all_games():
    result = await select_all_games()
    return result


# @router.post("/",
#              response_model=ResponsePostGame,
#              summary="Посмотреть список всех игр",
#              description="Позволяет посмотреть список всех игр")
# async def add_game(data: ConstructAddGame = Depends(ConstructAddGame.as_query),
#                    session: AsyncSession = Depends(get_async_session)):
#     res = await game_repository.add_object(session=session, data=data.model_dump())
#     if res:
#         return ResponsePostGame(**res)
#     else:
#         raise HTTPException(status_code=400, detail="Данный пользователь не найден")
#
#
# @router.delete("/add_url/{id_dalete}",
#              response_model=ResponseRemoveGame,
#              summary="Удалить матч по uuid4",
#              description="Этот эндпоинт позволяет добавить URL видео YouTube в систему. "
#                          "Необходимо предоставить ссылку на видео через query параметр 'url'.")
# async def remove_dame(id_delete: ConstructRemoveGame = Depends(ConstructRemoveGame.as_query),
#                       session: AsyncSession = Depends(get_async_session)):
#     res = await game_repository.delete_field(session=session, delete_filter=id_delete.model_dump())
#     if res:
#         return ResponseRemoveGame(**res)
#     else:
#         raise HTTPException(status_code=400, detail="Данный пользователь не найден")
#
