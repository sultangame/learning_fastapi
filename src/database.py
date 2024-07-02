from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.config import settings


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)


engine = create_async_engine(settings.DB_URL)
async_session_maker = async_sessionmaker(bind=engine)
