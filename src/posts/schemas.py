from pydantic import BaseModel
from typing import Optional


class UserRelDTO(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class PostCreate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[int] = None


class PostRead(PostCreate):
    id: Optional[int] = None
    owner: Optional[UserRelDTO] = None

    class Config:
        from_attributes = True


class PostUpdate(PostCreate):
    pass
