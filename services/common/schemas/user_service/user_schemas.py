from datetime import datetime
from typing import Optional

from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate
from pydantic import BaseModel, EmailStr


class SUserGet(BaseUser[int]):
    id: int

    name: str
    role_id: int
    email: EmailStr

    created_at: datetime
    updated_at: datetime
    

class SUserCreate(BaseUserCreate):
    name: str
    role_id: int
    email: EmailStr
    password: str


class SUserSearch(BaseModel):
    name: Optional[str] = None
    role_id: Optional[int] = None
    email: Optional[EmailStr] = None


class SUserPut(BaseModel):
    name: str
    role_id: int
    email: EmailStr


class SUserPatch(BaseUserUpdate):
    name: Optional[str] = None
    role_id: Optional[int] = None
    email: Optional[EmailStr] = None


class SUserCreateResult(BaseModel):
    ok: bool = True
    id: int


class SUserResult(BaseModel):
    ok: bool = True
