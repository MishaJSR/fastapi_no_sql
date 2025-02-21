from pydantic import BaseModel, Field
from fastapi import Query
from pydantic import UUID4


class ResponsePostCountry(BaseModel):
    id: UUID4 = Field(
        strict=True,
        examples=["3422b448-2460-4fd2-9183-8000de6f8343"],
        description="UUID4 country in str",
    )


class CreateCountry(BaseModel):
    name: str = Field(strict=True, max_length=50)

    @classmethod
    def as_query(cls,
                 name: str = Query(...,
                                   example="Russia",
                                   description="Название страны (до 50 символов)"),
                 ):
        return cls(name=name)


class CreateCountryID(BaseModel):
    id: UUID4 = Field(strict=False)

    @classmethod
    def as_query(cls,
                 id: UUID4 = Query(...,
                                   example="0637e3b9-bea1-4aed-a8bc-8272235e946b",
                                   description="uuid4 страны"),
                 ):
        return cls(id=id)
