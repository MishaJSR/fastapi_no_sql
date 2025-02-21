import datetime
import string
import random

from fastapi import APIRouter, Depends, HTTPException

from database.methods.CountryMethods import get_games_by_country_id
from database.methods.GameMethods import select_all_games, add_game, get_games_by_stadium
from routers.country.schemas import CreateCountryID
from routers.game.schemas import ResponseAllGames, ResponsePostGame, CreateGame, ResponseSuccessAddThousandGame
from routers.stadium.schemas import CreateStadiumID
from routers.utils import generate_random_word

router = APIRouter(
    prefix="/game",
    tags=["Game"]
)


@router.get("/",
            response_model=list[ResponseAllGames],
            summary="Посмотреть список всех игр",
            description="Позволяет посмотреть список всех игр")
async def check_all_games(offset: int = 0, limit: int = 100) -> list[ResponseAllGames]:
    games = await select_all_games(offset=offset, limit=limit)
    return [ResponseAllGames(**game.to_dict()) for game in games]


@router.post("/add_game",
             response_model=ResponsePostGame,
             summary="Добавить игру",
             description="Позволяет добавить игру. Используются query параметры")
async def add_game_by_p(data: CreateGame = Depends(CreateGame.as_query)) -> ResponsePostGame:
    res = await add_game(game_data=data.model_dump())
    if res:
        return ResponsePostGame(id=res)
    else:
        raise HTTPException(status_code=400, detail="Ошибка добавления игры")


@router.get("/get_all_games_by_stadium",
            response_model=list[ResponseAllGames],
            summary="Посмотреть список всех игр по UUID стадиона",
            description="Посмотреть список всех игр по UUID стадиона. Используются query параметры")
async def get_all_games_by_stadium(data: CreateStadiumID = Depends(CreateStadiumID.as_query),
                                   offset: int = 0, limit: int = 100) -> list[ResponseAllGames]:
    games = await get_games_by_stadium(stadium_id=data.id, offset=offset, limit=limit)
    if games:
        return [ResponseAllGames(**game.to_dict()) for game in games]
    else:
        raise HTTPException(status_code=400, detail="Данные стадиона или игр не найдены")


@router.get("/get_games_by_county_id",
            response_model=list[ResponseAllGames],
            summary="Посмотреть список всех игр в стране",
            description="Посмотреть список всех игр в стране по UUID страны. Используются query параметры")
async def add_country_by_p(data: CreateCountryID = Depends(CreateCountryID.as_query),
                           offset: int = 0, limit: int = 100) -> list[ResponseAllGames]:
    games = await get_games_by_country_id(country_id=data.id, offset=offset, limit=limit)
    if games:
        return [ResponseAllGames(**game.to_dict()) for game in games]
    else:
        raise HTTPException(status_code=400, detail="Данный пользователь не найден")


@router.post("/add_many_games",
             response_model=ResponseSuccessAddThousandGame,
             summary="Добавляет в таблицу 10000 игр с рандомными командами",
             description="Позволяет создать 10000 игр с UUID переданного стадиона.\n"
                         " Испольуются query параметры")
async def add_a_by_p(data: CreateStadiumID = Depends(CreateStadiumID.as_query)) -> ResponseSuccessAddThousandGame:
    for el in range(10000):
        some_dict = {
            "m_date": datetime.datetime.now(),
            "team1": generate_random_word(3),
            "team2": generate_random_word(3),
            "stadium_id": data.id
        }
        _ = await add_game(game_data=some_dict)
        return ResponseSuccessAddThousandGame(status="Success add all games")
    else:
        raise HTTPException(status_code=400, detail="Ошибка добавления или UUID стадиона не найден")
