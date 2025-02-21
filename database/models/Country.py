import uuid

from sqlalchemy import TIMESTAMP, String, DateTime, func, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, relationship

from database.database import Base


class Country(Base):
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    stadium: Mapped["Stadium"] = relationship(
        "Stadium",
        back_populates="country",
        uselist=True,
        lazy="selectin"
    )