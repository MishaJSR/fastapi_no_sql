import uuid

from sqlalchemy import TIMESTAMP, String, DateTime, func, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, relationship

from database.database import Base
from database.models.Stadium import Stadium


class Game(Base):
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    m_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)
    team1: Mapped[str] = mapped_column(String(5), nullable=False)
    team2: Mapped[str] = mapped_column(String(5), nullable=False)
    stadium_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("stadiums.id", ondelete="CASCADE"), nullable=False)
    stadium: Mapped["Stadium"] = relationship(
        "Stadium",
        back_populates="game",
        uselist=False
    )