from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SUserGet(BaseModel):
    name: str
    role_id: int
    created_at: datetime
    updated_at: datetime
    

class SUserCreate(BaseModel):
    name: str
    role_id: int


class SUserSearch(BaseModel):
    role_id: Optional[int] = None


class SUserPut(BaseModel):
    role_id: int


class SUserPatch(BaseModel):
    role_id: Optional[int] = None


class SUserResult(BaseModel):
    ok: bool = True
