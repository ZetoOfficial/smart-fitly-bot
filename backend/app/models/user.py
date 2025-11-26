from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlalchemy import BigInteger, DateTime, String, func
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.checkin import Checkin
    from app.models.daily import Daily
    from app.models.goal import Goal
    from app.models.group import Group, GroupUser
    from app.models.measurement import Measurement


class UserRole(str, Enum):
    TRAINER = "Trainer"
    STUDENT = "Student"


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    telegram_id: Mapped[Optional[int]] = mapped_column(BigInteger, unique=True)
    username: Mapped[Optional[str]] = mapped_column(String(255))
    fullname: Mapped[Optional[str]] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole, name="user_role_enum"), nullable=False)
    tz: Mapped[str] = mapped_column(String(64), nullable=False, default="UTC")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    groups_owned: Mapped[list["Group"]] = relationship(
        "Group", back_populates="owner", cascade="all, delete-orphan"
    )
    group_memberships: Mapped[list["GroupUser"]] = relationship(
        "GroupUser", back_populates="user", cascade="all, delete-orphan"
    )
    daily_entries: Mapped[list["Daily"]] = relationship(
        "Daily", back_populates="user", cascade="all, delete-orphan"
    )
    goal: Mapped[Optional["Goal"]] = relationship(
        "Goal", back_populates="user", cascade="all, delete-orphan", uselist=False
    )
    measurements: Mapped[list["Measurement"]] = relationship(
        "Measurement", back_populates="user", cascade="all, delete-orphan"
    )
    checkins: Mapped[list["Checkin"]] = relationship(
        "Checkin", back_populates="user", cascade="all, delete-orphan"
    )
