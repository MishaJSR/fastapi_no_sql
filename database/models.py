import uuid

from sqlalchemy import TIMESTAMP, String, DateTime, func, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase

from database.repo.repository import SQLAlchemyRepository


class Base(DeclarativeBase):
    ...
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

class Game(Base):
    __tablename__ = 'game'
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    m_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)
    stadium: Mapped[str] = mapped_column(String(50), nullable=False)
    team1: Mapped[str] = mapped_column(String(5), nullable=False)
    team2: Mapped[str] = mapped_column(String(5), nullable=False)

class GameRepository(SQLAlchemyRepository):
    model = Game


game_repository = GameRepository()