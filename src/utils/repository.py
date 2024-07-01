from sqlalchemy import select, delete, update
from src.database import async_session_maker
from sqlalchemy.orm import joinedload
from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    async def find_all(self, order_by, join):
        raise NotImplementedError

    @abstractmethod
    async def find_by_pk(self, pk: int, join):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def create(data: dict):
        raise NotImplementedError

    @abstractmethod
    async def edit(self, pk: int, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete_one_by_id(self, pk: int):
        raise NotImplementedError


class AsyncRepository(Repository):
    model = None

    async def find_all(self, order_by, join) -> list:
        async with async_session_maker() as session:
            stmt = select(self.model).order_by(order_by).options(
                joinedload(join)
            )
            answer = await session.execute(stmt)
            result = answer.scalars().unique()
            return list(result)

    async def find_by_pk(self, pk: int, join):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id == pk).options(
                joinedload(join)
            )
            answer = await session.execute(stmt)
            result = answer.scalar()
            return result

    @staticmethod
    async def create(data: dict):
        async with async_session_maker() as session:
            session.add(data)
            await session.commit()
            await session.refresh(data)
            return data

    async def edit(self, pk: int, data: dict):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == pk).values(**data)
            await session.execute(stmt)
            await session.commit()

    async def delete_one_by_id(self, pk: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == pk)
            await session.execute(stmt)
            await session.commit()
