from pydantic import BaseModel, EmailStr, Field, validator, field_validator, UUID4
import re


class SUserRegister(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Имя, от 3 до 50 символов")
    login: str = Field(..., min_length=3, max_length=50, description="Логин, от 3 до 50 символов")
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")

class ResponseUserRegistrate(BaseModel):
    id: UUID4 = Field(
        strict=True,
        examples=["3422b448-2460-4fd2-9183-8000de6f8343"],
        description="UUID4 registration in str",
    )