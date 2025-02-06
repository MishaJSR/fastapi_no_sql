from datetime import datetime

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
                                    description="Team two name",),
                 ):
        return cls(m_date=m_date, stadium=stadium, team1=team1, team2=team2)


class ConstructRemoveGame(BaseModel):
    match_uuid4: UUID4 = Field(strict=True)

    @classmethod
    def as_query(cls,
                 match_uuid4: UUID4 = Query(...,
                                     example="0637e3b9-bea1-4aed-a8bc-8272235e946b",
                                     description="Match uuid4"),
                 ):
        return cls(match_uuid4=match_uuid4)


class ResponseAllGame(BaseModel):
    id: UUID4 = Field(
        strict=True,
        examples=["3422b448-2460-4fd2-9183-8000de6f8343"],
        description="Match id",
    )
    m_date: str = Field(
        strict=True,
        examples=[""],
        description="Match date",
    )
    stadium: str = Field(
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
