from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from services.user_service.user_role.models import RoleSpaceType


class SUserRoleGet(BaseModel):
    user_name: str
    space_id: int
    space_type: RoleSpaceType
    role_id: int
    created_at: datetime
    updated_at: datetime


class SUserRoleCreate(BaseModel):
    user_name: str
    space_id: int
    space_type: RoleSpaceType
    role_id: int


class SUserRoleSearch(BaseModel):
    user_name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[RoleSpaceType] = None
    role_id: Optional[int] = None


class SUserRoleUpdate(BaseModel):
    user_name: str
    space_id: int
    space_type: RoleSpaceType
    role_id: Optional[int] = None


class SUserRoleResult(BaseModel):
    ok: bool = True
