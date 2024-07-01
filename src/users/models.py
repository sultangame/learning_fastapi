from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Boolean
from src.database import Base
if TYPE_CHECKING:
    from src.posts import Post


class User(Base):
    __tablename__ = 'users'
    username: Mapped[str] = mapped_column(String(length=356), unique=True)
    email: Mapped[str] = mapped_column(String(length=356), unique=True)
    first_name: Mapped[str] = mapped_column(String(length=256), nullable=True)
    last_name: Mapped[str] = mapped_column(String(length=256), nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(length=256))
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    posts: Mapped[List[Post]] = relationship(
        back_populates="owner", uselist=True
    )
