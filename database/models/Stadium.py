import uuid

from sqlalchemy import TIMESTAMP, String, DateTime, func, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, relationship

from database.database import Base


class Stadium(Base):
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    build_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    game: Mapped["Game"] = relationship(
        "Game",
        back_populates="stadium",
        uselist=True,  # Обеспечивает связь один-к-многим
        lazy="selectin"  # Автоматически загружает связанные данные из Bonds_calc при запросе Bond
    )