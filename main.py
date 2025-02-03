from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

au = {"prefix": "/api/v1"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)