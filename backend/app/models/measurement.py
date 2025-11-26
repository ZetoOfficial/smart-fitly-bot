from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlalchemy import Date, DateTime, Float, ForeignKey, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.user import User


class Measurement(Base):
    __tablename__ = "measurements"
    __table_args__ = (UniqueConstraint("user_id", "month", name="uq_measurement_user_month"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    month: Mapped[date] = mapped_column(Date, nullable=False)

    weight: Mapped[Optional[float]] = mapped_column(Float)
    waist: Mapped[Optional[float]] = mapped_column(Float)
    hip: Mapped[Optional[float]] = mapped_column(Float)
    chest: Mapped[Optional[float]] = mapped_column(Float)
    arm: Mapped[Optional[float]] = mapped_column(Float)
    thigh: Mapped[Optional[float]] = mapped_column(Float)

    photos: Mapped[Optional[list[str]]] = mapped_column(JSONB)

    inbody_file_key: Mapped[Optional[str]] = mapped_column(Text)
    body_fat_pct: Mapped[Optional[float]] = mapped_column(Float)
    skeletal_muscle_mass: Mapped[Optional[float]] = mapped_column(Float)
    tbw_kg: Mapped[Optional[float]] = mapped_column(Float)
    bmr_kcal: Mapped[Optional[float]] = mapped_column(Float)
    visceral_fat_rating: Mapped[Optional[float]] = mapped_column(Float)

    note: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    user: Mapped["User"] = relationship("User", back_populates="measurements")
