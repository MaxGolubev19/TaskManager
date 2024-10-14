from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SDependencyGet(BaseModel):
    parent_id: int
    child_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SDependencyCreate(BaseModel):
    parent_id: int
    child_id: int


class SDependencySearch(BaseModel):
    parent_id: Optional[int] = None
    child_id: Optional[int] = None


class SDependencyResult(BaseModel):
    ok: bool = True
