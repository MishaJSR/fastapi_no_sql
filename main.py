import logging

from fastapi import FastAPI, APIRouter
import uvicorn
from contextlib import asynccontextmanager
import betterlogging as bl

from routers.game.game_router import router as game_router
from routers.auth.auth_router import router as auth_router
from routers.stadium.stadium_router import router as stadium_router
from routers.country.country_router import router as country_router
from routers.elast.elastic import router as elastic_router




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
main_router = APIRouter(prefix="/api/v1")
routers = [game_router, auth_router, country_router, stadium_router, elastic_router]
for router in routers:
    main_router.include_router(router)
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)
