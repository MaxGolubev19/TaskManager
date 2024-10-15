from sqlalchemy.orm import Mapped, mapped_column

from user_service.database import Model, created_at, updated_at, str_pk


class UserOrm(Model):
    __tablename__ = "users"

    name: Mapped[str_pk]
    role_id: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
