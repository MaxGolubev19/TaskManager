from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SBoardGet(BaseModel):
    id: int
    name: str
    adventure_id: int
    party_id: int
    created_at: datetime
    updated_at: datetime


class SBoardCreate(BaseModel):
    name: str
    adventure_id: int
    party_id: int


class SBoardSearch(BaseModel):
    name: Optional[str] = None
    adventure_id: Optional[int] = None
    party_id: Optional[int] = None


class SBoardUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    adventure_id: Optional[int] = None
    party_id: Optional[int] = None


class SBoardResult(BaseModel):
    ok: bool = True


class SBoardCreateResult(BaseModel):
    ok: bool = True
    id: int
