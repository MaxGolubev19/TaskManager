from enum import Enum as Enum
from typing import Optional

from sqlalchemy.orm import Mapped

from quest_service.database import Model, int_pk, created_at, updated_at


class CategorySpaceType(str, Enum):
    PARTY = "party"
    ADVENTURE = "adventure"
    BOARD = "board"


class CategoryOrm(Model):
    __tablename__ = "categories"

    id: Mapped[int_pk]
    name: Mapped[str]
    space_id: Mapped[Optional[int]]
    space_type: Mapped[CategorySpaceType]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
