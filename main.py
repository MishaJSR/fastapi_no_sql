import logging

from fastapi import FastAPI, APIRouter
import uvicorn
from contextlib import asynccontextmanager
import betterlogging as bl

from game.game_router import router as game_router

main_router = APIRouter(prefix="/api/v1")


def setup_logging():
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)
    logging.basicConfig(
        level=log_level,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting server")


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield
    logging.info("Stop server")


app = FastAPI(lifespan=lifespan)

main_router.include_router(game_router)
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)
