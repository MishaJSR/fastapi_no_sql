from database.dao.base import BaseDAO
from database.models.Game import Game
from database.models.Stadium import Stadium


class StadiumDao(BaseDAO):
    model = Stadium


class GameDao(BaseDAO):
    model = Game