from database.dao.base import BaseDAO
from database.models.Country import Country
from database.models.Game import Game
from database.models.Stadium import Stadium
from database.models.User import User


class StadiumDao(BaseDAO):
    model = Stadium


class GameDao(BaseDAO):
    model = Game


class CountryDao(BaseDAO):
    model = Country


class UserDao(BaseDAO):
    model = User
