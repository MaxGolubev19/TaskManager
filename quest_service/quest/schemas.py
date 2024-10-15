from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SQuestGet(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    category_id: int
    column_id: int
    board_id: int
    adventure_id: int
    party_id: int
    user_id: Optional[int] = None
    deadline: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime


class SQuestCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category_id: int
    column_id: int
    board_id: int
    adventure_id: int
    party_id: int
    user_id: Optional[int] = None
    deadline: Optional[datetime] = None


class SQuestSearch(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    column_id: Optional[int] = None
    board_id: Optional[int] = None
    adventure_id: Optional[int] = None
    party_id: Optional[int] = None
    user_id: Optional[int] = None
    deadline: Optional[datetime] = None


class SQuestUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    category_id: Optional[int] = None
    column_id: Optional[int] = None
    board_id: Optional[int] = None
    adventure_id: Optional[int] = None
    party_id: Optional[int] = None
    user_id: Optional[int] = None
    deadline: Optional[datetime] = None


class SQuestResult(BaseModel):
    ok: bool = True


class SQuestCreateResult(BaseModel):
    ok: bool = True
    id: int
