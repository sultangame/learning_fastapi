from fastapi import HTTPException, status
from pydantic import BaseModel
from .repository import Repository


class Service:
    joins: list = None
    model = None

    def __init__(self, repository: Repository):
        self.repository: Repository = repository()

    async def returning_joins(self):
        for item in self.joins:
            return item

    async def find_all(self, order_by):
        join = await self.returning_joins()
        answer = await self.repository.find_all(order_by=order_by, join=join)
        return answer

    async def find_by_pk(self, pk: int):
        join = await self.returning_joins()
        answer = await self.repository.find_by_pk(pk=pk, join=join)
        if answer is not None:
            return answer
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with pk {pk} not found"
        )

    async def create(self, schema: BaseModel):
        data = self.model(**schema.model_dump())
        return await self.repository.create(data)

    async def edit(self, pk: int, schema: BaseModel):
        data: dict = schema.model_dump(exclude_unset=True)
        await self.repository.edit(pk=pk, data=data)
        answer = await self.find_by_pk(pk=pk)
        return answer

    async def delete(self, pk: int):
        one = await self.find_by_pk(pk=pk)
        if one:
            await self.repository.delete_one_by_id(pk=pk)
            return {"message": f"Item with pk {pk} deleted"}
        return one
