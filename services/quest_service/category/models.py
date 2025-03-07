from typing import Optional

from sqlalchemy.orm import Mapped

from services.common.schemas.quest_service.category_schemas import CategorySpaceType
from services.quest_service.database import Model, int_pk, created_at, updated_at


class CategoryOrm(Model):
    __tablename__ = "category"

    id: Mapped[int_pk]
    name: Mapped[str]
    space_id: Mapped[Optional[int]]
    space_type: Mapped[CategorySpaceType]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
