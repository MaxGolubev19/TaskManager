from sqlalchemy.orm import Mapped

from user_service.database import Model, int_pk, created_at, updated_at


class UserOrm(Model):
    __tablename__ = "users"

    id: Mapped[int_pk]
    name: Mapped[str]
    role_id: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
