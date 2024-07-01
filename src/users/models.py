from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from src.database import Base


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
