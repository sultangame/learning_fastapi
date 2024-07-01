from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from src.database import Base


class Post(Base):
    __tablename__ = 'posts'
    title: Mapped[str] = mapped_column(String(length=356))
    description: Mapped[str] = mapped_column(Text())
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), ondelete='CASCADE', onupdate='CASCADE'
    )
    owner: Mapped[str] = relationship(
        back_populates="posts", uselist=True, cascade="all, delete, delete-orphan"
    )
