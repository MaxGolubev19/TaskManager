from sqlalchemy import PrimaryKeyConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from services.common.schemas.user_service.role_schemas import RoleSpaceType
from services.user_service.database import Model, created_at, updated_at


class UserRoleOrm(Model):
    __tablename__ = "user_roles"

    user_name: Mapped[str] = mapped_column(ForeignKey("users.name", ondelete="CASCADE"))
    space_id: Mapped[int]
    space_type: Mapped[RoleSpaceType]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    __table_args__ = (
        PrimaryKeyConstraint('user_name', 'space_id', 'space_type'),
    )
