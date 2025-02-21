import uuid

from sqlalchemy import TIMESTAMP, String, DateTime, func, Integer, ForeignKey
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
        uselist=True,
        lazy="selectin"
    )
    country_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("countrys.id", ondelete="CASCADE"), nullable=False)
    country: Mapped["Country"] = relationship(
        "Country",
        back_populates="stadium",
        uselist=True
    )