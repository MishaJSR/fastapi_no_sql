from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from fastapi import Query
from pydantic import UUID4


class ConstructAddGame(BaseModel):
    m_date: datetime = Field(strict=True)
    stadium: str = Field(strict=True)
    team1: str = Field(strict=True)
    team2: str = Field(strict=True)

    @classmethod
    def as_query(cls,
                 m_date: datetime = Query(...,
                                          example="2025-02-03T14:30:00",
                                          description="Match date"),
                 stadium: str = Query(...,
                                      example="National Stadium, Warsaw",
                                      description="Stadium name", ),
                 team1: str = Query(...,
                                    example="POL",
                                    description="Team one name", ),

                 team2: str = Query(...,
                                    example="RUS",
                                    description="Team two name", ),
                 ):
        return cls(m_date=m_date, stadium=stadium, team1=team1, team2=team2)


class ResponseAllGames(BaseModel):
    id: UUID4 = Field(
        strict=True,
        examples=["3422b448-2460-4fd2-9183-8000de6f8343"],
        description="Match id",
    )
    m_date: datetime = Field(
        strict=True,
        examples=["2025-02-03T14:30:00"],
        description="Match data",
    )
    stadium_id: UUID4 = Field(
        strict=True,
        examples=["National Stadium, Warsaw"],
        description="Stadium name",
    )
    team1: str = Field(
        strict=True,
        examples=["POL"],
        description="Team one name",
    )
    team2: str = Field(
        strict=True,
        examples=["RUS"],
        description="Team two name",
    )


class ResponsePostGame(BaseModel):
    id: UUID4 = Field(
        strict=True,
        examples=["3422b448-2460-4fd2-9183-8000de6f8343"],
        description="UUID4 game in str",
    )

class ResponseSuccessAddThousandGame(BaseModel):
    status: str = Field(
        strict=True,
        examples=["3422b448-2460-4fd2-9183-8000de6f8343"],
        description="Success add all games",
    )


class CreateGame(BaseModel):
    m_date: Optional[datetime] = Field(default="2025-02-03T14:30:00")
    team1: str = Field(strict=True, min_length=3, max_length=5)
    team2: str = Field(strict=True, min_length=3, max_length=5)
    stadium_id: UUID4

    @classmethod
    def as_query(cls,
                 m_date: Optional[datetime] = Query(...,
                                                    example="2025-02-03T14:30:00",
                                                    description="Дата и время начала игры"),
                 team1: str = Query(...,
                                    example="Rus",
                                    description="Краткое название 1 команды (от 3 до 5 символов)"),
                 team2: str = Query(...,
                                    example="Port",
                                    description="Краткое название 2 команды (от 3 до 5 символов)"),
                 stadium_id: UUID4 = Query(...,
                                           example="0637e3b9-bea1-4aed-a8bc-8272235e946b",
                                           description="uuid4 игры"),
                 ):
        return cls(m_date=m_date, team1=team1, team2=team2, stadium_id=stadium_id)
