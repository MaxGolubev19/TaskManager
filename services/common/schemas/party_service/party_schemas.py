from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SPartyGet(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime


class SPartyCreate(BaseModel):
    name: str


class SPartySearch(BaseModel):
    name: Optional[str] = None


class SPartyPut(BaseModel):
    name: str


class SPartyPatch(BaseModel):
    name: Optional[str] = None


class SPartyResult(BaseModel):
    ok: bool = True


class SPartyCreateResult(BaseModel):
    ok: bool = True
    id: int
