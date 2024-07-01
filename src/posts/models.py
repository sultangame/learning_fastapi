from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from typing import TYPE_CHECKING
from src.database import Base
if TYPE_CHECKING:
    from src.users import User


class Post(Base):
    __tablename__ = 'posts'
    title: Mapped[str] = mapped_column(String(length=356))
    description: Mapped[str] = mapped_column(Text())
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
    )
    owner: Mapped[User] = relationship(
        back_populates="posts", uselist=True, cascade="all, delete, delete-orphan"
    )
