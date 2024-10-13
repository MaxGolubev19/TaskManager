from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from quest_service.column.models import ColumnSpaceType


class SColumnGet(BaseModel):
    id: int
    name: str
    space_id: int
    space_type: ColumnSpaceType
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SColumnCreate(BaseModel):
    name: str
    space_id: int
    space_type: ColumnSpaceType


class SColumnSearch(BaseModel):
    name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[ColumnSpaceType] = None


class SColumnUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[ColumnSpaceType] = None


class SColumnResult(BaseModel):
    ok: bool = True


class SColumnCreateResult(BaseModel):
    ok: bool = True
    id: int
