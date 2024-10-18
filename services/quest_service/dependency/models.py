from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import Mapped

from services.quest_service.database import Model, created_at, updated_at


class DependencyOrm(Model):
    __tablename__ = "dependency"

    parent_id: Mapped[int]
    child_id: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    __table_args__ = (
        PrimaryKeyConstraint('parent_id', 'child_id'),
    )
