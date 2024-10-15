from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from user_service.role.models import RoleSpaceType


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


class SRoleUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[RoleSpaceType] = None


class SRoleResult(BaseModel):
    ok: bool = True


class SRoleCreateResult(BaseModel):
    ok: bool = True
    id: int
