from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class CategorySpaceType(str, Enum):
    PARTY = "party"
    ADVENTURE = "adventure"
    BOARD = "board"


class SCategoryGet(BaseModel):
    id: int
    name: str
    space_id: int
    space_type: CategorySpaceType
    created_at: datetime
    updated_at: datetime


class SCategoryCreate(BaseModel):
    name: str
    space_id: int
    space_type: CategorySpaceType


class SCategorySearch(BaseModel):
    name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[CategorySpaceType] = None


class SCategoryPut(BaseModel):
    name: str
    space_id: int
    space_type: CategorySpaceType


class SCategoryPatch(BaseModel):
    name: Optional[str] = None
    space_id: Optional[int] = None
    space_type: Optional[CategorySpaceType] = None


class SCategoryResult(BaseModel):
    ok: bool = True


class SCategoryCreateResult(BaseModel):
    ok: bool = True
    id: int
