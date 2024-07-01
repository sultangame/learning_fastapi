from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)


async_url: str = "sqlite+aiosqlite:///test.db"
engine = create_async_engine(async_url)
async_session_maker = async_sessionmaker(bind=engine)
