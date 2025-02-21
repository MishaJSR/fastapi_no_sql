import uuid

from sqlalchemy import TIMESTAMP, String, DateTime, func, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, relationship

from database.database import Base


class User(Base):
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    login: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False, default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False, default=func.now(), onupdate=func.now())
