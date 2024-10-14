from enum import Enum as Enum
from typing import Optional

from sqlalchemy.orm import Mapped

from board_service.database import Model, int_pk, created_at, updated_at


class ColumnSpaceType(str, Enum):
    PARTY = "party"
    ADVENTURE = "adventure"
    BOARD = "board"


class ColumnOrm(Model):
    __tablename__ = "columns"

    id: Mapped[int_pk]
    space_id: Mapped[Optional[int]]
    space_type: Mapped[ColumnSpaceType]
    order: Mapped[int]
    name: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
