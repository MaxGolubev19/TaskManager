from enum import Enum
from typing import Optional

from sqlalchemy.orm import Mapped

from services.user_service.database import Model, int_pk, created_at, updated_at


class RoleSpaceType(str, Enum):
    GLOBAL = "global"
    PARTY = "party"
    ADVENTURE = "adventure"


class RoleOrm(Model):
    __tablename__ = "roles"

    id: Mapped[int_pk]
    name: Mapped[str]
    space_id: Mapped[Optional[int]]
    space_type: Mapped[RoleSpaceType]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
