from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class RoleSpaceType(str, Enum):
    GLOBAL = "global"
    PARTY = "party"
    ADVENTURE = "adventure"


class SRoleGet(BaseModel):
    id: int
    name: str
    space_id: Optional[int]
    space_type: RoleSpaceType
    created_at: datetime
    updated_at: datetime


class SRoleCreate(BaseModel):
    name: str
    space_id: Optional[int] = None
    space_type: RoleSpaceType


class SRoleSearch(BaseModel):
    name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[RoleSpaceType] = None


class SRolePut(BaseModel):
    name: str
    space_id: Optional[int] = None
    space_type: RoleSpaceType


class SRolePatch(BaseModel):
    name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[RoleSpaceType] = None


class SRoleResult(BaseModel):
    ok: bool = True


class SRoleCreateResult(BaseModel):
    ok: bool = True
    id: int
