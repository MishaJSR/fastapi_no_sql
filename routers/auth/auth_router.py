from fastapi import APIRouter, HTTPException

from routers.auth.schemas import SUserRegister, ResponseUserRegistrate
from routers.auth.utils import get_password_hash
from database.methods.UserMethods import check_is_auth_user, registrate_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register/",
             response_model=ResponseUserRegistrate,
             summary="Регистрация нового пользователя",
             description=
             """Регистрация нового пользователя:\n
             name: Имя, от 3 до 50 символов
             login: Логин, от 3 до 50 символов
             email: Электронная почта
             password: Пароль, от 5 до 50 знаков
             """,
             )
async def register_user(user_data: SUserRegister) -> ResponseUserRegistrate:
    user_dict = user_data.model_dump()
    user = await check_is_auth_user(user_data=user_dict)
    if user:
        raise HTTPException(
            status_code=409,
            detail='Пользователь уже существует'
        )
    user_dict['password'] = get_password_hash(user_data.password)
    user_id = await registrate_user(user_data=user_dict)
    return ResponseUserRegistrate(id=user_id)