from enum import Enum

from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped

from user_service.database import Model, created_at, updated_at


class RoleSpaceType(str, Enum):
    PARTY = "party"
    ADVENTURE = "adventure"


class UserRoleOrm(Model):
    __tablename__ = "user_roles"

    user_id: Mapped[int]
    space_id: Mapped[int]
    space_type: Mapped[RoleSpaceType]
    role_id: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'space_id', 'space_type'),
        UniqueConstraint('user_id', 'space_id', 'space_type', name='id_user_space_role')
    )
