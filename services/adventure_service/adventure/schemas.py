from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SAdventureGet(BaseModel):
    id: int
    name: str
    party_id: int
    created_at: datetime
    updated_at: datetime


class SAdventureCreate(BaseModel):
    name: str
    party_id: int


class SAdventureSearch(BaseModel):
    name: Optional[str] = None
    party_id: Optional[int] = None


class SAdventureUpdate(BaseModel):
    name: Optional[str] = None
    party_id: Optional[int] = None


class SAdventureResult(BaseModel):
    ok: bool = True


class SAdventureCreateResult(BaseModel):
    ok: bool = True
    id: int
