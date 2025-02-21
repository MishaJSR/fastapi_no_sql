import datetime
import string
import random

from fastapi import APIRouter, Depends, HTTPException

from database.methods.StadiumMethods import add_stadium
from routers.stadium.schemas import CreateStadium, ResponseStadiumAdd, ResponseSuccessAddThousandStadium
from routers.country.schemas import CreateCountryID

router = APIRouter(
    prefix="/stadium",
    tags=["Stadium"]
)


def generate_random_word(length=10):
    letters = string.ascii_letters  # Все буквы (заглавные и строчные)
    random_word = ''.join(random.choice(letters) for _ in range(length))
    return random_word


@router.post("/add_stadium",
             response_model=ResponseStadiumAdd,
             summary="Добавить стадион",
             description="Позволяет добавить стадион. Используются query параметры")
async def add_stadium_by_p(data: CreateStadium = Depends(CreateStadium.as_query)) -> ResponseStadiumAdd:
    res = await add_stadium(stadium_data=data.model_dump())
    if res:
        return ResponseStadiumAdd(id=res)
    else:
        raise HTTPException(status_code=400, detail="Ошибка добавления стадиона")


@router.post("/add_many_stad",
             response_model=ResponseSuccessAddThousandStadium,
             summary="Добавляет в таблицу 1000 стадионов с рандомными названиями",
             description="Позволяет создать 1000 стадионов с UUID переданной страны.\n"
                         " Испольуются query параметры")
async def add_a_by_p(data: CreateCountryID = Depends(CreateCountryID.as_query)) -> ResponseSuccessAddThousandStadium:
    for el in range(1000):
        some_dict = {
            "name": generate_random_word(),
            "build_date": datetime.datetime.now(),
            "country_id": data.id
        }
        _ = await add_stadium(stadium_data=some_dict)
        return ResponseSuccessAddThousandStadium(status="Success add all stadiums")
    else:
        raise HTTPException(status_code=400, detail="Ошибка добавления или UUID страны не найден")
