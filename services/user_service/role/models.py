from typing import Optional

from sqlalchemy.orm import Mapped

from services.common.schemas.user_service.role_schemas import RoleSpaceType
from services.user_service.database import Model, int_pk, created_at, updated_at


class RoleOrm(Model):
    __tablename__ = "role"

    id: Mapped[int_pk]
    name: Mapped[str]
    space_id: Mapped[Optional[int]]
    space_type: Mapped[RoleSpaceType]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
