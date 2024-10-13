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

    class Config:
        from_attributes = True


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


class SDependencyGet(BaseModel):
    id: int
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


class SQuestResult(BaseModel):
    ok: bool = True


class SQuestCreateResult(BaseModel):
    ok: bool = True
    id: int
