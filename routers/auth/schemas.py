from pydantic import BaseModel, EmailStr, Field, validator, field_validator
import re


class SUserRegister(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Имя, от 3 до 50 символов")
    login: str = Field(..., min_length=3, max_length=50, description="Логин, от 3 до 50 символов")
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")
