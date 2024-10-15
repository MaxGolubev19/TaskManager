from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from board_service.column.models import ColumnSpaceType


class SColumnGet(BaseModel):
    id: int
    space_id: int
    space_type: ColumnSpaceType
    order: int
    name: str
    created_at: datetime
    updated_at: datetime


class SColumnCreate(BaseModel):
    space_id: int
    space_type: ColumnSpaceType
    order: int
    name: str


class SColumnSearch(BaseModel):
    space_id: Optional[int] = None
    space_type: Optional[ColumnSpaceType] = None
    order: Optional[int] = None
    name: Optional[str] = None


class SColumnUpdate(BaseModel):
    id: int
    space_id: Optional[int] = None
    space_type: Optional[ColumnSpaceType] = None
    order: Optional[int] = None
    name: Optional[str] = None


class SColumnResult(BaseModel):
    ok: bool = True


class SColumnCreateResult(BaseModel):
    ok: bool = True
    id: int
