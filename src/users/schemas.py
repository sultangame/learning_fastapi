from pydantic import BaseModel, EmailStr
from typing import Optional


class PostsRelDTO(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None


class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_staff: Optional[bool] = None


class UserCreate(UserBase):
    hashed_password: Optional[str] = None


class UserRead(UserBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

