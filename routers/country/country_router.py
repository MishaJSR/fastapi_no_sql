import string
import random

from fastapi import APIRouter, Depends, HTTPException

from database.methods.CountryMethods import add_country
from routers.country.schemas import ResponsePostCountry, CreateCountry

router = APIRouter(
    prefix="/country",
    tags=["Country"]
)


@router.post("/county_add",
             response_model=ResponsePostCountry,
             summary="Добавить страну",
             description="Позволяет добавить страну. Используются query параметры")
async def add_country_by_p(data: CreateCountry = Depends(CreateCountry.as_query)) -> ResponsePostCountry:
    res = await add_country(country_data=data.model_dump())
    if res:
        return ResponsePostCountry(id=res)
    else:
        raise HTTPException(status_code=400, detail="Данный пользователь не найден")
