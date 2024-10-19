from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class RoleSpaceType(str, Enum):
    PARTY = "party"
    ADVENTURE = "adventure"


class SUserRoleGet(BaseModel):
    user_id: int
    space_id: int
    space_type: RoleSpaceType
    role_id: int
    created_at: datetime
    updated_at: datetime


class SUserRoleCreate(BaseModel):
    user_id: int
    space_id: int
    space_type: RoleSpaceType
    role_id: int


class SUserRoleSearch(BaseModel):
    user_id: Optional[int] = None
    space_id: Optional[int] = None
    space_type: Optional[RoleSpaceType] = None
    role_id: Optional[int] = None


class SUserRolePut(BaseModel):
    user_id: int
    space_id: int
    space_type: RoleSpaceType
    role_id: int


class SUserRolePatch(BaseModel):
    user_name: str
    space_id: int
    space_type: RoleSpaceType
    role_id: Optional[int] = None


class SUserRoleResult(BaseModel):
    ok: bool = True
