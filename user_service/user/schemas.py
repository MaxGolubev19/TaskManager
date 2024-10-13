from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SUserGet(BaseModel):
    id: int
    name: str
    role_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
    

class SUserCreate(BaseModel):
    name: str
    role_id: int


class SUserSearch(BaseModel):
    name: Optional[str] = None
    role_id: Optional[int] = None


class SUserUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    role_id: Optional[int] = None


class SUserResult(BaseModel):
    ok: bool = True


class SUserCreateResult(BaseModel):
    ok: bool = True
    id: int
