from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from fastapi import Query
from pydantic import UUID4


class ResponseStadiumAdd(BaseModel):
    id: UUID4 = Field(
        strict=True,
        examples=["3422b448-2460-4fd2-9183-8000de6f8343"],
        description="UUID4 stadium in str",
    )

class ResponseSuccessAddThousandStadium(BaseModel):
    status: str = Field(
        strict=True,
        examples=["Success add all stadiums"],
        description="Adding status",
    )



class CreateStadium(BaseModel):
    name: str = Field(strict=True)
    build_date: Optional[datetime] = Field(default="2025-02-03T14:30:00")
    country_id: UUID4

    @classmethod
    def as_query(cls,
                 name: str = Query(...,
                                   example="Old Traford",
                                   description="Название стадиона"),
                 build_date: Optional[datetime] = Query(...,
                                                        example="2025-02-03T14:30:00",
                                                        description="Дата постройки стадиона"),
                 country_id: UUID4 = Query(...,
                                           example="0637e3b9-bea1-4aed-a8bc-8272235e946b",
                                           description="uuid4 стадиона"),
                 ):
        return cls(name=name, build_date=build_date, country_id=country_id)


class CreateStadiumID(BaseModel):
    id: UUID4 = Field(strict=False)

    @classmethod
    def as_query(cls,
                 id: UUID4 = Query(...,
                                   example="0637e3b9-bea1-4aed-a8bc-8272235e946b",
                                   description="uuid4 стадиона"),
                 ):
        return cls(id=id)


