from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from quest_service.category.models import CategorySpaceType


class SCategoryGet(BaseModel):
    id: int
    name: str
    space_id: int
    space_type: CategorySpaceType
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SCategoryCreate(BaseModel):
    name: str
    space_id: int
    space_type: CategorySpaceType


class SCategorySearch(BaseModel):
    name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[CategorySpaceType] = None


class SCategoryUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[CategorySpaceType] = None


class SCategoryResult(BaseModel):
    ok: bool = True


class SCategoryCreateResult(BaseModel):
    ok: bool = True
    id: int
