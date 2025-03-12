from pydantic_settings import BaseSettings
from sqlalchemy import URL


class Settings(BaseSettings):
    DB_DRIVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DB_HOST: str
    DB_PORT: int

    def get_sql_url(self):
        url = URL.create(
            drivername=self.DB_DRIVER,
            host=self.DB_HOST,
            password=self.POSTGRES_PASSWORD,
            username=self.POSTGRES_USER,
            database=self.POSTGRES_DB,
            port=self.DB_PORT,
        ).render_as_string(hide_password=False)
        return url



settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
