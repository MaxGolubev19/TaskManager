from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ColumnSpaceType(str, Enum):
    PARTY = "party"
    ADVENTURE = "adventure"
    BOARD = "board"


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


class SColumnPut(BaseModel):
    space_id: int
    space_type: ColumnSpaceType
    order: int
    name: str


class SColumnPatch(BaseModel):
    space_id: Optional[int] = None
    space_type: Optional[ColumnSpaceType] = None
    order: Optional[int] = None
    name: Optional[str] = None


class SColumnResult(BaseModel):
    ok: bool = True


class SColumnCreateResult(BaseModel):
    ok: bool = True
    id: int
