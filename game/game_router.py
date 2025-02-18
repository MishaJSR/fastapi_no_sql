import datetime
import uuid

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.dao import GameDao
from database.methods.GameMethods import select_all_games, add_game, get_games_by_stadium
from database.methods.StadiumMethods import add_stadium
from game.schema import ResponseAllGames, ConstructAddGame, ResponsePostGame, ConstructRemoveGame, ResponseRemoveGame, \
    CreateStadium, CreateGame, CreateStadiumID

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


@router.post("/",
             response_model=ResponsePostGame,
             summary="Посмотреть список всех игр",
             description="Позволяет посмотреть список всех игр")
async def add_stadium_by_p(data: CreateStadium = Depends(CreateStadium)):
    res = await add_stadium(stadium_data=data.model_dump())
    if res:
        return ResponsePostGame(id=res)
    else:
        raise HTTPException(status_code=400, detail="Данный пользователь не найден")

@router.post("/game",
             response_model=ResponsePostGame,
             summary="Посмотреть список всех игр",
             description="Позволяет посмотреть список всех игр")
async def add_game_by_p(data: CreateGame = Depends(CreateGame)):
    res = await add_game(game_data=data.model_dump())
    if res:
        return ResponsePostGame(id=res)
    else:
        raise HTTPException(status_code=400, detail="Данный пользователь не найден")

@router.post("/std",
             response_model=list[ResponseAllGames],
             summary="Посмотреть список всех игр",
             description="Позволяет посмотреть список всех игр")
async def add_game_by_p(data: CreateStadiumID = Depends(CreateStadiumID)):
    games = await get_games_by_stadium(stadium_id=data.id)
    if games:
        return [ResponseAllGames(**game.to_dict()) for game in games]
    else:
        raise HTTPException(status_code=400, detail="Данный пользователь не найден")