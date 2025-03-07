from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped

from services.quest_service.database import Model, int_pk, created_at, updated_at


class QuestOrm(Model):
    __tablename__ = "quest"

    id: Mapped[int_pk]
    name: Mapped[str]
    description: Mapped[Optional[str]]
    category_id: Mapped[int]
    column_id: Mapped[int]
    board_id: Mapped[int]
    adventure_id: Mapped[int]
    party_id: Mapped[int]
    user_id: Mapped[Optional[int]]
    deadline: Mapped[Optional[datetime]]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
